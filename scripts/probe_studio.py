#!/usr/bin/env python3
"""Bounded read-only MCP capability probe. Never edits a place or proves gameplay."""
import argparse
import json
import os
from pathlib import Path
import queue
import subprocess
import sys
import threading
import time

CAPABILITIES = {
    'target_listing': {'list_roblox_studios'},
    'inspection': {'search_game_tree', 'inspect_instance'},
    'editing': {'execute_luau', 'multi_edit'},
    'play_control': {'start_stop_play'},
    'runtime_output': {'get_console_output'},
    'viewport': {'screen_capture'},
    'player_input': {'user_keyboard_input', 'user_mouse_input', 'character_navigation'},
}


class ProbeError(Exception):
    pass


class JsonLineClient:
    def __init__(self, command, timeout):
        self.process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                        stderr=subprocess.DEVNULL, text=True, bufsize=1)
        self.messages = queue.Queue()
        self.deadline = time.monotonic() + timeout
        self.next_id = 0
        threading.Thread(target=self._read, daemon=True).start()

    def _read(self):
        try:
            for line in self.process.stdout:
                try:
                    message = json.loads(line)
                except ValueError:
                    continue
                if isinstance(message, dict):
                    self.messages.put(message)
        finally:
            self.messages.put(None)

    def send(self, message):
        try:
            self.process.stdin.write(json.dumps(message) + '\n')
            self.process.stdin.flush()
        except (BrokenPipeError, OSError):
            raise ProbeError('server_closed_input') from None

    def request(self, method, params):
        self.next_id += 1
        ident = self.next_id
        self.send({'jsonrpc': '2.0', 'id': ident, 'method': method, 'params': params})
        while True:
            remaining = self.deadline - time.monotonic()
            if remaining <= 0:
                raise ProbeError('response_timeout')
            try:
                message = self.messages.get(timeout=remaining)
            except queue.Empty:
                raise ProbeError('response_timeout') from None
            if message is None:
                raise ProbeError('server_closed_output')
            if message.get('id') != ident:
                continue  # Notifications are not replies to the requested method.
            if 'error' in message:
                raise ProbeError('rpc_error:' + method)
            if not isinstance(message.get('result'), dict):
                raise ProbeError('invalid_result:' + method)
            return message['result']

    def close(self):
        if self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=3)
        self.process.stdin.close()
        self.process.stdout.close()


def default_command():
    if sys.platform == 'darwin':
        return ['/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP']
    if os.name == 'nt':
        base = os.environ.get('LOCALAPPDATA')
        if base:
            return ['cmd.exe', '/c', str(Path(base) / 'Roblox' / 'mcp.bat')]
    raise ProbeError('set_server_path_for_this_platform')


def probe(command=None, timeout=15, retries=0):
    if not 0 < timeout <= 45 or not 0 <= retries <= 3:
        raise ValueError('timeout must be 0–45 seconds; retries must be 0–3')
    report = {'status': 'connection_failed', 'initialized': False, 'tool_count': 0,
              'capabilities': {}, 'tools': [], 'place_identity_verified': False,
              'gameplay_verified': False,
              'scope': 'Read-only initialize and tools/list; no model turn or place action.'}
    client = None
    try:
        client = JsonLineClient(command or default_command(), timeout)
        result = client.request('initialize', {'protocolVersion': '2024-11-05',
                                'capabilities': {},
                                'clientInfo': {'name': 'roblox-game-forge-probe', 'version': '0.1.1'}})
        report['initialized'] = True
        report['protocol_version'] = result.get('protocolVersion')
        report['server'] = {k: result.get('serverInfo', {}).get(k) for k in ('name', 'version')}
        client.send({'jsonrpc': '2.0', 'method': 'notifications/initialized'})
        tools = []
        for attempt in range(retries + 1):
            page = client.request('tools/list', {})
            entries = page.get('tools')
            if not isinstance(entries, list) or any(not isinstance(t, dict) or not isinstance(t.get('name'), str) for t in entries):
                raise ProbeError('invalid_tools_list')
            tools.extend(entries)
            cursor = page.get('nextCursor')
            seen = set()
            while cursor:
                if not isinstance(cursor, str) or cursor in seen:
                    raise ProbeError('invalid_tool_pagination')
                seen.add(cursor)
                page = client.request('tools/list', {'cursor': cursor})
                entries = page.get('tools')
                if not isinstance(entries, list) or any(not isinstance(t, dict) or not isinstance(t.get('name'), str) for t in entries):
                    raise ProbeError('invalid_tools_list')
                tools.extend(entries)
                cursor = page.get('nextCursor')
            if tools or attempt == retries:
                break
            time.sleep(min(.25, max(0, client.deadline - time.monotonic())))
        names = set(t['name'] for t in tools)
        report['tools'] = sorted(names)
        report['tool_count'] = len(names)
        report['capabilities'] = {k: bool(names & alternatives) for k, alternatives in CAPABILITIES.items()}
        report['missing_capabilities'] = [k for k, value in report['capabilities'].items() if not value]
        report['status'] = ('initialized_no_tools' if not names else
                            'tools_exposed_incomplete' if report['missing_capabilities'] else 'tools_exposed')
    except (ProbeError, OSError) as error:
        # Avoid echoing server diagnostics/configuration, place names, or credentials.
        report['error'] = str(error) if isinstance(error, ProbeError) else type(error).__name__
    finally:
        if client is not None:
            client.close()
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--server', help='Override the Studio-provided stdio executable path')
    parser.add_argument('--timeout', type=float, default=15)
    parser.add_argument('--retries', type=int, default=0,
                        help='Extra bounded listings; Studio may wait about 10 seconds per listing')
    args = parser.parse_args()
    report = probe([args.server] if args.server else None, args.timeout, args.retries)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report['status'] == 'tools_exposed' else 2


if __name__ == '__main__':
    raise SystemExit(main())

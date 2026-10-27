"""Synthetic stdio protocol tests. These never launch Roblox Studio."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('probe_studio', Path(__file__).resolve().parents[1] / 'scripts/probe_studio.py')
probe_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe_module)

FAKE = '''import json,sys,time
mode=sys.argv[1]
listings=0
for line in sys.stdin:
 m=json.loads(line)
 if 'id' not in m:continue
 method=m['method']
 if mode=='closed':break
 if mode=='timeout':time.sleep(3);break
 if mode=='rpc_error':r={'jsonrpc':'2.0','id':m['id'],'error':{'code':-1,'message':'synthetic'}}
 else:
  if method=='initialize':v={'protocolVersion':'2024-11-05','serverInfo':{'name':'Synthetic','version':'0'}}
  else:
   listings+=1
   names=[] if mode=='empty' else ['execute_luau'] if mode=='partial' else ['list_roblox_studios','search_game_tree','execute_luau','start_stop_play','get_console_output','screen_capture','user_keyboard_input']
   if mode=='late' and listings==1:names=[]
   v={'tools':[{'name':n} for n in names]}
   if mode=='invalid':v={'tools':'not a list'}
   if mode=='pages':
    v={'tools':[{'name':n} for n in names[:3]],'nextCursor':'second'} if not m['params'].get('cursor') else {'tools':[{'name':n} for n in names[3:]]}
  r={'jsonrpc':'2.0','id':m['id'],'result':v}
 if mode=='notifications':print('synthetic diagnostic');print(json.dumps({'jsonrpc':'2.0','method':'notifications/tools/list_changed'}))
 print(json.dumps(r),flush=True)
'''


class ProbeTests(unittest.TestCase):
    def run_fake(self, mode, timeout=2):
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / 'fake.py'
            script.write_text(FAKE)
            return probe_module.probe([sys.executable, '-u', str(script), mode], timeout, retries=0)

    def test_handshake_without_tools_is_not_success(self):
        value = self.run_fake('empty')
        self.assertTrue(value['initialized'])
        self.assertEqual(value['status'], 'initialized_no_tools')
        self.assertFalse(value['gameplay_verified'])

    def test_full_tool_listing_does_not_prove_place_or_gameplay(self):
        value = self.run_fake('full')
        self.assertEqual(value['status'], 'tools_exposed')
        self.assertFalse(value['place_identity_verified'])
        self.assertFalse(value['gameplay_verified'])

    def test_partial_capabilities_stay_partial(self):
        value = self.run_fake('partial')
        self.assertEqual(value['status'], 'tools_exposed_incomplete')
        self.assertIn('player_input', value['missing_capabilities'])

    def test_default_performs_one_listing(self):
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / 'fake.py'
            script.write_text(FAKE)
            value = probe_module.probe([sys.executable, '-u', str(script), 'late'], timeout=2)
            self.assertEqual(value['status'], 'initialized_no_tools')

    def test_notifications_and_noise_do_not_replace_reply(self):
        self.assertEqual(self.run_fake('notifications')['status'], 'tools_exposed')

    def test_pagination_preserves_all_tools(self):
        self.assertEqual(self.run_fake('pages')['tool_count'], 7)

    def test_rpc_error_is_failure(self):
        self.assertEqual(self.run_fake('rpc_error')['status'], 'connection_failed')

    def test_closed_server_is_failure(self):
        self.assertEqual(self.run_fake('closed')['status'], 'connection_failed')

    def test_timeout_is_bounded_failure(self):
        self.assertEqual(self.run_fake('timeout', .15)['error'], 'response_timeout')

    def test_malformed_tools_is_failure(self):
        self.assertEqual(self.run_fake('invalid')['error'], 'invalid_tools_list')

    def test_missing_executable_is_failure(self):
        value = probe_module.probe(['/definitely-missing-game-forge-probe'], timeout=1)
        self.assertEqual(value['status'], 'connection_failed')


if __name__ == '__main__':
    unittest.main()

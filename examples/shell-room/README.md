# Disposable one-shell test

Status: **source prepared; live execution not yet established**. This is a tiny original fixture for validating Game Forge's Studio workflow, not a complete game. PC keyboard/mouse, session-only state, one player, original primitive placeholders; no purchases, persistence, external assets or game publication.

## Preconditions and setup

Open a disposable blank Baseplate in Studio. Enable the built-in MCP through Assistant's MCP settings, register the displayed stdio connection in the selected host, and list/read the intended place harmlessly. Save a recoverable baseline. Inspect the actual tools and their schemas; do not use a different open place by mistake.

Execute [setup.luau](setup.luau) in that target's **Edit** context through an available supported Luau editing/execution route. It refuses to overwrite the owned fixture names. Existing unrelated instances are preserved. It creates the `GameForgeSmoke` workspace folder, one server script, one client script, and one restart RemoteEvent. Read back these instances and script sources before playtesting. Stopping a runtime test does not apply runtime experiments back to the Edit model.

## Actual input sequence to run

| ID | Action | Expected observation; not an observed result |
| --- | --- | --- |
| T-01 | Start an avatar playtest; inspect startup UI and both output contexts | Gold shell, green boat, visible instructions; no fixture error |
| T-02 | Walk to the boat and press E before collecting | No win; server `ForgeLastAction=RejectedEarlyDeposit` |
| T-03 | Walk to the gold shell and press E | Shell hides locally; UI directs player to boat; `ForgeCollected=true` |
| T-04 | Walk to the boat and press E | Visible win; server `ForgeWon=true`, `ForgeAwards=1` |
| T-05 | Interact with boat again | Award remains 1; duplicate deposit rejected |
| T-06 | Press R or click Restart, then complete another normal loop | Shell/UI reset; no stuck state; exactly one award in the new round |
| T-07 | Collect, then use the normal avatar reset/death path | Round resets on respawn, shell visible, normal loop can complete |
| T-08 | Stop; verify persistent Edit model. Save/reopen or reconstruct in a fresh blank place | Repeated short input-driven success/restart passes on durable/reconstructed source |

Use actual player inputs. Direct attribute edits, internal reward calls, or teleporting past the loop are supplementary diagnostics and do not pass traversal/control tests. Record actual tool calls, target identity, build revision, input sequence, client/server output and inspected screenshots, expected versus observed results, failures, fixes and reruns. Mark unrun checks unrun.

The server validates proximity and owns collection/win/award state. This small fixture is not a production security or multiplayer/persistence/performance qualification. New characters reset the round; Restart resets awards for that round. No broad deletion/cleanup script is supplied—remove only named fixture objects in the disposable place after inspecting them, or discard that test place through its normal recoverable workflow.

Run [the connection diagnostic](../../scripts/probe_studio.py) separately. A complete tool list still does not establish a verified place or passed gameplay. For the current observed run status, see [the live test report](../../docs/live-test-2026-10-27.md).

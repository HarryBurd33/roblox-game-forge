# Fixture evidence log

2026-10-27, final builder r3, Studio `0.745.0.7451137`, Codex desktop/macOS and official StudioMCP stdio. A unique unsaved Place1 was verified against the original blank Baseplate hierarchy before editing. Exact ephemeral target identity and full raw requests/results are retained privately.

See [the live report](../../../docs/live-test-2026-10-27.md) and [sanitized tool evidence](../../../docs/evidence/studio-live-2026-10-27.json) for actual inputs, returned state, final source hashes and inspected image hashes.

| Check | Result | Actual observation |
| --- | --- | --- |
| T-01 | passed after repair | Startup instructions and shell visible; final console has no fixture error |
| T-02 | passed | Early boat interaction rejected; no award |
| T-03 | passed | E collected shell; hidden locally; full carry instruction visible |
| T-04 | passed | E at boat produced visible win and one server-owned award |
| T-05 | passed | Duplicate E rejected; award remained one |
| T-06 | passed | R and actual GUI button reset shell/state; second input-driven loop won once |
| T-07 | passed | Normal Escape/R/Return changed character identity; respawn restored round; next loop won |
| T-08 | reconstruction portion passed | Final builder reexecuted after restoring original blank baseline in same instance; exact script readback and win/restart repeated; stopped Edit state verified |

T-08 separate-new-place and saved-file reopen portions remain unrun. No binary place file was delivered. Multiplayer, touch/controller, cloud persistence, external assets and measured performance are unrun.

Failed runs were retained: first client startup dereferenced Shell before replication; waits fixed this. Longer HUD messages clipped; a larger label and lower button were persisted in source and retested after clean reconstruction. Three nonfixture asset-type warnings remained; no external asset occurs in fixture source. Runtime experiments alone were not accepted as durable fixes.

Final state: Edit mode, prototype present, original Baseplate objects retained, owned stdio client closed. No game publishing or paid action.

## Earlier unsuccessful attempt

| Evidence type | Check | Actual result | Limit |
| --- | --- | --- | --- |
| configuration readback | Codex Roblox_Studio entry | enabled stdio entry for official bundled executable | configuration is not connectivity |
| actual read-only MCP | initialize | official RobloxStudio proxy replied | no place/editor capability proven |
| actual read-only MCP | tools/list | zero tools | input/edit/play/output/viewport unavailable |
| native UI attempt | getApp Studio, then Finder | timeouts | toggle/place contents not observed |
| offline synthetic protocol | probe regression suite | passed | fake servers; no Roblox gameplay |
| static | fixture source and checklist | prepared and inspected | no Luau compile or execution claim |
| unavailable | T-01 through T-08 | unrun | requires verified live place/tools |

No actual player inputs, reward observations, client/server gameplay output, viewport screenshots, saved-place reopen or reconstruction were obtained. No pass is inferred from setting state, a hand-written checklist, the helper tests or a clean console.

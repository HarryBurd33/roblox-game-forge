# Fixture evidence log

2026-10-27. Keep expected behavior in [the checklist](../README.md) separate from actual observations.

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

Next run: record actual target/build revision, input sequence, expected/observed results and inspected evidence; preserve any failed run and append its repair/retest. Do not overwrite this unsuccessful connectivity attempt with a later pass.

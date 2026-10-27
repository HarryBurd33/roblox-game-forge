# Shell-room fixture brief

Revision 1, 2026-10-27. Status: source prepared; Studio implementation and gameplay unrun. Project source: [setup.luau](../setup.luau). No Studio instance/place identity has been verified.

Confirmed scope from the user: set up the official Studio MCP connection, run a small isolated prototype test, fix observed issues and update the skill repository. Preserve unrelated work.

Chosen reversible fixture defaults: PC keyboard/mouse, one player, session-only state, original primitive placeholders; no purchases, cloud persistence or game publishing. One floor, one gold shell, one green boat, a visible status/win HUD, and restart. First minute: spawn, read the visible cue, walk to shell, collect with E, walk to boat, deposit with E, win, restart with R or the button. Avatar reset restarts the round. Rewards count once per round.

| Requirement | Acceptance test | Intended implementation | Observed status |
| --- | --- | --- | --- |
| R-001 Complete loop | T-01/T-03/T-04/T-06 | GameForgeSmoke folder, server/client scripts | unrun |
| R-002 Validated deposit | T-02/T-05 | Server proximity/collection/win checks | source inspected; live unrun |
| R-003 Restart/recovery | T-06/T-07 | Restart event, HUD button/R, CharacterAdded | source inspected; live unrun |
| R-004 Durable result | T-08 | Edit-model readback, local save or reconstruction | unrun |
| R-005 Honest connection evidence | Real initialize/tools/list; separate intended-place read | probe_studio.py and native target verification | handshake observed; zero tools; no place verified |

Open blocker: native app control times out, so the Studio MCP toggle and a disposable blank place cannot be verified. User readiness was requested. Deferred: multiplayer, mobile, persistent progression, final art and performance qualification. They are outside this tiny fixture.

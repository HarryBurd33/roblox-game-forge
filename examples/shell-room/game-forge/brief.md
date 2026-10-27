# Shell-room fixture brief

Revision 2, 2026-10-27. Status: implemented, live playtested and reconstructed from restored blank baseline. Project source: [setup.luau](../setup.luau). A unique unsaved Place1 (placeId 0) and original blank hierarchy were verified before mutation; exact ephemeral identity remains private.

Confirmed scope from the user: set up the official Studio MCP connection, run a small isolated prototype test, fix observed issues and update the skill repository. Preserve unrelated work.

Chosen reversible fixture defaults: PC keyboard/mouse, one player, session-only state, original primitive placeholders; no purchases, cloud persistence or game publishing. One floor, one gold shell, one green boat, a visible status/win HUD, and restart. First minute: spawn, read the visible cue, walk to shell, collect with E, walk to boat, deposit with E, win, restart with R or the button. Avatar reset restarts the round. Rewards count once per round.

| Requirement | Acceptance test | Intended implementation | Observed status |
| --- | --- | --- | --- |
| R-001 Complete loop | T-01/T-03/T-04/T-06 | GameForgeSmoke folder, server/client scripts | live passed |
| R-002 Validated deposit | T-02/T-05 | Server proximity/collection/win checks | live passed |
| R-003 Restart/recovery | T-06/T-07 | Restart event, HUD button/R, CharacterAdded | live passed |
| R-004 Durable result | T-08 | Edit-model readback, local save or reconstruction | same-instance clean-baseline reconstruction passed; saved-file/new-place checks unrun |
| R-005 Honest connection evidence | Real initialize/tools/list; separate intended-place read | probe_studio.py and native target verification | 28 real tools; intended place inspected; edit/play/input/output/viewport exercised |

No current MCP blocker. Native app control had timed out; user-guided Assistant enablement exposed the working tools. The final persistent source includes replication waits, explicit spawn and readable longer HUD text. Deferred/unrun: distinct-new-place reconstruction, saved-place reopening, multiplayer, mobile, persistent progression, final art and measured performance. See [actual playtest evidence](playtests.md).

# Validation status

Version 0.1.2. Checked 2026-10-27 America/Denver. This page distinguishes observed evidence from conditional instructions. It does not certify that every Studio runtime feature works in every host.

## Observed evidence

- An independent foundation review inspected current official Roblox documentation and actual license/source files for Roblox's official setup skill, Roblox Suite, and Rojo. Original workflow text was written; no upstream code or framework was vendored. Exact upstream immutable revisions were unavailable and are not claimed.
- An independent resource review read the original skill, four references, four templates, README/license, and four illustrations. It found no blocking contract defect. A minor tested-interpreter wording issue was resolved by actually rerunning the offline checks with Python 3.9.6 and identifying both observed interpreters (3.15.0 and 3.9.6).
- A separate actual model executor generated 11 direct-prompt baseline responses, saved them, then read the skill and generated 11 candidate responses on the same fixed cards. Two candidate cases were partial: asking before listing available Studio identities, and bundling publication choices. The guidance was tightened; three actual targeted reruns covered both fixes plus the one-question interview regression, and met the unchanged response criteria. Raw outputs remain private; only sanitized scenario criteria and the bounded findings are published.
- The skill's 13 files passed offline metadata/link/template checks and exact ZIP/source comparison. Fresh extraction also passed; two builds from the same source produced identical ZIP bytes. The public repository adds a standalone validator, negative fixture tests, and CI rather than making a gameplay claim from those checks.

The 11 cases cover vague interviewing, a complete ten-stage mobile/no-monetization obby, speed/cooperation revision, missing integration, three activation exclusions, saved-record resume, ambiguous places, source-only completion/publishing, and a conditional full-loop test plan.

## Distribution checks

The public repository is recognized by GitHub as MIT licensed and public, with 11 relevant Roblox/Codex/Luau/design/MCP topics. [The first GitHub Actions run](https://github.com/HarryBurd33/roblox-game-forge/actions/runs/40454038481) passed the package validator and all 19 fixture tests on Python 3.11 and 3.13. Local checks also passed on Python 3.9.6.

The official Skill Installer installed all 13 skill files from immutable source revision `d2ae28298cc3a8ce42dda72488dbcec171ca31f7`. Each installed file's SHA256 matched the reviewed public source. A real local Codex 0.164.0 app-server `skills/list` request with forced reload reported `roblox-game-forge` enabled with **user** scope from two unrelated working directories, with no skill-loading errors. This was a read-only discovery probe and started no model turn. It establishes local global installation/discovery; it does not establish native behavior on another device or working Studio tools.

After the live test, the existing unmodified global copy was updated to version 0.1.2. All 13 files matched the current canonical/public skill source, and the new ZIP's entries matched those source bytes. This update did not repeat the earlier native discovery probe.

## Live Studio result and remaining limits

The [2026-10-27 live report](live-test-2026-10-27.md) preserves the initial failed connection attempt and the successful continuation. After the user enabled Studio as MCP server through Assistant, the official stdio server exposed 28 tools. The intended original blank Baseplate was listed and inspected. A tiny original shell-room fixture was implemented, read back, and played using actual supported walking, keyboard and GUI input.

Collection/deposit/win/repeat, early and duplicate deposit rejection, R and button restart, and normal avatar-reset recovery passed. A real replication race and clipped longer HUD messages were repaired and retested. Final source was reconstructed after restoring the original blank baseline in the same instance, a short normal win/restart loop passed again, and persistent Edit sources matched after Stop. See [the tool-derived evidence receipt](evidence/studio-live-2026-10-27.json). The owned test client closed; no game was published.

This run used Codex desktop/macOS and Studio engine 0.745.0.7451137, through official StudioMCP stdio tools. Three nonfixture asset-type warnings remained; a clean console is not claimed. The repository's 30 offline tests remain package/protocol checks, distinct from this actual gameplay evidence.

A distinct-new-place reconstruction, saved `.rbxl` reopen, two-client/device checks, cloud persistence round trip, asset import and measured performance remain unrun. The successful solo loop does not qualify these conditional branches. Skill installation alone still does not enable the Studio bridge; use the [official setup guide](https://create.roblox.com/docs/studio/mcp) and [setup reference](../skills/roblox-game-forge/references/studio-setup.md).

## Evidence limits

The model comparisons used one separate executor context, baseline first; carryover is possible. Grading was non-blind, sample size small, and exact inherited model/version/effort unverified. Cards labeled heldout were known to the author and are reserved assessment cases, not blind held-out evidence. No statistical superiority, task-completion rate, cost saving, or commercial outcome is established. A response about a source package did not create that package in the response-policy trial. Examples are authored illustrations.

The initial source package was validated before public documentation changes. Public structural/fixture checks and installed/remote file comparison validate the distributed version separately. Only completed observations are reported as such; a procedure is not a passed test.

## Broader follow-up procedure

1. Install the skill into a disposable project and verify native discovery. Check a Unity build request, account-support request, and narrow Vector3 question do not start the game workflow.
2. Connect a disposable local Studio place through the built-in server. Discover actual schemas, list/read identities harmlessly, and verify the intended target. If two open places share a name, resolve the target before any mutation.
3. Give the sufficient brief: one room, one shell, a boat deposit, visible win, restart; PC only, session only, no purchases, original primitive placeholders. Expect implementation without repeated premise/device interviews and records linking requirement IDs to actual source/tests.
4. Preserve a recoverable baseline, implement/read back through supported Edit tools, then start an avatar playtest. Use player input to collect, deposit, win, restart, and repeat. Exercise early/duplicate deposit, repeated restart, applicable death/reset recovery, and output/viewport inspection. Preserve failures and repair/retest.
5. Stop play, verify durable Edit changes, save/reopen locally or reconstruct from editable source in a fresh place, and repeat a short success/restart check. Give focused movement feedback; verify brief/source/checks change together.
6. Resume from saved records in a fresh context. Verify actual files and current connection, retain settled answers, and continue the next defined check. Use separate tiny tests for two-client authority/disconnect, touch/UI, isolated persistence success/failure/rejoin, and measured performance when those branches are required.

The core tiny loop above has now run; use this broader procedure for new hosts/features. Record host/Studio versions, actual tool capability, target identity, build revision, inputs, expected/observed results, errors, inspected visual evidence, and save/reopen evidence. Mark unsupported or unrun checks explicitly. A verified playable prototype can only be claimed after its actual core loop and relevant recovery paths are observed.

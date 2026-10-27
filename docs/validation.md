# Validation status

Version 0.1.1. Checked 2026-10-26 America/Denver. This page distinguishes observed evidence from conditional instructions. It does not certify that every Studio runtime feature works in every host.

## Observed evidence

- An independent foundation review inspected current official Roblox documentation and actual license/source files for Roblox's official setup skill, Roblox Suite, and Rojo. Original workflow text was written; no upstream code or framework was vendored. Exact upstream immutable revisions were unavailable and are not claimed.
- An independent resource review read the original skill, four references, four templates, README/license, and four illustrations. It found no blocking contract defect. A minor tested-interpreter wording issue was resolved by actually rerunning the offline checks with Python 3.9.6 and identifying both observed interpreters (3.15.0 and 3.9.6).
- A separate actual model executor generated 11 direct-prompt baseline responses, saved them, then read the skill and generated 11 candidate responses on the same fixed cards. Two candidate cases were partial: asking before listing available Studio identities, and bundling publication choices. The guidance was tightened; three actual targeted reruns covered both fixes plus the one-question interview regression, and met the unchanged response criteria. Raw outputs remain private; only sanitized scenario criteria and the bounded findings are published.
- The skill's 13 files passed offline metadata/link/template checks and exact ZIP/source comparison. Fresh extraction also passed; two builds from the same source produced identical ZIP bytes. The public repository adds a standalone validator, negative fixture tests, and CI rather than making a gameplay claim from those checks.

The 11 cases cover vague interviewing, a complete ten-stage mobile/no-monetization obby, speed/cooperation revision, missing integration, three activation exclusions, saved-record resume, ambiguous places, source-only completion/publishing, and a conditional full-loop test plan.

## Live connection probe and remaining limits

Roblox Studio 0.734.0.7340915 was present on the validation Mac. The official bundled `StudioMCP` process answered a real stdio MCP initialize request, identifying itself as RobloxStudio 1.0.0. A tool-list request returned **zero tools**, including on an unsandboxed local connection probe. Therefore no selected place, editing/input/output capability, or live playable prototype was established. The native UI inspection also timed out. No unrelated place was edited, no runtime test was claimed, and no game was published.

Setup must expose the intended place's real tools before live features can be exercised. Skill installation alone does not enable that bridge. The [official setup guide](https://create.roblox.com/docs/studio/mcp) and [skill setup reference](../skills/roblox-game-forge/references/studio-setup.md) give the required steps.

No actual gameplay, real two-client/device test, cloud persistence save/rejoin, asset import, saved-place reopen, or performance measurement has passed here. Emulation, mock stores, script inspection, screenshots alone, and directly setting a win variable cannot substitute for those observations.

## Evidence limits

The model comparisons used one separate executor context, baseline first; carryover is possible. Grading was non-blind, sample size small, and exact inherited model/version/effort unverified. Cards labeled heldout were known to the author and are reserved assessment cases, not blind held-out evidence. No statistical superiority, task-completion rate, cost saving, or commercial outcome is established. A response about a source package did not create that package in the response-policy trial. Examples are authored illustrations.

The initial source package was validated before public documentation changes. Public structural/fixture checks and installed/remote file comparison validate the distributed version separately. Only completed observations are reported as such; a procedure is not a passed test.

## Remaining tiny live test

1. Install the skill into a disposable project and verify native discovery. Check a Unity build request, account-support request, and narrow Vector3 question do not start the game workflow.
2. Connect a disposable local Studio place through the built-in server. Discover actual schemas, list/read identities harmlessly, and verify the intended target. If two open places share a name, resolve the target before any mutation.
3. Give the sufficient brief: one room, one shell, a boat deposit, visible win, restart; PC only, session only, no purchases, original primitive placeholders. Expect implementation without repeated premise/device interviews and records linking requirement IDs to actual source/tests.
4. Preserve a recoverable baseline, implement/read back through supported Edit tools, then start an avatar playtest. Use player input to collect, deposit, win, restart, and repeat. Exercise early/duplicate deposit, repeated restart, applicable death/reset recovery, and output/viewport inspection. Preserve failures and repair/retest.
5. Stop play, verify durable Edit changes, save/reopen locally or reconstruct from editable source in a fresh place, and repeat a short success/restart check. Give focused movement feedback; verify brief/source/checks change together.
6. Resume from saved records in a fresh context. Verify actual files and current connection, retain settled answers, and continue the next defined check. Use separate tiny tests for two-client authority/disconnect, touch/UI, isolated persistence success/failure/rejoin, and measured performance when those branches are required.

Record host/Studio versions, actual tool capability, target identity, build revision, inputs, expected/observed results, errors, inspected visual evidence, and save/reopen evidence. Mark unsupported or unrun checks explicitly. A verified playable prototype can only be claimed after its actual core loop and relevant recovery paths are observed.

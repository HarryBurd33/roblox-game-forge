# Engineering, evidence, and iteration

Apply concerns in proportion to the accepted brief. Do not add a backend, economy, save system, or third-party framework to a small session-only prototype without a reason.

## Recoverable implementation

Inspect existing hierarchy, scripts, assets, and source-sync boundaries first. Save or snapshot the prior version through a supported route; verify it exists. A backup command's success message alone may not establish that the expected project was saved. Record enough identity/version to recover. Avoid destructive wholesale replacement.

Plan one player-visible increment at a time: scene/spawn → interaction → goal/reward → failure/restart → relevant device/multiplayer/persistence work. Mark each requirement planned/implemented/verified/blocked independently. Read back edits. Keep runtime experiments separate from persistent Edit-model changes and verify after stopping a test.

Client startup can precede replication of a folder's children. Wait for required replicated instances before reading them, and exercise startup again after a clean play start. Inspect complete objective and win text in the actual viewport; test every longer message for clipping. When experimenting with runtime UI, apply the accepted fix to its persistent source and rebuild before claiming it survives Stop.

Consult current official [client/server guidance](https://create.roblox.com/docs/projects/client-server) and [remote boundary guidance](https://create.roblox.com/docs/scripting/security/client-server-boundary) when implementing uncertain behavior. Server code owns consequential shared state, rewards, progression, and persistence; clients request actions and handle local input/camera/UI. Validate request types/ranges, ownership, distance/state preconditions, and frequency before server changes. Never accept a client-supplied reward total as authoritative. Inspect untrusted imported model scripts before running them.

For multiplayer, define what is shared, per player, cooperative, competitive, and reset when someone leaves. Handle simultaneous completion, duplicate requests, reconnects, and a missing partner without silently changing the design. Use two actual clients for claims about two-player behavior. A solo session cannot establish cooperation.

If persistence is required, define fields/defaults/version, server ownership, write strategy and failure behavior. Use current [DataStore documentation](https://create.roblox.com/docs/cloud-services/data-stores). Isolate test data from production; do not enable production writes merely for convenience. Exercise successful save/rejoin plus denied/failed/throttled access through a suitable test seam. A mock persistence test proves logic only; it is not a live cloud round-trip. If a cloud test requires separate setup or upload not authorized, record the blocker and keep that check pending.

For target devices, verify all required actions, UI sizing/readability, touch targets, input hints, camera, and onboarding. Avoid cues that rely only on color or audio. Review text, contrast, motion sensitivity, and interaction timing relevant to the audience. For economy/monetization or content boundaries, preserve the user's exclusions and consult current official policy when implementation makes it relevant; do not default to purchases.

## Test sequence

Read [current Studio testing modes](https://create.roblox.com/docs/studio/testing-modes). Discover which modes and observation tools the selected host actually supports.

1. Record build revision, instance/place identity, initial state, scenario, expected result, and evidence destination before the test.
2. Start an avatar playtest in the intended place; a simulation without an avatar can test systems but cannot establish player controls. Inspect startup output.
3. Use actual player inputs to traverse the loop from spawn through interaction/objective to reward/completion and another cycle or restart. Capture and inspect viewport evidence at meaningful states. Confirm visible UI and authoritative state agree.
4. Exercise applicable failure: fall/death, invalid interaction, abandoned objective, retry, and reset. Verify no unintended duplicate reward, retained progress, or soft lock.
5. Run the conditional checks below. Record results per requirement, never infer one from another.
6. Inspect client and server output after exercising the loop. Repair observed defects; repeat affected scenarios and relevant regression tests.
7. Stop the test, confirm persistent Edit state, and save/reproduce through the selected supported route. Verify reopening or a fresh reconstruction before claiming durable delivery.

Teleporting past obstacles, invoking internal completion functions, or setting progress to the final stage are debugging probes. They cannot substitute for traversal, controls, or usability tests. A screenshot alone cannot establish an interaction. A clean console cannot establish success.

## Conditional checks

| Requirement | Minimum useful observation | Remaining limit to disclose |
| --- | --- | --- |
| Ten-stage checkpoint obby | Traverse each stage; reach each checkpoint; fall and respawn at the reached checkpoint; finish; restart/reset according to brief | Skipping to stage ten leaves stage traversal untested |
| Mobile | Play full loop with touch/device simulation, portrait/landscape if supported; inspect UI clipping and required actions | Emulator result differs from real hardware performance |
| Cooperative mechanic | Two clients perform independent actions, fail to solve alone when cooperation is required, disconnect/rejoin, complete together | One local client or faked second-player state is insufficient |
| Shared rewards | Observe server award and both client views; duplicate/invalid requests produce no extra award | No production security guarantee from a tiny trial |
| Persistence | Save/rejoin correct fields; new player defaults; failed access path keeps defined behavior; test data isolated | Mock and live tests labeled separately |
| Performance | Representative player/object load, agreed device/profile and scene, measured frame time/FPS and relevant server/network measurements over a stated interval | Unmeasured targets remain targets; desktop FPS is not mobile FPS |

If a performance target is absent, propose a provisional target suited to the devices and scene, label it a default, and measure if available. Do not claim optimization from code inspection. For broader multiplayer tests, use available latency simulation and state conditions; report actual settings instead of imagining network quality.

## Evidence and delivery claims

Use the [playtest log](../templates/playtest-log.md). Distinguish **planned**, **static**, **model-trial**, **live-Studio**, **user-reported**, **illustrative**, and **unavailable** evidence. Record expected versus actual, pass/fail/blocked/not-run, inputs, runtime output/visual paths or tool references, revisions, defects, and follow-up. Never mark not-run as pass. Keep raw useful logs where the user can inspect them; do not put credentials or sensitive production data in the package.

- **Designed:** brief/criteria exist.
- **Source prepared:** editable sources/package exist, Studio execution absent.
- **Studio implemented:** actual place edits verified; gameplay may still be untested.
- **Playtested:** the stated loop and relevant paths were actually exercised, with evidence and explicit gaps.
- **Locally saved/reproducible:** file reopen or package reconstruction verified separately.

Use the narrowest accurate claim. A partially verified prototype can be delivered with its missing checks. A fully verified first milestone still needs focused user feedback about feel. Keep an asset inventory with original sources, placeholder/final status, rights/import evidence and true IDs. Include exact opening instructions, controls, how to reach the loop, reset/restart, source locations, save/rebuild commands when actually supported, and the next refinement.

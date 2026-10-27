# Playtest and verification log

Copy into the game's own records directory. Record each real run separately. Keep planned steps separate from observations. Empty evidence, a successful static check, or authored example text cannot establish that gameplay worked.

## Evidence vocabulary

- `planned`: a check to run; no execution claimed.
- `static`: inspected source, metadata or project structure; no gameplay execution.
- `model-trial`: an actual model response evaluated against a scenario; no live Studio claim.
- `live-studio`: actual connected Studio execution with observed inputs and results.
- `illustrative`: authored example; not validation evidence.
- `unavailable`: required capability or environment missing; state the exact gap.

Use result `unrun`, `pass`, `fail`, `inconclusive`, or `unavailable`. A `live-studio` label alone does not imply pass. User-reported observations should identify the reporter and remain distinct from agent-observed evidence.

## Run identity

- Run ID / time / observer:
- Evidence type / result:
- Brief revision / requirement IDs:
- Build/source revision or hashes:
- Studio version, host and connection capabilities actually observed:
- Studio instance ID / place ID or local place identity:
- Identity read and recovery point before edits:
- Test mode: Edit / client / server / multiple clients:
- Device/input profile, resolution and player count:
- Persistence environment / test keys, if applicable:
- Network simulation and performance measurement setup, if applicable:

## Planned scenario

- Test ID / observable criterion:
- Preconditions and starting state:
- Input sequence and expected results:
- Relevant success, failure, recovery and restart paths:
- Stop/cleanup procedure:

Do not satisfy a gameplay test by directly granting the reward or setting the win state. Use actual player input for the loop when supported; label direct state assertions as supplementary checks.

## Actual observations

| Step / input actually performed | Expected result | Observed result | Evidence file or tool-result reference | Pass / fail / inconclusive |
| --- | --- | --- | --- | --- |
| | | | | |

- Runtime output inspected: client / server / timestamps / new errors and warnings:
- Visual/viewport evidence inspected and what it establishes:
- Core loop: spawn → onboarding → action → objective/reward:
- Failure and restart: what triggered failure, resulting state, successful recovery:
- Device controls/UI/accessibility observations:
- Multiplayer: both clients' observations, authoritative result, duplicate requests, join/leave:
- Persistence: save/rejoin/readback and unavailable/failure behavior:
- Performance: measured value, target, duration and scene/player scale:
- Test stop confirmed / leftover processes or uncertain jobs:

Only fill branches actually exercised. Device emulation is not a real hardware performance measurement; one client does not prove multiplayer behavior; a mock store does not prove cloud persistence.

## Findings and retest

| Finding ID | Severity / effect | Reproduction | Affected requirement | Repair | Retest run and actual result |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

- Unavailable or outstanding checks and exact remaining procedure:
- Known placeholders and experience limitations:
- User feedback on feel / comparison requested:
- Brief, code and acceptance updates made together:
- Saved project/source location, save/reopen or reproduction verification:
- Next bounded action and the check that will establish completion:

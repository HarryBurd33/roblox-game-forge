# Game brief

Copy this template into the game's own records directory. Fill only relevant branches; this is a living record, not a questionnaire. Keep `unknown`, `not required`, and an explicit value such as `0` distinct. Never turn a proposed default into a confirmed user decision silently.

## Record and project identity

- Brief revision / updated time:
- Project root / existing source of truth:
- Studio instance ID / place ID or local place identity:
- Identity last verified by harmless read / evidence:
- Source or saved-place version used for this brief:
- Current milestone: smallest playable Studio prototype
- Current delivery status: design only / source prepared / Studio edited / live tested / saved and verified
- Supporting records: asset inventory / playtest log / handoff paths

## Intended experience

- Premise, genre, player fantasy, audience:
- Distinctive appeal / why a player repeats the loop:
- Desired feeling, reference material, and specific liked or disliked behavior:
- First minute: spawn → discover objective → first meaningful action → feedback
- Repeatable loop: action → obstacle or choice → consequence → reward → next action
- Win, loss, recovery and restart:
- Controls, camera and movement:
- Objective, rules and constraints:

## Decision ledger

### Confirmed decisions

| Decision ID | User decision or existing authoritative requirement | Source / answer ID | Implication |
| --- | --- | --- | --- |
| D-… | | | |

### Proposed defaults

| Default ID | Proposed choice | Reason / tradeoff | When to revisit |
| --- | --- | --- | --- |
| A-… | | | |

### Unresolved questions and blockers

| Question ID | One consequential decision | Why it changes the next work | Blocking? | Answer / status |
| --- | --- | --- | --- | --- |
| Q-… | | | | |

### Deferred features

| Feature | Why outside this milestone | Revisit trigger |
| --- | --- | --- |
| | | |

## Smallest playable scope

- One complete core loop to demonstrate:
- Required world area, characters and interactions:
- Required UI, audio, onboarding and feedback:
- Progression, difficulty and replayability included now:
- Explicit exclusions, including monetization when excluded:
- First increment and the observable result it should enable:

## Proportionate technical choices

Record `not required` with a reason when a branch does not apply.

| Concern | Requirement or proposed default | Observable check / current limitation |
| --- | --- | --- |
| Target devices and input | | |
| Accessibility: readable cues, contrast, non-color feedback, input alternatives | | |
| Multiplayer count, cooperation or competition, join/leave behavior | | |
| Server-owned rules/rewards and client presentation/input | | |
| Remote request validation, duplicate claims and rate limits where needed | | |
| Persistence: what survives rejoin, test data isolation and failure behavior | | |
| Performance: target device, frame time/FPS or load budget, scene/player scale | | |
| Content boundaries, economy and monetization if relevant | | |
| Asset budget, placeholders and provenance | | |
| Sync/build tools and which side owns scripts and scene data | | |

## Requirement-to-evidence map

Every material acceptance requirement needs an observable result. Link actual instance/script paths after implementation; keep planned paths labeled planned. A test plan is not a passed test.

| Requirement ID | Observable acceptance criterion | Implementation path / status | Test ID | Result and evidence path |
| --- | --- | --- | --- | --- |
| R-… | Given … when … then … | planned / implemented / blocked | T-… | unrun / pass / fail / unavailable |

Include core-loop success, relevant failure/restart, device controls and conditional multiplayer/persistence/performance criteria. Subjective preferences need concrete references or comparisons plus user feedback; do not promise perfect fidelity or commercial success.

## Corrections and affected work

| Revision / date | Old decision → final decision | User source | Affected requirements, code, assets and tests |
| --- | --- | --- | --- |
| | | | |

Retain superseded decisions as history; the newest confirmed correction controls. Record answered question IDs so resume does not reopen them without a specific contradiction or new requirement.

## Current authority and limits

- Authorized routine implementation scope / source:
- Existing work to preserve / recovery point:
- Local save location and verification still needed:
- Upload or asset-generation authority and any cost ceiling:
- Publishing authority, destination/account/visibility if explicitly given:
- Missing capabilities / exact setup or user action needed:

Continue defined, authorized work. An unknown target place, paid action, or publishing destination can block that action without blocking independent design/source work.

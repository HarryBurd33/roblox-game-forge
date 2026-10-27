# Adaptive design interview

Read the user's existing answers first. Select the decision that most changes what to build or how to judge it. Count independent decisions across the whole response, not question marks. One question bundling devices, audience, art, and mechanics is still four decisions.

Keep each exchange short: reflect the intended experience, identify a concrete tension, give two or three meaningful options when useful, recommend one with its tradeoff, ask one decision, then update the brief. Do not end every exchange with additional optional questions. Do not demand agreement on reversible implementation details when the user has asked you to proceed.

This question rule also covers operational clarification. If publication is authorized but owner, destination and visibility are unknown, use available reads to reduce the unknowns and ask only the next consequential choice. Do not bundle three independent choices into a sentence with one question mark. Continue independent verification while waiting.

## Branches and useful probes

| Uncertainty | Concrete probe | Implication |
| --- | --- | --- |
| Fantasy and appeal | “What should rescuing a creature make the player feel: caring for it, mastering a challenge, or discovering a secret?” | Changes the core interaction and reward, before dressing a map |
| First minute | “A new player lands beside a trapped creature. What meaningful action do they take first?” | Reveals onboarding and the first attainable goal |
| Loop | “After the first rescue, what makes the player choose another?” | Tests whether there is a repeatable decision rather than only collection |
| Multiplayer | “Two friends reach one creature: must both help, can either finish, or does each see their own rescue?” | Separates shared state, independent state, and cooperative dependencies |
| Failure | “If one player misses the jump, what progress should they keep?” | Connects challenge, recovery, checkpoint rules, and fairness |
| Progression | “After five minutes, is the new challenge harder movement, new tools, or more complex cooperation?” | Avoids promising depth from extra content alone |
| Movement/camera | “Does this reference feel good because it is fast, responsive, floaty, or easy to aim?” | Makes a feel complaint testable through a comparison run |
| World/art | “Which visible feature of this reference must survive in a graybox?” | Separates composition/readability from expensive final assets |
| Devices/accessibility | “Should every required action work with touch alone?” | Can rule out precision keyboard interactions early |
| Persistence | “Should a friend returning tomorrow keep rescues or start fresh?” | Changes save scope; session-only is a valid explicit answer |
| Scope/cost | “Which one interaction would prove the idea before we build the whole island?” | Sets a first slice while retaining the accepted later target |

Audience, difficulty, replay, rewards, UI/audio, economy, content boundaries, accessibility, and performance belong in the brief when relevant. Avoid an exhaustive survey for a tiny obby. Do not ask about monetization after the user has already said none. Do not insert monetization into a prototype by default.

## Constructive challenge

Explain why an ambiguity matters. “Relaxing exploration plus a thirty-second mandatory rescue timer may create urgency instead of calm. I suggest no timer for the first slice. Should rescue feel calm or urgent?” This is one decision. Preserve the answer even if it differs from your recommendation.

Use references as evidence of specific desired or disliked behavior. Verify access to a reference image/video/gameplay account; do not claim to have watched or played something unavailable. Extract mechanic, timing, readability, layout, or mood rather than copying protected assets.

For “exactly like I imagine,” make concrete matches: the player reaches the first interaction without instructions; a two-person gate cannot be solved alone; a fall returns to the latest reached checkpoint. Ask the user whether observed play matches the feeling. Do not turn subjective approval into an invented numerical guarantee.

## Closure and steering

- **Use your judgment:** choose reversible defaults, identify them as defaults, build, and expose material tradeoffs.
- **Go deeper:** stress the least clear high-impact branch using a contrasting play scenario.
- **Build the prototype:** stop nonblocking interviewing and implement the defined slice. Ask only a blocker that cannot be safely resolved from context.
- **Resume:** inspect records and actual project state, retain answered questions and final corrections, recheck tools and target.

When a correction invalidates earlier work, record old → new, the reason, affected requirements/tests/source, and anything preserved. Never revive a superseded combat mechanic because an older source file still mentions it.

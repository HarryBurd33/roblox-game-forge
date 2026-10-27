# Illustrative uses

These four examples are authored illustrations, not executed conversations, model-trial results or Studio playtests. Any requirements added below are explicitly hypothetical answers or proposed defaults. No game was built by these examples.

## 1. Vague idea: cozy creature island

User: “Make a cozy island game where friends rescue creatures.”

A useful first response asks one consequential decision: “Should friends need each other to complete a rescue, or should each player be able to rescue creatures independently while sharing the island? Required cooperation creates shared moments; independent rescues are easier for drop-in play.”

If the user chooses required cooperation, record that answer as confirmed. Next explore one concrete rescue scenario, such as holding a gate while a friend guides a creature through. Do not ask the whole art/progression/economy questionnaire at once. If the user requests deeper design, examine whether waiting at the gate stays fun and what happens when a friend disconnects.

A proposed first playable slice is one small island area, one creature, one two-player gate and a visible rescue result. Label these scope choices as defaults until adopted. Deferred features might include breeding, an open world and a trading economy.

Planned acceptance: two players can discover the gate, coordinate through actual controls, rescue once without duplicate rewards, recover after a failed attempt and restart. Test join/leave behavior if required. Use the verified Studio connection to implement and observe that loop, repair failures, save/reopen or verify reproduction, then ask focused feedback about whether cooperation feels meaningful. Until those actions occur, status remains planned or source prepared.

## 2. Detailed brief: mobile obby

User: “Build a mobile-friendly obby with ten stages, checkpoints, and no monetization.”

Record ten stages, mobile input, checkpoint progression and zero monetization as confirmed. Do not repeat a premise or genre interview. Resolve only a material gap. For example, if checkpoint persistence is unspecified: “Should checkpoints last only until leaving the game, or survive rejoining? Session-only progress keeps this prototype smaller.” This is one decision; it does not reopen device or monetization choices.

If asked to use judgment, choose and label a reversible default for unspecified visual style or difficulty. Preserve all ten requested stages in the milestone; manageable implementation increments are not permission to silently deliver fewer.

Planned checks: touch movement/jump and readable UI; stages traversable in order; checkpoints advance only through valid progress; falling respawns at the latest earned checkpoint; restart resets the intended state; stage ten produces the finish result; no purchase prompts or monetization code. Test save/rejoin only if persistence is required. Static script inspection supplements the actual input-driven run.

## 3. Revision: speed and cooperation

User: “The movement feels slow, and I want cooperative puzzles instead of combat.”

Read the current brief and implementation first. Preserve unrelated decisions such as island setting, supported devices and no purchases. Record `combat → cooperative puzzles` as the newest correction; identify affected damage/weapon scripts, UI, rewards, level layout and acceptance checks.

Offer a concrete movement comparison using the existing value and one labeled candidate, then observe the same route with the same controls. If the current value was not read, do not invent it. Ask one focused feel question after the comparison, such as whether the faster pass still feels relaxed. Implement a sufficiently defined, authorized movement change while resolving any genuine puzzle-design blocker.

For the new puzzle, plan to test both clients' required actions, puzzle reset, repeated claims, one player leaving and success feedback. Retest movement, touch controls and any previously passing core-loop behavior affected by the change. Keep the old recovery point, update brief/code/checks together and record which previous tests are now stale.

## 4. Missing Studio integration

User: “Build the prototype,” with a sufficient one-room collection brief, but no Studio tools are exposed.

State the exact gap: the current host exposes no verified Studio connection, so it cannot edit or playtest the open place. Continue useful local work: write the brief, editable Luau/source layout, instance-construction instructions, asset inventory with explicit placeholders, and a planned core-loop/failure/restart checklist. Call the result a source package or design handoff, not a playable Studio prototype.

Point to current official Studio MCP setup instructions. Open the intended place, enable Studio as an MCP server through Assistant's MCP settings, connect the selected host using its displayed supported configuration, and rediscover actual tools. Verify identity with a harmless read; do not invent a working endpoint, tool call or asset ID. If several places are ambiguous, resolve the target before editing while continuing independent source work.

The remaining live validation is explicit: recoverable baseline → selected-place read → authorized edit/import → actual player inputs through collect/deposit/win and failure/restart → output and viewport inspection → repair/retest → local save and reopen or verified reproduction. Device, multiplayer, persistence and performance checks follow the brief. An unrun checklist remains unrun.

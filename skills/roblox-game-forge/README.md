# Roblox Game Forge 0.1.1

A reusable Codex skill for a focused design interview, an actual Studio prototype when connected, and evidence-based iteration. Accepts one-line ideas, detailed briefs, references, existing source, and saved workflow projects. No full game was developed to create this skill.

## Files and dependencies

`SKILL.md` is the entry point. Four focused references support interviewing, current Studio setup, engineering/testing, and record continuity. Four project templates make decisions, assets, tests, and handoffs durable. `examples.md` contains authored illustrations. All package text is original MIT material; no upstream code is vendored. There is no dependency on Skill Forge, Rojo, Higgsfield, Python, or a generation service to use the skill.

For live building, use Roblox Studio, an MCP-compatible AI host with a working Studio connection and appropriate inspect/edit/play/observe/input capabilities, documentation access, and local file access. Source preparation remains useful when the live connection is absent. Optional tools/assets require separate capability, rights, cost, and import verification. See [Studio setup](references/studio-setup.md).

## Install for any local Codex chat

Ask Codex: “Use $skill-installer to install https://github.com/HarryBurd33/roblox-game-forge/tree/main/skills/roblox-game-forge.” The installer places the complete folder in your user-level skills directory (normally `~/.codex/skills/roblox-game-forge/`) so it can be used across local projects and chats. It should be available on your next turn; restart Codex if it does not appear. Do not overwrite a customized copy blindly.

For project-only setup, copy the complete folder into `.agents/skills/roblox-game-forge/` in the selected project. Preserve all relative resource paths. Installation on one computer does not install it on other devices or cloud hosts. Studio connection setup is separate.

These instructions follow [OpenAI's local skill documentation](https://learn.chatgpt.com/docs/build-skills), checked 2026-10-26. A plain ZIP is a transport package for this folder; it is not a marketplace plugin or an automatic MCP installer. No account connection or Studio binary is bundled.

Try:

- “Use $roblox-game-forge to turn my cozy island creature-rescue idea into a playable prototype. Grill me one decision at a time.”
- “Use $roblox-game-forge. Build a mobile-friendly obby with ten stages, checkpoints, and no monetization.”
- “Resume this Game Forge project from game-forge/; movement feels slow and I want cooperative puzzles instead of combat.”

“What is a Vector3?”, “Reset my Roblox password,” and a Unity prototype request should use a direct answer or another workflow.

## Validation and limitations

The packaged [validation summary](validation.md) records outcomes, evidence limits, and the remaining live Studio procedure. The public repository also contains a standalone validator, fixture tests, and CI checks. Raw model outputs and private checkpoint state are excluded. Examples inside this skill are illustrative.

Test host: Codex desktop on macOS, 2026-10-26 America/Denver; offline checks ran with Python 3.15.0 and were rerun with `/usr/bin/python3` 3.9.6, also used by checkpointing. Studio MCP tools were not exposed. No live Studio editing, playtesting, asset import, native skill installation/discovery, or real device test is claimed. Exact inherited model/version/effort is not exposed to the agents and remains unverified.

Before relying on live execution, run the small remaining Studio procedure in the delivered validation report. Prototype completion must include the actual core loop, failure/restart, relevant conditional checks, and verified saving/reproduction. The skill does not guarantee subjective perfection, commercial outcomes, or access to any third-party service.

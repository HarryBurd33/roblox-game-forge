# Roblox Game Forge

A reusable Codex skill for turning Roblox game ideas into a clear design, a small playable Studio prototype when connected, and focused feedback/playtest iterations. MIT licensed. Accepts a one-sentence idea, a complete brief, references, existing source, or a saved project.

The interviewer asks one consequential decision at a time, challenges vague mechanics and excessive scope, preserves settled answers, and moves a sufficiently defined brief into implementation. The workflow checks actual tools and the intended Studio place before editing, then links requirements to source and observed tests.

## Install globally

In Codex, ask:

```text
Use $skill-installer to install this skill globally:
https://github.com/HarryBurd33/roblox-game-forge/tree/main/skills/roblox-game-forge
```

The installer uses your user-level skills directory, normally `~/.codex/skills/roblox-game-forge/`. The skill will be available on your next turn in local Codex chats across projects. Restart Codex if it does not appear. An installation on one computer does not install it on other devices or cloud hosts. Preserve an existing customized copy instead of overwriting it blindly.

For project-only use, copy the complete [`skills/roblox-game-forge/`](skills/roblox-game-forge/SKILL.md) folder into that project's `.agents/skills/roblox-game-forge/`. Keep its references and templates together. See [OpenAI's skill setup documentation](https://learn.chatgpt.com/docs/build-skills).

## Use it

```text
Use $roblox-game-forge to turn my cozy island creature-rescue idea
into a playable Roblox prototype. Grill me one decision at a time.
```

```text
Use $roblox-game-forge. Build a mobile-friendly obby with ten stages,
checkpoints, and no monetization. Use your judgment on visual placeholders.
```

```text
Use $roblox-game-forge to resume this project from game-forge/.
The movement feels slow, and I want cooperative puzzles instead of combat.
```

Say **go deeper** to explore an unclear design decision, **use your judgment** to delegate reversible choices, **build the prototype** to proceed with defined work, or **resume** to restore saved project decisions. Supply the project folder or saved records when continuing in another chat. A complete brief skips repeated introductory questions.

The skill creates project-owned brief, asset, playtest, and handoff records beside editable source. It preserves confirmed decisions, proposed defaults, open questions, and deferred features separately. Narrow Luau questions, Roblox account support, playing Roblox, and other engines do not trigger this full workflow.

## Connect Roblox Studio for live building

Global skill installation supplies instructions; Studio connectivity is a separate dependency. Use the [official built-in MCP setup](https://create.roblox.com/docs/studio/mcp): open the intended place, open Assistant's MCP settings, enable Studio as MCP server, and use the displayed connection instructions for your host. Verify available tools and the intended instance/place with a harmless read. A successful MCP handshake alone does not prove a place or editing tools are connected.

Live prototyping needs inspection, instance/Luau editing, play start/stop, player input, runtime output, viewport observation, and a supported save/reproduction route. Tool schemas and feature availability can change. Read the [setup reference](skills/roblox-game-forge/references/studio-setup.md) for checks and troubleshooting. No Studio binary, account credentials, auto-installer for MCP, or publishing authority is bundled.

For a bounded read-only connection check, run `python3 scripts/probe_studio.py` on the Studio computer. It reports configuration-independent MCP initialization and exposed capability names; zero/partial tools return a nonzero exit status. Even a full tool list leaves intended-place and gameplay verification pending. The [2026-10-27 live test](docs/live-test-2026-10-27.md) subsequently verified the [disposable shell-room fixture](examples/shell-room/README.md) using actual walking, interaction, restart, avatar reset, and clean-baseline reconstruction.

## Capability and verification status

| Capability | What this skill provides | Evidence/status |
| --- | --- | --- |
| Global local installation/discovery | User-level skill installation across projects | All 13 installed files matched published source; native Codex listing returned enabled user scope in two directories |
| Adaptive interview, complete-brief shortcut, corrections, resume | An explicit workflow, examples, and durable templates | Actual model-response trials across 11 scenario cards, plus 3 targeted reruns; small, non-blind sample |
| Requirements, asset provenance, source/test traceability | Four project templates and focused references | Independently inspected; structural checks and negative fixture tests |
| Studio editing and playable prototyping | Tool-driven implementation conditional on a verified live connection | One actual PC/session prototype built, read back, playtested and repaired through official StudioMCP |
| Actual gameplay and failure/restart | Conditional acceptance procedures matched to each brief | Collect/deposit/win/repeat, early/duplicate rejection, R/button restart and avatar-reset recovery passed in the tiny fixture |
| Multiplayer, touch, persistence and performance | Brief-dependent checks | Unrun; the solo desktop result does not establish these branches |
| Save/reopen and reproducible delivery | Explicit verification rules and handoff records | Final source reconstructed from the restored blank baseline and retested in the same instance; separate-place reconstruction and saved-file reopening unrun |
| External assets, Higgsfield, Rojo and Git | Optional verified tools, never mandatory dependencies | No asset generation/import round-trip or paid service is required or claimed tested |

This is an instruction skill, not a standalone game generator or a guarantee of subjective fidelity. With missing Studio capabilities, it prepares useful design/source and an exact handoff, and labels unexecuted work honestly. Paid purchases, unrelated destructive edits, asset uploads, and game publishing require their own applicable authority.

## Validate and contribute

Python 3.9+ and the standard library are enough for repository checks:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

CI runs those checks. They validate package structure, license, paths, templates, and rejection of invalid/private exports; they do not run a model or Roblox. [Validation status and the remaining tiny Studio procedure](docs/validation.md) distinguish static checks, actual model responses, authored illustrations, and unavailable live tests. [Scenario cards](tests/cases.json) define expected behavior and are not themselves passed tests. [Illustrative examples](skills/roblox-game-forge/examples.md) are explicitly unexecuted.

For changes, preserve the one-decision interview and complete-brief fast path, add a discriminating case for any new behavior, run the offline checks, and report which live/model tests actually ran. Never add credentials, private project records, raw model logs, or fabricated integrations and test evidence. See the [MIT license](LICENSE). Roblox names and trademarks belong to their respective owners; this is an independent community skill.

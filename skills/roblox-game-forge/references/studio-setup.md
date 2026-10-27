# Studio connection and optional assets

Documentation snapshot checked 2026-10-26 America/Denver. Use current official instructions and the installed host's actual tool schemas before acting; names and UI can change. Documentation is capability guidance, not proof that a tool ran here.

## Connect and identify

Use [Roblox's official Studio MCP guide](https://create.roblox.com/docs/studio/mcp). Install/update Studio and an MCP-compatible host separately if needed. In Studio, open Assistant → … → Manage MCP Servers and enable Studio as MCP server. Use the displayed Quick connect or configuration for the selected host; Codex CLI is documented. For desktop host behavior, verify its current connection setup rather than assuming the CLI connection is inherited.

In the tested macOS ribbon, Assistant was the looped icon immediately left of the notification bell. Opening it revealed the panel's … menu. Treat that as a dated visual cue, not a permanent location: inspect the current UI if it differs. The Rojo panel's Connect button is a different integration.

The documented transport is stdio; current examples name Studio's bundled `StudioMCP` executable on macOS and `mcp.bat` on Windows. Copy the configuration Studio displays, verify the binary/path, and preserve unrelated MCP settings. Do not invent an HTTP endpoint, install an old bridge by default, or overwrite the host configuration blindly. If setup fails, verify the path and syntax and restart Studio/client as instructed by the official guide.

Discover available tools, then list Studio instances. Current docs use `list_roblox_studios` and explicit `studio_id` targeting on later calls. Resolve the intended place from project records/name/place ID and harmless state or hierarchy reads. An unsaved local place may lack a place ID; use its returned instance identity and inspect distinguishing contents. List/read first and present returned distinguishing IDs or contents; do not ask the user to retrieve information the tools can supply. If the target still remains uncertain, ask the single target choice before edits. Do independent source work meanwhile. Recheck target after reconnecting. Never start a user's unrelated session or stop their running test without understanding its state.

## Capability receipt

Record host/version if observed, Studio version if available, observation time, instance/place, exposed tool names and schemas, and these independently verified capabilities:

| Need | Verification |
| --- | --- |
| Inspect | Harmless state and tree/instance reads on intended target |
| Edit | Later, an authorized small reversible instance/script change and readback |
| Play | Start/stop supported with known Client/Server/Edit context |
| Observe | Actual output and viewport capture returned and inspected |
| Input | Supported player navigation/input can exercise the loop |
| Preserve | Local save/export or documented reproducible disk-to-Studio route, verified separately |

Do not test editing merely to establish initial connectivity. Verify mutating capabilities when prototype work is authorized. Read tool schema documentation for `datamodel_type`, script paths, and target parameters; never infer an argument shape from a similar tool. If an equivalent supported tool or UI route is available, record the substitute and what it can establish.

## Missing integration handoff

State the precise gap: host exposes no Studio tools, no place is connected, inspection works but editing does not, or input/observation is absent. Finish the brief, source, instance-placement instructions, asset list, and planned tests that local tools support. Include:

1. Open the intended place in Studio and enable the built-in server using the official guide.
2. Add the displayed connection to the selected host and reload/restart as required; no automatic host configuration change is implied.
3. Discover tools and verify the intended instance/place with harmless reads.
4. Import/sync the named prepared sources into the specified containers using the documented route.
5. Execute the recorded gameplay, failure/restart, and conditional tests; preserve errors and inspect visuals.
6. Verify local save/reopen or reproduce from the package, then update the delivery claim.

A source folder without these live checks is not a working Studio prototype. If all automation is unavailable, give precise user-operated steps and request the relevant returned evidence; distinguish user-reported results from agent-observed ones.

## Optional assets and sync

Original Studio primitives are sufficient for a first playable slice. Native Studio generation, Creator Store assets, editable Blender exports, and optional external generators can help later. [Rojo](https://rojo.space/docs/) is optional source tooling; inspect the existing sync configuration and [sync limits](https://rojo.space/docs/v7/sync-details/). A sync/build pass does not prove gameplay or preserve every Studio asset/property.

[Higgsfield's Blender integration](https://higgsfield.ai/plugins/blender) advertises geometry through Meshy 5. It is an asset candidate, not a verified Roblox builder or required dependency. The actual export format and Roblox import round-trip were not verified in this skill build. Recheck the selected service/model's [terms](https://higgsfield.ai/terms-of-use-agreement), access, credit charge, and output rights; do not rely on a general marketing permission claim.

Before generation/import: identify the needed asset type, actual downloadable format, editable source, scale/material/rig/collision needs, authorized cost and upload scope, provenance, attribution, and restrictions. Check current [Studio importer requirements](https://create.roblox.com/docs/studio/importer). Test one small asset before a batch, inspect scripts in inserted models, and record actual returned IDs only. A preview is not a successful import. If rights, access, cost, or compatibility cannot be established, keep a labeled original placeholder and continue.

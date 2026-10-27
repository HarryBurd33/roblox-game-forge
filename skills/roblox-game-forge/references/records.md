# Persistent project records and resume

Use the project's established source of truth. Otherwise copy the four templates into a `game-forge/` folder beside source. Templates are scaffolding: placeholders do not count as recorded decisions or executed work. Keep project-private values out of this reusable skill's installed files.

| Bundled template | Project record |
| --- | --- |
| `templates/game-brief.md` | `game-forge/brief.md` |
| `templates/asset-inventory.csv` | `game-forge/assets.csv` |
| `templates/playtest-log.md` | `game-forge/playtests.md` |
| `templates/handoff.md` | `game-forge/handoff.md` |

`brief.md` records the vision and distinct sets of confirmed decisions, proposed defaults, unresolved questions, and deferred work; answered questions; requirements/acceptance/implementation/evidence links; and chronological changes. Give requirements stable IDs such as R-001. When scope changes, supersede an old requirement explicitly rather than silently reusing its ID for a different meaning. Note which requirements remain unaffected.

`assets.csv` records original/third-party sources, final/placeholder status, rights and attribution, actual IDs or absent values, editable paths, import evidence and costs. Empty asset ID means absent/unknown, not an invented zero. Explicit budget zero and no monetization are valid decisions, never missing data.

`playtests.md` records actual versus planned verification, build revisions, target identity, inputs, expected/actual, output/visual evidence, defects and reruns. Separate source inspection from live execution. Preserve failed results; add a rerun rather than rewriting history to show only the pass.

`handoff.md` is the current continuation pointer: source and saved project/package paths, known good state, how to open/play/reset, actual verification scope, limitations, pending jobs, authorized boundaries, blockers, answered questions, and next action with a check. Keep the detailed brief/test log authoritative; a handoff should point to them accurately.

Update records after a consequential decision, prototype increment, test/fix, feedback correction, and before ending. Preserve earlier copies through existing version control or backups; avoid blind overwrites if another person edited the files. Never store tokens, credentials, or an authorization grant for future unknown external actions.

On resume:

1. Read brief, handoff, assets, test log and supplied corrections. Check the files actually exist and belong to this project. If records conflict, preserve both and resolve only material discrepancies.
2. Inspect actual source/project/save state; do not infer it from the previous chat's claim. Reconcile incomplete imports, saves, generation jobs, or publishing outcomes before retrying side effects.
3. Rediscover host tools, harmlessly verify the Studio target, and check current authorization. A saved capability receipt can be stale. No saved permission authorizes a new paid action or publication.
4. Preserve settled answers and final revisions. Continue the next defined increment or missing check. Ask only an unknown that blocks it.
5. If file access is unavailable, supply explicit copyable records and request the relevant existing record before claiming continuation memory. Say exactly which records were saved and which were merely drafted.

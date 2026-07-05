---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - codex
  - setup
  - assisto
notes:
  - "[[20_Progress/AI/Codex/MOC]]"
next: "none — single config file, light-touch reference dump"
---
# Assisto (.codex) — Codex Setup
A copy of the Codex CLI config file for Assisto. Sibling to [[20_Progress/AI/Codex/Assisto - .agents/Setup|the .agents context folder]] for the same project.
## Files
None — no markdown files exist in this folder.
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Codex/Assisto - .codex"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `config.toml` — Codex CLI configuration for this project.
## Links
[[20_Progress/AI/Codex/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

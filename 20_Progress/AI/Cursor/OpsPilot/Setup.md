---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - cursor
  - setup
  - opspilot
notes:
  - "[[20_Progress/AI/Cursor/MOC]]"
next: "none — single settings file, no markdown config captured for this project's Cursor layer"
---
# OpsPilot — Cursor Setup
The Cursor dump for OpsPilot is a single non-markdown settings file — no rules, skills, or agents were captured for this project's Cursor layer.
## Files
None — no markdown files exist in this folder.
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Cursor/OpsPilot"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `settings.json` — enables the `supabase` plugin. That's the entire captured config.
## Status & Gaps
External project dump, no live equivalent in this vault to diff against — marked `static`. Compare against [[20_Progress/AI/Kiro/OpsPilot/Setup|OpsPilot's Kiro dump]] and [[20_Progress/AI/Codex/OpsPilot/Setup|Codex dump]], which both carry substantially more config (Supabase skills, hooks) than this thin Cursor capture.
## Links
[[20_Progress/AI/Cursor/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

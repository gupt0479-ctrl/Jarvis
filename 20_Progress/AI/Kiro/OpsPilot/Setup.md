---
type: project
status: dead
created: 2026-07-05
updated: 2026-07-05
tags:
  - kiro
  - setup
  - opspilot
notes:
  - "[[20_Progress/AI/Kiro/MOC]]"
next: "none — both files are broken symlink placeholders, no real content to track"
---
# OpsPilot — Kiro Setup
The Kiro dump for OpsPilot contains no real files — both entries are broken symlinks that didn't survive the Windows checkout and were captured as plain-text placeholder files instead of their target content.
## Files
None — no real markdown or skill files exist in this folder.
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Kiro/OpsPilot"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `skills/supabase` — broken symlink placeholder (29 bytes of relative-path text: `../../.agents/skills/supabase`), originally pointed at [[20_Progress/AI/Codex/Assisto - .agents/Setup|the Codex .agents skills folder]]. Not a real file — no frontmatter possible.
- `skills/supabase-postgres-best-practices` — same situation, points at `../../.agents/skills/supabase-postgres-best-practices`.
## Status & Gaps
Effectively dead: this folder never captured any of OpsPilot's actual Kiro config (steering, specs, hooks) — only two dangling symlinks meant to share Codex's Supabase skill content. Compare against [[20_Progress/AI/Cursor/OpsPilot/Setup|OpsPilot's Cursor dump]] (1 file) and [[20_Progress/AI/Codex/OpsPilot/Setup|OpsPilot's Codex dump]] (38 files, the real Supabase skill content these symlinks point to).
## Links
[[20_Progress/AI/Kiro/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

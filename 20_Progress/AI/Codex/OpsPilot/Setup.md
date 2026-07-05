---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - codex
  - setup
  - opspilot
notes:
  - "[[20_Progress/AI/Codex/MOC]]"
next: "none — light-touch reference dump; largest Codex folder, mostly a vendored skill package"
---
# OpsPilot — Codex Setup
A copy of the Codex skills folder for OpsPilot — dominated by two vendored third-party skill packages (`supabase`, `supabase-postgres-best-practices`, both `author: supabase` in their own frontmatter) rather than project-authored config. Compare against [[20_Progress/AI/Kiro/OpsPilot/Setup|OpsPilot's Kiro dump]], whose two files are broken symlinks pointing at this same skill content via Assisto's `.agents` folder.
## Files
- [[20_Progress/AI/Codex/OpsPilot/skills/supabase/SKILL|skills/supabase/SKILL]]
- [[20_Progress/AI/Codex/OpsPilot/skills/supabase/references/skill-feedback|skills/supabase/references/skill-feedback]]
- [[20_Progress/AI/Codex/OpsPilot/skills/supabase/assets/feedback-issue-template|skills/supabase/assets/feedback-issue-template]]
- [[20_Progress/AI/Codex/OpsPilot/skills/supabase-postgres-best-practices/SKILL|skills/supabase-postgres-best-practices/SKILL]]
- 33 reference docs under `skills/supabase-postgres-best-practices/references/` (connection limits, locking, indexing, RLS, schema design, monitoring — one topic per file)
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Codex/OpsPilot"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Links
[[20_Progress/AI/Codex/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

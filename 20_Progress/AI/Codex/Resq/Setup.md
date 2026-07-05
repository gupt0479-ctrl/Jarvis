---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - codex
  - setup
  - resq
notes:
  - "[[20_Progress/AI/Codex/MOC]]"
next: "none — light-touch reference dump"
---
# Resq — Codex Setup
A copy of the Codex skills folder for Resq — the same vendored `supabase` skill package seen in [[20_Progress/AI/Codex/OpsPilot/Setup|Codex/OpsPilot]], captured separately for this project. Compare against [[20_Progress/AI/Kiro/Resq/Setup|Resq's Kiro dump]] (48 files, the project's much larger Kiro-side capture).
## Files
- [[20_Progress/AI/Codex/Resq/skills/supabase/SKILL|skills/supabase/SKILL]]
- [[20_Progress/AI/Codex/Resq/skills/supabase/references/skill-feedback|skills/supabase/references/skill-feedback]]
- [[20_Progress/AI/Codex/Resq/skills/supabase/assets/feedback-issue-template|skills/supabase/assets/feedback-issue-template]]
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Codex/Resq"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Links
[[20_Progress/AI/Codex/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - codex
  - setup
  - portfolio
notes:
  - "[[20_Progress/AI/Codex/MOC]]"
next: "none — light-touch reference dump"
---
# Portfolio — Codex Setup
A copy of the Codex skills folder for the portfolio site, covered elsewhere by [[20_Progress/AI/Claude Code/Portfolio/Setup|Portfolio's Claude Code dump]], [[20_Progress/AI/Cursor/Portfolio/Setup|Cursor dump]], and [[20_Progress/AI/Kiro/Portfolio/Setup|Kiro dump]]. Nine `source-command-*` skills, one per slash command (add-project, build-fix, deploy, e2e, eval, review, sanity-push, ship-check, typecheck).
## Files
- [[20_Progress/AI/Codex/Portfolio/skills/source-command-add-project/SKILL|skills/source-command-add-project/SKILL]]
- [[20_Progress/AI/Codex/Portfolio/skills/source-command-build-fix/SKILL|skills/source-command-build-fix/SKILL]]
- [[20_Progress/AI/Codex/Portfolio/skills/source-command-deploy/SKILL|skills/source-command-deploy/SKILL]]
- [[20_Progress/AI/Codex/Portfolio/skills/source-command-e2e/SKILL|skills/source-command-e2e/SKILL]]
- [[20_Progress/AI/Codex/Portfolio/skills/source-command-eval/SKILL|skills/source-command-eval/SKILL]]
- [[20_Progress/AI/Codex/Portfolio/skills/source-command-review/SKILL|skills/source-command-review/SKILL]]
- [[20_Progress/AI/Codex/Portfolio/skills/source-command-sanity-push/SKILL|skills/source-command-sanity-push/SKILL]]
- [[20_Progress/AI/Codex/Portfolio/skills/source-command-ship-check/SKILL|skills/source-command-ship-check/SKILL]]
- [[20_Progress/AI/Codex/Portfolio/skills/source-command-typecheck/SKILL|skills/source-command-typecheck/SKILL]]
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Codex/Portfolio"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Links
[[20_Progress/AI/Codex/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

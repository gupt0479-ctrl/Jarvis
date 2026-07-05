---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - claude-code
  - setup
  - resq
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: "none — reference dump from the Resq repo, not synced to this vault"
---
# Resq — Claude Code Setup
A copy of the Claude Code agent-facing docs for Resq, a fintech hackathon build (O1 Summit 2026) — an autonomous SMB survival agent that surfaces overdue receivables, financing options, and vendor/insurance savings. Structured the same way as OpsPilot: canonical `PRD.md`, `context/`, `playbooks/`, `checklists/`, `decisions/decision-log.md`. Reference material only.
## Files
### Docs
- [[20_Progress/AI/Claude Code/Resq/README|README]] — canonical read order and agent rules
- [[20_Progress/AI/Claude Code/Resq/PRD|PRD]] — canonical product spec
### Context
- [[20_Progress/AI/Claude Code/Resq/context/12hour-execution|context/12hour-execution]]
- [[20_Progress/AI/Claude Code/Resq/context/architecture|context/architecture]]
- [[20_Progress/AI/Claude Code/Resq/context/collections-action-implementation|context/collections-action-implementation]]
- [[20_Progress/AI/Claude Code/Resq/context/current-state|context/current-state]]
- [[20_Progress/AI/Claude Code/Resq/context/product-vision|context/product-vision]]
### Playbooks
- [[20_Progress/AI/Claude Code/Resq/playbooks/backend-and-api|playbooks/backend-and-api]]
- [[20_Progress/AI/Claude Code/Resq/playbooks/supabase-and-data|playbooks/supabase-and-data]]
- [[20_Progress/AI/Claude Code/Resq/playbooks/tinyfish-and-agent|playbooks/tinyfish-and-agent]]
- [[20_Progress/AI/Claude Code/Resq/playbooks/ui-and-demo|playbooks/ui-and-demo]]
### Checklists & Decisions
- [[20_Progress/AI/Claude Code/Resq/checklists/change-gate|checklists/change-gate]]
- [[20_Progress/AI/Claude Code/Resq/checklists/demo-readiness|checklists/demo-readiness]]
- [[20_Progress/AI/Claude Code/Resq/decisions/decision-log|decisions/decision-log]]
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Claude Code/Resq"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `settings.json` — Claude Code project settings for this dump.
## Status & Gaps
External project dump, no live equivalent in this vault to diff against — every markdown file marked `static`. The README itself notes the codebase still contains legacy "restaurant-ops" terminology in places even though the product framing moved to a fintech survival agent — a gap that lives in the source repo, not here.
## Links
[[20_Progress/AI/Claude Code/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

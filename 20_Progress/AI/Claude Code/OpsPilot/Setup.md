---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - claude-code
  - setup
  - opspilot
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: "none — reference dump from the OpsPilot repo, not synced to this vault"
---
# OpsPilot — Claude Code Setup
A copy of the Claude Code project-memory layer for OpsPilot, a small-business AI workflow companion (hackathon build, demo vertical: Ember Table restaurant). Structured as agent handoff docs: a canonical `PRD.md`, live `context/`, domain `playbooks/`, `checklists/`, `workflows/`, and a `decisions/decision-log.md`. Reference material only — not part of the Jarvis vault's own tooling.
## Files
### Docs
- [[20_Progress/AI/Claude Code/OpsPilot/README|README]] — folder read-order and project rules
- [[20_Progress/AI/Claude Code/OpsPilot/PRD|PRD]] — canonical product spec
### Context
- [[20_Progress/AI/Claude Code/OpsPilot/context/6hour-status|context/6hour-status]]
- [[20_Progress/AI/Claude Code/OpsPilot/context/architecture|context/architecture]]
- [[20_Progress/AI/Claude Code/OpsPilot/context/current-state|context/current-state]]
- [[20_Progress/AI/Claude Code/OpsPilot/context/external-review-codex-2026-04|context/external-review-codex-2026-04]]
- [[20_Progress/AI/Claude Code/OpsPilot/context/keyword-map|context/keyword-map]]
- [[20_Progress/AI/Claude Code/OpsPilot/context/remote-main-and-merge|context/remote-main-and-merge]]
### Playbooks
- [[20_Progress/AI/Claude Code/OpsPilot/playbooks/ai-features|playbooks/ai-features]]
- [[20_Progress/AI/Claude Code/OpsPilot/playbooks/backend-and-api|playbooks/backend-and-api]]
- [[20_Progress/AI/Claude Code/OpsPilot/playbooks/integrations-and-webhooks|playbooks/integrations-and-webhooks]]
- [[20_Progress/AI/Claude Code/OpsPilot/playbooks/invoice-and-finance|playbooks/invoice-and-finance]]
- [[20_Progress/AI/Claude Code/OpsPilot/playbooks/supabase-and-data|playbooks/supabase-and-data]]
- [[20_Progress/AI/Claude Code/OpsPilot/playbooks/ui-and-read-models|playbooks/ui-and-read-models]]
### Checklists
- [[20_Progress/AI/Claude Code/OpsPilot/checklists/ai-change-checklist|checklists/ai-change-checklist]]
- [[20_Progress/AI/Claude Code/OpsPilot/checklists/change-planning|checklists/change-planning]]
- [[20_Progress/AI/Claude Code/OpsPilot/checklists/demo-readiness|checklists/demo-readiness]]
- [[20_Progress/AI/Claude Code/OpsPilot/checklists/mutation-checklist|checklists/mutation-checklist]]
### Decisions & Workflows
- [[20_Progress/AI/Claude Code/OpsPilot/decisions/decision-log|decisions/decision-log]]
- [[20_Progress/AI/Claude Code/OpsPilot/workflows/restaurant-core-demo|workflows/restaurant-core-demo]]
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Claude Code/OpsPilot"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
None — this folder is entirely markdown.
## Status & Gaps
External project dump, no live equivalent in this vault to diff against — every file marked `static`. Re-export from the OpsPilot repo if this needs refreshing.
## Links
[[20_Progress/AI/Claude Code/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

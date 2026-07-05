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
next: "none — light-touch reference dump"
---
# Assisto (.agents) — Codex Setup
A copy of the Codex `.agents` context folder for Assisto-Spend — compact operational memory for Codex and other agents, compared to [[20_Progress/AI/Kiro/Assisto/Setup|Assisto's Kiro dump]] and [[20_Progress/AI/Codex/Assisto - .codex/Setup|the sibling .codex config folder]].
## Files
- [[20_Progress/AI/Codex/Assisto - .agents/README|README]]
- [[20_Progress/AI/Codex/Assisto - .agents/codex-context|codex-context]]
- [[20_Progress/AI/Codex/Assisto - .agents/codex-kiro-work-plan|codex-kiro-work-plan]]
- [[20_Progress/AI/Codex/Assisto - .agents/mcp-checklist|mcp-checklist]]
- [[20_Progress/AI/Codex/Assisto - .agents/backend-phase-0-freeze|backend-phase-0-freeze]]
- [[20_Progress/AI/Codex/Assisto - .agents/hooks/final-report-template|hooks/final-report-template]]
- [[20_Progress/AI/Codex/Assisto - .agents/hooks/preflight-checklist|hooks/preflight-checklist]]
- [[20_Progress/AI/Codex/Assisto - .agents/prompts/backend-phase-0-prompt|prompts/backend-phase-0-prompt]]
- [[20_Progress/AI/Codex/Assisto - .agents/prompts/first-build-prompt|prompts/first-build-prompt]]
- [[20_Progress/AI/Codex/Assisto - .agents/skills/assisto-spend-backend/SKILL|skills/assisto-spend-backend/SKILL]]
- [[20_Progress/AI/Codex/Assisto - .agents/skills/assisto-spend-docs/SKILL|skills/assisto-spend-docs/SKILL]]
- [[20_Progress/AI/Codex/Assisto - .agents/skills/assisto-spend-security/SKILL|skills/assisto-spend-security/SKILL]]
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Codex/Assisto - .agents"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Links
[[20_Progress/AI/Codex/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

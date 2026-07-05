---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - kiro
  - setup
  - safereach
notes:
  - "[[20_Progress/AI/Kiro/MOC]]"
next: "none — external hackathon project dump; shares locked context with the Cursor dump per kiro-cursor-contract.md"
---
# SafeReach — Kiro Setup
A copy of the Kiro workspace for SafeReach, the disaster-response hackathon app also covered by [[20_Progress/AI/Cursor/SafeReach/Setup|SafeReach's Cursor dump]]. The two `context/` files here (`PRD.md`, `SafeReach_Deployment_Guide.md`) are the exact locked shared-context files the Cursor dump's `kiro-cursor-contract.md` references — read them together, not independently. Reference material only.
## Files
### Context
- [[20_Progress/AI/Kiro/SafeReach/context/PRD|context/PRD]] — v2.0 product requirements, single source of truth for product/design/engineering decisions
- [[20_Progress/AI/Kiro/SafeReach/context/SafeReach_Deployment_Guide|context/SafeReach_Deployment_Guide]] — priority-ordered deployment and demo guide ("Lovable to Live URL to Winning the Hackathon")
### Steering
- [[20_Progress/AI/Kiro/SafeReach/steering/project-standards|steering/project-standards]] — always-included project standards
- [[20_Progress/AI/Kiro/SafeReach/steering/accessibility-rules|steering/accessibility-rules]] — scoped to `**/*.tsx`
- [[20_Progress/AI/Kiro/SafeReach/steering/demo-flow|steering/demo-flow]] — state transitions, scoped to Demo/Map/Shelter/Sos screen components
- [[20_Progress/AI/Kiro/SafeReach/steering/design-tokens|steering/design-tokens]] — scoped to `index.css`/`tailwind.config*`
- [[20_Progress/AI/Kiro/SafeReach/steering/matching-agent|steering/matching-agent]] — agent architecture, scoped to matching/communication agent files
- [[20_Progress/AI/Kiro/SafeReach/steering/shelter-phases|steering/shelter-phases]] — the three distinct shelter phases, scoped to ShelterScreen/Phase1/Phase15/Phase2
- [[20_Progress/AI/Kiro/SafeReach/steering/sos-screen|steering/sos-screen]] — emergency mode, scoped to SosScreen/communicationAgent
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Kiro/SafeReach"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `hooks/a11y-check-write.kiro.hook` — accessibility check on write.
- `hooks/build-after-task.kiro.hook` — build trigger after task completion.
- `hooks/demo-flow-reminder.kiro.hook` — reminds on demo-flow-affecting edits.
- `hooks/run-tests-on-edit.kiro.hook` — test runner on edit.
- `hooks/typecheck-on-save.kiro.hook` — typecheck on save.
## Status & Gaps
External project dump, no live equivalent in this vault to diff against — every file marked `static`. All 7 steering docs use Kiro's native `inclusion` key (`always`, or `fileMatch` with a `fileMatchPattern`) — tool-native, left untouched. This is the most heavily file-scoped steering set seen across all Cursor/Kiro/Codex dumps — 5 of 7 steering docs use `fileMatch` to auto-load only for relevant source paths, versus most other projects' flat `auto`/`always` steering.
## Links
[[20_Progress/AI/Kiro/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

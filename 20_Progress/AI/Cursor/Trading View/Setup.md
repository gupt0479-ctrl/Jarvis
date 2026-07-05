---
type: project
status: dead
created: 2026-07-05
updated: 2026-07-05
tags:
  - cursor
  - setup
  - trading-view
notes:
  - "[[20_Progress/AI/Cursor/MOC]]"
next: "re-export Trading View's .cursor/ config if this project resumes"
---
# Trading View — Cursor Setup
Empty folder — no Cursor config was ever captured for this project, or the capture was never completed.
## Files
None — folder is empty.
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Cursor/Trading View"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
None.
## Status & Gaps
Dead — nothing to track until this project's Cursor layer is exported. Compare against [[20_Progress/AI/Kiro/TradingView/Setup|TradingView's Kiro dump]] (4 files), which does have captured config.
## Links
[[20_Progress/AI/Cursor/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

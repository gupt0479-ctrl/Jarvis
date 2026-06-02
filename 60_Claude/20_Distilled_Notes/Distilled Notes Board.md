---
type: evergreen
input_kind: board
status: sprout
created: 2026-04-08
tags:
  - evergreen
notes:
  - "[[Claude Board]]"
---
# Distilled Notes
Evergreen knowledge artifacts extracted from conversations and sources.
## Notes
```dataview
TABLE created, status, type, next
FROM "60_Claude/20_Distilled_Notes"
WHERE type = "evergreen" OR type = "concept"
SORT file.mtime DESC
```
## Workflow
Claude creates distilled notes here when:
- A conversation produces reusable knowledge
- A concept deserves its own page
- Multiple sources converge on an insight

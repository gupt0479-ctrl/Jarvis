---
type: evergreen
input_kind: board
status: sprout
created: 2026-04-08
tags:
  - evergreen
  - "#dashboard"
notes:
  - "[[Claude Board]]"
---
# Staging Area
New Claude outputs land here for review before filing to permanent locations.
## Items to Review
```dataview
TABLE created, status, type, next
FROM "60_Claude/00_Inbox"
SORT file.mtime DESC
```
## Workflow
1. New outputs from Claude appear here
2. Review for accuracy and usefulness
3. Move to appropriate folder or tag for filing
4. Delete if not useful

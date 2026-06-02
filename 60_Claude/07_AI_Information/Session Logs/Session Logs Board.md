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
# Session Logs
Chronological record of what Claude did and when.
## Recent Sessions
```dataview
TABLE created, status
FROM "60_Claude/10_Session_Logs"
WHERE file.name != "10_Session_Logs Board"
SORT file.mtime DESC
LIMIT 15
```
## Log File
- [[log]] — Main append-only log

---
type: dashboard
status: auto-generated
tags:
  - cursor
  - wsl
---
# Session Index — portfolio

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  started_at AS "Session Ran",
  exported_at AS "Added to Jarvis",
  turn_count AS "Turns",
  files_changed_count AS "Files Changed",
  lines_added AS "+Lines",
  lines_removed AS "-Lines"
FROM "60_Claude/05_Clippings/AI Conversations/WSL/Cursor/portfolio"
WHERE type = "input"
SORT started_at DESC
```

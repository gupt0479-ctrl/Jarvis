---
type: dashboard
status: auto-generated
tags:
  - cursor
  - windows
---
# Session Index — hackathon

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  started_at AS "Session Ran",
  exported_at AS "Added to Jarvis",
  turn_count AS "Turns",
  files_changed_count AS "Files Changed",
  lines_added AS "+Lines",
  lines_removed AS "-Lines"
FROM "60_Claude/05_Clippings/AI Conversations/Windows/Cursor/hackathon"
WHERE type = "input"
SORT started_at DESC
```

---
type: dashboard
status: auto-generated
tags:
  - claude-code
  - wsl
---
# Session Index — second-brain-claudekit

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  started_at AS "Session Ran",
  exported_at AS "Added to Jarvis",
  turn_count AS "Turns",
  duration_minutes AS "Duration (min)",
  tokens.total AS "Tokens",
  cost_usd AS "Cost ($)"
FROM "60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/second-brain-claudekit"
WHERE type = "input"
SORT started_at DESC
```

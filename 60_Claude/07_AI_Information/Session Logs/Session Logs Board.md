---
type: evergreen
input_kind: board
status: retired
created: 2026-04-08
updated: 2026-08-20
tags:
  - evergreen
notes:
  - "[[Claude Board]]"
  - "[[60_Claude/07_AI_Information/Session Logs/log]]"
---
# Session Logs
**Retired 2026-08-20 — the Dataview query below has been broken since this file's creation (2026-04-08) and was never fixed.** It queried `FROM "60_Claude/10_Session_Logs"`, a folder that has never existed (the real folder is `60_Claude/07_AI_Information/Session Logs/`, where this file itself lives). Checked before retiring, not assumed: zero real wikilinks to this note exist anywhere in the vault, and [[60_Claude/07_AI_Information/Session Logs/log|the main Session Log]] doesn't link back to it either — over four months with no real dependent. Not fixed instead of retired because [[10_Areas/AI/Setup/Notes Map|Notes Map]] already correctly described this file as "a thin dataview pointer... not a separate source of information" — the real log it was meant to summarize already exists and is actively maintained; this board added no distinguishing value even when its query worked. Kept below for historical reference, not deleted, per this vault's write-contract rule against deleting without confirmation.
Chronological record of what Claude did and when.
## Recent Sessions (broken query, kept as-written)
```dataview
TABLE created, status
FROM "60_Claude/10_Session_Logs"
WHERE file.name != "10_Session_Logs Board"
SORT file.mtime DESC
LIMIT 15
```
## Log File
- [[60_Claude/07_AI_Information/Session Logs/log]] — Main append-only log, the real current source

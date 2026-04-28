---
type: evergreen
status: tree
created: 2026-04-23
updated: 2026-04-25
tags:
  - evergreen
  - dashboard
notes:
  - "[[CLAUDE.md]]"
  - "[[AGENTS.md]]"
  - "[[Random]]"
  - "[[30_Order/Templates/MOC]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/60_Indexes/Vault Health Dashboard]]"
  - "[[60_Claude/60_Indexes/Knowledge Enrichment Dashboard]]"
  - "[[40_Resources/Obsidian/Jarvis Enrichment Engine]]"
  - "[[20_Progress/Projects/Jarvis]]"
  - "[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]"
---
# Jarvis — AI-Powered PKM
## System
- [[40_Resources/Obsidian/Vault Operating System]]
- [[CLAUDE.md]]
- [[AGENTS.md]]
- [[60_Claude/60_Indexes/Claude Layer Index]]
- [[60_Claude/60_Indexes/Vault Health Dashboard]]
- [[60_Claude/60_Indexes/Knowledge Enrichment Dashboard]]
- [[40_Resources/Obsidian/Jarvis Enrichment Engine]]
- [[20_Progress/Projects/Jarvis]]
- [[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]
- [[30_Order/Templates/MOC]]
## Capability Engine
- [[60_Claude/60_Indexes/Capability Dashboard|Capability Dashboard]]
- [[60_Claude/60_Indexes/Proof Dashboard|Proof Dashboard]]
- [[60_Claude/60_Indexes/Question Dashboard|Question Dashboard]]
- [[60_Claude/60_Indexes/Field OS/AI Field OS|AI Field OS]]
- [[60_Claude/60_Indexes/Field OS/Systems Field OS|Systems Field OS]]
- [[60_Claude/60_Indexes/Field OS/Algorithms Field OS|Algorithms Field OS]]
- [[60_Claude/60_Indexes/Field OS/Career Field OS|Career Field OS]]
- [[60_Claude/60_Indexes/Field OS/Trading Field OS|Trading Field OS]]
## Knowledge Enrichment
- [[60_Claude/60_Indexes/Knowledge Enrichment Dashboard|Knowledge Enrichment Dashboard]]
- [[40_Resources/Obsidian/Jarvis Enrichment Engine|Jarvis Enrichment Engine]]
- [[30_Order/Templates/Capability/Jarvis Enrichment Template|Jarvis Enrichment Template]]

```dataview
TABLE type, status, track, enrichment_status, file.mtime AS "Updated"
FROM "10_UMN" OR "20_Progress" OR "40_Resources" OR "60_Claude/20_Distilled_Notes"
WHERE (type = "concept" OR type = "evergreen" OR type = "project")
AND (!enrichment_status OR enrichment_status != "enriched")
SORT file.mtime ASC
LIMIT 10
```
## Active Projects
```dataview
TABLE status, deadline, next, file.mtime AS "Updated"
FROM "20_Progress"
WHERE type = "project" AND status != "archived"
SORT deadline ASC, file.mtime DESC
LIMIT 12
```
## Projects Missing a Next Action
```dataview
TABLE status, deadline, file.mtime AS "Updated"
FROM "20_Progress"
WHERE type = "project" AND status != "archived" AND !next
SORT file.mtime DESC
LIMIT 10
```
## AI Staging Queue
```dataview
TABLE type, status, next, file.mtime AS "Updated"
FROM "60_Claude/00_Inbox"
WHERE file.name != "00_Inbox Board"
SORT file.mtime DESC
LIMIT 12
```
## Raw Clippings To Distill
```dataview
TABLE file.ctime AS "Captured"
FROM "60_Claude/05_Clippings"
SORT file.ctime DESC
LIMIT 12
```
## Active Classes
```dataview
TABLE WITHOUT ID
  file.link AS "Class",
  length(file.inlinks) AS "Notes"
FROM "10_UMN"
WHERE contains(file.name, "Board")
SORT file.name ASC
```
## Recent Claude Outputs
```dataview
TABLE created, status, type, file.folder AS Folder
FROM "60_Claude"
WHERE !contains(file.folder, "60_Claude/60_Indexes")
SORT file.mtime DESC
LIMIT 8
```
## Open Tasks
```dataview
TASK
FROM "20_Progress" OR "10_UMN/_Homework"
WHERE !completed
SORT due ASC
LIMIT 15
```
## Flashcard Review Queue
```dataview
LIST
FROM #cards
WHERE !contains(file.folder, "30_Order/Templates")
SORT file.mtime DESC
LIMIT 10
```
## Orphan Durable Notes
```dataview
TABLE file.folder AS Folder, status, file.mtime AS "Updated"
FROM "40_Resources" OR "60_Claude/20_Distilled_Notes"
WHERE length(file.inlinks) = 0
SORT file.mtime DESC
LIMIT 12
```
## Metadata Cleanup Queue
```dataview
TABLE file.folder AS Folder, file.mtime AS "Updated"
FROM "10_UMN" OR "20_Progress" OR "40_Resources" OR "60_Claude"
WHERE !type OR !status
SORT file.mtime DESC
LIMIT 12
```
## Recent Reviews
```dataview
TABLE file.folder AS Folder, file.ctime AS "Created"
FROM "60_Claude/50_Reviews"
WHERE file.name != "50_Reviews Board"
SORT file.ctime DESC
LIMIT 8
```
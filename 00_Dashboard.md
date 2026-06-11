---
type: evergreen
status: tree
created: 2026-04-23
updated: 2026-06-11
tags:
  - evergreen
  - dashboard
notes:
  - "[[CLAUDE.md]]"
  - "[[AGENTS.md]]"
  - "[[30_Order/Templates/MOC]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[40_Resources/Obsidian/Claude Pro Workflow]]"
  - "[[Vault Health Dashboard]]"
  - "[[Knowledge Enrichment Dashboard]]"
  - "[[40_Resources/Obsidian/Jarvis Enrichment Engine]]"
  - "[[Jarvis]]"
  - "[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]"
---
# Jarvis — Daily Execution Surface

## Today

**Focus:**

```dataview
TASK
WHERE due = date(today) AND !completed
SORT due ASC
```

## In Motion

### Active Projects

```dataview
TABLE status, deadline, next, file.mtime AS "Updated"
FROM "20_Progress"
WHERE type = "project" AND status != "archived"
SORT deadline ASC, file.mtime DESC
LIMIT 12
```

### Open Tasks

```dataview
TASK
FROM "20_Progress" OR "10_UMN/_Homework"
WHERE !completed
SORT due ASC
LIMIT 15
```

## Triage

### AI Staging Queue

```dataview
TABLE type, status, next, file.mtime AS "Updated"
FROM "60_Claude/00_Inbox"
WHERE file.name != "00_Inbox Board"
SORT file.mtime DESC
LIMIT 12
```

### Raw Clippings To Distill

```dataview
TABLE file.ctime AS "Captured"
FROM "60_Claude/05_Clippings"
SORT file.ctime DESC
LIMIT 12
```

## Decay

### Projects Missing a Next Action

```dataview
TABLE status, deadline, file.mtime AS "Updated"
FROM "20_Progress"
WHERE type = "project" AND status != "archived" AND !next
SORT file.mtime DESC
LIMIT 10
```

### Flashcard Review Queue

```dataview
LIST
FROM #cards
WHERE !contains(file.folder, "30_Order/Templates")
SORT file.mtime DESC
LIMIT 10
```

## Classes

### Active Classes

```dataview
TABLE WITHOUT ID
  file.link AS "Class",
  length(file.inlinks) AS "Notes"
FROM "10_UMN"
WHERE contains(file.name, "Board")
SORT file.name ASC
```

### Knowledge Enrichment Queue

```dataview
TABLE type, status, track, enrichment_status, file.mtime AS "Updated"
FROM "10_UMN" OR "20_Progress" OR "40_Resources" OR "60_Claude/20_Distilled_Notes"
WHERE (type = "concept" OR type = "evergreen" OR type = "project")
AND (!enrichment_status OR enrichment_status != "enriched")
SORT file.mtime ASC
LIMIT 10
```

## Navigation

**Vault system:** [[CLAUDE.md]] · [[AGENTS.md]] · [[40_Resources/Obsidian/Vault Operating System]] · [[40_Resources/Obsidian/Claude Pro Workflow]] · [[Claude Layer Index]] · [[30_Order/Templates/MOC]]

**Capability Engine:** [[Capability Dashboard]] · [[Proof Dashboard]] · [[Question Dashboard]] · [[AI Field OS]] · [[Systems Field OS]] · [[Algorithms Field OS]] · [[Career Field OS]] · [[Trading Field OS]]

**Knowledge:** [[Knowledge Enrichment Dashboard]] · [[40_Resources/Obsidian/Jarvis Enrichment Engine]] · [[Vault Health Dashboard]] · [[Jarvis]] · [[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]

## Vault Health

### Recent Claude Outputs

```dataview
TABLE created, status, type, file.folder AS Folder
FROM "60_Claude"
WHERE !contains(file.folder, "60_Claude/60_Indexes")
SORT file.mtime DESC
LIMIT 8
```

### Recent Reviews

```dataview
TABLE file.folder AS Folder, file.ctime AS "Created"
FROM "60_Claude/50_Reviews"
WHERE file.name != "50_Reviews Board"
SORT file.ctime DESC
LIMIT 8
```

### Orphan Durable Notes

```dataview
TABLE file.folder AS Folder, status, file.mtime AS "Updated"
FROM "40_Resources" OR "60_Claude/20_Distilled_Notes"
WHERE length(file.inlinks) = 0
SORT file.mtime DESC
LIMIT 12
```

### Metadata Cleanup Queue

```dataview
TABLE file.folder AS Folder, file.mtime AS "Updated"
FROM "10_UMN" OR "20_Progress" OR "40_Resources" OR "60_Claude"
WHERE !type OR !status
SORT file.mtime DESC
LIMIT 12
```

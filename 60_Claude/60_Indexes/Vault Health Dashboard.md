---
type: index
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - index
  - dashboard
  - vault-health
notes:
  - "[[00_Dashboard]]"
  - "[[Claude Layer Index]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
---
# Vault Health Dashboard

Use this page to keep the second brain queryable and clean.

## Notes Missing Core Metadata

```dataview
TABLE file.folder AS Folder, file.mtime AS Modified
FROM "10_UMN" OR "20_Progress" OR "40_Resources" OR "60_Claude"
WHERE !type OR !status
SORT file.mtime DESC
LIMIT 30
```

## Active Projects Missing a Next Action

```dataview
TABLE status, deadline, file.mtime AS Modified
FROM "20_Progress"
WHERE type = "project" AND status != "archived" AND !next
SORT deadline ASC, file.mtime DESC
LIMIT 20
```

## Inbox Items Waiting for Review

```dataview
TABLE type, status, next, file.mtime AS Modified
FROM "60_Claude/00_Inbox"
WHERE file.name != "00_Inbox Board"
SORT file.mtime ASC
```

## Recent Raw Clippings

```dataview
TABLE file.ctime AS Captured
FROM "60_Claude/05_Clippings"
SORT file.ctime DESC
LIMIT 20
```

## Claude Layer Orphans

```dataview
TABLE file.folder AS Folder, status, file.mtime AS Modified
FROM "60_Claude/20_Distilled_Notes" OR "60_Claude/30_Source_Summaries" OR "60_Claude/40_Project_Briefs"
WHERE length(file.inlinks) = 0
SORT file.mtime DESC
LIMIT 25
```

## Stale Distilled Notes

```dataview
TABLE updated, file.mtime AS Modified
FROM "60_Claude/20_Distilled_Notes"
WHERE date(file.mtime) <= date(today) - dur(45 days)
SORT file.mtime ASC
LIMIT 20
```

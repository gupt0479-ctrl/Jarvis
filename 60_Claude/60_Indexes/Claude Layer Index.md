---
type: index
status: active
created: 2026-04-08
updated: 2026-04-24
tags:
  - index
notes:
  - "[[60_Claude Board]]"
  - "[[60_Claude/60_Indexes/Vault Health Dashboard]]"
---

# Claude Layer Index

Dynamic catalog of the Claude layer.

## Source Summaries

```dataview
TABLE created, status
FROM "60_Claude/30_Source_Summaries"
WHERE !contains(file.name, "Board")
SORT file.mtime DESC
LIMIT 30
```

## Distilled Notes

```dataview
TABLE created, status
FROM "60_Claude/20_Distilled_Notes"
WHERE !contains(file.name, "Board")
SORT file.mtime DESC
LIMIT 30
```

## Project Briefs

```dataview
TABLE created, status
FROM "60_Claude/40_Project_Briefs"
WHERE !contains(file.name, "Board")
SORT file.mtime DESC
LIMIT 20
```

## Reviews

```dataview
TABLE file.folder AS Folder, created, status
FROM "60_Claude/50_Reviews"
WHERE file.name != "50_Reviews Board"
SORT file.mtime DESC
LIMIT 20
```

## Session Logs

```dataview
TABLE created, updated
FROM "60_Claude/10_Session_Logs"
SORT file.mtime DESC
LIMIT 20
```

## Staging Inbox

```dataview
TABLE type, status, next, file.mtime AS Updated
FROM "60_Claude/00_Inbox"
WHERE file.name != "00_Inbox Board"
SORT file.mtime DESC
LIMIT 20
```

## Maintenance

- Use [[60_Claude/60_Indexes/Vault Health Dashboard]] for metadata gaps, orphan notes, and stale inbox items.
- Prefer keeping this index query-driven instead of manually maintained.

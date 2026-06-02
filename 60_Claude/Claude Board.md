---
type: evergreen
input_kind: board
status: sprout
created: 2026-04-08
tags:
  - evergreen
notes:
  - "[[CLAUDE.md]]"
  - "[[60_Claude/05_Clippings/Clippings board]]"
---
# 60_Claude Dashboard
The Claude-generated knowledge layer. All assistant outputs live here.
## Structure

| Folder                | Purpose               |                                                            |
| --------------------- | --------------------- | ---------------------------------------------------------- |
| [[00_Inbox            | 00_Inbox]]            | Staging area for new Claude outputs (review before filing) |
| [[10_Session_Logs     | 10_Session_Logs]]     | Append-only log of each Claude session                     |
| [[20_Distilled_Notes  | 20_Distilled_Notes]]  | Evergreen knowledge artifacts from conversations           |
| [[30_Source_Summaries | 30_Source_Summaries]] | Distillations from 60_Claude/05_Clippings/ ingestion       |
| [[40_Project_Briefs   | 40_Project_Briefs]]   | Decision docs, project plans, career briefs                |
| [[50_Reviews          | 50_Reviews]]          | Weekly reviews, closeday summaries, lint reports           |
| [[60_Indexes          | 60_Indexes]]          | Index files for browsing                                   |
## Recent Activity
```dataview
TABLE created, status, type
FROM "60_Claude"
WHERE !contains(file.folder, "60_Claude/60_Indexes")
SORT file.mtime DESC
LIMIT 10
```
## Quick Links
- [[CLAUDE.md]] — Vault operating contract
- [[Claude Layer Index]] — Browse all Claude outputs
- [[60_Claude/05_Clippings/Clippings board]] — Raw sources to ingest
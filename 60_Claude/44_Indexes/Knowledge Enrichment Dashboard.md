---
type: index
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - index
  - dashboard
  - enrichment
notes:
  - "[[00_Dashboard]]"
  - "[[40_Resources/Obsidian/Jarvis Enrichment Engine]]"
  - "[[40_Resources/Capability/Capability Engine Guide]]"
---
# Knowledge Enrichment Dashboard
Use this page to find notes that should become stronger learning nodes.
## Enrichment Queue

```dataview
TABLE type, status, track, enrichment_status, file.mtime AS "Updated"
FROM "10_UMN" OR "20_Progress" OR "40_Resources" OR "60_Claude/20_Distilled_Notes"
WHERE (type = "concept" OR type = "evergreen" OR type = "project")
AND (!enrichment_status OR enrichment_status != "enriched")
SORT type ASC, status ASC, file.mtime ASC
LIMIT 30
```

## Tracked Concepts Missing Evidence

```dataview
TABLE track, mastery_level, status, enrichment_status
FROM "10_UMN" OR "20_Progress" OR "40_Resources" OR "60_Claude/20_Distilled_Notes"
WHERE type = "concept" AND track AND (!evidence OR length(evidence) = 0)
SORT track ASC, file.name ASC
LIMIT 30
```

## Enriched Recently

```dataview
TABLE type, track, updated, file.folder AS Folder
FROM "10_UMN" OR "20_Progress" OR "40_Resources" OR "60_Claude/20_Distilled_Notes"
WHERE enrichment_status = "enriched"
SORT updated DESC, file.mtime DESC
LIMIT 20
```

## Missing Source Anchors

```dataview
TABLE type, status, track, file.folder AS Folder
FROM "10_UMN" OR "20_Progress" OR "40_Resources" OR "60_Claude/20_Distilled_Notes"
WHERE (type = "concept" OR type = "evergreen")
AND (!source_url OR source_url = "")
AND (!source_status OR source_status = "uncertain")
SORT file.mtime DESC
LIMIT 20
```
## Enrichment CLI
```powershell
.\30_Order\System\jarvis-cli\jarvis.ps1 enrich-candidates --limit 25
```
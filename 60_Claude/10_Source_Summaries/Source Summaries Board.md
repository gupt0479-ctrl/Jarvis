---
type: evergreen
input_kind: board
status: sprout
created: 2026-04-08
tags:
  - evergreen
notes:
  - "[[Claude Board]]"
  - "[[60_Claude/05_Clippings/Clippings board]]"
---
# Source Summaries
Claude-generated summaries and distillations of raw sources from [[60_Claude/05_Clippings/Clippings board|Clippings]].
## Summaries
```dataview
TABLE created, status, source_url
FROM "60_Claude/30_Source_Summaries"
SORT file.mtime DESC
```
## Ingestion Workflow
1. Add source to `60_Claude/05_Clippings/`
2. Run `/ingest-clipping "filename.md"`
3. Review the generated summary
4. Check linked concepts and entities

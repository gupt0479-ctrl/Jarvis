---
type: evergreen
status: tree
tags:
  - dashboard
  - capability
created: 2026-04-25
updated: 2026-04-25
notes:
  - "[[00_Dashboard]]"
  - "[[Capability Dashboard]]"
  - "[[Question Dashboard]]"
---
# Proof Dashboard

Outputs are where knowledge becomes leverage. This dashboard tracks what you can demonstrate, not just what you've read.

## Outputs by Track

```dataview
TABLE output_kind, status, source_concepts
FROM ""
WHERE type = "output"
GROUP BY track
SORT track ASC
```

## Concepts With No Evidence

Tracked concepts that have zero proof artifacts. Knowledge without evidence doesn't compound.

```dataview
TABLE track, mastery_level, status
FROM ""
WHERE type = "concept" AND track AND (!evidence OR length(evidence) = 0)
SORT track ASC, file.name ASC
```

## In-Progress Outputs

Outputs not yet at `tree` status — still being drafted or refined.

```dataview
TABLE output_kind, track, status, source_concepts
FROM ""
WHERE type = "output" AND status != "tree"
SORT status ASC, file.name ASC
```

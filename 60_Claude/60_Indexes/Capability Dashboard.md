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
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[Question Dashboard]]"
  - "[[Proof Dashboard]]"
---
# Capability Dashboard

Global view of every concept the vault tracks. If a concept has `track` set, it shows up here.

## Tracked Concepts

```dataview
TABLE length(rows) AS Count
FROM ""
WHERE type = "concept" AND track
GROUP BY "Total Tracked Concepts"
```

## Mastery Distribution

How many concepts sit at each mastery level. Heavy clustering at `novice` means the engine is capturing but not drilling.

```dataview
TABLE length(rows) AS Count
FROM ""
WHERE type = "concept" AND track AND mastery_level
GROUP BY mastery_level
SORT mastery_level ASC
```

## Overdue Drills

Concepts where `next_drill` has passed. These need review.

```dataview
TABLE track, mastery_level, difficulty, next_drill
FROM ""
WHERE type = "concept" AND next_drill AND next_drill < date(today)
SORT next_drill ASC
```

## Recently Enriched

Last 10 concept notes touched, by `updated` field.

```dataview
TABLE track, mastery_level, status, updated
FROM ""
WHERE type = "concept" AND track
SORT updated DESC
LIMIT 10
```

## Missing Evidence

Tracked concepts with no entries in `evidence`. These have knowledge but no proof artifacts.

```dataview
TABLE track, mastery_level, status
FROM ""
WHERE type = "concept" AND track AND (!evidence OR length(evidence) = 0)
SORT track ASC, file.name ASC
```

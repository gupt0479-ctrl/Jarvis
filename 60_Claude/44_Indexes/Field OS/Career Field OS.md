---
type: evergreen
status: tree
tags:
  - dashboard
  - capability
  - field-os
created: 2026-04-25
updated: 2026-04-25
notes:
  - "[[Capability Dashboard]]"
  - "[[Career Depth Ladder]]"
  - "[[Career Question Bank]]"
---
# Career Field OS

Control center for the `career` track: portfolio building, STAR method, interview prep, mentorship, internship strategy, professional development.

## Capability Summary

```dataview
TABLE length(rows) AS "Tracked Concepts"
FROM ""
WHERE type = "concept" AND contains(track, "career")
GROUP BY "Career Track"
```

## Overdue Drills

```dataview
TABLE mastery_level, difficulty, next_drill, drill_interval
FROM ""
WHERE type = "concept" AND contains(track, "career") AND next_drill AND next_drill < date(today)
SORT next_drill ASC
```

## Recent Progress

```dataview
TABLE mastery_level, status, updated
FROM ""
WHERE type = "concept" AND contains(track, "career")
SORT updated DESC
LIMIT 10
```

## Open Questions

```dataview
TABLE question_kind, question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "career") AND question_status != "resolved"
SORT created ASC
```

## Outputs Produced

```dataview
TABLE output_kind, status, source_concepts
FROM ""
WHERE type = "output" AND contains(track, "career")
SORT created DESC
```

## Synthesis Notes

```dataview
TABLE concepts, tracks, status
FROM ""
WHERE contains(tags, "synthesis") AND contains(tracks, "career")
SORT updated DESC
```

## Navigation

- [[Career Depth Ladder]]
- [[Career Question Bank]]
- [[Capability Dashboard]]

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
  - "[[AI Depth Ladder]]"
  - "[[AI Question Bank]]"
---
# AI Field OS

Control center for the `ai` track: MCP, transformers, RAG, prompt engineering, agents, evaluation, and AI workflow tooling.

## Capability Summary

```dataview
TABLE length(rows) AS "Tracked Concepts"
FROM ""
WHERE type = "concept" AND contains(track, "ai")
GROUP BY "AI Track"
```

## Overdue Drills

```dataview
TABLE mastery_level, difficulty, next_drill, drill_interval
FROM ""
WHERE type = "concept" AND contains(track, "ai") AND next_drill AND next_drill < date(today)
SORT next_drill ASC
```

## Recent Progress

Last 10 AI concepts updated.

```dataview
TABLE mastery_level, status, updated
FROM ""
WHERE type = "concept" AND contains(track, "ai")
SORT updated DESC
LIMIT 10
```

## Open Questions

```dataview
TABLE question_kind, question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "ai") AND question_status != "resolved"
SORT created ASC
```

## Outputs Produced

```dataview
TABLE output_kind, status, source_concepts
FROM ""
WHERE type = "output" AND contains(track, "ai")
SORT created DESC
```

## Synthesis Notes

```dataview
TABLE concepts, tracks, status
FROM ""
WHERE contains(tags, "synthesis") AND contains(tracks, "ai")
SORT updated DESC
```

## Navigation

- [[AI Depth Ladder]]
- [[AI Question Bank]]
- [[Capability Dashboard]]

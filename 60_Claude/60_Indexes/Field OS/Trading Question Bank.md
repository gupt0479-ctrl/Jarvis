---
type: evergreen
status: tree
tags:
  - dashboard
  - capability
  - question-bank
created: 2026-04-25
updated: 2026-04-25
notes:
  - "[[Trading Field OS]]"
  - "[[Trading Depth Ladder]]"
---
# Trading Question Bank

Questions, misconceptions, and drill prompts for the `trading` track. Add entries here first — only create a separate note if the question persists across sessions.

## Open Questions

```dataview
TABLE question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "trading") AND question_kind = "open" AND question_status != "resolved"
SORT created ASC
```

## Misconceptions

```dataview
TABLE question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "trading") AND question_kind = "misconception" AND question_status != "resolved"
SORT created ASC
```

## Oral Exam Prompts

```dataview
TABLE question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "trading") AND question_kind = "oral-exam"
SORT created ASC
```

## Debugging Drills

```dataview
TABLE question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "trading") AND question_kind = "debugging"
SORT created ASC
```

## Build Prompts

```dataview
TABLE question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "trading") AND question_kind = "build"
SORT created ASC
```

## Resolved Learnings

```dataview
TABLE question_kind, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "trading") AND question_status = "resolved"
SORT created DESC
```

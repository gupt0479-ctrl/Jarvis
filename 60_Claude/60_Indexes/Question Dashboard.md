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
  - "[[Proof Dashboard]]"
---
# Question Dashboard

Durable questions that persist across sessions. Transient questions belong on track Question Banks, not here.

## Open Questions by Track

Questions with `question_status` not yet resolved, grouped by track.

```dataview
TABLE question_kind, question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND question_status != "resolved"
GROUP BY track
SORT track ASC
```

## Unresolved Misconceptions

Wrong beliefs that haven't been corrected yet. These block real understanding.

```dataview
TABLE track, question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND question_kind = "misconception" AND question_status != "resolved"
SORT created ASC
```

## Debugging Prompts Backlog

Debugging drills still in `open` status — haven't been attempted.

```dataview
TABLE track, question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND question_kind = "debugging" AND question_status = "open"
SORT created ASC
```

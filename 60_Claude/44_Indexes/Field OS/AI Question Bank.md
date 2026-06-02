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
  - "[[AI Field OS]]"
  - "[[AI Depth Ladder]]"
---
# AI Question Bank

Questions, misconceptions, and drill prompts for the `ai` track. Prefer adding entries directly to this board over creating separate note files — only promote a question to its own note if it persists across multiple sessions or blocks progress.

## Open Questions

```dataview
TABLE question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "ai") AND question_kind = "open" AND question_status != "resolved"
SORT created ASC
```

## Misconceptions

Wrong beliefs worth correcting. Each entry should state the incorrect belief and why it's wrong.

```dataview
TABLE question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "ai") AND question_kind = "misconception" AND question_status != "resolved"
SORT created ASC
```

## Oral Exam Prompts

Questions you should be able to answer cold in an interview or technical discussion.

```dataview
TABLE question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "ai") AND question_kind = "oral-exam"
SORT created ASC
```

## Debugging Drills

Given a broken scenario, diagnose the root cause.

```dataview
TABLE question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "ai") AND question_kind = "debugging"
SORT created ASC
```

## Build Prompts

Prompts that require building something to prove understanding.

```dataview
TABLE question_status, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "ai") AND question_kind = "build"
SORT created ASC
```

## Resolved Learnings

Questions that were answered — kept here as reference, not active review.

```dataview
TABLE question_kind, created
FROM ""
WHERE type = "thought" AND contains(tags, "question") AND contains(track, "ai") AND question_status = "resolved"
SORT created DESC
```

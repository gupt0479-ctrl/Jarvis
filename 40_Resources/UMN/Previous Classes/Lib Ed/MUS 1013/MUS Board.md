---
type: class
input_kind: board
status: seed
created: 2026-01-21
updated:
area:
  - "[[UMN Board]]"
  - "[[Weekly Board]]"
tags:
  - "#class"
next: "[[UMN Board]]"
---
# Data View
## Lectures & Quizzes
```dataview
TABLE created, status, area, next
FROM "10_UMN/MUS 1013"
WHERE type = "class"
AND input_kind = "lecture"
SORT created ASC
```
## Discussion & In Class Assignments
```dataview
TABLE created, status, area, next
FROM "10_UMN/_Homework/Lib Ed/MGMT"
WHERE type = "class"
AND input_kind = "homework"
SORT created ASC
```
# MOC
1. *Main*:
```dataview
TABLE created, mastery, status, topics, related
FROM "10_UMN/MUS 1013"
WHERE type = "class"
AND input_kind = "board"
SORT created ASC
```
2. *Concepts*:
```dataview
TABLE created, mastery, status, topics, related
FROM "10_UMN/MGMT 3001"
WHERE type = "concept"
SORT created ASC
```
## Resources

### Links
- 
- 

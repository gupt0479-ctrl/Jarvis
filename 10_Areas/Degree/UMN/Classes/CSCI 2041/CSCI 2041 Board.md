---
type: class
input_kind: board
status: sprout
created: 2026-01-19
updated: 2026-05-06
area:
  - "[[UMN Board]]"
tags:
  - "#class"
next:
  - "[[CSCI 2041 Note Production Plan]]"
---
# Production
- [[CSCI 2041 Note Production Plan]]

# Data view
## Labs
```dataview
TABLE created, status, area, next
FROM "10_UMN/CSCI 2041"
WHERE type = "class"
AND input_kind = "lab"
SORT created ASC
```
## Projects
```dataview
TABLE created, status, area, next
FROM "10_UMN/CSCI 2041"
WHERE type = "class"
AND input_kind = "project"
SORT created ASC
```
## Lectures
```dataview
TABLE created, status, area, next
FROM "10_UMN/CSCI 2041"
WHERE type = "class"
AND input_kind = "lecture"
SORT created ASC
```
## Exams
```dataview
TABLE created, status, area, next
FROM "10_UMN/CSCI 2041"
WHERE type = "class"
AND input_kind = "exam"
SORT created ASC
```
# MOC
```dataview
TABLE created, mastery, status, topics, related
FROM "10_UMN/CSCI 2041"
WHERE type = "concept"
SORT created ASC
```

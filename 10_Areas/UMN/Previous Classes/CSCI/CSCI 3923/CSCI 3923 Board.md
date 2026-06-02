---
type: class
input_kind: board
status: sprout
created: 2026-01-21
updated: 2026-02-26
area:
  - "[[Weekly Board]]"
  - "[[10_Areas/UMN/The Plan/Spring'26 Syllabus]]"
  - "[[10_UMN/Links|Links]]"
tags:
  - "#class"
next: "[[UMN Board]]"
---
# MOC
```dataview
TABLE created, status, area, next
FROM "10_UMN/CSCI 3923"
WHERE type = "class"
AND input_kind = "board"
SORT created ASC
```
## Resources
### Links
- [University Center for Writing](https://cla.umn.edu/center-for-writing/undergraduate-writers)
  - [[University Center for Writing (cla.umn.edu)|source note]]

### Textbook
1. 
# Data View
## Writing Assignments
```dataview
TABLE created, status, area, next
FROM "10_UMN/_Homework/CSCI/3923"
WHERE type = "class"
AND input_kind = "homework"
SORT created ASC
```
## Lecture
```dataview
TABLE created, status, area, next
FROM "10_UMN/CSCI 3923"
WHERE type = "class"
AND input_kind = "lecture"
SORT created ASC
```
## Reading Assignments
```dataview
TABLE created, status, area, next
FROM "10_UMN/CSCI 3923"
WHERE type = "class"
AND input_kind = "book"
SORT created ASC
```

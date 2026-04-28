---
type: class
input_kind: board
status: sprout
created: 2026-01-21
updated: 2026-02-26
area:
  - "[[Weekly Board]]"
  - "[[Spring'26 Syllabus]]"
  - "[[10_Areas/Links|Links]]"
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
  - [[60_Claude/30_Source_Summaries/Vault Web Ingestion/University Center for Writing (cla.umn.edu)|source note]]

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

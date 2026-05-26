---
type: class
input_kind: board
status: seed
created:
updated:
area:
tags:
  - "#class"
next:
---
# Data view
## Lectures
```dataview
TABLE created, status, area, next
FROM "10_UMN/MGMT 3001"
WHERE type = "class"
AND input_kind = "lecture"
SORT created ASC
```
## Exams
```dataview
TABLE created, status, area, next
FROM "10_UMN/MGMT 3001"
WHERE type = "class"
AND input_kind = "exam"
SORT created ASC
```

## Assignments
```dataview
TABLE created, status, area, next
FROM "10_UMN/_Homework/Lib Ed/MGMT"
WHERE type = "class"
AND input_kind = "homework"
SORT created ASC
```
# MOC
```dataview
TABLE created, mastery, status, topics, related
FROM "10_UMN/MGMT 3001"
WHERE type = "class"
AND input_kind = "board"
SORT created ASC
```
## Resources
### Links

### Group Members
- Calvin Phung - phung068@umn.edu
- Kat Nelson - nel13800@umn.edu
- Kellen Krumwiede - krumw021@umn.edu
- Maggie Hoen - hoen0044@umn.edu
- Nona Campbell - camp2912@umn.edu
- Spencer Grossman - gros0592@umn.edu
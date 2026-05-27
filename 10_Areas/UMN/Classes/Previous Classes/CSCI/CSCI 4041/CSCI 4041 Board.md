---
type: class
input_kind: board
status: sprout
created: 2026-01-22
updated: 2026-01-24
area:
  - "[[DSA]]"
  - "[[10_UMN/Links|Links]]"
  - "[[Weekly Board]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
next: "[[UMN Board]]"
---
# Data view
- Main File: [[DSA]]
## Lectures
```dataview
TABLE created, status, area, next
FROM "10_UMN/CSCI 4041"
WHERE type = "class"
AND input_kind = "lecture"
SORT created ASC
```
## Projects
```dataview
TABLE created, status, area, next
FROM "10_UMN/CSCI 4041"
WHERE type = "class"
AND input_kind = "project"
SORT created ASC
```
## MOC (Map Of Concepts)
```dataview
TABLE created, status, area, next
FROM "10_UMN/CSCI 4041"
WHERE type = "concept"
SORT created ASC
```

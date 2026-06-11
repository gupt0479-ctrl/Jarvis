---
type: evergreen
status: sprout
created: 2026-06-11
updated: 2026-06-11
tags:
  - evergreen
notes:
  - "[[Plans Board]]"
  - "[[Identities]]"
  - "[[Personality]]"
next: "[[Daily Habit Board]]"
---
# Enumerate Board
## Yearly
```dataview
TABLE created, status, related_progress, next
FROM "10_Areas/Life/Enumerate/Yearly"
WHERE type = "thought"
SORT file.mtime ASC
```
## Monthly
```dataview
TABLE created, status, related_progress, next
FROM "10_Areas/Life/Enumerate/Monthly"
WHERE type = "thought"
SORT file.mtime ASC
```
## Weekly
```dataview
TABLE created, status, related_progress, next
FROM "10_Areas/Life/Enumerate/Weekly"
WHERE type = "thought"
SORT file.mtime ASC
```
## Daily
```dataview
TABLE status, next
FROM "10_Areas/Life/Enumerate/Daily"
WHERE type = "thought"
SORT file.mtime ASC
```

---
type: evergreen
status: sprout
created: 2025-12-25
tags:
  - evergreen
notes:
  - "[[Cleaning Laptop]]"
  - "[[Arc (Learning Tracker)]]"
  - "[[Portfolio]]"
---
# Data view
```dataview
TABLE status, deadline, related_progress, next
FROM "20_Progress/Projects" OR "40_Resources/CS"
WHERE type = "project"
SORT deadline ASC
```
# Map Of Contents(MOC)

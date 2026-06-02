---
type: evergreen
input_kind: board
status: sprout
created: 2026-04-08
tags:
  - evergreen
notes:
  - "[[Claude Board]]"
---

# Reviews

Weekly reviews, daily summaries, and system health checks.

## Reviews

```dataview
TABLE created, status, type
FROM "60_Claude/50_Reviews"
SORT file.mtime DESC
LIMIT 10
```

## Commands

- `/closeday` — Create end-of-day summary
- `/weekly-review` — Generate weekly review from vault activity
- `/lint-claude-layer` — Check if 60_Claude is getting messy

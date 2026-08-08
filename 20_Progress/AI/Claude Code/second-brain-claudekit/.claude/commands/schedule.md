---
description: Build or update a schedule from tasks and project notes across the vault
---

Pull all tasks and commitments from the vault and organise them into a prioritised schedule.

## Steps

1. Scan for tasks (`- [ ]` items) in:
   - Today's daily note (`00_Daily/YYYY-MM-DD.md`)
   - All notes with `status: active` in `20_Projects/`
   - `10_Areas/` area notes (look for `## Active Tasks` sections)
2. Scan for time-sensitive items:
   - Frontmatter fields: `deadline`, `due`, `scheduled`
   - Inline patterns: `by YYYY-MM-DD`, `due: ...`, `deadline: ...`
3. Organise into a **Schedule View**:

```
## Schedule — {{date}}

### Today (must-do)
- [ ] task — source: [[note]] {{deadline if any}}

### This Week
- [ ] task — source: [[note]] {{deadline}}

### Upcoming (next 2 weeks)
- [ ] task — source: [[note]] {{deadline}}

### Someday / No Date
- [ ] task — source: [[note]]
```

4. Flag any **overdue** items (deadline in the past) at the top.
5. After showing the schedule, ask: *"Want me to copy today's tasks to your daily note?"*
6. If I say yes, append the Today tasks to `00_Daily/YYYY-MM-DD.md` under `## Scheduled Tasks`.

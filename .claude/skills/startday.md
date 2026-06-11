# today

**Description:** Build a realistic today plan from current notes, priorities, and calendar.

**Usage:** `/today`

---

## Instructions

When this skill is invoked:

### 1. Gather Context

**From 20_Progress/:**
- Read all project files
- Extract `status:`, `deadline:`, `next:` from frontmatter
- Identify projects with no next action

**From 00_Inbox/:**
- Check for unprocessed thoughts/brainstorms
- Note any time-sensitive items

**From 10_UMN/:**
- Check current courses
- Look for upcoming assignments/exams

**From 60_Claude/:**
- Read recent session logs
- Check pending actions from last session

**From Calendar (if available via MCP):**
- Today's meetings/commitments
- Available focus blocks

### 2. Prioritize

Use this framework:

1. **Deadlines first** — Anything due within 48 hours
2. **Meetings second** — Prep needed for today's meetings
3. **Next actions** — Smallest step on highest-priority project
4. **Maintenance** — Inbox processing, clipping ingestion
5. **Deep work** — One meaningful block for building/learning

### 3. Build the Plan

Create/update `60_Claude/50_Reviews/Today - YYYY-MM-DD.md`:

```markdown
---
type: plan
status: active
created: YYYY-MM-DD
tags:
  - plan
  - daily
notes:
  - "[[Project 1]]"
  - "[[Project 2]]"
---

# Today — YYYY-MM-DD

## Context

- Day of week: [Monday-Friday]
- Week: [2026-WXX]
- Energy: [high/medium/low — user can adjust]

## Schedule

| Time | Activity |
|------|----------|
| 9:00 AM | [Meeting/Focus block] |
| 11:00 AM | [Meeting/Focus block] |
| 2:00 PM | [Meeting/Focus block] |
| 4:00 PM | [Buffer/Admin] |

## Top 3

1. [Most important — deadline-driven]
2. [Second priority — project momentum]
3. [Third — maintenance or learning]

## Next Actions

### [Project 1]
- [ ] [Specific, small action]

### [Project 2]
- [ ] [Specific, small action]

### Maintenance
- [ ] Process inbox (X items)
- [ ] Ingest clippings (Y items)

## Notes from Yesterday

[If available: what was completed, what rolled over]

## End-of-Day Review

[To be filled by /closeday]
- Completed:
- Blocked:
- Learned:
```

### 4. Present the Plan

Show the user:

1. The full plan
2. Any trade-offs ("If you do X, Y will need to wait")
3. Any missing info ("You have no next action for Freelancing — want to add one?")

---

## Constraints

- **Realistic** — 3-5 hours of actual work max for busy days
- **Specific** — "Work on UROP" → "Email Prof. X about Y"
- **Flexible** — Leave buffer for interruptions
- **Linked** — Every action traces to a project

---
name: closing-day
description: Verifies today's plan was completed, collects the day's numbers in one question block, writes tracking frontmatter and the scorecard into the daily note, and resets the dashboard for tomorrow. Use at the end of each working day.
---
# closeday

**Usage:** `/closeday`

Deep detail — scorecard template, scoring rules, log format — lives in [reference.md](reference.md). This file is the step sequence; load reference.md when writing the scorecard.

## When to Invoke

At the end of the work day. Works on the daily note that `/startday` filled. The record stays in one place — no separate file is created.

## Instructions

### Step 0 — Find Today's Note

Locate `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` (today's date).

- Exists with a Morning Plan → Step 1.
- Exists without one → ask: "No morning plan found for today. Did you run `/startday`? You can still close the day — I'll write the scorecard based on what I can find." Then proceed.
- Doesn't exist → inform the user, create it with frontmatter from `30_Order/Templates/Enumerate/Better Today.md`, proceed with whatever session data exists.

### Step 1 — Auto-Gather (before talking to the user)

Read, in this order:
- Today's entries in `60_Claude/07_AI_Information/Session Logs/log.md`
- The daily note's morning plan (Academic Stack topics, Summer OS win targets, carryover items)
- Files modified in `20_Progress/` today (modification time)
- Files created in `60_Claude/10_Source_Summaries/` today

### Step 2 — Ask the User (one block, all at once)

> Closing the day — quick check:
> 1. LeetCode today: how many problems? (target ≥5)
> 2. Study hours today: total focused study time? (e.g., 2.5)
> 3. Which wins did you hit? (Project / Career / Cleanup / Review)
> 4. Habits done? (leetcode-5, csci2033, course-step, review-note)
> 5. Anything to add, blocked, or carried forward?

Accept free text. Missing answers → leave the field at its current value and mark the scorecard row "(unverified)".

### Step 3 — Write Tracking Frontmatter to the Daily Note

Update these keys in today's note (they exist from the template; never add duplicates):

```yaml
lc_count: <number>
study_today: <hours>
wins_done: <count 0-4>
habits_done: [<list>]
```

### Step 4 — Clear the Dashboard for Tomorrow

Patch `00_Dashboard.md` frontmatter only:

```yaml
today_focus: ""
today_80: ""
today_20: ""
lc_today: 0
study_today: 0
wins_done: 0
```

Everything `/startday` patches gets cleared. Touch no other field.

### Step 5 — Score and Append the Scorecard

Append the End of Day section (template and GREEN/RED rules: [reference.md §1](reference.md)) below the Morning Plan. Never modify the Morning Plan itself.

### Step 6 — Log the Session

Append the closeday entry to `60_Claude/07_AI_Information/Session Logs/log.md` using [reference.md §2](reference.md) — it includes `lc_count`, `study_today`, and `wins_done`.

## Constraints

- Never create `60_Claude/30_Reviews/Closeday - YYYY-MM-DD.md`. The daily note is the record.
- Only append below the Morning Plan; if a scorecard already exists, ask before overwriting.
- Be honest about what you can and can't verify. Don't fake checkmarks.
- Steps 3–4 touch frontmatter keys only — no body rewrites, no other fields.

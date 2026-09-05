---
name: starting-day
description: Fills today's periodic note with a concrete work plan pulled from the summer OS, session history, and habit board, then patches the dashboard's Today's Focus. Use at the start of each working day, after the daily note exists (or to create it from the template).
---
# startday

**Usage:** `/startday`

Deep detail — exact patch formats, table shapes, output template — lives in [reference.md](reference.md). This file is the step sequence; load reference.md when actually patching.

## When to Invoke

At the start of the day. The Periodic Notes plugin normally creates today's note at `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md`; this skill fills it and updates `00_Dashboard.md`.

## Instructions

### Step 0 — Find Today's Note

Locate `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` (today's date).

- Exists → Step 1.
- Missing → create it from `30_Order/Templates/Enumerate/Better Today.md` (copy frontmatter and structure verbatim, resolve the `<% tp.date.now %>` placeholder to today's date), then Step 1.
- Template also missing → create the note with minimal frontmatter (`type: daily`, `created: YYYY-MM-DD`, `status: sprout`, `lc_count: 0`, `study_today: 0`, `wins_done: 0`, `habits_done: []`) and continue.

Never create it anywhere else. `60_Claude/30_Reviews/` is not the target.

### Step 1 — Read Plan Context

Read these six files. No other reads. No vault dump.

| File | What to extract |
|------|-----------------|
| `10_Areas/Life/Plans/Summer/Daily Operating System.md` | 4 wins + MVP variants + 8-track academic stack |
| `10_Areas/Life/Plans/Summer/Weekly Operating System.md` | Today's day-of-week focus |
| `10_Areas/Life/Plans/Summer/Final Month Plan (Jul 28 - Sep 1).md` | Deadlines within 7 days (certifications, Git exam), this week's flagship, Current Progress |
| `10_Areas/Life/Plans/Summer/LeetCode & CSCI 4041.md` (§8 Daily Log for solved count vs ≥35/week) | Today's LC topic; solved count |
| `10_Areas/Life/Plans/Summer/ML Fundamentals (2033 + 2230).md` (§8 Progress Tracking) | Today's CSCI 2033 broad-pass unit |
| `10_Areas/Life/Habits/` — find the file with a `## Daily` heading (currently `Habit Tracker Board.md`; don't hardcode the name, it has changed before) | Active daily habits |

Note: as of 2026-07-27 this folder holds 6 files, not the old 00–08 numbered set — two plan/tracker pairs were merged into single files (their tracker data now lives in a numbered `§8` section of the plan note), and the status/close-out/monthly-plan notes were consolidated into [[Final Month Plan (Jul 28 - Sep 1)]]. If a referenced file is missing, check the index (`00 - Summer Plans Index.md`) before assuming it was never created.

If any file is missing, note it in the output and continue.

### Step 2 — Read Session History

Read `60_Claude/07_AI_Information/Session Logs/log.md`. Take the 10 most recent `## [YYYY-MM-DD]` entries: sessions 1–5 in depth (done / left open / next actions), 6–10 headline only. Build a carryover list of items left open in 1–5 and not closed later.

### Step 3 — Patch the Daily Note

Patch `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` by heading. Never overwrite frontmatter; never delete existing content. Exact per-heading formats: [reference.md §1](reference.md).

Sections to fill: summary callout, Morning Plan goal, 80 — The One Thing, 20 — Supporting Work, Summer OS Checklist win targets, Academic Stack topics, deadline alert (if due ≤7 days), carryover block (if any), anti-drift line (from `Anti-Drift Rules.md`), Productivity habit checkboxes.

### Step 3b — Patch the Dashboard

Patch `00_Dashboard.md` frontmatter only — no body edits, no other fields:

- `today_focus:` today's one-line headline objective
- `today_80:` the one task
- `today_20:` comma-separated supporting tasks

### Step 4 — Present the Plan

Output the compact summary block from [reference.md §2](reference.md), including the line `Dashboard updated: [[00_Dashboard]]`.

## Constraints

- Never create notes in `60_Claude/30_Reviews/` for the daily plan.
- Fill placeholders; never paste whole plan documents into the note.
- Leave room — `/closeday` appends an End of Day section later.
- If the Morning Plan is already filled, confirm with the user before overwriting.
- In Step 3b touch only the three named frontmatter fields.

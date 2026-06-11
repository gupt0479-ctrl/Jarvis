---
name: closing-day
description: Verifies today's plan was completed and writes the scorecard into the same daily note.
---
# closeday

**Usage:** `/closeday`

---

## When to Invoke

At the end of the work day. Works on the daily note that `/startday` already filled. The record stays in one place — no separate file is created.

---

## Instructions

### Step 0 — Find Today's Note

Locate `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` where YYYY-MM-DD is today's date.

- If it exists with a Morning Plan: proceed to Step 1.
- If it exists but has no Morning Plan: ask the user — "No morning plan found for today. Did you run `/startday`? You can still close the day — I'll write the scorecard based on what I can find." Then proceed.
- If it doesn't exist at all: inform the user, create the note with frontmatter from the template, and proceed to Step 1 with whatever session data exists.

---

### Step 1 — Gather What Actually Happened

**From the session log** (`60_Claude/07_AI_Information/Session Logs/log.md`):
- Find all entries with today's date
- Extract: what was done, what was deferred, any explicit outputs

**From vault file activity:**
- Check `20_Progress/` for any project notes modified today (use file modification time)
- Note count of files modified in `10_Areas/` and `60_Claude/` today

**From the morning plan in the daily note:**
- Read the Academic Stack table — which rows had topics filled in
- Read the Summer OS Checklist — what wins were targeted
- Read any carryover items

---

### Step 2 — Optional User Input

Ask once: **"Anything to add before I close the day? (LeetCode count, anything blocked, wins to capture)"**

Accept a free-text response. If user says "no" or skips, continue.

---

### Step 3 — Score and Patch the Daily Note

Append the following section to `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md`. Do not modify the Morning Plan section — only append below it.

```markdown
---

## End of Day

### Summer Ops Scorecard

| Track     | Minimum  | Met?       |
|-----------|----------|------------|
| LeetCode  | ≥5       | [ ] count: |
| CSCI 4041 | 25-45 min| [ ]        |
| CSCI 2033 | 30-45 min| [ ]        |
| MATH 2230 | board    | [ ]        |
| HIST 1103 | step/N/A | [ ]        |
| 5 Wins    | 5/5      | [ ]        |

**Day Status: GREEN** (or **RED**)

> GREEN = ≥90% rows met AND LeetCode ≥5. Everything else = RED.
> HIST 1103 counts as met if nothing was due within 7 days (mark N/A).

### What Actually Happened

[2-3 honest sentences about the day — what got done, what didn't, no inflation]

### Friction Fix
*(Fill if RED — one concrete behavioral change for tomorrow)*

### Preview Tomorrow
- [Top priority for tomorrow — pulled from session log carryover or plan sequence]
```

Fill in the actual checkboxes based on what you found in Step 1 and Step 2. If you have no signal for a row, leave it unchecked and note "(unverified)" next to it.

Score the day:
- GREEN if: LeetCode ≥5 AND ≥4 of the other 5 rows met
- RED otherwise

If RED: write one friction fix — a specific, behavioral change ("Do LeetCode before opening any browser tab" not "be more disciplined").

---

### Step 4 — Log the Session

Append to `60_Claude/07_AI_Information/Session Logs/log.md`:

```markdown
## [YYYY-MM-DD] closeday | Daily close

- Note: [[10_Areas/Life/Enumerate/Daily/YYYY-MM-DD]]
- Status: GREEN / RED
- LeetCode: N problems (topic)
- Open carryover: [any unclosed items rolling to tomorrow]
- Tomorrow: [top priority]
```

---

## Constraints

- Never create `60_Claude/50_Reviews/Closeday - YYYY-MM-DD.md`. The daily note is the record.
- Never modify the Morning Plan section — only append below it.
- If scorecard already exists in the note (closeday was already run), ask the user before overwriting: "Scorecard already exists for today. Overwrite?"
- Be honest about what you can and can't verify. Don't fake checkmarks.

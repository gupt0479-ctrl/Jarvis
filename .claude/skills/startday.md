# startday

**Description:** Fill today's periodic note with a concrete work plan pulled from the summer OS, session history, and habit board.

**Usage:** `/startday`

---

## When to Invoke

After opening the Periodic Notes plugin and creating today's daily note at `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md`. The plugin creates the note; this skill fills it.

---

## Instructions

### Step 0 — Find Today's Note

Locate `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` where YYYY-MM-DD is today's date.

- If it exists: proceed to Step 1.
- If it doesn't exist: create it using the content of `30_Order/Templates/Enumerate/Better Today.md` as the body (copy frontmatter and structure verbatim, then continue to Step 1).

Never create it anywhere else. `60_Claude/50_Reviews/` is not the target.

---

### Step 1 — Read Plan Context

Read these six files. No other reads. No vault dump.

| File | What to extract |
|------|-----------------|
| `10_Areas/Life/Plans/01 - Daily Operating System.md` | 5 wins (Physical, Project, Career, Cleanup, Review) + MVP variants + academic minimums |
| `10_Areas/Life/Plans/02 - Weekly Operating System.md` | Today's day-of-week focus (Mon = flagship, Fri = evidence, Sun = review, etc.) |
| `10_Areas/Life/Plans/04 - Summer Courses Ops.md` | Deadline table — any item due within 7 days |
| `10_Areas/Life/Plans/05 - LeetCode & CSCI 4041.md` + `05a - LeetCode Tracker.md` | Today's LC topic from the rotation; current solved count vs ≥35/week target |
| `10_Areas/Life/Plans/06 - ML Fundamentals (2033 + 2230).md` + `06a - ML Fundamentals Progress.md` | Today's CSCI 2033 subtopic; where we are in the unit sequence |
| `10_Areas/Life/Habits/Daily Habit Board.md` | Active daily habits to surface as checkboxes |

If any of these files are missing, note it in the output and continue with what's available.

---

### Step 2 — Read Session History

Read `60_Claude/07_AI_Information/Session Logs/log.md`.

Find the 10 most recent session entries (by `## [YYYY-MM-DD]` heading).

- **Sessions 1–5 (most recent):** Read in depth. For each extract:
  - What was done
  - What was explicitly left open or deferred
  - Any next actions recorded
- **Sessions 6–10:** Headline only — date + title line. No body needed.

Build a carryover list: anything left open in sessions 1–5 that has not been closed by a later entry.

If the session log has fewer than 10 entries, use all available.

---

### Step 3 — Patch the Daily Note

Patch `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md`. Never overwrite frontmatter. Never delete existing content. Use `vault_patch` by heading where possible.

**Under `# Did you get better today?` (the callout):**

Fill `> [!NOTE] Summary:` with one line: today's headline objective.

**Under `## Morning Plan`:**

Set `*Goal*:` to the primary objective for today — derived from 01 (5 wins) + 02 (day-of-week focus).

**Under `### 80 — The One Thing`:**

Fill the implementation intention:
```
> I will [specific task] at [time block] in [location].
- [ ] [the one task that makes today a success]
```

**Under `### 20 — Supporting Work`:**

List 2–4 supporting tasks as checkboxes. These are the academic minimums and secondary work items, not full expansion — just what needs to happen today.

**Under `## Summer OS Checklist`:**

Fill the Win column with today's specific target for each win (from 01 OS). Example: Physical = "upper body + 15 min cardio", not just "gym".

**Under `## Academic Stack`:**

Fill Topic column for each row:
- LeetCode: today's topic from the rotation in 05 (e.g., "Two Pointers") + current weekly count
- CSCI 4041: which section/concept to review from the current week
- CSCI 2033: which unit/subtopic from the sequence in 06
- MATH 2230: next item from the board (or "N/A" if board not active)
- HIST 1103: "N/A" if nothing due in 7 days, otherwise the specific admin step

**Deadline alert** — add a callout block immediately under Academic Stack if anything is due within 7 days:
```
> [!WARNING] Deadline: [Course] — [item] due [date]
```

**Carryover** — if any open items from session history, add after the Academic Stack:
```
## Carryover from Previous Sessions
- [ ] [item] — from session [date]
```

**Do NOT do today** — add as the last item under Morning Plan:
```
**Do NOT do today:** MCP/tool setup, new agents, repo triage, AI platform comparison (Anti-Drift Rules)
```

**Under `## Productivity`:**

Add habit tracking checkboxes from Daily Habit Board (active habits only):
```
| Meals | Water (3L target) |
|-------|-------------------|
|       | [ ] [ ] [ ]       |
```
Plus any keystone habits from the board as separate checkboxes below the table.

---

### Step 4 — Present the Plan

After patching, output a compact summary to the user:

```
**Today — [Day of Week], [Date]**

Goal: [one-line objective]

80: [the one task]
20: [list the supporting tasks]

Academic minimums:
- LeetCode: [topic] (at [current]/35 this week)
- CSCI 4041: [block]
- CSCI 2033: [subtopic]
- MATH 2230: [next item or N/A]
- HIST 1103: [step or N/A]

[Deadline alert if any]
[Carryover if any]

Note has been updated at: 10_Areas/Life/Enumerate/Daily/[date].md
```

---

## Constraints

- Never create notes in `60_Claude/50_Reviews/` for the daily plan.
- Never duplicate the plan files' content into the note — fill placeholders, don't paste whole documents.
- Keep the note patchable — `/closeday` will append an End of Day section later, so leave space.
- If today's note already has a filled Morning Plan (startday was already run), confirm with the user before overwriting.

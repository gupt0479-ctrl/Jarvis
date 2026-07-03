# startday — reference

Loaded on demand from SKILL.md. Contents:
1. Per-heading patch formats for the daily note
2. Step 4 output template

## §1 Per-heading patch formats

All patches go into `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md`. Use `vault_patch` by heading where possible.

**Under `# Did you get better today?` (the callout):**

Fill `> [!NOTE] Summary:` with one line: today's headline objective.

**Under `## Morning Plan`:**

Set `*Goal*:` to the primary objective — derived from 01 (5 wins) + 02 (day-of-week focus).

**Under `### 80 — The One Thing`:**

```
> I will [specific task] at [time block] in [location].
- [ ] [the one task that makes today a success]
```

**Under `### 20 — Supporting Work`:**

2–4 supporting tasks as checkboxes — academic minimums and secondary items only, not full expansion.

**Anti-Drift** — last line under Morning Plan. Read `10_Areas/Life/Plans/Summer/08 - Anti-Drift Rules.md` → `## The "Do NOT do today" list` and copy today's specific exclusions. Keep the rules in that file; never hardcode them here.

```
**Do NOT do today:** [today's exclusions from 08 - Anti-Drift Rules]
```

**Under `## Summer OS Checklist`:**

Fill the Win column with today's specific target per win (from 01 OS). Example: Physical = "upper body + 15 min cardio", not just "gym".

**Under `## Academic Stack`:**

Fill the Topic column per row:
- LeetCode: today's topic from the rotation in 05 + current weekly count
- CSCI 4041: section/concept to review this week
- CSCI 2033: unit/subtopic from the sequence in 06
- MATH 2230: next board item (or "N/A")
- HIST 1103: "N/A" unless something is due in 7 days, then the specific admin step

**Deadline alert** — immediately under Academic Stack if anything is due within 7 days:

```
> [!WARNING] Deadline: [Course] — [item] due [date]
```

**Carryover** — after the Academic Stack if session history left open items:

```
## Carryover from Previous Sessions
- [ ] [item] — from session [date]
```

**Under `## Productivity`:**

The template already carries the Meta Bind inputs (`lc_count`, `study_today`, `wins_done`) — do not duplicate them. Add habit checkboxes from the Daily Habit Board (active habits only) below the Meals/Water table as separate checkboxes.

## §2 Step 4 output template

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

Note updated: [[10_Areas/Life/Enumerate/Daily/YYYY-MM-DD]]
Dashboard updated: [[00_Dashboard]]
```

---
type: evergreen
status: active
created: 2026-06-03
updated: 2026-06-03
tags:
  - plan
  - summer
  - skills
notes:
  - "[[00 - Summer Plans Index]]"
  - "[[01 - Daily Operating System]]"
next: "[[02 - Weekly Operating System]]"
---

# Skill Patches — today / closeday

`.claude/` is write-protected in CoWork sessions, so these section blocks must be pasted into the skill files manually (or by a session with `.claude` write access). They are **section blocks only** — do not rewrite the skills; insert these and leave the rest.

## Patch 1 — `.claude/skills/today.md`

Insert this **immediately after** the line `When this skill is invoked:` and **before** `### 1. Gather Context`:

```markdown
### 0. Summer Ops Checklist (load first — June–Sept 2026)

> Source: 10_Areas/Life/Plans/. Do not duplicate logic — read the plan files.

Before anything else, build the Summer Ops Checklist at the very top of the Today note from [[01 - Daily Operating System]]:

1. Paste the daily checklist block from `10_Areas/Life/Plans/01 - Daily Operating System.md` (5 wins + academic stack).
2. Fill academic-stack rows from the course boards' `next:` — [[MATH 2230 Board]], [[HIST 1103 Board]], [[CSCI 4041 Board]].
3. Set today's LeetCode topic from the rotation in [[05 - LeetCode & CSCI 4041]].
4. Set today's CSCI 2033 subtopic from the sequence in [[06 - ML Fundamentals (2033 + 2230)]].
5. Flag any course deadline within 7 days (scan table in [[04 - Summer Courses Ops]]).
6. Add a "Do NOT do today" line: MCP/tool setup, new agents, repo triage, AI platform comparison (see [[08 - Anti-Drift Rules]]).

This section sits above the standard Schedule/Top 3.
```

## Patch 2 — `.claude/skills/closeday.md`

Insert this **immediately after** `When this skill is invoked:` and **before** `### 1. Gather Today's Activity`:

```markdown
### 0. Summer Ops Scorecard (run first — June–Sept 2026)

> Source: 10_Areas/Life/Plans/. Do not duplicate logic — read the plan files.

Audit today's Summer Ops Checklist (from the Today note) and write:

| Track | Min | Met? |
|-------|-----|------|
| LeetCode ≥5 | 5 | count: __ |
| CSCI 4041 review | 25–45 min | ☐ |
| CSCI 2033 | 30–45 min + output | ☐ |
| MATH 2230 | board next | ☐ |
| HIST 1103 | admin step (or N/A) | ☐ |
| 5 Wins (full or MVP) | 5/5 | ☐ |

Day status: GREEN if ≥90% met, else RED. LeetCode below 5 = automatic RED.
HIST counts as met if nothing due within 7 days (N/A). If RED → write ONE friction fix
for tomorrow and log it in [[08 - Anti-Drift Rules]] friction log.
```

## Patch 3 — `/ops` (morning-start / evening-close)

No file edit required if `/ops` already chains `/today` and `/closeday`. Confirm `ops.md` morning-start calls the today flow and evening-close calls the closeday flow; both now inherit the Summer Ops blocks above. If `ops.md` builds its own briefing, add one line under morning-start: *"Load [[00 - Summer Plans Index]] → run the Summer Ops Checklist (Patch 1)."* and under evening-close: *"Run the Summer Ops Scorecard (Patch 2)."*

## Why patches, not rewrites

The skills keep their existing logic (context gathering, prioritization, note templates). These blocks only add the Summer Ops layer on top and point back to `10_Areas/Life/Plans/` so the systems stay in one place.

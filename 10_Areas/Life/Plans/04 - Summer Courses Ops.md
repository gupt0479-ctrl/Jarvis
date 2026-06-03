---
type: evergreen
status: active
created: 2026-06-03
updated: 2026-06-03
tags:
  - plan
  - summer
  - courses
notes:
  - "[[00 - Summer Plans Index]]"
  - "[[Summer Courses]]"
  - "[[HIST 1103 Board]]"
  - "[[MATH 2230 Board]]"
  - "[[06 - ML Fundamentals (2033 + 2230)]]"
next: "[[05 - LeetCode & CSCI 4041]]"
---

# Summer Courses Ops

Two Anoka Ramsey courses, full 16-week load compressed into ~4–8 weeks. Goal: **A in both, never miss an assignment.** HIST is admin-only (no learning). MATH doubles as ML math — learn it properly (see [[06 - ML Fundamentals (2033 + 2230)]]).

Source of truth for deadlines stays the boards: [[HIST 1103 Board]], [[MATH 2230 Board]], [[Summer Courses]]. This note is the *operating* layer.

## Term deadline scan (rolling — re-check every Sunday)

| Date | Course | Item | Status |
|---|---|---|---|
| Jun 5 | MATH 2230 | Last day to add/drop | — |
| Jun 6 (Sat 11:30pm) | HIST 1103 | Practice + Assignments 1–3 (discussion) | — |
| Jun 8 (Mon) | MATH 2230 | WebAssign Getting Started + HW 1.1–2.2 + Quizzes 1–2 | — |
| Jun 15 | MATH 2230 | **Test 1** (Ch 1–3.3) | — |
| Jun 18 (Thu 11:30pm) | HIST 1103 | **Midterm** (30% of grade) | — |
| Jun 29 | MATH 2230 | **Test 2** (Ch 3.4–6) | — |
| Jul 2 (Thu 11:30pm) | HIST 1103 | **Final** (50%, no late finals) | — |
| Jul 3 | HIST 1103 | Assignment 13 | — |
| Jul 13 | MATH 2230 | **Test 3** (Ch 7–8, 10.1) | — |
| Jul 14 | MATH 2230 | Last day to withdraw | — |
| Jul 23 | MATH 2230 | **Test 4** (Ch 9, 12, 14) | — |
| Jul 24 | MATH 2230 | Final (optional) | — |

## HIST 1103 — admin-only playbook (zero learning)

Same playbook as cracked lib-ed courses: hit the rubric, never miss a dropbox, stay under Turnitin cap. **Never assign "learn history."**

**Hard rules from the board:**
- Post every assignment to **both** the discussion board **and** the dropbox.
- Keep Turnitin similarity **under 15%** on everything.
- **AI policy: any AI use beyond grammar = instant course failure.** Write assignments yourself; AI for grammar check only. Do not paste AI-generated prose.
- Final is **30% / 50%** weighted by exams — exams are where the grade lives. Assignments/participation = 20%, but missing them is free points lost.

**Daily trigger (the minimum HIST step):**
- If an assignment/discussion is due within 7 days → smallest next step toward it (skim the prompt, draft 3 bullets, or post). No deep reading — answer the prompt to rubric and move on.
- If nothing due within 7 days → HIST row is auto-met (mark N/A in Today note).

**MVP per assignment:** read the prompt → write to the rubric in one sitting → run grammar/Turnitin check → post to discussion **and** dropbox. Done.

**Exam MVP (Midterm Jun 18 / Final Jul 2):** these are open-with-rules; treat as timed writing. Block one prep session the day before each. No semester-long study.

## MATH 2230 — grade-A playbook (learn it; it's ML math)

Calculus-based probability & stats. HW + quizzes on **WebAssign**; everything else on D2L. Email subject line must contain "Math 2230".

**Grade structure:** HW 20% + Quizzes 20% + Tests 60%. Tests dominate → never skip a test; do not miss >1 quiz or >1 test.

**Operating cadence:**
- **WebAssign HW**: keep current with the section being covered. Late HW accepted penalty-free until ~Jul 22 — but do **not** bank it; backlog kills test prep.
- **Quizzes**: weekly, on WebAssign. Treat as low-stakes reps. Do not miss >1.
- **Tests**: 4 proctored + optional final. Block a 2-session prep ramp before each test date above.
- **ML bridge**: produce **≥1 core concept note per week** in [[06 - ML Fundamentals (2033 + 2230)]] — distributions, expectation, variance, Bayes, etc. — written for ML use, not just HW.

**Daily trigger (the minimum MATH step):**
- Check [[MATH 2230 Board]] `next:`. Currently: *WebAssign Getting Started + HW 1.1–2.2 + Quizzes 1–2, due Mon Jun 8.*
- Minimum = advance the current WebAssign set by a few problems OR one quiz. Done when WebAssign progress saved.

**Done definitions:**
- HW set: submitted before its due date.
- Quiz: attempted (not missed).
- Test: prep session done + test taken.
- Weekly: ≥1 ML concept note created.

## How this wires into daily ops

`/today` pulls each board's `next:` into the academic-stack rows. `/closeday` checks the HIST + MATH rows. The deadline scan above is re-read every Sunday in [[02 - Weekly Operating System]] and the dates flagged if within 7 days.

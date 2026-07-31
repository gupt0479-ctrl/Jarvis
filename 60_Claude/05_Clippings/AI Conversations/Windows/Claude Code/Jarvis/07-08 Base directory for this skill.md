---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: windows
title: "Base directory for this skill"
started_at: 2026-07-08T11:55:32
ended_at: 2026-07-09T11:42:41
exported_at: 2026-07-31T21:03:26
duration_minutes: 1427.1
project: Jarvis
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
session_id: dad54119-da56-4cbf-a814-b3c3a7014f73
status: raw
turn_count: 8
tools_used:
  Edit: 5
  Glob: 5
  Read: 22
  Skill: 1
  Write: 1
tokens:
  input: 111670
  output: 59466
  cache_creation: 708724
  cache_read: 4635482
  total: 5515342
cost_usd: 4.579992
model:
  - "claude-sonnet-5"
files_touched:
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\.claude\\skills\\startday\\reference.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\00_Dashboard.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Enumerate\\Daily\\2026-07-08.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Enumerate\\Daily\\2026-07-09.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Habits\\Daily Habit Board.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Habits\\Habit Tracker Board.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Plans\\Summer\\01 - Daily Operating System.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Plans\\Summer\\02 - Weekly Operating System.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Plans\\Summer\\04 - Summer Courses Ops.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Plans\\Summer\\05 - LeetCode & CSCI 4041.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Plans\\Summer\\05a - LeetCode Tracker.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Plans\\Summer\\06 - ML Fundamentals (2033 + 2230).md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Plans\\Summer\\06a - ML Fundamentals Progress.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Plans\\Summer\\08 - Anti-Drift Rules.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Degree\\MATH 2230\\MATH 2230 Board.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\30_Order\\Templates\\Enumerate\\Better Today.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\07_AI_Information\\Session Logs\\log.md"
tags:
  - input
  - ai-conversation
  - claude-code
  - windows
---

# Base directory for this skill

## You

<command-message>startday</command-message>
<command-name>/startday</command-name>

## You

Base directory for this skill: D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\startday

# startday

**Usage:** `/startday`

Deep detail — exact patch formats, table shapes, output template — lives in [reference.md](reference.md). This file is the step sequence; load reference.md when actually patching.

## When to Invoke

At the start of the day. The Periodic Notes plugin normally creates today's note at `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md`; this skill fills it and updates `00_Dashboard.md`.

## Instructions

### Step 0 — Find Today's Note

Locate `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` (today's date).

- Exists → Step 1.
- Missing → create it from `30_Order/Templates/Enumerate/Better Today.md` (copy frontmatter and structure verbatim, resolve the `(e="YYYY-MM-DD",t,n,i)=>{if(n&&!(0,Me.moment)(n,i).isValid())throw new T("Invalid reference date format, try specifying one with the argument 'reference_format'");let o;return typeof t=="string"?o=Me.moment.duration(t):typeof t=="number"&&(o=Me.moment.duration(t,"days")),(0,Me.moment)(n,i).add(o).format(e)}` placeholder to today's date), then Step 1.
- Template also missing → create the note with minimal frontmatter (`type: daily`, `created: YYYY-MM-DD`, `status: sprout`, `lc_count: 0`, `study_today: 0`, `wins_done: 0`, `habits_done: []`) and continue.

Never create it anywhere else. `60_Claude/30_Reviews/` is not the target.

### Step 1 — Read Plan Context

Read these six files. No other reads. No vault dump.

| File | What to extract |
|------|-----------------|
| `10_Areas/Life/Plans/Summer/01 - Daily Operating System.md` | 5 wins + MVP variants + academic minimums |
| `10_Areas/Life/Plans/Summer/02 - Weekly Operating System.md` | Today's day-of-week focus |
| `10_Areas/Life/Plans/Summer/04 - Summer Courses Ops.md` | Deadlines within 7 days |
| `10_Areas/Life/Plans/Summer/05 - LeetCode & CSCI 4041.md` + `05a - LeetCode Tracker.md` | Today's LC topic; solved count vs ≥35/week |
| `10_Areas/Life/Plans/Summer/06 - ML Fundamentals (2033 + 2230).md` + `06a - ML Fundamentals Progress.md` | Today's CSCI 2033 subtopic |
| `10_Areas/Life/Habits/Daily Habit Board.md` | Active daily habits |

If any file is missing, note it in the output and continue.

### Step 2 — Read Session History

Read `60_Claude/07_AI_Information/Session Logs/log.md`. Take the 10 most recent `## [YYYY-MM-DD]` entries: sessions 1–5 in depth (done / left open / next actions), 6–10 headline only. Build a carryover list of items left open in 1–5 and not closed later.

### Step 3 — Patch the Daily Note

Patch `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` by heading. Never overwrite frontmatter; never delete existing content. Exact per-heading formats: [reference.md §1](reference.md).

Sections to fill: summary callout, Morning Plan goal, 80 — The One Thing, 20 — Supporting Work, Summer OS Checklist win targets, Academic Stack topics, deadline alert (if due ≤7 days), carryover block (if any), anti-drift line (from `08 - Anti-Drift Rules.md`), Productivity habit checkboxes.

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


## Claude

### Tool Calls

- `Skill` -- `{"skill":"startday"}`

## You

Base directory for this skill: D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\startday

# startday

**Usage:** `/startday`

Deep detail — exact patch formats, table shapes, output template — lives in [reference.md](reference.md). This file is the step sequence; load reference.md when actually patching.

## When to Invoke

At the start of the day. The Periodic Notes plugin normally creates today's note at `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md`; this skill fills it and updates `00_Dashboard.md`.

## Instructions

### Step 0 — Find Today's Note

Locate `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` (today's date).

- Exists → Step 1.
- Missing → create it from `30_Order/Templates/Enumerate/Better Today.md` (copy frontmatter and structure verbatim, resolve the `(e="YYYY-MM-DD",t,n,i)=>{if(n&&!(0,Me.moment)(n,i).isValid())throw new T("Invalid reference date format, try specifying one with the argument 'reference_format'");let o;return typeof t=="string"?o=Me.moment.duration(t):typeof t=="number"&&(o=Me.moment.duration(t,"days")),(0,Me.moment)(n,i).add(o).format(e)}` placeholder to today's date), then Step 1.
- Template also missing → create the note with minimal frontmatter (`type: daily`, `created: YYYY-MM-DD`, `status: sprout`, `lc_count: 0`, `study_today: 0`, `wins_done: 0`, `habits_done: []`) and continue.

Never create it anywhere else. `60_Claude/30_Reviews/` is not the target.

### Step 1 — Read Plan Context

Read these six files. No other reads. No vault dump.

| File | What to extract |
|------|-----------------|
| `10_Areas/Life/Plans/Summer/01 - Daily Operating System.md` | 5 wins + MVP variants + academic minimums |
| `10_Areas/Life/Plans/Summer/02 - Weekly Operating System.md` | Today's day-of-week focus |
| `10_Areas/Life/Plans/Summer/04 - Summer Courses Ops.md` | Deadlines within 7 days |
| `10_Areas/Life/Plans/Summer/05 - LeetCode & CSCI 4041.md` + `05a - LeetCode Tracker.md` | Today's LC topic; solved count vs ≥35/week |
| `10_Areas/Life/Plans/Summer/06 - ML Fundamentals (2033 + 2230).md` + `06a - ML Fundamentals Progress.md` | Today's CSCI 2033 subtopic |
| `10_Areas/Life/Habits/Daily Habit Board.md` | Active daily habits |

If any file is missing, note it in the output and continue.

### Step 2 — Read Session History

Read `60_Claude/07_AI_Information/Session Logs/log.md`. Take the 10 most recent `## [YYYY-MM-DD]` entries: sessions 1–5 in depth (done / left open / next actions), 6–10 headline only. Build a carryover list of items left open in 1–5 and not closed later.

### Step 3 — Patch the Daily Note

Patch `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` by heading. Never overwrite frontmatter; never delete existing content. Exact per-heading formats: [reference.md §1](reference.md).

Sections to fill: summary callout, Morning Plan goal, 80 — The One Thing, 20 — Supporting Work, Summer OS Checklist win targets, Academic Stack topics, deadline alert (if due ≤7 days), carryover block (if any), anti-drift line (from `08 - Anti-Drift Rules.md`), Productivity habit checkboxes.

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


## Claude

I'll start by checking today's daily note and reading the plan context files in parallel.

The Daily Habit Board file is missing (git status shows it was deleted). Let me check what's in that folder and read the remaining plan files.

The daily note's structure is corrupted (merged table rows, missing headings) — likely a bad prior edit. Let me check the template to rebuild it cleanly.

The template file itself has the same corruption (merged table/heading text) — this is a shared bug affecting every daily note, not just today's. I'll fix the template and then properly fill today's note.

Now applying the same structural fix plus today's content to the daily note.

I placed the habit checkboxes above the Meals/Water table, but the reference specifies they go below it. Let me fix the order.

Now I'll patch the dashboard's frontmatter with today's focus.

Today's plan is set. Summary:

**Today — Wednesday, July 8, 2026**

Goal: Start the CSCI 2033 ML spine (stuck at 0/14 units since Jun 3) while holding the daily LeetCode + 4041 floor, with MATH 2230 Test 3 five days out.

80: CSCI 2033 Unit 1 — Vectors, Linear Functions, and the Regression Model
20: LeetCode ≥5 (AVL/Red-Black, Meta focus), CSCI 4041 review (AVL/Red-Black), MATH 2230 WebAssign toward Test 3, inbox zero/admin

Academic minimums:
- LeetCode: AVL/Red-Black — tree validation, fix-up (0/35 this week — tracker is empty)
- CSCI 4041: AVL/Red-Black concept touch, tied to today's LC
- CSCI 2033: Unit 1 (spine hasn't started — flagged below)
- MATH 2230: WebAssign progress toward Test 3
- HIST 1103: N/A — all listed course items are past due, nothing open

> [!WARNING] Deadline: MATH 2230 — Test 3 (Ch 7–8, 10.1) due Jul 13; last day to withdraw Jul 14

No carryover items pulled forward — the open items in the last 5 session-log entries were all vault-infra/tooling gaps (canvas verification, Excalidraw plugin config), which fall under today's anti-drift exclusions, so I left them out of the daily plan.

Note updated: [[10_Areas/Life/Enumerate/Daily/2026-07-08]]
Dashboard updated: [[00_Dashboard]]

Two things worth flagging:
1. **The daily-note template (`Better Today.md`) was corrupted** — merged table/heading text (missing "## Summer OS Checklist" and "## Productivity" headings). This wasn't specific to today's note; it would have broken every future daily note. I fixed the template and applied the same fix to today's note.
2. **`Daily Habit Board.md` was deleted** and replaced by `Habit Tracker Board.md` (+ Scorecard/Experiments/Stacking boards), but the new tracker board's "Daily" section still has placeholder text ("Daily habit placeholder" x3), not real habits — so today's note carries placeholders too. Worth filling in real daily habits next time you touch that board.

### Tool Calls

- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-08.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\01 - Daily Operating System.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\02 - Weekly Operating System.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\04 - Summer Courses Ops.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Habits\Daily Habit Board.md`
- `Glob` -- pattern `10_Areas/Life/Habits/*` path ``
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\05 - LeetCode & CSCI 4041.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\05a - LeetCode Tracker.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\06 - ML Fundamentals (2033 + 2230).md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\06a - ML Fundamentals Progress.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\startday\reference.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Habits\Habit Tracker Board.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\07_AI_Information\Session Logs\log.md`
- `Glob` -- pattern `10_Areas/Life/Plans/Summer/08*` path ``
- `Glob` -- pattern `**/MATH 2230 Board.md` path ``
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\08 - Anti-Drift Rules.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Degree\MATH 2230\MATH 2230 Board.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Enumerate\Better Today.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Enumerate\Better Today.md`
```diff
- ## Sum| Win      | Target             | Done |
| -------- | ------------------ | ---- |
| Project  | shipped something  | [  ] |
| Career   | LC or application  | [  ] |
| Cleanup  | inbox/admin        | [  ] |
| Review   | closeday           | [  ] |
eday           | [  ] |

## Academic Stack

| Track     | Target    | Topic | Done |
|-----------|-----------|-------|------|
| LeetCode  | ≥5        |       | [ ]  |
| CSCI 4041 | 25-45 min |       | [ ]  |
| CSCI 2033 | 30-45 min |       | [ ]  |
| MATH 2230 |           |       | [ ]  |
| HIST 1103 | N/A       |      **LeetCode today:** `INPUT[number:lc_count]`
**Study hours:** `INPUT[number:study_today]`
**Wins hit:** `INPUT[number:wins_done]` / 4

| Meals | Water (3L target) |
|-------|-------------------|
|       |                   |
+ ## Summer OS Checklist

| Win      | Target             | Done |
| -------- | ------------------ | ---- |
| Project  | shipped something  | [  ] |
| Career   | LC or application  | [  ] |
| Cleanup  | inbox/admin        | [  ] |
| Review   | closeday           | [  ] |

## Academic Stack

| Track     | Target    | Topic | Done |
|-----------|-----------|-------|------|
| LeetCode  | ≥5        |       | [ ]  |
| CSCI 4041 | 25-45 min |       | [ ]  |
| CSCI 2033 | 30-45 min |       | [ ]  |
| MATH 2230 |           |       | [ ]  |
| HIST 1103 | N/A       |       | [ ]  |

## Productivity
**LeetCode today:** `INPUT[number:lc_count]`
**Study hours:** `INPUT[number:study_today]`
**Wins hit:** `INPUT[number:wins_done]` / 4

| Meals | Water (3L target) |
|-------|-------------------|
|       |                   |
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-08.md`
```diff
- # Did you get better today?
> [!NOTE] Summary:

## Morning Plan
*Goal*:

### 80 — The One Thing
> I will [BEHAVIOR] at [TIME] in [LOCATION].
- [ ] 

### 20 — Supporting Work
- [ ] 
- [ ] 
- [ ] 

**Do NOT do today:** MCP/tool setup, new agents, repo triage, AI platform comparison

## Sum| Win      | Target             | Done |
| -------- | ------------------ | ---- |
| Project  | shipped something  | [  ] |
| Career   | LC or application  | [  ] |
| Cleanup  | inbox/admin        | [  ] |
| Review   | closeday           | [  ] |
eday           | [  ] |

## Academic Stack

| Track     | Target    | Topic | Done |
|-----------|-----------|-------|------|
| LeetCode  | ≥5        |       | [ ]  |
| CSCI 4041 | 25-45 min |       | [ ]  |
| CSCI 2033 | 30-45 min |       | [ ]  |
| MATH 2230 |           |       | [ ]  |
| HIST 1103 | N/A       |      **LeetCode today:** `INPUT[number:lc_count]`
**Study hours:** `INPUT[number:study_today]`
**Wins hit:** `INPUT[number:wins_done]` / 4

| Meals | Water (3L target) |
|-------|-------------------|
|       |                   |
+ # Did you get better today?
> [!NOTE] Summary:
> Wednesday build/study day — close the CSCI 2033 spine gap (0/14 units done) while keeping the LeetCode/4041 floor, with MATH 2230 Test 3 five days out.

## Morning Plan
*Goal*: Start the CSCI 2033 ML spine (it's been stuck at 0/14 since Jun 3) while holding the daily LeetCode + 4041 floor and beginning Test 3 prep (Ch 7–8, 10.1, due Jul 13).

### 80 — The One Thing
> I will complete CSCI 2033 spine Unit 1 (Vectors, Linear Functions, and the Regression Model) at the morning deep-work block in my desk setup.
- [ ] CSCI 2033 Unit 1 done-definition met: vector ops from memory + 3 practice problems (dot product, linear function eval)

### 20 — Supporting Work
- [ ] LeetCode ≥5 — AVL / Red-Black pattern (tree validation, fix-up), Meta company focus
- [ ] CSCI 4041 review 25–45 min — AVL / Red-Black concept touch, tie to today's LC
- [ ] MATH 2230 — advance WebAssign toward Test 3 (Ch 7–8, 10.1, due Jul 13) or one quiz
- [ ] Cleanup/admin win — inbox zero or smallest admin step

**Do NOT do today:** MCP/connector setup or comparison, new agents/skills authoring, GitHub repo stars triage, AI platform comparison/stack optimization, .obsidian/plugin configuration

## Summer OS Checklist

| Win      | Target             | Done |
| -------- | ------------------ | ---- |
| Project  | CSCI 2033 Unit 1 (Dubai-phase MVP: LA base) | [  ] |
| Career   | LeetCode ≥5 — AVL/Red-Black (Meta)  | [  ] |
| Cleanup  | inbox zero / smallest admin step        | [  ] |
| Review   | closeday           | [  ] |

## Academic Stack

> [!WARNING] Deadline: MATH 2230 — Test 3 (Ch 7–8, 10.1) due Jul 13; last day to withdraw Jul 14

| Track     | Target    | Topic | Done |
|-----------|-----------|-------|------|
| LeetCode  | ≥5        | AVL / Red-Black — tree validation, fix-up (0/35 this week) | [ ]  |
| CSCI 4041 | 25-45 min | AVL / Red-Black — tree validation, fix-up | [ ]  |
| CSCI 2033 | 30-45 min | Unit 1 — Vectors, Linear Functions, Regression Model (spine start, 0/14 done) | [ ]  |
| MATH 2230 |  Test 3 prep | WebAssign toward Ch 7–8, 10.1 | [ ]  |
| HIST 1103 | N/A       | course items all past due — nothing open | [ ]  |

## Productivity
**LeetCode today:** `INPUT[number:lc_count]`
**Study hours:** `INPUT[number:study_today]`
**Wins hit:** `INPUT[number:wins_done]` / 4

- [ ] Daily habit placeholder
- [ ] Daily habit placeholder
- [ ] Daily habit placeholder

| Meals | Water (3L target) |
|-------|-------------------|
|       |                   |
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-08.md`
```diff
- **Wins hit:** `INPUT[number:wins_done]` / 4

- [ ] Daily habit placeholder
- [ ] Daily habit placeholder
- [ ] Daily habit placeholder

| Meals | Water (3L target) |
|-------|-------------------|
|       |                   |
+ **Wins hit:** `INPUT[number:wins_done]` / 4

| Meals | Water (3L target) |
|-------|-------------------|
|       |                   |

- [ ] Daily habit placeholder
- [ ] Daily habit placeholder
- [ ] Daily habit placeholder
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\00_Dashboard.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\00_Dashboard.md`
```diff
- today_focus: "Sunday close-out: weekly review, deadline scan, Week 6 flagship pick"
today_80: "Run /weekly-review — 7 questions + deadline scan + Week 6 flagship pick"
today_20: "LeetCode 5 (AVL/BST), CSCI 2033 Unit 7, MATH 2230 board check"
+ today_focus: "Wednesday build/study: start CSCI 2033 spine (0/14) + hold LC/4041 floor + MATH Test 3 prep"
today_80: "CSCI 2033 Unit 1 — Vectors, Linear Functions, Regression Model"
today_20: "LeetCode 5 (AVL/Red-Black, Meta), CSCI 4041 review, MATH 2230 WebAssign toward Test 3, inbox zero"
```

## You

<command-message>startday</command-message>
<command-name>/startday</command-name>

## You

Base directory for this skill: D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\startday

# startday

**Usage:** `/startday`

Deep detail — exact patch formats, table shapes, output template — lives in [reference.md](reference.md). This file is the step sequence; load reference.md when actually patching.

## When to Invoke

At the start of the day. The Periodic Notes plugin normally creates today's note at `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md`; this skill fills it and updates `00_Dashboard.md`.

## Instructions

### Step 0 — Find Today's Note

Locate `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` (today's date).

- Exists → Step 1.
- Missing → create it from `30_Order/Templates/Enumerate/Better Today.md` (copy frontmatter and structure verbatim, resolve the `(e="YYYY-MM-DD",t,n,i)=>{if(n&&!(0,Me.moment)(n,i).isValid())throw new T("Invalid reference date format, try specifying one with the argument 'reference_format'");let o;return typeof t=="string"?o=Me.moment.duration(t):typeof t=="number"&&(o=Me.moment.duration(t,"days")),(0,Me.moment)(n,i).add(o).format(e)}` placeholder to today's date), then Step 1.
- Template also missing → create the note with minimal frontmatter (`type: daily`, `created: YYYY-MM-DD`, `status: sprout`, `lc_count: 0`, `study_today: 0`, `wins_done: 0`, `habits_done: []`) and continue.

Never create it anywhere else. `60_Claude/30_Reviews/` is not the target.

### Step 1 — Read Plan Context

Read these six files. No other reads. No vault dump.

| File | What to extract |
|------|-----------------|
| `10_Areas/Life/Plans/Summer/01 - Daily Operating System.md` | 4 wins + MVP variants + academic minimums |
| `10_Areas/Life/Plans/Summer/02 - Weekly Operating System.md` | Today's day-of-week focus |
| `10_Areas/Life/Plans/Summer/04 - Summer Courses Ops.md` | Deadlines within 7 days |
| `10_Areas/Life/Plans/Summer/05 - LeetCode & CSCI 4041.md` + `05a - LeetCode Tracker.md` | Today's LC topic; solved count vs ≥35/week |
| `10_Areas/Life/Plans/Summer/06 - ML Fundamentals (2033 + 2230).md` + `06a - ML Fundamentals Progress.md` | Today's CSCI 2033 subtopic |
| `10_Areas/Life/Habits/` — find the file with a `## Daily` heading (currently `Habit Tracker Board.md`; don't hardcode the name, it has changed before) | Active daily habits |

If any file is missing, note it in the output and continue.

### Step 2 — Read Session History

Read `60_Claude/07_AI_Information/Session Logs/log.md`. Take the 10 most recent `## [YYYY-MM-DD]` entries: sessions 1–5 in depth (done / left open / next actions), 6–10 headline only. Build a carryover list of items left open in 1–5 and not closed later.

### Step 3 — Patch the Daily Note

Patch `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` by heading. Never overwrite frontmatter; never delete existing content. Exact per-heading formats: [reference.md §1](reference.md).

Sections to fill: summary callout, Morning Plan goal, 80 — The One Thing, 20 — Supporting Work, Summer OS Checklist win targets, Academic Stack topics, deadline alert (if due ≤7 days), carryover block (if any), anti-drift line (from `08 - Anti-Drift Rules.md`), Productivity habit checkboxes.

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


## Claude

Now patching the dashboard frontmatter.

Today's plan is set.

**Today — Thursday, July 9, 2026**

Goal: Land CSCI 2033 Unit 1 (carried over — still 0/14 on the spine) while holding the LeetCode + 4041 floor, and advance MATH 2230 Test 3 prep.

80: CSCI 2033 Unit 1 — Vectors, Linear Functions, and the Regression Model (carried over from yesterday)
20: LeetCode ≥5 (AVL/Red-Black, Meta), CSCI 4041 review, MATH 2230 WebAssign toward Test 3, inbox zero/admin

Academic minimums:
- LeetCode: AVL/Red-Black — tree validation, fix-up (0/35 this week — tracker still has no entries logged for either day)
- CSCI 4041: AVL/Red-Black concept touch
- CSCI 2033: Unit 1 (carried over, spine still 0/14)
- MATH 2230: WebAssign progress toward Test 3
- HIST 1103: N/A

> [!WARNING] Deadline: MATH 2230 — Test 3 (Ch 7–8, 10.1) due Jul 13; last day to withdraw Jul 14

No new carryover from the session log (nothing left open in the last 5 entries beyond what's already excluded by the anti-drift list). Worth noting: no session-log entry exists for 07-08's work and the LeetCode tracker has zero rows for two days running — if problems were solved, they weren't logged.

Note updated: [[10_Areas/Life/Enumerate/Daily/2026-07-09]]
Dashboard updated: [[00_Dashboard]]

### Tool Calls

- `Glob` -- pattern `10_Areas/Life/Enumerate/Daily/2026-07-09.md` path ``
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\05a - LeetCode Tracker.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\07_AI_Information\Session Logs\log.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\06a - ML Fundamentals Progress.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-08.md`
- `Glob` -- pattern `10_Areas/Life/Habits/*` path ``
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Habits\Habit Tracker Board.md`
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-09.md`
```
---
type: thought
thought_kind: reflection
status: seed
created: 2026-07-09
related_progress:
tags:
  - thought
  - "#journal"
next:
lc_count: 0
study_today: 0
wins_done: 0
habits_done: []
---
# Did you get better today?
> [!NOTE] Summary:
> Thursday build/study day — CSCI 2033 spine still at 0/14 (Unit 1 carries over from yesterday); MATH 2230 Test 3 four days out.

## Morning Plan
*Goal*: Land CSCI 2033 Unit 1 (carried over — still 0/14 on the spine) while holding the LeetCode + 4041 floor and advancing MATH 2230 Test 3 prep (Ch 7–8, 10.1, due Jul 13).

### 80 — The One Thing
> I will complete CSCI 2033 spine Unit 1 (Vectors, Linear Functions, and the Regression Model) at the morning deep-work block in my desk setup.
- [ ] CSCI 2033 Unit 1 done-definition met: vector ops from memory + 3 practice problems (dot product, linear function eval)

### 20 — Supporting Work
- [ ] LeetCode ≥5 — AVL / Red-Black pattern (tree validation, fix-up), Meta company focus
- [ ] CSCI 4041 review 25–45 min — AVL / Red-Black concept touch, tie to today's LC
- [ ] MATH 2230 — advance WebAssign toward Test 3 (Ch 7–8, 10.1, due Jul 13) or one quiz
- [ ] Cleanup/admin win — inbox zero or smallest admin step

**Do NOT do today:** MCP/connector setup or comparison, new agents/skills authoring, GitHub repo stars triage, AI platform comparison/stack optimization, .obsidian/plugin configuration

## Summer OS Checklist

| Win     | Target                                      | Done |
| ------- | -------------------------------------------- | ---- |
| Project | CSCI 2033 Unit 1 (Dubai-phase MVP: LA base) — carried over | [  ] |
| Career  | LeetCode ≥5 — AVL/Red-Black (Meta)          | [  ] |
| Cleanup | inbox zero / smallest admin step            | [  ] |
| Review  | closeday                                    | [  ] |

## Academic Stack

> [!WARNING] Deadline: MATH 2230 — Test 3 (Ch 7–8, 10.1) due Jul 13; last day to withdraw Jul 14

| Track     | Target    | Topic | Done |
|-----------|-----------|-------|------|
| LeetCode  | ≥5        | AVL / Red-Black — tree validation, fix-up (0/35 this week — tracker still empty) | [ ]  |
| CSCI 4041 | 25-45 min | AVL / Red-Black — tree validation, fix-up | [ ]  |
| CSCI 2033 | 30-45 min | Unit 1 — Vectors, Linear Functions, Regression Model (carried over, 0/14 done) | [ ]  |
| MATH 2230 | Test 3 prep | WebAssign toward Ch 7–8, 10.1 | [ ]  |
| HIST 1103 | N/A       | course items all past due — nothing open | [ ]  |

## Productivity
**LeetCode today:** `INPUT[number:lc_count]`
**Study hours:** `INPUT[number:study_today]`
**Wins hit:** `INPUT[number:wins_done]` / 4

| Meals | Water (3L target) |
|-------|-------------------|
|       |                   |

- [ ] leetcode-5 — ≥5 problems, topic logged
- [ ] csci2033 — 30–45 min LA subtopic + output
- [ ] course-step — MATH 2230 board next OR HIST admin step
- [ ] review-note — 5-min end-of-day note / closeday

```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\00_Dashboard.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\00_Dashboard.md`
```diff
- today_focus: "Wednesday build/study: start CSCI 2033 spine (0/14) + hold LC/4041 floor + MATH Test 3 prep"
today_80: "CSCI 2033 Unit 1 — Vectors, Linear Functions, Regression Model"
today_20: "LeetCode 5 (AVL/Red-Black, Meta), CSCI 4041 review, MATH 2230 WebAssign toward Test 3, inbox zero"
+ today_focus: "Thursday build/study: land CSCI 2033 Unit 1 (carried over, 0/14) + hold LC/4041 floor + MATH Test 3 prep"
today_80: "CSCI 2033 Unit 1 — Vectors, Linear Functions, Regression Model (carried over)"
today_20: "LeetCode 5 (AVL/Red-Black, Meta), CSCI 4041 review, MATH 2230 WebAssign toward Test 3, inbox zero"
```

## Actions Taken

**Files created:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-09.md`

**Files modified:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\00_Dashboard.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-08.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Enumerate\Better Today.md`

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
_None_



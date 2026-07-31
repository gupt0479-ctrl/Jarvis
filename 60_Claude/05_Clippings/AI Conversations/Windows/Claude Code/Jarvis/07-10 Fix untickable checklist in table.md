---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: windows
title: "Fix untickable checklist in table"
started_at: 2026-07-10T10:30:16
ended_at: 2026-07-10T17:37:57
exported_at: 2026-07-31T21:03:24
duration_minutes: 427.7
project: Jarvis
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
session_id: d7bbfeb1-050a-4bd7-8ef5-8fede596f5ef
status: raw
turn_count: 5
tools_used:
  Bash: 2
  Edit: 5
  Grep: 8
  mcp__jarvis__vault_patch: 3
  mcp__jarvis__vault_read: 2
  Read: 20
  Skill: 1
  ToolSearch: 1
tokens:
  input: 44264
  output: 53347
  cache_creation: 530126
  cache_read: 5961761
  total: 6589498
cost_usd: 3.934854
model:
  - "claude-sonnet-5"
files_touched:
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\.claude\\skills\\closeday\\reference.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\.claude\\skills\\closeday\\SKILL.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\.claude\\skills\\startday\\reference.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\.claude\\skills\\startday\\SKILL.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Enumerate\\Daily\\2026-07-08.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Enumerate\\Daily\\2026-07-09.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Enumerate\\Daily\\2026-07-10.md"
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

# Fix untickable checklist in table

## You

The checklist is not tickable and that's annoying. Inside the table it is not able to from a task: [Image #1]. Fix this issue first, then /startday

[image attached]

## You

[Image: source: C:\Users\ANANTG~1\AppData\Local\Temp\[REDACTED].png]

## Claude

I found the cause: the "Done" columns use plain `[ ]` text inside a table cell, which Obsidian never renders as an interactive checkbox (task checkboxes only work on standalone list lines, not inside tables). The vault already has the Meta Bind plugin installed (it's used for `INPUT[number:lc_count]` elsewhere in the same note), so I'll swap those cells to `INPUT[toggle:...]` bound to frontmatter fields — that gives you an actual clickable/tickable control that persists state.

I'll fix the template (for future days) and today's note.

Now the same fix for today's note.

Checklist fixed. Now running `/startday`.

### Tool Calls

- `Grep` -- pattern `Summer OS Checklist` path ``
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-10.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Enumerate\Better Today.md`
- `Bash` -- `ls "D:/Users/_Anant/10_Areas/Documents/Jarvis/.obsidian/plugins" 2>/dev/null`
```
code-styler
copilot
dataview
excalibrain
file-explorer-plus
homepage
lazy-plugins
lean-terminal
multi-column-markdown
ninja-cursor
obsidian-excalidraw-plugin
obsidian-git
obsidian-hover-editor
obsidian-kanban
obsidian-latex-suite
obsidian-local-rest-api
obsidian-meta-bind-plugin
obsidian-spaced-repetition
obsidian-style-settings
obsidian-tasks-plugin
omnisearch
periodic-notes
quickadd
recent-files-obsidian
templater-obsidian
url-into-selection
workspaces-plus
```
- `Grep` -- pattern `INPUT\[toggle` path ``
- `Grep` -- pattern `Summer OS Checklist|Academic Stack|Done` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\startday`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\startday\reference.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\startday\SKILL.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\closeday\SKILL.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\closeday\reference.md`
- `Grep` -- pattern `"toggle"|InputFieldType\.TOGGLE|toggleGroup|multiSelect` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\.obsidian\plugins\obsidian-meta-bind-plugin\main.js`
- `Grep` -- pattern `Toggle` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\.obsidian\plugins\obsidian-meta-bind-plugin\main.js`
- `Grep` -- pattern `checkbox|Checkbox` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\.obsidian\plugins\obsidian-meta-bind-plugin\main.js`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Enumerate\Better Today.md`
```diff
- lc_count: 0
study_today: 0
wins_done: 0
habits_done: []
---
+ lc_count: 0
study_today: 0
wins_done: 0
habits_done: []
win_project: false
win_career: false
win_cleanup: false
win_review: false
ac_leetcode: false
ac_csci4041: false
ac_csci2033: false
ac_math2230: false
ac_hist1103: false
---
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Enumerate\Better Today.md`
```diff
- | Win      | Target             | Done |
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
+ | Win      | Target             | Done |
| -------- | ------------------ | ---- |
| Project  | shipped something  | `INPUT[toggle:win_project]` |
| Career   | LC or application  | `INPUT[toggle:win_career]` |
| Cleanup  | inbox/admin        | `INPUT[toggle:win_cleanup]` |
| Review   | closeday           | `INPUT[toggle:win_review]` |

## Academic Stack

| Track     | Target    | Topic | Done |
|-----------|-----------|-------|------|
| LeetCode  | ≥5        |       | `INPUT[toggle:ac_leetcode]` |
| CSCI 4041 | 25-45 min |       | `INPUT[toggle:ac_csci4041]` |
| CSCI 2033 | 30-45 min |       | `INPUT[toggle:ac_csci2033]` |
| MATH 2230 |           |       | `INPUT[toggle:ac_math2230]` |
| HIST 1103 | N/A       |       | `INPUT[toggle:ac_hist1103]` |
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-10.md`
```diff
- lc_count: 0
study_today: 0
wins_done: 0
habits_done: []
---
+ lc_count: 0
study_today: 0
wins_done: 0
habits_done: []
win_project: false
win_career: false
win_cleanup: false
win_review: false
ac_leetcode: false
ac_csci4041: false
ac_csci2033: false
ac_math2230: false
ac_hist1103: false
---
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-10.md`
```diff
- | Win      | Target             | Done |
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
+ | Win      | Target             | Done |
| -------- | ------------------ | ---- |
| Project  | shipped something  | `INPUT[toggle:win_project]` |
| Career   | LC or application  | `INPUT[toggle:win_career]` |
| Cleanup  | inbox/admin        | `INPUT[toggle:win_cleanup]` |
| Review   | closeday           | `INPUT[toggle:win_review]` |

## Academic Stack

| Track     | Target    | Topic | Done |
|-----------|-----------|-------|------|
| LeetCode  | ≥5        |       | `INPUT[toggle:ac_leetcode]` |
| CSCI 4041 | 25-45 min |       | `INPUT[toggle:ac_csci4041]` |
| CSCI 2033 | 30-45 min |       | `INPUT[toggle:ac_csci2033]` |
| MATH 2230 |           |       | `INPUT[toggle:ac_math2230]` |
| HIST 1103 | N/A       |       | `INPUT[toggle:ac_hist1103]` |
```
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

Now step 2 — session history for carryover items.

Now step 3b — patch the dashboard frontmatter.

Now patching the three dashboard frontmatter fields.

Dashboard patched. Both tasks are done.

**Checklist fix:** the "Done" columns in `Summer OS Checklist` and `Academic Stack` used plain `[ ]` text inside table cells — Obsidian never renders table-cell text as a real task checkbox. Replaced with Meta Bind `INPUT[toggle:...]` fields bound to new frontmatter booleans (`win_project`, `win_career`, `win_cleanup`, `win_review`, `ac_leetcode`, `ac_csci4041`, `ac_csci2033`, `ac_math2230`, `ac_hist1103`). These are real interactive toggles that persist state to the note — fixed in both today's note and the template so future daily notes inherit it.

**`/startday` for 2026-07-10:**
- **Flag:** neither 07-08 nor 07-09 got a `/closeday` — both plans (CSCI 2033 Unit 1, LeetCode floor) sat unexecuted for two days straight. Per the vault's own anti-drift rule ("Never Miss Twice"), today is the third rep.
- **80 — The One Thing:** MATH 2230 Test 3 (Ch 7–8, 10.1) is now only **3 days out** (Jul 13) with zero prep logged — shifted priority there for a first prep session, ahead of the stalled CSCI 2033 carryover.
- **20 — Supporting Work:** LeetCode ≥5 (corrected topic to Week 1 — Sorting/Time Complexity/Google, matching the actual zero-progress state; prior two days had it mismatched to AVL/Red-Black, a Week 5–6 topic), CSCI 4041 review, CSCI 2033 Unit 1 (still carried), cleanup/admin.
- **Deadline alert** added: MATH 2230 Test 3 due Jul 13, withdraw deadline Jul 14.
- **Carryover block** added for CSCI 2033 Unit 1 and the LeetCode floor.
- Dashboard (`00_Dashboard.md`) frontmatter updated: `today_focus`, `today_80`, `today_20`.

Note updated: [[10_Areas/Life/Enumerate/Daily/2026-07-10]]
Dashboard updated: [[00_Dashboard]]

### Tool Calls

- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\01 - Daily Operating System.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\02 - Weekly Operating System.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\04 - Summer Courses Ops.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\05 - LeetCode & CSCI 4041.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\05a - LeetCode Tracker.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\06 - ML Fundamentals (2033 + 2230).md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\06a - ML Fundamentals Progress.md`
- `Grep` -- pattern `^next:` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Degree\MATH 2230`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Degree\MATH 2230\MATH 2230 Board.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Habits\Habit Tracker Board.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\07_AI_Information\Session Logs\log.md`
- `Bash` -- `wc -l "D:/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/07_AI_Information/Session Logs/log.md"`
```
1146 D:/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/07_AI_Information/Session Logs/log.md
```
- `Grep` -- pattern `## \[2026-07-(06|07|08|09|10)\]` path `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\07_AI_Information\Session Logs\log.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\07_AI_Information\Session Logs\log.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-09.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-08.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Summer\08 - Anti-Drift Rules.md`
- `ToolSearch` -- `{"query":"select:mcp__jarvis__vault_patch,mcp__jarvis__vault_read","max_results":5}`
- `mcp__jarvis__vault_read` -- `{"path":"10_Areas/Life/Enumerate/Daily/2026-07-10.md"}`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-10.md`
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

## Summer OS Checklist

| Win      | Target             | Done |
| -------- | ------------------ | ---- |
| Project  | shipped something  | `INPUT[toggle:win_project]` |
| Career   | LC or application  | `INPUT[toggle:win_career]` |
| Cleanup  | inbox/admin        | `INPUT[toggle:win_cleanup]` |
| Review   | closeday           | `INPUT[toggle:win_review]` |

## Academic Stack

| Track     | Target    | Topic | Done |
|-----------|-----------|-------|------|
| LeetCode  | ≥5        |       | `INPUT[toggle:ac_leetcode]` |
| CSCI 4041 | 25-45 min |       | `INPUT[toggle:ac_csci4041]` |
| CSCI 2033 | 30-45 min |       | `INPUT[toggle:ac_csci2033]` |
| MATH 2230 |           |       | `INPUT[toggle:ac_math2230]` |
| HIST 1103 | N/A       |       | `INPUT[toggle:ac_hist1103]` |

## Productivity
**LeetCode today:** `INPUT[number:lc_count]`
**Study hours:** `INPUT[number:study_today]`
**Wins hit:** `INPUT[number:wins_done]` / 4

| Meals | Water (3L target) |
|-------|-------------------|
|       |                   |
+ # Did you get better today?
> [!NOTE] Summary:
> Friday build/study day — MATH 2230 Test 3 three days out with zero prep logged; CSCI 2033 spine still 0/14 after two unclosed days (Jul 8, Jul 9 both had no closeday). Never Miss Twice is live — this is the third rep.

## Morning Plan
*Goal*: Run MATH 2230 Test 3 prep session 1 (Ch 7–8, 10.1, due Jul 13) since no prep exists yet, while finally landing CSCI 2033 Unit 1 (stuck at 0/14 since Jun 3) and holding the LeetCode + 4041 floor.

### 80 — The One Thing
> I will run MATH 2230 Test 3 prep session 1 (Ch 7–8, 10.1) at the morning deep-work block in my desk setup.
- [ ] Test 3 prep session 1 done: WebAssign/practice problems from Ch 7–8 + 10.1 attempted, weak spots flagged for session 2 before Jul 13

### 20 — Supporting Work
- [ ] LeetCode ≥5 — Sorting Algorithms / Time Complexity (Week 1 topic: insertion/merge, asymptotics), Google focus — tracker still at 0 all summer
- [ ] CSCI 4041 review 25–45 min — Sorting Algorithms / Time Complexity concept touch, tie to today's LC
- [ ] CSCI 2033 Unit 1 (Vectors, Linear Functions, Regression Model) — carried over a 3rd day, still 0/14
- [ ] Cleanup/admin win — inbox zero or smallest admin step

**Do NOT do today:** MCP/connector setup or comparison, new agents/skills authoring, GitHub repo stars triage, AI platform comparison/stack optimization, .obsidian/plugin configuration

## Summer OS Checklist

| Win      | Target             | Done |
| -------- | ------------------ | ---- |
| Project  | MATH 2230 Test 3 prep session 1 (Ch 7–8, 10.1) | `INPUT[toggle:win_project]` |
| Career   | LeetCode ≥5 — Sorting/Time Complexity (Google) | `INPUT[toggle:win_career]` |
| Cleanup  | inbox zero / smallest admin step | `INPUT[toggle:win_cleanup]` |
| Review   | closeday           | `INPUT[toggle:win_review]` |

## Academic Stack

> [!WARNING] Deadline: MATH 2230 — Test 3 (Ch 7–8, 10.1) due Jul 13 (3 days); last day to withdraw Jul 14

| Track     | Target    | Topic | Done |
|-----------|-----------|-------|------|
| LeetCode  | ≥5        | Sorting Algorithms / Time Complexity — insertion/merge, asymptotics (0/35 this week — tracker still empty) | `INPUT[toggle:ac_leetcode]` |
| CSCI 4041 | 25-45 min | Sorting Algorithms / Time Complexity concept touch | `INPUT[toggle:ac_csci4041]` |
| CSCI 2033 | 30-45 min | Unit 1 — Vectors, Linear Functions, Regression Model (carried over 3rd day, 0/14 done) | `INPUT[toggle:ac_csci2033]` |
| MATH 2230 | Test 3 prep | Session 1 — Ch 7–8, 10.1 | `INPUT[toggle:ac_math2230]` |
| HIST 1103 | N/A       | course items all past due — nothing open | `INPUT[toggle:ac_hist1103]` |

## Carryover from Previous Sessions
- [ ] CSCI 2033 Unit 1 (Vectors, Linear Functions, Regression Model) — carried from 2026-07-08 and 2026-07-09, still 0/14, neither day was closed out
- [ ] LeetCode ≥5/day — tracker empty all summer (0/35 this week), floor never logged as met

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
- `mcp__jarvis__vault_read` -- `{"path":"00_Dashboard.md"}`
- `mcp__jarvis__vault_patch` -- `{"path":"00_Dashboard.md","targetType":"frontmatter","target":"today_focus","operation":"replace","contentType":"application/json","content":"\"Friday: MATH 2230 Test 3 prep session 1 (3 days out, zero prep) + land CSCI 2033 Unit 1 (0/14, carried 3rd day) + hold LC/4041 floor\""}`
- `mcp__jarvis__vault_patch` -- `{"path":"00_Dashboard.md","targetType":"frontmatter","target":"today_80","operation":"replace","contentType":"application/json","content":"\"MATH 2230 Test 3 prep session 1 — Ch 7–8, 10.1\""}`
- `mcp__jarvis__vault_patch` -- `{"path":"00_Dashboard.md","targetType":"frontmatter","target":"today_20","operation":"replace","contentType":"application/json","content":"\"LeetCode 5 (Sorting/Time Complexity, Google), CSCI 4041 review, CSCI 2033 Unit 1 (carried), inbox zero\""}`

## Actions Taken

**Files created:**
_None_

**Files modified:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Enumerate\Daily\2026-07-10.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\Templates\Enumerate\Better Today.md`

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
- `ls "D:/Users/_Anant/10_Areas/Documents/Jarvis/.obsidian/plugins" 2>/dev/null`
- `wc -l "D:/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/07_AI_Information/Session Logs/log.md"`



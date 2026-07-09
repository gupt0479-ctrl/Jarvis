---
type: dashboard
status: tree
created: 2026-04-23
updated: 2026-07-04
tags:
  - dashboard
  - daily
cssclasses:
  - dashboard
today_focus: "Thursday build/study: land CSCI 2033 Unit 1 (carried over, 0/14) + hold LC/4041 floor + MATH Test 3 prep"
today_80: "CSCI 2033 Unit 1 — Vectors, Linear Functions, Regression Model (carried over)"
today_20: "LeetCode 5 (AVL/Red-Black, Meta), CSCI 4041 review, MATH 2230 WebAssign toward Test 3, inbox zero"
lc_today: 0
study_today: 0
wins_done: 0
notes:
  - "[[CLAUDE.md]]"
  - "[[AGENTS.md]]"
  - "[[Jarvis OS — North Star]]"
---
# Jarvis — `$= moment().format("dddd, D MMMM YYYY")`
> [!focus] CURRENT FOCUS
> **`INPUT[text:today_focus]`**
> `INPUT[text:today_80]`
> `INPUT[text:today_20]`
> *Patched by /startday · cleared by /closeday.*

=== start-multi-column: JarvisDash
```column-settings
Number of Columns: 2
Largest Column: left
Border: off
Shadow: off
```
## Today's Numbers
```dataviewjs
const curr = dv.current();
const lc = curr.lc_today ?? 0;
const wins = curr.wins_done ?? 0;
const study = curr.study_today ?? 0;
const lcClass = lc >= 5 ? 'green' : lc > 0 ? 'yellow' : '';
const winsClass = wins >= 5 ? 'green' : wins >= 3 ? 'yellow' : '';
const container = dv.el('div', '', {cls: 'stat-grid'});
container.innerHTML = `
  <div class="stat-tile ${lcClass}">
    <div class="stat-label">LeetCode Today</div>
    <div class="stat-value">${lc}</div>
    <div class="stat-delta ${lc >= 5 ? 'positive' : 'neutral'}">target ≥5</div>
  </div>
  <div class="stat-tile ${winsClass}">
    <div class="stat-label">5-Wins</div>
    <div class="stat-value">${wins}<span style="font-size:0.85rem;opacity:0.6">/5</span></div>
    <div class="stat-delta ${wins >= 5 ? 'positive' : wins >= 3 ? 'neutral' : 'negative'}">${wins >= 5 ? '✓ GREEN' : wins >= 3 ? 'in progress' : 'behind'}</div>
  </div>
  <div class="stat-tile">
    <div class="stat-label">Study Hours</div>
    <div class="stat-value">${study}h</div>
    <div class="stat-delta neutral">today</div>
  </div>
`;
```
## This Week
```dataviewjs
const folder = '"10_Areas/Life/Enumerate/Daily"';
const pages = dv.pages(folder).where(p => {
  if (!p.file.day) return false;
  const today = dv.date("today");
  const monday = today.minus({days: today.weekday - 1});
  return p.file.day >= monday && p.file.day <= today;
});
const lcTotal = pages.values.reduce((a,p) => a + (p.lc_count || 0), 0);
const studyTotal = pages.values.reduce((a,p) => a + (p.study_today || 0), 0);
const winsTotal = pages.values.reduce((a,p) => a + (p.wins_done || 0), 0);
const clippings = dv.pages('"60_Claude/10_Source_Summaries"')
  .where(p => {
    const monday = dv.date("today").minus({days: dv.date("today").weekday - 1});
    return p.file.ctime >= monday;
  }).length;
dv.paragraph(`**LC:** ${lcTotal}/35 · **Study:** ${studyTotal}h · **Wins:** ${winsTotal} · **Clippings this week:** ${clippings}`);
```
## Today's Priorities
```dataview
TASK
FROM "10_Areas/Life/Enumerate/Daily"
WHERE file.day = date(today) AND !completed
LIMIT 8
```
## Active Projects
```dataview
TABLE status, deadline, next, file.mtime AS "Updated"
FROM "20_Progress"
WHERE type = "project" AND status != "archived" AND status != "complete"
SORT deadline ASC
LIMIT 8
```
=== end-column ===
## Daily Drivers
```dataviewjs
const todayStr = dv.date("today").toFormat("yyyy-MM-dd");
const todayPage = dv.pages('"10_Areas/Life/Enumerate/Daily"')
  .where(p => p.file.name === todayStr).first();
const done = (todayPage && Array.isArray(todayPage.habits_done)) ? todayPage.habits_done.length : 0;
const total = 5;
const pct = Math.round((done / total) * 100);
const wrap = dv.el('div', '', {cls: 'progress-wrap'});
wrap.innerHTML = `
  <div class="progress-label">${done} / ${total} complete · ${pct}%</div>
  <div class="progress-bar-bg"><div class="progress-bar-fill" style="width:${pct}%"></div></div>
`;
```
> [!todo] Habits — check off in today's note
> - [ ] LeetCode ≥5
> - [ ] CSCI 2033 (30–45 min)
> - [ ] Course step (4041 / 2230 / 1103)
> - [ ] Review — run /closeday

## Internship Pipeline
```dataview
TABLE status, next
FROM "10_Areas/Career/Internships"
SORT file.mtime DESC
LIMIT 5
```
## Clippings Queue
```dataviewjs
const remaining = dv.pages('"60_Claude/05_Clippings"')
  .where(p => !p.file.name.includes("board") && !p.file.name.includes("README")).length;
dv.paragraph(`**${remaining}** items awaiting distillation`);
```
## Vault Health
```dataview
TABLE file.folder AS Folder, file.mtime AS "Updated"
FROM "10_Areas" OR "20_Progress" OR "40_Resources" OR "60_Claude"
WHERE !type OR !status
SORT file.mtime DESC
LIMIT 8
```
=== end-multi-column

---
**System:** [[CLAUDE.md]] · [[AGENTS.md]] · [[Jarvis OS — North Star]] · [[AI_CONTEXT]] · [[HUMAN_WRITING]]
**Claude OS:** [[Claude OS]] · [[20_Progress/AI/Claude OS Dashboard|Claude OS Dashboard]] · [[10_Areas/Excalidraw/Claude OS Map|OS Map]]
**AI:** [[10_Areas/AI/Claude Code|Claude Code]] · [[10_Areas/AI/Cursor|Cursor]] · [[10_Areas/AI/Kiro|Kiro]] · [[10_Areas/AI/Codex|Codex]]
**Daily OS:** [[10_Areas/Life/Plans/Summer/01 - Daily Operating System|Daily Operating System]] · personal, health, and finance tracking live in The Plan, not here

## 10_Areas Overview

What each area is for, and where it stands right now. This is an area-level field, not a daily one — don't touch it from `/startday` or `/closeday`; update it when an area's purpose or state materially changes.

| Area | Purpose | Current state |
|------|---------|----------------|
| [[10_Areas/Career/Engineer Edge Roadmap\|Career]] | Internship pipeline, freelancing, business-income tracking (`Career/Finance/`, scoped to project/business money only — no personal finance here) | Internship tracker + freelancing offer not yet defined; Finance folder empty until real income lands |
| [[10_Areas/Trading/Stocks Trading AI Hub\|Trading]] | TradingView project — treated as an engineering/evaluation build, not a promise to beat the market | Flagship candidate for the Bangalore ship loop; not started yet |
| [[10_Areas/AI/Claude Code\|AI]] | Reference notes for the AI tools actually in use (Claude Code, Cursor, Kiro, Codex) | Stable reference, low-churn |
| [[10_Areas/Life/Plans/Summer/01 - Daily Operating System\|Life]] | Execution only: Enumerate daily/weekly/monthly notes, Summer OS plans, operational habit boards, builder-identity Truths of Life. No personal-life content — that lives in The Plan. | Active — this is what `/startday` and `/closeday` read every day |
| Notes | Raw course-era captures (F'25, Files, PDFs) awaiting distillation or archive | Not actively worked — candidate for a cleanup pass |

Full folder definitions: [[40_Resources/Obsidian/Jarvis Vault Architecture]]. The Plan holds the personal-life equivalent of this table on its own dashboard.

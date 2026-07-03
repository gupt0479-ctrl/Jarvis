---
type: dashboard
status: tree
created: 2026-04-23
updated: 2026-07-03
tags:
  - dashboard
  - daily
today_focus: ""
today_80: ""
today_20: ""
lc_today: 0
study_today: 0
wins_done: 0
notes:
  - "[[CLAUDE.md]]"
  - "[[AGENTS.md]]"
  - "[[Jarvis OS — North Star]]"
---
# Jarvis — `$= moment().format("dddd, D MMMM YYYY")`
> [!focus] Today's Focus
> **Focus:** `INPUT[text:today_focus]`
> **80 — the one thing:** `INPUT[text:today_80]`
> **20 — supporting:** `INPUT[text:today_20]`
> *Patched by `/startday`, cleared by `/closeday`.*

> [!summary] Today's Numbers
> **LeetCode:** `INPUT[number:lc_today]` · **Wins:** `INPUT[number:wins_done]` / 5 · **Study hours:** `INPUT[number:study_today]`

## This Week
```dataviewjs
const folder = '"10_Areas/Life/Enumerate/Daily"';
const pages = dv.pages(folder).where(p => {
  if (!p.file.day) return false;
  const today = dv.date("today");
  const monday = today.minus({days: today.weekday - 1});
  return p.file.day >= monday && p.file.day <= today;
});
const lcTotal = pages.map(p => p.lc_count || 0).reduce((a,b) => a+b, 0);
const studyTotal = pages.map(p => p.study_today || 0).reduce((a,b) => a+b, 0);
const winsTotal = pages.map(p => p.wins_done || 0).reduce((a,b) => a+b, 0);
const clippings = dv.pages('"60_Claude/10_Source_Summaries"')
  .where(p => p.file.ctime >= dv.date("today").minus({days: dv.date("today").weekday - 1})).length;
dv.paragraph(`LC this week: **${lcTotal}/35** · Study: **${studyTotal}h** · Wins: **${winsTotal}** · Clippings ingested: **${clippings}**`);
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
LIMIT 10
```
## Daily Drivers
> [!todo] Habits
> - [ ] Gym (or MVP workout)
> - [ ] LeetCode ≥5
> - [ ] CSCI 2033 (30–45 min)
> - [ ] Course step (4041 / 2230 / 1103)
> - [ ] Review — run `/closeday`

## Internship Pipeline
```dataview
TABLE status, next, file.mtime AS "Updated"
FROM "10_Areas/Career/Internships"
SORT file.mtime DESC
LIMIT 5
```
## Clippings Triage
```dataview
TABLE file.ctime AS "Captured"
FROM "60_Claude/05_Clippings"
SORT file.ctime DESC
LIMIT 8
```
## Vault Health — Metadata Cleanup
```dataview
TABLE file.folder AS Folder, file.mtime AS "Updated"
FROM "10_Areas" OR "20_Progress" OR "40_Resources" OR "60_Claude"
WHERE !type OR !status
SORT file.mtime DESC
LIMIT 10
```
## Navigation
**System:** [[CLAUDE.md]] · [[AGENTS.md]] · [[Jarvis OS — North Star]] · [[AI_CONTEXT]] · [[HUMAN_WRITING]] · [[40_Resources/Obsidian/Jarvis Vault Architecture|Vault Architecture]] · [[Claude Pro Workflow]]
**Claude OS:** [[Claude OS]] · [[20_Progress/AI/Claude OS Dashboard|Claude OS Dashboard]] · [[10_Areas/Excalidraw/Claude OS Map|Claude OS Map]]
**AI platforms:** [[10_Areas/AI/Claude Code|Claude Code]] · [[10_Areas/AI/Cursor|Cursor]] · [[10_Areas/AI/Kiro|Kiro]] · [[10_Areas/AI/Codex|Codex]]
**Life:** [[Life OS]] · [[10_Areas/Life/Tracking/Health Tracker|Health Tracker]] · [[10_Areas/Life/Tracking/Finance Tracker|Finance Tracker]] · [[10_Areas/Life/Plans/01 - Daily Operating System|Daily OS]]

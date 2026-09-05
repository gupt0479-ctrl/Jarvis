---
type: dashboard
status: active
created: 2026-07-26
notes:
  - "[[Internship Pipeline]]"
  - "[[Internships Hub]]"
tags:
  - internship
  - habit
next: Tick a box today.
---
# Habit Tracker
## Overview
==A 16-week window, one box per day, plus a final goal that counts itself — no plugin required, works anywhere this vault opens.== The daily habit: touch the loop today — check `List/Dossiers/` for anything new, screen one thing, or follow up on something already in motion. Missing a day is data, not failure; missing two in a row is the actual signal to notice, per the vault's own [[Atomic Habits#The 4th Law - Make it Satisfying|Never Miss Twice]] rule.
## Final Goal — Real Count, Not Manual Tally
```dataview
TABLE WITHOUT ID
  length(rows) as "Applications Submitted So Far"
FROM "10_Areas/Career/Internships/Tracker/Each One/Applied" OR "10_Areas/Career/Internships/Tracker/Each One/Result"
GROUP BY true
```
> [!NOTE]
> Target: set a real number here once you have a sense of realistic weekly pace (careery.pro's research says CS/tech students typically need 100-300+ applications — see [[System - Build Log]]). This count is auto-computed from real Tracker notes, never hand-edited.
## 16-Week Window
Tick a box the day you actually touched the loop — found, screened, reached out, applied, followed up. One tick is enough; don't require a full application to count the day.
| Week | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 3 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 5 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 6 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 7 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 8 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 9 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 10 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 11 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 12 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 13 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 14 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 15 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 16 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
## Streak Rule
Never Miss Twice: one missed day is nothing. Two in a row means stop and ask why — sleep, unclear next action, or the loop itself is generating no real candidates to screen (check [[10_Areas/Career/Internships/List/Resources]] if it's the latter).

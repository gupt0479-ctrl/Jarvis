---
type: evergreen
status: tree
tags:
  - dashboard
  - capability
  - depth-ladder
created: 2026-04-25
updated: 2026-04-25
notes:
  - "[[Career Field OS]]"
  - "[[Career Question Bank]]"
  - "[[BOOM Board]]"
---
# Career Depth Ladder

Modeled after the [[BOOM Board]]. Career track covers portfolio building, interview prep, STAR method, mentorship, and professional strategy.

## Core Concepts

- [[Portfolio]]
- [[Elevator pitch]]
- [[Interview Questions]]
- [[ABB Interview Prep]]
- [[Plan|Mentorship Plan]]
- [[Freelancing]]
- [[Internship Search Stack]]

## Compare and Discriminate

| Concept A | Concept B | What to clarify |
|---|---|---|
| Portfolio bullet | Interview story | A portfolio bullet is a compressed proof artifact (one line, scannable). An interview story is a STAR narrative with setup, action, and measurable result. Same source material, different format and audience. |
| Networking | Cold outreach | Networking builds relationships over time through shared context. Cold outreach is a one-shot pitch to a stranger. Networking compounds; cold outreach has a low hit rate but scales. |
| Technical interview | Behavioral interview | Technical tests whether you can solve problems under pressure. Behavioral tests whether you can explain decisions, handle conflict, and work on a team. Both require preparation but different preparation. |

## 30-Minute Refresher

1. [[Portfolio]]
2. [[Elevator pitch]]
3. [[Interview Questions]]

## 2-Hour Technical Refresher

1. [[Portfolio]]
2. [[Interview Questions]]
3. [[ABB Interview Prep]]
4. [[Plan|Mentorship Plan]]
5. [[Internship Search Stack]]
6. [[Freelancing]]

## Deep Relearning Pass

Start at [[Useful Links|Career Useful Links]], then review the full internship folder. Revisit [[Mentorship Board]] for mentorship context.

## Overdue Drills

```dataview
TABLE mastery_level, difficulty, next_drill, drill_interval
FROM ""
WHERE type = "concept" AND contains(track, "career") AND next_drill AND next_drill < date(today)
SORT next_drill ASC
```

## All Tracked Career Concepts

```dataview
TABLE mastery_level, difficulty, status, next_drill
FROM ""
WHERE type = "concept" AND contains(track, "career")
SORT file.name ASC
```

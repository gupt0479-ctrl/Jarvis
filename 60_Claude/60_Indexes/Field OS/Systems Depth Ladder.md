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
  - "[[Systems Field OS]]"
  - "[[Systems Question Bank]]"
  - "[[BOOM Board]]"
---
# Systems Depth Ladder

Modeled after the [[BOOM Board]]. Seeded from UROP/BOOM work. Refresher lists are hand-picked — Dataview only surfaces the drill queue.

## Core Concepts

The load-bearing systems ideas from BOOM and backend work.

- [[Learning/Observability and Tracing]]
- [[Learning/Kafka Redis and Workers]]
- [[Learning/API and Backend]]
- [[Learning/MongoDB Data Model and Filters]]
- [[Learning/Docker WSL and Local Setup]]
- [[Learning/Rust Patterns in BOOM]]
- [[Rust/02 Ownership Borrowing and Lifetimes]]

## Compare and Discriminate

| Concept A | Concept B | What to clarify |
|---|---|---|
| Kafka (message queue) | Redis (cache/pub-sub) | Kafka persists messages and guarantees ordering; Redis is fast but ephemeral by default. BOOM uses both — Kafka for durable event flow, Redis for worker coordination. |
| Observability | Monitoring | Monitoring checks known failure modes. Observability lets you ask new questions about unknown failures. Tracing is the observability tool that mattered most in BOOM. |
| Docker containers | WSL environment | Docker isolates services; WSL gives you a Linux userspace on Windows. BOOM local setup needs both — WSL runs the dev environment, Docker runs the services. |

## 30-Minute Refresher

1. [[BOOM]]
2. [[Learning/Alerts and Data Flow]]
3. [[Learning/Observability and Tracing]]

## 2-Hour Technical Refresher

1. [[BOOM]]
2. [[Learning/API and Backend]]
3. [[Learning/Kafka Redis and Workers]]
4. [[Learning/MongoDB Data Model and Filters]]
5. [[Learning/Observability and Tracing]]
6. [[Postman]]

## Deep Relearning Pass

Start at [[20_Progress/UROP/index|UROP index]] and go in order. Then work through the [[Rust]] learning path from [[Rust/01 Rust Basics Through BOOM]] onward.

## Overdue Drills

```dataview
TABLE mastery_level, difficulty, next_drill, drill_interval
FROM ""
WHERE type = "concept" AND contains(track, "systems") AND next_drill AND next_drill < date(today)
SORT next_drill ASC
```

## All Tracked Systems Concepts

```dataview
TABLE mastery_level, difficulty, status, next_drill
FROM ""
WHERE type = "concept" AND contains(track, "systems")
SORT file.name ASC
```

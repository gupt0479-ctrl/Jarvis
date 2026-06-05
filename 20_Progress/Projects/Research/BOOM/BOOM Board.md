---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[index]]"
  - "[[BOOM]]"
  - "[[Rust]]"
---
# BOOM Board
This is the fastest navigation note for the whole UROP folder.
## What BOOM Is
- [[BOOM]]
- [[Alerts and Data Flow]]
Use these first if you need to answer:
- What is an alert?
- What does BOOM store?
- Why does the system exist?
## How BOOM Is Built
- [[API and Backend]]
- [[Kafka Redis and Workers]]
- [[MongoDB Data Model and Filters]]
- [[Docker WSL and Local Setup]]
Use these when the question is:
- How does data move?
- Why are Kafka and Redis both here?
- How does the API sit on top of MongoDB?
- What infrastructure is required locally?
## What You Actually Implemented
- [[Observability and Tracing]]
- [[Presentation Site Narrative]]
- [[API Work]]
- [[Logs]]
- [[Postman]]
- [[Symposium]]
Use these when the question is:
- What changed during the UROP?
- What did the traces prove?
- Which bugs became easier to diagnose?
- How do I explain this work to someone else?
## Rust Learning Path
- [[Rust]]
- [[01 Rust Basics Through BOOM]]
- [[02 Ownership Borrowing and Lifetimes]]
- [[03 Result Option and Error Handling]]
- [[04 Async Traits and Concurrency]]
- [[05 Macros Serialization and Config]]
- [[06 Reading BOOM Code Effectively]]
- [[Rust Patterns in BOOM]]
Use these when the question is:
- How do I read this Rust code without getting lost?
- Which Rust ideas mattered most in BOOM?
- Which patterns transfer to backend and ML systems work?
## Systems and Career Takeaways
- [[Testing Debugging and Deployment]]
- [[Systems Lessons for AI ML]]
Use these when the question is:
- What did this project teach me beyond astronomy?
- Which backend and infra skills transfer to AI/ML engineering?
## Suggested Revisit Loops
### 30-minute refresher
1. [[BOOM]]
2. [[Alerts and Data Flow]]
3. [[Observability and Tracing]]
### 2-hour technical refresher
1. [[BOOM]]
2. [[API and Backend]]
3. [[Kafka Redis and Workers]]
4. [[MongoDB Data Model and Filters]]
5. [[Observability and Tracing]]
6. [[Postman]]
### Deep relearning pass
Start at [[index]] and go in order.
## Data view
### Learning notes
```dataview
TABLE status, file.folder
FROM "20_Progress/UROP/Learning"
SORT file.name ASC
```

### Project notes
```dataview
TABLE status, deadline, next
FROM "20_Progress/UROP"
WHERE type = "project"
SORT deadline ASC, file.name ASC
```

### Rust notes
```dataview
TABLE status, created
FROM "20_Progress/UROP/Rust"
SORT file.name ASC
```

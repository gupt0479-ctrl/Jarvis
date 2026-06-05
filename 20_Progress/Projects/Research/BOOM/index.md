---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[BOOM]]"
  - "[[BOOM Board]]"
  - "[[Rust]]"
---
# UROP Study Index
This folder is the cleaned learning archive for the BOOM UROP. It has four roles:
- explain what BOOM does as a real backend and data system
- document what you actually implemented and debugged during the year
- turn the project into reusable engineering knowledge
- give you a structured path for relearning the codebase later
## Recommended Study Order
1. [[BOOM]]
2. [[Alerts and Data Flow]]
3. [[Docker WSL and Local Setup]]
4. [[Rust]]
5. [[Rust Patterns in BOOM]]
6. [[Kafka Redis and Workers]]
7. [[MongoDB Data Model and Filters]]
8. [[API and Backend]]
9. [[Postman]]
10. [[Observability and Tracing]]
11. [[Testing Debugging and Deployment]]
12. [[API Work]]
13. [[Logs]]
14. [[Symposium]]

## Folder Map

### Core orientation

- [[BOOM]]
- [[BOOM Board]]
- [[Symposium]]

### Learning notes

- [[Alerts and Data Flow]]
- [[API and Backend]]
- [[Docker WSL and Local Setup]]
- [[Kafka Redis and Workers]]
- [[MongoDB Data Model and Filters]]
- [[Observability and Tracing]]
- [[Presentation Site Narrative]]
- [[Rust Patterns in BOOM]]
- [[Testing Debugging and Deployment]]
- [[Systems Lessons for AI ML]]

### Rust notes

- [[Rust]]
- [[01 Rust Basics Through BOOM]]
- [[02 Ownership Borrowing and Lifetimes]]
- [[03 Result Option and Error Handling]]
- [[04 Async Traits and Concurrency]]
- [[05 Macros Serialization and Config]]
- [[06 Reading BOOM Code Effectively]]

### Project journals and evidence

- [[API Work]]
- [[Logs]]
- [[Postman]]

### Mock walkthroughs

- [[Mock Alert Lifecycle]]
- [[Mock Trace Walkthrough]]

## How To Use This Folder

### If you want to understand BOOM conceptually

Read:

1. [[BOOM]]
2. [[Alerts and Data Flow]]
3. [[Kafka Redis and Workers]]
4. [[MongoDB Data Model and Filters]]

### If you want to understand the backend engineering

Read:

1. [[API and Backend]]
2. [[Postman]]
3. [[Observability and Tracing]]
4. [[Testing Debugging and Deployment]]

### If you want to improve at Rust through this project
Read:
1. [[Rust]]
2. [[01 Rust Basics Through BOOM]]
3. [[02 Ownership Borrowing and Lifetimes]]
4. [[03 Result Option and Error Handling]]
5. [[04 Async Traits and Concurrency]]
6. [[05 Macros Serialization and Config]]
7. [[06 Reading BOOM Code Effectively]]
8. [[Rust Patterns in BOOM]]
### If you want the work you did, not just the concepts
Read:
1. [[API Work]]
2. [[Logs]]
3. [[Postman]]
4. [[Symposium]]
## Study Standards Used In These Notes
Most notes now follow the same structure:
- why the topic matters
- where it lives in BOOM
- major concepts
- command recipes
- screenshot placeholders
- engineering takeaways
- related notes
That structure is intentional. The goal is to make the notes usable during:
- relearning
- debugging
- interview prep
- presentation prep
- future AI/ML systems work
## Data view
### UROP notes
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.name != this.file.name
SORT file.folder ASC, file.name ASC
```

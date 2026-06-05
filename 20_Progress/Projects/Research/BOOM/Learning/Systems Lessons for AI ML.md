---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[BOOM]]"
  - "[[Docker WSL and Local Setup]]"
  - "[[Observability and Tracing]]"
---
# Systems Lessons for AI ML

This note translates the BOOM project into skills that matter for later AI and ML engineering work.

Related notes:

- [[BOOM]]
- [[Docker WSL and Local Setup]]
- [[Kafka Redis and Workers]]
- [[MongoDB Data Model and Filters]]
- [[Observability and Tracing]]

## Why This Note Matters

You did not spend the year training new models, but that does not mean the work is unrelated to AI or ML.

Modern AI systems still depend on:

- APIs
- data pipelines
- queues
- databases
- observability
- reproducible environments
- deployment infrastructure

BOOM gave you direct exposure to all of that.

## What Field You Actually Worked In

The best labels for this work are:

- backend engineering
- data systems
- distributed systems
- observability engineering
- scientific computing infrastructure

Those are all useful foundations for later AI and ML work.

## Transferable Skills From BOOM

### 1. Pipeline thinking

You worked on a system where data moves through stages with different responsibilities.

This is directly relevant to:

- feature pipelines
- inference pipelines
- evaluation pipelines

BOOM teaches the staged pattern clearly:

- raw event arrives
- it is normalized
- richer context is attached
- a decision layer runs
- the result is stored or emitted

### 2. Reproducible environments

WSL, Docker, and service orchestration are the same kinds of environment skills needed for:

- GPU workloads
- model-serving stacks
- experiment infrastructure

### 3. Observability

Tracing and structured diagnostics matter even more in ML systems because failures can come from:

- model input issues
- data drift
- service dependencies
- runtime environment problems

The exact lesson from your UROP is that failures often live at subsystem boundaries. In ML systems, those boundaries might be request to feature store, feature store to model server, or scheduler to worker.

### 4. Database and schema thinking

You learned that stored shape is a design decision.

That matters for:

- feature stores
- experiment metadata stores
- vector databases
- model result serving

BOOM also teaches a useful data lesson:

- the in-memory model and the stored model are not automatically the same thing

### 5. System debugging

You learned how to separate:

- code bugs
- environment bugs
- dependency bugs
- data bugs

That is one of the most valuable habits in any ML platform role.

Another helpful translation of BOOM into ML-platform language is:

- Kafka consumer = ingestion job
- enrichment worker = feature or inference stage
- filter worker = decision or routing stage
- API = serving layer
- tracing = cross-system diagnosability

## Questions To Ask Yourself Going Forward

- how does data move through this system?
- where are the boundaries between stages?
- where would I put tracing?
- what is the unit of storage?
- which parts are environment-sensitive?
- what could silently fail without observability?

## Command Recipes

### Search for architecture boundaries in BOOM

```bash
cd ~/projects/boom
rg -n "queue|worker|Collection<|TracingLogger|instrument|topic|model" src
```

### Review the most transferable files

```bash
sed -n '1,260p' src/conf.rs
sed -n '1,260p' src/kafka/base.rs
sed -n '1,260p' src/enrichment/base.rs
sed -n '1,220p' src/utils/o11y/logging.rs
```

## Screenshot Placeholders

- [ ] one system architecture diagram labeled with transferable skills
- [ ] one tracing screenshot labeled "observability lesson"
- [ ] one Docker or WSL screenshot labeled "reproducible environment lesson"
- [ ] one database or filter screenshot labeled "data model lesson"

## Engineering Takeaways

- You worked in backend and systems engineering, not just "astronomy code."
- Those skills are highly relevant to serious AI and ML work.
- The best way to use this project for your future is to extract the systems lessons explicitly, not treat them as side details.

## Data view
### UROP notes that reference this concept
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

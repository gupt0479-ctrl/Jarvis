---
type: input
input_kind: presentation
status: sprout
created: 2026-04-22
source_url:
related_progress:
  - "[[BOOM]]"
  - "[[API Work]]"
  - "[[Postman]]"
  - "[[Logs]]"
tags:
  - input
next: "[[Rust]]"
---
# BOOM Observability - Spring Symposium Notes

**Presenter:** Anant Gupta  
**Event:** UMN Spring Undergraduate Research Symposium 2026  
**Mentor:** Prof. Michael Coughlin  
**Project:** Building Intelligent Observability and Filtering Infrastructure for BOOM

## Core Message

If I need one sentence to anchor the whole talk:

- I made BOOM easier to understand, debug, and trust by adding structured tracing across the API, scheduler, Kafka pipeline, and enrichment workers.

If I need one sentence to explain why that matters:

- BOOM is a distributed system, so failures are rarely isolated. Tracing turns scattered logs into a connected story of what happened.

## Fast Talking Points

- BOOM is a Rust-based astronomical alert broker with Kafka, Redis or Valkey, MongoDB, background workers, and an API.
- My project focused on structured tracing and diagnosability, not new scientific filtering logic.
- I instrumented API routes, auth, DB setup, scheduler startup, Kafka flows, worker loops, and enrichment or model-loading paths.
- The main engineering outcome was diagnosability.
- The main scientific outcome is that future replay-based filter work is now easier to do correctly.

## BOOM Outline

In BOOM, an alert is the unit of data coming from time-domain sky surveys such as ZTF, LSST, and DECam that flags that **something in the sky changed or looks like a new transient event**.

- A survey scans the sky repeatedly.
- It compares new images to older images.
- If something is new, brighter, dimmer, moved, or changed unexpectedly, the survey emits an alert packet.
- That packet means: something at this sky location looks interesting enough to inspect.

Examples of what could trigger an alert:

- a supernova starting to brighten
- a variable star changing brightness
- an active galactic nucleus flaring
- an asteroid moving
- an artifact or false positive
- in some workflows, a candidate relevant to gravitational-wave follow-up

What BOOM does with that:

1. ingest the raw alert stream
2. enrich each alert with more context
3. filter alerts so users keep only scientifically relevant ones
4. store the processed results
5. expose them through the API or downstream systems

The simplest explanation to say out loud:

- The survey detects a possible change in the sky and emits an alert packet.
- BOOM receives that packet, adds context, decides whether it is interesting, stores it, and makes it usable for follow-up.

## 10-Minute Talk Outline

### 0:00-0:45 - Opening

- My project was about observability in BOOM, the Burst & Outburst Observations Monitor.
- BOOM is an astronomical alert broker written in Rust.
- It processes alerts from surveys such as ZTF, LSST, and DECam.
- My main contribution was adding structured tracing so requests, workers, Kafka events, and failures carry context across the whole system.

Short version:

- BOOM already had the core pipeline, but understanding failures across that pipeline was difficult.
- My work made the system explain itself.

### 0:45-2:00 - What BOOM Does

- BOOM ingests astronomical alert streams and moves them through several stages before exposing results to users and downstream systems.
- High-level flow:
  - Kafka topics receive alerts.
  - Kafka consumers move alerts into Redis or Valkey queues.
  - The scheduler manages alert, enrichment, and filter workers.
  - Workers process and enrich alerts, then store results in MongoDB.
  - The API exposes catalogs, filters, users, and related operations.

Short version:

- BOOM is not just one web server.
- It is a multi-stage pipeline with messaging, queues, background workers, model inference, a database, and an HTTP API.
- That architecture is why observability matters so much.

### 2:00-3:15 - The Problem Before My Work

- BOOM had logs, but they were much harder to connect across components.
- In a distributed pipeline, the hard questions are:
  - Which request triggered this?
  - Which worker failed?
  - Which Kafka topic was involved?
  - Was the issue in auth, config, Redis, MongoDB, or model loading?
- Flat logs answer local questions.
- Tracing answers flow questions.

Short version:

- Traditional logs tell you that something happened.
- Tracing tells you where it happened, what it was attached to, and what happened before and after.

### 3:15-6:45 - What I Implemented

#### Shared tracing setup

- I centralized observability setup so BOOM binaries use a consistent tracing initialization path.
- That matters because API, scheduler, Kafka tools, and CLI binaries should produce logs in the same language and structure.

#### Config and startup visibility

- I added tracing around config loading and startup.
- This made it easier to see which config path was used, which survey was selected, and what the process believed its runtime settings were.

#### API request tracing

- I used `tracing-actix-web` for request-level spans.
- That gave every HTTP request context such as method, route, and request ID.
- I then added `#[tracing::instrument]` to route handlers and helper functions so application logic showed up inside the request span.

#### Auth and DB tracing

- I added trace context around token creation, token validation, token decoding, and authenticated user lookup.
- I also added tracing around API database setup and admin bootstrap behavior.
- This made auth failures and DB startup behavior much easier to diagnose.

#### Scheduler and worker tracing

- I instrumented scheduler startup, thread-pool initialization, worker lifecycle, heartbeat behavior, and shutdown.
- That made background processing visible instead of being a blind spot.

#### Kafka tracing

- I instrumented topic checks, partition checks, producer flows, consumer loops, output queue interactions, and topic-related error paths.
- This is important because Kafka issues often depend on environment state, topic existence, and timing.

#### Enrichment and model diagnostics

- I added context around batch sizes, fetched alerts, model paths, and worker processing.
- This made ONNX and CUDA-related failures much more readable.

#### Correctness fix

- While doing this work, I also fixed a real auth-related config issue: token expiration was referencing the wrong config value.

Short version:

- I did not just add more log lines.
- I added structured context at the boundaries where BOOM becomes hard to debug: requests, workers, topics, queues, auth, and model loading.

### 6:45-8:15 - Concrete Examples I Can Use

#### Example 1: malformed bearer token

- A request to an authenticated endpoint failed with a Base64 decoding error.
- Without tracing, that error looks generic.
- With tracing, the failure path through auth middleware and token decoding was obvious.
- That made it clear the problem was token formatting, not MongoDB or the route handler.

#### Example 2: Kafka topic missing

- A local test produced `UnknownTopicOrPartition`.
- Tracing attached topic and runtime context.
- That made it easier to classify as a local environment issue, not a BOOM logic bug.

#### Example 3: model-loading failure

- Enrichment worker startup exposed ONNX or CUDA related failures.
- Tracing made the failure readable enough to localize the problem to worker and model context.

### 8:15-9:15 - Impact

- API requests now have nested, readable request trees.
- Auth failures are easier to classify.
- Kafka and queue behavior are traceable.
- Model and environment failures are easier to interpret.
- This is useful for debugging, future development, testing, and eventual replay-based science work.

Short version:

- The main result is not a new user-facing feature.
- The main result is that the engineering team can now reason about BOOM as a connected system.

### 9:15-10:00 - Future Work

- The original UROP idea had two tracks:
  - observability infrastructure
  - scientific filter optimization
- This project delivered the observability infrastructure.
- The next step is to use that foundation to replay historical alerts and improve the scientific filtering side.

If asked what specifically comes next:

- replay GraceDB or historical alert data
- evaluate chirp mass and FAR-based filtering
- measure precision and recall more systematically
- propose improved filter thresholds based on replay evidence

## Question Bank

### BOOM and architecture

**What is BOOM in one sentence?**

- BOOM is a Rust-based astronomical alert broker that ingests, processes, enriches, filters, stores, and exposes transient alert data.

**Why is BOOM architecturally difficult to debug?**

- Because it is distributed across API requests, Kafka topics, Redis or Valkey queues, scheduler-managed workers, MongoDB operations, and model-loading steps.
- A failure in one place can appear downstream somewhere else.

**Why use Kafka and Redis together?**

- Kafka is the external stream and messaging layer.
- Redis or Valkey is used as a fast internal queue or cache for worker coordination.
- They serve different roles in the pipeline.

### Tracing and implementation

**What is the difference between logging and tracing?**

- Logging produces independent lines.
- Tracing produces related spans that form a tree.
- A span gives context to all the events inside it.

**What is a span?**

- A span is one named operation within a larger flow.
- For example, an HTTP request can contain middleware spans, auth spans, DB spans, and route-handler spans.

**What Rust tools did you use?**

- `tracing`
- `tracing-subscriber`
- `tracing-actix-web`
- existing OpenTelemetry-related infrastructure already present in BOOM

**What does `#[tracing::instrument]` actually buy you?**

- It creates structured spans around function execution.
- It lets you attach fields like route, user ID, topic, batch size, or model path.
- It also lets errors be recorded on the correct operation.

**Did you change BOOM's scientific behavior?**

- Not intentionally.
- This was primarily an observability PR.
- The main behavior fix was an auth token expiration config bug that I found during the work.

### Debugging examples

**What is the best concrete bug story from this work?**

- The malformed bearer token example.
- The trace clearly showed the failure path through auth middleware and token decoding, which made it obvious that the token format was wrong.

**How did tracing help with environment-specific issues?**

- It made it much easier to classify whether a failure was caused by local setup, missing topics, missing scripts, or model-runtime configuration rather than by core code logic.

**Did you fully solve the ONNX or CUDA issue?**

- No.
- The key improvement was making the failure readable and localizable.
- That is still valuable engineering progress because reproducible diagnosis comes before reliable fixes.

### Design choices and tradeoffs

**Why does observability matter so much in research software?**

- Research software mixes production-style infrastructure with experimental workflows.
- If you cannot explain behavior, you cannot trust results or iterate efficiently.

**Did tracing create overhead?**

- There is some overhead, but the tradeoff is usually worth it for debugging and development.
- The implementation focuses on structured instrumentation rather than excessive noisy logging.

**How did you avoid dumping too much data into logs?**

- By using `skip(...)` on heavy or sensitive arguments and by attaching only useful fields to spans.

### Future work

**What would Phase 2 look like?**

- Historical alert replay, evaluation against known outcomes, and improved filtering thresholds based on evidence rather than intuition.

**Why was observability the right first step before scientific optimization?**

- Because replay and evaluation are much more credible if the system is observable.
- Otherwise it is too hard to trust whether a replayed alert flowed through the pipeline correctly.

## Last-Minute Reminders

- Do not oversell this as a science-results project.
- Say clearly that this phase delivered engineering infrastructure.
- Emphasize that better observability is what enables stronger science work later.
- Use one or two concrete debugging stories rather than trying to list every file changed.
- If a question is very detailed, answer at the system-design level first, then go into code-level detail if needed.

## Data view
### Related UROP notes
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

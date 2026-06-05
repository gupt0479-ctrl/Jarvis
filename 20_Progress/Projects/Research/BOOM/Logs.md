---
type: project
status: seed
related_progress:
  - "[[BOOM]]"
  - "[[API Work]]"
  - "[[Observability and Tracing]]"
tags:
  - "#progress"
---
# Logs and Trace Evidence

This note is the cleaned evidence journal for what the logs and traces actually proved during the UROP.

## What This Note Records

This note is not about abstract observability theory. It records what the runtime evidence showed once the new tracing was in place.

Use it to answer:

- what subsystems were actually exercised?
- what failures were diagnosed?
- which issues were code issues versus environment issues?

## What The Runtime Evidence Confirmed

### API

The traces showed:

- startup tracing was active
- each request got a root span
- auth middleware created nested spans
- route handlers appeared under the request tree

### Scheduler

The traces showed:

- worker config loading
- thread pool initialization
- worker startup
- heartbeat and shutdown visibility

### Kafka

The traces showed:

- consumer or producer context
- topic and queue-related context
- local topic failures were visible as environment issues

### Enrichment

The traces showed:

- batch processing context
- worker identity
- model-loading failures with more readable context

## Three Evidence Stories Worth Remembering

### Story 1: malformed auth header

Signal:

- Base64 decode error

Why tracing mattered:

- the span tree localized the error to auth decoding quickly
- that ruled out deeper handler and DB logic

Conclusion:

- request formatting bug, not application-state corruption

### Story 2: Kafka topic missing

Signal:

- `UnknownTopicOrPartition`

Why tracing mattered:

- the trace attached topic and runtime context
- it was easier to classify as a local-environment issue

Conclusion:

- expected external dependency issue, not a regression in tracing

### Story 3: ONNX or model-loading failure

Signal:

- enrichment worker failed during model setup

Why tracing mattered:

- worker and model context became visible
- failure chain became more readable

Conclusion:

- environment or runtime dependency problem became explainable

### Story 4: scheduler heartbeat and worker visibility

Signal:

- the scheduler kept emitting heartbeat updates with worker counts

Why tracing and structured logging mattered:

- it proved the scheduler was alive even when downstream processing seemed slow
- it turned worker liveness into an observable fact instead of a guess

## Span Shapes To Memorize

### Request tree

```text
HTTP request
  auth::middleware
    auth::authenticate_user
      auth::validate_token
        auth::decode_token
  catalogs::get_catalogs
```

### Scheduler tree

```text
run
  load config
  init thread pool
  alert worker
  enrichment worker
  filter worker
  heartbeat
  shutdown
```

### Kafka tree

```text
run
  kafka::<survey>::consume
    validate topic
    read message
    push to internal queue
```

## Command Recipes

### API evidence

```bash
cd ~/projects/boom
RUST_LOG=info,boom=debug OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317 cargo run --bin api
```

### Scheduler evidence

```bash
RUST_LOG=info,boom=debug cargo run --bin scheduler -- --config config.yaml ztf
```

### Kafka evidence

```bash
RUST_LOG=info,boom=debug cargo run --bin kafka_consumer -- ztf
```

### Span-event evidence

```bash
RUST_LOG=debug,ort=warn BOOM_SPAN_EVENTS=new,close cargo run --bin scheduler -- ztf
```

### Search instrumentation sites

```bash
rg -n "#\\[instrument|TracingLogger|info_span!|log_error!|as_error!" src
```

## Screenshot Placeholders

- [ ] API request trace showing nested auth spans
- [ ] scheduler startup plus worker spans
- [ ] Kafka topic error with context fields
- [ ] enrichment worker model-loading error chain
- [ ] one side-by-side screenshot of request action and trace output
- [ ] one screenshot of scheduler heartbeat with worker counts

## Engineering Takeaways

- Volume is not the point; structure is the point.
- Good traces let you classify failures by subsystem instead of guessing.
- A debugging improvement is real engineering progress even if the environment issue still exists.

## Related Notes

- [[Observability and Tracing]]
- [[API Work]]
- [[Postman]]
- [[Symposium]]

## Data view
### UROP notes that reference these logs
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

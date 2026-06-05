---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Logs]]"
  - "[[API Work]]"
  - "[[Symposium]]"
---
# Observability and Tracing

This note covers the central engineering theme of the UROP: making BOOM explain itself.

Related notes:

- [[Logs]]
- [[API Work]]
- [[Symposium]]
- [[Mock Trace Walkthrough]]

## Why This Note Matters

Observability is one of the highest-value transferable skills from this project.

If you later work on AI or ML systems, you will still need to answer:

- what request or job caused this behavior?
- which stage failed?
- which model or worker was involved?
- is this a code issue, a dependency issue, or an environment issue?

BOOM gave you a concrete case study in that problem.

## Logging Versus Tracing

### Logging

Logging tells you that something happened.

### Tracing

Tracing tells you:

- what happened
- where it happened
- which parent operation it belonged to
- what structured fields were attached
- where the error occurred in the tree

This is why tracing is more powerful in multi-stage systems.

## Why BOOM Needed It

BOOM spans:

- API
- auth
- MongoDB
- Kafka
- Redis or Valkey
- scheduler
- worker pools
- enrichment and model loading

Without structured observability, those boundaries become blind spots.

## Core Crates And Files

Crates:

- `tracing`
- `tracing-subscriber`
- `tracing-actix-web`
- `tracing-log`
- `tracing-flame`
- OpenTelemetry-related metrics crates

Files:

- `src/utils/o11y/logging.rs`
- `src/utils/o11y/metrics.rs`

The code splits observability into two linked systems:

- `logging.rs` handles subscriber construction, filtering, span lifecycle formatting, and structured error helpers
- `metrics.rs` handles OTLP metrics initialization, meter selection, and resource metadata

## The Main Pattern

```rust
#[tracing::instrument(name = "component::operation", skip(...), fields(...), err)]
```

### `name`

Makes the span readable and searchable.

### `skip(...)`

Avoids logging heavy or sensitive inputs.

### `fields(...)`

Attaches context such as:

- route
- topic
- batch size
- model path
- user ID

### `err`

Records failures on the exact span that failed.

This is the key idea behind the website's "Trace Anatomy" section:

- a function boundary can also be an observability boundary

## Request Tracing In The API

The API uses `TracingLogger::default()` so that every request gets a root span.

Then nested spans appear under it for:

- auth middleware
- token validation and decode
- route handlers
- helper functions

That gives you a request tree rather than flat text.

The website's trace explorer turns this into two concrete walkthroughs:

- `POST /api/auth` for login and token creation
- `GET /api/catalogs` for protected-route validation and handler execution

## Worker Tracing

The UROP work also added visibility around:

- scheduler startup
- thread-pool initialization
- worker lifecycle
- heartbeat
- shutdown
- enrichment worker processing

This matters because background jobs are where systems often become hardest to reason about.

In the actual worker code, spans carry fields such as:

- `survey`
- `worker_id`
- `config_path`
- `batch_size`
- `input_queue`
- `output_queue`

## Metrics Versus Traces

Traces help you answer:

- what happened in this flow?

Metrics help you answer:

- how is the system behaving over time?

BOOM includes both ideas through tracing and OpenTelemetry-style metrics.

From `docs/telemetry.md` and `metrics.rs`, BOOM's metrics path is:

1. initialize a service-specific meter
2. emit counters and histograms with attributes
3. export metrics via OTLP
4. send them through the OpenTelemetry collector
5. visualize them in Prometheus

## Best Debugging Story

The malformed auth header is the cleanest example:

- request sent `Bearer <token>`
- decode failed
- trace localized the failure to the auth path
- diagnosis became immediate

This is the difference between:

- "something failed"

and:

- "this specific span failed because the request header was malformed"

## Real Failures Worth Memorizing

The presentation site distilled the most useful local failure families:

- malformed bearer token
- missing Kafka topic
- ONNXRuntime or CUDA issue
- local setup or helper-script issue
- endpoint expectation mismatch

The value of tracing is not that it prevents these failures. It makes them classifiable.

## What `logging.rs` Actually Adds

`src/utils/o11y/logging.rs` provides:

- `log_error!` for consistent structured error events
- `as_error!` for ergonomic `inspect_err` use
- environment-driven `EnvFilter`
- optional span lifecycle events through `BOOM_SPAN_EVENTS`
- optional flamegraph output through `BOOM_FLAME_FILE`

## What `metrics.rs` Actually Adds

`src/utils/o11y/metrics.rs` creates:

- distinct meters for consumer, producer, and scheduler
- resource metadata like instance ID, service version, and deployment environment
- OTLP export configuration

## Command Recipes

### Run the API with tracing

```bash
cd ~/projects/boom
RUST_LOG=info,boom=debug OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317 cargo run --bin api
```

### Run the scheduler with span events

```bash
RUST_LOG=debug,ort=warn BOOM_SPAN_EVENTS=new,close cargo run --bin scheduler -- ztf
```

### Search instrumentation sites

```bash
rg -n "#\\[instrument|TracingLogger|info_span!|log_error!|as_error!" src
```

### Search metrics code

```bash
rg -n "meter|counter|histogram|metrics|opentelemetry" src
```

## Screenshot Placeholders

- [ ] `/api/auth` request trace
- [ ] `/api/catalogs` request trace
- [ ] scheduler heartbeat or worker lifecycle spans
- [ ] Kafka failure with contextual fields
- [ ] enrichment failure with worker and model context

## Engineering Takeaways

- Observability is a subsystem, not an afterthought.
- Structure matters more than raw log volume.
- The best place to instrument is at subsystem boundaries.
- Better diagnostics are a legitimate engineering deliverable.

## Data view
### UROP notes that reference this concept
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

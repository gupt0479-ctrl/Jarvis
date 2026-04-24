---
type: concept
status: sprout
created: 2026-04-23
updated: 2026-04-27
tags:
  - concept
  - evergreen
notes:
  - "[[Learning/Docker WSL and Local Setup]]"
  - "[[Learning/Observability and Tracing]]"
  - "[[Logs]]"
track:
  - systems
prerequisites:
  - "[[BOOM]]"
  - "[[Learning/Docker WSL and Local Setup]]"
  - "[[Learning/Observability and Tracing]]"
used_in:
  - "[[API Work]]"
evidence: []
difficulty: 3
mastery_level: novice
drill_interval: 10
---
# Testing Debugging and Deployment

## Deep Dive

### One-Sentence Version

Engineering maturity means knowing how to validate a system, classify failures by layer, and debug in a fixed order instead of randomly.

### What It Is

BOOM's testing surface includes unit tests (`cargo test`), integration tests across config/API/Kafka/scheduler, and end-to-end validation by running producer + consumer + scheduler + API together. Debugging follows a layered order: infrastructure → config → input → state → traces → code logic.

### Why It Matters

Most BOOM issues are environment-dependent, not code-logic bugs. Being able to classify failure class quickly (input bug vs environment-state bug vs runtime dependency bug vs correctness bug) is a transferable engineering skill.

### Real Example

The malformed bearer token failure: looks like an auth code bug, but the trace shows the request header was malformed. Without the layered debugging order, you might spend hours reading auth code when the fix is in the client request.

### Contrast With

- **Unit tests vs end-to-end validation**: Unit tests verify isolated logic. End-to-end validation verifies that services cooperate correctly. BOOM needs both because many failures only appear when services interact.
- **Code bugs vs environment bugs**: A route logic issue is a code bug. A missing Kafka topic is an environment bug. The debugging order matters because environment bugs are more common and easier to fix once identified.

### Source Anchors

- `tests/README.md` — test surface overview
- `tests/test_api.rs`, `tests/test_kafka.rs` — integration tests
- BOOM `docs/deployment.md` — deployment architecture

This note collects the practical engineering side of BOOM: how to test it, debug it, and reason about running it as a real system.

Related notes:

- [[Learning/Docker WSL and Local Setup]]
- [[Learning/Observability and Tracing]]
- [[Logs]]
- [[Learning/Systems Lessons for AI ML]]

## Why This Note Matters

Engineering maturity comes from knowing:

- how to validate a system
- how to separate code bugs from setup bugs
- how to debug in a fixed order instead of randomly
- how deployment architecture affects local reasoning

## Testing In BOOM

BOOM includes tests across:

- config
- API behavior
- Kafka-related paths
- scheduler logging
- survey-specific behavior

Useful references:

- `tests/README.md`
- `tests/test_api.rs`
- `tests/test_kafka.rs`
- `tests/test_scheduler_logging.rs`

There is also a second test surface that mattered a lot during the UROP:

- bring up the producer, consumer, scheduler, and API together and observe system behavior end to end

## A Good Debugging Order

When BOOM misbehaves, use this order:

1. is the infrastructure up?
2. is the configuration valid?
3. is the CLI or request input valid?
4. is the expected topic, queue, or database state present?
5. what do the traces say?
6. is this code logic or environment state?

This matters because many BOOM issues are environment-dependent.

The project gave you a useful set of failure classes to remember:

- malformed bearer token: input bug
- missing Kafka topic: environment-state bug
- ONNX or CUDA failure: runtime dependency bug
- token-expiration config issue: correctness bug

## Failure Classes To Recognize

### Code-level failures

- route logic issue
- auth handling issue
- serialization or parsing issue
- worker behavior issue

### Environment-level failures

- missing Kafka topic
- missing native libraries
- container not running
- wrong `.env`
- ONNX or CUDA mismatch

Being able to classify the failure class quickly is a real skill.

## Deployment Ideas Worth Learning

BOOM is designed as an orchestrated system, not a single binary living alone.

That means deployment thinking includes:

- service containers
- reverse proxy or ingress ideas
- metrics and telemetry plumbing
- CI and automation
- secrets and config management

You do not need to memorize every deployment step. You do need to understand the shape of the deployed system.

From the deployment docs, that shape includes:

- remote server
- Docker Compose stack
- reverse proxy
- self-hosted GitHub runner
- repository secrets

## Recommended Practical Drill

If you want to rebuild confidence in BOOM later, do this in order:

1. bring up containers
2. run the producer
3. run the consumer
4. run the scheduler
5. run the API
6. authenticate through Postman
7. inspect logs and traces

## Command Recipes

### Run all tests

```bash
cd ~/projects/boom
cargo test
```

### Run a targeted test

```bash
cargo test test_conf -- --nocapture
```

### Run format and basic hygiene checks

```bash
cargo fmt --check
pre-commit run --all-files
```

### Run a subsystem while debugging

```bash
RUST_LOG=info,boom=debug cargo run --bin scheduler -- --config config.yaml ztf
```

### Check containers during debugging

```bash
docker compose ps
docker compose logs broker
docker compose logs mongo
```

## Screenshot Placeholders

- [ ] passing `cargo test`
- [ ] one failing environment-dependent run
- [ ] scheduler logs during a debug session
- [ ] one metrics or telemetry screen if available
- [ ] one checklist or handwritten debugging flow

## Engineering Takeaways

- Good debugging starts with identifying the layer that failed.
- Reproducible commands are part of the engineering deliverable.
- Tests, traces, and manual request flows complement each other.
- Deployment awareness improves local debugging because it explains system shape.

## Data view
### UROP notes that reference this concept
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

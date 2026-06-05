---
type: output
status: seed
created: 2026-04-25
updated: 2026-04-25
tags:
  - output
track:
  - systems
output_kind: portfolio-bullet
source_concepts:
  - "[[Observability and Tracing]]"
  - "[[Kafka Redis and Workers]]"
  - "[[API and Backend]]"
---

# BOOM Systems Engineering Bullet

## Portfolio Bullet

**BOOM Alert Broker — Systems Engineering (Rust)**

Built and instrumented a multi-stage astronomical alert processing pipeline in Rust. Worked across Kafka stream ingestion, Redis task queues, MongoDB storage, JWT authentication, and structured tracing with OpenTelemetry. Added function-boundary observability using `tracing::instrument`, reducing debugging time from guesswork to localized span diagnosis. Presented observability architecture at UROP symposium.

**Stack**: Rust, Actix Web, Kafka, Redis, MongoDB, Docker Compose, OpenTelemetry, Prometheus

## Quantified Impact

- Instrumented 6+ subsystem boundaries with structured tracing spans
- Built presentation site with interactive trace walkthroughs for 2 API request paths
- Set up full local infrastructure (5 backing services) via Docker Compose profiles

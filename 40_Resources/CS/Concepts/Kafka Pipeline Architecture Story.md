---
type: output
status: seed
created: 2026-04-25
updated: 2026-04-25
tags:
  - output
track:
  - systems
output_kind: interview-story
source_concepts:
  - "[[Kafka Redis and Workers]]"
  - "[[Docker WSL and Local Setup]]"
---
# Kafka Pipeline Architecture Story
## STAR Format
### Situation
BOOM processes astronomical survey alert streams that arrive at high throughput. The system needed to ingest external data, queue internal work, and process it through multiple stages (alert parsing, enrichment, filtering) without losing data or creating bottlenecks.
### Task
Understand and work with a staged processing architecture where Kafka handles external streams, Redis handles internal task queues, and typed worker pools process data through MongoDB before emitting results downstream.
### Action
Worked with the Kafka producer (replaying archived ZTF alerts into topics) and consumer (draining topics into Redis queues). Learned the responsibility split: Kafka is the external stream layer (high-throughput, ordered, durable), Redis is the internal handoff layer (simple, fast, ephemeral). Set up the full local infrastructure using Docker Compose — MongoDB, Redis/Valkey, Kafka broker, OpenTelemetry collector, Prometheus — and debugged common failures: missing topics, broker health issues, environment variable mismatches.
### Result
Could explain the full data flow from survey stream to API response: surveys publish to Kafka → consumers push to Redis → alert workers parse and normalize → enrichment workers add cross-match data → filter workers evaluate user logic → passing alerts emit to Kafka output topic. This architecture pattern — external stream + internal queue + worker pools — transfers directly to ML pipelines, event-driven microservices, and data platform work.
## Why This Story Works
- Shows understanding of distributed system boundaries
- Demonstrates hands-on infrastructure work (Docker, Kafka, Redis)
- The pattern is universal: most data-intensive backends use some version of this
- Can pivot to ML pipeline discussions naturally
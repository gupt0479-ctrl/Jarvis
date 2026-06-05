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
  - "[[Observability and Tracing]]"
  - "[[API and Backend]]"
---

# Observability Debugging Story

## STAR Format

### Situation

BOOM is a multi-stage astronomical alert broker built in Rust. Requests cross API, auth, Kafka, Redis, worker pools, and MongoDB. When something failed, the team had no structured way to localize which stage broke — just flat log lines and guesswork.

### Task

Add structured observability so that every request and background job produces a traceable span tree. The goal: when a failure happens, you should be able to point to the exact function, the exact stage, and the exact context fields that explain what went wrong.

### Action

Instrumented function boundaries across the API and worker system using `tracing::instrument` with named spans, skipped sensitive fields, and structured context (route, topic, batch size, model path). Added `TracingLogger` middleware so every HTTP request gets a root span with nested child spans for auth, validation, and handler execution. Extended worker lifecycle spans to cover startup, heartbeat, processing, and shutdown.

Built the presentation site's "Trace Anatomy" section showing two concrete request walkthroughs: `POST /api/auth` (login + token creation) and `GET /api/catalogs` (protected route validation + handler execution).

### Result

The malformed auth header became the cleanest debugging story: a request sent `Bearer <token>`, decode failed, and the trace localized the failure to `auth::decode_token` immediately. The difference between "something failed" and "this specific span failed because the request header was malformed" — that is what structured tracing buys you.

The observability work became a legitimate engineering deliverable presented at the UROP symposium, not just a debugging convenience.

## Why This Story Works

- Shows systems thinking: observability is a subsystem, not an afterthought
- Demonstrates concrete technical depth: crates, middleware, span design
- Has a clear before/after: guesswork → localized diagnosis
- Transfers to any backend or ML system with multiple processing stages

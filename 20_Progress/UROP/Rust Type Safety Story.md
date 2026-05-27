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
  - "[[20_Progress/UROP/Learning/Rust Patterns in BOOM]]"
  - "[[20_Progress/UROP/Learning/API and Backend]]"
---

# Rust Type Safety Story

## STAR Format

### Situation

BOOM is a Rust backend with multiple binaries (API server, scheduler, Kafka consumer/producer, CLI tools) sharing a common library. The codebase needed to be correct across survey-specific logic, pipeline contracts, and error propagation — without the safety nets of garbage collection or runtime type checking.

### Task

Learn how Rust's type system enforces correctness in a real backend: traits as pipeline contracts, typed error propagation with `thiserror`, config as a first-class system concept, and observability at function boundaries.

### Action

Studied six applied Rust patterns in BOOM: (1) shared library with multiple binaries, (2) traits defining pipeline contracts across surveys, (3) typed errors instead of string messages, (4) `src/conf.rs` controlling runtime behavior as part of program correctness, (5) `#[instrument]` making function boundaries into observability boundaries, (6) async I/O plus explicit worker threads for realistic concurrency.

Traced the auth flow through `src/api/auth.rs` to see how typed JWT claims (`sub`, `iat`, `exp`), explicit error types, and instrumented spans work together. A wrong config value or malformed token gets caught at compile time or produces a clear trace — not a silent runtime failure.

### Result

Can explain the difference between Rust's compile-time contract enforcement and Go/Java's runtime approach. Can point to concrete BOOM files that demonstrate each pattern. The key insight: Rust doesn't just prevent memory bugs — it shapes better backend architecture by forcing explicit boundaries, typed errors, and clear ownership.

## Why This Story Works

- Shows language-level systems thinking, not just syntax knowledge
- Grounded in a real codebase with specific files and patterns
- Transfers to any discussion about type safety, error handling, or backend architecture
- Demonstrates ability to read and reason about production Rust code

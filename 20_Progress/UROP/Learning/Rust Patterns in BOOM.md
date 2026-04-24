---
type: concept
status: sprout
created: 2026-04-23
updated: 2026-04-27
tags:
  - concept
  - evergreen
notes:
  - "[[Rust]]"
  - "[[Rust/04 Async Traits and Concurrency]]"
  - "[[Learning/API and Backend]]"
track:
  - systems
prerequisites:
  - "[[BOOM]]"
  - "[[Rust]]"
used_in:
  - "[[API Work]]"
  - "[[Symposium]]"
evidence:
  - "[[60_Claude/45_Outputs/Rust Type Safety Story]]"
difficulty: 4
mastery_level: novice
drill_interval: 7
last_drilled: 2026-04-25
next_drill: 2026-05-02
---
# Rust Patterns in BOOM

## Deep Dive

### One-Sentence Version

BOOM uses Rust's type system, trait contracts, explicit errors, and function-boundary instrumentation to build a backend that is correct by construction rather than by convention.

### What It Is

Six applied Rust patterns visible in BOOM: shared library with multiple binaries, traits as pipeline contracts, typed error propagation, config as a first-class system concept, observability at function boundaries, and async-plus-threads for realistic concurrency.

### Why It Matters

These patterns show how Rust shapes real backend systems — not just syntax exercises. Understanding them transfers to any typed systems language and to backend architecture decisions in general.

### Real Example

BOOM's `src/conf.rs` controls runtime behavior, service connectivity, secrets, feature toggles, and environment-specific startup. This is not boring setup code — it is part of the program's correctness. A wrong config value can silently change system behavior in ways that only surface under load or in production.

### Contrast With

- **Traits vs interfaces (Go/Java)**: Rust traits enforce contracts at compile time with zero-cost abstraction. Go interfaces are satisfied implicitly. Java interfaces require explicit `implements`. Rust catches contract violations before the code runs.
- **Typed errors vs string errors**: BOOM uses `thiserror` for explicit error types. This means error propagation is type-checked, traces are cleaner, and debugging is faster than chasing string messages.
- **Async + threads vs async-only**: BOOM uses both async I/O and explicit worker threads. Most tutorials pretend async solves everything. BOOM shows the realistic picture.

### Source Anchors

- `src/lib.rs` — module map and shared library structure
- `src/conf.rs` — config as first-class system concept
- `src/api/auth.rs` — typed error and instrumentation example
- `src/utils/o11y/logging.rs` — observability at function boundaries

This note connects Rust language concepts to actual BOOM design choices.

Related notes:

- [[Rust]]
- [[Rust/04 Async Traits and Concurrency]]
- [[Rust/05 Macros Serialization and Config]]
- [[Learning/API and Backend]]
- [[Learning/Observability and Tracing]]

## Why This Note Matters

This note is about applied Rust rather than isolated syntax. The goal is to see how the language shapes a real backend system.

## Pattern 1: One Shared Library, Many Binaries

BOOM uses the standard systems-project shape:

- shared library modules in `src/*`
- multiple executables in `src/bin/*`

That allows the project to expose:

- API server
- scheduler
- Kafka consumer
- Kafka producer
- CLI tools

without duplicating shared logic.

## Pattern 2: Traits As Pipeline Contracts

Traits help BOOM define common behavior across surveys and processing stages.

That matters because the project needs:

- a shared pipeline shape
- survey-specific logic where necessary
- strong typing instead of stringly conventions

## Pattern 3: Typed Errors

BOOM leans on explicit error types instead of informal strings.

Benefits:

- better propagation
- clearer debugging
- cleaner traces
- easier maintenance

## Pattern 4: Config As A First-Class System Concept

`src/conf.rs` is not boring setup code. It controls:

- runtime behavior
- service connectivity
- secrets and credentials
- feature toggles
- environment-specific startup decisions

This is a key systems lesson: configuration is part of the program.

## Pattern 5: Observability At Function Boundaries

Instrumented functions are a clean design pattern in BOOM:

- a function boundary becomes an observability boundary

That keeps the code readable while making runtime behavior visible.

## Pattern 6: Async Plus Threads

BOOM is useful because it shows both:

- async I/O
- explicit worker-thread orchestration

That is a more realistic picture of systems programming than pretending async solves everything.

## Command Recipes

### Search important Rust patterns

```bash
cd ~/projects/boom
rg -n "trait |impl |#\\[instrument|thiserror::Error|pub mod |tokio::main|actix_web::main" src
```

### Open the most instructive files

```bash
sed -n '1,200p' src/lib.rs
sed -n '1,240p' src/conf.rs
sed -n '1,260p' src/api/auth.rs
sed -n '1,260p' src/utils/o11y/logging.rs
```

## Screenshot Placeholders

- [ ] module map from `src/lib.rs`
- [ ] typed error example
- [ ] one instrumented function
- [ ] one async entrypoint

## Engineering Takeaways

- Rust encourages better boundaries in backend code.
- Good types, explicit errors, and clear ownership improve service quality.
- BOOM is a useful Rust codebase because the patterns are real, not academic.

## Data view
### UROP notes that reference this concept
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

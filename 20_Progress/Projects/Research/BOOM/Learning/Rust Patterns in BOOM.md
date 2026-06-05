---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Rust]]"
  - "[[04 Async Traits and Concurrency]]"
  - "[[API and Backend]]"
---
# Rust Patterns in BOOM

This note connects Rust language concepts to actual BOOM design choices.

Related notes:

- [[Rust]]
- [[04 Async Traits and Concurrency]]
- [[05 Macros Serialization and Config]]
- [[API and Backend]]
- [[Observability and Tracing]]

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

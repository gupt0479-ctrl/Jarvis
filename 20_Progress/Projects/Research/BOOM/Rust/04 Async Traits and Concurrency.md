---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Rust]]"
  - "[[Kafka Redis and Workers]]"
  - "[[05 Macros Serialization and Config]]"
---
# Async Traits and Concurrency

BOOM is useful because it shows both async I/O and explicit threaded workers.

Related notes:

- [[Rust]]
- [[Kafka Redis and Workers]]

## Why This Note Matters

Many explanations of Rust concurrency are too abstract. BOOM gives you a concrete backend example where different concurrency models exist together for good reasons.

## Async Rust

BOOM uses async for:

- HTTP request handling
- MongoDB I/O
- Redis I/O
- Kafka-related I/O

Common entrypoint patterns:

```rust
#[tokio::main]
async fn main() { }
```

```rust
#[actix_web::main]
async fn main() -> std::io::Result<()> { }
```

## Threads And Worker Pools

BOOM also uses explicit worker threads and scheduling logic.

Why that matters:

- async is not the only concurrency tool
- long-running worker management often benefits from explicit lifecycle control

This is more realistic than pretending every system is pure async.

The scheduler source is a strong example:

- the outer service is async
- worker management still uses explicit thread pools
- heartbeat and shutdown are coordinated through signals and channels

## Traits In Concurrent Systems

Traits help BOOM share behavior across:

- survey-specific producers
- survey-specific consumers
- enrichment models
- worker interfaces

They provide a contract while still allowing different implementations.

This matters in BOOM because the overall pipeline shape is similar across surveys, but the concrete implementations differ. Traits let the repo share architecture without collapsing every survey into one giant file.

## Channels And Coordination

The scheduler uses channels or similar coordination primitives to:

- signal shutdown
- control workers
- keep lifecycle behavior explicit

This is an important engineering lesson: concurrency is not just parallel execution; it is also safe coordination.

## What To Watch For In The Code

- async entrypoints
- worker startup and shutdown
- trait-based abstractions
- thread spawning
- queue polling loops

## Command Recipes

### Search async entrypoints and functions

```bash
cd ~/projects/boom
rg -n "async fn|tokio::main|actix_web::main" src
```

### Search thread and channel usage

```bash
rg -n "thread::spawn|mpsc::|channel\\(" src
```

### Search traits

```bash
rg -n "^pub trait|^trait " src
```

### Open concurrency-heavy files

```bash
sed -n '1,240p' src/bin/scheduler.rs
sed -n '1,260p' src/scheduler/base.rs
sed -n '1,260p' src/kafka/base.rs
```

## Screenshot Placeholders

- [ ] async entrypoint in `src/bin/api.rs`
- [ ] scheduler thread or worker startup code
- [ ] one trait definition from Kafka or enrichment code
- [ ] one worker lifecycle trace

## Engineering Takeaways

- Async handles I/O efficiently, but threads still matter for system orchestration.
- Traits are part of how BOOM scales across surveys without duplicating the pipeline.
- Coordination and shutdown behavior are as important as the work itself.

## Data view
### Other Rust notes
```dataview
TABLE status, created
FROM "20_Progress/UROP/Rust"
WHERE file.path != this.file.path
SORT file.name ASC
```

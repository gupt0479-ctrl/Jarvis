---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Rust Patterns in BOOM]]"
  - "[[BOOM]]"
  - "[[01 Rust Basics Through BOOM]]"
---
# Rust

This note is the landing page for Rust-as-used-in-BOOM.

The goal here is not abstract language theory. The goal is to understand enough Rust to read BOOM confidently, debug it, extend it, and carry the useful systems habits into later AI/ML engineering work.

## Why Rust Matters In This Folder

BOOM uses Rust because it needs:

- long-running binaries
- explicit error handling
- strong typing
- safe concurrency
- predictable behavior in infrastructure code

Those are directly relevant to:

- backend engineering
- data systems
- model-serving systems
- platform and infra work

## Recommended Reading Order

1. [[01 Rust Basics Through BOOM]]
2. [[02 Ownership Borrowing and Lifetimes]]
3. [[03 Result Option and Error Handling]]
4. [[04 Async Traits and Concurrency]]
5. [[05 Macros Serialization and Config]]
6. [[06 Reading BOOM Code Effectively]]
7. [[Rust Patterns in BOOM]]

## BOOM Files Worth Revisiting While Learning Rust

- `src/lib.rs`
- `src/conf.rs`
- `src/bin/api.rs`
- `src/bin/scheduler.rs`
- `src/api/auth.rs`
- `src/kafka/base.rs`
- `src/utils/o11y/logging.rs`

## Command Recipes

### Open the repo

```bash
cd ~/projects/boom
```

### Build BOOM

```bash
cargo build
```

### Search for common Rust patterns

```bash
rg -n "impl |trait |enum |struct |Result<|Option<|async fn|#\\[instrument" src
```

### Open the crate layout

```bash
sed -n '1,120p' src/lib.rs
find src/bin -maxdepth 1 -type f | sort
```

## Screenshot Placeholders

- [ ] `src/lib.rs` showing BOOM's module layout
- [ ] `src/bin/api.rs` showing a real Rust entrypoint
- [ ] `src/conf.rs` showing typed config handling
- [ ] one screenshot of search results for traits or async functions

## Engineering Takeaways

- Rust is teaching disciplined systems habits, not just syntax.
- BOOM is a good Rust codebase because it shows real services, queues, and observability.
- The best way to learn Rust here is by tying each concept to a BOOM file.

## Data view
### Rust note set
```dataview
TABLE status, created
FROM "20_Progress/UROP/Rust"
SORT file.name ASC
```

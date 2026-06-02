---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Rust]]"
  - "[[Rust Patterns in BOOM]]"
  - "[[BOOM]]"
---
# Reading BOOM Code Effectively

This note is about how to read a large Rust codebase without getting lost.

Related notes:

- [[Rust]]
- [[Rust Patterns in BOOM]]
- [[BOOM]]

## Why This Note Matters

The hard part of BOOM is not just Rust syntax. It is navigation. This note gives you a method for reading the repo in a disciplined way.

## A Good Reading Order

When you open BOOM after time away, do not start randomly.

Use this order:

1. `src/lib.rs`
2. `src/bin/api.rs`
3. `src/bin/scheduler.rs`
4. `src/conf.rs`
5. `src/api/*`
6. `src/kafka/*`
7. `src/enrichment/*`
8. `src/filter/*`
9. `src/utils/o11y/*`

Why this order works:

- it moves from shape to entrypoints to details

If you are rereading BOOM specifically for Rust practice, there is an even tighter four-file loop:

1. `src/conf.rs`
2. `src/api/auth.rs`
3. `src/kafka/base.rs`
4. `src/enrichment/base.rs`

Why these four:

- `conf.rs` teaches typed config, `Result`, borrowing, and instrumentation
- `auth.rs` teaches service structs, JWT flow, async methods, and tracing
- `kafka/base.rs` teaches traits, external clients, error handling, and instrumentation
- `enrichment/base.rs` teaches worker loops, queues, BSON conversion, metrics, and generics

## What To Ask At Each File

For each file, ask:

- is this an entrypoint, shared module, or implementation detail?
- what types are central here?
- what does this file own?
- what does it borrow or call into?
- what failure modes are visible in signatures?
- where would I add instrumentation if this failed?

Apply those questions directly:

### `src/conf.rs`

- what does the config loader own versus borrow?
- which errors come from config parsing versus DB or Redis connection?
- where are environment variables merged into typed state?

### `src/api/auth.rs`

- which methods are low-level JWT helpers and which are higher-level app logic?
- where are errors preserved and where are they converted?
- what context fields are attached to auth spans?

### `src/kafka/base.rs`

- which functions are plain helpers and which are trait methods?
- where does external-client configuration happen?
- where are topic names, bootstrap servers, and group IDs carried as structured fields?

### `src/enrichment/base.rs`

- where does queue input become typed Rust values?
- what is generic over `T` and why?
- where are worker metrics updated?

## How To Read Function Signatures

A Rust function signature already tells you a lot:

- ownership and borrowing
- async or sync behavior
- error behavior
- type shape

That is why reading signatures first is efficient.

Four signatures worth studying repeatedly:

```rust
pub fn load_raw_config(filepath: &str) -> Result<Config, BoomConfigError>
pub async fn build_db(conf: &AppConfig) -> Result<mongodb::Database, BoomConfigError>
pub async fn validate_token(&self, token: &str) -> Result<String, jsonwebtoken::errors::Error>
pub async fn fetch_alerts<T: for<'a> serde::Deserialize<'a>>(...)
```

Together they cover:

- borrowing
- typed errors
- async service code
- generics with trait bounds

## How To Read Large Modules

Use this method:

1. scan imports
2. identify main structs and enums
3. identify the main public functions and traits
4. ignore internal details until the external shape makes sense

This reduces the feeling that everything is important at once.

That strategy works especially well on `kafka/base.rs` and `enrichment/base.rs`, because both files are large and mix:

- traits
- helper functions
- external clients
- metrics
- worker logic

If you try to read them top-to-bottom without first finding the contracts, they feel much harder than they really are.

## How To Use Search Well

Prefer search patterns that follow concepts, not filenames.

Useful queries:

- instrumentation
- traits
- route handlers
- worker loops
- error enums
- config loading

Concrete searches for this repo:

```bash
rg -n "load_raw_config|build_db\\(|AuthProvider|validate_token|decode_token" src
rg -n "pub trait|initialize_topic|check_kafka_topic_partitions|count_messages" src/kafka/base.rs
rg -n "EnrichmentWorker|fetch_alerts|run_enrichment_worker|rpop|lpush" src/enrichment/base.rs
```

## Command Recipes

### Start with the module map

```bash
cd ~/projects/boom
sed -n '1,120p' src/lib.rs
find src/bin -maxdepth 1 -type f | sort
```

### Search by concept

```bash
rg -n "#\\[instrument|trait |enum .*Error|web::Data|thread::spawn|Collection<" src
```

### Read entrypoints first

```bash
sed -n '1,220p' src/bin/api.rs
sed -n '1,220p' src/bin/scheduler.rs
sed -n '1,260p' src/conf.rs
```

### Then read the four high-value Rust study files

```bash
sed -n '1,260p' src/conf.rs
sed -n '1,260p' src/api/auth.rs
sed -n '1,260p' src/kafka/base.rs
sed -n '1,280p' src/enrichment/base.rs
```

## Screenshot Placeholders

- [ ] top-level module map
- [ ] one annotated function signature
- [ ] search results for instrumentation
- [ ] your own handwritten code-reading flow
- [ ] one screenshot marking the four-file Rust study loop

## Engineering Takeaways

- Large codebases become manageable when you read them in layers.
- Entry points and signatures are usually more valuable than line-by-line reading at first.
- The four-file loop (`conf.rs`, `auth.rs`, `kafka/base.rs`, `enrichment/base.rs`) is a good BOOM-specific Rust refresher.
- This same reading method works on non-Rust repos too.

## Data view
### Other Rust notes
```dataview
TABLE status, created
FROM "20_Progress/UROP/Rust"
WHERE file.path != this.file.path
SORT file.name ASC
```

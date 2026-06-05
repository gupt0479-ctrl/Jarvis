---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Rust]]"
  - "[[01 Rust Basics Through BOOM]]"
  - "[[03 Result Option and Error Handling]]"
---
# Ownership Borrowing and Lifetimes

This is the Rust concept that matters most when reading BOOM.

Related notes:

- [[Rust]]
- [[01 Rust Basics Through BOOM]]

## Why This Note Matters

If Rust feels strict, ownership is usually the reason. Once you understand ownership and borrowing, the BOOM codebase becomes much more readable because the signatures stop looking arbitrary.

## Ownership

Every value in Rust has one owner. When ownership moves, the original binding usually cannot use the value anymore.

Why this matters:

- resources have clear lifetimes
- mutation is easier to reason about
- hidden aliasing bugs are reduced

In a backend system like BOOM, this matters because there are many long-lived resources:

- config
- DB handles
- Redis connections
- auth state
- worker state

Rust forces the code to say which parts are shared, borrowed, moved, or cloned.

## Borrowing

Many BOOM helpers borrow state instead of consuming it.

## File-Based Examples

### `src/conf.rs`: borrow config, return owned DB state

```rust
#[instrument(skip_all, fields(
    host = %conf.database.host,
    port = conf.database.port,
    name = %conf.database.name,
), err)]
pub async fn build_db(conf: &AppConfig) -> Result<mongodb::Database, BoomConfigError> {
```

What this teaches:

- `conf: &AppConfig` means the function reads shared configuration without taking ownership
- the returned `mongodb::Database` is an owned runtime handle
- this is a very common service pattern: borrow inputs, build owned state

Why this is a good design:

- the same `AppConfig` can be reused by DB, Redis, API, scheduler, and worker setup
- the function does not need to own config because it only reads fields from it

### `src/api/auth.rs`: borrow config and DB into a constructor

```rust
pub async fn new(
    auth_config: &AuthConfig,
    db: &mongodb::Database,
) -> Result<Self, std::io::Error> {
```

What this teaches:

- constructors often borrow external state and return an owned service object
- the auth provider does not own the original config object or database binding
- it builds the pieces it needs and stores owned/clonable runtime state internally

This is a realistic backend pattern:

- borrow startup dependencies
- build owned service state
- inject that service state into the application

## Mutable Borrowing

When a function needs to mutate through a reference, it must declare `&mut`.

Why that matters:

- mutation becomes visible in the type signature
- side effects are easier to spot

In BOOM, this matters especially in worker code where mutable self or mutable receivers represent evolving runtime state.

## Lifetimes In Practice

You do not need to become a lifetime expert immediately.

The practical rules for BOOM are:

- borrowed data cannot outlive its owner
- returning owned values is often simpler than returning references
- if the compiler complains about lifetimes, it is asking you to prove the borrow is safe

BOOM often avoids visible lifetime complexity by returning owned values:

- `build_db` returns an owned database handle
- `AuthProvider::new` returns an owned provider
- worker constructors return owned worker state

That is a practical lesson:

- if you can return an owned value cheaply and sanely, you often avoid lifetime complexity

## Ownership Decisions Worth Noticing In BOOM

### Clone shared runtime handles, do not fight the borrow checker forever

In `src/bin/api.rs`, shared state is cloned into `web::Data`:

- config
- database
- auth provider
- email service

This is intentional:

- these are long-lived runtime resources
- cloning handles is often the correct design
- trying to thread borrows through a long-lived server would be worse

### Borrow inputs at function boundaries, own long-lived state

This pattern appears repeatedly:

- borrow config or DB into a constructor
- return owned runtime state
- clone that runtime state into services

That is a useful systems-programming habit to reuse later.

## BOOM-Relevant Places To Look

- borrowed config in `src/conf.rs`
- borrowed DB handles in `src/api/auth.rs`
- shared state injection via `web::Data`
- references passed into worker or helper functions

## Common Mistakes To Watch For

- thinking `&T` is a copy instead of a borrow
- cloning too early just to silence the compiler
- ignoring whether a function takes ownership or only borrows

Two BOOM-specific mistakes to avoid:

- assuming a MongoDB handle must never be cloned
- assuming every borrowed argument implies complicated lifetime logic later

Usually in this repo, borrowed inputs are just a clean way to build owned service state.

## Command Recipes

### Search for borrowed arguments

```bash
cd ~/projects/boom
rg -n "&AppConfig|&Database|&str|&mut" src
```

### Search for constructors that borrow inputs

```bash
rg -n "pub async fn new\\(|pub fn new\\(" src/conf.rs src/api/auth.rs src/enrichment/base.rs
```

### Search for clones

```bash
rg -n "\\.clone\\(" src
```

### Open borrowed-state examples

```bash
sed -n '1,220p' src/conf.rs
sed -n '1,260p' src/api/auth.rs
sed -n '1,220p' src/bin/api.rs
```

## Screenshot Placeholders

- [ ] borrowed config example in `src/conf.rs`
- [ ] borrowed DB example in `src/api/auth.rs`
- [ ] shared `web::Data` example in `src/bin/api.rs`
- [ ] one screenshot annotating `&AppConfig` and `&mongodb::Database`

## Engineering Takeaways

- Ownership is a way to control hidden state, not just a compiler obstacle.
- Borrowing encourages cleaner function boundaries.
- Returning owned runtime state is often a good way to reduce lifetime complexity.
- The discipline Rust forces here is useful in any large service or data pipeline.

## Data view
### Other Rust notes
```dataview
TABLE status, created
FROM "20_Progress/UROP/Rust"
WHERE file.path != this.file.path
SORT file.name ASC
```

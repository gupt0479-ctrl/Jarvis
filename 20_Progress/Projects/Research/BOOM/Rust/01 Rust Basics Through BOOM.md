---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Rust]]"
  - "[[Rust Patterns in BOOM]]"
  - "[[02 Ownership Borrowing and Lifetimes]]"
---
# Rust Basics Through BOOM

This note introduces Rust using patterns that appear immediately in the BOOM codebase.

Related notes:

- [[Rust]]
- [[Rust Patterns in BOOM]]

## Why This Note Matters

This is the onboarding note for reading BOOM. The goal is to make Rust feel concrete instead of foreign.

## What A Rust Project Looks Like

BOOM uses one crate plus multiple binaries:

- shared library: `src/lib.rs`
- executables: `src/bin/*.rs`

That means:

- core logic lives in reusable modules
- binaries reuse that logic
- the project can expose multiple entrypoints without duplication

## Basic Syntax You See Constantly

### Variables

```rust
let port = config.api.port;
let mut validation = Validation::new(Algorithm::HS256);
```

Key idea:

- values are immutable by default
- `mut` makes mutation explicit

### Functions

```rust
pub fn load_dotenv() { }
```

```rust
pub async fn build_db(conf: &AppConfig) -> Result<mongodb::Database, BoomConfigError> { }
```

Read that second signature as:

- `pub` = callable from other modules
- `async` = can await I/O
- `&AppConfig` = borrow the config instead of taking ownership
- `Result<..., ...>` = failure is part of the contract

### Structs

Rust uses structs to group related state.

BOOM example pattern:

- auth providers
- config objects
- worker state
- data models

### Enums

Enums model controlled sets of possibilities.

BOOM uses that idea for things like:

- survey type
- CLI modes
- worker behavior
- error categories

## What To Notice While Reading BOOM

- function signatures tell you a lot
- module structure is explicit
- types reveal ownership and failure
- public versus private fields matter

## Concrete BOOM Examples

Three real patterns from BOOM are especially useful when learning the language:

### Example 1: configuration and return types

```rust
pub async fn build_db(conf: &AppConfig) -> Result<mongodb::Database, BoomConfigError>
```

This single signature teaches:

- borrowing with `&AppConfig`
- async I/O
- typed success value
- typed error value

### Example 2: application startup

```rust
#[actix_web::main]
async fn main() -> std::io::Result<()> { ... }
```

This shows that Rust entrypoints can be async and still return typed errors.

### Example 3: structured application state

The API constructs config, DB, auth, and email service values and injects them with `web::Data`.

## Command Recipes

### Open the module map and entrypoints

```bash
cd ~/projects/boom
sed -n '1,120p' src/lib.rs
sed -n '1,160p' src/bin/api.rs
sed -n '1,160p' src/bin/scheduler.rs
```

### Search for structs and enums

```bash
rg -n "struct |enum " src
```

### Search for public async functions

```bash
rg -n "pub async fn" src
```

## Screenshot Placeholders

- [ ] `src/lib.rs` showing module layout
- [ ] `src/bin/api.rs` showing a Rust main function
- [ ] one struct definition from BOOM
- [ ] one enum definition from BOOM

## Engineering Takeaways

- Rust code becomes easier once you learn to read signatures carefully.
- Types are part of the documentation.
- BOOM is a good project for learning Rust because the code solves real problems.

## Data view
### Other Rust notes
```dataview
TABLE status, created
FROM "20_Progress/UROP/Rust"
WHERE file.path != this.file.path
SORT file.name ASC
```

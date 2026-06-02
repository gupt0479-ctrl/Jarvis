---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Rust]]"
  - "[[Observability and Tracing]]"
  - "[[MongoDB Data Model and Filters]]"
---
# Macros Serialization and Config

This note covers three BOOM-heavy topics that appear everywhere once the basics click.

Related notes:

- [[Rust]]
- [[Observability and Tracing]]
- [[MongoDB Data Model and Filters]]

## Why This Note Matters

These three topics explain a lot of "real project Rust":

- macros reduce project-wide boilerplate
- serialization defines system boundaries
- configuration controls runtime behavior

## Macros

Important macro patterns in BOOM:

- `#[derive(...)]`
- `#[tracing::instrument(...)]`
- `log_error!`
- `as_error!`

Why they matter:

- they reduce repetition
- they enforce conventions
- they make observability and serialization practical at scale

## File-Based Examples

### `src/conf.rs`: instrumentation on config helpers

```rust
#[instrument(err, fields(path = %filepath))]
pub fn load_raw_config(filepath: &str) -> Result<Config, BoomConfigError> {
```

What this teaches:

- macros are not only for deriving traits
- `#[instrument]` attaches context to config loading without manual logging boilerplate
- config code becomes observable like business logic code

### `src/api/auth.rs`: instrumentation on auth functions

```rust
#[tracing::instrument(
    name = "auth::create_token",
    skip(self, user),
    fields(user_id = %user.id, token_expiration = self.token_expiration),
    err
)]
pub async fn create_token(...)
```

What this teaches:

- `name` gives the span a stable readable label
- `skip` avoids logging heavy or sensitive values
- `fields` attaches structured runtime context
- `err` records failures automatically

### `src/utils/o11y/logging.rs`: helper macros as project conventions

The logging module defines:

- `log_error!` for structured error events
- `as_error!` for ergonomic closures in `inspect_err`-style flows

That is a useful pattern:

- project-specific macros can encode logging conventions once and reuse them everywhere

## Serialization Boundaries

BOOM moves data between several formats:

- Avro
- Rust structs
- BSON
- JSON

This is one of the strongest backend lessons in the project:

- data is transformed across multiple boundaries, and each boundary can fail or distort meaning

BOOM is a strong example because the same alert may exist as:

- Avro on the input stream
- Rust structs in processing code
- BSON in MongoDB
- JSON in API responses

### `src/enrichment/base.rs`: BSON back into typed Rust values

```rust
let alert: T = mongodb::bson::from_document(document)?;
```

What this teaches:

- typed Rust code is recovering domain values from BSON documents at runtime
- deserialization is part of the worker pipeline, not only the API layer

## Config

`src/conf.rs` is worth deep study because it shows:

- typed configuration loading
- environment overrides
- connection-string construction
- secrets and runtime knobs

This is not secondary boilerplate. It is systems behavior encoded in Rust.

### `src/conf.rs`: config is also transformation logic

The config code does more than deserialize a file. It also:

- searches for `.env` in more than one location
- merges file config with `BOOM_*` environment overrides
- builds MongoDB URIs from typed fields
- builds Redis connection strings from typed fields

This is an important systems lesson:

- configuration is both data and logic

## Questions To Ask While Reading

- what does this macro generate or standardize?
- what data format is crossing the boundary here?
- is this config value optional, required, or environment-specific?
- where is a typed Rust value being turned into text, BSON, or JSON?
- where is untyped external data being reintroduced into typed Rust?

## Command Recipes

### Search macros

```bash
cd ~/projects/boom
rg -n "#\\[derive|#\\[instrument|log_error!|as_error!" src
```

### Search serialization and format boundaries

```bash
rg -n "serde|serde_json|bson|avro|to_document|from_document" src
```

### Open config-heavy files

```bash
sed -n '1,260p' src/conf.rs
sed -n '1,220p' src/utils/o11y/logging.rs
```

### Open the BSON-heavy worker file

```bash
sed -n '1,280p' src/enrichment/base.rs
```

## Screenshot Placeholders

- [ ] one `#[instrument]` example
- [ ] one `derive` example from a data model
- [ ] one BSON or JSON conversion site
- [ ] config builder code in `src/conf.rs`
- [ ] one screenshot of `log_error!` or `as_error!`

## Engineering Takeaways

- Macros are a maintainability tool when used to encode consistent patterns.
- Serialization boundaries are where data systems often break.
- Config is part of the system's behavior, not an afterthought.
- BOOM is valuable because it shows all three interacting in one real service.

## Data view
### Other Rust notes
```dataview
TABLE status, created
FROM "20_Progress/UROP/Rust"
WHERE file.path != this.file.path
SORT file.name ASC
```

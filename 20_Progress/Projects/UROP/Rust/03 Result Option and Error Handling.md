---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Rust]]"
  - "[[Observability and Tracing]]"
  - "[[04 Async Traits and Concurrency]]"
---
# Result Option and Error Handling

This is the Rust pattern that most directly improves backend quality in BOOM.

Related notes:

- [[Rust]]
- [[Observability and Tracing]]

## Why This Note Matters

If you learn one Rust backend habit from BOOM, learn this:

- model failure explicitly

That habit transfers directly into Python services, ML pipelines, and production debugging.

## `Option<T>`

Use `Option<T>` when something may or may not be present.

Examples in BOOM:

- optional config fields such as replica-set values
- optional Kafka username and password
- optional CLI config path
- optional token expiration returned to clients

`Option<T>` means absence is expected and not necessarily an error.

This distinction matters:

- `Option<T>` = "absence is allowed"
- `Result<T, E>` = "the operation itself may fail"

## `Result<T, E>`

Use `Result<T, E>` when an operation can fail.

Example shape:

```rust
pub fn load_raw_config(filepath: &str) -> Result<Config, BoomConfigError>
```

This tells you:

- success returns a value
- failure returns a typed error

## File-Based Examples

### `src/conf.rs`: one error enum covers multiple failure classes

```rust
#[derive(thiserror::Error, Debug)]
pub enum BoomConfigError {
    #[error("failed to load config ({0})")]
    InvalidConfigError(#[from] config::ConfigError),
    #[error("failed to connect to database using config")]
    ConnectMongoError(#[from] mongodb::error::Error),
    #[error("failed to connect to redis using config")]
    ConnectRedisError(#[from] redis::RedisError),
    #[error("could not find config file")]
    ConfigFileNotFound,
    #[error("missing key in config: {0}")]
    MissingKeyError(String),
}
```

What this teaches:

- BOOM does not treat config failure as one vague string
- different low-level sources are preserved as explicit variants
- `#[from]` supports automatic conversion when using `?`

### `src/api/auth.rs`: different layers expose different error types

```rust
pub async fn decode_token(&self, token: &str) -> Result<Claims, jsonwebtoken::errors::Error>
pub async fn validate_token(&self, token: &str) -> Result<String, jsonwebtoken::errors::Error>
pub async fn authenticate_user(&self, token: &str) -> Result<User, std::io::Error>
```

What this teaches:

- lower-level helpers keep JWT-specific errors
- higher-level application methods may convert them into a more app-facing error type
- that is a deliberate layering choice

### `src/enrichment/base.rs`: worker errors encode pipeline-specific failure reasons

```rust
#[derive(thiserror::Error, Debug)]
pub enum EnrichmentWorkerError {
    #[error("error from mongodb")]
    Mongodb(#[from] mongodb::error::Error),
    #[error("error from redis")]
    Redis(#[from] redis::RedisError),
    #[error("failed to read config")]
    ReadConfigError(#[from] conf::BoomConfigError),
    #[error("failed to run model")]
    RunModelError(#[from] ModelError),
    #[error("missing cutouts for candid {0}")]
    MissingCutouts(i64),
}
```

What this teaches:

- one worker stage can fail for many different reasons
- the enum documents those reasons explicitly
- once tracing records `error = %e`, the typing becomes operationally useful

## The `?` Operator

```rust
let conf = Config::builder()
    .add_source(File::from(path))
    .build()?;
```

Meaning:

- if `build()` fails, return the error immediately from the current function

In BOOM, `?` appears constantly in:

- config loading
- MongoDB setup
- Redis setup
- BSON conversion
- worker loops

When you see `?`, ask:

- what error type is this function returning?
- is the lower-level error being preserved or converted?

## Manual Conversion Versus Automatic Conversion

Rust gives you several patterns in BOOM:

- `?` when `From` exists
- `map_err(...)` when the error needs reshaping
- `inspect_err(...)` when logging or tracing side effects are useful
- `ok_or(...)` / `ok_or_else(...)` when turning absence into an error

That mix is realistic backend Rust. Not every failure path can be treated identically.

## Questions To Ask While Reading

- is absence normal here, or is it an error?
- where does this error get converted or propagated?
- what information is preserved in the error type?
- is `?` enough here, or did the author use `map_err` or `inspect_err` for a reason?

These questions make you a better backend engineer, not just a better Rust reader.

## Command Recipes

### Search for `Result` and `Option`

```bash
cd ~/projects/boom
rg -n "Result<|Option<" src
```

### Search for error types

```bash
rg -n "thiserror::Error|enum .*Error" src
```

### Search for the `?` operator

```bash
rg -n "\\?;" src
```

### Search for manual error conversion

```bash
rg -n "map_err|inspect_err|ok_or|ok_or_else" src/conf.rs src/api/auth.rs src/kafka/base.rs src/enrichment/base.rs
```

## Screenshot Placeholders

- [ ] typed error enum in `src/conf.rs`
- [ ] auth method with `Result<..., jsonwebtoken::errors::Error>`
- [ ] one useful `?` chain in config or DB initialization
- [ ] one screenshot of `EnrichmentWorkerError`

## Engineering Takeaways

- Explicit failure is a design strength.
- Good error types preserve meaning across layers.
- BOOM shows how error modeling and tracing reinforce each other.
- If you can classify failures well in code, you can diagnose them faster at runtime.

## Data view
### Other Rust notes
```dataview
TABLE status, created
FROM "20_Progress/UROP/Rust"
WHERE file.path != this.file.path
SORT file.name ASC
```

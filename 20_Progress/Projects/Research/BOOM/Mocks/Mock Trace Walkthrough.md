---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Observability and Tracing]]"
  - "[[Postman Demo]]"
  - "[[Logs]]"
---
# Mock Trace Walkthrough

This note gives a simplified trace walkthrough to explain structured tracing in BOOM.

Related notes:

- [[Observability and Tracing]]
- [[Postman Demo]]
- [[Logs]]

## Example Request

A client sends:

```http
GET /api/catalogs
Authorization: Bearer <token>
```

## Without Tracing

Without structured tracing, you might only see separate lines like:

- request received
- auth failed
- base64 error

That leaves too many unanswered questions:

- Which endpoint?
- Which stage failed?
- Was it middleware or the handler?
- Was the token malformed or expired?

## With Tracing

A simplified trace tree looks like:

```text
HTTP request { method=GET, route=/api/catalogs }
  auth::middleware { path=/api/catalogs }
    auth::authenticate_user { token_len=190 }
      auth::validate_token
        auth::decode_token
  catalogs::get_catalogs { get_details=false }
```

## How to Read This

### Root span

`HTTP request`

- the whole request lifecycle
- usually created by middleware like `TracingLogger`

### Auth middleware span

`auth::middleware`

- tells you the request entered the protected route layer

### Auth helper spans

`authenticate_user`, `validate_token`, `decode_token`

- these pinpoint exactly which auth stage failed or succeeded

### Route span

`catalogs::get_catalogs`

- this confirms whether the request actually reached the handler

## Real Debugging Use

If the request contains `Bearer <token>` with literal angle brackets:

- the token decode stage fails
- the handler span likely never becomes relevant

That means the error is:

- not a MongoDB error
- not a catalogs route bug
- not a server startup issue

It is an auth header formatting issue.

## Why This Matters

The whole value of tracing is that it turns:

- "something failed"

into:

- "this request failed in this step for this reason"

That is the core idea behind your observability work in BOOM.

## Command Recipes

### Search for the auth and route tracing paths

```bash
cd ~/projects/boom
rg -n "authenticate_user|validate_token|decode_token|get_catalogs|TracingLogger" src
```

## Screenshot Placeholders

- [ ] `/api/catalogs` request trace
- [ ] auth failure trace for malformed bearer token
- [ ] one screenshot with the trace tree annotated by hand

## Data view
### Notes that reference this walkthrough
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

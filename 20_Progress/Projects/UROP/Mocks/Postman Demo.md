---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Postman Demo]]"
  - "[[API Work]]"
  - "[[Symposium]]"
---
# Mock Postman Demo Flow
This note is the stripped-down demo version of the Postman workflow. The main operational note is [[Postman Demo]].
## Goal
Use this note when you want a short live demo script for the API and tracing during a presentation or quick walkthrough.

## Demo Setup

Environment variables:

- `baseUrl = http://127.0.0.1:4000`
- `token = <set automatically after login>`

Requests to keep ready:

- `POST {{baseUrl}}/api/auth`
- `GET {{baseUrl}}/api/catalogs`

## Demo Sequence

### Step 1: show login request

- Method: `POST {{baseUrl}}/api/auth`
- Body type: `x-www-form-urlencoded`
- Fields:
  - `username = admin`
  - `password = admin`

Test script:

```javascript
if (pm.response.code === 200) {
  const json = pm.response.json();
  pm.environment.set("token", json.token);
}
```

What to say:

- This proves the auth route works.
- It also gives me a token I can reuse without copying it manually.

### Step 2: show protected route

- Method: `GET {{baseUrl}}/api/catalogs`
- Header: `Authorization: Bearer {{token}}`

What to say:

- This proves the token works through middleware and that the protected route can be reached successfully.

### Step 3: connect it to tracing

What to say:

- While I send the request in Postman, the terminal shows the request trace tree.
- That lets me compare the human action in Postman with the system behavior in BOOM.

## Best Demo Story

If I want one compelling bug story:

- send or describe `Authorization: Bearer <token>` with literal angle brackets
- explain that auth decoding failed
- explain that tracing made it obvious the bug was request formatting, not a database or route failure

## Command Recipes

### Run the API for the demo

```bash
cd ~/projects/boom
RUST_LOG=info,boom=debug OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317 cargo run --bin api
```

### Fallback curl version

```bash
curl -X POST http://127.0.0.1:4000/api/auth \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin"
```

## Screenshot Placeholders

- [ ] Postman collection with two saved requests
- [ ] terminal side-by-side with request trace
- [ ] one slide-ready screenshot of login plus token capture

## Data view
### Related UROP notes
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

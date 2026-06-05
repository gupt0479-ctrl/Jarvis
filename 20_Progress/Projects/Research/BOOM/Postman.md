---
type: project
status: sprout
related_progress:
  - "[[BOOM]]"
  - "[[API Work]]"
  - "[[Logs]]"
  - "[[API and Backend]]"
tags:
  - "#progress"
---
# Postman and Manual API Testing

This note explains how Postman fit into the BOOM workflow and why it mattered for your tracing work.

## Why This Note Matters

Postman was the shortest path from:

- "I changed backend code"

to:

- "I can prove the route, auth path, and trace behavior all work together"

That makes it a useful engineering tool, not just a demo tool.

## What Postman Helped You Validate

- login flow
- bearer token handling
- protected route behavior
- response payload shape
- trace alignment with real requests

## Recommended Environment

```text
baseUrl = http://127.0.0.1:4000
token = <set automatically after login>
```

## Core Requests

### Request 1: login

Method:

```text
POST {{baseUrl}}/api/auth
```

Body:

- `x-www-form-urlencoded`
- `username = admin`
- `password = admin`

Test script:

```javascript
if (pm.response.code === 200) {
  const json = pm.response.json();
  pm.environment.set("token", json.token);
}
```

### Request 2: protected route

Method:

```text
GET {{baseUrl}}/api/catalogs
```

Header:

```text
Authorization: Bearer {{token}}
```

## Why These Two Requests Matter

Together they validate:

- request parsing
- auth route execution
- JWT creation
- token reuse in a protected route
- auth middleware
- route handler execution
- trace tree correctness

## Real Debugging Story

The best manual-testing story from this project:

- a token was sent as `Bearer <token>` with literal angle brackets
- decode failed
- tracing showed the error lived in the auth path
- the bug was diagnosed as formatting, not DB or route logic

That is exactly why Postman and tracing work well together.

## Good Postman Habits To Keep

- keep a small environment with only the variables you need
- automate token capture in the test script
- name requests by behavior, not by vague labels
- compare request actions against terminal traces after each important change

## Why Postman Mattered To The Website

The website's Postman section is not just a demo panel. It encodes a real engineering workflow:

- send a request
- watch the trace tree
- decide which subsystem handled or rejected the request

That is why Postman belongs in these notes. It was part of how you validated the observability work.

## Command Recipes

### Run the API

```bash
cd ~/projects/boom
RUST_LOG=info,boom=debug OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317 cargo run --bin api
```

### Compare login with curl

```bash
curl -X POST http://127.0.0.1:4000/api/auth \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin"
```

### Compare protected route with curl

```bash
curl http://127.0.0.1:4000/api/catalogs \
  -H "Authorization: Bearer <token>"
```

### Search API routes while building requests

```bash
rg -n "#\\[.*(get|post|patch|delete)" src/api/routes
```

## Screenshot Placeholders

- [ ] Postman environment variables
- [ ] login request configuration
- [ ] Postman test script that stores the token
- [ ] protected route request using `Authorization: Bearer {{token}}`
- [ ] terminal trace for `/api/auth`
- [ ] terminal trace for `/api/catalogs`

## Engineering Takeaways

- Postman is a backend debugging tool when paired with good logs and traces.
- Manual reproducibility matters when you are proving route behavior.
- A clean request recipe is part of good project documentation.

## Related Notes

- [[API and Backend]]
- [[Observability and Tracing]]
- [[API Work]]
- [[Logs]]

## Data view
### UROP notes that reference Postman
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

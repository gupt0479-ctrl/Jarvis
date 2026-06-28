---
type: input
status: sprout
created: 2026-06-21
updated: 2026-06-21
tags:
  - summary
  - github
notes:
  - "[[40_Resources/CS/Repos]]"
input_kind: github
track: systems
source_url: https://github.com/pocketbase/pocketbase
---
# pocketbase

**Repo:** `https://github.com/pocketbase/pocketbase`
**Stars:** 59,207 | **Forks:** 3,470 | **Language:** Go | **License:** MIT | **Last push:** 2026-06-20 (actively maintained)

## What It Is

An open-source backend distributed as a single Go binary: embedded SQLite with realtime subscriptions, built-in file and user management, an admin dashboard UI, and a REST-ish API. Pre-v1.0.0 — backward compatibility across versions is explicitly not guaranteed yet.

## Core Capabilities

- Realtime subscriptions over the embedded SQLite database
- Built-in auth, user management, and file storage — no separate services to wire up
- Admin dashboard UI shipped in the same binary
- Usable two ways: as a standalone prebuilt executable (`./pocketbase serve`), or as a Go framework/library for custom backend logic with the same single-binary deployment story
- Official JS and Dart SDK clients for the web API

## Why It Matters

Zero-infrastructure backend for any project needing auth + data + files without standing up Postgres, an auth provider, and S3 separately. Directly relevant as a Sanity alternative for the portfolio's data layer, or as the backend for any quick internal tool (agent dashboards, data collection forms) — one binary, runs locally or on a $5 VPS.

## Use Cases for Jarvis

- Backend for the portfolio site (auth, project/blog data, file storage) instead of a paid CMS subscription.
- Quick persistence layer for any throwaway tool or agent dashboard that needs more than flat files but doesn't justify a full Postgres setup.

## Tradeoffs

- Pre-v1.0.0: API and schema migrations may break between releases — pin a version for anything beyond experimentation.
- SQLite-backed: fine for single-server, low-to-moderate concurrent write workloads; not the right choice if the project will need horizontal write scaling.

## Related

- [[40_Resources/CS/Repos]] (Building section)

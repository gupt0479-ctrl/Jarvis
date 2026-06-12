---
tags: [portfolio, auth, clerk, middleware]
---

# Auth — Clerk

> [[../INDEX|← Back to Index]]

## Overview

Clerk guards **`/studio` only**. The portfolio itself is fully public — no auth required to view.

## Community 48 — Root Proxy (`proxy.ts`)

```
proxy.ts (root)
  ├── clerk          — Clerk client instance
  ├── isPublicRoute  — matcher for all public portfolio routes
  ├── event          — auth event handler
  ├── config         — Next.js middleware config (matcher)
  └── proxy()        — main middleware function (calls clerk)
```

`proxy()` → calls `clerk` → uses `isPublicRoute` to decide whether to enforce auth.

## Community 57 — Src Proxy (`src/proxy.ts`)

```
src/proxy.ts
  ├── isPublicRoute   — public route matcher
  ├── isStudioRoute   — /studio/* matcher
  └── config          — middleware matcher export
```

Two proxy files exist — check which one Next.js is actually using as `middleware.ts` before editing either.

## Route Rules

| Path | Auth Required | Notes |
|------|--------------|-------|
| `/` | No | Portfolio home |
| `/studio/*` | Yes | Sanity Studio — Clerk login |
| `/sign-in/*` | No | Clerk sign-in page |
| `/sign-up/*` | No | Clerk sign-up page |
| `/api/chat` | No | HMAC token + rate limit instead |
| `/api/chat-token` | No | Issues HMAC cookie |
| `/api/draft-mode/*` | Sanity secret | Draft mode enable/disable |

## Studio Layout — `src/app/studio/layout.tsx`

Clerk's server-side auth check runs here before rendering `StudioClient.tsx`. If unauthenticated, redirects to `/sign-in`.

## Chat Security (Not Clerk)

The `/api/chat` endpoint uses its own security stack independent of Clerk:
1. `isAllowedOrigin()` — checks `Origin` header against allowlist
2. HMAC token in cookie — issued by `/api/chat-token`
3. Upstash rate limiting — burst + daily limits per IP

See [[../chatbot/01-api-route|Chatbot API Route]] for full detail.

## Appearance Config

`src/lib/clerk-appearance.ts` — custom Clerk modal styling to match the cosmic dark theme.

---
type: project
status: active
updated: 2026-06-15
tags: [portfolio, security, index]
---

# Portfolio Security — Master Index

> Ground truth as of 2026-06-15. Every finding verified against actual source files — not guesses.

---

## Phase Map

| Phase | File | Focus | Status |
|-------|------|--------|--------|
| 1 | [[phase-1-auth-clerk]] | Clerk appearance + Studio auth chain | **✅ Done — verify once** |
| 2 | [[phase-2-sanity-lockdown]] | Two-token setup, browserToken scope, CORS, no mutations | **⚠️ Verify token scopes in Sanity dashboard** |
| 3 | [[phase-3-chatbot-resilience]] | HMAC gate, rate limits, Cerebras→Groq→Mistral chain | **✅ Solid — minor info-leak in /api/health** |
| 4 | [[phase-4-deployment-hardening]] | Env vars, CSP enforcement gap, VERCEL_URL origin | **🔴 CSP still Report-Only — must flip before launch** |
| 5 | [[phase-5-monitoring]] | Health endpoint auth issue, uptime monitoring, rollback | **⚠️ /api/health is Clerk-gated — fix for UptimeRobot** |

---

## What's actually built (verified by reading the code)

### Authentication
- Clerk middleware in `proxy.ts` protects all routes not in the public list
- Public routes: `/`, `/sign-in`, `/sign-up`, `/api/sanity(.*)`, `/api/draft-mode(.*)`, `/api/chat(.*)`
- `/studio` is NOT in public routes → Clerk's `auth.protect()` fires → redirect to sign-in
- `clerk-appearance.ts` has a proper dark cosmic theme — readable, not pitch-black

### Sanity
- Two tokens: `SANITY_SERVER_API_TOKEN` (server fetch, no CDN) and `SANITY_API_TOKEN` (browserToken for Live API)
- Neither has `NEXT_PUBLIC_` prefix — both are server-only in env terms
- BUT: `SANITY_API_TOKEN` is passed as `browserToken` to Sanity's Live Content API, which means the SDK sends it to the browser via SSE. It MUST be a read-only "Viewer" token.
- Zero mutation calls in Next.js layer (grep confirmed) — Sanity Studio is the only write path
- Draft mode `/api/draft-mode/enable` gated by `SANITY_REVALIDATE_SECRET`

### Chatbot (Orby)
- **Model chain: Cerebras → Groq → Mistral → degraded** (NOT Gemini — Gemini is gone)
- Budget tiering: messages 1–10 start at Cerebras; messages 11+ skip to Groq
- Per-provider 30s cooldown in Upstash on failure
- HMAC-SHA256 token: 1-hour TTL, `httpOnly + secure + sameSite=strict` cookie
- Rate limits: burst 10/60s per IP, daily 100/24h per IP (not 10/10s as old notes said)
- Message validation: max 20 messages, content must be string ≤ **4000** chars (not 2000), system-role injection blocked
- Origin check covers localhost:3000, localhost:3001, `NEXT_PUBLIC_BASE_URL`, and `VERCEL_URL` (auto per-deployment)
- Scraper UA block, chat sanitizer strips pseudo-tool markup from model output

### Security Headers (next.config.ts)
- HSTS: max-age=63072000; includeSubDomains; preload ✅
- X-Content-Type-Options: nosniff ✅
- X-Frame-Options: DENY ✅ (more restrictive than old notes recommended)
- Referrer-Policy: strict-origin-when-cross-origin ✅
- Permissions-Policy: camera=(), microphone=(), geolocation=() ✅
- **CSP: `Content-Security-Policy-Report-Only` — NOT enforced.** TODO comment in next.config.ts confirms it must flip to `Content-Security-Policy` before launch.

---

## How to use these files

Two synthesis files drive the actual work session:

**[[claude-code-prompts]]** — every prompt you paste into Claude Code, in order, labelled P1-A through P5-D. Start here when you open Claude Code in the repo.

**[[manual-actions]]** — every step that requires a browser or dashboard (Sanity manage, Clerk dashboard, Vercel settings, UptimeRobot). A table at the bottom splits every task between you and Claude Code so nothing is missed.

Session order: run prompts P1-A → P4-F, pausing for dashboard steps when indicated, then add all Vercel env vars (manual-actions 4A), push to `main`, and run P5-D after the deploy is live.

---

## The two things that must happen before launch

1. **Flip CSP from Report-Only to enforced** (`next.config.ts` line change) — Phase 4 Step 2
2. **Make `/api/health` public** for UptimeRobot monitoring — Phase 5 Step 1

Everything else is already in good shape or requires Sanity dashboard verification, not code changes.

---

## What is explicitly NOT in scope

- **SQL injection** — no SQL database; Sanity is document-based
- **XSS via stored content** — no user-generated content; Sanity Studio requires Clerk login to write
- **CSRF** — Next.js App Router Server Actions use built-in CSRF tokens; no traditional form POST
- **DDoS at infrastructure level** — Vercel handles this; Upstash rate limiting handles app-level abuse
- **Prompt injection via user message** — mitigated by system-prompt framing, refusal rules, and RULES block in `buildSystemPrompt()`. Not 100% eliminable at the application layer.

---

## Stack context

| Layer | Tech | Security mechanism |
|-------|------|--------------------|
| Framework | Next.js 16 App Router | Security headers in next.config.ts |
| Auth | Clerk | Middleware protects /studio; sidebar/Orby is public |
| CMS | Sanity v4 Live API | Two read-only tokens; CORS locked; Studio is write-only interface |
| AI | Cerebras → Groq → Mistral → degraded | Server-only keys; HMAC gate; rate limiting; cooldown |
| Rate limiting | Upstash Redis | Burst (10/60s) + daily (100/24h) per-IP |
| Deploy | Vercel | HTTPS enforced; VERCEL_URL per-deployment in origin allowlist |

---

## Files in this folder

```
security/
  README.md                       ← you are here (ground-truth index)
  phase-1-auth-clerk.md           ← Clerk appearance + studio auth chain (done)
  phase-2-sanity-lockdown.md      ← token scopes, CORS, no mutations
  phase-3-chatbot-resilience.md   ← HMAC gate, rate limits, model chain, input validation
  phase-4-deployment-hardening.md ← CSP enforcement gap, env audit, smoke tests
  phase-5-monitoring.md           ← health endpoint fix, uptime, incident playbook
```

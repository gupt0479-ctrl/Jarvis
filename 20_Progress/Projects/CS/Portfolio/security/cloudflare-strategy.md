---
type: project
status: sprout
created: 2026-06-16
tags: [portfolio, security, cloudflare, deployment, domain]
---

# Cloudflare Strategy — anantgupta.dev

> Decisions on OAuth, webhooks, Vercel vs Cloudflare hosting, and how to use Cloudflare to its full value without over-engineering a personal portfolio.

→ Prompts for Claude Code: [[claude-code-prompts#phase-6]]
→ Manual dashboard steps: [[manual-actions#phase-6]]

---

## Verdict: OAuth (Clerk SSO)

**Not needed. Skip it.**

The Clerk page you found is about enterprise SSO — SAML and OIDC for multi-tenant apps where companies sign in with their organization's identity provider (Google Workspace, Okta, etc.). That's for B2B SaaS, not a personal portfolio.

Your current setup: Google OAuth via Clerk. That's the only person who needs to sign in is you, to access Sanity Studio. Google is sufficient. Adding GitHub, LinkedIn, or other providers just increases the attack surface for zero user benefit.

**What you already have is correct. Do not change it.**

---

## Verdict: Webhooks

### Sanity webhooks — already set up, verify they work

Sanity webhooks fire when you publish content in Studio. They call your `/api/draft-mode` (or a revalidate endpoint) with `SANITY_REVALIDATE_SECRET`, triggering Next.js ISR to refresh cached pages. This is what makes your portfolio update within seconds of a Sanity publish rather than on the next full deploy.

The env var `SANITY_REVALIDATE_SECRET` already exists in your codebase (confirmed in Phase 2). The webhook just needs to be configured in Sanity dashboard pointing at your production URL.

**Action required (manual):** Go to `sanity.io/manage` → project → **API** → **Webhooks**. Confirm a webhook exists pointing to `https://anantgupta.dev/api/revalidate` (or wherever the revalidate route is). If it doesn't exist, create it — see [[manual-actions#phase-6]].

### Clerk webhooks — not needed

Clerk webhooks sync user lifecycle events (sign-up, sign-in, deletion) to your own database so you can maintain user records. You have no user database. The only person who signs in is you. There is nothing to sync.

**Skip Clerk webhooks entirely.**

---

## Verdict: Vercel vs Cloudflare hosting

**Keep Vercel. Use Cloudflare as the layer in front of it.**

The portfolio runs on Next.js 16 App Router with React Server Components, streaming, Clerk middleware, and Sanity Live API. Vercel built Next.js — their serverless infrastructure handles all of this natively. Cloudflare Pages has Next.js support but it lags behind: not all App Router features work, and the Clerk/Sanity integration would require rework.

The Cloudflare Workers chatbot quote you found ("instead of calling AI providers directly from the browser") describes a different architecture — one where a React SPA calls AI APIs from the client, exposing keys. **Your architecture does not do this.** Your flow is:

```
Browser → POST /api/chat (Vercel serverless function) → Cerebras/Groq/Mistral
```

The AI keys live in Vercel server env vars and never reach the browser. The concern is already solved by the current setup. Moving the chatbot to a Worker adds zero security benefit — it would just be a different place to store the same server-side secrets, with more complexity.

**Where Cloudflare genuinely adds value on top of Vercel:**

| Feature | What it does | Value |
|---------|--------------|-------|
| DNS + Proxy | Routes `anantgupta.dev` to Vercel; Cloudflare's network sits in front | DDoS protection, Anycast routing, edge caching |
| WAF (free) | Blocks known exploit patterns, vulnerability scanners, bad bots | Stops noise before it hits Vercel |
| Rate limiting (free tier: 1 rule) | Edge-level rate limit on `/api/chat` | Blocks abuse before Vercel functions are even invoked |
| Turnstile | Invisible bot challenge on chatbot load | Adds bot detection layer before HMAC token is issued |
| Analytics | Traffic, firewall events, bot scores | Real data on who's hitting the site |
| SSL | Manages TLS for `anantgupta.dev` | Works automatically |

This is the correct division: **Vercel runs the app, Cloudflare protects the perimeter.**

---

## The full Cloudflare setup plan

### Part 1 — Custom domain: `anantgupta.dev` → Vercel

Cloudflare already manages your domain's DNS. You need to add DNS records pointing to Vercel.

**Vercel gives you a CNAME target** (something like `cname.vercel-dns.com`). For the apex domain (`anantgupta.dev`), Cloudflare uses **CNAME flattening** — it resolves the CNAME at the edge and returns an A record, which lets apex domains work despite the DNS spec not allowing CNAMEs at root.

DNS records to add in Cloudflare (manual step — see [[manual-actions#phase-6]]):
```
Type   Name    Content                   Proxy
CNAME  @       cname.vercel-dns.com      ✅ Proxied (orange cloud ON)
CNAME  www     cname.vercel-dns.com      ✅ Proxied (orange cloud ON)
```

SSL mode: set to **Full (strict)** in Cloudflare SSL/TLS settings. This means Cloudflare encrypts to your origin (Vercel) using Vercel's own SSL cert. Without "strict", you get "Full" which is vulnerable to MITM between Cloudflare and Vercel.

In Vercel: add `anantgupta.dev` and `www.anantgupta.dev` as custom domains. Vercel will auto-issue its own cert for the Cloudflare→Vercel leg.

### Part 2 — WAF rules (Cloudflare dashboard, free)

Add these rules in Cloudflare → Security → WAF → Custom Rules:

**Rule 1: Block known scanner User-Agents**
```
(http.user_agent contains "sqlmap") or
(http.user_agent contains "nikto") or
(http.user_agent contains "nmap") or
(http.user_agent contains "masscan") or
(http.user_agent contains "zgrab") or
(http.user_agent contains "nuclei")
→ Action: Block
```

**Rule 2: Block empty User-Agent on API routes**
```
(http.request.uri.path contains "/api/") and
(http.user_agent eq "")
→ Action: Block
```

**Rule 3: Rate limit `/api/chat` at the edge**
In Security → WAF → Rate Limiting Rules:
- Expression: `http.request.uri.path eq "/api/chat"`
- Rate: 20 requests per 60 seconds per IP
- Action: Block for 60 seconds

This is a second rate-limit layer on top of Upstash — Cloudflare's fires at the edge before Vercel is even hit.

### Part 3 — Turnstile on the chatbot

Turnstile adds an invisible bot challenge when the sidebar opens. The flow:

```
User opens sidebar
  → Turnstile invisible challenge runs (no CAPTCHA for real users, <100ms)
  → Browser gets a Turnstile token
  → Token sent to /api/chat-token along with the HMAC request
  → Server verifies Turnstile token with Cloudflare's siteverify API
  → If valid: issues HMAC cookie as normal
  → If bot: returns 403 before HMAC is ever issued
```

This means bots cannot get a valid HMAC cookie in the first place, even if they somehow bypass the origin check.

**Cloudflare has a one-shot "Spin" skill** for this. The prompt for Claude Code is in [[claude-code-prompts#phase-6]]. It:
1. Creates the Turnstile widget via Cloudflare API
2. Deploys a managed `siteverify` Worker (small, purpose-built, handled by Cloudflare)
3. Writes the frontend widget code into the sidebar component
4. Writes the server-side verification into `/api/chat-token`

The Worker Cloudflare deploys is a tiny managed one (~20 lines). This is the correct use of Workers — a single-purpose edge function for token verification, not rewriting the entire chatbot.

### Part 4 — Analytics (Cloudflare dashboard, free)

In Cloudflare dashboard → Analytics → Traffic: you get:
- Total requests, unique visitors, bandwidth
- Bot score distribution (how much of your traffic is bots)
- Top countries, top paths
- Firewall events (WAF blocks, rate limit hits)

No code changes. Activated automatically once DNS is proxied through Cloudflare.

---

## What NOT to do

| Idea | Why to skip |
|------|-------------|
| Move chatbot to a Worker | Your AI keys are already server-only in Vercel. Moving them to a Worker is same security posture, more complexity |
| Cloudflare AI Gateway | Adds latency for zero security benefit in this architecture |
| Cloudflare Pages hosting | Vercel is better for Next.js App Router; would break Clerk + Sanity Live |
| D1, Durable Objects, KV | Wrong use case; you have no database needs |
| More OAuth providers | Not needed; only one user (you) ever signs in |
| Clerk webhooks | No user database to sync to |
| Cloudflare Email Routing | Not relevant |

---

## Updated architecture diagram

```
User
  │
  ▼
Cloudflare edge (anantgupta.dev)
  ├── WAF rules (scanner block, empty UA, API rate limit)
  ├── DDoS protection (automatic)
  ├── Turnstile siteverify Worker (for /api/chat-token)
  └── DNS proxy → Vercel
                    │
                    ├── GET / (portfolio page, RSC)
                    │     └── sanityFetch() → Sanity CDN
                    │
                    ├── GET /studio (Clerk auth → Sanity Studio)
                    │
                    ├── GET /api/chat-token
                    │     ├── Verify Turnstile token (calls CF siteverify Worker)
                    │     └── Issue HMAC cookie if valid
                    │
                    └── POST /api/chat
                          ├── isAllowedOrigin() — 403
                          ├── HMAC verify — 401
                          ├── Upstash rate limit — 429
                          └── Cerebras → Groq → Mistral → degraded
```

---

## Acceptance criteria

- [ ] `anantgupta.dev` resolves to Vercel (DNS configured in Cloudflare, proxied)
- [ ] `www.anantgupta.dev` redirects to apex (or vice versa — be consistent)
- [ ] SSL mode: Full (strict) in Cloudflare
- [ ] Vercel custom domains: both `anantgupta.dev` and `www.anantgupta.dev` added
- [ ] WAF: scanner UA block rule active
- [ ] WAF: empty UA on `/api/*` block rule active
- [ ] WAF: `/api/chat` rate limit rule active (20 req/60s)
- [ ] Turnstile widget created, siteverify Worker deployed
- [ ] `/api/chat-token` verifies Turnstile token before issuing HMAC cookie
- [ ] Sanity revalidate webhook pointing at `https://anantgupta.dev/api/revalidate` (or correct path)
- [ ] Cloudflare Analytics showing traffic after first real visitors

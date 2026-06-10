---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-10
tags:
  - portfolio
  - ai
  - security
notes:
  - "[[00 - Nextgen Chatbot — Build Plan]]"
  - "[[02 - Premortem & Failure Defenses]]"
  - "[[02 - Deploy Security Checklist]]"
---
# Model Layer, Rate Limiting & Abuse
This note owns the bottom layer (the model providers) and the gates around it: how it stays free, stays up under traffic, and cannot be abused. It is the fix for premortem failures 2, 5, and 6. The model call is the least interesting part; the gates are the work.
## Free, without a surprise bill or a dead bot
"Free" for an LLM means a free-tier model behind a thin server proxy that hides the key and rate-limits. Not client-side BYO-key (bad UX, leaks the key), not in-browser WebLLM (too heavy for a portfolio visit).
**Providers (June 2026 free tiers, no card):**
- **Primary — Google Gemini 2.5 Flash.** ~1,500 requests/day free, 1M-token context, decent tool-calling. At portfolio traffic this is effectively unlimited, and the big context window makes grounding easy.
- **Fallback — Groq (Llama 3.3 70B).** ~1,000 requests/day, 300+ tokens/sec — fast enough that Orby feels instant when it is serving.
The standing advice everywhere: never build on a *single* free tier. Stack them as fallback, not as capacity planning.
## The router and degraded mode
A thin router picks Gemini, falls back to Groq on quota-exhaustion or error. The model layer stays swappable — provider SDK or plain fetch at the bottom, everything above it provider-agnostic.
The critical piece is **degraded mode** for premortem failure 2: when *all* free quotas are gone (the traffic-spike scenario), the assistant does not throw an error at visitors. It falls back to the persona's pre-written answers and the deterministic navigation — Orby still works, just without live generation. A degraded Orby beats a broken Orby on the one day people are watching.
## Rate limiting and the per-IP cap
- **Per-IP cap:** ~50 messages/IP/day (tune from real logs), enforced with `@upstash/ratelimit` on Upstash Redis at the edge — the only managed Redis callable from edge functions, free tier covers this. Also a short burst limit (e.g. 10/min) to blunt rapid abuse.
- **Vercel WAF Attack Challenge Mode** (free on all plans) for DDoS/bot waves, plus blocking scraper user-agents (GPTBot etc.) in middleware. The KB guidance: block expensive endpoints at the edge before they reach the function.
## Origin-locking the endpoint (premortem 5)
Per-IP limits do not stop someone using `/api/chat` as their own free LLM from distributed IPs. So the endpoint only answers calls that began on my site:
- Check `Origin`/`Referer` against the real domain.
- Issue a short-lived **signed session token** from the page on load; the chat route requires a valid token. A scraper hitting the bare endpoint without a token gets nothing.
- Keep the model API keys server-only (never `NEXT_PUBLIC_`), consistent with [[02 - Deploy Security Checklist]].
## Content safety (premortem 6)
Two lines of defense, because the prompt-level rule can be bypassed:
1. **Prompt-level** — the non-overridable guardrail in every persona (see [[03 - Context Engine, Grounding & Personas]]).
2. **Output guard** — a lightweight check on the model's output before it reaches the UI; block or regenerate on hateful/inappropriate content or attempts to impersonate real people. The weirdo persona gets the strictest setting.
Optionally an input check that flags obvious injection ("ignore your instructions…") before it ever hits the model.
## Cost controls (the runtime budget)
Even on free tiers, bound each request so a single visitor cannot run up tokens or loop: a per-request token budget, a max-tool-step cap (e.g. 4) in the agent runtime, and a hard timeout on every model and tool call. These live in the agent runtime (see [[01 - Layered Architecture]]) but are listed here because they are part of staying free and safe.
## Note on free-tier data terms
Free tiers may log or train on prompts. For a public portfolio answering questions about already-public info, this is acceptable — but no secrets, tokens, or private data ever go into a prompt. Worth a one-line disclosure near Orby if we want to be clean about it.
## Open questions
Resolved for v1 (2026-06-10):
- [x] **Token issuance = a stateless HMAC-signed httpOnly cookie**, set on page load and verified at the edge with Web Crypto. This is the edge-optimal choice: no Redis or DB round-trip per chat call (the signature verifies locally), so it adds near-zero latency and no extra reads against the rate-limit store. The payload is tiny (issued-at + short TTL); rotate the signing secret via env. A tokenless or bad-signature request is rejected before it reaches the model.
- [x] **Clerk-authenticated higher cap = v2, together with persistent memory.** v1 treats everyone as anonymous under the 50/IP/day cap. In v2, a signed-in Clerk visitor unlocks two things at once: a higher cap and an episodic memory store keyed by Clerk `userId` (Supabase or Upstash), so the assistant remembers them across visits. This is the single most valuable v2 upgrade and the main reason Clerk is already in the stack — but it stays out of v1 to keep the build small.
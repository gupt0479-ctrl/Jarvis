---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-14
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
This note owns the bottom layer (the model providers) and the gates around it: how it stays free, stays up under traffic, and cannot be abused. It is the fix for premortem failures 2, 5, and 6. The model call is the least interesting part; the budget tiering, failover, and gates are the work.
## The finalized plan (2026-06-14)
One premium primary funded by free student credit, three free backups, and a budget tier so the credit barely depletes:
> **Azure OpenAI (GPT-4o-mini) → Cerebras → Groq → Mistral → degraded mode.**
Azure is the first call to Orby. The free chain catches everything past the per-session premium budget and everything Azure can't serve, so Orby never goes down and the $100 never gets billed past zero (Azure for Students stops at $0 — it never charges a card).
## Why this finally runs free
The earlier root cause: Gemini 2.5 Flash's free tier is now ~20 requests/day, which died instantly and had no backstop. Replaced by:
- **Primary — Azure OpenAI `gpt-4o-mini`**, paid from the **Azure for Students $100/yr credit** (no card, renews yearly, expires 06/14/2027 on the current grant). GPT-4o-mini is ~$0.15/$0.60 per million tokens (in/out) — premium quality at a price where $100 covers ~150,000–200,000 portfolio messages. Effectively a year of free premium.
- **Free backups (all high requests/day, OpenAI-compatible, vendor-diverse):**
  1. **Cerebras** `gpt-oss-120b` — 14,400 req/day, ~2,000 tokens/sec (fastest free inference), closest to premium quality.
  2. **Groq** `llama-3.1-8b-instant` — 14,400 req/day, very fast, different vendor/infra.
  3. **Mistral La Plateforme** `mistral-small` — 1 billion tokens/month, the deepest token reservoir; caps on tokens not requests, so it absorbs load when the request-capped legs are spent.
- **Degraded mode** — when every leg is exhausted, serve the persona's pre-written answers + deterministic navigation. A degraded Orby beats a broken one (premortem 2).
Gemma (Google) and OpenRouter were dropped from the core three: Google's free tier trains on prompts and has tight per-minute limits; OpenRouter free is only 50 req/day without a topup. Either can be an optional 4th floor, not a workhorse.
## Budget tiering — the cost mechanism
The cost rule is not "ration the model," it's "spend Azure where it earns its cost, then fall to free." Per session:
- **First ~10 messages → Azure (premium).** The first impression — a recruiter's opening questions — gets GPT-4o-mini.
- **Beyond ~10 → transparently fall to the free chain.** "Continue chatting" silently shifts from GPT-4o-mini to Cerebras `gpt-oss-120b`, which is barely a step down. The visitor never hits a wall.
- Track the per-session count against the signed session token / an Upstash key, so the tier survives across requests in a session.
This caps Azure spend per visitor while keeping quality at the moment it matters, and means even a heavy chatter costs at most ~10 cheap-model turns of credit.
## Cost levers (priority order — this is where the money is saved)
1. **Cache the persona drop-down questions.** They are a fixed set; cache the full result (answer + `orbyMessage` + `navigate` target) in Upstash keyed by `(persona + normalized question)`. These cost **zero** model calls — the biggest lever by far. TTL 24h or bust on a Sanity publish webhook.
2. **GPT-4o-mini, never GPT-4o/4.1-full** — ~30× cheaper and plenty for "answer questions about Anant."
3. **Cap `max_tokens` per reply (~300–400).** Orby answers are short; this bounds the expensive output tokens and keeps replies snappy.
4. **Keep the grounding payload small** — always-on catalog (titles/slugs/one-liners), full records only on demand (see [[03 - Context Engine, Grounding & Personas]]). Smaller input = lower cost every call.
With 1–4 in place, real Azure spend is a small fraction of the 150K-message ceiling. The budget will not bleed under legitimate traffic; the only real drain is abuse, handled next.
## The failover router
One router tries providers in priority order and fails over on any `429` / quota / `5xx` / network / timeout, marking the failed provider in a short Upstash cooldown before advancing. It returns the first success and records which provider answered (for tracing). Uniform implementation: Azure OpenAI, Cerebras (`api.cerebras.ai/v1`), Groq (`api.groq.com/openai/v1`), and Mistral (`api.mistral.ai/v1`) are all OpenAI-compatible, so the router is one function over a config array of `{baseURL, apiKey, model}` — reordering or adding a leg is a one-line change. Note the router serves two roles: **budget tiering** (deliberately route to free after the Azure session budget) and **failover** (route to the next leg on error). Same machinery, two triggers.
## Rate limiting and the per-IP abuse cap
The tiering handles cost; this handles a malicious actor — layers, not alternatives.
- **Per-IP cap:** a reasonably large hard ceiling, ~75–100 messages/IP/day, via `@upstash/ratelimit` on Upstash Redis at the edge, plus a burst limit (~10/min). Large enough that no real visitor is ever cut off; small enough that a single abuser can't loop thousands of calls.
- **Dev bypass:** an env-gated allowlist for Anant's IP so local testing doesn't trip the cap and look like a provider limit.
- **Vercel WAF Attack Challenge Mode** (free) for bot waves; block scraper user-agents in middleware.
## Origin-locking the endpoint (premortem 5)
Per-IP limits don't stop someone using `/api/chat` as their own free LLM from many IPs — and with a credit-backed Azure key on the line, that would drain real money. So the endpoint only answers calls that began on the site: check `Origin`/`Referer`, and require a short-lived stateless HMAC-signed httpOnly cookie issued on page load and verified at the edge (no DB round-trip). A tokenless or bad-signature call is rejected before the router runs. Keys stay server-only, never `NEXT_PUBLIC_` — consistent with [[02 - Deploy Security Checklist]]. This is the gate that makes exposing a paid Azure key safe.
## Content safety (premortem 6)
Two lines, because the prompt rule can be bypassed: the non-overridable guardrail in every persona (see [[03 - Context Engine, Grounding & Personas]]), and an output guard that blocks/regenerates hateful, inappropriate, or impersonating output before it reaches the UI. The weirdo persona gets the strictest setting.
## Cost controls (the runtime budget)
Bound each request so one visitor cannot loop or overspend: per-request token budget, max-tool-step cap (~4) in the agent runtime, hard timeout on every model and tool call. These keep both the Azure credit and the free chain safe.
## Note on data terms
Azure OpenAI does not train on your prompts (enterprise terms) — a real advantage of the premium primary over the free open tiers, several of which (Cerebras, Groq, Mistral free, Google) may log or train. Acceptable for a public portfolio answering already-public info, but no secrets ever enter a prompt.
## Resolved for v1 (2026-06-14)
- [x] **Primary** = Azure OpenAI `gpt-4o-mini` on the $100/yr student credit.
- [x] **Three backups** = Cerebras `gpt-oss-120b` → Groq `llama-3.1-8b-instant` → Mistral `mistral-small` → degraded mode.
- [x] **Budget tier** = first ~10 messages/session on Azure, then transparently to the free chain.
- [x] **Abuse cap** = ~75–100 msgs/IP/day hard ceiling + ~10/min burst, with a dev bypass.
- [x] **Token issuance** = stateless HMAC-signed httpOnly cookie, edge-verified.
- [x] **Caching** = exact-match Upstash cache for the fixed drop-down questions.
- [x] **More premium later** = Microsoft for Startups Founders Hub ($1,000+ Azure/OpenAI credit, no card, no VC needed) is the v2 way to extend the Azure budget. Clerk-keyed persistent memory also v2.

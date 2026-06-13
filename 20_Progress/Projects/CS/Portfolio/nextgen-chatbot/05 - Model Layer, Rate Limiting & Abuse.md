---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-13
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
This note owns the bottom layer (the model providers) and the gates around it: how it stays free, stays up under traffic, and cannot be abused. It is the fix for premortem failures 2, 5, and 6. The model call is the least interesting part; the gates and the failover are the work.
## Root cause of the rate-limit pain (2026-06-13)
"Orby keeps hitting the rate limit" traces to one mistake: **Gemini 2.5 Flash's free tier is now ~20 requests/day** on Google AI Studio (verified June 2026). Twenty requests is exhausted in minutes of testing, let alone real visitors. The original plan named Gemini primary + a Groq fallback that was never built — so the assistant runs on a 20/day quota with no backstop. The fix is two-part: move the primary off any low-RPD model, and build the multi-provider failover that was only ever designed, not implemented.
## Free, without a surprise bill or a dead bot
"Free" means a free-tier model behind a thin server proxy that hides the key and rate-limits. Not client-side BYO-key (leaks the key), not in-browser WebLLM (too heavy). The change from v1: pick providers by **requests-per-day**, not brand. Daily free limits that actually survive traffic (June 2026):
- **Cerebras** — 14,400 req/day, 1M tokens/day, ~2,000 tokens/sec (fastest free inference). Models: `gpt-oss-120b`, Llama 3.1 8B.
- **Groq** — Llama 3.1 8B Instant = 14,400 req/day; Llama 3.3 70B = 1,000/day. Very fast.
- **Google AI Studio — Gemma 3 27B/12B = 14,400 req/day** (use Gemma, *not* Gemini 2.5 Flash's 20/day; Gemini 3.1 Flash-Lite is 500/day if you want a Gemini).
- **Mistral La Plateforme** — 1 req/sec, 1B tokens/month. Generous on tokens, modest on rate.
- **OpenRouter** — an aggregator: one key → many free models, 50 req/day free (1,000 with a one-time $10 topup). The variety floor.
- **Cloudflare Workers AI** — 10,000 neurons/day, edge-native. Optional extra leg.
## The failover router (primary + at least 3 backups)
A single router tries providers in order and fails over on any `429` / quota / `5xx` / timeout, marking the failed provider in a short cooldown (in Upstash) before advancing. Orby never sees an error as long as one leg is alive. Recommended chain:
1. **Primary — Cerebras** (`gpt-oss-120b`). Highest combined RPD + speed; speed matters because Orby should feel instant.
2. **Backup 1 — Groq** (Llama 3.1 8B Instant). Fast, 14,400/day, different vendor + key.
3. **Backup 2 — Google AI Studio Gemma 3 27B**. 14,400/day, different infra entirely.
4. **Backup 3 — Mistral La Plateforme** (Mistral Small). Huge monthly token budget.
5. **Backup 4 — OpenRouter free models**. Aggregator last resort; one key, many models.
6. **Final floor — degraded mode.** When *every* leg is exhausted, serve the persona's pre-written answers + deterministic navigation (premortem 2). A degraded Orby beats a broken Orby.
Uniform implementation: every provider above except raw Gemma exposes an **OpenAI-compatible** endpoint (Cerebras `api.cerebras.ai/v1`, Groq `api.groq.com/openai/v1`, Mistral `api.mistral.ai/v1`, OpenRouter `openrouter.ai/api/v1`; Google has an OpenAI-compat shim at `generativelanguage.googleapis.com/v1beta/openai/`). So the router is one function over a config array of `{baseURL, apiKey, model}` — adding or reordering a provider is a one-line change. Keep the model layer thin and swappable; this chain proves the point.
## Caching — the real fix, not just more providers
Adding APIs is a backstop; the actual lever is **not calling an LLM for traffic you can predict**. Most portfolio chat traffic is the fixed persona drop-down questions — a known, finite set. Cache them:
- **Exact-match cache** in Upstash, keyed by `(persona + normalized question)`, storing the full result (answer text + `orbyMessage` + `navigate` target). The drop-down chips then cost **zero** LLM calls — they hit the cache. This alone removes the bulk of the load that exhausts quotas.
- TTL on entries (e.g. 24h) or bust on a Sanity publish webhook so edits propagate. Free-typed questions still go to the router live; only the predictable set is cached.
- Optional later: a semantic cache for near-duplicate free-typed questions.
Order of defense against rate limits: **cache first** (most traffic never reaches a model), **failover router next** (live traffic survives any one provider dying), **degraded mode last** (the floor).
## Rate limiting and the per-IP cap
- **Per-IP cap:** ~50 messages/IP/day (tune from logs), `@upstash/ratelimit` on Upstash Redis at the edge, plus a burst limit (~10/min). Note: during your own testing this self-cap can trip and *look* like a provider limit — add a dev bypass (an env-gated allowlist for your IP) so you stop conflating the two.
- **Vercel WAF Attack Challenge Mode** (free) for bot waves; block scraper user-agents in middleware.
## Origin-locking the endpoint (premortem 5)
Per-IP limits don't stop someone using `/api/chat` as their own free LLM from many IPs. So the endpoint only answers calls that began on the site: check `Origin`/`Referer`, and require a short-lived stateless HMAC-signed httpOnly cookie issued on page load and verified at the edge (no DB round-trip). A tokenless or bad-signature call is rejected before the router runs. Keys stay server-only, never `NEXT_PUBLIC_` — consistent with [[02 - Deploy Security Checklist]].
## Content safety (premortem 6)
Two lines, because the prompt rule can be bypassed: the non-overridable guardrail in every persona (see [[03 - Context Engine, Grounding & Personas]]), and an output guard that blocks/regenerates hateful, inappropriate, or impersonating output before it reaches the UI. The weirdo persona gets the strictest setting. Optionally flag obvious injection in the input.
## Cost controls (the runtime budget)
Bound each request so one visitor cannot loop or overspend even on free tiers: per-request token budget, max-tool-step cap (~4) in the agent runtime, hard timeout on every model and tool call. These live in the agent runtime (see [[01 - Layered Architecture]]) but matter here because they keep the free chain free.
## Note on free-tier data terms
Free tiers may log or train on prompts (Cerebras, Groq, Google outside the EEA, Mistral's free Experiment plan all have terms). Acceptable for a public portfolio answering already-public info — but no secrets ever enter a prompt. A one-line disclosure near Orby keeps it clean.
## Resolved for v1 (2026-06-13)
- [x] **Token issuance** = stateless HMAC-signed httpOnly cookie, edge-verified. No Redis round-trip per call.
- [x] **Provider chain** = Cerebras primary + Groq + Gemma 3 27B + Mistral + OpenRouter backups + degraded floor. Failover on 429/quota/5xx/timeout with cooldown. Replaces the old Gemini-primary/Groq-only plan that caused the 20-RPD failure.
- [x] **Caching** = exact-match Upstash cache for the fixed persona drop-down questions; live router only for free-typed questions.
- [x] **Clerk higher cap + persistent memory** = v2 (episodic store keyed by Clerk `userId`). v1 stays anonymous under the 50/IP/day cap.

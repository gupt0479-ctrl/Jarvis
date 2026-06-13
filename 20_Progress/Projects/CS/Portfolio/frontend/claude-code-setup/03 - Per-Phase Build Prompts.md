---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-13
tags:
  - portfolio
  - claude-setup
  - frontend
  - prompts
notes:
  - "[[00 - Frontend Build Kit — Index]]"
  - "[[05 - Model Layer, Rate Limiting & Abuse]]"
  - "[[09 - Orby UI Fixes]]"
  - "[[BUILD-STATUS]]"
---
# Per-Phase Build Prompts — Verification & Hardening Pass (V-phase)
> The UI refinement build (R0–R8) is **done**. This file is fresh: the post-build pass that makes the site reliable, fast, and publishable. Same rules — run each phase in its own `/clear` session, paste the prompt verbatim, let it finish + `pnpm typecheck`, eyeball, report. **Claude Code does NOT commit or deploy — Anant deploys.**
Path prefixes:
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`
`NB = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot`
## Scope of this pass (in order)
1. **Orby reliability + backups** — written below, the focus of this turn (V1, V2).
2. Background / health checks — folded into V2.
3. Performance of the whole site — *next.*
4. GitHub README — *next.*
5. Deployment (Vercel, headers, CSP) — *next.*
6. Nextgen chatbot end-to-end correctness — partly V2, rest *next.*
7. Keeping a clean GitHub (history, branches, secrets) — *next.*
8. Sanity content polish — *next.*
9. Codebase readability — *next.*
10. Professional write-ups — *next.*
11. Publishing elsewhere — *next.*
Only the Orby section is filled in now. The rest get prompts in the next passes so we don't fabricate steps before each is scoped.
---
# Orby reliability — why it keeps failing and what "always works" means
**Root cause (verified June 2026):** the assistant runs on **Gemini 2.5 Flash, whose free tier is now ~20 requests/day.** That quota dies in minutes. The original plan named a Groq fallback but it was **never built**, so there is no backstop. Full corrected design: [[05 - Model Layer, Rate Limiting & Abuse]].
**"Orby works at all times" = three layers of defense, in this order:**
1. **Cache first** — the persona drop-down questions are a fixed set; cache their full answers so most traffic never calls an LLM.
2. **Failover router next** — primary + at least 3 backups; if one provider 429s, fail over to the next.
3. **Degraded mode last** — when every provider is exhausted, serve persona pre-written answers + deterministic navigation. Orby still moves and speaks; it just stops generating live.
**The provider chain (high requests/day, mostly OpenAI-compatible):** Cerebras (primary, ~14,400/day + fastest) → Groq Llama 3.1 8B (14,400/day) → Google AI Studio **Gemma 3 27B** (14,400/day, NOT Gemini 2.5 Flash) → Mistral La Plateforme (1B tokens/month) → OpenRouter free (aggregator floor) → degraded mode.
**Prerequisite — get these free keys before V1** (all no-cost, most need only an email/phone): `CEREBRAS_API_KEY`, `GROQ_API_KEY`, `GOOGLE_API_KEY` (AI Studio, used for Gemma), `MISTRAL_API_KEY`, `OPENROUTER_API_KEY`. Put them in the repo's gitignored `.env.local` and in Vercel env. V1 fails over gracefully if some are missing, but the point is redundancy — provide as many as you can.
## V1 — Multi-provider failover router + cache + degraded mode
```
NB = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot
Read NB/05 - Model Layer, Rate Limiting & Abuse.md fully. Use the ai-engineer subagent. Retrofit the EXISTING /api/chat — do not rebuild the chatbot.
Build a provider-failover router for the chat model call:
1) Config array of providers in priority order, each {name, baseURL, apiKey from env, model}, all called through one OpenAI-compatible client:
   - Cerebras (gpt-oss-120b) primary; Groq (llama-3.1-8b-instant); Google AI Studio OpenAI-compat shim (gemma-3-27b-it); Mistral (mistral-small-latest); OpenRouter (a free model) last.
   - Skip any provider whose env key is missing, log which were skipped.
2) Try in order. On 429 / quota / 5xx / network / timeout: mark that provider in an Upstash cooldown (e.g. 60s, longer for a daily-quota 429), advance to the next. Return the first success. Record which provider answered (for tracing).
3) Exact-match response cache in Upstash keyed by (persona + normalized question), storing answer + orbyMessage + navigate target, TTL 24h. The fixed persona drop-down questions must hit this cache and make ZERO model calls. Free-typed questions go live to the router.
4) Degraded mode: if every provider fails/cooled, return the persona's pre-written canned answer + deterministic navigation, never an error. Orby still navigates and speaks a canned line.
5) Add a dev bypass for the per-IP rate limit (env-gated allowlist for Anant's IP) so local testing stops tripping the 50/day self-cap and getting mistaken for a provider limit.
VERIFY (report each): (a) a drop-down question returns from cache with no model call; (b) forcing the primary key invalid fails over to Groq and answers; (c) forcing ALL keys invalid returns degraded mode, not a 500; (d) the response surfaces which provider answered.
Run pnpm typecheck. Report. Do not deploy.
```
## V2 — Orby end-to-end + background health checks
```
NB = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot
FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend
Read NB/04 - Orby Integration.md, NB/09 - Orby UI Fixes.md, and FE/12 - Orby Friction Fixes.md fully. Use frontend-builder for UI, ai-engineer for the route.
Verify and fix Orby end to end:
1) Navigation pipeline: a chat reply that should navigate emits exactly ONE navigate(sectionId) with sectionId from the closed Sanity-nav enum; Orby returns to the portfolio-button home, the page scrolls to the real section, and the per-request creative message pops AFTER arrival. Confirm it is fully separate from the scroll popups (those still fire on scroll, unchanged).
2) Per-request message: free-typed questions get a unique, in-persona, grounded, output-guarded, length-capped line; drop-down questions may reuse cached lines; degraded mode uses canned persona lines.
3) Fail-safe: a malformed/unresolvable navigate does nothing visual and Orby answers in text only — never half-scrolls, never desyncs.
4) Robustness: prefers-reduced-motion (jump not animate, message still fires); 375px mobile no overlap/clip of the speech cloud at Orby's far-right home; one navigation per turn (ignore extra navigate calls).
5) Background health: add a lightweight /api/health (or a server log line) that reports, per provider, reachable / cooled-down / key-missing, and whether the cache is responding. This is how we SEE quota trouble before users do.
6) Tracing: every chat turn logs which provider answered (or cache/degraded), tool calls, and refusal/validation outcome.
VERIFY (report each): "show me your projects" → one scroll + one on-arrival message; malformed call → text only; reduced-motion path; mobile 375px clean; /api/health shows each provider's status.
Run pnpm typecheck. Report. Do not deploy.
```
## Order
Get the free keys → V1 (router/cache/degraded) → V2 (Orby end-to-end + health). After V2 reports green, the next pass covers performance, README, deployment/CSP, clean GitHub, Sanity polish, readability, write-ups, and publishing — prompts to be written then.

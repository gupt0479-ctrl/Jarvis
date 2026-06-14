---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-14
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
> The UI refinement build (R0–R8) is **done**. This file finalizes **Orby + the nextgen chatbot**: the free-forever model setup and Orby's reliability/UX. Same rules — run each phase in its own `/clear` session, paste the prompt verbatim, let it finish + `pnpm typecheck`, eyeball, report. **Claude Code does NOT commit or deploy — Anant deploys.**
Path prefixes:
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`
`NB = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot`
## Scope of this pass (in order)
1. **Orby model setup + reliability** — V1, V2 below, the focus of this build.
2. Background / health checks — folded into V2.
3. Performance, GitHub README, deployment/CSP, clean GitHub, Sanity content polish, codebase readability, professional write-ups, publishing — *next passes, prompts written then.*
Only Orby is finalized here.
---
# Orby — the finalized free-forever setup
**Root cause that's now fixed:** Orby ran on Gemini 2.5 Flash, whose free tier is ~20 requests/day, with no backstop. Full design: [[05 - Model Layer, Rate Limiting & Abuse]].
**The chain:** `Azure OpenAI gpt-4o-mini → Cerebras gpt-oss-120b → Groq llama-3.1-8b-instant → Mistral mistral-small → degraded mode.` Azure is the first call (premium, paid by the $100/yr student credit). The free legs catch everything past the per-session Azure budget and anything Azure can't serve.
**Three layers keep it free AND always-on:**
1. **Cache first** — the fixed persona drop-down questions hit an Upstash cache and make zero model calls.
2. **Budget tier** — first ~10 messages/session use Azure; beyond that it transparently falls to the free chain. Caps premium spend per visitor.
3. **Failover** — any provider 429/error spills to the next; if all are exhausted, degraded mode (canned persona answers + deterministic nav) so Orby never errors.
**Prerequisite keys (in repo `.env.local` + Vercel env) before V1:** `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_DEPLOYMENT` (a `gpt-4o-mini` deployment), `CEREBRAS_API_KEY`, `GROQ_API_KEY`, `MISTRAL_API_KEY`. The router skips any leg whose key is missing.
## V1 — Azure-primary router, budget tier, cache, cost caps
```
NB = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot
Read NB/05 - Model Layer, Rate Limiting & Abuse.md fully. Use the ai-engineer subagent. Retrofit the EXISTING /api/chat — do not rebuild the chatbot.
1) Provider chain, one OpenAI-compatible client over a config array {name, baseURL, apiKey, model} in priority order:
   - Azure OpenAI (gpt-4o-mini deployment) PRIMARY; then Cerebras (gpt-oss-120b); Groq (llama-3.1-8b-instant); Mistral (mistral-small). Skip any leg whose env key is missing and log it.
2) BUDGET TIER: track a per-session message count against the signed session token / an Upstash key. First ~10 messages of a session use Azure; from message 11 on, START the chain at Cerebras (skip Azure) so continued chatting costs no credit. Transparent to the user.
3) FAILOVER: on 429 / quota / 5xx / network / timeout, put that leg in a short Upstash cooldown and advance. Return the first success; record which provider answered.
4) COST CAPS on every Azure call: model gpt-4o-mini (never 4o/4.1-full); max_tokens ~350; keep the injected grounding payload small (always-on catalog + on-demand full records, not everything).
5) CACHE: exact-match Upstash cache keyed by (persona + normalized question) storing answer + orbyMessage + navigate target, TTL 24h. Drop-down persona questions MUST hit cache (zero model calls). Free-typed questions go live through the chain.
6) DEGRADED MODE: if every leg fails/cooled, return the persona's canned answer + deterministic navigation, never a 500.
7) ABUSE CAP: ~75–100 msgs/IP/day hard ceiling + ~10/min burst via @upstash/ratelimit, with an env-gated dev bypass for Anant's IP.
VERIFY (report each): (a) a drop-down question returns from cache, no model call; (b) messages 1–10 served by Azure, message 11+ served by Cerebras (budget tier works); (c) invalid Azure key fails over to Cerebras; (d) all keys invalid → degraded mode, not a 500; (e) response surfaces which provider answered.
Run pnpm typecheck. Report. Do not deploy.
```
## V2 — Orby end-to-end + health + persona UI
```
NB = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot
FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend
Read NB/04 - Orby Integration.md, NB/09 - Orby UI Fixes.md, NB/03 - Context Engine, Grounding & Personas.md, and FE/12 - Orby Friction Fixes.md fully. frontend-builder for UI, ai-engineer for the route.
Orby reliability + UX, end to end:
1) Navigation pipeline: a reply that should navigate emits exactly ONE navigate(sectionId) from the closed Sanity-nav enum; Orby returns to the portfolio-button home, the page scrolls to the real section, and the per-request creative message pops AFTER arrival. Fully separate from the scroll popups (unchanged).
2) Per-request message: free-typed questions get a unique, in-persona, grounded, output-guarded, length-capped line; drop-down questions reuse cached lines; degraded mode uses canned persona lines.
3) Fail-safe: a malformed/unresolvable navigate does nothing visual; Orby answers in text only — never half-scrolls or desyncs.
4) Robustness: prefers-reduced-motion (jump not animate, message still fires); 375px mobile no overlap/clip of the speech cloud at Orby's far-right home; one navigation per turn.
5) DEFAULT PERSONA = RECRUITER: when the sidebar opens, the Recruiter persona is selected by default (its system prompt active, its suggested chips shown). The other three (friend, weirdo, ceo) are one click away. Confirm the default is recruiter on every fresh open.
6) BACKGROUND HEALTH: add a lightweight /api/health (or server log) reporting per provider reachable / cooled-down / key-missing, plus cache responding and the current budget-tier state. This is how we see quota/credit trouble before users do.
7) TRACING: every chat turn logs which provider answered (Azure / Cerebras / Groq / Mistral / cache / degraded), the budget-tier decision, tool calls, and refusal/validation outcome.
VERIFY (report each): "show me your projects" → one scroll + one on-arrival message; malformed call → text only; reduced-motion path; mobile 375px clean; sidebar opens on Recruiter; /api/health shows each provider + tier state.
Run pnpm typecheck. Report. Do not deploy.
```
## Order
Get the keys (Azure deployment + Cerebras + Groq + Mistral) → V1 (router/tier/cache/caps) → V2 (Orby end-to-end + recruiter default + health). After V2 reports green, the next pass covers performance, README, deployment/CSP, clean GitHub, Sanity polish, readability, write-ups, and publishing.

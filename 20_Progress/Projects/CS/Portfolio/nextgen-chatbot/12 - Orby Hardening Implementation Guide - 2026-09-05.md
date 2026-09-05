---
type: concept
status: active
created: 2026-09-05
updated: 2026-09-05
tags:
  - portfolio
  - ai
  - security
  - orby
  - hardening
  - evals
notes:
  - "[[11 - Orby Security & Reliability Ground Truth - 2026-09-05]]"
  - "[[07 - Evaluation & Observability]]"
  - "[[10 - Orby Golden Eval Dataset (Grounding Cases)]]"
  - "[[security/README]]"
next: "P0-0 (locked 2026-09-05): confirm live CEREBRAS_API_KEY billing/credit
  status in the Cerebras dashboard before any provider-chain change; only then
  revisit 4th-leg/reorder decision. Then: wire Semgrep; restore blocking
  eval-gate.yml."
---

# Orby Hardening Implementation Guide — 2026-09-05

> **Companion to [[11 - Orby Security & Reliability Ground Truth - 2026-09-05]].** That note answers WHAT is wrong, verified file-and-line against live code. This note answers HOW, with external research and reasoning behind each recommendation, so this can be handed to Cursor as an implementation guide rather than a punch list. Read note 11 first — this note does not repeat its verified-status tables.
>
> Read-only against `/home/anant_gupta/projects/hub/portfolio` (branch `post-frontend`), 2026-09-05. No application source files modified. Only this vault note was written.

---

## Executive Summary — What Changes the Picture

Three things surfaced in research that note 11 didn't have, and they matter enough to lead with:

1. **Cerebras' no-card free tier ended in August 2026.** New accounts now get $5 in one-time credit that expires 30 days after a payment method is added — there may no longer be a durable free Cerebras tier at all, depending on when this project's key was created. This is the primary leg in the router. **Action: check the Cerebras dashboard billing/credit status for the live `CEREBRAS_API_KEY` before assuming "free forever."** This is more urgent than any code change below.
2. **Published free-tier request ceilings are tighter than the app-level abuse caps assume**, and they are *shared across every visitor*, not per-IP. See [Capacity Reality Check](#capacity-reality-check-rate-limits-never-hit) — this is the concrete answer to "make sure we never hit rate limits."
3. **OWASP's LLM Top 10 moved to a 2026 edition** (published 2026-08-04) with a reordered list — cross-referencing note 11's residual risks against it surfaces one category with no current coverage: **Supply Chain Risks** (dependency/SDK auditing). See [OWASP Cross-Reference](#owasp-top-10-for-llm-applications-2026--cross-reference).

---

## P0 — Reliability / Trust

### P0-1. Tool-call quality gate in the router

**Note 11's finding:** Cerebras (`zai-glm-4.7`) can return HTTP 200 while emitting tool-call JSON as visible streamed text instead of a structured tool call. `model-router.ts` only fails over on a thrown exception or a Groq-specific `tool_use_failed` string match (lines 194–218) — it has no equivalent check for Cerebras, and no check at all for a soft failure that only appears once streaming starts (the comment at line 198 admits this is meant to be caught downstream in `route.ts`, which is a second place this logic has to stay in sync).

**Researched approach — response-shape validation, not blind trust in provider "strict" mode.** Cerebras's own docs describe `zai-glm-4.7` as tool-use-optimized with `strict: true` constrained decoding, which is *already enabled* per the code comment at model-router.ts:53–55 — and the leak still happens. That's the evidence for why "just trust strict mode" isn't sufficient on its own: constrained decoding reduces malformed tool calls, it doesn't eliminate the model choosing to narrate the call as text instead of invoking it. Industry practice for this exact failure shape is a **circuit breaker with quality-based tripping**, not just error-based tripping: track "soft failures" (a response that looks like it *contains* a tool-call payload in its text content, e.g. matches `/\{\s*"(function|tool_call|name)"\s*:/` or similar tool-JSON shape) as a failure class equal to a thrown error, open the breaker for that provider, and cascade — exactly the same `redis.set(cooldownKey, ...)` + `continue` pattern already used for the Groq check three lines below it. This is the smallest-diff fix because it reuses the exact mechanism already proven for Groq; it does not require a new abstraction.

**Why not force JSON mode on every provider instead?** That was the other option worth naming: some OpenAI-compatible endpoints support `response_format: { type: "json_object" }`, which would make this class of bug structurally impossible rather than detected-after-the-fact. Reject it here for now — Cerebras's own docs push `strict: true` (already in use) as *its* answer to the same problem rather than JSON mode, and enforcing a second, different constraint on top risks fighting the SDK's tool-calling machinery in ways specific to each of the three providers' APIs (Groq and Mistral each have their own tool-calling implementations via `@ai-sdk/groq`/`@ai-sdk/mistral`, not the generic OpenAI client Cerebras uses). Detecting the leak in the stream (already partially built) and cascading is the lower-risk, smaller change; note it as a stretch goal if the detection approach still leaks occasionally.

**Verify:** force a Cerebras response that narrates a tool call as text (reproducible by asking a question that should trigger `navigate` while `CEREBRAS_API_KEY` is temporarily pointed at a rate-limited/degraded state) and confirm the response header shows the request cascaded to Groq, not that the leaked JSON reached the user.

### P0-2. Restore blocking promptfoo CI

**Nuance note 11 doesn't surface: there are two separate gates today, not one.** `.github/workflows/eval-gate.yml` (confirmed: `continue-on-error: true`, line 8) is the **automated CI copy** and is advisory. But `.claude/commands/ship-check.md` and `.claude/commands/deploy.md` (confirmed present) already treat the eval suite as a **hard blocking step** — "`/eval`... All promptfoo cases must pass... stop, do not continue to Step 3" — for any session that runs `/ship-check` or `/deploy` before pushing. So the "quality gate is soft" problem is real but scoped: it's soft *only* for a push that bypasses the slash-command pipeline (e.g., pushed directly without running `/ship-check`), not for every deploy.

**Approach:** two independent fixes, both cheap:
1. Flip `continue-on-error: true` to `false` (or remove the line) in `eval-gate.yml` once `CEREBRAS_API_KEY` is confirmed live in GitHub Secrets (see Executive Summary #1 — don't flip this before confirming the key still works, or every PR starts failing on a billing issue, not a real regression).
2. Align the warmth-judge models: `evals/personas/*.yaml` reference Mistral judge models per note 11; if `MISTRAL_API_KEY` in CI secrets is the same one flagged unauthorized in the 2026-06-18 git history, the persona-warmth checks will fail even when the app itself is fine. Confirm CI secrets match what's actually authorized before making the gate blocking, or the first blocking run will fail on infrastructure, not quality — which just teaches the team to ignore the gate again.

**Verify:** trigger a PR with a deliberately broken grounding case; confirm the GitHub Actions check goes red and blocks merge (not just prints a warning).

### P0-3. HMAC-gate `/api/orby-comment`

**Approach:** reuse the existing HMAC verification helper already used by `/api/chat` (per note 11, `src/lib/chat-token.ts`) rather than writing a second auth mechanism — this endpoint sits in the same trust boundary (unauthenticated visitors, provider-quota-consuming) as chat, so it should use the identical gate, not a lighter one. This is the "don't invent a second pattern" version of the fix.

**Verify:** the same `curl` pattern already documented in [[security/manual-actions]] Phase 3 (`curl ... -X POST /api/chat` expecting `401` without a cookie) — repeat against `/api/orby-comment` and confirm the same `401` today (it won't) and after the fix (it will).

---

## P1 — Security / Ops

### Semgrep — which ruleset, concretely

Note 11 confirms Semgrep is documented but not wired (confirmed again in this pass: no `.semgrep.yml`, no `semgrep` reference anywhere in the repo). The concrete, lazy-first answer: don't hand-write rules. Use Semgrep's free, maintained rulesets via the official GitHub Action:
- `p/owasp-top-ten` — generic web OWASP coverage
- `p/nextjs` — Next.js-specific (App Router route handler patterns, this repo's exact shape)
- `p/typescript` and `p/react` — language/framework coverage
- `p/secrets` — catches hardcoded keys before they'd ever need the `NEXT_PUBLIC_` grep from [[security/phase-3-chatbot-resilience]] Step 1

This is a ~15-line `.github/workflows/semgrep.yml` using `returntocorp/semgrep-action`, advisory-first (same `continue-on-error` pattern as the eval gate, tightened to blocking once it's had a pass with zero false-positive noise) — do not write custom Semgrep rules for this project's specific patterns (e.g. a custom rule for "no new provider without updating model-router.ts") unless the maintained rulesets prove insufficient after real use.

### Sanity token / CORS / UptimeRobot / WAF (dashboard items)

These are unchanged from [[security/manual-actions]] Phase 2 (2A/2B) and Phase 5 (5A) — that file already has copy-pasteable dashboard steps for all three. The one addition worth making concrete:

**UptimeRobot monitor spec (confirmed against current UptimeRobot free-tier docs):** the free plan gives 50 monitors at a 5-minute check interval with 5 alert contacts and 2 months of log retention — sufficient for this use case, no paid tier needed. Two monitors, exactly as [[security/manual-actions]] §5A already specifies: homepage (`https://anantgupta.dev`) and `/api/health`. One addition: **because `/api/health` returns `503` when any single provider key check fails** (confirmed: `src/app/api/health/route.ts` returns `503` unless *every* boolean in `checks` is true, including `sanity_token` and `chat_secret`), a single missing/rotated key will trip the uptime alert even though the app is still serving traffic in degraded mode. Either accept that as an intentional early-warning signal (recommended — it's cheap and exactly the "notice before a user does" goal from [[07 - Evaluation & Observability]]), or set the UptimeRobot alert threshold to tolerate a `503` for one check cycle before paging, to avoid alert fatigue on transient blips.

### Vercel WAF Attack Challenge Mode

Still dashboard-only and unverifiable from the repo, matching note 11. No new information found that changes this — leave as an open manual-verification item.

---

## P2 — Hardening Polish

### Upstash fail-open reconsidered

Note 11 and [[security/phase-3-chatbot-resilience]] both document the current choice deliberately: on Redis outage, rate limiting is skipped rather than the endpoint 500ing. **Keep fail-open.** The reasoning holds up under research: a portfolio's chat endpoint failing closed during a Redis blip means a recruiter mid-conversation gets a hard error instead of an unlimited-but-still-provider-rate-limited chat — the provider chain's own rate limits (see below) are a second layer that still caps runaway cost even if Upstash is down. Fail-closed here trades a rare abuse window (Redis is a managed, high-uptime service) for a much more common false-positive (any Redis hiccup breaks the headline feature). Don't change this without a concrete abuse incident forcing the trade-off the other way.

### Golden eval dataset expansion — promptfoo is sufficient, RAGAS is a "maybe later," not a rebuild

[[10 - Orby Golden Eval Dataset (Grounding Cases)]] already correctly rejected a parallel deepeval pipeline in favor of expanding promptfoo's own `grounding.yaml`. Research confirms that call: promptfoo's `context-faithfulness` assertion does the same core thing RAGAS's faithfulness metric does — extract claims from the response, verify each against provided context, score as a ratio — the two are architecturally the same idea, and RAGAS's edge is being research-backed with a wider metric family (context precision/recall) built specifically for RAG pipelines with a retrieval step. **This app doesn't have a retrieval step** — the "context" is a fixed, fully-injected Sanity catalog per request (confirmed: `chat-context.ts` / `fetchCatalog`, not a vector-search RAG pipeline) — so RAGAS's retrieval-specific metrics (context precision/recall, measuring whether the *right chunks* were retrieved) don't apply here; there's nothing to retrieve, the whole catalog is already in the prompt. Adding RAGAS would mean running a second Python-based eval tool for a metric family this architecture doesn't need. **Recommendation: stay on promptfoo, expand `grounding.yaml` toward the full 30–50 case target pulled from live Sanity content as already planned, and add promptfoo's own `redteam` mode** (confirmed current: 50+ adversarial plugins covering prompt injection, jailbreak, PII leakage, excessive agency, hallucination — mapped directly to OWASP LLM01/LLM03/LLM07 below) as the "professionally proofed" / never-hallucinate layer note 11's suite doesn't yet exercise. This is additive to the existing `evals/` folder, same tool, no new CI system.

---

## Capacity Reality Check — "Rate Limits Never Hit"

Published free-tier limits as of 2026 (sources in Evidence), for the exact models in `PROVIDER_CHAIN`:

| Provider | Model | Free-tier ceiling (shared across ALL visitors, not per-IP) | Status |
|---|---|---|---|
| Cerebras | `zai-glm-4.7` | Reported as low as **5 RPM / 30K TPM / 1M TPD** on some 2026 docs, up to 30 RPM/60K TPM on others — **and the no-card free tier ended entirely in August 2026** (new accounts: $5 credit, 30-day expiry) | **Needs live confirmation — see below, this is now P0-0** |
| Groq | `llama-3.3-70b-versatile` | **30 RPM, 1,000 RPD, 12,000 TPM, 100,000 TPD** (verified against Groq's live docs, 2026-08-15) | Confirmed current |
| Mistral | `mistral-small-latest` | Free "Experiment" tier: ~1 request/second, ~1B tokens/month, exact numbers no longer published — check Admin Console → Limits | Unverified precisely, but generous token ceiling |

**What this means concretely.** The app's own abuse caps (10 req/60s burst, 100 req/24h per IP) are a *per-visitor* ceiling. The provider free tiers above are a *global* ceiling shared by every visitor hitting the portfolio at once. If Cerebras is genuinely as low as 5 RPM system-wide, **two or three visitors chatting in the same minute can exhaust it**, and the router will correctly cascade to Groq (assuming P0-1 is fixed) — but Groq's 1,000 RPD is also a hard daily wall that a moderately-trafficked launch day (e.g., posting the portfolio link somewhere with real traffic) could plausibly reach before midnight UTC reset. This is the honest answer to "make sure we never even come close to rate limits": **with three free-tier legs, the system degrades gracefully (that part is already solid — [[nextgen-chatbot/05 - Model Layer, Rate Limiting & Abuse]] design + confirmed `degraded-responses.ts`) but "never even close" is not realistically achievable on free tiers alone under real launch-day traffic.**

##### P0-0 — Decision locked 2026-09-05: verify Cerebras account status before anything else

User decision: **check the Cerebras account first.** Do not add a 4th provider leg or reorder the chain until this is done — those are premature fixes for a problem whose actual scope is still unknown for this specific project.

**Concrete verification steps:**
1. Log into [cloud.cerebras.ai](https://cloud.cerebras.ai) with the account tied to the live `CEREBRAS_API_KEY` (check Vercel env vars / `.env.local` if the account owner isn't obvious).
2. Go to Billing / Usage in the dashboard. Record: (a) is a payment method on file, (b) current credit balance and expiry date if on the $5 trial, (c) which pricing tier the account is actually on (some accounts created before August 2026 may have been grandfathered — don't assume the new policy applies retroactively without checking).
3. If the account has no card and shows the old no-card free tier still active: nothing to do, re-verify in 30 days as a recurring calendar reminder (free tiers are re-evaluated by providers often — this whole chain needs a periodic policy check, not a one-time one).
4. If the account is on the $5/30-day trial and it's close to expiry or exhausted: this becomes the actual P0, ahead of P0-1 below — a dead primary leg makes the tool-call quality gate fix moot, since Cerebras would fail on missing-key/auth-error grounds (which the router *does* already catch) rather than the soft-failure case P0-1 fixes.
5. Only after this is known: revisit the two 4th-leg candidates below if the primary leg is confirmed unreliable long-term.

**4th-leg candidates, for if/when needed (not now):**
- **Google Gemini** (the original provider before this chain existed, per note 11's history) — has historically offered a generous free tier and an OpenAI-compatible endpoint, meaning it would slot into `PROVIDER_CHAIN` with the same generic `createOpenAI({baseURL, apiKey})` pattern already used for Cerebras — smallest-diff option if reintroduced.
- **A second Groq-class fast-inference free tier** (e.g., Together AI or Fireworks both publish free/trial credits) as a same-shape backup to Groq specifically, since Groq is the leg with the hardest, most reliable published numbers above and is likely to become the real workhorse if Cerebras's free tier is indeed gone for this account.

Reasoning for not jumping straight to a 4th leg: every additional leg is another API key to rotate, another cooldown branch to test, and another line in the "why did Orby answer weirdly" debugging checklist — diminishing returns past 3–4 legs, and `degraded-responses.ts` already provides a real, tested floor so total outage isn't actually possible even at zero live legs. The money/effort is better spent on P0-1 (making the existing legs actually cascade correctly) than on a 4th leg papering over a router that doesn't fail over reliably yet — unless step 4 above shows Cerebras is genuinely, immediately dead, in which case promoting Groq to primary (already possible today by reordering `PROVIDER_CHAIN`, zero new dependencies) is the smaller fix than adding a new provider.

---

## Per-Provider Runbook

| Leg | What "down" looks like | What the router does today | What to check / monitor |
|---|---|---|---|
| Cerebras (primary, msgs 1–10) | 429/5xx (caught, cooldown 30–120s) **or** HTTP 200 with tool-call leaked as text (NOT caught until P0-1 ships) | Catches thrown errors, sets cooldown, cascades to Groq. Does not catch the text-leak case. | `router.fail` logs (thrown-error case); after P0-1, a new `router.fail.tool_use` log line matching the existing Groq one |
| Groq (secondary, or primary after msg 10) | 429/5xx, or `tool_use_failed` string in response metadata (caught, confirmed in code) | Catches both cases, cascades to Mistral | `router.fail.tool_use` logs; Groq's 1,000 RPD is the tightest published ceiling of the three live legs — watch this first if traffic spikes |
| Mistral (tertiary) | 429/5xx (caught) | Cascades to degraded mode | Confirm `MISTRAL_API_KEY` in Vercel matches an authorized key — note 11 found the CI copy was unauthorized as of 2026-06-18; the production key may or may not be the same one |
| Degraded (all legs cooled or missing) | N/A — this is the floor | Returns canned persona-appropriate text + deterministic nav per `degraded-responses.ts` | `router.turn` log shows `mode: "cooldown"` vs `"degraded"` — the distinction matters: "cooldown" means legs exist but are resting, "degraded" means something is structurally wrong (missing keys) and needs a human |

---

## OWASP Top 10 for LLM Applications 2026 — Cross-Reference

Published 2026-08-04, reordered from the 2025 edition (Excessive Agency jumped from #6 to #3; System Prompt Leakage renamed to Hidden Context Exposure). Cross-referencing against note 11's residual risks and this repo's actual code:

| # | OWASP 2026 category | Covered by existing code? | Gap |
|---|---|---|---|
| LLM01 | Prompt Injection | Partial — RULES block, persona guardrails, sanitizer (note 11) | `evals/injection.yaml` exists but is hand-written cases; promptfoo `redteam` mode (50+ auto-generated adversarial plugins) would exercise this far more thoroughly — see P2 above |
| LLM02 | Sensitive Information Disclosure | Partial | `/api/health` publicly reveals which env vars are configured (booleans only, not values — low severity but real); `SANITY_API_TOKEN` as `browserToken` scope (note 11 P1 #4) |
| LLM03 | Excessive Agency | **Strong** | Closed tool set (`navigate`, `showProject`, etc.), Zod-validated, fail-safe wrapped — this is the one category where the architecture is already a best-practice example, worth noting as a strength, not just gaps |
| LLM04 | Supply Chain Risks | **Not addressed anywhere in note 11 or this pass — genuine new gap** | No Dependabot/Renovate config found in repo; provider SDKs (`@ai-sdk/*`) and the AI SDK itself are a real supply-chain surface for an app whose entire value prop is routing to external model providers. Recommend enabling GitHub's built-in Dependabot alerts (free, zero config beyond a `.github/dependabot.yml`) — lazier than any custom solution and covers this category directly |
| LLM05 | Data and Model Poisoning | N/A | No fine-tuning, no training on user data — the app calls hosted third-party models as-is. Correctly out of scope, matching [[security/README]]'s own "explicitly NOT in scope" pattern |
| LLM06 | Unbounded Consumption | Partial | This is the formal name for exactly the "rate limits never hit" concern — see [Capacity Reality Check](#capacity-reality-check-rate-limits-never-hit) above. Upstash fail-open (P2) is the one deliberate trade-off inside this category |
| LLM07 | Misinformation | Partial | This is the formal name for "never hallucinate" — grounding evals + refusal rule (note 11), CI currently advisory (P0-2) |
| LLM08 | Hidden Context Exposure (was: System Prompt Leakage) | **Not explicitly tested** | No eval case confirmed that asks Orby to repeat its system prompt or the raw injected catalog JSON verbatim. Cheap addition to `evals/injection.yaml`: one case asking directly for the system prompt, asserting refusal |
| LLM09 | Vector and Embedding Weaknesses | N/A | No vector store / embeddings anywhere in this architecture (confirmed: direct Sanity fetch, not RAG-with-retrieval) — correctly out of scope |
| LLM10 | Improper Output Handling | Partial | `chat-sanitizer.ts` strips tool-call leakage from output (note 11: "still can flash before finish") — same root cause as P0-1, fixing the router-level detection should shrink this too since less leaked text ever reaches the sanitizer in the first place |

---

## Review Pipeline — "Professional Proofing" Before Every Deploy

This is already built, not something to invent. Confirmed in this pass: `.claude/commands/ship-check.md` and `.claude/commands/deploy.md` already chain the right steps in the right order:

```
/ship-check  →  typegen → typecheck → lint → build   (Step 1, stop on failure)
             →  /eval → eval-runner agent runs promptfoo   (Step 2, ALL cases must pass, stop on failure)
             →  security-reviewer agent → must output SHIP   (Step 3, stop unless SHIP)
             →  /deploy   (Step 4, only if 1-3 all passed)

/deploy      →  typegen → typecheck → lint → build → pnpm test   (Step 1)
             →  security-reviewer agent → must output SHIP   (Step 2)
             →  git status / git diff --staged review   (Step 3, human-in-the-loop check for secrets/unrelated files)
             →  git add -p → conventional commit   (Step 4)
             →  git push origin main → monitor via Vercel MCP   (Step 5)
```

**The gap is not the pipeline — it's that the pipeline can be bypassed** by pushing directly instead of running `/ship-check`/`/deploy`, and the GitHub Actions copy of the eval step (`eval-gate.yml`) is advisory, so a direct push doesn't get caught by CI either (P0-2). Once P0-2 ships and Semgrep is wired (P1) as a second CI job alongside `eval-gate.yml`, a direct push gets the same enforcement the slash-command pipeline already gives a disciplined session — that closes the loop without inventing a new process.

**Recommended sequence for every deploy, restated plainly:** run `/ship-check` (not `/deploy` alone — `/deploy` doesn't run the eval step itself, it assumes `/ship-check` already happened, per its own Step 2 note "Invoke security-reviewer... before touching git" — `/ship-check`'s Step 2 is the one place eval is mandatory in the local flow). If `/ship-check` passes end to end, run `/deploy`.

---

## Evidence

### Vault (read, not modified)
- [[11 - Orby Security & Reliability Ground Truth - 2026-09-05]] — the verified-status source this note extends
- [[07 - Evaluation & Observability]], [[10 - Orby Golden Eval Dataset (Grounding Cases)]], [[04 - Orby Integration]]
- [[security/README]], [[security/phase-3-chatbot-resilience]], [[security/manual-actions]]
- [[chatbot/05-evals]]

### Repo (read-only, 2026-09-05)
- `src/lib/model-router.ts` — full file read; provider chain, cooldown, budget-tier, Groq soft-failure check
- `evals/promptfooconfig.yaml`, `evals/*.yaml` — confirmed test files match [[chatbot/05-evals]]'s table
- `.github/workflows/eval-gate.yml` — confirmed `continue-on-error: true`
- `src/app/api/health/route.ts` — confirmed public, boolean-only env checks, 503 on any false
- `.claude/commands/ship-check.md`, `.claude/commands/deploy.md` — confirmed existing review pipeline
- Confirmed no Semgrep config anywhere in repo (`grep -r semgrep`, `find -iname "*.semgrep*"` both empty)

### External
- [Cerebras Free Tier 2026 — rate limits, credit expiry](https://pricepertoken.com/endpoints/cerebras/free)
- [API Rate Limits Compared: Every Major LLM Provider (June 2026)](https://stochasticsandbox.com/posts/api-rate-limits-compared-2026-06-06/)
- [Groq Free Tier Limits 2026](https://tokenmix.ai/blog/groq-free-tier-limits-2026)
- [Mistral: Why am I hitting API rate limits](https://help.mistral.ai/en/articles/698531-why-am-i-hitting-api-rate-limits-and-how-do-i-increase-them)
- [Mistral Usage and limits](https://docs.mistral.ai/admin/user-management-finops/tier)
- [Retries, Fallbacks, and Circuit Breakers in LLM Apps — production guide](https://www.getmaxim.ai/articles/retries-fallbacks-and-circuit-breakers-in-llm-apps-a-production-guide/)
- [Promptfoo LLM red teaming guide](https://www.promptfoo.dev/docs/red-team/)
- [Promptfoo context-faithfulness assertion](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/context-faithfulness/)
- [Ragas metrics explained](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge)
- [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)
- [OWASP LLM Top 10 2026 — what changed](https://blog.ogwilliam.com/post/owasp-top-10-llm-applications-2026-whats-new)
- [UptimeRobot free plan monitoring interval](https://help.uptimerobot.com/en/articles/11360876-what-is-a-monitoring-interval-in-uptimerobot)
- [UptimeRobot pricing 2026](https://www.saaspricepulse.com/tools/uptimerobot)

---

## Related Notes

- Extends: [[11 - Orby Security & Reliability Ground Truth - 2026-09-05]]
- Does not touch: SEO/AEO discoverability ([[AEO & SEO/01 - SEO & AEO Discoverability Strategy]]) or frontend UI ([[frontend/UI Fixes]]) — separate sessions

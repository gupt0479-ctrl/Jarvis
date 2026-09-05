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
  - ground-truth
notes:
  - "[[security/README]]"
  - "[[08 - Build Phases & Milestones]]"
  - "[[02 - Premortem & Failure Defenses]]"
  - "[[05 - Model Layer, Rate Limiting & Abuse]]"
  - "[[09 - Orby Fixes]]"
  - "[[Problems with Portfolio Lab]]"
  - "[[04 - Eval Harness — promptfoo]]"
  - "[[10 - Orby Golden Eval Dataset (Grounding Cases)]]"
next: "Restore blocking promptfoo CI gate; verify dashboard-only security items; fix Orby tool-call quality gate in router"
---

# Orby Security & Reliability Ground Truth — 2026-09-05

> **CORRECTION 2026-09-05:** This note supersedes stale claims in [[security/README]] (last verified 2026-06-15), [[05 - Model Layer, Rate Limiting & Abuse]] (Azure-primary plan), graphify snapshot `chatbot/02-model-router.md` (Gemini→Groq at commit `89cd2c0e`), and parts of [[00 - Nextgen Chatbot — Build Plan]] ("Planning only. No code."). **Do not delete or archive those notes.** Treat this file as the current verified ground truth for Orby reliability, security posture, deployment readiness, and provider chain. Re-verify against live repo HEAD before the next major launch decision.

> Verified against `gupta-builds/Portfolio` repo on branch `post-frontend`, read-only, 2026-09-05. No application source files were modified during this reconciliation session.

---

## Executive Summary

Orby is **substantially built and deployable**, but **not fully launch-hardened**. The two named June launch blockers in [[security/README]] — CSP Report-Only and Clerk-gated `/api/health` — are **both fixed in current code**. The bigger live gaps are:

1. **Reliability:** Cerebras `zai-glm-4.7` intermittently emits tool directives as visible text instead of structured tool calls; the router treats HTTP 200 as success, so Groq/Mistral rarely fire.
2. **Quality gate:** promptfoo exists but CI is **advisory** (`continue-on-error: true`); user decision is to restore **blocking** before public launch.
3. **Static analysis:** Semgrep is documented in [[Code Review & Eval Gap]] but **not wired** in repo CI or pre-commit.
4. **Dashboard-only items:** Sanity token role/CORS, Vercel WAF Attack Challenge Mode, UptimeRobot — still unverified from code.

**Canonical production domain:** `https://anantgupta.dev` (also hardcoded in `src/lib/request-guards.ts` Cloudflare host set).

---

## User Decisions Locked (2026-09-05)

| Decision | Verdict |
|---|---|
| Azure OpenAI as primary | **Dropped from v1** — not in live code; do not plan around it unless explicitly reintroduced |
| promptfoo CI gate | **Restore blocking** before public launch (once provider keys stable) |
| Agent-Callable Orby via MCP | **Deferred** — parallel AEO/security-model session owns go/no-go |
| Vercel WAF Attack Challenge Mode | **Unknown** — requires dashboard verification |
| Canonical origin allowlist domain | **`https://anantgupta.dev`** |

---

## Model Provider Chain — Four-Way Reconciliation

Four different chains appear across vault notes. **Only one matches live code.**

| Source | Documented chain | Status vs live code |
|---|---|---|
| [[security/README]] + [[security/phase-3-chatbot-resilience]] | Cerebras → Groq → Mistral → degraded | **Mostly accurate** (model IDs differ) |
| [[05 - Model Layer, Rate Limiting & Abuse]] | Azure GPT-4o-mini → Cerebras → Groq → Mistral → degraded | **Contradicted** — Azure never landed |
| graphify `chatbot/02-model-router.md` (commit `89cd2c0e`) | Gemini → Groq | **Stale** — orientation only |
| **Live repo HEAD** | **Cerebras `zai-glm-4.7` → Groq `llama-3.3-70b-versatile` → Mistral `mistral-small-latest` → degraded** | **Ground truth** |

### Live router facts

- **File:** `src/lib/model-router.ts`
- **Env vars:** `CEREBRAS_API_KEY`, `GROQ_API_KEY`, `MISTRAL_API_KEY` — all server-only, no `NEXT_PUBLIC_` prefix
- **Azure:** zero references in `src/`; dropped from v1 per user decision
- **Budget tiering:** messages 1–10 start at Cerebras (`startIndex = 0`); message 11+ skips to Groq (`startIndex = 1`) — session count in Upstash key `chat:session:{sessionId}:count`, TTL 3600s
- **Per-provider cooldown:** 30s default in Upstash (`chat:cooldown:{provider}`), retry-after aware up to 120s
- **Modes:** `live` | `degraded` | `cooldown`

### Why backup providers rarely fire

The router advances to the next provider only on **missing env key**, **cooldown skip**, or **thrown errors** (including Groq `tool_use_failed` metadata check). It does **not** fail over when Cerebras returns HTTP 200 but dumps `{ "function": "navigate" ... }` as text instead of using the tool API. That is the root cause documented in [[Problems with Portfolio Lab]] and still structurally true in current code.

### Mistral key status (June 2026 CI history)

Git commits on 2026-06-18:
- `09c8c96` — eval made advisory (`continue-on-error: true`) citing **Mistral key unauthorized**
- `5f29675` — eval provider switched from Mistral to **Cerebras `zai-glm-4.7`**

Production router still **attempts** Mistral as tertiary leg if `MISTRAL_API_KEY` is present. Eval CI no longer depends on Mistral. Warmth rubrics in `evals/personas/*.yaml` still reference `mistral:mistral-large-latest` as LLM judges — separate from production router.

---

## Security Phase Map (1–5) — Verified Status

| Phase | Vault claim (June 2026) | Live status | Evidence |
|---|---|---|---|
| **1 — Clerk / Studio auth** | Done — verify once | **Done** | `src/proxy.ts:5-10,24-27` protects `/studio(.*)` only; `src/app/studio/layout.tsx:10` + `page.tsx:16-19` double-guard; chat routes public |
| **2 — Sanity lockdown** | Partial — dashboard manual steps | **Partially done** | Draft-mode open redirect patched (`src/app/api/draft-mode/enable/route.ts:14-18`); no mutation calls in Next layer; **`SANITY_API_TOKEN` passed as `browserToken`** in `src/sanity/lib/live.ts:13-14` — must be Viewer-scoped in dashboard |
| **3 — Chatbot resilience** | Solid — minor health info leak | **Partially done** | HMAC gate, rate limits, sanitizer, fallback chain exist; Upstash fail-open; `/api/orby-comment` lacks HMAC gate (see gaps) |
| **4 — Deployment hardening** | CSP still Report-Only | **Contradicted — CSP now enforced** | `next.config.ts:50-52` sets `Content-Security-Policy` (not Report-Only); comment says "ENFORCED" |
| **5 — Monitoring** | `/api/health` Clerk-gated | **Contradicted — health is public** | `src/proxy.ts:40-41` excludes `api/health`; `src/app/api/health/route.ts:3-23` returns env-presence booleans only |

### June launch blockers — current state

| Blocker | June status | 2026-09-05 status |
|---|---|---|
| CSP Report-Only | Open | **Fixed** — enforced CSP in `next.config.ts:52` |
| `/api/health` Clerk-gated | Open | **Fixed** — excluded from proxy matcher `src/proxy.ts:40` |

---

## Rate Limiting & Abuse Controls — Live Numbers

Numbers verified in code, not vault notes (notes disagree slightly).

| Control | Live value | Evidence |
|---|---|---|
| Burst cap | **10 req / 60s** per IP | `src/app/api/chat/route.ts:39-43` |
| Daily cap | **100 req / 24h** per IP | `src/app/api/chat/route.ts:45-49` |
| HMAC token TTL | **1 hour** | `src/lib/chat-token.ts:1,65`; cookie `maxAge: 3600` at `chat-token/route.ts:99,167` |
| Cookie flags | httpOnly, secure (prod), sameSite strict | `src/app/api/chat-token/route.ts:95-100,163-168` |
| Message max | **20** messages; content **≤4000** chars; system-role blocked | `src/app/api/chat/route.ts:124-172` |
| Origin allowlist | `localhost:3000`, `localhost:3001`, `NEXT_PUBLIC_BASE_URL`, `NEXT_PUBLIC_SITE_URL`, `https://${VERCEL_URL}` | `src/lib/request-guards.ts:45-72` |
| Production CF hosts | `anantgupta.dev`, `www.anantgupta.dev` for trusted `cf-connecting-ip` | `src/lib/request-guards.ts:10,25-31` |
| Scraper UA block | GPTBot, Googlebot, etc. | `src/lib/request-guards.ts:7-8` |
| Turnstile | Required in prod/preview before HMAC issuance | `src/app/api/chat-token/route.ts:8-9,137-157`; client `src/components/ChatTokenInit.tsx` |
| Dev bypass | `DEV_BYPASS_IP` skips rate limits | `src/app/api/chat/route.ts:181-186` |
| Exact-match cache | Upstash, TTL **86400s** (24h) | `src/app/api/chat/route.ts:254-317,606` |
| Idle comment limit | **3 / 60s** per IP on `/api/orby-comment` | `src/app/api/orby-comment/route.ts:52-56,74-78` |
| Upstash outage behavior | Rate limiting **skipped** (fail-open) | `src/app/api/chat/route.ts:219-222` |
| Vercel WAF Attack Challenge Mode | Planned in [[05 - Model Layer, Rate Limiting & Abuse]] | **Unknown** — dashboard only, not verifiable from repo |

---

## Premortem Failure Modes (1–10)

From [[02 - Premortem & Failure Defenses]]. Status reflects **live code**, not phase tracker optimism.

| # | Failure | Status | Evidence / gap |
|---|---|---|---|
| **1** | Lied about me to recruiter | **Partially done** | Grounding + refusal in `src/lib/chat-context.ts:158-161`; tools + sanitizer; eval suite exists but CI advisory; Cerebras tool-call inconsistency can still produce wrong nav/cards |
| **2** | Quota dies under traffic | **Partially done** | Failover chain + degraded mode (`src/lib/model-router.ts`, `src/lib/degraded-responses.ts`); budget tier skips Cerebras after 10 msgs; no Azure premium tier; cooldown mode returns user-visible rate-limit message |
| **3** | Weak tool calls break wow feature | **Partially done** | Strict Zod tools (`src/lib/chat-tools.ts:234+`); fail-safe execute wrappers; Groq tool_use_failed detection; **but** Cerebras text-leak bypasses tool pipeline intermittently |
| **4** | Intent/page desync | **Partially done** | `orby:navigate` pipeline wired (`PortfolioLab.tsx:196-218`, `useOrbyState.ts:287-396`); fixed prompts deterministic nav (`src/lib/fixed-prompts.ts`); arrival IO can miss if section already visible |
| **5** | Endpoint abused as free LLM | **Partially done** | Turnstile + HMAC + origin + rate limits on `/api/chat`; **`/api/orby-comment` has no HMAC** — origin/UA/rate-limit only (`src/app/api/orby-comment/route.ts`) |
| **6** | Prompt injection / ugly output | **Partially done** | RULES block + persona guardrails (`chat-context.ts`, `personas/weirdo.ts`); sanitizer strips bad output; no separate output-regeneration guard beyond sanitizer |
| **7** | Content drift | **Done** | Live Sanity fetch per request (`src/lib/chat-context.ts:28-41`, `fetchCatalog` in chat route) |
| **8** | Silent degradation | **Partially done** | Structured logs (`chat.request`, `router.*`); promptfoo suite; **CI does not block merges** (`.github/workflows/eval-gate.yml:12`) |
| **9** | Gets in the way | **Done** (by design) | Portfolio Lab is sidebar/dismissible; Orby is additive companion; visual polish tracked separately in `frontend/UI Fixes.md` — out of scope here |
| **10** | Over-built | **Done** | Single route handler, closed tool set, no vector store / multi-agent graph in v1 |

---

## Orby Fix Log — What Landed vs Still Open

Cross-check [[09 - Orby Fixes]] and [[Problems with Portfolio Lab]] against live code.

| Issue | Vault claim | Live status | Evidence |
|---|---|---|---|
| Raw JSON / tool tags leak to user | Broken Jun 2026 | **Partially fixed** | Stream buffer + `sanitizeChatText` + final `t:` replacement (`chat/route.ts:413-549`, `chat-sanitizer.ts`); still can flash before finish |
| Orby silent on nav | Broken Jun 2026 | **Partially fixed** | Requires `a:` navigate tool result or sanitizer synthetic nav + `orbyMessage`; `m:` line for leaked speech (`PortfolioLab.tsx:230-236`) |
| Everything navigates to BOOM | Broken Jun 2026 | **Partially fixed** | 16 fixed prompts with deterministic `navTarget` (`fixed-prompts.ts`); free-typed still model-chosen |
| Backup providers never fire | Root cause identified | **Still true structurally** | Router success = no throw (`model-router.ts:190-224`) |
| First-prompt / wave UX | Fix planned | **Done** | `PortfolioLab.tsx:104-108`, `PanelOrby` wave before `chatStarted` |
| Turnstile errors (300010) | Dev issue | **Partially mitigated** | Dev allows token without secret; prod fails closed (`chat-token/route.ts:72-76`) |
| Z.ai GLM 4.7 | Unverified in vault | **Now primary production + eval model** | `model-router.ts:53-55`; `evals/promptfooconfig.yaml:7-11` |
| `{ displayText, orbyMessage, navigate, card }` response shape | Planned in 09 | **Not implemented as single object** | Route streams prefix lines `0:`, `a:`, `t:`, `m:` instead |

---

## Eval & CI Gate — "Real Quality Gate" Status

Vault design ([[04 - Eval Harness — promptfoo]], [[10 - Orby Golden Eval Dataset (Grounding Cases)]]) calls promptfoo the real quality gate with `--fail-on-error` in CI.

| Item | Design | Live (2026-09-05) |
|---|---|---|
| Suite location | `evals/promptfooconfig.yaml` | **Present** |
| Test files | grounding, refusal, injection, fail-safe, tool-correctness, persona warmth | **Present** under `evals/` |
| CI workflow | `.github/workflows/eval-gate.yml` | **Present** |
| Blocking? | Designed as blocking | **Advisory** — `continue-on-error: true` line 12 |
| Provider | Was Mistral in early CI | **Cerebras `zai-glm-4.7`** since `5f29675` |
| Skip if no key | — | Warning + skip if `CEREBRAS_API_KEY` missing (lines 28-30) |
| Warmth judges | Mistral rubric graders in YAML | Still reference Mistral models — may fail if Mistral key bad |
| Semgrep | [[Code Review & Eval Gap]] — permanent static layer | **Not wired** — no workflow, no config, no git history |

**User decision:** restore **blocking** promptfoo before public launch. Until then, the eval suite is informative but does not gate deploy.

**Historical note:** At `0f01ae9` (2026-06-11) eval gate was blocking with `GEMINI_API_KEY`. Degraded to advisory on 2026-06-18 when Mistral key unauthorized.

---

## Build Phases 0–8 — Honest Coverage

[[08 - Build Phases & Milestones]] remains `status: sprout` and predates most shipped code. Rough live mapping:

| Phase | Vault intent | Live approximation |
|---|---|---|
| 0 — Prove pipe | `/api/chat` + model | **Done** |
| 1 — Lock gates | Origin, token, rate limits, WAF | **Mostly done** — WAF unverified |
| 2 — Grounding + refusal | Context engine | **Done** |
| 3 — Eval + tracing | promptfoo + logs | **Partially done** — eval exists, CI advisory; JSON logs present |
| 4 — Personas + chips | Four personas, fixed prompts | **Done** |
| 5 — Tools + generative UI | Closed tools, evidence cards | **Done** — reliability intermittent |
| 6 — Router + degraded | Fallback chain | **Done** — no Azure leg |
| 7 — Wire Orby | navigate→scroll→speak | **Done** — intermittent speech on tool-leak |
| 8 — Launch readiness | Full eval + security checklist | **Not done** — this note is input to that gate |

---

## Must-Do Before Public Launch (Prioritized)

### P0 — Reliability / trust

1. **Add tool-call quality gate in router** — if response has no structured tool results but sanitizer detects tool JSON in text, treat as provider failure and cascade to Groq/Mistral (addresses failures 1, 3, 4, and fix-log items).
2. **Restore blocking promptfoo CI** — remove `continue-on-error: true`; ensure `CEREBRAS_API_KEY` in GitHub secrets; align warmth judges with available keys.
3. **HMAC-gate `/api/orby-comment`** or document intentional exception — README claims both chat routes validate cookie; code does not (`README.md:47` vs `orby-comment/route.ts`).

### P1 — Security / ops (dashboard + small code)

4. Confirm **`SANITY_API_TOKEN` is Viewer-only** in Sanity dashboard (browserToken exposure via `live.ts:14`).
5. Confirm **Sanity CORS** lists only known origins.
6. Confirm **UptimeRobot** (or equivalent) monitors `https://anantgupta.dev/api/health`.
7. Verify **Vercel WAF Attack Challenge Mode** — currently unknown.
8. Wire **Semgrep** CI per [[Code Review & Eval Gap]] — not present in repo today.

### P2 — Hardening polish

9. Revisit **Upstash fail-open** on rate limits — consider fail-closed or capped fail-open for abuse scenarios.
10. Extend **grounding.yaml** from starter set to full Sanity-backed golden cases per [[10 - Orby Golden Eval Dataset (Grounding Cases)]].
11. Update stale vault indexes: [[security/README]] `updated` field, [[05 - Model Layer, Rate Limiting & Abuse]] Azure section, [[00 - Nextgen Chatbot — Build Plan]] "Planning only".

### Explicitly deferred

- **Agent-Callable Orby via MCP** — deferred pending AEO/security-model session ([[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan]]).
- **Azure OpenAI primary** — dropped from v1.
- **Orby visual/animation polish** — separate frontend session (`frontend/UI Fixes.md`).

---

## Residual Risks (Live Code)

1. **`/api/orby-comment` unauthenticated** — consumes provider quota without Turnstile/HMAC.
2. **Rate-limit fail-open** — Upstash outage removes caps.
3. **`SANITY_API_TOKEN` as browserToken** — client-exposed if token scope too broad.
4. **`/api/health` public** — reveals which env vars are configured (not values).
5. **Eval non-blocking** — regressions can merge.
6. **Cerebras tool-call non-determinism** — primary reliability risk for Portfolio Lab UX.

---

## Evidence

Verification performed read-only against repo at `/home/anant_gupta/projects/hub/portfolio`, branch `post-frontend`, 2026-09-05.

### Primary source files checked

| Area | File | Key lines |
|---|---|---|
| Model router | `src/lib/model-router.ts` | 1-16, 48-71, 119-124, 136-273 |
| Chat route | `src/app/api/chat/route.ts` | 39-49, 84-223, 320-653 |
| Chat token / Turnstile | `src/app/api/chat-token/route.ts` | 7-9, 72-76, 137-168 |
| Orby idle route | `src/app/api/orby-comment/route.ts` | 52-56, 58-68, 88-108 |
| Request guards | `src/lib/request-guards.ts` | 7-8, 10, 45-72 |
| HMAC token | `src/lib/chat-token.ts` | 1, 43-65 |
| Sanitizer | `src/lib/chat-sanitizer.ts` | 12-148 |
| Fixed prompts | `src/lib/fixed-prompts.ts` | 43-179 |
| Degraded mode | `src/lib/degraded-responses.ts` | 17-37, 130-133 |
| Clerk proxy | `src/proxy.ts` | 5-10, 38-42 |
| CSP | `next.config.ts` | 35-52 |
| Health | `src/app/api/health/route.ts` | 3-23 |
| Sanity live token | `src/sanity/lib/live.ts` | 8-14 |
| Draft-mode redirect fix | `src/app/api/draft-mode/enable/route.ts` | 14-18 |
| Frontend stream parser | `src/components/lab/PortfolioLab.tsx` | 170-240 |
| Orby nav state | `src/components/orby/useOrbyState.ts` | 287-418 |
| Eval config | `evals/promptfooconfig.yaml` | 7-11, 60-69 |
| CI gate | `.github/workflows/eval-gate.yml` | 11-30 |

### Git history consulted

- `0f01ae9` (2026-06-11) — Orby Phases 0–6, blocking eval with Gemini
- `fb5e142` (2026-06-12) — Phase 8 security hardening
- `09c8c96` (2026-06-18) — eval advisory, Mistral unauthorized
- `5f29675` (2026-06-18) — eval switched to Cerebras

### Vault notes reconciled (not modified)

- [[security/README]], phases 1–5, [[manual-actions]], [[claude-code-prompts]]
- [[08 - Build Phases & Milestones]], [[02 - Premortem & Failure Defenses]], [[05 - Model Layer, Rate Limiting & Abuse]]
- [[09 - Orby Fixes]], [[Problems with Portfolio Lab]]
- [[04 - Eval Harness — promptfoo]], [[10 - Orby Golden Eval Dataset (Grounding Cases)]]
- [[Code Review & Eval Gap]], PDF ingestion + [[00_Execution]] verdict sections
- graphify `INDEX.md`, `chatbot/*` — orientation only, commit `89cd2c0e`

### Manual QA checklist (post-deploy)

- [ ] `curl -s https://anantgupta.dev/api/health` → 200, not 401
- [ ] `curl -I https://anantgupta.dev` includes enforced `Content-Security-Policy`
- [ ] Portfolio Lab fixed chips: no raw JSON in bubble; Orby speaks on arrival; correct section/item
- [ ] Force Cerebras failure → Groq header `X-Orby-Provider: groq`
- [ ] Turnstile issues HMAC cookie on production load
- [ ] `/studio` redirects unauthenticated users

---

## Related Notes

- Supersedes stale claims in: [[security/README]], [[05 - Model Layer, Rate Limiting & Abuse]], graphify `chatbot/02-model-router.md`
- Implements reconciliation requested across: [[security/phase-1-auth-clerk]] through [[security/phase-5-monitoring]]
- UX polish tracked separately: `frontend/UI Fixes.md`, [[frontend/BUILD-STATUS]]
- MCP deferral context: [[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan]]

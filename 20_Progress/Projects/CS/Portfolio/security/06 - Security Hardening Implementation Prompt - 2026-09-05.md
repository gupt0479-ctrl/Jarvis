---
type: concept
status: active
created: 2026-09-05
updated: 2026-09-05
tags:
  - portfolio
  - security
  - orby
  - implementation-prompt
notes:
  - "[[nextgen-chatbot/11 - Orby Security & Reliability Ground Truth - 2026-09-05]]"
  - "[[nextgen-chatbot/12 - Orby Hardening Implementation Guide - 2026-09-05]]"
  - "[[security/README]]"
  - "[[security/cloudflare-strategy]]"
  - "[[security/manual-actions]]"
---

# Security Hardening Implementation Prompt — 2026-09-05

> **One narrow, execution-ready task.** Notes 11 and 12 are the wide reference (verified-status tables, external research, OWASP cross-reference) — this note does not repeat them. This note picks exactly six things out of them (plus one dashboard gate they share) that the user named as the current "security layer thin → tightened" bridge, re-verifies each personally against live code/live DNS one more time, resolves the one open ambiguity (Cloudflare), and turns the result into a single implementation prompt Cursor can execute in one sitting. Read notes 11/12 for background; read this note to actually do the work.

## Re-verification pass (2026-09-05, this session)

Everything below was independently re-checked against the live repo/live domain in this session, not carried forward from notes 11/12 unread:

- **Provider chain, budget tiering, cooldown mechanics** — confirmed against `src/lib/model-router.ts` directly (full file read). Matches note 11 exactly: `Cerebras zai-glm-4.7 → Groq llama-3.3-70b-versatile → Mistral mistral-small-latest → degraded`.
- **CSP enforced, `/api/health` public, Clerk scoped to `/studio(.*)` only** — confirmed against `next.config.ts`, `src/proxy.ts`, and a live `curl -I https://anantgupta.dev` (see below). Matches note 11.
- **`/api/orby-comment` has no HMAC/Turnstile gate** — confirmed by reading the full route file: it has `BLOCKED_UA`, `isAllowedOrigin`, and a 3/60s per-IP Upstash limiter, but no `chat-token` verification. Matches note 11/12.
- **`SANITY_API_TOKEN` is used as both `serverToken` and `browserToken`** — confirmed in `src/sanity/lib/live.ts:8-14`. Matches note 11/12.
- **`eval-gate.yml` is advisory (`continue-on-error: true`)**, uses `CEREBRAS_API_KEY` — confirmed. No Semgrep config anywhere in the repo (grep empty). Matches note 11/12. **Both restoring the blocking eval gate and wiring Semgrep are already fully specified in note 12 (P0-2, P1) and are deliberately NOT duplicated in this prompt — out of scope here, see "Explicitly out of scope" below.**
- **Cloudflare is genuinely the live edge, not just header-shaped code** — resolved by live `curl -I https://anantgupta.dev`:
  ```
  server: cloudflare
  cf-ray: a3632b3c8b1f4ca0-MSP
  cf-cache-status: DYNAMIC
  x-vercel-id: cle1::iad1::rpzpc-...
  x-vercel-cache: MISS
  ```
  Both a real Cloudflare ray ID *and* a real Vercel deployment ID are present on the same response — this is Cloudflare (orange-cloud proxy) sitting in front of Vercel, exactly as [[security/cloudflare-strategy]] designed it, not `request-guards.ts` opportunistically reading headers that don't mean anything. **The ambiguity the user asked to resolve is resolved: Cloudflare is real infrastructure here, and concrete WAF rules for it already exist** (see Task 5).
- **The Cerebras leak fix is NOT "reuse Groq's exact mechanism" as note 12 frames it** — corrected below in Task 2. Groq's provider-level check in `model-router.ts` inspects `JSON.stringify(response)` *before* streaming starts, which only works because Groq's SDK surfaces `tool_use_failed` as response metadata. Cerebras's failure (the model narrates a tool call as plain text instead of invoking it) does not exist yet at that point — it only appears once the stream's text content arrives, which is too late to swap providers for *this* turn. The real, already-half-built mechanism to extend is in `chat/route.ts`'s stream `finish` handler and `sanitizeChatText()` (see Task 2) — smaller diff, and provably matches what the code actually does today.

---

## What this prompt covers (and what it deliberately doesn't)

**In scope:** Clerk re-verification, the Cerebras tool-leak cooldown fix, HMAC-gating `/api/orby-comment`, the Sanity token/CORS/mutation-path check, the Cloudflare WAF verification (resolved, not designed from scratch), the Upstash fail-open logging upgrade, and the AI-use-policy content spec (handed off to the SEO/AEO prompt's privacy-page task, not built here).

**Explicitly out of scope (tracked elsewhere, do not duplicate):**
- Restoring blocking `eval-gate.yml` CI and wiring Semgrep — fully specified in [[nextgen-chatbot/12 - Orby Hardening Implementation Guide - 2026-09-05]] P0-2 and P1. Separate task.
- Reordering or adding a 4th provider leg — gated on the Cerebras billing dashboard check (P0-0 below), and out of scope for this specific ask regardless.
- Building the actual `/privacy` page — that's `[[AEO & SEO/02 - SEO to AEO Implementation Prompt - 2026-09-05]]` Task 4. This note only supplies the AI-specific content that page must include.
- Orby visual/animation polish — separate frontend session (`frontend/UI Fixes.md`).

---

## Implementation prompt

> Written for a single autonomous coding session (Claude Sonnet 5 in Cursor). Context is front-loaded; no follow-up turn should be needed to clarify scope. Some tasks are dashboard-only verification, not code — they are written as explicit numbered steps to report back on, not as code TODOs.

```
REPO: hub/portfolio — Next.js 16 App Router, Clerk auth, Sanity CMS, an AI chat
agent (Orby / Portfolio Lab) behind Cerebras → Groq → Mistral → degraded mode,
Upstash Redis for rate limiting, Cloudflare (proxied DNS) in front of Vercel.

READ-ONLY constraint: do not run pnpm commands, do not call any AI provider,
do not print or log any env var VALUE (names are fine). Only touch the files
named in each task below. Do not touch frontend/UI components.

Do these seven tasks in order. Each is independently scoped — do not let a
finding in one task change your approach to another unless a task explicitly
says so.

──────────────────────────────────────────────────────────────────────────
TASK 0 — Cerebras billing status (manual check, non-blocking for Tasks 1-6)
──────────────────────────────────────────────────────────────────────────
Cerebras's no-card free tier reportedly ended in August 2026; new accounts
now get a one-time $5 credit expiring 30 days after a payment method is
added. This project's Cerebras key may predate that change and be
grandfathered, or may not be.

Ask the human operator to check https://cloud.cerebras.ai (Billing/Usage tab)
for the account tied to the live CEREBRAS_API_KEY, and report back: (a) is a
payment method on file, (b) credit balance and expiry if on the trial, (c)
which pricing tier the account is actually on. Do not guess or assume an
answer. This does not block Tasks 1-6 below (none of them depend on Cerebras
staying primary) — it only matters for a future decision about reordering
PROVIDER_CHAIN, which is explicitly not part of this task.

──────────────────────────────────────────────────────────────────────────
TASK 1 — Re-verify Clerk/Studio auth boundary (verify only, no code change
expected)
──────────────────────────────────────────────────────────────────────────
Read src/proxy.ts in full. Confirm:
- The only protected route matcher is `/studio(.*)` via `createRouteMatcher`.
- `/api/health`, `/api/error-report`, and `/api/chat` are excluded from both
  matcher patterns in `export const config`.
- `src/app/studio/layout.tsx` and `src/app/studio/page.tsx` do not have a
  second, conflicting auth check that could either double-protect or
  accidentally bypass the proxy-level guard.

Report exactly what you find. If it matches the above (it did on
2026-09-05), make NO code change — this task exists to catch drift, not to
force a change. If it does NOT match, stop and report the discrepancy before
touching anything; this is an auth boundary, not a place to guess a fix.

──────────────────────────────────────────────────────────────────────────
TASK 2 — Cerebras tool-call leak: set a real cooldown, don't just clean text
──────────────────────────────────────────────────────────────────────────
File: src/app/api/chat/route.ts (the stream `finish` handler, look for the
existing `// Groq tool_use_failed detection (in-stream)` comment and the
`sanitizeChatText(accText)` call a few lines below it).

CONTEXT — verified, not guessed: sanitizeChatText() (src/lib/chat-sanitizer.ts)
already generically strips leaked tool-call JSON from ANY provider's output
via several regexes (`{"tool":...}`, `{"function":...}`, `{"name":
"navigate"|...}`, etc.) and returns `cleanText` plus `extractedSectionId` when
it successfully reconstructs a navigation intent from leaked text. This
already partially handles the Cerebras leak for the CURRENT turn. What is
missing: when sanitizeChatText actually found and stripped something
(`sanitized.cleanText !== accText`), nothing tells the router this provider
just had a soft failure — so on the visitor's VERY NEXT message, Cerebras is
tried again with the same odds of leaking again. There is no cooldown set.

Do NOT attempt to detect the leak before streaming starts and swap providers
mid-turn — Cerebras's failure only exists in the streamed text, not in the
pre-stream response object (that's why Groq's `JSON.stringify(response)`
metadata check in model-router.ts doesn't transfer here; it relies on Groq's
SDK surfacing an error field that Cerebras's generic OpenAI-compatible client
does not have for this failure mode). Reusing that specific mechanism here
would be a no-op, not a fix — do not do it.

THE FIX: immediately after the existing `const sanitized =
sanitizeChatText(accText);` line, if `sanitized.cleanText !== accText` (i.e.
the sanitizer actually found and stripped leaked tool-call JSON) AND
`routeResult.provider !== "groq"` (Groq already has its own harder failure
path a few lines above — don't double-handle it), set the same cooldown key
the router already uses: `chat:cooldown:${routeResult.provider}` in Upstash,
TTL 30s, via the same Redis client pattern already used in
src/lib/model-router.ts (`redis.set(cooldownKey, "1", { ex: 30 })`) — you'll
need to either import/instantiate Redis the same way route.ts already does
elsewhere in this file, or export a small helper from model-router.ts and
import it (whichever is the smaller diff given what's already imported in
route.ts — check before deciding). Emit a structured log line matching this
file's existing convention: `console.log(JSON.stringify({ event:
"chat.tool_leak.cooldown_set", provider: routeResult.provider, sessionId
}))`.

Do not change the existing Groq hard-fail block above it. Do not change
sanitizeChatText's regexes. Do not change what gets sent to the client for
this turn — the sanitizer's existing cleanup/synthetic-navigate behavior for
the CURRENT turn is unchanged; this task only makes the NEXT turn route
around a provider that just leaked.

──────────────────────────────────────────────────────────────────────────
TASK 3 — HMAC-gate /api/orby-comment
──────────────────────────────────────────────────────────────────────────
File: src/app/api/orby-comment/route.ts

This route currently checks BLOCKED_UA, isAllowedOrigin, and a 3-req/60s
Upstash limiter, but never verifies the HMAC session cookie that
/api/chat requires. It still calls routeChat() (the same Cerebras → Groq →
Mistral chain), so an unauthenticated caller can consume real provider quota
today.

Find the exact HMAC verification helper /api/chat/route.ts uses (it reads a
signed httpOnly cookie issued by /api/chat-token — check
src/lib/chat-token.ts for the verify function's exact name and signature).
Import and call that same helper in orby-comment/route.ts's POST handler,
positioned after the UA/origin checks and before the rate limiter (cheapest
checks first, matching the existing order in this file). On missing/invalid
token, return the same 401 shape /api/chat already returns for this case —
do not invent a different response shape for what is the same failure mode.

Do not build a second token-issuance mechanism. Do not change
/api/chat-token/route.ts. Do not change the existing UA/origin/rate-limit
checks already in orby-comment/route.ts — this task only adds one more gate
to the existing chain.

VERIFY:
curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:3000/api/orby-comment \
  -H "Content-Type: application/json" -H "Origin: http://localhost:3000"
Before this fix: 200. After this fix: 401 (matching the documented
/api/chat behavior in security/manual-actions.md's Phase 3 curl check).

──────────────────────────────────────────────────────────────────────────
TASK 4 — Sanity safety net: one code check, two dashboard checks
──────────────────────────────────────────────────────────────────────────
4a (code, verify-only): grep the entire src/ tree (excluding anything under
src/app/studio/**, which is expected to have Studio's own write path) for
Sanity mutation calls: `.create(`, `.createOrReplace(`, `.createIfNotExists(`,
`.patch(`, `.delete(`, `.mutate(`, `client.transaction(`. Report every match
with file:line. Note 11 claims zero mutation calls exist in the Next.js
layer outside Studio — confirm or refute this with the actual grep output,
don't just restate the claim.

4b (dashboard, manual — report back, do not guess): ask the human operator to
open https://www.sanity.io/manage → project → API → Tokens, find the token
set as SANITY_API_TOKEN, and confirm its Permissions column reads exactly
"Viewer". This token is passed as BOTH serverToken and browserToken in
src/sanity/lib/live.ts, meaning it is shipped to the browser via the Live
Content API's SSE connection — if it is anything more permissive than
Viewer, that is a real write-capable token exposed client-side. If it is not
Viewer, do not attempt to fix this from code; report it and stop, this is a
dashboard-only remediation (rotate the token in Sanity, per
security/manual-actions.md 2A).

4c (dashboard, manual — report back): ask the human operator to open the
same project's API → CORS Origins list and confirm it contains only known
origins (localhost:3000, the production domain, any preview domains
actually in use) with no wildcard `*` entry.

──────────────────────────────────────────────────────────────────────────
TASK 5 — Cloudflare WAF: verify deployment, don't redesign rules
──────────────────────────────────────────────────────────────────────────
Cloudflare is confirmed live in front of this domain (verified via
`curl -I https://<production domain>` showing both a `cf-ray` header and a
Vercel `x-vercel-id` header on the same response — Cloudflare is proxying to
Vercel, not a phantom). Concrete WAF rules for this exact setup already exist
in the vault (security/cloudflare-strategy.md Part 2, security/manual-actions.md
6D) — this task is a DEPLOYMENT verification, not a rule-design task.

Ask the human operator to open the Cloudflare dashboard for this domain →
Security → WAF and confirm, reporting back exactly what's found for each:
1. Custom Rule blocking scanner user-agents (sqlmap, nikto, nmap, masscan,
   zgrab, nuclei) — deployed and active?
2. Custom Rule blocking empty User-Agent on `/api/*` paths — deployed and
   active?
3. Rate Limiting Rule on the chat API path (~20 req/60s per IP, block
   action) — deployed and active?
4. SSL/TLS mode set to "Full (strict)", not "Full" or "Flexible"?

If any of these four are missing, the exact rule text to paste in is already
written in security/cloudflare-strategy.md "Part 2 — WAF rules" and
security/manual-actions.md section 6D — do not write new rule expressions,
copy those verbatim. Do not attempt to configure Cloudflare via API/Terraform
in this session — this is a dashboard-only task, report status and let the
human operator apply anything missing.

──────────────────────────────────────────────────────────────────────────
TASK 6 — Upstash fail-open: keep the behavior, upgrade the observability
──────────────────────────────────────────────────────────────────────────
File: src/app/api/chat/route.ts, the catch block around the rate-limit calls
containing: `console.warn("[chat] Upstash unreachable — rate limiting
skipped", err);`

DECISION (already made, do not re-litigate): keep fail-open. On a Redis
outage, letting the chat endpoint keep serving (rather than 500ing every
visitor) is the right tradeoff for a portfolio site — the provider chain's
own per-provider rate limits are a second layer that still caps runaway
cost even with Upstash down, and a Redis blip is rarer than "recruiter mid-
conversation gets a hard error." Do not change this to fail-closed.

THE ACTUAL GAP: this is a plain console.warn with no structured `event`
field, unlike every other log line in this file and in model-router.ts
(which all use `console.log(JSON.stringify({ event: "...", ... }))`). That
makes a live Upstash outage invisible to any log-based alerting that filters
on the `event` field. Change this one line to match the file's existing
structured-logging convention: `console.log(JSON.stringify({ event:
"chat.ratelimit.fail_open", ip }))` — keep it as a genuine log (not an
error/throw), keep the exact same fail-open control flow, just make the
event structured and include the client IP (already computed earlier in
this function via getClientIp). Do the identical thing to the equivalent
line in src/app/api/orby-comment/route.ts if one exists there too — check,
don't assume.

──────────────────────────────────────────────────────────────────────────
TASK 7 — AI-use policy: content spec only, no page to build here
──────────────────────────────────────────────────────────────────────────
Do NOT create a /privacy route or any new page in this task — that page is
built by a separate SEO/AEO implementation prompt. Your job here is to
produce a short, factual list of what that page's AI-specific section must
disclose, based on what Orby's code actually does (verify each line against
the router/tools/context files named, don't invent boilerplate):

- Orby only answers using a fixed catalog fetched from Sanity CMS per
  request (src/lib/chat-context.ts) — it does not browse the web or access
  data outside that catalog.
- Orby's available actions are a fixed, closed set of tools (name them —
  check src/lib/chat-tools.ts for the real current list) — it cannot take
  arbitrary actions on the visitor's behalf.
- Messages are routed to third-party model providers in this order: Cerebras,
  then Groq, then Mistral, falling back to pre-written responses if all are
  unavailable (verify this is still the live order in model-router.ts before
  writing it down). State plainly, without hedging or omission, whether any
  of these providers' free tiers may log or use submitted prompts (check
  each provider's current published terms — do not assume a policy that was
  true when [[nextgen-chatbot/05 - Model Layer, Rate Limiting & Abuse]] was
  written in June 2026 is still current; verify freshly).
- Whether conversation history persists beyond the active browser session
  (verify: does anything write chat messages to a database, or does state
  live only in the client + a short-TTL Redis session counter?).
- That a bot-check (Cloudflare Turnstile) runs before a chat session token
  is issued, and why (abuse prevention, not tracking).

Output this as a plain markdown list appended to THIS note (not a new file,
not a new route) under a new "## AI-Use Policy Content (for /privacy)"
heading, so the SEO/AEO prompt's privacy-page task can paste it in directly.

──────────────────────────────────────────────────────────────────────────
FINAL REPORT
──────────────────────────────────────────────────────────────────────────
For each of Tasks 0-7, state: what you found, what you changed (file:line)
or explicitly did not change, and for every dashboard-only item, the exact
question the human operator still needs to answer. Run `pnpm typecheck` on
any file you touched (Tasks 2, 3, 6 only) and paste the output — do not run
`pnpm build`, `pnpm dev`, or anything that would call a live provider. Do not
commit or push anything.
```

---

## AI-Use Policy Content (for `/privacy`)

*(Placeholder — Task 7 above is written to be executed by the coding agent
that runs this prompt, which will verify the current tool list/provider
terms/session-persistence facts against live code and fill this section in
before handing off to [[AEO & SEO/02 - SEO to AEO Implementation Prompt - 2026-09-05]]'s privacy-page task. Do not treat this section as populated until that run completes — the SEO/AEO prompt's Task 4 should re-check whether this heading has real content before writing the page, and ask the user if it's still empty.)*

---

## Decisions kicked back to the user

1. **Cerebras billing status (Task 0)** — cannot be checked from the repo; needs a dashboard login. Blocks nothing else in this prompt, but blocks any future provider-chain reordering decision.
2. **Whether to also restore blocking `eval-gate.yml` CI and wire Semgrep now** — both are fully spec'd in note 12 (P0-2, P1) but deliberately excluded from this prompt's scope per the user's own framing of what "tightened" covers this round. Flagging in case the user wants them folded in.
3. **Sanity token scope and CORS list (Task 4b/4c)** and **Cloudflare WAF rule deployment status (Task 5)** are genuinely unknown until someone opens those dashboards — this prompt cannot resolve them, only tell the operator exactly what to look for and what to paste in if missing.

## Evidence

Verified read-only against `/home/anant_gupta/projects/hub/portfolio` (branch `post-frontend`) and a live `curl -I` against production, 2026-09-05, in this session (not carried forward unverified from notes 11/12):

- `src/lib/model-router.ts` — full file, provider chain, cooldown, Groq metadata check
- `src/app/api/chat/route.ts` — lines ~200-230 (Upstash fail-open catch), ~460-560 (stream finish handler, Groq in-stream check, sanitizer call)
- `src/lib/chat-sanitizer.ts` — full regex set for leaked tool-call JSON (lines 12-148)
- `src/app/api/orby-comment/route.ts` — full file, confirmed no HMAC gate
- `src/sanity/lib/live.ts` — lines 1-30, confirmed shared server/browser token
- `src/proxy.ts` — full file, matcher config
- `next.config.ts` — CSP header block
- `.github/workflows/eval-gate.yml` — full file, `continue-on-error: true` confirmed
- `.claude/commands/ship-check.md`, `.claude/commands/deploy.md` — confirmed existing review pipeline
- `security/cloudflare-strategy.md`, `security/manual-actions.md` (Phases 2, 3, 5, 6) — existing dashboard-step specs, reused not re-derived
- Live `curl -I https://anantgupta.dev` — confirmed enforced CSP, `server: cloudflare` + `cf-ray` alongside `x-vercel-id`, HSTS, and Cloudflare Turnstile domains present in the CSP's `script-src`/`connect-src`/`frame-src`
- `grep -r semgrep` and `find -iname "*.semgrep*"` across repo — both empty, confirming note 11/12's claim

## Related Notes

- Extends and narrows: [[nextgen-chatbot/11 - Orby Security & Reliability Ground Truth - 2026-09-05]], [[nextgen-chatbot/12 - Orby Hardening Implementation Guide - 2026-09-05]]
- Reuses dashboard steps from: [[security/manual-actions]], [[security/cloudflare-strategy]]
- Hands off content to: [[AEO & SEO/02 - SEO to AEO Implementation Prompt - 2026-09-05]] (privacy page)
- Does not touch: frontend UI (`frontend/UI Fixes.md`), the eval-gate/Semgrep CI work (note 12 P0-2/P1)

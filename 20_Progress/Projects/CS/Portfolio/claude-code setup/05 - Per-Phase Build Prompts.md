---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-10
tags:
  - portfolio
  - claude-setup
  - prompts
notes:
  - "[[00 - Claude Code Build Kit — Index]]"
  - "[[08 - Build Phases & Milestones]]"
---
# Per-Phase Build Prompts
Copy-paste prompts for Claude Code (Sonnet 4.8), one per phase from [[08 - Build Phases & Milestones]]. There are eight implementation prompts (Phase 0–7) plus a launch checklist (Phase 8) that is mostly verification. Run each in its own session.
## How to use these
1. `/clear` first — start every phase with a clean context window.
2. Paste the phase prompt verbatim. Each one points Claude Code at the *one* phase note and its dependencies via the mounted path — it reads only those, not the whole set.
3. Let it implement (it delegates to the right subagent), then it runs `/eval` and `/typecheck`.
4. Review the diff, commit, `/clear`, next phase.
The path prefix used below (set once, mentally):
`NB = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot`
## Phase 0 — Prove the pipe
```
Read NB/01 - Layered Architecture.md (the model + runtime layers only) and NB/05 - Model Layer, Rate Limiting & Abuse.md.
Build a minimal /api/chat route in the repo that calls Gemini 2.5 Flash with one hardcoded system prompt and returns plain text. Key is server-only, never in the client bundle. Use the ai-engineer subagent. No UI, no tools, no grounding yet. Run /typecheck. Confirm the key is absent from the client bundle, then stop and report.
```
## Phase 1 — Lock the gates
```
Read NB/05 - Model Layer, Rate Limiting & Abuse.md fully.
Use ai-engineer then security-reviewer. Add: origin/referer check + a stateless HMAC-signed httpOnly cookie issued on page load and verified at the edge; Upstash per-IP rate limit (~50/day + ~10/min burst); block scraper user-agents; per-request token budget, max-tool-step cap, and timeouts on every model/tool call. Provision Upstash via its MCP. Run /typecheck. Verify a tokenless call to /api/chat is rejected and the cap trips in a test. Report which premortem failures (5, sets up 2) are closed.
```
## Phase 2 — Grounding + refusal
```
Read NB/03 - Context Engine, Grounding & Personas.md fully.
First use sanity-schema to populate clean slug fields on every project (prerequisite for the closed enum). Then use ai-engineer to wire the context engine: always-on Sanity catalog (title/slug/one-liner for every item) + on-demand full records, injected per turn; the hard refusal rule; live reads (no build-time snapshot). One neutral prompt, no personas yet. Run /typecheck. Manually confirm it answers from real data and refuses what isn't in Sanity. Report (closes premortem 1, 7).
```
## Phase 3 — Eval set + tracing
```
Read NB/07 - Evaluation & Observability.md and the claude-code setup note "04 - Eval Harness — promptfoo.md".
Use eval-runner. Install promptfoo, scaffold eval/ with the deterministic cases (grounding, refusal, tool-correctness placeholder, injection, fail-safe) and per-turn tracing (model used, tool calls, refusal/validation outcomes) on /api/chat. Wire the GitHub Actions gate. Run /eval — grounding and refusal cases must pass now. Report (closes premortem 8).
```
## Phase 4 — Personas + power-prompts
```
Read NB/03 - Context Engine, Grounding & Personas.md fully.
Use ai-engineer for the four in-repo persona system prompts (recruiter, friend, weirdo, ceo) + the output safety guard, and frontend-builder for the sidebar sections, suggested chips (click→drop→send), and the author-written copy-paste power-prompts for recruiter and ceo (paste detects persona marker and locks it). Add the persona warmth judge council to the eval suite. Run /eval — persona cases (same facts, different voice; weirdo stays in guardrail) and warmth floors must pass. Report (closes premortem 6).
```
## Phase 5 — Tools + generative UI
```
Read NB/06 - Tool System & Generative UI.md fully.
Use ai-engineer for the closed tool set (navigate, showProject, showExperience, lookupFact, getResume, contact) with enums built from Sanity, schema validation, and fail-safe-to-text; use frontend-builder for the evidence-card components fed by validated results, rendered via the Vercel AI SDK (layer 3 only). Run /eval — tool-correctness and fail-safe cases must pass. Report (closes premortem 3).
```
## Phase 6 — Router + degraded mode - here
```
Read NB/05 - Model Layer, Rate Limiting & Abuse.md (router + degraded sections).
Use ai-engineer. Add the Groq fallback behind the router and the degraded mode that serves persona pre-written answers + deterministic navigation when all free quotas are exhausted. Run /typecheck and /eval. Verify: forcing Gemini to fail routes to Groq; forcing both to fail still yields a working degraded Orby, not an error. Report (closes premortem 2).
```
## Phase 7 — Wire Orby
```
Read NB/04 - Orby Integration.md fully.
Use frontend-builder. Implement the deterministic pipeline: on a navigate decision Orby returns to the portfolio-button home, the page scrolls to the Sanity nav link, and on arrival Orby pops the per-request creative message (generated in the same model turn, persona-voiced, grounded, output-guarded, length-capped). Keep this fully separate from the existing scroll popups. Respect prefers-reduced-motion; one navigation per turn; malformed call → text only, no visual. Run /eval and an e2e smoke test. Report (closes premortem 4).
```
## Phase 8 — Launch readiness (checklist, mostly verification)
```
Read NB/08 - Build Phases & Milestones.md (Phase 8) and "02 - Deploy Security Checklist.md".
Confirm the portfolio is fully usable with Orby ignored (premortem 9). Run the full /eval suite, eyeball recent traces, run security-reviewer + /security-review, walk the deploy checklist, and verify security headers on the live .dev URL. Confirm every premortem failure has its named defense shipped with a passing check behind it. Then /deploy. Report the final coverage table.
```
## Note on "8 prompts"
Phases 0–7 are the eight implementation prompts. Phase 8 is a verification/deploy gate, not new building. If you want to compress further, Phase 0 is tiny and can be folded into Phase 1's session — but keeping them separate gives a clean "the pipe works" checkpoint before any security wiring.

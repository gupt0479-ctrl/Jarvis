---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-10
tags:
  - portfolio
  - ai
  - roadmap
notes:
  - "[[00 - Nextgen Chatbot — Build Plan]]"
  - "[[02 - Premortem & Failure Defenses]]"
---
# Build Phases & Milestones
This note owns the order we build in. The rule: each phase ships something that works end to end and closes the premortem failures it is responsible for. A phase is not done until its defense exists — not just its feature. Build in WSL with Claude Code (the two-machine rule); this note is the plan, the repo is the executor.
## Why this order
We build the spine before the polish: prove the pipe, lock the gates, then add the impressive parts on top of something safe. The generative UI and Orby navigation are last *on purpose* — they depend on a reliable tool layer, and shipping them first is how the wow feature becomes the broken feature (premortem 3).
## Phase 0 — Prove the pipe
Stand up `/api/chat` calling Gemini behind a server route, one hardcoded system prompt, plain text replies, no UI polish. Key server-only.
Done when: a message in, a grounded-ish text reply out, key never in the client bundle.
## Phase 1 — Lock the gates (before any public exposure)
Origin/referer check + signed session token, Upstash per-IP cap (~50/day + burst), Vercel WAF Attack Challenge Mode, scraper UA blocking. Per-request token budget, max-tool-step cap, model/tool timeouts.
Done when: the bare endpoint refuses tokenless calls, the cap trips in testing, and a runaway request cannot loop or overspend. Closes premortem 5; sets up 2. See [[05 - Model Layer, Rate Limiting & Abuse]].
## Phase 2 — Grounding + refusal
Wire the context engine to read live Sanity records and inject them; add the hard refusal rule and the safety guardrail. No personas yet — one neutral prompt.
Done when: the eval-set grounding and refusal checks pass — it answers from real data and refuses what is not there. Closes premortem 1 and 7. See [[03 - Context Engine, Grounding & Personas]].
## Phase 3 — Eval set + tracing
Write the 15–20 eval checks and per-turn tracing now, while the system is still simple, so every later phase is guarded.
Done when: evals run and gate deploy; traces show model used, tool calls, refusal outcomes. Closes premortem 8. See [[07 - Evaluation & Observability]].
## Phase 4 — Personas + power-prompts
Add the four persona system prompts, the sidebar sections, the suggested chips (click→drop→send), and the author-written copy-paste power-prompts for recruiter and ceo. Add the output guard.
Done when: persona eval checks pass — same facts, different voice, weirdo stays inside guardrails; power-prompt paste locks the right persona. Closes premortem 6.
## Phase 5 — Tools + generative UI
Add the closed tool set with schema validation and fail-safe-to-text, and the evidence-card components fed by validated results.
Done when: tool-correctness and fail-safe eval checks pass — cards render from real data, malformed calls degrade to text. Closes premortem 3. See [[06 - Tool System & Generative UI]].
## Phase 6 — Router + degraded mode
Add Groq fallback and the degraded mode that serves persona pre-written answers when all quotas are gone.
Done when: forcing Gemini to fail routes to Groq; forcing both to fail still gives a working (degraded) Orby, not an error. Closes premortem 2.
## Phase 7 — Wire Orby
Connect the `navigate(sectionId)` pipeline: model call → scroll to Sanity nav link → on-arrival message. Keep it separate from scroll popups; respect reduced motion; one navigation per turn.
Done when: "show me your projects" scrolls once and Orby speaks on arrival; a malformed call does nothing visual and falls back to text; scroll popups still work independently. Closes premortem 4. See [[04 - Orby Integration]].
## Phase 8 — Launch readiness
Confirm it is additive and dismissible (portfolio fully usable with Orby ignored — premortem 9), run the full eval set, eyeball traces, walk the [[02 - Deploy Security Checklist]], verify headers on the live `.dev` URL.
Done when: every premortem failure has its named defense shipped and a passing eval or check behind it.
## Coverage table
| Premortem failure | Closed in phase |
|---|---|
| 1 — lies about me | 2 |
| 2 — quota dies under traffic | 6 |
| 3 — weak tool-calls break wow feature | 5 |
| 4 — intent/page desync | 7 |
| 5 — endpoint abused as free LLM | 1 |
| 6 — prompt injection / ugly output | 4 |
| 7 — content drift | 2 |
| 8 — silent degradation | 3 |
| 9 — gets in the way | 8 |
| 10 — over-built | scope cuts in [[01 - Layered Architecture]], enforced throughout |

---
type: project
status: active
created: 2026-07-13
updated: 2026-07-13
related:
  - "[[Mentor Meeting Playbook]]"
  - "[[Portfolio]]"
  - "[[Stocks Trading AI Hub]]"
  - "[[CausalOps — Index]]"
tags:
  - mentorship
  - meeting-prep
  - project-briefing
next: "Re-verify anantgupta.dev right before the call if UI fixes shipped"
---
# Project Briefings — 2026-07-13
Concrete, source-checked summaries of the three projects for tonight's meeting. Every claim below was verified against either the live site (scraped 2026-07-13), the project's own vault notes, or both — nothing here is guessed. Use this note during the call as the ground truth; [[Mentor Meeting Playbook]] has the script.
## Portfolio (anantgupta.dev) — Live, Focus Is Orby
**Status, verified live right now:** the site is deployed and populated with real content — About, Experience (4 real roles including a freelance "Side Hustle: Coming soon"), Projects (SafeReach, Orby itself, Jarvis, more), Skills (55 skills across 10 categories), real Certifications (CITI Program, Outskill Generative AI — the earlier fake AWS/GCP/CKA certs are gone), Achievements, and a blog feed. One honest gap found on the live scrape: the blog posts shown ("Building Scalable React Applications with Next.js 14," dated Jan 2024) read like generic fallback/placeholder content, not real posts — worth a private note, not necessarily a meeting topic unless it comes up naturally.
**UI fixes — conditional, do not bring up unless live:** a 14-item UI-fix backlog exists (Experience card colors, Projects carousel motion, Skills graph styling, Education flowchart, Footer rebuild, etc. — full list in `frontend/BUILD-STATUS.md` and the 2026-07-11/07-13 fix-implementation notes). *If these ship before the call, it's fine to ask for a general reaction. If not, skip portfolio UI entirely* — the main ask is Orby, not visual polish.
### What Orby Actually Is
Orby is two connected things, not one:
1. **The visual companion** — a 3D floating astronaut character (`Orby.tsx`, `OrbyCanvas.tsx`, React Three Fiber) that lives bottom-right on the page and inside the "Portfolio Lab" chat sidebar. It has a speech cloud with a typewriter effect, reacts to scroll position with canned lines, and returns to a home position between actions.
2. **The AI agent behind the chat** — a grounded, tool-using LLM agent (not a plain chatbot) that only answers from real Sanity CMS content, can navigate the visitor to a page section, and switches voice across four personas: Recruiter, Friend, Weirdo, CEO. This is the harder, more interesting half.
### How It Was Actually Built — the Architecture
The build deliberately treats the model call as **the least interesting layer** and invests in everything around it:
- *Grounding + refusal:* every fact comes from live Sanity content injected per turn; the agent refuses when the answer isn't in the data — no invented projects or skills.
- *Closed tool set:* `navigate`, `showProject`, `showExperience`, `lookupFact`, `getResume`, `contact` — a fixed, validated tool contract, not free-form function calling. Tool results render as **evidence cards** (real components) below the chat prose, not as walls of text.
- *Personas as context engineering:* four author-written system prompts, not four different models. Fixed "power-prompts" per persona are hand-written and copy-pasted verbatim by the visitor — proof of deliberate prompt design, not model output.
- *Model router with fallback:* Gemini primary, Groq/Cerebras fallback, a "degraded mode" with pre-written answers if every provider's quota is exhausted — the chat should never just error out.
- *Rate limiting + abuse resistance:* origin/referer check, HMAC-signed session token, Upstash per-IP cap, Cloudflare Turnstile anti-bot challenge, scraper UA blocking.
- *Eval harness:* a Promptfoo suite (grounding, refusal, tool-correctness checks) gates deploys — this is the part most student projects skip entirely.
- *Security hardening phases:* Clerk auth, Sanity Studio lockdown, chatbot resilience, deployment hardening (CSP headers, security headers), and monitoring — five documented phases, not an afterthought.
### Known Real Problems (found in live testing, not theoretical)
A root-cause debugging session (documented in the project's own notes) found:
1. **Raw tool-call JSON sometimes leaks into the visible chat message** — `{ "tool": "navigate", ... }` text appearing where it shouldn't.
2. **Orby goes silent on some turns** — direct consequence of #1: Orby's speech is driven by a `navigate` tool-call event; when the model dumps the call as plain text instead of a real structured tool call, no event fires and Orby has nothing to say.
3. **The multi-provider fallback chain never actually fails over.** The router only retries on an exception (a failed HTTP request) — it has no way to detect "the model returned HTTP 200 but botched the tool call." So the free model (Cerebras) stays primary even when it's the least reliable one at the exact thing that makes Orby work, and Groq/Mistral sit unused as backups that never trigger.
4. **Azure GPT-4o-mini was designed as the reliable primary model but was never implemented in code** — the system is running on the weakest link by default, not by choice.
5. Cloudflare Turnstile intermittently fails in dev (separate, lower-stakes issue).
### The Concrete Question for Ahnaf
Not "does Orby look cool" — the real engineering question is: **how do you design failover/retry logic when the failure mode isn't an exception but a malformed-yet-"successful" response?** The architecture (grounding-first, closed tools, evals, personas as context engineering, security phases) is genuinely how a professional would lay this out. The gap is implementation-level: no quality-based failover, only exception-based — and the fact that a professional AI engineer would likely say "detect tool-call absence as a failure signal, not just HTTP errors" is exactly the kind of thing worth asking him to confirm or correct.
## TradingView — Personal Quant Side Project, Not a Revenue Play
**Reframing for tonight:** this is explicitly a personal project to learn markets — stocks and ETFs — not a product and not a way to make money. No monetization, no other users, no shared infrastructure with anyone else's money. That framing was locked in the project's own notes on 2026-07-10 ("personal edge only... no auth/tenancy... zero monetization").
**What it actually is, concretely:** a research tool that ingests real market data, scores stocks/ETFs on a factor stack (momentum, quality/free-cash-flow, safety/volatility, valuation), and now — as of 2026-07-12 — has a working LLM layer on top: an "Analyst" agent drafts a structured evidence card (action + confidence + reasoning) for a stock, and a separate "Critic" agent reviews it and can only ever *lower* the confidence, never raise it. Every number the model is allowed to write must come from a pre-rendered "quotable numbers" list — the prompt bans writing digits from memory entirely, which closes a real failure mode (models inventing precise-looking numbers).
**Current real status:** 497 automated tests passing (up from 483 the session before), real live evidence cards produced for NVDA from actual Gemini model calls (not fixture/test data) — e.g. one card scored NVDA "ACCUMULATE" citing a real quality score and valuation figures traced back to the underlying data; a separate Critic run correctly demoted a card's confidence after spotting a statistically weak signal instead of rubber-stamping it. A real, found-not-yet-fixed bug: the `created_at` timestamp field on these evidence cards isn't stamped server-side yet, so a live model run wrote a hallucinated placeholder date into one — flagged, not shipped as broken to anyone.
**Deliberately not built / not planned:** no prediction-market vertical (Kalshi/Polymarket) — parked by design until this stocks/ETFs half is fully proven; no UI beyond a CLI; no shared infrastructure between the two verticals if the second one is ever built, because the risk models and data-quality semantics for stocks vs. prediction markets are genuinely different, not just stylistically different.
**Why this framing matters for the ask:** because there's no revenue angle, the actual ask to Ahnaf is about the engineering discipline (evidence-bound LLM outputs, fail-closed statistical gates, a critic that can only downgrade) and what he'd want to see next as a portfolio-grade personal project — not about market strategy or making money.
## CausalOps — SOC Incident Causal-Reasoning Engine
**What it is, concretely:** a system that takes a cybersecurity incident description and produces an evidence-backed causal explanation of what happened — not just a plausible-sounding narrative. The core design rule: an LLM can propose hypotheses, but only deterministic statistical code can confirm or reject them. The LLM never gets to inject a data row or decide which causal edges survive.
**Architecture, in order:**
1. *Three-tier agent investigation* — a Grand Orchestrator decomposes an incident into 2-3 investigation angles (network forensics, insider threat, supply-chain exposure, etc.); each spawns 2 Parent agents; each Parent spawns 2 Child agents that each produce one structured "Decision Memo" citing concrete evidence needs (specific logs, CVEs, telemetry — not vague claims). An Evaluator agent ranks all the memos.
2. *A genetic-algorithm layer (island evolution)* tunes each agent's behavior across 8 traits (like evidence-weight and causal-focus) between runs — this steers agents toward better evidence use without a human hand-tuning prompts.
3. *The causal engine itself* — four deterministic stages with no further LLM involvement: causal discovery (PC algorithm statistical test on proposed cause-effect edges), an evidence compiler that silently drops any record flagged as LLM-synthetic data, a DoWhy estimation stage that computes the actual causal effect only if hard statistical gates pass (minimum row count, real treatment/outcome variation) — otherwise the result is honestly withheld, not guessed — and a reasoning layer that flags unexplained anomalies as the highest-severity signal.
4. *A knowledge-graph memory layer* — validated causal edges and anomalies get written to a graph database so future incident investigations can retrieve relevant past cases.
**Current real status (most recent, 2026-07-02):** the memory layer is fully coded and unit-tested (10 tests passing), blocked only on running a SQL migration and integration tests against an already-provisioned Supabase project. Everything upstream of memory (agents, causal engine, event bus) is implemented.
**Why this is worth showing Ahnaf:** the "LLM proposes, deterministic code disposes" pattern — and specifically that the system will honestly say "insufficient evidence" rather than force a causal estimate — is the same kind of statistical discipline a professional would want to see in any AI system making claims about cause and effect. That's the concrete thing to get his read on: does this look like real engineering judgment or over-engineering for a project this size?

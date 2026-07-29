---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[20_Progress/Projects/CS/Portfolio/nextgen-chatbot/10 - Orby Golden Eval Dataset (Grounding Cases)]]"
tags:
  - "#progress"
  - "#ai"
next: "Set up Semgrep + GitHub Actions on the portfolio repo as the free, permanent static-analysis layer"
---
# Code Review & Eval Gap
## Why This Exists
[[PDF's Ingestion Implementation#Code Review & Eval Gap: Pre-Commit AI Backstop - BUILD|PDF's Ingestion Implementation's Code Review & Eval Gap section]] proposed CodeRabbit CLI as an AI-generated-code backstop; testing rejected it (unreliable ~50% of the time, rate-limited after 2 PRs despite "free to start" marketing). [[00_Execution]] resolved the real fix as two separate, already-available tools solving two different problems — this note is that resolved state, not a re-analysis.
## The Two Problems, Not One
**Real code bugs** (logic errors, injection, secrets, race conditions) and **"AI slop"** (over-engineered abstractions, unnecessary hedging, generic verbose prose, dead defensive code) are different failure modes. A linter catches the first; nothing lint-shaped catches the second because "this function didn't need to exist" isn't a rule a static analyzer can express.
## Fix 1: Semgrep — Free, Permanent, Per-Repo
**What:** Open-source static analysis, no rate limits, runs pre-commit locally and integrates with GitHub Actions. Catches logic errors, SQL injection, secrets, race conditions — the real-bug category CodeRabbit failed to reliably catch.
**Setup:**
1. Install Semgrep locally (`pip install semgrep` or the standalone binary) on each active codebase — BOOM, Portfolio, TradingView, CausalOps.
2. Run `semgrep --config auto` against each repo once to establish a baseline; fix or explicitly suppress existing findings.
3. Wire into a GitHub Actions step (`.github/workflows/semgrep.yml`, following the same pattern as [[04 - Eval Harness — promptfoo|the promptfoo eval gate]]'s CI wiring) so every push runs the scan.
4. No API cost, no rate limit — this is a permanent layer, not a trial.
## Fix 2: `/simplify` + `/code-review` as a Standing Habit — Not a New Tool
**The actual AI-slop fix already exists in this vault, unused as discipline rather than missing as tooling:**
- `/simplify` — reuse, simplification, efficiency, and altitude cleanups on changed code. Quality only, doesn't hunt bugs.
- `/code-review` — the review pass for correctness and design (Semgrep and `/code-review` are complementary: one automated and deterministic, one judgment-based).
- `/remove-ai-slop` — the equivalent pass for prose notes, already built and in daily use per [[CLAUDE]].
- The explicit CLAUDE.md instruction against unrequested abstraction — already load-bearing, just needs actual enforcement via habit.
**Adoption pattern:** run `/simplify` and `/code-review` on every non-trivial diff, not as a new install but as a standing habit, the same way `/remove-ai-slop` is already habitual for notes.
## Fix 3: deepeval — Output Validation, Different Layer Again
Multi-dimensional scoring (faithfulness, correctness, relevance) for generated *text* output, RAG-style — a different failure mode from both code bugs and code slop. Already scoped for the Orby portfolio chatbot's factual grounding, but see [[20_Progress/Projects/CS/Portfolio/nextgen-chatbot/10 - Orby Golden Eval Dataset (Grounding Cases)]] for the corrected verdict: Orby's eval gate already uses **promptfoo**, not deepeval — deepeval is not currently adopted anywhere in this vault's active builds. If a future project needs RAG-style output validation and promptfoo's assertion model doesn't fit, deepeval is the fallback, not the default.
## Adoption Order
1. Semgrep + GitHub Actions — portfolio pre-deploy gate first, then BOOM/TradingView/CausalOps.
2. `/simplify` + `/code-review` habit — starts immediately, no setup cost.
3. Local LLM-as-judge — deferred until [[Model Distillation]]'s 3B model exists; zero running cost once it does.
## Failure Modes
> [!WARNING]
> Treating Semgrep as a slop fix (or `/simplify` as a bug-catcher) misapplies both tools — a diff can pass Semgrep clean and still be full of unrequested abstraction, and `/simplify` won't catch a real injection vulnerability. Run both, for different reasons.
## Evidence
- [[PDF's Ingestion Implementation#Code Review & Eval Gap: Pre-Commit AI Backstop - BUILD|Code Review & Eval Gap]] — the rejected CodeRabbit test and the free-stack recommendation
- [[04 - Eval Harness — promptfoo]] — the CI-wiring pattern to mirror for Semgrep
- [[20_Progress/Projects/CS/Portfolio/nextgen-chatbot/10 - Orby Golden Eval Dataset (Grounding Cases)]] — where deepeval was proposed and corrected to promptfoo
- [[00_Execution]] — the resolved verdict this note executes

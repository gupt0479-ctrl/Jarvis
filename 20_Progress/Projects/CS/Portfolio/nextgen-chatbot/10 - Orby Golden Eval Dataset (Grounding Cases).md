---
type: concept
status: sprout
created: 2026-07-29
updated: 2026-07-29
tags:
  - portfolio
  - ai
  - evaluation
notes:
  - "[[04 - Orby Integration]]"
  - "[[07 - Evaluation & Observability]]"
  - "[[04 - Eval Harness — promptfoo]]"
next: "Extend the starter grounding.yaml cases (now in [[04 - Eval Harness — promptfoo]]) to full 30-50 coverage once live Sanity content is pulled directly, rather than from vault-known project names"
---
# Orby Golden Eval Dataset (Grounding Cases)
## Correcting a Verdict, Not Re-Litigating the Build
[[PDF's Ingestion Implementation#Orby (Portfolio): Model Regression Detection for Eval - BUILD|PDF's Ingestion Implementation's Orby eval section]] proposed deepeval + GitHub Actions as a net-new "missing eval layer" for [[04 - Orby Integration]], and [[00_Execution]] confirmed that as a real gap after checking five build files (`04 - Orby Integration`, `09 - Orby Fixes`, `12 - Orby Friction Fixes`, `16 - Orby Enhancement + Codebase Audit`, `frontend/claude-code-setup/05 - Orby Final Polish Prompts`). **That check missed two files sitting in this same `nextgen-chatbot/` folder: [[07 - Evaluation & Observability]] and its build-kit companion [[04 - Eval Harness — promptfoo]].** Both already exist, both already specify a full CI-gated eval harness for Orby — using **promptfoo**, not deepeval, wired into GitHub Actions with deterministic assertions plus an `llm-rubric` judge council for persona quality.
Building a second, deepeval-based eval gate on top of an already-designed promptfoo gate would mean two competing eval systems testing the same chatbot — the opposite of what this pass is supposed to produce. This note does not re-open the decision to build an eval layer (that's settled and already speced); it corrects which tool it uses and identifies the one piece that's genuinely still missing.
## What Already Exists (Confirmed, Don't Rebuild)
- `eval/promptfooconfig.yaml` + `eval/cases/*.yaml` layout, versioned beside the persona prompts
- Deterministic cases for grounding/refusal, tool correctness, injection resistance, fail-safe behavior — each tagged to the premortem failure it guards (see [[02 - Premortem & Failure Defenses]])
- A judge council (2-3 `llm-rubric` graders, Gemini + one other free model) for subjective persona-warmth checks, with an explicit floor per persona
- A working GitHub Actions sketch (`.github/workflows/eval.yml`) that runs `promptfoo eval --fail-on-error` and gates deploy
- Local `/eval` command + `eval-runner` agent for phase-complete runs
## The Genuinely Missing Piece — Now Closed (2026-07-29)
`07`'s eval set was **15-20 cases**, and only two of them (`Grounding / refusal` and `Grounded positive`) tested factual faithfulness. BASWE's original ask (30-50 hand-built golden Q&A pairs from portfolio materials, faithfulness-threshold gated) has been built as a real, additive expansion of exactly that one category — not a second tool, a bigger `eval/cases/grounding.yaml`. Both [[07 - Evaluation & Observability]] and [[04 - Eval Harness — promptfoo]] have been edited directly with the expansion; this note records what changed and why, it doesn't hold the only copy of the plan.
**What actually landed:**
1. [[04 - Eval Harness — promptfoo]] now has a concrete `grounding.yaml` starter set — 7 example cases (BOOM, CausalOps, TradingView, Jarvis as positive-grounding; unsupported AWS cert / production ML deployment / FAANG employment as refusal cases) drawn from real vault project names, following the exact assertion shape already established in that file.
2. [[07 - Evaluation & Observability]] now states the eval set is ~45-55 cases total (up from 15-20), with the grounding category specifically gated on an aggregate **0.8 faithfulness threshold** rather than zero-tolerance per case.
3. The starter set is not yet the full 30-50 — it's drawn from project names already known in this vault, not the live Sanity CMS content. **Genuinely still open:** pulling every actual resume bullet and skill claim directly from Sanity (per [[Web Ingestion Implementation#Agent-Ready Infrastructure (AEO + MCP) - BUILD|the AEO pass's confirmed chatbot architecture]]) to extend the starter set to full coverage — this requires access to the live portfolio codebase/CMS, which this vault-editing pass doesn't have.
## Failure Modes
> [!WARNING]
> Building a parallel deepeval pipeline instead of expanding `grounding.yaml` creates two GitHub Actions checks judging the same chatbot with different pass/fail logic — the next person to touch Orby won't know which one is authoritative. There should be exactly one eval gate.
> [!WARNING]
> A golden dataset that goes stale when portfolio content changes (new project added, resume updated) is worse than no dataset — it'll pass tests against facts that no longer exist. Regenerate the grounding cases whenever Sanity content changes materially, not just once.
## Evidence
- [[04 - Orby Integration]] — the chatbot this eval layer covers
- [[07 - Evaluation & Observability]] — the existing eval design this note extends, not replaces
- [[04 - Eval Harness — promptfoo]] — the concrete YAML/CI wiring already specified
- [[00_Execution]] — the verdict this note corrects on tool choice while keeping the underlying build decision intact

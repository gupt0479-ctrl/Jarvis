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
next: "Write 30-50 grounding.yaml cases from real Sanity portfolio content, one per project/skill/resume claim"
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
## The Genuinely Missing Piece
`07`'s eval set is currently **15-20 cases**, and only two of them (`Grounding / refusal` and `Grounded positive`) test factual faithfulness — whether Orby's answers about Anant's actual work are true. BASWE's original ask (30-50 hand-built golden Q&A pairs from portfolio materials, faithfulness-threshold gated) is a real, additive expansion of exactly that one category — not a second tool, a bigger `eval/cases/grounding.yaml`.
**Concrete build steps:**
1. Pull every factual claim Orby can be asked about from the real portfolio content source (Sanity documents backing `api/chat/route.ts`, per [[Web Ingestion Implementation#Agent-Ready Infrastructure (AEO + MCP) - BUILD|the AEO pass's confirmed chatbot architecture]]) — every project, every resume bullet, every named skill and tool.
2. For each fact, write one **positive grounding case** ("Tell me about his BOOM project" → must reference the real Kafka/Redis/MongoDB stack, must not invent unlisted tech) and, where a plausible-but-false claim exists, one **negative/refusal case** ("Has Anant used [tool not in his record]?" → must refuse, matching the existing pattern in `04 - Eval Harness — promptfoo`'s Kubernetes example).
3. Target 30-50 total cases — BASWE's number — split roughly evenly between positive grounding and refusal, covering every project folder under `20_Progress/Projects/CS/` that the portfolio actually surfaces.
4. Add these as `contains-json` / `javascript` / targeted `llm-rubric` assertions in `eval/cases/grounding.yaml`, following the exact YAML shape already established in [[04 - Eval Harness — promptfoo]] — don't introduce a new assertion syntax.
5. Wire a faithfulness threshold into the existing CI gate: fail the build if fewer than a set percentage of grounding cases pass (BASWE's own framing: >0.8 faithfulness to merge), not just "any case fails."
6. Run this against a resume/portfolio-content update the same way any other prompt or model change triggers a re-run per [[07 - Evaluation & Observability]]'s "minimum before launch" checklist.
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

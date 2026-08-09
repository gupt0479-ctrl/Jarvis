---
type: project
status: paused
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Code Review & Eval Gap]]"
tags:
  - "#progress"
  - "#ai"
next: "Deferred — pick up scoping which task to distill once the new laptop arrives next month"
---
# Model Distillation
## Why This Exists
[[PDF's Ingestion Implementation#Model Distillation: Distill 70B into 3B for Task-Specific Offline Inference - BUILD|PDF's Ingestion Implementation's Model Distillation section]] specs a 70B-teacher → 3B-student pipeline (distilabel for data generation, Unsloth + LoRA for fine-tuning, Ollama for offline deployment), ~$11.50 per distilled model. [[00_Execution]] deferred this to the new laptop, next month — this note records that deferred state honestly rather than resolving the open question prematurely.
## Current State
**Deferred, not started.** The pipeline itself (three steps: generate training data, fine-tune with Unsloth, deploy to Ollama) is fully specified in the source PDF and doesn't need re-deriving when this resumes. What's genuinely unresolved is **which task to distill** — the source PDF's own "Recommended Starting Point" leans trading but says explicitly it needs more scoping first. Don't pick for it here.
## The Four Candidate Tasks (Recorded, Not Decided)
1. **Trading-specific model** — predict market direction from news/sentiment/technicals; train on the trading bot's research→prediction pipeline outputs; deploy for fast offline market analysis. Open question: would a distilled 3B sentiment classifier beat Kronos for speed, or is it orthogonal to Kronos entirely?
2. **Jarvis skill distillation** — distill a specific repetitive Jarvis workflow (e.g. `/challenge` pressure-testing or `/ideas` generation) so it runs offline without API cost. Open question: which Jarvis skill is repetitive enough to justify the $11.50 + 90-minute build?
3. **Portfolio/Orby distillation** — extract structured info from resume/projects/experience for the AI Lab agent, reducing API calls and improving recruiter-interaction privacy. Open question: redundant with deepeval/GPT-4o-vision, or complementary to the promptfoo eval gate already built for Orby (see [[10 - Orby Golden Eval Dataset (Grounding Cases)]])?
4. **Repetitive task extraction** — JSON extraction from unstructured documents (financial reports, research summaries) for BOOM alert enrichment, trading research, or Jarvis ingestion. Open question: which of those three ingestion pipelines would benefit most?
## Why Trading Is the Named Lean (Not a Decision)
The source PDF's own reasoning: the trading bot needs fast, repetitive sentiment/direction classification; a distilled 3B runs offline (useful for a Bangalore trip with spotty internet); cost is negligible against trading upside; it pairs with the existing Kronos time-series model. This is a lean, explicitly flagged as needing more scoping — not a commitment.
## Red Flags To Remember When This Resumes
- **EOS token discipline** — the chat template must place the model's end-of-sequence token between training examples, or context leaks across examples and the model hallucinates. Verify before the 90-minute fine-tune run, not after.
- **Always dry-run first** (`pipeline.dry_run()`) — a misconfigured full run of 3,000 examples costs ~$7 for unusable data.
- **No eval story in the source PDF** — build a held-out test set (10%) and a task-specific metric (Brier score for probability tasks) before trusting the distilled model matches the 70B teacher.
- **Quantization tradeoff** — Q4_K_M GGUF is the safe default; step up to Q5_K_M or F16 if the 3B undershoots on the chosen task.
## Next Action
None until the new laptop arrives. When it does: pick one task from the four above (not all — the source PDF's own framing is "a narrow task, not all of Jarvis or all of trading"), collect 100-200 seed examples, and start with `distilabel`'s dry-run.
## Evidence
- [[PDF's Ingestion Implementation#Model Distillation: Distill 70B into 3B for Task-Specific Offline Inference - BUILD|Model Distillation]] — the full three-step pipeline spec
- [[Code Review & Eval Gap]] — where a local LLM-as-judge (built on this distilled model) is deferred to once this exists
- [[00_Execution]] — the resolved verdict this note executes without prematurely resolving the task-selection question

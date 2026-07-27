---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[Claude Code Free with Ollama (PDF)]]"
  - "[[ML Fundamentals (2033 + 2230)]]"
source_url: 60_Claude/05_Clippings/PDFs/Clone Setup Guide (June 2026).pdf
source_note: "[[Clone Setup Guide (June 2026).pdf]]"
input_kind: pdf
track: ai
---
# Clone — Distill a 70B into a 3B (Local, Offline, ~$12) — Summary
**Source:** `60_Claude/05_Clippings/PDFs/Clone Setup Guide (June 2026).pdf` (@keshavsuki)
**Ingested:** 2026-07-04
**Pages:** 6
## Source
A build guide for **task-specific model distillation**: use a 70B teacher (Together AI) to generate synthetic training data, filter it, LoRA-fine-tune a 3B student (Unsloth), and run it offline in Ollama — total build cost ~$12, running cost $0.
## Key Claims
- ==A small model is dumb alone but can learn a *narrow task* from a big one: the 70B generates thousands of perfect labeled examples, the 3B trains on them, and the 3B replicates the 70B's behavior on that one task without the 70B's weights==
- The result runs locally at **~60 tokens/sec on an Apple-Silicon MacBook, no internet, no API key, nothing leaving the machine** — the real unlock for health/legal/finance clients where data can't leave the building
- **The four tools:** Together AI (70B teacher API), distilabel (synthetic-data pipeline + judge), Unsloth (2× faster LoRA fine-tune, exports GGUF), Ollama (local inference)
- **Always dry-run first** — distilabel validates the pipeline DAG for free before any billable API calls; a misconfigured full run of 3,000 examples costs ~$7 and produces unusable data
- **The EOS token between examples is critical** — without the model's end-of-sequence token (e.g. `<|eot_id|>`), examples leak context into each other and the model hallucinates at inference; Unsloth's SFTTrainer handles it if the correct chat template is applied (verify before training)
> [!NOTE] The guide self-corrects two script errors: Together AI's "$3.3B" was the Feb-2025 Series B (reported raising $1B at $7.5B by May 2026); distilabel's "3.2K stars" is unconfirmed. Honest sourcing.
## Full Content — the three steps
1. **Generate training data (distilabel).** Build a `Pipeline` with a `TogetherLLM` teacher (`Meta-Llama-3.1-70B-Instruct-Turbo`): `LoadDataFromHub` (100–200 raw seed examples) → `TextGeneration` (system prompt defines the task, e.g. extract structured JSON from a medical note, 3 generations each) → `UltraFeedback` judge (same 70B scores them) → `KeepColumns`. `pipeline.dry_run(...)` validates free; `pipeline.run(...)` then `push_to_hub`.
2. **Fine-tune (Unsloth).** `FastLanguageModel.from_pretrained('Llama-3.2-3B-Instruct', load_in_4bit=True)` → add LoRA adapters (`r=16`, target `q/k/v/o_proj`, alpha 16) → `SFTTrainer` (batch 4, grad-accum 4, 3 epochs, lr 2e-4) → `save_pretrained_gguf(quantization_method='q4_k_m')`. ~90 min on one A100 (Colab/RunPod) for 3,000 examples. 2× faster / 60–70% less VRAM than standard HF training.
3. **Deploy (Ollama).** Write a `Modelfile` (`FROM ./…unsloth.Q4_K_M.gguf`, `temperature 0.1`, system prompt) → `ollama create` → run, or call the OpenAI-compatible `http://localhost:11434/api/generate` endpoint. The Modelfile's `FROM` filename must match Unsloth's exact GGUF output name.
**Cost breakdown:** generate 3,000 examples (~5M tokens ≈ $4.40) + judge/filter (~3M ≈ $2.64) + A100 fine-tune (~90 min ≈ $4.50) = **~$11.50**. The PDF also includes a paste-into-Claude-Code prompt that scaffolds all three scripts, asks for keys first, and runs the dry-run before spending.
## Why It Matters
This is the cleanest end-to-end example of the **frozen-teacher → cheap-student** pattern that shows up across the ingested pile (the TRIBE v2 paper's frozen-encoder approach, the AI/ML pivot guide's LoRA fine-tuning project, the AI Engineer roadmap's fine-tuning section) — and it's a realistic Bangalore-flagship-scale build: a deployed, evaluated, task-specific model for ~$12 is exactly the "3 deployed projects" bar with a strong cost/privacy story. It pairs with [[Claude Code Free with Ollama (PDF)]] (same Ollama local-inference layer) and the [[ML Fundamentals (2033 + 2230)]] track (LoRA/gradient-descent are the math being applied). The dry-run-before-spending and EOS-token discipline are the kind of concrete gotchas that make a portfolio project sound like real engineering in an interview.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/Clone Setup Guide (June 2026).pdf`
- [[Claude Code Free with Ollama (PDF)]] — the same Ollama local-serving layer
- [[ML Fundamentals (2033 + 2230)]] — LoRA/fine-tuning math
- [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] — lists a LoRA fine-tuning project as a portfolio piece
## Open Questions
- [ ] Is a task-specific distilled 3B a viable Bangalore flagship (deployed + evaluated + $12 cost story), and what narrow task?
- [ ] What's the eval story — how do you measure the 3B actually matches the 70B on the task (RankIC-style held-out set)?
- [ ] Does the free Together AI / Colab tier cover a first build without real spend?
## Flashcards
#cards/ai
What is task-specific distillation, in one sentence?::Use a **large teacher model to generate thousands of labeled examples** for a narrow task, then fine-tune a **small student** on them so it replicates the teacher's behavior on that task — without the teacher's weights.
What are the four tools in the Clone pipeline and their roles?::**Together AI** (70B teacher API), **distilabel** (synthetic-data pipeline + judge), **Unsloth** (2× faster LoRA fine-tune → GGUF), **Ollama** (offline local inference).
Why dry-run the distilabel pipeline first?::It **validates the DAG and column declarations for free** before any billable API calls — a misconfigured full run of 3,000 examples costs ~$7 and yields unusable data.
Why is the EOS token between training examples critical?::Without the model's end-of-sequence token, examples **leak context into each other** and the model hallucinates at inference; Unsloth handles it only if the correct chat template is applied.

---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - local-models
  - inference
source_url: https://github.com/lyogavin/airllm
notes:
  - "[[40_Resources/CS/Repos]]"
---
# AirLLM

**GitHub:** [lyogavin/airllm](https://github.com/lyogavin/airllm) | **Stars:** 21.7k | **Updated:** Sep 2024 (core); README Jun 2026

## What it is
Streams 70B LLM layers one-at-a-time from disk to VRAM during inference, so you never need to fit the full model in memory — 70B runs on 4GB GPU, 405B Llama3.1 on 8GB VRAM, no quantization required by default.

## How Anant uses it
**Verdict: Conditional — different use case than Jan.** Jan (llama.cpp + GGUF) is for interactive chat. AirLLM is for running very large models programmatically from Python when you need a 70B+ model and only have a mid-tier GPU. If you want to call a 70B from Python code in the trading project or a Jarvis skill, airllm makes that feasible without needing quantization. For general chat use, Jan stays superior.

## How to install / run it (Windows)
```bash
pip install airllm
```
Then in Python:
```python
from airllm import AutoModel
model = AutoModel.from_pretrained("garage-bAInd/Platypus2-70B-instruct")
```
The model is downloaded from HuggingFace and split into layers on first run — requires significant disk space (70B ≈ 140GB). CUDA required (Windows CUDA works). Optional 4bit/8bit compression with `bitsandbytes`: speeds up 3x with minimal accuracy loss.

## Caveats / current state
- Core code last updated Sep 2024; not stale but not actively developed either
- Downloads models from HuggingFace — gated models need `hf_token` param
- First run decomposes the model into layer shards: slow and disk-heavy
- **Useful for running local models beyond Jan's sweet spot?** Yes, specifically for 70B+ models where GGUF quantization would degrade quality. If you have a 4–8GB GPU and want 70B model quality without quantization, this is the only real option short of buying more VRAM. Jan tops out practically around 13B–30B GGUF on consumer hardware.
- CPU inference supported as of v2.10.1 (NavodPeiris contribution), but much slower
- License: Apache-2.0

## Connects to
[[40_Resources/CS/Repos]]

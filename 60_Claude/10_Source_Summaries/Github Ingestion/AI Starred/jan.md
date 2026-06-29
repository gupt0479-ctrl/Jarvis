---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ai
  - local
  - llm
source_url: https://github.com/janhq/jan
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Jan

**GitHub:** [janhq/jan](https://github.com/janhq/jan) | **Stars:** 43.3k | **Updated:** active (Jun 2026)

## What it is
Fully offline, open-source ChatGPT alternative for desktop (Windows/Mac/Linux). Tauri-based app with LlamaCPP under the hood. Download models from the in-app Hub (GGUF format), run inference entirely locally — no network call after model download. Also supports remote API endpoints (OpenAI, Anthropic, etc.) as an alternative backend, making it a unified local+cloud chat client.

Key properties: no data leaves the machine by default, runs without internet after setup, supports model switching, has a clean UI.

## How Anant uses it
Primary use case: run a capable local model (Llama 3.3 70B Q4 or similar) for tasks where sending data to Claude/GPT is undesirable — working with proprietary trading signals, API keys in context, or anything Anant doesn't want going to Anthropic's servers. Also useful when the Claude Max session limit hits and work needs to continue.

Secondary use case: test whether a particular GGUF model is worth using before integrating it into a Python pipeline via LlamaCPP or llama.cpp directly.

## How to install / run it (Windows)
Download installer from jan.ai. The app handles model downloads internally — select a model in the Hub tab and Jan downloads + sets it up. No CLI needed for basic use. For hardware sizing, use [[60_Claude/10_Source_Summaries/Github Ingestion/AI Starred/llmfit]] first to find what fits.

## Caveats / current state
Active (43.3k stars, regular releases, 68 active branches). LlamaCPP performance on CPU-only Windows can be slow for 13B+ models — GPU acceleration requires CUDA or Vulkan setup. The Tauri-based app has had occasional Windows-specific bugs. The remote API mode (using Jan as a ChatGPT/Claude frontend) is useful but defeats the "offline" purpose. VRAM limits are the main constraint: 8GB VRAM comfortably runs 8B models at Q4, 13B at Q3.

**Verdict: yes** — install as the local inference layer. Use when data privacy matters or when cloud session limits hit.

## Connects to
- [[40_Resources/CS/Repos]]
- [[60_Claude/10_Source_Summaries/Github Ingestion/AI Starred/llmfit]]

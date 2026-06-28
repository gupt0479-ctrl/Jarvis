---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - claude
  - ml-research
  - agents
source_url: https://github.com/karpathy/autoresearch
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Autoresearch (Karpathy)

**GitHub:** [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | **Stars:** 88.9k | **Updated:** Mar 2026

## What it is
Gives Claude Code (or any LLM) a single-GPU LLM training loop and lets it iterate autonomously overnight: the agent edits `train.py`, trains for a fixed 5-minute window, checks `val_bpb`, keeps or discards the change, and repeats ~100 times while you sleep. It's a tool for ML researchers to let AI search neural architecture and hyperparameter space.

## How Anant uses it
**Verdict: Not applicable to Jarvis or trading — this is ML training research tooling.**

"By Karpathy, needs to be used" — but it's domain-specific. autoresearch is specifically for iterating on LLM pretraining code (based on his nanochat GPT implementation). It requires a single NVIDIA GPU and Python training code. It is NOT a general automated research agent for:
- Reading and summarizing papers
- Answering questions
- Trading research
- Knowledge management

If you later work on ML training research (e.g., for a course project or internship), this is worth revisiting. For now, it's a fascinating concept to understand (AI that runs its own experiments) but has no direct Jarvis or trading application.

## How to install / run it (Windows)
There's a Windows fork: [jsegov/autoresearch-win-rtx](https://github.com/jsegov/autoresearch-win-rtx). Main repo targets H100/Linux:
```bash
# Requires uv
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run prepare.py   # one-time data prep
uv run train.py     # manual test run
# Then point Claude Code at program.md and let it go
```

## Caveats / current state
- 88.9k stars (viral due to Karpathy's reputation, not production maturity)
- Last meaningful commit Mar 2026; 3 months old
- MIT license
- **Production-ready?** Yes, for its specific use case (LLM training on H100). The scope is narrow by design — one GPU, one file (`train.py`), one metric (`val_bpb`).
- **Is there something better?** For ML research automation: ASI-Evolve does the same thing with more structure. For general research: `/last30days`, web search, Claude. autoresearch's value is the simplicity of the concept, not the generality.

## Connects to
[[40_Resources/CS/Repos]]

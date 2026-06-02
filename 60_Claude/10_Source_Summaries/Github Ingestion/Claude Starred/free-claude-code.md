---
type: input
status: seed
created: 2026-05-28
tags:
  - github
  - claude
source_url: https://github.com/Alishahryar1/free-claude-code
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Free Claude Code

**What it is:** A Python proxy server that intercepts Claude Code's Anthropic API calls and reroutes them to NVIDIA NIM (40 req/min free), OpenRouter, DeepSeek, LM Studio, or llama.cpp — letting you use Claude Code's interface with non-Anthropic models at no cost.

**Why it's here:** Useful for running Claude Code sessions at scale without burning API credits, or for testing with open models locally.

**Why it's not a priority:** If Anant already has an Anthropic API key, the main value proposition (zero cost) disappears. The models available via free tiers (GLM, Kimi, step-3.5-flash) are meaningfully weaker than Claude for complex agentic tasks. The proxy adds a layer of latency and a configuration maintenance burden. Save this for situations where the API budget is exhausted or for running bulk experiments that don't need full Claude quality.

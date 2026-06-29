---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ai
  - reference
  - llm
source_url: https://github.com/cheahjs/free-llm-api-resources
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Free LLM API Resources

**GitHub:** [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | **Stars:** 24.3k | **Updated:** Jun 23 2026 (auto-updated via bot)

## What it is
Curated, frequently-updated list of legitimate free/trial LLM API access. Two categories: **Free Providers** (no payment required) and **Providers with trial credits** (one-time free credits). Deliberately excludes services that reverse-engineer existing chatbots.

**Free tier highlights (as of Jun 2026):**
- **OpenRouter** — 20 req/min, 50 req/day (1,000/day with $10 lifetime topup). Models: Llama 3.3 70B, Qwen3-Coder, GPT-OSS 120B/20B, Gemma 4 31B, and more
- **Google AI Studio** — Gemini 3.5 Flash (20 req/day), Gemma 3 27B (14,400 req/day), multiple variants
- **Groq** — Llama 3.3 70B (1,000 req/day), Llama 3.1 8B (14,400 req/day), Qwen3-32B; fast inference
- **Cerebras** — GPT-OSS 120B and Llama 3.1 8B at 14,400 req/day, 1M tokens/day
- **GitHub Models** — GPT-5, GPT-4.1, o4-mini, DeepSeek R1, Llama 4; rate limits depend on Copilot tier
- **Cloudflare Workers AI** — 10,000 neurons/day; Llama, Qwen, DeepSeek variants
- **HuggingFace Inference Providers** — $0.10/month free credit; models <10GB

**Trial credits (one-time):**
- Baseten ($30), NLP Cloud ($15 + phone verification), AI21 ($10/3mo), Upstage ($10/3mo), Modal ($5/mo → $30 with payment method), SambaNova ($5/3mo), Scaleway (1M tokens), Nebius/Hyperbolic/Fireworks ($1 each)

## How Anant uses it
When the trading project or Jarvis needs a cheap/free model inference call for a non-critical task (summarization, classification, quick reasoning), check this list before spinning up a paid API call. Groq free tier is good for fast Llama 3.3 70B calls. Google AI Studio works for Gemini calls during prototyping (before the trading system has a budget). GitHub Models is useful for quick Claude/GPT access if you have Copilot Pro.

Reference this when evaluating whether to use self-hosted inference (jan, llmfit) vs. free cloud API.

## How to install / run it (Windows)
No install — it's a README. The repo auto-updates via GitHub Actions weekly.

## Caveats / current state
Bot-maintained (auto-PR to update README when model lists change). Some providers go offline or change limits without notice. The "free" tiers at OpenRouter/Google/Groq are real but insufficient for high-frequency production use. Providers with trial credits expire — check dates before relying on them. Excludes unofficial proxies for policy reasons.

**Verdict: yes** — bookmark and check when starting a new project that needs LLM inference on a zero-budget prototype.

## Connects to
- [[40_Resources/CS/Repos]]

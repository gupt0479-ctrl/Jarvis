---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - ai-research
  - agents
source_url: https://github.com/GAIR-NLP/ASI-Evolve
notes:
  - "[[40_Resources/CS/Repos]]"
---
# ASI-Evolve

**GitHub:** [GAIR-NLP/ASI-Evolve](https://github.com/GAIR-NLP/ASI-Evolve) | **Stars:** 781 | **Updated:** Apr 2026

## What it is
GAIR-NLP (SJTU) agentic research framework: three agents (Researcher, Engineer, Analyzer) run a closed loop of hypothesis → code → experiment → lesson, iterating autonomously. It proved +0.97 pts on neural architecture search, +18 pts MMLU on data curation, +12.5 pts on RL algorithm design vs GRPO — all from autonomous overnight runs.

## How Anant uses it
**Verdict: Both paper AND tool, but primarily useful as research reading now.** The `skills/evolve` subdirectory contains a Claude Code skill you can install for a lightweight version. The full pipeline requires:
1. A problem where "better code = better outcome" and a measurable eval script
2. An LLM API (OpenAI-compatible, so Claude via proxy works)
3. A domain you can define with an initial program + evaluation function

For the trading project: theoretically you could point ASI-Evolve at a backtesting evaluator and let it search for better signal-processing algorithms. Practically, the trading codebase isn't yet structured as a clean input/evaluator pair. File this as something to revisit when TradingAgents has a working backtester.

## How to install / run it (Windows)
```bash
git clone https://github.com/GAIR-NLP/ASI-Evolve.git
cd ASI-Evolve
pip install -r requirements.txt  # Python 3.10+
# Set API key in experiments/<name>/config.yaml
python main.py --experiment circle_packing_demo --steps 10 --sample-n 3 --eval-script /path/to/eval.sh
```
Requires bash on PATH for eval scripts — use WSL2 on Windows or adapt eval.sh to PowerShell. OpenAI-compatible API endpoint required.

**Quick Claude Code skill install:**
Copy `skills/evolve/` into `.claude/skills/` and register it.

## Caveats / current state
- Paper published Mar 2026 (arxiv 2603.29640), code updated Apr 2026 — recent and real
- Apache-2.0 license
- 781 stars (small, academic repo — not production-grade tooling)
- The "Skill" version trades depth for convenience: less controlled than full pipeline
- **Best for research?** Yes — read the paper for ideas on multi-agent research loops. The actual tool is genuinely useful if you have a well-defined optimization problem with an evaluator script. Not a general "do research for me" agent; it's an algorithm search engine.
- Anything better? ASI-Evolve's niche (autonomous algorithm search) is unique. For general deep research, `/last30days` or Karpathy's approach of giving Claude Code a bounded problem is more practical.

## Connects to
[[40_Resources/CS/Repos]]

---
type: input
status: sprout
created: 2026-05-29
tags:
  - github
  - trading
  - multi-agent
  - finance
  - llm
notes:
  - "[[40_Resources/CS/Repos]]"
---
# TradingAgents — TauricResearch

**Repo:** https://github.com/TauricResearch/TradingAgents
**Stars:** 80,510 | **Language:** Python | **License:** Apache 2.0
**Paper:** https://arxiv.org/pdf/2412.20138

## What It Is

Multi-agent LLM framework for financial trading. Each agent is a specialist (analyst, researcher, trader, risk manager) and they coordinate through a structured communication protocol. Research-grade but buildable.

## Agent Architecture

- **Analyst agents**: process market data, news, filings
- **Researcher agents**: synthesize and form theses
- **Trader agents**: make execution decisions
- **Risk manager agents**: veto or modify orders

This mirrors a real trading firm's org structure, which is the key insight: LLM agents map well to analyst/PM/risk roles.

## Why It's Relevant

Directly relevant to trading/finance system building goals. Shows how to structure a multi-agent financial system with clear separation of concerns. The paper provides the theoretical grounding; the code provides the implementation reference.

## What to Extract

1. The agent communication pattern (structured, role-based)
2. How they handle uncertainty / confidence levels in financial decisions
3. Their backtesting and evaluation framework

## Related

- [[40_Resources/CS/Repos]] (AI section)
- [[Kronos]] — foundation model for financial markets language
- [[anthropics-financial-services]] — Anthropic's official finance agent demos

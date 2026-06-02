---
type: input
status: sprout
created: 2026-05-29
tags:
  - github
  - swarm-intelligence
  - financial-forecasting
  - prediction
  - python
notes:
  - "[[40_Resources/CS/Repos]]"
---
# MiroFish

**Repo:** https://github.com/666ghj/MiroFish
**Stars:** 63,070 | **Language:** Python | **License:** AGPL-3.0

## What It Is

Swarm intelligence engine for prediction. "Predicting anything" via a multi-agent simulation where LLM agents act as a swarm — each agent has a view, they interact, consensus emerges. Applies to financial forecasting, public opinion analysis, social prediction.

## Core Mechanism

- Multi-agent simulation: N agents, each with partial information
- Knowledge graph to maintain agent memory and relationships
- Agents vote/debate → ensemble prediction
- Works on financial data, social media trends, any temporal series

## Why It's Interesting

The swarm approach to prediction is architecturally different from single-model forecasting. Instead of one model making a prediction, you get emergent consensus from many interacting agents. This mirrors how real markets work (distributed information → price discovery).

## Caveats

- AGPL-3.0 = licensing restriction for commercial use
- 63K stars but relatively new (Nov 2025); verify stability
- "Predicting anything" is a strong claim; check benchmarks

## Related

- [[40_Resources/CS/Repos]] (AI section)
- [[TradingAgents]] — structured agent approach to trading
- [[Kronos]] — foundation model for financial markets language

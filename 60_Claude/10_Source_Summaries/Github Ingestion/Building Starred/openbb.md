---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - finance
  - python
  - trading
source_url: https://github.com/OpenBB-finance/OpenBB
notes:
  - "[[40_Resources/CS/Repos]]"
---
# OpenBB

**GitHub:** [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | **Updated:** actively maintained

## What it is
Open-source financial data platform for analysts, quants, and AI agents. Covers equities, options, crypto, forex, macroeconomic data, and alternative data through a unified Python SDK. Works as a CLI terminal or a Python library. Connects to ~100 data providers (Yahoo Finance, Polygon.io, FRED, Intrinio, Tiingo, etc.) via a standardized interface — switch providers without rewriting data access code.

Two main surfaces:
- **OpenBB Platform** (Python SDK) — `pip install openbb`; call `obb.equity.price.historical("AAPL")` regardless of which provider is configured
- **OpenBB Hub** — cloud-based dashboards and sharing (optional, account required)

Built-in AI/agent integration: the platform exposes tools that LLM agents can call directly for financial data retrieval.

## How Anant uses it
Primary data layer for the trading project. Instead of hardcoding Yahoo Finance calls and rewriting when the API changes, OpenBB's abstraction layer means provider switches are config changes. The LLM agent integration means TradingAgents can call `obb.equity.price.historical` directly without custom tool wrappers.

Key workflow: use the Python SDK in the TradingView financial AI pipeline for market data ingestion → pass to analysis agents → output to Polymarket or TradingView dashboards.

## How to install / run it (Windows)
```bash
pip install openbb

# or with extras for specific providers
pip install "openbb[all]"  # installs all provider packages

# Basic usage:
from openbb import obb
data = obb.equity.price.historical("AAPL", provider="yfinance")
```
OpenBB Hub account is optional — the Python SDK works fully offline (with free data providers).

## Caveats / current state
Actively maintained. AGPL-3.0 license — commercial use requires checking compatibility. Not all data providers are free: Polygon, Intrinio, and alternatives data require paid API keys. The "OpenBB" terminal (the old CLI) was deprecated in favor of the Python SDK as the primary interface. The Hub/cloud features are separate from the SDK and require an account. For the trading project, Yahoo Finance + FRED + crypto providers cover most needs at zero cost.

**Verdict: yes** — use as the data abstraction layer for the trading project. Prevents provider lock-in and has native agent integration.

## Connects to
- [[40_Resources/CS/Repos]]

---
type: input
status: sprout
created: 2026-06-21
updated: 2026-06-21
tags:
  - summary
  - github
notes:
  - "[[40_Resources/CS/Repos]]"
input_kind: github
track: trading
source_url: https://github.com/tradesdontlie/tradingview-mcp
---
# tradingview-mcp

**Repo:** `https://github.com/tradesdontlie/tradingview-mcp`
**Stars:** 3,781 | **Forks:** 1,861 | **Language:** JavaScript | **Last push:** 2026-04-04

## What It Is

An MCP server bridging Claude Code to a locally running TradingView Desktop app via the Chrome DevTools Protocol (CDP) — the same standard Electron debug interface used by VS Code, Slack, and Discord — for AI-assisted chart analysis, Pine Script development, and workflow automation.

## Core Capabilities

- Reads and controls the already-running TradingView Desktop instance through CDP; does not connect to TradingView's servers or APIs directly
- Requires a valid TradingView subscription and the Desktop app already installed and running
- All data processing happens locally — nothing is transmitted or stored externally by this tool
- Explicitly framed as a research project studying how LLM agents interact with stateful desktop financial applications (latency, context limits, ambiguous UI state, Pine Script interpretation)

## Why It Matters

Directly relevant to the trading project's chart-analysis needs: instead of building a technical-analysis module from scratch, this gives Claude Code a tool call into TradingView's actual chart state.

> [!WARNING]
> This depends on undocumented internal TradingView APIs exposed via the Electron debug port — the README itself flags that these can change or break without notice on any TradingView update, and recommends pinning the Desktop app version if stability matters.

## Use Cases for Jarvis

- Connect to the analyst agent in a TradingAgents-style setup: send a ticker, get Claude's interpretation of the live chart, route that into the broader trading pipeline.
- Requires TradingView Desktop installed locally with the debug port manually enabled (`--remote-debugging-port=9222`) — not a zero-setup install.

## Tradeoffs

- Tied to TradingView Desktop's internal Electron structure; explicitly not guaranteed to keep working across TradingView updates.
- Does not work without an active TradingView subscription — this isn't a free data source, it's an automation layer on top of one you're already paying for.
- Chart interaction only — README is explicit that it does not execute real trades.

## Related

- [[40_Resources/CS/Repos]] (Building section)

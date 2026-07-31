---
type: input
input_kind: ai-conversation
source_app: cowork
source_os: windows
title: "Suggest me some must install plugins for the project"
started_at: 2026-07-08T22:49:31
ended_at: 2026-07-08T22:50:34
exported_at: 2026-07-31T21:03:57
duration_minutes: 1
project: 2026-07
session_id: c630a283-7c33-4ae3-9dd4-47ae7949fc0e
status: raw
turn_count: 2
tools_used:
  ToolSearch: 1
  WebSearch: 3
tokens:
  input: 16
  output: 4043
  cache_creation: 247261
  cache_read: 348595
  total: 599915
cost_usd: 1.099225
model:
  - "claude-sonnet-5"
files_touched: []
tags:
  - input
  - ai-conversation
  - cowork
  - windows
---

# Suggest me some must install plugins for the project

## You

Suggest me some must install plugins for the project TradingView. These plugins are for cursor working with some of the latest models.

## Claude

Here's a practical stack for a "TradingView" project in Cursor, working with latest models.

**Core MCP servers** (Cursor caps at ~40 active tools total, so pick a focused set):

- **TradingView MCP** (LewisWJackson) — connects via Chrome DevTools Protocol to control TradingView directly: write/compile Pine Script, pull live OHLCV data, manage alerts, capture chart screenshots. This has ~81 tools on its own, so disable other unrelated MCPs while using it.
- **PineScript Syntax Checker / PineScript MCP Server** — lighter-weight alternative if you just need Pine Script validation, fixing, and generation without full TradingView control.
- **Context7** — pulls current, version-specific docs into context (useful since Pine Script v6 and TradingView's API change often and models' training data lags).
- **GitHub MCP** — if the strategy code lives in a repo, for PRs/commits/reviews from inside Cursor.
- **Playwright MCP** — for browser automation/testing if you're building anything web-facing around the charts.

**Editor extensions** (Cursor is a VSCode fork, so standard VSCode extensions work too):

- A Pine Script syntax-highlighting extension (search "Pine Script" in the marketplace) — Cursor's AI features don't include native Pine Script awareness, so highlighting alone still helps.
- GitLens or similar git-blame extension if multiple people touch strategy code.
- Error Lens for inline diagnostics.

One practical note: keep active MCP servers to 5–6 max and Cursor rules to 3–5 — more than that causes context overload or silently dropped tool access per multiple 2026 guides.

Sources:
- [TradingView MCP Server Guide (2026)](https://www.mcpgee.com/servers/tradingview-mcp)
- [TradingView Pine Script MCP: Write, Edit and Run Strategies with Claude AI](https://blog.pickmytrade.trade/tradingview-pine-script-mcp-claude-ai/)
- [PineScript Syntax Checker](https://mcpmarket.com/server/pinescript-syntax-checker)
- [Best MCP Servers for Cursor (2026)](https://toolradar.com/blog/best-mcp-servers-cursor)
- [The 15 MCP Servers Worth Wiring Into Claude Code and Cursor (2026)](https://codersera.com/blog/[REDACTED]/)
- [12 Must Have Extensions for Cursor](https://matthewpua.medium.com/[REDACTED])

If this project is actually WSL-based dev work, note this falls outside Cowork's scope per your Jarvis setup — you'd install/configure these directly in Cursor or via Claude Code in WSL, not through this session.

### Tool Calls

- `ToolSearch` -- `{"query":"WebSearch","max_results":3}`
- `WebSearch` -- `{"query":"best Cursor IDE extensions plugins 2026 must install"}`
- `WebSearch` -- `{"query":"Cursor MCP servers latest models 2026 recommended"}`
- `WebSearch` -- `{"query":"Cursor Pine Script TradingView extension MCP"}`

## Actions Taken

**Files created:**
_None_

**Files modified:**
_None_

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
_None_



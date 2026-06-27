---
type: input
status: sprout
created: 2026-06-27
tags:
  - github
  - claude
  - mcp
  - trading
source_url: https://github.com/caiovicentino/polymarket-mcp-server
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Polymarket MCP Server

**GitHub:** [caiovicentino/polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)

Worth installing? for the tradingview product?

- 45-tool MCP for claude desktop via polymarket's CLOB API. setup (~10 min):
	1. git clone the repo
	2. cd polymarket-mcp-server && ./quickstart.sh
	3. start in DEMO mode (no wallet, read-only)
	4. full mode needs a polygon wallet and is not available to US persons under polymarket's ToS
- demo .env: `MAX_ORDER_SIZE_USD=50`, `MAX_TOTAL_EXPOSURE_USD=200`, `REQUIRE_CONFIRMATION_ABOVE_USD=25`
- heads up: v0.1.0 experimental. engineering 
- demo only - stay in demo if you're in the US. not financial advice, not legal advice.

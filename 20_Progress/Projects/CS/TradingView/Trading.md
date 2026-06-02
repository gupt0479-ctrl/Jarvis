awesome here's everything

repo: https://github.com/TauricResearch/TradingAgents

7 AI agents that work like a trading firm - fundamentals, sentiment, news, technical analyst, bull/bear debate, risk manager, trader - all collaborating on buy/sell/hold decisions

setup (~10 min):
1) git clone the repo
2) pip install .
3) add your claude api key to .env
4) tradingagents analyze AAPL --date 2026-01-15

key config: open default_config.py, set backbone to "claude-sonnet-4-6"

heads up: research tool only. backtests don't guarantee live returns. start on paper trading first. this is not financial advice or legal advice.
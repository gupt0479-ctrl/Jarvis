---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - claude
  - skills
source_url: https://github.com/mvanhorn/last30days-skill
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Last30Days Skill

**GitHub:** [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

## What it is
Claude Code agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web — then synthesizes a grounded summary with recency bias (last 30 days). The key function: given a topic, it pulls from multiple real-time sources and returns a synthesized view of current discussion, not just static search results.

## How Anant uses it
Directly applicable to the trading project — when evaluating a stock, sector, or market event, running this skill gives a synthesized view of recent community discussion across Reddit (wallstreetbets, investing), HN, and Polymarket prediction markets in one pass. More targeted than a generic web search because it pulls from discussion platforms rather than just news articles.

Also useful for Jarvis sessions that start with "what's changed in X in the last month" — this skill hits the sources Claude can't natively access.

## How to install / run it (Windows)
Install as a Claude Code skill by copying into `.claude/skills/` or registering via the skills directory. Depends on having relevant search/scraping tools accessible to the agent (Firecrawl or equivalent).

## Caveats / current state
Small/independent repo (mvanhorn). The quality depends on the underlying search provider — if the skill uses web search tools, results are only as good as those sources. Polymarket integration is the most distinctive part; most research tools skip prediction markets. Check the README for exact source list and whether Reddit/X require auth tokens.

**Verdict: yes** — install for trading project research workflow. The Polymarket + Reddit combination is not covered by standard web search skills.

## Connects to
- [[40_Resources/CS/Repos]]

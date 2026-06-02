---
type: input
status: seed
created: 2026-05-28
tags:
  - github
  - claude
source_url: https://github.com/anthropics/financial-services
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Claude for Financial Services (Anthropic)

**What it is:** Anthropic's official reference repo for financial-services Claude deployments — contains Cowork plugins and Managed Agent templates for IB pitch decks, equity research, GL reconciliation, KYC screening, and private equity diligence workflows, with MCP connectors to Bloomberg, Morningstar, FactSet, S&P Global, PitchBook, and others.

**Why it's here:** Directly relevant if BOOM's research involves financial modeling, earnings analysis, or deal tracking — the repo ships actual working agents and skills, not just documentation.

**Why it's not a priority:** The financial-services workflows (DCF/LBO models, LP reporting, NAV tie-out) are targeted at professional finance teams, not CS undergraduate research. If BOOM involves quantitative research that touches public market data, revisit the equity-research vertical specifically — `/earnings`, `/comps`, and `/screen` commands could be useful. Otherwise, the S&P Global and LSEG MCP connectors require paid subscriptions that likely aren't available.

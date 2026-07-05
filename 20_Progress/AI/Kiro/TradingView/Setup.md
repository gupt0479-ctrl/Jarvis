---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - kiro
  - setup
  - tradingview
notes:
  - "[[20_Progress/AI/Kiro/MOC]]"
next: "none — external project dump, single spec captured"
---
# TradingView — Kiro Setup
A copy of one Kiro spec for a beginner-safe AI market research desk project — the Data Ingestion Foundation, a provider-agnostic OHLCV ingestion system (DuckDB storage, Pydantic validation, Typer CLI). Reference material only; the only Kiro capture for this project across all three platforms (Cursor's Trading View folder is empty).
## Files
### Specs (data-ingestion-foundation)
- [[20_Progress/AI/Kiro/TradingView/specs/data-ingestion-foundation/design|specs/data-ingestion-foundation/design]] — local, timestamped, auditable market-data substrate architecture
- [[20_Progress/AI/Kiro/TradingView/specs/data-ingestion-foundation/requirements|specs/data-ingestion-foundation/requirements]] — provider-agnostic OHLCV fetch, DuckDB storage, provenance, freshness, quality reports, read API
- [[20_Progress/AI/Kiro/TradingView/specs/data-ingestion-foundation/tasks|specs/data-ingestion-foundation/tasks]] — bottom-up implementation plan: config/models → storage → providers → normalization → quality → API → CLI
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Kiro/TradingView"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `specs/data-ingestion-foundation/.config.kiro` — Kiro spec metadata.
## Status & Gaps
External project dump, no live equivalent in this vault to diff against — marked `static`. This is the thinnest Kiro capture of the six real projects (one spec, no steering or hooks); compare against [[20_Progress/AI/Cursor/Trading View/Setup|Trading View's Cursor dump]], which is empty.
## Links
[[20_Progress/AI/Kiro/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

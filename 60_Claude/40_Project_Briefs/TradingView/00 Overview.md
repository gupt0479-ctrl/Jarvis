---
type: reference
status: active
created: 2026-06-25
updated: 2026-06-25
tags:
  - trading
  - ai
  - graphify
  - knowledge-graph
source: graphify
source_repo: gupta-builds/TradingView (setup branch)
notes:
  - "[[Trading with Ai]]"
---

# TradingView — graphify Knowledge Graph

This folder is a [graphify](https://github.com/safishamsi/graphify) knowledge graph of the `research_data` / TradingView codebase (`github.com/gupta-builds/TradingView`, `setup` branch), generated 2026-06-25. It maps **everything currently in the repo**: the 27 Python source/test files, `README.md`/`CLAUDE.md`/`Docs/RESEARCH.md`, the full `.kiro/specs/data-ingestion-foundation/` design-first spec (requirements → design → tasks), the new `.claude/` agents and skills, `config/*.toml`, and `Docs/Quant Foundations.pdf` (a personal quant-interview-prep roadmap, included as background context).

This folder contains **only graphify output** — no copies of source code. Everything here is generated from (and cites) the real files in the repo; nothing was invented (see Honesty Rules below).

## How to navigate

- **Communities/** (95 notes) — thematic clusters (e.g. "Data Quality Auditor", "Provider Registry", "Quant Foundations & SEC/EDGAR Reference Docs"). Each has a cohesion score, member list, bridge nodes, and links to neighboring communities. **Start here.**
- **Nodes/** (922 notes) — one atomic note per entity/concept (classes, functions, requirements, design decisions). Linked via `[[wikilinks]]` and tagged `#graphify/code`, `#graphify/document`, `#graphify/rationale`, `#graphify/paper`. 59 notes with garbled/truncated auto-generated names (long docstring fragments) were excluded for readability — their content is still covered inside `GRAPH_REPORT.md` and the relevant Community notes.
- **GRAPH_REPORT.md** — the full raw audit report (every community, full knowledge-gap list).
- **graph.html** — interactive force-directed graph, open directly in any browser.

## Corpus

981 nodes · 1929 edges · 95 communities (40 source files: 27 code, 12 docs/config, 1 PDF) · ~41,200 words · 63% EXTRACTED / 37% INFERRED / 0% AMBIGUOUS edges.

## God Nodes (most-connected core abstractions)

1. `OHLCVRecord` — 132 edges — the canonical price record every other layer depends on
2. `ProviderFetchResult` — 58 edges
3. `PriceAdjustment` — 54 edges
4. `QualityStatus` — 51 edges
5. `_valid_record_kwargs()` — 40 edges (Hypothesis test strategy, heavily reused across property tests)
6. `ProviderConfig` — 35 edges
7. `ProviderCapabilities` — 34 edges
8. `InsufficientDataError` — 33 edges
9. `DataQualityReport` — 32 edges
10. `ProviderRegistry` — 31 edges

## Surprising Connections

- `FinRobot (specialized financial agents)` ↔ `Multi-Agent Research Design` — design.md's research-baseline citation links to RESEARCH.md's actual agent-role table.
- `Evidence Card JSON Shape` ↔ `DataEvidencePacket Model` — RESEARCH.md's example JSON and design.md's Pydantic schema describe the same contract from two angles.
- `Risk Manager Agent` ↔ `data_quality_reports Schema` — the *future* AI risk-manager role and the *already-built* quality-report table are quietly the same enforcement point.
- `Research Desk Data Flow` ↔ `Ingestion Data Flow` — RESEARCH.md's and CLAUDE.md's pipeline diagrams describe the same flow with different vocabulary.
- `Evidence Card Cautious Action Labels` ↔ `Evidence Card Action Labels` — confirms RESEARCH.md and CLAUDE.md haven't drifted on the allowed action vocabulary.

## Hyperedges (group relationships)

- **Ingestion Pipeline Component Chain** — Provider Registry → Provider Fetchers → Raw Payload Writer → Normalizer → Market Calendar → Data Quality Auditor
- **research_data Module Map** — models, config, storage, normalization, calendar, quality, read_api
- **Multi-Agent Research Design Roles** — Technical/Fundamentals/Sentiment Analyst, Bull/Bear Case, Risk Manager, Portfolio Allocation Reviewer, Student Tutor (not yet implemented — this is the planned Month-3 architecture from RESEARCH.md)

## Knowledge gaps the graph surfaced

- 383 isolated/single-connection nodes — mostly individual Hypothesis property-test bodies and numbered Requirement/Property statements. Expected for a spec this granular, but worth a skim if you want to spot under-cross-referenced requirements.
- `Docs/Quant Foundations.pdf` has weak structural links into the rest of the graph (it's background self-study material, not yet wired into the actual strategy-engine plan) — see `quantfoundations_strategy_backtesting_engine` and `quantfoundations_probability_fundamentals` in Nodes/ for the two genuine cross-links that do exist.

## Suggested questions this graph can answer

- Why does `OHLCVRecord` bridge nearly every community (validation, normalization, storage, quality, evidence)?
- Why does `DataQualityAuditor` bridge Data Quality, Market Calendar, and the validation-model communities?
- Why does `MarketCalendar` bridge six different calendar-test communities plus Data Quality?
- Are the 129 INFERRED edges touching `OHLCVRecord` actually correct, or did deep-mode over-infer?

## Querying this graph

From the repo (`/home/anant_gupta/projects/hub/tradingview`):

```bash
graphify query "How does data flow from a provider fetch to the daily_ohlcv table?"
graphify path "ProviderRegistry" "DataQualityAuditor"
graphify explain "DataEvidencePacket"
```

Or via the `graphify-tradingview` MCP server (added alongside this folder) using `query_graph`, `get_node`, `get_neighbors`, `get_community`, `god_nodes`, `graph_stats`, `shortest_path`.

## Keeping this current

Re-run `/graphify --update` in the repo as the codebase evolves (code-only changes skip the LLM entirely), then re-copy the `Communities/`, `Nodes/`, `GRAPH_REPORT.md`, and `graph.html` here. `00 Overview.md` is hand-maintained — update it manually if the corpus changes significantly.

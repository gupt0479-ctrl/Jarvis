---
type: reference
status: active
created: 2026-06-25
updated: 2026-07-12
tags:
  - trading
  - ai
  - graphify
  - knowledge-graph
source: graphify
source_repo: gupta-builds/TradingView (main, post-PR
notes:
  - "[[Fable 5 — Read Order (TradingView folder)]]"
  - "[[20_Progress/Projects/CS/TradingView/Session Findings/Session Findings — AI Brain Hub (2026-07-12)]]"
---

# TradingView — graphify Knowledge Graph

This folder is a [graphify](https://github.com/safishamsi/graphify) knowledge graph of the `research_data` / TradingView codebase (`github.com/gupta-builds/TradingView`), incrementally rebuilt 2026-07-12 (`graphify --update`) on top of the 2026-06-25 baseline and the 2026-07-11 Phase 2 rebuild. This pass folds in **Phase 3 — the AI brain hub** (LLM seam merged to `main` via PR #4, commit `c754f00`): the `cards/` and `agents/` packages, the `Docs/PHASE3_AI_BRAIN_*` design trio, `fable5_run_memory.md`, and every other file that changed since the last graph build (39 code files re-parsed by AST, 15 docs re-extracted semantically; 3 files graphify's own detector stopped seeing this run — `config/assets.toml`, `config/providers.toml`, `tests/test_property_no_secrets.py` — verified still present on disk and *not* pruned from the graph; see Known Issues below).

This folder contains **only graphify output** — no copies of source code. Everything here is generated from (and cites) the real files in the repo; nothing was invented (see Honesty Rules below).

## How to navigate

- **Communities/** (142 notes) — thematic clusters (e.g. "AI Hub Card/Critic Contracts & Branches", "LLM Client Router (C4)", "Data Quality Auditor Checks"). Each has a cohesion score, member list, bridge nodes, and links to neighboring communities. **Start here** — Community 0 is the Phase 3 AI hub itself.
- **Nodes/** (2213 notes) — one atomic note per entity/concept (classes, functions, requirements, design decisions). Linked via `[[wikilinks]]` and tagged `#graphify/code`, `#graphify/document`, `#graphify/rationale`, `#graphify/paper`. 28 notes with garbled/truncated auto-generated names (long docstring fragments cut mid-word) were excluded for readability — their content is still covered inside `GRAPH_REPORT.md` and the relevant Community notes.
- **GRAPH_REPORT.md** — the full raw audit report (every community, full knowledge-gap list).
- **graph.html** — interactive force-directed graph, open directly in any browser.

## Corpus

2241 nodes · 4476 edges · 142 communities (115 shown, 27 thin omitted) · 151 source files (122 code, 28 docs, 1 PDF) · ~103,725 words · 79% EXTRACTED / 21% INFERRED / 0% AMBIGUOUS edges.

## God Nodes (most-connected core abstractions)

1. `OHLCVRecord` — 118 edges — still the canonical price record every layer depends on, now including the AI-hub allowlist/evidence path
2. `BrainStore` — 83 edges — the closed-loop persistence hub; AI hub reads gate runs/decisions through it
3. `ProviderConfig` — 55 edges
4. `_valid_record_kwargs()` — 40 edges (Hypothesis test strategy, heavily reused)
5. `PriceReadAPI` — 37 edges
6. `ProviderRegistry` — 33 edges
7. `normalize_fetch_result()` — 31 edges
8. `DataQualityAuditor` — 31 edges
9. `batch_insert_ohlcv()` — 31 edges
10. `StrategyReturns` — 29 edges

## Phase 3 hyperedges (new this pass)

- **Four-Gate Promotion Harness (OOS → MC → WF → DSR)** — `gate_out_of_sample`, `gate_monte_carlo`, `gate_walk_forward`, `gate_deflated_sharpe`, `gates_harness_gateharness` [EXTRACTED 1.00]
- **Cursor vs Fable Division of Labor** — `role_cursor_owner`, `role_fable_owner`, `branch_feat_phase2b_promotion_study`, `branch_feat_phase3_llm_seam`, `agents_md_working_agreement` [INFERRED 0.85]
- **Phase 3 LLM Seam Live Smoke Flow (NVDA)** — `agents_llmclient_livellmclient`, `cards_models_evidencecard`, `cards_models_criticreview`, `scripts_live_ai_card_smoke`, `symbol_nvda` [EXTRACTED 1.00]

## Surprising connections

- `Requirement 16: Scope Boundaries` ↔ `Guardrail Check Grep Skill` — the ingestion spec's scope-boundary requirement and the `.claude/skills/guardrail-check` grep sweep are the same rule enforced twice, in prose and in code.
- `GateHarness` → three `test_gates.py` cases (`test_harness_rejects_misaligned_benchmark`, `..._runs_all_four_in_order_for_edge`, `..._short_circuits_on_first_failure`) — the harness's fixed-order/short-circuit contract is exercised by name, not just by type.
- `load_config()` → `test_universe_has_fourteen_symbols()` — the package-invariants CI canary calls back into config loading directly, which is why universe-size drift fails fast.

## Knowledge gaps the graph surfaced

- 66 isolated/single-connection nodes (`research-data`, `FinGPT (curated financial data pipelines)`, `Repository Shape`, table-schema doc stubs, etc.) — mostly reference-doc fragments and standalone schema notes; expected, not a defect.
- 27 thin communities (<3 nodes) omitted from `GRAPH_REPORT.md`'s community list — run `graphify query` to explore them individually.
- The `Year-Ahead Base Architecture Contract` ↔ `Data Ingestion Foundation` edge is still tagged AMBIGUOUS (low confidence) — worth a manual look if the two docs' relationship needs to be pinned down precisely.

## Suggested questions this graph can answer

- Why does `OHLCVRecord` bridge nearly every community, now including the AI hub's numeric-allowlist and evidence-ref path?
- Why does `main()` (desk CLI) bridge `Fundamentals Backfill & Study Scripts`, `Citation Ingest CLI`, `BrainStore Decisions & Persistence`, and `Quality-Momentum Strategy Pack`?
- Why does `MarketCalendar` bridge six different calendar-test communities plus `Data Quality Auditor Checks`?
- Are the 919 INFERRED edges (21% of the graph, avg confidence 0.73) touching `OHLCVRecord` and `BrainStore` actually correct, or did deep-mode over-infer on the newly merged AI-hub code?

## Querying this graph

From the repo (`/home/anant_gupta/projects/hub/tradingview`):

```bash
graphify query "How does an EvidenceCard get built from a ScorePacket without ever seeing raw OHLCV?"
graphify path "LiveLLMClient" "CardValidationError"
graphify explain "GateSummaryProjection"
```

Or via the `graphify-tradingview` MCP server using `query_graph`, `get_node`, `get_neighbors`, `get_community`, `god_nodes`, `graph_stats`, `shortest_path`.

## Known issues (this pass)

- Graphify's own file detector stopped scanning `config/assets.toml`, `config/providers.toml`, and `tests/test_property_no_secrets.py` this run (not flagged as `skipped_sensitive` either — they simply weren't returned by `detect_incremental`, likely an ignore-pattern change in the installed `graphify` package, currently 0.9.4 vs the skill's pinned 0.7.10). All three files still exist on disk and were verified before the `--update` merge step, so their existing graph nodes were **not** pruned — but they also won't pick up further edits until this is root-caused. Worth a `graphify` package/skill version sync before the next run.
- Token-cost accounting (`cost.json`) undercounts this run — the one semantic-extraction subagent's real token usage wasn't written back into its chunk file before merging, so this pass's entry shows 0 in / 0 out. Cosmetic only; extraction quality is unaffected.

## Keeping this current

Re-run `/graphify --update` in the repo as the codebase evolves (code-only changes skip the LLM entirely), then re-copy the `Communities/`, `Nodes/`, `GRAPH_REPORT.md`, and `graph.html` here. `00 Overview.md` is hand-maintained — update it manually if the corpus changes significantly.

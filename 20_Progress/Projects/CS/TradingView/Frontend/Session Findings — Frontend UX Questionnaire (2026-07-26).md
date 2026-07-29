---
type: session-recap
status: active
created: 2026-07-26
updated: 2026-07-26
related_progress:
  - "[[Session Findings — AI Brain Hub (2026-07-12)]]"
  - "[[Phase 3 — AI Brain Hub Landed (2026-07-12)]]"
  - "[[Year-Ahead Base — Fable 5 Architecture Contract]]"
  - "[[Fable 5 — Read Order (TradingView folder)]]"
  - "[[Postmortem - Stocks-ETFs First, Prediction Markets Second]]"
tags:
  - trading
  - frontend
  - ui
  - questionnaire
track:
  - trading
  - ui
next: "Cursor writes the V1 Streamlit build from [[Frontend Build Plan — V1 UI Spec]]; review its output against this note and the plan"
---
# Session Findings — Frontend UX Questionnaire (2026-07-26)
> [!WARNING] Partially superseded (2026-07-26, same day)
> This note captures the first pass, run before the user supplied their own detailed round-1/round-2 answers directly in [[QNA for UI]]. That note is now the higher-fidelity source — it overrides the stack choice (Streamlit dropped), the Watchlist/Stock-Detail navigation model, and the Dashboard's top-6 logic described below. Keep this note for the reasoning trail and the vault-terminology grounding, which still hold.
==Full Q&A audit trail for the first frontend/UI planning session on this desk. No UI has existed in code until now — confirmed zero Streamlit/Next.js code in the repo as of Phase 3. Locked decisions SoT going forward: [[QNA for UI]] (round 2 onward), [[Frontend Build Plan — V1 UI Spec]] (pending rewrite).==
## Mission
Cursor (Haiku 4.5) ran a clarifying-question pass to scope the first UI build for the personal stocks/ETFs desk. Claude reviewed the full project history — Canon, Phases, Session Findings, Research, the pre-Canon Product Spec — before answering, since Cursor's questions assumed screen shapes that partially predate the current gate/brain architecture.
## Correction before answering
The only prior UI prose in the vault is the pre-Canon (2026-04-26) Product Spec's 7-screen sketch: dashboard, portfolio tracker, watchlist, stock detail, strategy lab, evidence feed, alerts. It predates `EvidenceCard`/`CriticReview`, the four-gate pipeline, the brain/citation loop, and the paper engine's timed-entry/replay model landed in Phase 2 and Phase 3. Three older Distilled Notes (Hermes Agent, Trading Resources Roadmap, AI-Assisted Trading) describe a rejected autonomous-execution/Kelly-sizing vision, superseded by [[Postmortem - Stocks-ETFs First, Prediction Markets Second]] and the Cursor Alignment Pass. Neither is treated as settled scope here.
## Block A — Navigation
### A1 — Header items
**Answer:** `research_data | Dashboard | Watchlist | Tests | Strategies | My Stocks | Brain-Journal | Bots-Hub | Settings`. No additional top-level section — every CLI surface (`init-db`, `ingest-prices`, `audit-prices`, `benchmark`, `brain propose/approve/reject/decide`, `analyze-symbol`, `critique-spec`) maps onto one of these 8 items; none is orphaned.
### A2 — Watchlist vs Dashboard
**Answer:** Watchlist is its own nav item, not a Dashboard section — full 14-symbol list. Dashboard shows a curated 5.
## Block B — Dashboard
### B1 — "Top 5" logic
**Answer: Hybrid.** A pinned favorites list (user-chosen, stable membership) with an urgency badge computed from `EvidenceCard.confidence` plus non-HOLD action, so the same 5 buttons stay in place but the ones needing attention today stand out.
### B2 — Operational panel contents
**Answer:**
- Ingest/bots status — last run plus ✓/⚠️/✗ per provider (Polygon, Tiingo, FMP, SEC EDGAR, csv_fixture), sourced from `ingestion_runs`.
- Human steps required — count of `StrategySpec.status == proposed` awaiting approval, plus count of paper `Thesis` rows awaiting pre-approval, both linking into filtered Strategies/My Stocks views.
- Paper P&L — total unrealized, today's delta, and vs-VOO using the required `voo_return_same_period` field. Never shown without the VOO comparison.
- Cost tracking — LLM call counts/estimated cost by provider (Gemini Flash primary, Groq, Ollama fallback) from the agents runner. Not subscription/billing chrome — single user, no auth.
### B3 — Refresh
**Answer:** Load plus manual "Refresh" button only. No polling, no websockets — single-user local desk, matches the existing CLI-first interaction model.
## Block C — Watchlist
### C1 — Scope
**Answer:** All 14 symbols from `config/assets.toml` (canonical `BRKB` internally). No ad-hoc "add ticker" search — universe expansion is explicitly gated on RankIC/journal evidence, not a UI feature.
### C2 — Columns
**Answer:** Symbol | Company | Action | Confidence | Data Quality | Last Reviewed | Paper Status (open / closed / none).
### C3 — Click-through
**Answer:** Full-page navigation to `/stock/{SYMBOL}`, not a modal. Too much lives on the detail view — evidence card, critic review, chart, gate status, paper position, journal — for an overlay to hold comfortably.
## Block D — Stock Detail (`/stock/{SYMBOL}`)
### D1 — Confirmed content, all six
1. Header — action badge (never BUY/SELL), capped confidence, `last_reviewed`, `next_review_date`.
2. Price chart — TradingView widget embed with MA20/50/200, RSI-14, Bollinger, ATR. These are the only indicators the system computes; no ad-hoc indicator picker.
3. Factor score panel — `momentum_score`, `safety_score`, `quality_fcf_score`, `valuation` composite, each as rank (1–14) plus raw value plus the `ScorePacket` context string.
4. Evidence Card (full fields: action, confidence, summary, evidence, risks, opposing_evidence, invalidation_conditions, next_review_date, data_quality) with the Critic Review directly beneath it, visually subordinate — the critic can only lower confidence, never raise it, and the layout should not imply otherwise.
5. Gate/spec status — if a `StrategySpec` targets this symbol, an inline mini gate strip (OOS/MC/WF/DSR) linking to its full row on Tests.
6. Paper position plus journal — if a `Thesis` is open or closed on this symbol: entry/exit price and date, P&L vs VOO, `source_card_id` link back to the evidence card that triggered it, and any linked `JournalEntry` lessons.
## Block E — Tests
### E1 — Pipeline view
**Answer:** Fixed-order gate strip OOS → MC → WF → DSR (order is immutable per Canon) with aggregate pass/fail status above a log table.
### E2 — Log granularity
**Answer:** One row per spec's full gate run, not one row per individual gate. Row = spec name, OOS/MC/WF/DSR ✓/✗ inline, overall demo-eligible/failed, date. Click expands to the four numeric fields (`oos_net_sharpe`, `mc_p5_return`, `wf_pct_positive`, `deflated_sharpe_probability`), the linked `JournalEntry`, and the promote/demote decision if one exists.
### E3 — Failure styling
**Answer:** A failed gate is a correct, informative outcome — Phase 2's first OOS failure on thin data was logged as "proof over narrative," not a bug. Style fails neutrally, not as alarm-red errors.
## Block F — Strategies
### F1 — Sections
**Answer:** Filter chips: All | Proposed | Approved/Under test | Demo-eligible/Promoted | Demoted. Default view shows active plus promoted; historical/demoted reachable via filter.
### F2 — Sort
**Answer:** Most recent gate activity — a spec that was just re-tested jumps to the top, matching the "take the one that adjusts" instruction. Proposed-but-untested specs sort by proposal date within their own bucket.
### F3 — Detail view
**Answer:** Full `StrategySpec` params, the `Citation` that proposed it, complete gate history (not just latest run), every promote/demote decision over time, and linked journal entries. Approve/promote/demote actions live here, gated to the human (`anant`) — `validate_human_identity` already blocks `cursor`/`claude`/`fable` from calling these, so a UI approve button is safe only when the acting user is the human.
## Block G — My Stocks (paper trading hub)
### G1 — Contents
**Answer:** Filterable by symbol and by status (open/closed/all). Each position: entry date/price, exit date/price if closed, unrealized/realized P&L, P&L vs VOO, `spec_id`/`source_card_id` links, `review_frequency`/`next_review_date`.
### G2 — Reuse, not duplicate
**Answer:** Clicking a position opens the same Stock Detail page (paper-position section), not a separate detail view — avoids building two versions of the chart/evidence-card UI.
### G3 — Replay vs live
**Answer:** Visually distinguish accelerated historical-replay journals from the live calendar paper book (for example a "Replay" vs "Live" tag) so a backtest-style journal entry is never mistaken for a real time-paced paper trade.
## Block H — Brain-Journal
### H1 — Shape
**Answer:** Card grid of vault notes with visible frontmatter, filterable by symbol/tag/date. Mirrors the existing one-way DB → vault mirror (`data/cards/{SYMBOL}_live_mirror.md`, "DB wins on conflict").
### H2 — Editability
**Answer:** View-only. No inline frontmatter editing in the UI — editing the mirror would fight the DB-wins rule. An "open in Obsidian" link covers real edits.
### H3 — Relationship to Tests-page journal entries
**Answer:** Different surfaces for the same underlying `JournalEntry`/`Citation` rows. Tests shows the gate-run journal entry inline with its spec; Brain-Journal is the full vault-mirror browsing view. Cross-link both directions.
## Block I — Bots-Hub
### I1 — Scope
**Answer:** Status plus manual triggers. Show ingest status, last analyst/critic run per symbol, LLM call/cost counts, and buttons ("Run ingest now," "Run analyst on {symbol}," "Run gate test on {spec}") that call the existing CLI functions directly — no new execution logic.
### I2 — Logs
**Answer:** Collapsed by default, expandable per run, to avoid noise.
### I3 — Boundary
**Answer:** Bots-Hub cannot approve/promote/demote a spec — that stays on Strategies (or the CLI), preserving the human-gate rule.
## Block J — Stack and cross-cutting rules
### J1 — Stack
**Answer:** Streamlit first, Python stays source of truth, reads directly off DuckDB / existing read APIs rather than standing up a separate REST layer. TradingView chart embedded via `st.components.v1.html`. Multipage via `st.navigation`/`pages/`; Stock Detail uses a `?symbol=` query param since Streamlit pages aren't natively parameterized.
### J2 — Non-negotiable UI rules
- Action vocabulary only: `WATCH | HOLD | ACCUMULATE | REDUCE | AVOID | INSUFFICIENT_DATA`. Never BUY/SELL, never "guaranteed"/"risk-free."
- Displayed confidence is always capped by `max_confidence` (data-quality-derived) — never show an unclamped model number.
- Every number on screen must trace to a `ScorePacket`/gate field — no UI-invented stats.
- No auto-trading, no broker execution, no execution controls anywhere.
- No auth/multi-tenant chrome — single local user.
- Review-prompt phrasing only ("Review NVDA because momentum rank dropped"), never command phrasing ("Sell NVDA now").
- Fixed 14-symbol universe, no ad-hoc ticker search in V1.
## Open items for Cursor
- Exact color mapping for the six action states — needs a palette, not specified here.
- Whether "Run gate test on {spec}" from Bots-Hub needs a confirmation dialog before kicking off a potentially long-running gate pipeline.
- Whether Streamlit's native multipage routing is sufficient for the `?symbol=` deep link, or whether it needs a thin custom router.

---
type: project
status: active
created: 2026-07-26
updated: 2026-07-26
related_progress:
  - "[[Session Findings — Frontend UX Questionnaire (2026-07-26)]]"
  - "[[Phase 3 — AI Brain Hub Landed (2026-07-12)]]"
  - "[[Year-Ahead Base — Fable 5 Architecture Contract]]"
  - "[[Math-First Map — Existing Code to Factor Brain]]"
tags:
  - trading
  - frontend
  - ui
  - streamlit
track:
  - trading
  - ui
next: "Cursor builds pages in this order: Watchlist + Stock Detail first (they carry the most shared components), then Dashboard, then Tests/Strategies, then My Stocks/Brain-Journal/Bots-Hub"
---
# Frontend Build Plan — V1 UI Spec
> [!WARNING] Partially superseded (2026-07-26, same day)
> The user's own round-2 QNA answers in [[QNA for UI]] changed real scope after this note was written: Streamlit is dropped entirely, Stock Detail merges into My Stocks (no separate `/stock/{SYMBOL}` page), Watchlist click-through is a modal everywhere (not full-page nav), Dashboard's 5 non-starred slots are dynamic-by-confidence not a static pin list, and the build sequence is now prototype (coded Next.js/React, mock data) → finish backend infra → real production UI, not a single Streamlit V1. The page-by-page content below (data sources, gate/spec logic, non-negotiable rules) is still accurate — treat the **stack, navigation mechanics, and page-merge decisions** as overridden by [[QNA for UI]] until this note gets a full rewrite.
==This is the source-of-truth build spec for the first UI this desk has ever had. Decisions here come from [[Session Findings — Frontend UX Questionnaire (2026-07-26)]]; read that note for the reasoning trail, this note for the page-by-page spec Cursor should build against.==
## Ground rules (apply to every page)
- **Stack:** Streamlit, Python source of truth. Reads directly off DuckDB / existing read APIs (`PriceReadAPI`, brain CLI internals) — no separate REST layer for V1.
- **Nav:** `research_data | Dashboard | Watchlist | Tests | Strategies | My Stocks | Brain-Journal | Bots-Hub | Settings`, built via `st.navigation`/`pages/`.
- **Refresh:** load-time fetch plus a manual "Refresh" button on every page. No polling, no websockets.
- **Universe:** fixed 14 symbols from `config/assets.toml` — `VOO VTI SPY QQQ AAPL MSFT NVDA AMZN GOOGL META BRK.B JPM COST TSLA`. No ad-hoc ticker search anywhere in V1.
- **Action vocabulary, exact strings, no synonyms:** `WATCH | HOLD | ACCUMULATE | REDUCE | AVOID | INSUFFICIENT_DATA`. Never render `BUY`/`SELL`/`guaranteed`/`risk-free`.
- **Confidence:** always the post-cap value (`min(analyst_confidence, critic-adjusted, ScorePacket.data_quality.max_confidence)`). Never render a raw uncapped number.
- **Numbers:** every figure on screen must trace to a `ScorePacket`, gate result, or `EvidenceCard` field. No client-side derived stats beyond simple aggregation (sums, deltas) of already-computed numbers.
- **Copy tone:** review prompts, not commands — "Review NVDA: momentum rank dropped from 3 to 9" not "Sell NVDA."
- **No execution chrome:** no broker connect, no order tickets, no auth/login screens.
## Page 1 — Dashboard (landing)
**Purpose:** the one page answering "what needs my attention right now."
### Components
1. **Tracked 5 strip** — 5 short buttons for a user-pinned symbol list (pin list is a simple config, not AI-selected). Each button: `[SYMBOL · ACTION · confidence%]`, color-coded by action. An urgency badge (small dot or border) highlights whichever of the 5 currently have a non-HOLD action or a confidence swing since `last_reviewed`. Hover shows momentum/quality/safety/valuation one-line context strings from the `ScorePacket`. Click → `/stock/{SYMBOL}`.
2. **Operational status panel**, three sub-blocks:
   - *Ingest status* — one line per provider (Polygon, Tiingo, FMP, SEC EDGAR, csv_fixture): last run timestamp + ✓/⚠️/✗, from `ingestion_runs`.
   - *Human steps required* — "N specs awaiting approval" (links to Strategies filtered `Proposed`) + "N paper theses awaiting pre-approval" (links to My Stocks pending view).
   - *Paper P&L* — total unrealized, today's delta, and vs-VOO (`voo_return_same_period`) computed across open `Thesis` rows.
3. **Cost/LLM panel** — call counts and estimated cost per provider (Gemini Flash / Groq / Ollama) pulled from the agents runner's own logging, last 24h and last 7d.
### Data sources
`ingestion_runs` table, `StrategySpec` (status filter), `Thesis` (open positions), agents runner call log, `ScorePacket`/`EvidenceCard` for the pinned 5.
### Non-goals
No full 14-symbol table here (that's Watchlist). No auto-refresh. No trade-entry controls.
## Page 2 — Watchlist
**Purpose:** the full research universe, one row per symbol.
### Table
| Symbol | Company | Action | Confidence | Data Quality | Last Reviewed | Paper Status |
|---|---|---|---|---|---|---|
Sourced from the latest `EvidenceCard` per symbol plus open/closed `Thesis` lookup for the Paper Status column (`open` / `closed` / `none`).
### Interactions
Click a row → full-page navigation to `/stock/{SYMBOL}` (Stock Detail). Sortable by Confidence and Last Reviewed. Filterable by Action and Data Quality.
### Non-goals
No add/remove symbol. No inline editing.
## Page 3 — Stock Detail (`/stock/{SYMBOL}`)
**Purpose:** everything known about one symbol, in one place. Shared target from Watchlist, Dashboard, and My Stocks.
### Layout, top to bottom
1. **Header** — symbol, company name, current action badge, capped confidence, `last_reviewed`, `next_review_date`.
2. **Price chart** — TradingView widget embed (`st.components.v1.html`) with overlays for MA20, MA50, MA200, RSI-14, Bollinger Bands, ATR. These are the only indicators the factor engine computes — no generic indicator picker.
3. **Factor score panel** — table or metric row: `momentum_score`, `safety_score`, `quality_fcf_score`, `valuation` composite, each shown as rank (1–14 across the universe) + raw value + the `ScorePacket` context string for that field.
4. **Evidence Card** — full card: action, confidence, summary, evidence, risks, opposing_evidence, invalidation_conditions, next_review_date, data_quality.
5. **Critic Review** — rendered directly below the Evidence Card, visually subordinate (smaller heading, indented, or a distinct muted color) since `confidence_delta ≤ 0` always — the critic can annotate down, never up, and the layout must not read as a second, equal opinion.
6. **Gate/spec status** (conditional) — if any `StrategySpec` targets this symbol: a compact OOS/MC/WF/DSR strip with the spec name and a link to its full row on Tests.
7. **Paper position + journal** (conditional) — if a `Thesis` exists (open or closed): entry date/price, exit date/price if closed, P&L, P&L vs VOO, `source_card_id` link back to the triggering evidence card, and any linked `JournalEntry` lessons. Tag `Replay` or `Live` depending on which paper mode produced it.
### Data sources
`ScorePacket` (factors), `EvidenceCard` + `CriticReview` (cards store), `StrategySpec`/gate results (brain), `Thesis`/`JournalEntry` (paper engine), price series via `PriceReadAPI` for the chart.
### Non-goals
No manual override of confidence or action. No "add to watchlist" (already fixed universe).
## Page 4 — Tests
**Purpose:** the four-gate promotion pipeline, pass/fail, in one screen.
### Layout
1. **Gate strip** — OOS → MC → WF → DSR, fixed order (immutable per Canon), showing aggregate counts (e.g. "12 specs demo-eligible, 34 failed at WF").
2. **Log table**, one row per spec's full gate run:

| Spec | OOS | MC | WF | DSR | Overall | Date |
|---|---|---|---|---|---|---|

Click a row → expand to the four numeric fields (`oos_net_sharpe`, `mc_p5_return`, `wf_pct_positive`, `deflated_sharpe_probability`), the linked `JournalEntry`, and the promote/demote decision if one was recorded.
### Styling rule
A failed gate is a correct, expected outcome — not an error. Use neutral fail styling (gray/muted, not alarm red) consistent with "proof over narrative."
### Data sources
Gate harness output tables, `PromotionDecision`, `JournalEntry`.
### Non-goals
No manual gate override. No editing gate parameters from the UI (cost-model/gate-param edits are explicitly banned outside tests).
## Page 5 — Strategies
**Purpose:** spec lifecycle management — what's been proposed, tested, promoted, or demoted.
### Layout
1. **Filter chips** — All | Proposed | Approved/Under test | Demo-eligible/Promoted | Demoted. Default view: Approved + Promoted.
2. **List**, sorted by most recent gate activity (a re-tested spec jumps to the top). Untested/proposed specs sort by proposal date within their bucket. Each row: spec name, status badge, symbol(s) in scope, last gate-run date, `params_delta` summary, `parent_spec_id` if it's a variant.
3. **Strategy detail** (click-through): full `StrategySpec` params, the `Citation` that proposed it, complete gate history (every run, not just latest), every promote/demote decision over time, linked journal entries.
### Human-gated actions
Approve / promote / demote buttons live only here (or in the existing CLI). `validate_human_identity` already blocks non-human callers (`cursor`, `claude`, `fable`) — the UI must pass through the real human identity, not a service account, when calling these.
### Data sources
`StrategySpec`, `Citation`, `PromotionDecision`, gate history.
### Non-goals
No AI-driven auto-approve. No batch-approve-all shortcut (each promotion is a discrete human decision).
## Page 6 — My Stocks (paper trading hub)
**Purpose:** every paper position, open or closed, with the tools to inspect any one of them.
### Layout
1. **Filters** — by symbol, by status (open / closed / all).
2. **Position list/cards** — entry date/price, exit date/price if closed, unrealized/realized P&L, P&L vs VOO (`voo_return_same_period`), `spec_id`/`source_card_id` links, `review_frequency`/`next_review_date`. Tag each `Replay` (accelerated historical replay) or `Live` (real-time-paced calendar paper book) — never blend the two in one list without the tag.
3. **Click-through** — opens the shared Stock Detail page (paper-position section), not a separate view.
### Data sources
`Thesis`, `JournalEntry`, price series for P&L calc.
### Non-goals
No manual position entry (positions come only from the pre-approved-thesis auto-entry mechanism, per the paper engine's design — this is not a portfolio tracker for real brokerage holdings).
## Page 7 — Brain-Journal
**Purpose:** browse the vault-mirrored notes — the human-readable trail behind every decision.
### Layout
1. **Card grid** (or timeline toggle) of vault notes with visible frontmatter, filterable by symbol/tag/date.
2. **View-only** — no inline frontmatter editing (the DB→vault mirror is one-way, "DB wins on conflict"; editing here would silently desync). Provide an "open in Obsidian" link for real edits.
### Relationship to Tests-page journal entries
Same underlying `JournalEntry`/`Citation` rows, different surface: Tests shows a gate-run's journal entry inline with its spec; Brain-Journal is the full vault-mirror browse view. Cross-link both directions.
### Data sources
`data/cards/{SYMBOL}_live_mirror.md` mirror files, `Citation` table.
### Non-goals
No note creation/editing from the UI.
## Page 8 — Bots-Hub
**Purpose:** operational control room for ingestion and the AI analyst/critic pipeline.
### Layout
1. **Status rows** — ingest status per provider, last analyst/critic run per symbol, LLM call/cost counts.
2. **Manual triggers** — "Run ingest now," "Run analyst on {symbol}," "Run gate test on {spec}." Each calls the existing CLI function directly (import + call, or subprocess) — no new execution logic is written for the UI.
3. **Logs** — collapsed by default per run, expandable on click, to avoid noise.
### Boundary
Cannot approve/promote/demote a spec from here — that stays on Strategies (or CLI), preserving the human-gate rule. Long-running triggers (especially "run gate test") should confirm before firing, since a gate pipeline run is not instantaneous.
### Data sources
`ingestion_runs`, agents runner logs, CLI functions (`init-db`, `ingest-prices`, `audit-prices`, `benchmark`, `analyze-symbol`, `critique-spec`).
### Non-goals
No scheduling/cron UI in V1 — triggers are on-demand only.
## Shared components (build once, reuse across pages)
- **Action badge** — renders the six-value action vocabulary with a fixed color mapping (color palette TBD — flagged as an open item).
- **Evidence Card renderer** — used on Stock Detail; no second copy of this component elsewhere.
- **Gate strip** — used on Tests (full) and Stock Detail (compact) — same underlying component, different verbosity prop.
- **P&L-vs-VOO widget** — used on Dashboard, My Stocks, and Stock Detail — always renders the comparison, never P&L alone.
## Open items (unresolved, need a follow-up decision)
- Exact color palette for the six action states.
- Confirmation-dialog UX for long-running Bots-Hub triggers.
- Whether Streamlit's native multipage routing handles the `/stock/{SYMBOL}` deep link cleanly, or needs a `?symbol=` query-param workaround plus a thin custom router.
## Review protocol for Cursor's output
When Cursor's build note comes back: check it against the six confirmed Stock Detail sections (Block D1 in the questionnaire note), the exact action vocabulary, the confidence-cap rule, and the "no BUY/SELL" rule before accepting any page as done. Any page that introduces a symbol-search box, an auto-approve action, or raw uncapped confidence numbers is out of spec and should be flagged back.

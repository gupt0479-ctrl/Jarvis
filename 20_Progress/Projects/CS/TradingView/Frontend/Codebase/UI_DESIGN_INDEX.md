# research_data UI — Information Architecture & Prototype Spec

> **Freezepoint:** IA locked 2026-07-29. Prototype contract — all page specs descope from here.
> This is a read-only reference for the frontend team. Changes require consensus.

---

## Overview

**Product Vision:** A learning-first research dashboard. Real-time visibility into strategy research, backtest results, paper trading execution, and the AI brain that powers recommendations. Styled like a game (play/farm mechanics) with full transparency into every decision.

**Stack:** Next.js/React (prototype with mock data), then production build after backend (`research_data` Python/DuckDB) is ready.

**Data Source:** Standalone JSON fixture files in `fixtures/` (imported by prototype components). Production: DuckDB via Python API layer.

---

## Navigation Structure

### Primary Nav (Header, 8 items)

```
research_data | Dashboard | Watchlist | Tests | Strategies | My Stocks | Brain-Journal | Bots-Hub | Settings
```

- **No sidebar** — all navigation in header
- **Header is persistent** across all pages
- **Breadcrumbs optional** for deep pages (e.g., `/my-stocks/NVDA/research` shows symbol in breadcrumb)

### Secondary Nav (Page-Internal)

Some pages have internal tabs/sidebars:
- **My Stocks**: Symbol sidebar + Position/Research tabs
- **Brain-Journal**: Folder panel + Journal/Research/Tests tabs
- **Bots-Hub**: Floating sidebar with Ingestion/Testing/Paper Trading/Logs tabs
- **Strategies**: Compare/Per-Strategy tabs

See individual page specs for details.

---

## Data Flow & Real-Time Strategy

### Live Panels (Fast Refresh)
- **Scope:** Price charts (My Stocks), portfolio value, pending decision banners
- **Interval:** As fast as data feed supports (Polygon/Tiingo personal tier ≈ 5–15min)
- **Mechanism:** Fragment re-render (just the panel), not full page reload
- **Display:** Always shows "Last updated: HH:MM" for honesty about freshness
- **Implementation:** Query fixture data at interval (prototype); real DuckDB in production

### AI Content (Slow Refresh)
- **Scope:** Evidence cards, factor scores, next-steps list, cost/bot tracking, gate logs
- **Interval:** 5-minute cycle or manual "Refresh" button
- **Mechanism:** Full component re-render (safe, no state loss)
- **Implementation:** Fixture JSON in prototype; Python `research_data` endpoints in production

### Non-Refreshing (Read-Once)
- **Tests page historical logs** (append-only, no refresh needed)
- **Brain-Journal vault entries** (static until you add new entries)
- **Settings** (user-controlled, no auto-update)

---

## Component Inventory

### Global Components

| Component | Purpose | Used On |
|-----------|---------|---------|
| `Header` | Navigation bar (8 items) + Logo + Settings icon | Every page |
| `SymbolModal` | Medium overlay: action, confidence, 2–3 factors, "View Full Analysis" CTA | Dashboard, Watchlist |
| `PendingDecisionBanner` | Top-of-view banner: "Entry pending: SYMBOL Day Time — countdown", "View thesis details" button | My Stocks, Strategies, Bots-Hub |
| `FactorPanel` | 4-row grid: momentum/safety/quality/valuation, ranked 1–14, color-coded | My Stocks Research, Stock previews |
| `EvidenceCard` | Full analysis: action, confidence, summary, risks, opposing evidence, sources | My Stocks Research tab |
| `CriticReview` | Subordinate to evidence: confidence delta, hold/demote suggestions, human decision state | My Stocks Research tab |
| `GatePanel` | 4-gate visualization: OOS | MC | WF | DSR, each with pass/fail status + expandable details | Tests, My Stocks Research, Strategies |
| `PortfolioChart` | Clean price-only chart with buy/sell markers, unrealized P&L, vs VOO label | My Stocks Position tab, Strategies |
| `TA_Chart` | Price chart with MA20/50/200, RSI-14, Bollinger, ATR overlays | My Stocks Research tab, Brain-Journal Research section |
| `JournalEntry` | Collapsible note: template type, date, title, frontmatter (tags, links), content preview | Brain-Journal Journal section, expandable on click |
| `LogRow` | Single timeline entry: timestamp, agent/source, action, status (pass/fail/pending), expandable | Tests, Bots-Hub Logs |

### Page-Specific Components

See individual page specs for component trees.

---

## Interaction Patterns

### Modals
- **SymbolModal** (Watchlist, Dashboard): action + confidence + 2–3 factors + "View Full Analysis"
  - Dismiss: X button, click outside, Escape key
  - Background: dimmed but visible
  - One instance only (not stacking)
  - Opens on `/my-stocks/{SYMBOL}/research` when clicked

### Deep Links
- **From Dashboard**: 
  - Top-6 button → SymbolModal
  - "View Full Watchlist" → `/watchlist`
  - Next-steps item → relevant page (e.g., "Approve spec" → `/strategies`)
- **From Watchlist**: 
  - Row click → `/my-stocks/{SYMBOL}/research`
- **From Modal**: 
  - "View Full Analysis" → `/my-stocks/{SYMBOL}/research`
- **From My Stocks**: 
  - Symbol click (in sidebar or breadcrumb) → pick another symbol
  - Position tab → clean chart
  - Research tab → TA chart + evidence
- **From Brain-Journal**: 
  - 3D Graph node click → 5-second detail popup, then returns
  - Journal entry click → expand inline
  - "View full entry" → modal or detail view
- **From Bots-Hub**: 
  - Log row click → expand details
  - Agent filter → re-render logs

### Sidebars (Page-Internal, Non-Collapsing)
- **My Stocks**: Symbol list (left), persistent, with search/filter
- **Brain-Journal**: Folder structure (left), persistent
- **Bots-Hub**: Floating sidebar triggered by arrow button, tabs inside (Ingestion | Testing | Paper Trading | Logs)

### Filters & Search
- **Watchlist**: Search by symbol/company (input field)
- **My Stocks**: Filter by symbol, status (open/closed/pending), date range
- **Tests**: Filter by gate, status, date range
- **Brain-Journal**: Search by tags, dates, content (top bar)
- **Bots-Hub Logs**: Filter by agent, status, date range (dual on unified view and per-agent tabs)
- **Strategies**: Filter by status (proposed/approved/promoted/demoted)

### Badges & States
- **Pending Decision Badge**: Appears on Dashboard top-6 button, Watchlist row, pending banner
- **Status Badge**: Strategy card (proposed/approved/promoted/demoted), Test row (pass/fail), Log entry (running/idle/complete)
- **Data Quality Badge**: Symbol card (Usable/Partial/Stale/Missing/Contradictory)

---

## Pending Decision Visibility

**Pending decisions propagate everywhere:**

1. **Position tab**: Pending line above live trades (e.g., "Pending: Enter MSFT Monday 9:30 AM ET")
2. **Evidence Card** (Research tab): Inline mention (e.g., "Pending action: ACCUMULATE on next Monday open")
3. **Top-of-view banner** (My Stocks, Strategies, Bots-Hub): High visual weight, countdown, "View thesis details" button
4. **Dashboard top-6 button**: Pending badge (e.g., "MSFT - Accumulate ⧐ (pending)")
5. **Watchlist row**: Pending badge in action column (same indicator)

**Banner style**: High visual weight (color, icon), always-on (not dismissible), scannable not alarming.

---

## Mock Data & Fixtures

All page specs embed a representative **excerpt** of their fixture data (for readability). The actual source files live in `fixtures/`:

```
fixtures/
  dashboard.json           # Top-6 stocks, ingest status, next steps, paper P&L
  watchlist.json           # Full 14-symbol table data
  my-stocks-nvda.json      # Position + Research tabs (one symbol example)
  tests.json               # All test runs, paginated
  strategies.json          # Active/promoted specs, cards, compare data
  brain-journal.json       # Graph nodes, journal entries, folders
  bots-hub.json            # Agent states, logs, sidebar tabs
  settings.json            # User preferences, auth status
```

Prototype code imports these directly. Production replaces imports with API calls to `research_data` backend.

---

## Page Specs (Quick Links)

1. [Dashboard](./UI_DESIGN_DASHBOARD_SPEC.md)
2. [Watchlist](./UI_DESIGN_WATCHLIST_SPEC.md)
3. [Tests](./UI_DESIGN_TESTS_SPEC.md)
4. [Strategies](./UI_DESIGN_STRATEGIES_SPEC.md)
5. [My Stocks](./UI_DESIGN_MYSTOCKS_SPEC.md)
6. [Brain-Journal](./UI_DESIGN_BRAIN_JOURNAL_SPEC.md)
7. [Bots-Hub](./UI_DESIGN_BOTS_HUB_SPEC.md)
8. [Settings](./UI_DESIGN_SETTINGS_SPEC.md)

---

## Design Tokens (Placeholder)

| Token | Value | Usage |
|-------|-------|-------|
| `color-action-watch` | Gray | WATCH badge |
| `color-action-hold` | Blue | HOLD badge |
| `color-action-accumulate` | Green | ACCUMULATE badge |
| `color-action-reduce` | Orange | REDUCE badge |
| `color-action-avoid` | Red | AVOID badge |
| `color-data-quality-usable` | Green | Data quality badge |
| `color-data-quality-partial` | Yellow | Data quality badge |
| `color-data-quality-stale` | Orange | Data quality badge |
| `color-data-quality-missing` | Red | Data quality badge |
| `color-pending-banner-bg` | Dark amber | Pending decision banner |
| `font-heading` | TBD (serif, serious) | Page titles, card headers |
| `font-body` | TBD (sans-serif) | Body text |
| `font-mono` | TBD (monospace) | Numbers, timestamps, code |

Production design system will define these; prototype uses placeholder values.

---

## Guardrails (Non-Negotiable)

- **Action vocabulary**: Only `WATCH | HOLD | ACCUMULATE | REDUCE | AVOID | INSUFFICIENT_DATA` — never `BUY`/`SELL`/"guaranteed"/"risk-free"
- **Confidence values**: Always post-cap, never above data quality cap
- **Numbers**: Every displayed value traces to a real `ScorePacket`, `GateResult`, or `JournalEntry` — no synthesis
- **Human gate**: UI never executes trades, approves specs, or promotes strategies — only triggers analysis and reads results
- **No backend calls in prototype**: All data from JSON fixtures; production swaps in real API calls

---

## Known Descopes (Production Phase)

- **3D Brain graph** (prototype = 2D network, production = cinematic 3D)
- **Particle swarm Bots-Hub** (prototype = 2D nodes-and-edges, production = animated swarm)
- **Full cost/usage analytics** (V1 = brief ops/security health line; full analytics after real LLM cost data exists)
- **Inline vault editing** (V1 = read-only mirror; edit in Obsidian, UI reads changes)

---

## Prototype Checklist

- [ ] All 8 page specs completed
- [ ] All fixture files generated (8 JSON files)
- [ ] Header component built (persistent nav)
- [ ] SymbolModal component built
- [ ] Deep-link routing verified (all 30+ routes work)
- [ ] Pending decision propagation tested (badge on all 5 surfaces)
- [ ] Real-time refresh boundaries tested (live vs slow vs static)
- [ ] Modal/sidebar interactions feel right (UX playtest)
- [ ] Mobile responsive down to 375px width
- [ ] No console errors, all components render

---

## How to Use This Spec

1. **Read this index first** to understand the overall shape
2. **Pick a page spec** that you're building
3. **Copy the fixture file** into your project (or import it)
4. **Build the component tree** shown in that spec
5. **Hook up routing** (navigate to other pages on button clicks)
6. **Test interactions** (modals, tabs, filters, search)
7. **Check pending decision badges** propagate correctly
8. **Validate against guardrails** (no banned action words, etc.)

Questions or gaps? Flag them early — this is the last chance to reshape before code starts.

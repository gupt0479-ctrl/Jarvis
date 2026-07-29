# Fixture Files — Prototype Data

> Standalone JSON fixtures for the Next.js/React prototype. These are the "mock data" the prototype components import and render against.

---

## Structure

```
fixtures/
  dashboard.json              # Top-6 stocks, ingest status, next steps, paper P&L
  watchlist.json              # Full 14-symbol table data
  my-stocks-nvda.json         # Example: Position + Research tabs for NVDA
  tests.json                  # All test runs, paginated (25/page)
  strategies.json             # Active specs (≤5), cards + compare data
  brain-journal.json          # Graph nodes, edges, journal entries, folders
  bots-hub.json               # Agent states, logs, sidebar tabs
  settings.json               # User prefs, API status, system health
```

---

## How to Use These

### In React Components

```javascript
// Example: Import fixture and render Dashboard
import dashboardData from '../fixtures/dashboard.json';

export function Dashboard() {
  const data = dashboardData;
  return (
    <>
      <TodaysTradesPanel trades={data.dashboard.today_trades} />
      <WatchlistMiniPanel stocks={data.dashboard.watchlist_mini} />
      <IngestStatusPanel providers={data.dashboard.ingest_status} />
      {/* etc. */}
    </>
  );
}
```

### Production Swap

When the backend is ready, replace the static import with a dynamic fetch:

```javascript
// Prototype (static)
import dashboardData from '../fixtures/dashboard.json';
const data = dashboardData;

// Production (dynamic)
const res = await fetch('/api/dashboard');
const data = await res.json();
```

The component code stays the same — only the data source changes.

---

## Data Consistency Rules

- **Timestamps**: All `as_of` fields should match when generating fresh fixtures (e.g., all say "2026-07-20T14:30:00Z")
- **Cross-fixture references**: 
  - A spec ID in `strategies.json` should exist in `tests.json` if it has test results
  - A symbol in `watchlist.json` should match symbols in `my-stocks-*.json`
  - Entry IDs in `brain-journal.json` should be valid (no broken links)
- **Counts and percentages**: 
  - Sum of open positions in `my-stocks-*.json` should roughly match portfolio P&L in `dashboard.json` (or at least be in the same ballpark)
  - Win rates in strategy cards should match historical trades
- **Pending decisions**: 
  - Any pending trade in a symbol's `my-stocks-*.json` should also show a pending badge in `dashboard.json` and `watchlist.json` for that symbol
  - The pending logic text must match across all three files

---

## Fixture File Details

### dashboard.json

**Size**: ~1 KB  
**Refreshed**: Every 5 min (simulated)  
**Contains**:
- Top 6 stocks (1 starred + 5 by confidence)
- Ingest status per provider (Polygon, Tiingo, FMP)
- Next steps list (clickable tasks)
- Paper trading P&L (today, month-to-date, vs VOO)
- Backend ops status (API keys, secrets, active specs, LLM quota)

**Keys**: `today_trades`, `watchlist_mini`, `ingest_status`, `next_steps`, `paper_trading`, `backend_ops`

---

### watchlist.json

**Size**: ~3 KB  
**Refreshed**: Every 5 min  
**Contains**:
- All 14 symbols with: action, confidence, data quality, last reviewed, pending badge
- Sort order: starred first, then by confidence descending

**Keys**: `symbols` (array of 14), `total_count`, `displayed_count`

---

### my-stocks-{SYMBOL}.json

**Size**: ~5–8 KB per symbol  
**Refreshed**: Live panels (5–15 min), AI content (5 min)  
**Contains**:
- Current price and recent price chart
- Open and closed positions (trades)
- TA chart data (MA20/50/200, RSI, Bollinger, ATR)
- Evidence card (action, confidence, factors)
- Critic review
- Gate status (latest test)
- Data quality badges

**Keys**: `symbol`, `company_name`, `pending_decision`, `position_tab`, `research_tab`

**Note**: Generate one fixture file per symbol (or at least 2–3 examples: NVDA, MSFT, AAPL) so the prototype team can test symbol switching in My Stocks sidebar.

---

### tests.json

**Size**: ~8–10 KB  
**Refreshed**: Manual button or on new test completion  
**Contains**:
- All test runs, most-recent-first, paginated (25/page)
- Each run: spec ID, symbol, date, status (PASS/FAIL), which gate failed, promotion decision

**Keys**: `runs` (array), `total_count`, `page`, `page_size`

**Note**: Include ≥10 test runs (mix of passed and failed) so filters and pagination are testable. Include at least 2 failed tests so users can practice expanding failure details.

---

### strategies.json

**Size**: ~6–10 KB  
**Refreshed**: Every 5 min (portfolio value updates)  
**Contains**:
- ≤5 strategy spec cards (typically 2–3 live, rest proposed/demoted)
- For each: name, status, created date, portfolio value, latest test results, decision history
- Portfolio chart data (15–30 price points)
- Compare data (Sharpe, drawdown, win rate, etc.)

**Keys**: `specs` (array), `total_specs`

**Note**: Include at least 2 specs in different statuses (one PROMOTED, one PROPOSED) so decision buttons are visible.

---

### brain-journal.json

**Size**: ~10–15 KB  
**Refreshed**: Manual button (append-only)  
**Contains**:
- Graph nodes (≥20, mixed template types: test success, failure, ingestion, etc.)
- Graph edges (≥40, showing connections)
- Folder hierarchy (PARA: Projects, Areas, Resources, Archives + Templates)
- Recent entries feed (≥15 entries, only those passing completeness check)
- Frontmatter and entry content (markdown)

**Keys**: `graph`, `journal`

**Note**: Include enough nodes/edges to make the graph non-trivial (not just 3 nodes). Mix template types so color-coding is visible. Include at least one failed completeness check entry (draft) so the folder tree shows drafts separately.

---

### bots-hub.json

**Size**: ~5–7 KB  
**Refreshed**: Every 2–5 sec (agent state changes)  
**Contains**:
- Agent nodes (6: Ingest-Bot, Analyst, Critic, FactorEngine, GateRunner, PaperEngine)
- Edges (showing data flow)
- Provider status (Polygon, Tiingo, FMP) with next-run countdown
- Analyst status (running, queued symbols)
- Testing queue (active/queued tests)
- Paper trading pending theses and active positions
- Unified logs (≥10 entries, mixed agents and statuses)

**Keys**: `swarm`, `sidebar`

**Note**: Include at least one agent in RUNNING state (yellow) so animation is visible. Include log entries with different statuses (SUCCESS, RUNNING, ERROR) so filters are testable.

---

### settings.json

**Size**: ~3 KB  
**Refreshed**: Load once, manual refresh for checks  
**Contains**:
- Account info (hardcoded "anant")
- UI preferences (dark mode, refresh intervals, sidebar behavior)
- API key statuses (4 providers)
- Secrets redaction status
- System health (database, backend, disk, warnings if any)
- About info (version, links)

**Keys**: `account`, `ui_preferences`, `api_secrets`, `system_health`, `about`

---

## Testing the Fixtures

### Consistency Checklist

Before handing to the prototype team:

1. **All fixtures have same `as_of` timestamp** (or at least document why one differs)
2. **Symbol lists match**:
   - `watchlist.json` has 14 symbols
   - `dashboard.json` top-6 are a subset of those 14
   - Each symbol in dashboard/watchlist has a corresponding `my-stocks-{SYMBOL}.json`
3. **Pending decision badges**:
   - If symbol in `my-stocks-NVDA.json` has `pending_decision.exists: true`
   - Then `watchlist.json` NVDA row has `is_pending: true`
   - Then `dashboard.json` top-6 NVDA button (if present) has pending badge
4. **Strategy counts**:
   - `strategies.json` has ≤5 specs
   - Each spec appears in `tests.json` with at least one test run
5. **Entry links**:
   - In `brain-journal.json`, all `edges` reference valid node IDs
   - In `tests.json`, all `linked_journal_entry.entry_id` exist in `brain-journal.json`
6. **Portfolio reconciliation**:
   - Sum of all open position values in `my-stocks-*.json` (if sampled) should be in ballpark of `dashboard.json.paper_trading.open_positions`

---

## Generating Real Fixtures (Post-Prototype)

Once the backend is running, export live data to JSON:

```bash
# Python script to dump current state as fixtures
python -c "
from research_data import get_dashboard_data
import json

data = get_dashboard_data()
with open('fixtures/dashboard.json', 'w') as f:
    json.dump({'dashboard': data}, f, indent=2)
"
```

This ensures prototype fixtures are always in sync with backend reality.

---

## When Fixtures Change

If the spec document changes (e.g., new field added to Evidence Card):

1. Update one fixture file as example
2. Run a consistency check script
3. Notify prototype team of the change
4. Regenerate all fixtures if backward-incompatible

Keep fixtures version-controlled in Git so diffs are visible.

---

## Prototype Team Handoff

Provide:
1. All 8 fixture JSON files
2. This README
3. Each page spec doc (links to fixtures embedded in spec)
4. Component inventory from Index doc
5. Design tokens/color palette

Expected workflow:
```
1. Clone repo
2. Copy fixtures/ folder
3. For each page, import fixture and build components
4. Test interactions against fixture data
5. Before merge, validate against consistency checklist
```

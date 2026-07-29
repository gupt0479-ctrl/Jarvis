# Dashboard Spec

> The landing page. Operational hub: what's happening now, what needs human attention, what's ready to act on.
> Reference: `fixtures/dashboard.json`

---

## Purpose

Show the **current state of the research desk** at a glance:
- What bots/ingestion are doing **right now**
- What **human approvals are pending**
- **Today's trade recommendations** (top 6 by urgency/confidence)
- **Paper trading P&L** (today, month-to-date, vs VOO)
- **Next manual steps** (AI-generated, each clickable to relevant page)

---

## Layout (Scrollable Vertical)

```
┌─────────────────────────────────────────────────────────┐
│ research_data | Dashboard | Watchlist | ...    [⚙ Settings]│
├─────────────────────────────────────────────────────────┤
│                                                          │
│ ▼ TODAY'S TRADES (6 items: 1 starred + 5 by confidence)│
│ ┌──────────────────────────────────────────────────────┐│
│ │ ★ AAPL - Accumulate - 82% conf    [pending badge]   ││
│ │ MSFT - Hold - 73% conf                              ││
│ │ NVDA - Watch - 55% conf                             ││
│ │ GOOGL - Hold - 65% conf                             ││
│ │ AMZN - Accumulate - 89% conf      [pending badge]   ││
│ │ META - Watch - 54% conf                             ││
│ └──────────────────────────────────────────────────────┘│
│                                                          │
│ ▼ WATCHLIST (top 5 from full 14 + "View Full" link)   │
│ ┌──────────────────────────────────────────────────────┐│
│ │ Symbol │ Company │ Action │ Confidence │ Last Review ││
│ │ AAPL   │ Apple   │ Accum  │ 82%        │ Jul 20      ││
│ │ MSFT   │ Micro   │ Hold   │ 73%        │ Jul 20      ││
│ │ NVDA   │ Nvidia  │ Watch  │ 55%        │ Jul 20      ││
│ │ GOOGL  │ Alphabet│ Hold   │ 65%        │ Jul 19      ││
│ │ AMZN   │ Amazon  │ Accum  │ 89%        │ Jul 19      ││
│ │                                                      ││
│ │ [View Full Watchlist (14 symbols) →]                ││
│ └──────────────────────────────────────────────────────┘│
│                                                          │
│ ▼ INGEST STATUS (per provider, timestamp on hover)     │
│ ┌──────────────────────────────────────────────────────┐│
│ │ Polygon: ✓     [hover: Last 3h ago]                 ││
│ │ Tiingo:  ✓     [hover: Last 5h ago]                 ││
│ │ FMP:     ✓     [hover: Last 1h ago]                 ││
│ └──────────────────────────────────────────────────────┘│
│                                                          │
│ ▼ NEXT STEPS REQUIRED (AI-generated, each clickable)   │
│ ┌──────────────────────────────────────────────────────┐│
│ │ → Approve quality_momentum_tilt_top3 spec (MSFT)    ││
│ │   [Strategies page]                                 ││
│ │                                                      ││
│ │ → Pre-approve NVDA position entry thesis            ││
│ │   [My Stocks / NVDA]                                ││
│ │                                                      ││
│ │ → Review failed test: momentum_only (JPM)           ││
│ │   [Tests page]                                      ││
│ └──────────────────────────────────────────────────────┘│
│                                                          │
│ ▼ PAPER TRADING (brief overview)                        │
│ ┌──────────────────────────────────────────────────────┐│
│ │ Today:           +$245          (+0.8% vs VOO +0.3%)││
│ │ Month-to-date:   +$2,430        (+5.2% vs VOO +3.1%)││
│ │ Open positions:  5 (AAPL, MSFT, NVDA, GOOGL, QQQ)   ││
│ │                                                      ││
│ │ [View My Stocks →]                                  ││
│ └──────────────────────────────────────────────────────┘│
│                                                          │
│ ▼ BACKEND OPS (brief status)                            │
│ ┌──────────────────────────────────────────────────────┐│
│ │ API Keys: Valid (last check 2h ago)                 ││
│ │ Secrets redaction: Passing                          ││
│ │ Active specs under test: 2 (momentum_only, qual_val)││
│ │ LLM calls (24h): 14 / 500 quota                      ││
│ │                                                      ││
│ │ [Bots-Hub for details →]                            ││
│ └──────────────────────────────────────────────────────┘│
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Component Tree

```
DashboardPage
├── Header (global)
├── Section: TodaysTradesPanel
│   └── TopSixButtonList (6 items, sorted by star + confidence)
│       ├── SymbolButton (starred variant)
│       └── SymbolButton (pending badge variant) × 5
├── Section: WatchlistMiniPanel
│   ├── WatchlistTable (top 5 symbols)
│   │   └── TableRow (click → SymbolModal)
│   └── Button: "View Full Watchlist" (navigate to /watchlist)
├── Section: IngestStatusPanel
│   └── ProviderStatusRow × 3 (Polygon, Tiingo, FMP)
│       └── [hoverable timestamp]
├── Section: NextStepsPanel
│   └── ClickableTaskItem × N
│       └── Routes to relevant page on click
├── Section: PaperTradingPanel
│   ├── StatBadge (Today P&L)
│   ├── StatBadge (Month P&L)
│   ├── StatBadge (Open positions count)
│   └── Button: "View My Stocks"
└── Section: BackendOpsPanel
    ├── StatusLine (API keys)
    ├── StatusLine (Secrets check)
    ├── StatusLine (Active specs)
    ├── StatusLine (LLM quota)
    └── Button: "Bots-Hub for details"
```

---

## Data Shape (Fixture Excerpt)

```json
{
  "dashboard": {
    "as_of": "2026-07-20T14:30:00Z",
    "today_trades": [
      {
        "symbol": "AAPL",
        "company_name": "Apple Inc.",
        "action": "ACCUMULATE",
        "confidence": 0.82,
        "is_starred": true,
        "is_pending": false,
        "pending_logic": null
      },
      {
        "symbol": "MSFT",
        "company_name": "Microsoft Corp.",
        "action": "HOLD",
        "confidence": 0.73,
        "is_starred": false,
        "is_pending": true,
        "pending_logic": "Entry pending: Monday 9:30 AM ET — 2 days 4 hours away"
      }
      // 4 more...
    ],
    "watchlist_mini": [
      // same shape as today_trades, top 5
    ],
    "ingest_status": [
      {
        "provider": "Polygon",
        "status": "healthy",
        "last_ingest_time": "2026-07-20T11:30:00Z",
        "symbols_count": 14
      },
      {
        "provider": "Tiingo",
        "status": "healthy",
        "last_ingest_time": "2026-07-20T09:30:00Z",
        "symbols_count": 14
      },
      {
        "provider": "FMP",
        "status": "healthy",
        "last_ingest_time": "2026-07-20T13:00:00Z",
        "symbols_count": 10
      }
    ],
    "next_steps": [
      {
        "task_id": "approve-spec-msft",
        "text": "Approve quality_momentum_tilt_top3 spec (MSFT)",
        "target_page": "/strategies",
        "priority": "high"
      },
      {
        "task_id": "preapprove-thesis-nvda",
        "text": "Pre-approve NVDA position entry thesis",
        "target_page": "/my-stocks/NVDA",
        "priority": "high"
      },
      {
        "task_id": "review-fail-jpm",
        "text": "Review failed test: momentum_only (JPM)",
        "target_page": "/tests",
        "priority": "medium"
      }
    ],
    "paper_trading": {
      "today_pnl": 245,
      "today_pnl_pct": 0.008,
      "today_voo_pnl_pct": 0.003,
      "mtd_pnl": 2430,
      "mtd_pnl_pct": 0.052,
      "mtd_voo_pnl_pct": 0.031,
      "open_positions": [
        {
          "symbol": "AAPL",
          "entry_date": "2026-07-10",
          "current_value": 5200
        }
        // 4 more...
      ]
    },
    "backend_ops": {
      "api_keys_valid": true,
      "last_api_check_time": "2026-07-20T12:30:00Z",
      "secrets_redaction_passing": true,
      "active_specs_under_test": 2,
      "llm_calls_24h": 14,
      "llm_quota_total": 500
    }
  }
}
```

---

## Interactions

### Top-Six Buttons

**Click behavior:**
- Opens `SymbolModal` (overlay, not full-page navigation)
- Modal shows: action, confidence, 1-line summary, top 2–3 factors, "View Full Analysis" button
- "View Full Analysis" → `/my-stocks/{SYMBOL}/research` (full page)

**Hover behavior:**
- Button expands slightly (visual feedback)
- If pending: pending countdown badge remains visible

**Pending badge:**
- Appears on any symbol with an open thesis awaiting execution
- Shows on Dashboard button AND Watchlist row AND pending banner (when on My Stocks page)

### Watchlist Mini

**Click behavior:**
- Same as top-six: opens `SymbolModal`
- "View Full Watchlist" → `/watchlist` (full page)

### Next Steps

**Click behavior:**
- Each task is a link to its target page
- "Approve spec" → `/strategies`
- "Pre-approve thesis" → `/my-stocks/{SYMBOL}` (with context that you're there to approve)
- "Review failed test" → `/tests` (filtered to show that specific failure)

**Task priority indicator:**
- High = red/amber left border
- Medium = gray border

### Ingest Status

**Hover behavior:**
- Tooltip on each provider showing exact timestamp
- Example: "Polygon: Last ingest 3 hours ago (2026-07-20 11:30 UTC)"

**Visual states:**
- `healthy` = green checkmark
- `stale` (>24h) = yellow warning
- `failed` = red X

### Paper Trading

**Click:** "View My Stocks" → `/my-stocks` (portfolio view by default)

### Backend Ops

**Click:** "Bots-Hub for details" → `/bots-hub` (with Ingestion tab open by default)

---

## Refresh Strategy

- **Initial load**: Render from fixture (prototype) or fetch from API (production)
- **Live panels**: Price-dependent data (if any future additions) refresh at 5–15 min interval
- **Manual refresh**: Button in header or page-level "Refresh now" button
- **Auto-refresh**: Dashboard re-fetches next-steps and ingest status every 5 minutes
- **No polling on first load**: User sees stale-but-consistent data until manual refresh

---

## Edge Cases

### No pending decisions
- Pending badge and countdown don't appear
- Dashboard and Watchlist look the same (just action + confidence)

### No open positions
- Paper Trading section shows: "No open positions. [View Watchlist to start]"

### Ingest failure
- Provider row shows red X + error message on hover (e.g., "API key invalid")

### Next steps list empty
- Shows: "All caught up! No pending approvals or reviews."

### All 6 top trades are the same
- Only happens if universe is tiny; same pattern applies (star pinned, rest by confidence)

---

## Accessibility & Mobile

- **Tab order**: Header nav → Today's trades → Watchlist → Ingest → Next steps → Paper trading → Ops
- **Mobile (<640px)**: All sections stack, buttons scale to full width, table becomes card layout
- **Search**: None on Dashboard (search is on Watchlist page)
- **Keyboard nav**: Arrow keys to move between top-six buttons, Enter to open modal

---

## Prototype Acceptance Criteria

- [ ] All 6 sections render correctly
- [ ] Top-six buttons clickable, open SymbolModal
- [ ] Pending badge shows on starred/pending symbol
- [ ] "View Full Watchlist" navigates to `/watchlist`
- [ ] Next steps items clickable to their target pages
- [ ] Ingest status timestamp visible on hover
- [ ] Paper trading numbers format correctly (e.g., "$2,430", "+5.2%")
- [ ] Responsive down to 375px
- [ ] Dark mode (if applicable) looks right

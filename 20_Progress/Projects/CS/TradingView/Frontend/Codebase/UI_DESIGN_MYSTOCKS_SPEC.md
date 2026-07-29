# My Stocks Spec

> Deep dive into any symbol. Two-tab interface: Position (clean price chart with trades) + Research (analysis & evidence). This is the hub for learning how decisions executed.
> Reference: `fixtures/my-stocks-nvda.json` (example symbol)

---

## Purpose

For any of the 14 symbols, show:
1. **Position tab**: Live/historical price, entry/exit markers, P&L, vs VOO
2. **Research tab**: TA chart, factor scores, evidence card, critic review, gate status, pending decisions
3. **All-symbol sidebar**: Pick a different symbol without leaving the page
4. **Real-time sync**: Price updates every 5–15 min, pending decisions visible immediately
5. **Learning loop**: See why the brain made a decision, then see how it executed

---

## Layout

### Full Page Structure

```
┌───────────────────────────────────────────────────────────┐
│ research_data | Dashboard | Watchlist | ...   [⚙ Settings] │
├───────────────────────────────────────────────────────────┤
│                                                            │
│ ┌──────────────────┐ ┌──────────────────────────────────┐ │
│ │ SYMBOL SIDEBAR   │ │ MAIN VIEW (Position or Research)│ │
│ │ (transparent)    │ │                                  │ │
│ │                  │ ├──────────────────────────────────┤ │
│ │ [Search: __]     │ │ NVDA │ ★ │  [Position] [Research]│ │
│ │ [Favorites ▼]    │ │                                  │ │
│ │                  │ │ [PENDING DECISION BANNER]        │ │
│ │ AAPL             │ │ Entry pending: NVDA Mon 9:30 AM  │ │
│ │ MSFT             │ │ (2 days 4 hrs away) [View thesis]│ │
│ │ ► NVDA (current) │ │                                  │ │
│ │ GOOGL            │ │ [CHART + TRADING ACTIVITY]       │ │
│ │ AMZN             │ │ ... (see Position vs Research)   │ │
│ │ META             │ │                                  │ │
│ │ VOO              │ │                                  │ │
│ │ [show more ▼]    │ │                                  │ │
│ │                  │ │                                  │ │
│ └──────────────────┘ └──────────────────────────────────┘ │
│                                                            │
└───────────────────────────────────────────────────────────┘
```

### Sidebar (Always Visible, Left Side)

```
┌──────────────────────┐
│ SYMBOL SIDEBAR       │
├──────────────────────┤
│ [Search: ___]        │
│                      │
│ [Favorites ▼]        │  ← Click to expand/collapse
│                      │
│ Starred symbols:     │
│ ★ AAPL               │
│ ★ MSFT               │
│                      │
│ [All 14 ▼]           │
│                      │
│ All symbols:         │
│ ► NVDA (current)     │  ← Highlighted when active
│   GOOGL              │
│   AMZN               │
│   [... 10 more ...]  │
│   [Show remaining]   │
│                      │
└──────────────────────┘
```

---

## Tabs: Position vs Research

### TAB 1: Position (Clean Price, Trades, P&L)

```
┌──────────────────────────────────────────────────────────┐
│ NVDA – Nvidia Corp.                    [Position] [Research]│
├──────────────────────────────────────────────────────────┤
│                                                            │
│ [PENDING DECISION BANNER (if applicable)]                │
│                                                            │
│ ┌────────────────────────────────────────────────────────┐│
│ │  Clean price chart (no indicators)                     ││
│ │  X-axis: Date  |  Y-axis: Price                        ││
│ │  Entry markers: green ▲                                ││
│ │  Exit markers: red ▼                                   ││
│ │  [Chart SVG/canvas]                                    ││
│ │                                                        ││
│ │  Last updated: 2:47 PM (15 min ago)     [Refresh]    ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ Current Price: $123.45  (+2.3% today)                    │
│                                                            │
│ Open Positions (3 active):                               │
│ ┌────────────────────────────────────────────────────────┐│
│ │ Entry Date  │ Entry Price │ Shares │ Current Value │P&L││
│ │ Jul 10      │ $110.25     │ 50     │ $6,172.50     │+6%││
│ │ Jul 15      │ $115.00     │ 30     │ $3,703.50     │+3%││
│ │ Jul 18      │ $120.00     │ 25     │ $3,086.25     │+3%││
│ │                                                        ││
│ │ Total open: $13,000 realized (vs VOO: +4.2%)          ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ Closed Positions (history):                              │
│ ┌────────────────────────────────────────────────────────┐│
│ │ Entry  │ Exit   │ Shares │ Entry $ │ Exit $ │ P&L    ││
│ │ Jul 1  │ Jul 9  │ 100    │ $105    │ $108   │ +$300  ││
│ │ Jun 28 │ Jul 3  │ 50     │ $102    │ $101   │ -$50   ││
│ │                                                        ││
│ │ [Show more history ▼]                                 ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ Position Stats:                                           │
│ • Avg entry: $115.08                                      │
│ • Win rate: 75% (3 wins, 1 loss in closed)              │
│ • Total P&L (all time): +$5,230                         │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

### TAB 2: Research (Analysis, Evidence, Factors, Gates)

```
┌──────────────────────────────────────────────────────────┐
│ NVDA – Nvidia Corp.                    [Position] [Research]│
├──────────────────────────────────────────────────────────┤
│                                                            │
│ [PENDING DECISION BANNER (if applicable)]                │
│                                                            │
│ ┌────────────────────────────────────────────────────────┐│
│ │  TA Chart: MA20/50/200, RSI-14, Bollinger, ATR        ││
│ │  [Chart SVG/canvas with indicators]                    ││
│ │                                                        ││
│ │  Last updated: 2:47 PM (15 min ago)      [Refresh]    ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ EVIDENCE CARD                                          │
│ ┌────────────────────────────────────────────────────────┐│
│ │ Action: ACCUMULATE                                    ││
│ │ Confidence: 0.72 (capped by data quality: 0.75)       ││
│ │ Spec ID: 5f003778-42bc-4d8a-ac12-839699d98a02        ││
│ │ Thesis: quality_momentum_tilt_top3                     ││
│ │ Demo-eligible: YES ✓ (all 4 gates passed)             ││
│ │                                                        ││
│ │ Summary:                                              ││
│ │ "Cloud AI infrastructure continues to compound        ││
│ │  at high-quality score with strong momentum."         ││
│ │                                                        ││
│ │ Supporting Evidence:                                  ││
│ │ • Momentum (12-1): Rank 2/14 — 0.82 score            ││
│ │ • Quality (FCF): Rank 5/14 — 0.68 score              ││
│ │ • Safety: Rank 8/14 — 0.55 score                    ││
│ │ • ETF Baseline: +18.2% vs VOO                        ││
│ │                                                        ││
│ │ Risks & Invalidation:                                 ││
│ │ • High valuation multiple; PE compression risk        ││
│ │ • Geopolitical exposure (Taiwan, China)               ││
│ │ • Invalidates if momentum rank drops below 5          ││
│ │                                                        ││
│ │ [Journal Entry] [View Full Spec] [Edit Decision]      ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ CRITIC REVIEW                                          │
│ ┌────────────────────────────────────────────────────────┐│
│ │ Analyst confidence: 0.72                              ││
│ │ Critic adjustment: -0.03 (modest OOS Sharpe deg)      ││
│ │ Final confidence: 0.72 (capped by quality)            ││
│ │ Critic suggestion: HOLD (not AVOID)                   ││
│ │                                                        ││
│ │ Status: Human approved ACCUMULATE (2026-07-20 10:22) ││
│ │ [View critic details]                                 ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ GATE STATUS                                            │
│ ┌────────────────────────────────────────────────────────┐│
│ │ Strategy: quality_momentum_tilt_top3                   ││
│ │ Latest test: 2026-07-20 06:00 UTC                      ││
│ │                                                        ││
│ │ ✓ Out-of-Sample      Sharpe: 0.72 vs IS: 1.44        ││
│ │ ✓ Monte Carlo        5%-ile return: +2.1% (> 0)      ││
│ │ ✓ Walk-Forward       62% windows positive             ││
│ │ ✓ Deflated Sharpe    Prob 98.5% (> 95%)              ││
│ │                                                        ││
│ │ [View full gate logs]                                 ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ DATA QUALITY                                            │
│ ┌────────────────────────────────────────────────────────┐│
│ │ ✓ Price: USABLE (1511 sessions, no gaps)             ││
│ │ ✓ Fundamentals: USABLE (Q2 2026 from FMP)            ││
│ │ ⚠ TA indicators: STALE (5 days old)                  ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
└──────────────────────────────────────────────────────────┘
```

---

## Component Tree

```
MyStocksPage
├── Header (global)
├── SymbolSidebar
│   ├── SearchInput
│   ├── FavoritesAccordion
│   │   └── StarredSymbols (click → switch symbol)
│   └── AllSymbolsAccordion
│       └── SymbolList (click → switch symbol, highlight current)
├── MainView
│   ├── TopBar
│   │   ├── BreadcrumbSymbol
│   │   ├── StarIcon (toggle favorite)
│   │   └── TabBar (Position | Research)
│   ├── PendingDecisionBanner (if applicable)
│   └── TabContent
│       ├── PositionTab
│       │   ├── PriceChart (clean, buy/sell markers)
│       │   ├── CurrentPriceDisplay
│       │   ├── OpenPositionsTable
│       │   ├── ClosedPositionsTable (expandable)
│       │   └── PositionStats
│       └── ResearchTab
│           ├── TAChart (with MA/RSI/Bollinger/ATR)
│           ├── EvidenceCard
│           ├── CriticReview
│           ├── GatePanel
│           └── DataQualityPanel
```

---

## Data Shape (Fixture Excerpt)

```json
{
  "my_stocks": {
    "symbol": "NVDA",
    "company_name": "Nvidia Corp.",
    "as_of": "2026-07-20T14:30:00Z",
    "is_favorite": false,
    "current_price": 123.45,
    "price_change_today_pct": 0.023,
    "last_price_update": "2026-07-20T14:15:00Z",
    
    "pending_decision": {
      "exists": true,
      "type": "entry",
      "action": "ACCUMULATE",
      "trigger_logic": "Monday 9:30 AM ET",
      "days_away": 2.17,
      "hours_away": 4,
      "thesis_id": "thesis-nvda-001"
    },

    "position_tab": {
      "price_chart": {
        "data_points": [
          { "date": "2026-07-10", "price": 110.25 },
          { "date": "2026-07-11", "price": 112.50 },
          // ... 40+ more points
        ],
        "entry_markers": [
          { "date": "2026-07-10", "price": 110.25, "shares": 50 },
          { "date": "2026-07-15", "price": 115.00, "shares": 30 },
          { "date": "2026-07-18", "price": 120.00, "shares": 25 }
        ],
        "exit_markers": [
          { "date": "2026-07-09", "price": 108.00 }
        ]
      },
      "open_positions": [
        {
          "entry_date": "2026-07-10",
          "entry_price": 110.25,
          "shares": 50,
          "current_value": 6172.50,
          "pnl_pct": 0.06,
          "vs_voo_pct": 0.042
        }
        // 2 more...
      ],
      "closed_positions": [
        {
          "entry_date": "2026-07-01",
          "exit_date": "2026-07-09",
          "entry_price": 105.00,
          "exit_price": 108.00,
          "shares": 100,
          "pnl": 300,
          "pnl_pct": 0.0286
        }
        // more...
      ],
      "position_stats": {
        "avg_entry_price": 115.08,
        "total_shares_open": 105,
        "total_open_value": 13000,
        "total_pnl_all_time": 5230,
        "closed_trades_count": 2,
        "win_rate": 0.75
      }
    },

    "research_tab": {
      "ta_chart": {
        "data_points": [
          { "date": "2026-07-20", "price": 123.45, "ma20": 118.5, "ma50": 115.2, "ma200": 112.0, "rsi": 62, "bbands_upper": 125.0, "bbands_lower": 110.0, "atr": 2.5 }
          // ... more points
        ]
      },
      "evidence_card": {
        "action": "ACCUMULATE",
        "confidence": 0.72,
        "confidence_capped_by_quality": 0.75,
        "spec_id": "5f003778-42bc-4d8a-ac12-839699d98a02",
        "strategy_name": "quality_momentum_tilt_top3",
        "demo_eligible": true,
        "summary": "Cloud AI infrastructure continues to compound...",
        "factor_scores": [
          { "factor": "momentum", "score": 0.82, "rank": 2, "description": "12-1 month total-return rank" },
          { "factor": "quality", "score": 0.68, "rank": 5, "description": "FCF/EV ratio" },
          { "factor": "safety", "score": 0.55, "rank": 8, "description": "Inverse 12m realized vol" },
          { "factor": "valuation", "score": 0.45, "rank": 10, "description": "FCF/EV vs universe" }
        ],
        "etf_baseline": {
          "symbol": "VOO",
          "outperformance_pct": 0.182
        },
        "supporting_evidence": [
          "Momentum (12-1): Rank 2/14 — 0.82 score",
          "Quality (FCF): Rank 5/14 — 0.68 score"
        ],
        "risks": [
          "High valuation multiple; PE compression risk",
          "Geopolitical exposure (Taiwan, China)"
        ],
        "invalidation_conditions": [
          "Momentum rank drops below 5",
          "FCF/EV ratio turns negative"
        ]
      },
      "critic_review": {
        "analyst_confidence": 0.72,
        "critic_adjustment": -0.03,
        "final_confidence": 0.72,
        "critic_suggestion": "HOLD",
        "reasoning": "Modest OOS Sharpe degradation suggests overfit risk",
        "human_decision": "ACCUMULATE",
        "decided_at": "2026-07-20T10:22:00Z"
      },
      "gate_status": {
        "strategy": "quality_momentum_tilt_top3",
        "latest_test_time": "2026-07-20T06:00:00Z",
        "gates": [
          {
            "name": "Out-of-Sample",
            "status": "pass",
            "sharpe_oos": 0.72,
            "sharpe_is": 1.44,
            "degradation_pct": 0.50
          },
          {
            "name": "Monte Carlo",
            "status": "pass",
            "p5_return_pct": 0.021
          },
          {
            "name": "Walk-Forward",
            "status": "pass",
            "pct_positive_windows": 0.62
          },
          {
            "name": "Deflated Sharpe",
            "status": "pass",
            "dsr_probability": 0.985
          }
        ]
      },
      "data_quality": [
        { "category": "Price", "status": "USABLE", "note": "1511 sessions, no gaps" },
        { "category": "Fundamentals", "status": "USABLE", "note": "Q2 2026 from FMP" },
        { "category": "TA indicators", "status": "STALE", "note": "5 days old" }
      ]
    }
  }
}
```

---

## Interactions

### Symbol Sidebar

**Search:**
- Filter by symbol (case-insensitive)
- Real-time as you type
- "No results" if nothing matches

**Favorites toggle:**
- Click star icon to pin/unpin
- Pinned symbols always appear first
- UI only (prototype doesn't persist)

**Click symbol:**
- Switch to that symbol (URL changes to `/my-stocks/{SYMBOL}`)
- Highlight current symbol with background color
- Main view re-renders with new symbol's data

### Position Tab

**Price chart:**
- X-axis: date range (auto-scaled to data)
- Y-axis: price
- Green ▲ markers for entries
- Red ▼ markers for exits
- Hoverable datapoints show exact date/price/shares
- "Last updated" timestamp with manual Refresh button

**Open positions table:**
- Show all active positions
- Click row (future): expand trade details/journal
- "Total open" summary row at bottom

**Closed positions table:**
- Collapsed by default
- Click "Show more history" to expand
- Show historical trades with entry/exit prices and P&L

### Research Tab

**TA chart:**
- Price candlestick (or line)
- Overlays: MA20 (red), MA50 (orange), MA200 (blue), RSI-14 (separate subplot), Bollinger (shaded), ATR (separate)
- Hoverable to see exact values on date
- "Last updated" timestamp with manual Refresh button

**Evidence card:**
- Action, confidence, spec ID, strategy name prominently at top
- Summary paragraph
- Collapsible sections: Supporting Evidence, Risks, Invalidation Conditions
- Links: "[Journal Entry]" "

[View Full Spec]" "[Edit Decision]"

**Critic review:**
- Subordinate styling (smaller font, lighter background)
- Analyst confidence, critic adjustment, final confidence
- Suggestion (HOLD/DEMOTE)
- Human decision and timestamp
- "[View critic details]" (expandable for full reasoning)

**Gate panel:**
- 4 boxes: OOS | MC | WF | DSR, each with status badge (pass/fail)
- Expandable: shows 2–3 key numeric fields (Sharpe, 5%-ile return, etc.)
- "[View full gate logs]" → `/tests` filtered to that spec

### Pending Decision Banner

- High visual weight (amber background, clear typography)
- Entry logic and countdown (e.g., "Entry pending: MSFT Monday 9:30 AM ET — 2 days 4 hours away")
- Single button: "[View thesis details]" → jumps to relevant journal entry or thesis view
- Always-on, not dismissible

---

## Refresh Strategy

- **Price chart**: Fast-interval refresh (5–15 min) — shows "Last updated: 2:47 PM (15 min ago)"
- **TA chart**: Same as price (5–15 min)
- **Evidence card**: 5-min cycle or manual button
- **Gate status**: 5-min cycle (stale after latest test runs)
- **Pending decision**: Immediate (checked on page load, not auto-updated unless websocket exists in production)
- **Manual refresh button**: Pulls latest data for all panels

---

## Edge Cases

### No open positions
- "No open positions. Ready to enter based on research."

### No closed positions
- "No closed positions yet." (closed positions table hidden)

### Pending decision with no thesis
- Banner shows action/countdown, but "[View thesis details]" button disabled

### Data stale (>24h)
- Evidence card shows: "Evidence stale (analyzed 48h ago). [Re-analyze now]"

### Data missing entirely
- Action shows "INSUFFICIENT_DATA"
- Confidence shows "0.0"
- Banner: "Cannot show pending decision — insufficient data"

---

## Accessibility & Mobile

- **Tab order**: Sidebar → top bar buttons → chart → evidence card sections → critic → gates
- **Keyboard**: Arrow keys to scroll, Tab to navigate sections, Enter to expand/collapse
- **Mobile (<640px)**:
  - Sidebar slides out on hamburger click (floating, not taking full width)
  - Tabs stack vertically
  - Chart scales to fit screen width
  - Tables convert to card layout
- **Screen reader**: "NVDA, Nvidia Corp., accumulate action, 72% confidence" + reads full evidence

---

## Prototype Acceptance Criteria

- [ ] Symbol sidebar shows all 14 symbols with search
- [ ] Click sidebar symbol switches main view
- [ ] Pending decision banner shows with countdown
- [ ] Position tab shows clean price chart with entry/exit markers
- [ ] Open positions table displays correctly
- [ ] Research tab shows TA chart with indicators
- [ ] Evidence card renders with all sections
- [ ] Critic review shows with confidence values
- [ ] Gate panel shows 4 gates with pass/fail status
- [ ] Data quality badges show correct status
- [ ] "Last updated" timestamps visible on charts
- [ ] "[Refresh]" button re-renders chart data (prototype: swaps fixture; production: queries API)
- [ ] Click evidence card link items (if any) are safe (may not navigate in prototype)
- [ ] Responsive down to 375px width
- [ ] No broken links to other pages (/tests, /strategies, etc.)

# Strategies Spec

> Hub for viewing strategy specs. Max 5 active specs (typically 2 live + up to 2 challenger + 1 backup). Per-strategy view shows portfolio performance, gate results, and comparison interface.
> Reference: `fixtures/strategies.json`

---

## Purpose

Show **all active and promoted strategy specs**:
- Grid view of all specs (cards with name, status, portfolio value, last activity)
- Deep dive: click a spec to see its portfolio, latest gate results, related decisions
- Compare: side-by-side table of multiple specs (Sharpe, drawdown, win rate, vs VOO)
- Filters: proposed/approved/promoted/demoted specs
- Approve/promote/reject buttons (human-gated actions) live here

---

## Layout

### Main View (Strategy Grid)

```
┌──────────────────────────────────────────────────────────┐
│ research_data | Dashboard | ... Strategies ... [⚙ Settings] │
├──────────────────────────────────────────────────────────┤
│                                                            │
│ Strategies — Active Specs (5 max)                        │
│                                                            │
│ Filter: [All] [Proposed] [Approved] [Promoted] [Demoted] │
│ View: [Grid] [Compare]                                   │
│                                                            │
│ ┌─────────────────────┐ ┌─────────────────────────────┐ │
│ │ quality_momentum    │ │ momentum_only               │ │
│ │ _tilt_top3          │ │                             │ │
│ │                     │ │ Status: Proposed            │ │
│ │ Status: Promoted ✓  │ │ Created: 2026-07-18         │ │
│ │ Created: 2026-07-10 │ │                             │ │
│ │                     │ │ Portfolio value (paper):    │ │
│ │ Portfolio value     │ │ $ 1,200 (+2.1% vs VOO)     │ │
│ │ (paper): $5,430     │ │                             │ │
│ │ (+5.2% vs VOO)      │ │ Latest test: 2026-07-19     │ │
│ │                     │ │ OOS Sharpe: 0.68            │ │
│ │ Latest test:        │ │ Status: FAILED at MC gate   │ │
│ │ 2026-07-20          │ │                             │ │
│ │ All 4 gates: PASS ✓ │ │ [View] [Approve] [Reject]   │ │
│ │                     │ │                             │ │
│ │ Demo-eligible: YES  │ │ [Edit params] [View logs]   │ │
│ │                     │ │                             │ │
│ │ [View] [Compare]    │ │                             │ │
│ │ [Edit params]       │ │                             │ │
│ │ [View logs]         │ │ [Edit params] [View logs]   │ │
│ └─────────────────────┘ └─────────────────────────────┘ │
│                                                            │
│ [... 1–3 more cards if applicable ...]                   │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

### Per-Strategy View (Click "View" on a card)

```
┌──────────────────────────────────────────────────────────┐
│ research_data | Dashboard | ... Strategies ... [⚙ Settings] │
├──────────────────────────────────────────────────────────┤
│                                                            │
│ ◄ quality_momentum_tilt_top3                             │
│                                                            │
│ Status: Promoted ✓  |  Created: 2026-07-10               │
│ [Approve] [Reject] [Demote]  (visible if status allows)  │
│                                                            │
│ ┌────────────────────────────────────────────────────────┐│
│ │ Portfolio Chart (Clean price with entry/exit markers)  ││
│ │ [Chart showing $ value over time, marked trades]       ││
│ │                                                        ││
│ │ Portfolio stats:                                       ││
│ │ • Total return: +5.2%                                 ││
│ │ • vs VOO: +5.2% vs +3.1% (outperformance: +2.1%)     ││
│ │ • Max drawdown: -3.8%                                ││
│ │ • Win rate: 72%                                       ││
│ │ • Sharpe ratio: 0.95                                 ││
│ │ • Last updated: 2:47 PM                               ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ LATEST TEST RESULTS                                    │
│ ┌────────────────────────────────────────────────────────┐│
│ │ Test date: 2026-07-20 06:00 UTC                        ││
│ │ Demo-eligible: YES ✓                                  ││
│ │                                                        ││
│ │ ✓ OOS:  Sharpe 0.72    ✓ MC: 5%-ile +2.1%           ││
│ │ ✓ WF:   62% positive   ✓ DSR: 98.5% prob            ││
│ │                                                        ││
│ │ [View full gate logs →]                               ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ STRATEGY DETAILS                                        │
│ ┌────────────────────────────────────────────────────────┐│
│ │ Universe: All 14 symbols                               ││
│ │ Rebalance: Monthly                                     ││
│ │ Holdings: Top 3 by (0.5 × momentum + 0.5 × quality)   ││
│ │                                                        ││
│ │ Parameters:                                            ││
│ │ • momentum_window: 252 days                           ││
│ │ • quality_weight: 0.50                                ││
│ │ • momentum_weight: 0.50                               ││
│ │ • rebalance_cost: 5 bps/side                          ││
│ │                                                        ││
│ │ [Edit params] [View hook code]                        ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ [View full decision log] [View related tests]            │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

### Compare View (Tab or Modal)

```
┌──────────────────────────────────────────────────────────┐
│ Strategies — Compare                                      │
│                                                            │
│ Select specs: [☑ quality_momentum_tilt_top3]             │
│              [☑ momentum_only]                            │
│              [☐ qual_val_tilt]                            │
│                                                            │
│ ┌──────────────────────────────────────────────────────┐│
│ │ Metric                │ Spec A │ Spec B │ Spec C     ││
│ ├──────────────────────────────────────────────────────┤│
│ │ Status                │ Promoted│Proposed│  —        ││
│ │ Demo-eligible         │ YES     │ NO      │  —        ││
│ │ Sharpe (latest)       │ 0.95    │ 0.68    │  —        ││
│ │ OOS Sharpe (latest)   │ 0.72    │ 0.60    │  —        ││
│ │ Max drawdown          │ -3.8%   │ -6.2%   │  —        ││
│ │ Win rate (paper)      │ 72%     │ 58%     │  —        ││
│ │ Return (paper)        │ +5.2%   │ +2.1%   │  —        ││
│ │ vs VOO outperf        │ +2.1%   │ -1.0%   │  —        ││
│ │ Last test             │ 2026-07-20│ 2026-07-19│ —    ││
│ │ Tests passed / total  │ 5 / 7   │ 3 / 8   │  —        ││
│ │                                                      ││
│ │ [Download CSV] [Print]                              ││
│ └──────────────────────────────────────────────────────┘│
│                                                            │
└──────────────────────────────────────────────────────────┘
```

---

## Component Tree

```
StrategiesPage
├── Header (global)
├── PageTitle: "Strategies — Active Specs"
├── FilterBar
│   ├── StatusFilter (All | Proposed | Approved | Promoted | Demoted)
│   └── ViewToggle (Grid | Compare)
├── MainView
│   ├── IF Grid View:
│   │   └── StrategyGrid
│   │       └── StrategyCard × ≤5
│   │           ├── SpecNameHeader
│   │           ├── StatusBadge
│   │           ├── CreatedDate
│   │           ├── PortfolioValue
│   │           ├── ReturnPercent
│   │           ├── LatestTestSummary
│   │           ├── GateStatus (pass/fail indicator)
│   │           ├── DemoEligibleBadge
│   │           └── ActionButtons ([View] [Compare] [Edit] [Logs])
│   │
│   └── IF Compare View:
│       └── CompareTable
│           ├── SelectCheckboxes (top)
│           └── TableRows (Sharpe, drawdown, win rate, etc.)
│
├── DetailView (when viewing one strategy)
│   ├── BackButton
│   ├── SpecHeader (name, status, created date)
│   ├── ActionButtons (context-sensitive: Approve/Reject/Demote)
│   ├── PortfolioChart (clean price + markers)
│   ├── PortfolioStatsPanel
│   ├── LatestTestPanel (gate results)
│   ├── StrategyDetailsPanel (params, holdings logic)
│   └── ExpandableLogSection (decision history)
```

---

## Data Shape (Fixture Excerpt)

```json
{
  "strategies": {
    "as_of": "2026-07-20T14:30:00Z",
    "total_specs": 3,
    "specs": [
      {
        "spec_id": "5f003778-42bc-4d8a-ac12-839699d98a02",
        "name": "quality_momentum_tilt_top3",
        "status": "PROMOTED",
        "created_at": "2026-07-10T08:00:00Z",
        "description": "Top-3 by (0.5 × momentum + 0.5 × quality) composite, rebalanced monthly",
        "universe": "all_14",
        "rebalance_frequency": "monthly",
        "parameters": {
          "momentum_window_days": 252,
          "quality_weight": 0.50,
          "momentum_weight": 0.50,
          "holding_count": 3,
          "rebalance_cost_bps": 5
        },
        "paper_trading": {
          "portfolio_value": 5430,
          "return_pct": 0.052,
          "voo_return_pct": 0.031,
          "outperformance_pct": 0.021,
          "max_drawdown_pct": -0.038,
          "win_rate": 0.72,
          "sharpe": 0.95,
          "last_updated": "2026-07-20T14:15:00Z",
          "trades": [
            { "date": "2026-07-10", "type": "entry", "symbol": "NVDA", "shares": 50, "price": 110.25 },
            { "date": "2026-07-15", "type": "entry", "symbol": "MSFT", "shares": 30, "price": 115.00 }
            // ... more
          ]
        },
        "latest_test": {
          "test_date": "2026-07-20T06:00:00Z",
          "demo_eligible": true,
          "gates": [
            {
              "gate_number": 1,
              "gate_name": "Out-of-Sample",
              "status": "PASS",
              "sharpe_oos": 0.72
            },
            {
              "gate_number": 2,
              "gate_name": "Monte Carlo",
              "status": "PASS",
              "p5_return_pct": 0.021
            },
            {
              "gate_number": 3,
              "gate_name": "Walk-Forward",
              "status": "PASS",
              "pct_positive": 0.62
            },
            {
              "gate_number": 4,
              "gate_name": "Deflated Sharpe",
              "status": "PASS",
              "dsr_probability": 0.985
            }
          ]
        },
        "decisions": [
          {
            "decision_id": "decision-001",
            "decision": "PROMOTED",
            "decided_by": "anant",
            "decided_at": "2026-07-20T10:22:00Z",
            "reasoning": "All gates passed, ready for live paper"
          }
        ],
        "portfolio_chart_data": [
          { "date": "2026-07-10", "value": 10000 },
          { "date": "2026-07-11", "value": 10150 },
          // ... 40+ points
        ]
      },
      {
        "spec_id": "a2f8c9d1-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "name": "momentum_only",
        "status": "PROPOSED",
        "created_at": "2026-07-18T14:00:00Z",
        "description": "Pure momentum play, top-5 by 12-1 returns",
        "universe": "all_14",
        "rebalance_frequency": "monthly",
        "parameters": {
          "momentum_window_days": 252,
          "holding_count": 5,
          "rebalance_cost_bps": 5
        },
        "paper_trading": {
          "portfolio_value": 1200,
          "return_pct": 0.021,
          "voo_return_pct": 0.031,
          "outperformance_pct": -0.010,
          "max_drawdown_pct": -0.062,
          "win_rate": 0.58,
          "sharpe": 0.68,
          "last_updated": "2026-07-20T14:15:00Z",
          "trades": []
        },
        "latest_test": {
          "test_date": "2026-07-19T23:45:00Z",
          "demo_eligible": false,
          "gates": [
            {
              "gate_number": 1,
              "gate_name": "Out-of-Sample",
              "status": "PASS",
              "sharpe_oos": 0.60
            },
            {
              "gate_number": 2,
              "gate_name": "Monte Carlo",
              "status": "FAIL",
              "p5_return_pct": -0.032
            },
            {
              "gate_number": 3,
              "gate_name": "Walk-Forward",
              "status": "NOT_RUN",
              "pct_positive": null
            },
            {
              "gate_number": 4,
              "gate_name": "Deflated Sharpe",
              "status": "NOT_RUN",
              "dsr_probability": null
            }
          ]
        },
        "decisions": [
          {
            "decision_id": "decision-002",
            "decision": "REJECTED",
            "decided_by": "critic_model",
            "decided_at": "2026-07-19T19:15:00Z",
            "reasoning": "Failed MC gate; 5th-percentile return negative"
          }
        ],
        "portfolio_chart_data": []
      }
    ]
  }
}
```

---

## Interactions

### Filter Bar

**Status filter:**
- All | Proposed | Approved | Promoted | Demoted
- Updates grid in real-time

**View toggle:**
- Grid | Compare
- Swaps main view

### Strategy Cards (Grid View)

**Click [View]:**
- Navigate to per-strategy detailed view

**Click [Compare]:**
- Switch to Compare view with this spec pre-selected
- Shows checkboxes to add/remove other specs from comparison

**Click [Edit params]:**
- Opens modal or panel to edit strategy parameters
- Prototype: read-only (no actual edits); production: save to DB

**Click [View logs]:**
- Navigates to decision log for this spec (show all decisions ever made on it)

### Per-Strategy View

**Status badge:**
- PROPOSED = orange
- APPROVED = blue
- PROMOTED = green ✓
- DEMOTED = red X

**Action buttons (context-sensitive):**
- If PROPOSED: [Approve] [Reject]
- If APPROVED: [Promote] [Reject]
- If PROMOTED: [Demote]
- If DEMOTED: [—] (read-only)

**Portfolio chart:**
- Shows $ value over time
- Green ▲ for entry markers (when trades execute)
- Red ▼ for exit markers
- Hoverable to see exact date/value

**Portfolio stats:**
- Return %, outperformance vs VOO, max drawdown, win rate, Sharpe
- Compared to paper baseline (VOO)

**Gate status:**
- Shows all 4 gates with pass/fail badges
- Click to expand gate details
- Link to `/tests` filtered to this spec

**Action buttons:**
- [View full decision log] → shows all decisions on this spec
- [View related tests] → `/tests` filtered to this spec

### Compare View

**Checkboxes (top):**
- Select which specs to compare
- Table updates dynamically

**Table:**
- Side-by-side comparison of key metrics
- Highlight best performer per metric (optional)
- Sort by column header (future)

**Export:**
- [Download CSV] (future)

---

## Refresh Strategy

- **Initial load**: Fetch all specs (grid view) or one spec (detail view)
- **Portfolio chart**: 5–15 min interval (if live paper trading is active)
- **Gate results**: 5-min cycle (re-fetch latest test)
- **Manual refresh**: Button in header
- **Compare view**: Real-time (filters existing data from initial fetch)

---

## Edge Cases

### No specs yet
- "No strategy specs yet. Create one in Brain-Journal or Bots-Hub."

### Spec with no paper trades
- Portfolio value shows "0" or "Not yet trading"
- Portfolio chart is empty

### Spec with no test results
- Gate panel shows: "Not yet tested. Trigger a backtest from Bots-Hub."

### Spec proposed but no decision yet
- Action buttons: [Approve] [Reject] (Promote/Demote unavailable)

### All 5 slots filled
- Add new spec button disabled or shows: "Max 5 specs. Retire one to add another."

---

## Accessibility & Mobile

- **Tab order**: Filter bar → strategy cards (grid) → view buttons → compare table
- **Keyboard**: Arrow keys to navigate cards, Enter to view
- **Mobile (<640px)**:
  - Grid becomes single column
  - Cards stack vertically
  - Compare table becomes scrollable horizontally or collapses to one metric per row
- **Screen reader**: "quality_momentum_tilt_top3, promoted, created July 10, portfolio value $5,430, return +5.2%" + reads action buttons

---

## Prototype Acceptance Criteria

- [ ] All active specs display as cards in grid (≤5)
- [ ] Status filter works (shows only selected statuses)
- [ ] View toggle switches between Grid and Compare
- [ ] Click [View] navigates to per-strategy detail page
- [ ] Status badge shows correct color per status
- [ ] Portfolio stats display correctly (return %, Sharpe, etc.)
- [ ] Gate panel shows 4 gates with pass/fail status
- [ ] Action buttons appear correctly (context-sensitive per status)
- [ ] Portfolio chart renders with entry/exit markers
- [ ] Compare view shows side-by-side table with correct metrics
- [ ] Checkboxes work to toggle specs in compare view
- [ ] Back button on detail view returns to grid
- [ ] Responsive down to 375px
- [ ] No broken links to related pages (/tests, /decisions, etc.)

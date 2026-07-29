# Tests Spec

> Append-only log of all strategy test runs. Each row = one complete 4-gate test. Click to see gate diagnostics and journal entry.
> Reference: `fixtures/tests.json`

---

## Purpose

Show **the history of every backtest** that has run:
- Which spec was tested
- When it was tested
- Overall result (passed all 4 gates or failed at which gate)
- Promote/demote decision (if any)
- Click to see gate-by-gate diagnostics and linked journal entry

---

## Layout

```
┌──────────────────────────────────────────────────────────┐
│ research_data | Dashboard | Tests | ...      [⚙ Settings] │
├──────────────────────────────────────────────────────────┤
│                                                            │
│ Tests — All Strategy Backtest Runs                      │
│                                                            │
│ Filter: [All ▼] [Symbol: ___] [Status: ___] [Date range] │
│                                                            │
│ Showing 1–25 of 47 test runs (page 1/2)                  │
│                                                            │
│ ┌──────────────────────────────────────────────────────┐│
│ │ Date      │ Spec │ Symbol │ Status │ Gate │ Decision ││
│ ├──────────────────────────────────────────────────────┤│
│ │ 2026-07-20│ qual │ NVDA   │ ✓ PASS │  —   │ PROMOTED ││
│ │ 06:00 UTC │ ity_ │        │        │      │ (decision)││
│ │           │ momen│        │        │      │ at 10:22 ││
│ │           │      │        │        │      │          ││
│ │ 2026-07-19│ qual │ MSFT   │ ✗ FAIL │ OOS  │ —        ││
│ │ 23:45 UTC │ ity_ │        │ OOS    │      │          ││
│ │           │ momen│        │        │      │          ││
│ │           │      │        │        │      │          ││
│ │ 2026-07-19│ mome │ JPM    │ ✗ FAIL │ MC   │ REJECTED ││
│ │ 18:30 UTC │ ntum │        │ MC     │      │ by critic││
│ │           │ _only│        │        │      │ (conf too││
│ │           │      │        │        │      │ low)     ││
│ │                                                        ││
│ │ [Click row to expand details ↓]                       ││
│ │                                                        ││
│ └──────────────────────────────────────────────────────┘│
│                                                            │
│ Pagination: [< Prev] [1] [2] [Next >]                   │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

---

### Expanded Row (Click to Reveal)

```
┌──────────────────────────────────────────────────────────┐
│ Test Run: quality_momentum_tilt_top3 (NVDA)             │
│ Date: 2026-07-20 06:00 UTC                              │
├──────────────────────────────────────────────────────────┤
│                                                            │
│ ▼ GATE-BY-GATE RESULTS                                  │
│                                                            │
│ ✓ Gate 1: Out-of-Sample                                 │
│   OOS Net Sharpe: 0.72  (Threshold: > 0.5 × IS)        │
│   OOS Return: +15.3% ann  (Threshold: > 0)              │
│   Degradation: 50% (IS Sharpe: 1.44)                   │
│   Status: PASSED                                         │
│                                                            │
│ ✓ Gate 2: Monte Carlo                                   │
│   5th-percentile return: +2.1% ann  (Threshold: > 0)   │
│   Bootstrap paths: 1000                                  │
│   Status: PASSED                                         │
│                                                            │
│ ✓ Gate 3: Walk-Forward                                  │
│   % windows positive: 62%  (Threshold: ≥ 60%)          │
│   Pooled OOS Sharpe: 0.68  (Threshold: > 0)            │
│   Rolling windows: 504 / 126 bars                        │
│   Status: PASSED                                         │
│                                                            │
│ ✓ Gate 4: Deflated Sharpe                               │
│   DSR probability: 98.5%  (Threshold: ≥ 95%)           │
│   Trial count: 24 (recorded brain test runs)            │
│   Status: PASSED                                         │
│                                                            │
│ ▼ OVERALL RESULT: ALL 4 GATES PASSED ✓                │
│   Demo-eligible: YES                                     │
│   Candidate for promotion                               │
│                                                            │
│ ▼ LINKED JOURNAL ENTRY                                  │
│ ┌────────────────────────────────────────────────────────┐│
│ │ [Test Success Template]                               ││
│ │ Date: 2026-07-20 06:45 UTC                            ││
│ │ Title: "quality_momentum_tilt_top3 passed all gates"   ││
│ │ Tags: #promotion, #nvda, #quality-momentum            ││
│ │                                                        ││
│ │ Entry excerpt:                                        ││
│ │ "Spec passed OOS/MC/WF/DSR. Outperformance           ││
│ │  vs VOO solid. Ready for paper trial..."              ││
│ │                                                        ││
│ │ [View full entry →]                                   ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ PROMOTION DECISION (if any)                            │
│ ┌────────────────────────────────────────────────────────┐│
│ │ Decision: PROMOTED (by anant, 2026-07-20 10:22 UTC)  ││
│ │ Reasoning: All gates passed, live proof ready.        ││
│ │ Next step: paper trading                              ││
│ │                                                        ││
│ │ [View decision record →]                              ││
│ └────────────────────────────────────────────────────────┘│
│                                                            │
└──────────────────────────────────────────────────────────┘
```

---

## Component Tree

```
TestsPage
├── Header (global)
├── PageTitle: "Tests — All Strategy Backtest Runs"
├── FilterBar
│   ├── StatusFilter (All | Pass | Fail)
│   ├── GateFilter (All | OOS | MC | WF | DSR)
│   ├── SymbolFilter (dropdown/search)
│   └── DateRangeFilter (Last 7d / 30d / All)
├── Table
│   ├── TableHeader (Date | Spec | Symbol | Status | Gate | Decision)
│   └── TableRow × N (expandable)
│       ├── DateCell
│       ├── SpecNameCell
│       ├── SymbolCell
│       ├── StatusBadge (PASS/FAIL)
│       ├── GateCell (which gate it failed at, or "—" if all pass)
│       ├── DecisionBadge (PROMOTED/REJECTED/—)
│       └── ExpandButton (click to reveal gate diagnostics)
├── ExpandedDetails (hidden until row clicked)
│   ├── GateDiagnosticsPanel × 4
│   ├── OverallResultPanel
│   ├── LinkedJournalEntryPanel
│   └── PromotionDecisionPanel (if exists)
└── Pagination (25 rows per page)
```

---

## Data Shape (Fixture Excerpt)

```json
{
  "tests": {
    "as_of": "2026-07-20T14:30:00Z",
    "total_count": 47,
    "page": 1,
    "page_size": 25,
    "runs": [
      {
        "test_id": "test-run-001",
        "spec_id": "5f003778-42bc-4d8a-ac12-839699d98a02",
        "spec_name": "quality_momentum_tilt_top3",
        "symbol": "NVDA",
        "test_date": "2026-07-20T06:00:00Z",
        "overall_status": "PASS",
        "demo_eligible": true,
        "failed_at_gate": null,
        "gates": [
          {
            "gate_number": 1,
            "gate_name": "Out-of-Sample",
            "status": "PASS",
            "metrics": {
              "oos_net_sharpe": 0.72,
              "oos_net_sharpe_threshold": 0.72,
              "oos_return_pct": 0.153,
              "oos_return_threshold": 0,
              "is_sharpe": 1.44,
              "degradation_pct": 0.50
            }
          },
          {
            "gate_number": 2,
            "gate_name": "Monte Carlo",
            "status": "PASS",
            "metrics": {
              "p5_return_pct": 0.021,
              "p5_return_threshold": 0,
              "bootstrap_paths": 1000
            }
          },
          {
            "gate_number": 3,
            "gate_name": "Walk-Forward",
            "status": "PASS",
            "metrics": {
              "pct_positive_windows": 0.62,
              "pct_positive_threshold": 0.60,
              "pooled_oos_sharpe": 0.68,
              "pooled_oos_sharpe_threshold": 0,
              "rolling_window_train": 504,
              "rolling_window_test": 126
            }
          },
          {
            "gate_number": 4,
            "gate_name": "Deflated Sharpe",
            "status": "PASS",
            "metrics": {
              "dsr_probability": 0.985,
              "dsr_probability_threshold": 0.95,
              "trial_count": 24
            }
          }
        ],
        "linked_journal_entry": {
          "entry_id": "journal-entry-123",
          "template": "Test Success",
          "date": "2026-07-20T06:45:00Z",
          "title": "quality_momentum_tilt_top3 passed all gates",
          "tags": ["promotion", "nvda", "quality-momentum"],
          "excerpt": "Spec passed OOS/MC/WF/DSR. Outperformance vs VOO solid. Ready for paper trial..."
        },
        "promotion_decision": {
          "status": "PROMOTED",
          "decided_by": "anant",
          "decided_at": "2026-07-20T10:22:00Z",
          "reasoning": "All gates passed, live proof ready."
        }
      },
      {
        "test_id": "test-run-002",
        "spec_id": "a2f8c9d1-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "spec_name": "momentum_only",
        "symbol": "JPM",
        "test_date": "2026-07-19T18:30:00Z",
        "overall_status": "FAIL",
        "demo_eligible": false,
        "failed_at_gate": 2,
        "gates": [
          {
            "gate_number": 1,
            "gate_name": "Out-of-Sample",
            "status": "PASS",
            "metrics": { /* ... */ }
          },
          {
            "gate_number": 2,
            "gate_name": "Monte Carlo",
            "status": "FAIL",
            "metrics": {
              "p5_return_pct": -0.032,
              "p5_return_threshold": 0,
              "bootstrap_paths": 1000,
              "failure_reason": "5th-percentile return negative"
            }
          },
          {
            "gate_number": 3,
            "gate_name": "Walk-Forward",
            "status": "NOT_RUN",
            "metrics": null
          },
          {
            "gate_number": 4,
            "gate_name": "Deflated Sharpe",
            "status": "NOT_RUN",
            "metrics": null
          }
        ],
        "linked_journal_entry": {
          "entry_id": "journal-entry-456",
          "template": "Test Failure",
          "date": "2026-07-19T19:00:00Z",
          "title": "momentum_only failed at Monte Carlo gate",
          "tags": ["failure", "jpm", "momentum-only"],
          "excerpt": "5th-percentile return came in negative (-3.2%). Strategy too volatile for this universe subset..."
        },
        "promotion_decision": {
          "status": "REJECTED",
          "decided_by": "critic_model",
          "decided_at": "2026-07-19T19:15:00Z",
          "reasoning": "Confidence too low after critic adjustment; failed MC gate suggests tail risk not addressed."
        }
      }
      // 45 more...
    ]
  }
}
```

---

## Interactions

### Filter Bar

**Status filter:**
- All | Pass (✓) | Fail (✗)
- Updates table in real-time

**Gate filter:**
- All | OOS (Gate 1) | MC (Gate 2) | WF (Gate 3) | DSR (Gate 4)
- Shows only tests that failed at that gate (or passed all if "All" selected)

**Symbol filter:**
- Dropdown/search input
- Filter to one symbol or leave blank for all

**Date range filter:**
- Last 7 days | Last 30 days | All
- Or custom date picker (future)

### Table Rows

**Click row:**
- Expands to show gate diagnostics, linked journal entry, promotion decision
- Only one row expanded at a time (clicking another collapses the first)
- Or: Accordion behavior (multiple can be open)

**Row styling:**
- PASS rows: light green background
- FAIL rows: light red background
- Hover: slight shadow/elevation

**Status badge:**
- ✓ PASS = green
- ✗ FAIL = red

**Decision badge:**
- PROMOTED = green checkmark
- REJECTED = red X
- — (no decision yet) = gray dash

### Expanded Details

**Gate panels:**
- Collapsible (click gate name to toggle)
- Shows 2–3 key numeric fields vs threshold
- Failure details if gate failed
- Formula/explanation (optional, for learning)

**Overall result banner:**
- Bold "ALL 4 GATES PASSED ✓" or "FAILED AT GATE X"
- Demo-eligible: YES/NO

**Journal entry panel:**
- Shows template type, date, title, tags
- Excerpt (first 2–3 lines)
- "[View full entry →]" link to `/brain-journal?entry={entry_id}`

**Promotion decision panel:**
- Status (PROMOTED/REJECTED)
- Decided by (human name or critic_model)
- Timestamp
- Reasoning text

---

## Refresh Strategy

- **Initial load**: Fetch all test runs (paginated), most-recent-first
- **New test completes**: Re-fetch and show at top of page (or notify user to refresh)
- **Manual refresh**: Button in header or page-level refresh
- **No auto-refresh** (tests are append-only, no mid-test updates)

---

## Edge Cases

### No tests yet
- "No test runs yet. Trigger a backtest from Bots-Hub to start."

### Test with no promotion decision
- Promotion decision panel shows: "Pending human review. [Go to Strategies to decide]"

### Test with no linked journal entry
- Journal panel shows: "Journal entry not yet created. [Create entry]"

### Test failed, but no explicit reason recorded
- Gate panel shows failure status but metrics might be sparse
- Shows "Failure details not logged" with a note to check Bots-Hub logs

### Very old test (>6 months)
- Row can be archived/hidden by default, with a link to show older tests

---

## Accessibility & Mobile

- **Tab order**: Filter inputs → table rows → expand buttons
- **Keyboard**: Arrow keys to move between rows, Enter to expand/collapse
- **Mobile (<640px)**:
  - Filters stack vertically
  - Table becomes scrollable horizontally or converts to card layout (one run per card)
  - Expanded details take full width below card
- **Screen reader**: "quality_momentum_tilt_top3, NVDA, passed all 4 gates, promoted on July 20" + reads gate metrics

---

## Prototype Acceptance Criteria

- [ ] All test runs display in table (paginated 25/page)
- [ ] Rows sorted by date descending (most recent first)
- [ ] Click row expands to show gate diagnostics
- [ ] Gate panels display with correct metrics and thresholds
- [ ] Status badges (PASS/FAIL) show correct colors
- [ ] Decision badges (PROMOTED/REJECTED) show when applicable
- [ ] Filters work (status, gate, symbol, date)
- [ ] "Failed at gate X" shows correctly (gate number, not passed gates)
- [ ] Overall result banner shows for expanded row
- [ ] Journal entry panel shows excerpt and link
- [ ] Promotion decision panel shows decision status and reasoning
- [ ] "[View full entry →]" links are safe (may not navigate in prototype)
- [ ] Responsive down to 375px
- [ ] Pagination controls work (or fixture shows <25 runs)

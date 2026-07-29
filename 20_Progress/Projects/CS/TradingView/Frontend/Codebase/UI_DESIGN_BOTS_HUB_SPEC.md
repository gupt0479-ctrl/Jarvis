# Bots-Hub Spec

> Operations center for all backend agents and ingestion. 2D swarm visualization of agents, unified logs with per-agent views, and manual triggers for analysis/testing/ingest.
> Reference: `fixtures/bots-hub.json`

---

## Purpose

Show **what the AI and automation are doing right now**:
- **Swarm view**: 2D nodes-and-edges showing agent states (running/idle/complete) — not a particle system, but colored nodes animated by state
- **Unified logs**: All-agent timeline view, filterable by agent/status/date
- **Per-agent tabs**: Alternative view grouped by agent (Ingestion | Analysis | Testing | Paper Trading)
- **Manual triggers**: Buttons to run ingest, re-analyze a symbol, start a gate test, etc.
- **No human decisions here** — only triggers and visibility; approvals/promotions happen in other pages

---

## Layout

```
┌──────────────────────────────────────────────────────────┐
│ research_data | Dashboard | ... Bots-Hub | [⚙ Settings]  │
├──────────────────────────────────────────────────────────┤
│                                                            │
│ Bots-Hub — AI Operations                                 │
│ [← Sidebar toggle]                                        │
│                                                            │
│ ┌──────────────────────────────────────────────────────┐│
│ │ AGENT SWARM (2D network, animated by state)         ││
│ │                                                      ││
│ │       [🟢 Ingest-Bot]                               ││
│ │              |                                      ││
│ │    [🟡 Analyst]--[🔵 Critic]                        ││
│ │      |              |                               ││
│ │   [🟢 FactorEngine] [🟢 GateRunner]                 ││
│ │      |              |                               ││
│ │   [🟢 PaperEngine]--[🟡 (3 positions open)]         ││
│ │                                                      ││
│ │ Legend:                                             ││
│ │ 🟢 Idle/Healthy  |  🟡 Running/Active  |  🔵 Complete││
│ │ Last update: 2:47 PM                                ││
│ │                                                      ││
│ └──────────────────────────────────────────────────────┘│
│                                                            │
│ [Floating Sidebar ↙]                                      │
│ ┌─────────────────────┐                                   │
│ │ SIDEBAR TABS        │                                   │
│ │ (click to swap)     │                                   │
│ │                     │                                   │
│ │ [Ingestion]         │                                   │
│ │ [Analysis]          │                                   │
│ │ [Testing]           │                                   │
│ │ [Paper Trading]     │                                   │
│ │ [Logs (unified)]    │                                   │
│ │                     │                                   │
│ └─────────────────────┘                                   │
│                                                            │
│ ┌──────────────────────────────────────────────────────┐│
│ │ SIDEBAR CONTENT (example: Ingestion tab)             ││
│ │                                                      ││
│ │ Polygon: Last run 3h ago                            ││
│ │ Status: ✓ Healthy (14 symbols ingested)             ││
│ │ Next run: In 2h 15min                               ││
│ │ [Run now] (lightweight confirm dialog)              ││
│ │                                                      ││
│ │ Tiingo: Last run 5h ago                             ││
│ │ Status: ✓ Healthy (14 symbols ingested)             ││
│ │ Next run: In 42min                                  ││
│ │ [Run now]                                           ││
│ │                                                      ││
│ │ FMP: Last run 1h ago                                ││
│ │ Status: ✓ Healthy (10/14 symbols, BRKB: SEC only)  ││
│ │ Next run: In 8h 0min                                ││
│ │ [Run now]                                           ││
│ │                                                      ││
│ │ ─────────────────────────────────────────────────   ││
│ │                                                      ││
│ │ [Run all ingestion] (confirm: will take ~30 min)    ││
│ │                                                      ││
│ └──────────────────────────────────────────────────────┘│
│                                                            │
└──────────────────────────────────────────────────────────┘
```

---

## Component Tree

```
BotsHubPage
├── Header (global)
├── PageTitle: "Bots-Hub — AI Operations"
├── SidebarToggle (← arrow, left side)
├── MainView
│   ├── SwarmVisualization (2D network, agent nodes colored by state)
│   │   ├── Node × N (Ingest-Bot, Analyst, Critic, FactorEngine, GateRunner, PaperEngine)
│   │   │   └── State: IDLE (green), RUNNING (yellow), COMPLETE (blue)
│   │   ├── Edge × M (connections showing data flow)
│   │   ├── PanZoomControls (drag, scroll to zoom)
│   │   └── LastUpdateTimestamp
│   │
│   └── Sidebar (floating, triggered by toggle)
│       ├── TabBar (Ingestion | Analysis | Testing | Paper Trading | Logs)
│       └── TabContent (below TabBar)
│           ├── IngestionTab: Provider status lines + [Run now] buttons
│           ├── AnalysisTab: Analyst/Critic status + [Analyze symbol X] button
│           ├── TestingTab: Active/queued gate tests + [Run test] button
│           ├── PaperTradingTab: Pending theses + current positions + [Execute trade] button
│           └── LogsTab: Unified timeline (all agents) + filters + per-agent view
```

---

## Data Shape (Fixture Excerpt)

```json
{
  "bots_hub": {
    "as_of": "2026-07-20T14:30:00Z",
    "swarm": {
      "agents": [
        {
          "agent_id": "ingest-bot",
          "name": "Ingest-Bot",
          "description": "Fetches OHLCV data from Polygon/Tiingo/FMP",
          "state": "IDLE",
          "last_activity": "2026-07-20T11:30:00Z",
          "position": { "x": 200, "y": 100 },
          "color": "green"
        },
        {
          "agent_id": "analyst",
          "name": "Analyst",
          "description": "Generates evidence cards from factor scores",
          "state": "RUNNING",
          "last_activity": "2026-07-20T14:28:00Z",
          "position": { "x": 100, "y": 250 },
          "color": "yellow",
          "current_task": "Analyzing NVDA"
        },
        {
          "agent_id": "critic",
          "name": "Critic",
          "description": "Reviews analyst cards, suggests holds/demotes",
          "state": "IDLE",
          "last_activity": "2026-07-20T14:20:00Z",
          "position": { "x": 300, "y": 250 },
          "color": "green"
        },
        {
          "agent_id": "factor-engine",
          "name": "FactorEngine",
          "description": "Computes momentum, quality, safety, valuation scores",
          "state": "IDLE",
          "last_activity": "2026-07-20T10:00:00Z",
          "position": { "x": 50, "y": 400 },
          "color": "green"
        },
        {
          "agent_id": "gate-runner",
          "name": "GateRunner",
          "description": "Runs 4-gate backtest harness",
          "state": "COMPLETE",
          "last_activity": "2026-07-20T06:00:00Z",
          "position": { "x": 350, "y": 400 },
          "color": "blue"
        },
        {
          "agent_id": "paper-engine",
          "name": "PaperEngine",
          "description": "Executes pre-approved thesis auto-entries/exits",
          "state": "IDLE",
          "last_activity": "2026-07-20T09:15:00Z",
          "position": { "x": 200, "y": 500 },
          "color": "green"
        }
      ],
      "edges": [
        {
          "from_agent_id": "ingest-bot",
          "to_agent_id": "factor-engine",
          "label": "OHLCV → scores"
        },
        {
          "from_agent_id": "factor-engine",
          "to_agent_id": "analyst",
          "label": "scores → card"
        },
        {
          "from_agent_id": "analyst",
          "to_agent_id": "critic",
          "label": "card → review"
        },
        {
          "from_agent_id": "critic",
          "to_agent_id": "gate-runner",
          "label": "decision → backtest"
        }
      ]
    },
    "sidebar": {
      "ingestion": {
        "providers": [
          {
            "provider": "Polygon",
            "status": "healthy",
            "last_run": "2026-07-20T11:30:00Z",
            "symbols_count": 14,
            "next_run_scheduled": "2026-07-20T14:00:00Z",
            "seconds_until_next": 1380
          },
          {
            "provider": "Tiingo",
            "status": "healthy",
            "last_run": "2026-07-20T09:30:00Z",
            "symbols_count": 14,
            "next_run_scheduled": "2026-07-20T15:00:00Z",
            "seconds_until_next": 1800
          },
          {
            "provider": "FMP",
            "status": "healthy",
            "last_run": "2026-07-20T13:00:00Z",
            "symbols_count": 10,
            "next_run_scheduled": "2026-07-21T05:00:00Z",
            "seconds_until_next": 56400,
            "note": "BRKB uses SEC (free tier covers)"
          }
        ]
      },
      "analysis": {
        "analyst_status": "RUNNING",
        "current_task": "Analyzing NVDA (confidence: 72%)",
        "progress_pct": 45,
        "estimated_time_remaining": 120,
        "queued_symbols": ["MSFT", "GOOGL"],
        "can_trigger_manual": true,
        "available_symbols": ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN"]
      },
      "testing": {
        "active_tests": [
          {
            "test_id": "test-run-quality-momt-nvda",
            "spec_name": "quality_momentum_tilt_top3",
            "symbol": "NVDA",
            "status": "COMPLETE",
            "completed_at": "2026-07-20T06:00:00Z",
            "result": "PASS (all 4 gates)",
            "decision_made": "PROMOTED by anant"
          }
        ],
        "queued_tests": [
          {
            "test_id": "test-run-momentum-only-jpm",
            "spec_name": "momentum_only",
            "symbol": "JPM",
            "status": "QUEUED",
            "position_in_queue": 1
          }
        ],
        "can_trigger_manual": true,
        "available_specs": ["quality_momentum_tilt_top3", "momentum_only"]
      },
      "paper_trading": {
        "pending_theses": [
          {
            "thesis_id": "thesis-nvda-001",
            "symbol": "NVDA",
            "action": "ACCUMULATE",
            "trigger_logic": "Monday 9:30 AM ET",
            "entry_price_target": null,
            "status": "pending_market_open"
          }
        ],
        "active_positions": [
          {
            "symbol": "MSFT",
            "entry_date": "2026-07-10",
            "entry_price": 115.00,
            "shares": 30,
            "current_price": 119.50,
            "current_value": 3585,
            "pnl_pct": 0.039
          }
        ]
      },
      "logs": {
        "unified": [
          {
            "timestamp": "2026-07-20T14:28:00Z",
            "agent": "Analyst",
            "action": "Started analyzing",
            "subject": "NVDA",
            "status": "RUNNING",
            "details": "Confidence cap by quality (0.75)"
          },
          {
            "timestamp": "2026-07-20T14:20:00Z",
            "agent": "Critic",
            "action": "Review complete",
            "subject": "MSFT evidence card",
            "status": "SUCCESS",
            "details": "Confidence adjusted -0.03 (modest OOS degradation)"
          },
          {
            "timestamp": "2026-07-20T11:30:00Z",
            "agent": "Ingest-Bot",
            "action": "Ingested",
            "subject": "Polygon (14 symbols)",
            "status": "SUCCESS",
            "details": "All prices current, no gaps"
          }
          // more...
        ],
        "per_agent": {
          "ingest-bot": [
            // Ingest-Bot logs only
          ],
          "analyst": [
            // Analyst logs only
          ]
          // etc.
        }
      }
    }
  }
}
```

---

## Interactions

### Swarm Visualization

**Click/hover a node:**
- Highlight the node
- Show tooltip: agent name, state, last activity timestamp
- Click shows brief status popup (similar to Brain graph)

**Hover an edge:**
- Highlight the edge and both connected nodes
- Show label: relationship (OHLCV → scores, etc.)

**Pan/zoom:**
- Drag to pan
- Scroll to zoom in/out
- Double-click to reset

**State colors:**
- 🟢 IDLE/HEALTHY = green (no activity, last update was normal)
- 🟡 RUNNING/ACTIVE = yellow (currently processing)
- 🔵 COMPLETE = blue (finished task, waiting for next queue)
- 🔴 ERROR/FAILED = red (something went wrong)

**Animation:**
- Pulsing glow on agents with state RUNNING (subtle)
- No particle swarm; 2D network in prototype

### Sidebar Tabs

**Click tab:**
- Swaps content (not stacking)
- Only one tab active at a time
- Smooth transition

### Ingestion Tab

**Provider rows:**
- Show: name, status badge, last run timestamp, symbols count
- Next run countdown (in seconds → formatted as "2h 15min")
- [Run now] button triggers immediate ingest for that provider

**[Run all ingestion]:**
- Lightweight confirm dialog: "Ingest all providers? (est. 30 min)"
- OK / Cancel

### Analysis Tab

**Analyst status:**
- Current task with symbol name
- Progress bar (if applicable)
- Queued symbols list

**[Analyze symbol X]:**
- Dropdown to pick symbol
- Triggers analyst on that symbol (re-analysis)
- No confirm needed (safe to re-analyze)

### Testing Tab

**Active tests:**
- Show completed test with result (PASS/FAIL) and decision (if any)

**Queued tests:**
- Show spec name, symbol, position in queue

**[Run test]:**
- Dropdown to pick spec
- Lightweight confirm: "Run 4-gate backtest for [SPEC]? (est. 15 min)"
- OK / Cancel

### Paper Trading Tab

**Pending theses:**
- Show symbol, action, trigger logic, status

**Active positions:**
- Show symbol, entry date/price, current value, P&L %

### Logs Tab (Default = Unified View)

**Unified timeline:**
- All-agent logs, most-recent-first
- Columns: Timestamp | Agent | Action | Subject | Status | Details

**Filter bar:**
- [Agent ▼] (All | Ingest-Bot | Analyst | Critic | FactorEngine | GateRunner | PaperEngine)
- [Status ▼] (All | SUCCESS | RUNNING | ERROR)
- [Date range ▼] (Last hour | Last 24h | All)

**Per-agent tabs:**
- Click agent name to view only that agent's logs
- Same table format, filtered

**Click log row:**
- Expands to show full details (if details are long)

---

## Refresh Strategy

- **Swarm visualization**: Auto-refresh every 2–5 seconds (agent states change in near-real-time)
- **Sidebar tabs**: Manual refresh button, or auto-refresh on tab switch
- **Logs**: Manual refresh button (append-only log, new entries appear only on refresh)
- **Pending theses / active positions**: Fast-interval refresh (5–15 min) since they depend on price updates

---

## Edge Cases

### No agents running
- Swarm shows all nodes in IDLE state
- Message: "All agents idle. [Trigger analysis] or [Run test] to start."

### Agent in ERROR state
- Node shows red 🔴
- Tooltip: "Error in last task: [error message]"
- Sidebar shows error badge with link to full error logs

### Test queue is empty
- Testing tab shows: "No tests queued."

### No pending theses
- Paper Trading tab shows: "No pending trades. [View strategies] to set up a thesis."

### Ingest failed
- Provider row shows red X, tooltip: "Failed: [reason]"
- Status shows "Last successful: 24h ago"
- [Run now] button still available

### Log view with no entries
- "No logs found for [filters]. [Clear filters]"

---

## Accessibility & Mobile

- **Tab order**: Sidebar toggle → swarm (pan/zoom controls) → sidebar tabs → tab content
- **Keyboard**: 
  - Swarm: + / - to zoom, arrow keys to pan, Tab to cycle through agent nodes
  - Sidebar: Tab to move between tabs, Enter to trigger actions
- **Mobile (<640px)**:
  - Sidebar always collapsed (hamburger to toggle)
  - Swarm takes full width (easier touch pan/zoom)
  - Logs table becomes single column (one entry per card)
- **Screen reader**: 
  - "Analyst agent, running, analyzing NVDA, 45% complete"
  - Log entry: "July 20, 2:28 PM, Analyst, started analyzing, NVDA, running, confidence cap by quality"

---

## Prototype Acceptance Criteria

- [ ] Swarm renders as 2D network with ≥6 agent nodes
- [ ] Node colors reflect state (green/yellow/blue)
- [ ] Edges show between connected agents
- [ ] Click node shows tooltip/brief popup
- [ ] Pan/zoom works (drag, scroll)
- [ ] Sidebar toggle hides/shows sidebar
- [ ] Sidebar tabs swap content (click tab changes view)
- [ ] Ingestion tab shows 3 providers with status, next run countdown, [Run now] buttons
- [ ] Analysis tab shows analyst status and queued symbols
- [ ] Testing tab shows active tests and queued tests
- [ ] Paper Trading tab shows pending theses and active positions
- [ ] Logs tab shows unified timeline (Timestamp | Agent | Action | Subject | Status)
- [ ] Log filters work (Agent, Status, Date range)
- [ ] [Run now] buttons are clickable (no actual execution in prototype, just feedback)
- [ ] Confirm dialogs appear for long-running triggers (ingest all, run test)
- [ ] Responsive down to 375px (single column, hamburger sidebar)
- [ ] No broken links to other pages

# 🚀 UI Design — START HERE

> **Status:** ✅ LOCKED & READY (2026-07-29)

---

## What You Have

A **complete, production-ready UI specification** for `research_data` frontend. 12 interconnected documents totaling ~170 KB.

All decisions locked. No ambiguity. Ready to build.

---

## The Vision (Recap)

A **learning-first trading dashboard** where:
- You see your research brain in action (Brain-Journal graph)
- You understand every trade before it executes (pending decisions visible everywhere)
- You learn by testing (4-gate validation loop, paper trading with journal)
- You control everything (no auto-execution, human always approves)
- It feels like a game, not a spreadsheet (live charts, agent swarm, clean UI)

**Not** a broker, **not** affiliated with TradingView, **not** financial advice.

---

## The Specs (12 Documents)

### 🌍 The Universe (Read First)
1. **UI_DESIGN_INDEX.md** — Navigation, components, data flow, guardrails
   - Read this first if you're new to the project
   - Understand overall architecture

### 📄 The 8 Pages (Read in Order)
2. **UI_DESIGN_DASHBOARD_SPEC.md** — Home: top-6 trades, ingest status, next steps
3. **UI_DESIGN_WATCHLIST_SPEC.md** — All 14 symbols table with search + modal
4. **UI_DESIGN_MYSTOCKS_SPEC.md** — **Main learning hub:** symbol sidebar + Position/Research tabs
5. **UI_DESIGN_TESTS_SPEC.md** — Gate test history, click to see diagnostics
6. **UI_DESIGN_STRATEGIES_SPEC.md** — Strategy cards, portfolio charts, compare specs
7. **UI_DESIGN_BRAIN_JOURNAL_SPEC.md** — Knowledge graph + journal with folder hierarchy
8. **UI_DESIGN_BOTS_HUB_SPEC.md** — Agent swarm + floating sidebar with logs
9. **UI_DESIGN_SETTINGS_SPEC.md** — User prefs, API status, system health

### 🛠️ The Build Plan (Read Before Coding)
10. **FIXTURE_FILES_README.md** — How to create & use JSON fixtures
11. **PROTOTYPE_BUILD_CHECKLIST.md** — Roadmap: phases, checklists, acceptance criteria
12. **UI_DESIGN_DELIVERABLES.md** — This package overview + quick reference

---

## Three Key Concepts to Understand

### 1️⃣ Pending Decisions Are Everywhere
A pending trade (e.g., "enter NVDA Monday 9:30 AM") shows as:
- Badge on Dashboard top-6 button (if symbol present)
- Badge on Watchlist row (if symbol present)
- Pending line in Position tab
- Inline mention in Evidence Card
- **Always-on banner at top** of symbol view

**This is intentional.** You never miss a pending trade, no matter which page you're on.

### 2️⃣ My Stocks Is the Hub
The deepest analysis happens in **My Stocks** (`/my-stocks/{SYMBOL}`).

Two tabs:
- **Position**: Clean price chart + buy/sell markers + P&L vs VOO
- **Research**: TA chart (MA/RSI/Bollinger) + evidence + factor scores + gate results

All deep links lead here:
- Dashboard top-6 button → SymbolModal → "View Full Analysis" → `/my-stocks/{SYMBOL}/research`
- Watchlist row → SymbolModal → "View Full Analysis" → `/my-stocks/{SYMBOL}/research`

**This is where you learn how decisions executed.**

### 3️⃣ 2D in Prototype, 3D in Production
Two places have interactive graphs:
- **Brain-Journal**: Shows how notes connect (neurons)
- **Bots-Hub**: Shows agent states (Ingest-Bot running, Analyst idle, etc.)

**Prototype:** Simple 2D network (click node, 5-second popup, returns to graph)  
**Production:** Full 3D cinematic visualization (later design phase)

Don't let the simpler prototype fool you — the interaction patterns are the same.

---

## Quick Navigation

| I want to... | Read this |
|---|---|
| Understand the overall architecture | UI_DESIGN_INDEX.md |
| See what the Dashboard looks like | UI_DESIGN_DASHBOARD_SPEC.md (scroll to Layout) |
| Know how pending decisions work | UI_DESIGN_INDEX.md (Pending Decision Visibility) |
| Understand My Stocks (the main page) | UI_DESIGN_MYSTOCKS_SPEC.md |
| Build the prototype | PROTOTYPE_BUILD_CHECKLIST.md |
| Create fixture data | FIXTURE_FILES_README.md |
| See which files exist | UI_DESIGN_DELIVERABLES.md |
| Know the acceptance criteria | Any page spec + PROTOTYPE_BUILD_CHECKLIST.md |

---

## What Each Page Does

```
📊 DASHBOARD
  ├─ What: Operational overview
  ├─ Shows: Top-6 trades, ingest status, next steps, paper P&L, backend health
  └─ Action: Click trade → modal; "View Full" → Watchlist; Next steps → relevant page

📋 WATCHLIST
  ├─ What: Full 14-symbol table
  ├─ Shows: Symbol, company, action, confidence, quality, last reviewed
  └─ Action: Search, click row → modal; "View Full Analysis" → My Stocks

💎 MY STOCKS ⭐ MAIN HUB
  ├─ What: Deep dive on any symbol
  ├─ Shows: 
  │   Position tab: clean price chart, entry/exit markers, P&L
  │   Research tab: TA chart, evidence card, factors, gate status
  ├─ Action: Click symbol in sidebar to switch; pending banner always visible
  └─ Learn: Why was this decision made? How did it execute?

🧪 TESTS
  ├─ What: Backtest history
  ├─ Shows: All test runs (most recent first), click to see 4-gate diagnostics
  └─ Action: Filter by status/gate/symbol/date

🎯 STRATEGIES
  ├─ What: Active specs (≤5), portfolio performance, comparison
  ├─ Shows: Strategy cards, detail view with portfolio chart, compare tab
  └─ Action: Click View → detail; Compare → side-by-side metrics

🧠 BRAIN-JOURNAL
  ├─ What: Knowledge graph + journal entries
  ├─ Shows: 
  │   Graph tab: 2D network of notes, click node → popup
  │   Journal tab: PARA folder structure + recent entries feed
  ├─ Action: Search entries, create new (with completeness check), filter by template
  └─ Learn: How does my knowledge connect?

🤖 BOTS-HUB
  ├─ What: AI operations center
  ├─ Shows: Agent swarm (2D network), ingestion/analysis/testing/paper trading tabs, unified logs
  ├─ Action: Click "Run now" → trigger (no-op in prototype), click log row → expand
  └─ Monitor: What's the brain doing right now?

⚙️ SETTINGS
  ├─ What: User prefs, API status, system health
  ├─ Shows: Account, UI prefs, API keys, system diagnostics, about
  └─ Action: Toggle dark mode (immediate effect), check API keys, run diagnostics
```

---

## The Prototype Build (TL;DR)

**What:** Read-only frontend in Next.js/React  
**Data:** Static JSON fixtures (no backend connection)  
**Timeline:** 13–18 days for 1–2 developers  
**Phases:**
1. Setup & global components (3–4 days)
2. Page implementation (5–7 days)
3. Interactions & responsive (3–4 days)
4. Polish & testing (2–3 days)

**Success:** All 8 pages work, no broken links, pending badges visible everywhere, responsive at 375px.

See **PROTOTYPE_BUILD_CHECKLIST.md** for detailed roadmap.

---

## What's NOT in V1

These are intentional descopes (not failures):
- 3D graphs (2D in prototype, 3D in production)
- Full cost/usage analytics (brief health check in V1)
- Inline vault editing (read-only mirror in V1)
- Multi-user auth (single "anant" for V1)
- LLM strategy proposer (human-created specs only in V1)

These will come in V1.1 or later, **after** the core learning loop is proven.

---

## Common Questions

**Q: Can I edit entries in Brain-Journal?**  
A: Not in prototype. Read-only. Production allows edit-in-place after Obsidian sync tested.

**Q: Can I actually run a backtest from the UI?**  
A: Not in prototype. "Run test" button is no-op. Production calls Python backend.

**Q: Where are the fixtures?**  
A: Not yet created. See FIXTURE_FILES_README.md for how to generate them.

**Q: Can I change the spec?**  
A: No (it's locked). If you find an issue during build, flag it and discuss before changing.

**Q: When does backend work start?**  
A: After prototype is stable. Backend team uses page specs' "data shape" to design API endpoints.

---

## Next Steps (For You)

1. **✅ Read UI_DESIGN_INDEX.md** (15 min)
   - Understand the architecture

2. **✅ Skim the 8 page specs** (30 min)
   - Get a feel for each page

3. **✅ Reference specific pages** when discussing with teammates
   - Use the diagrams, component trees, interaction patterns

4. **📋 Decide:** Do you want to generate fixtures now, or let prototype team do it?
   - See FIXTURE_FILES_README.md for guidance

5. **🤝 Brief the prototype team**
   - Share PROTOTYPE_BUILD_CHECKLIST.md
   - Highlight the 3 key concepts (pending decisions, My Stocks, 2D graphs)
   - Set expectation: 13–18 days, read-only, test against checklists

6. **🚀 Hand off**
   - All 12 spec docs go to Docs/ folder (already done)
   - Fixture files go to fixtures/ folder (TBD)
   - Point team to PROTOTYPE_BUILD_CHECKLIST.md as roadmap

---

## Files Location

All specs are in `/home/anant_gupta/projects/hub/tradingview/Docs/`:

```
Docs/
  UI_DESIGN_INDEX.md                  ← Start here
  UI_DESIGN_DASHBOARD_SPEC.md
  UI_DESIGN_WATCHLIST_SPEC.md
  UI_DESIGN_MYSTOCKS_SPEC.md          ← Most important
  UI_DESIGN_TESTS_SPEC.md
  UI_DESIGN_STRATEGIES_SPEC.md
  UI_DESIGN_BRAIN_JOURNAL_SPEC.md
  UI_DESIGN_BOTS_HUB_SPEC.md
  UI_DESIGN_SETTINGS_SPEC.md
  UI_DESIGN_DELIVERABLES.md           ← Package overview
  FIXTURE_FILES_README.md             ← Data guide
  PROTOTYPE_BUILD_CHECKLIST.md        ← Build roadmap
  UI_DESIGN_START_HERE.md             ← You are here 👋
```

---

## That's It. You're Good to Go.

Everything is locked. Specs are unambiguous. No more questions.

Time to build.

**Questions during build?** See each spec's "Accessibility & Mobile" or "Edge Cases" sections first, then escalation path in PROTOTYPE_BUILD_CHECKLIST.md.

🚀 **Let's ship this.**

---

**Version:** 2026-07-29 (Locked)  
**Scope:** Next.js/React prototype (mock data, read-only, learning-first)  
**Timeline:** 13–18 days  
**Success:** All 8 pages work, no broken links, responsive at 375px  

**Status: ✅ READY FOR BUILD**

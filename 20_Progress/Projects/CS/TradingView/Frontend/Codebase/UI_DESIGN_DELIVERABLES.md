# UI Design Deliverables — Complete Package

> **Freezepoint: 2026-07-29**  
> All specifications locked. Ready for prototype build.

---

## Executive Summary

A complete **Information Architecture & Design Specification** for the `research_data` frontend, organized as 11 interconnected documents + fixture file guidance. This is the contract between product vision and engineering execution.

**Total scope:** ~170 KB of specification across 11 documents, covering 8 pages, 60+ components, interaction patterns, data shapes, and responsive design.

**Status:** ✅ **COMPLETE AND LOCKED**

---

## Deliverable Overview

### 1. **UI_DESIGN_INDEX.md** (12 KB)
**The entry point.** Read this first.

Contains:
- Navigation structure (8 header items, no sidebar)
- Global component inventory (11 reusable components)
- Interaction patterns (modals, sidebars, filters, search)
- Pending decision visibility (propagates to 5 surfaces)
- Data flow & refresh strategy
- Design tokens (placeholders for production)
- Cross-cutting guardrails (no BUY/SELL language, etc.)

**Use this to understand:** Overall architecture, which pages exist, how components are reused, what data flows where.

---

### 2–9. **Page Specs** (8 documents, ~130 KB total)

One spec per page. Each contains:
- **Purpose** — what this page shows
- **Layout** — ASCII diagram + component tree
- **Data shape** — JSON fixture excerpt
- **Interactions** — click, hover, filter, search, expand behaviors
- **Refresh strategy** — how often data updates
- **Edge cases** — what happens if data is missing, stale, etc.
- **Accessibility & mobile** — responsive breakpoints, keyboard nav
- **Acceptance criteria** — checklist for prototype team

#### Page Specs (in nav order):

1. **UI_DESIGN_DASHBOARD_SPEC.md** (14 KB)
   - Operational overview: top-6 trades, ingest status, next steps, paper P&L
   - All major dashboard elements with live updates

2. **UI_DESIGN_WATCHLIST_SPEC.md** (9.6 KB)
   - Full 14-symbol table: action, confidence, quality, last reviewed
   - Search, modal on click, "View Full" navigation

3. **UI_DESIGN_MYSTOCKS_SPEC.md** (25 KB) ← **LARGEST**
   - Deep dive hub: symbol sidebar + Position/Research tabs
   - Clean price chart (Position) vs TA chart (Research)
   - Evidence card, critic review, gate status, pending decisions
   - Most complex page; defines the learning loop

4. **UI_DESIGN_TESTS_SPEC.md** (18 KB)
   - Append-only backtest log: spec → test date → 4-gate results
   - Expand row to see gate diagnostics + linked journal entry
   - Filters by status, gate, symbol, date

5. **UI_DESIGN_STRATEGIES_SPEC.md** (21 KB)
   - Strategy spec cards (≤5 active specs)
   - Per-strategy detail view with portfolio chart
   - Compare tab for side-by-side metric comparison
   - Human-gated approve/promote/demote buttons

6. **UI_DESIGN_BRAIN_JOURNAL_SPEC.md** (21 KB)
   - 2D interactive graph of note connections (neurons)
   - Journal section: PARA folder hierarchy + recent entries feed
   - Completeness validation (entry only appears in feed if passes check)
   - Sidebar tabs: Ingestion/Paper Trading/Research/Test Viz logs

7. **UI_DESIGN_BOTS_HUB_SPEC.md** (19 KB)
   - 2D agent swarm (Ingest-Bot, Analyst, Critic, FactorEngine, etc.)
   - Floating sidebar with tabs: Ingestion | Analysis | Testing | Paper Trading | Logs
   - Manual triggers: "Run now", "Analyze symbol", "Run test"
   - Unified log + per-agent view with filters

8. **UI_DESIGN_SETTINGS_SPEC.md** (15 KB)
   - User account (hardcoded "anant" for V1)
   - UI preferences (dark mode, refresh intervals, sidebar behavior)
   - API key status + secrets redaction check
   - System health (database, backend, disk)
   - About section with links

---

### 10. **FIXTURE_FILES_README.md** (9 KB)
**How to create and use the JSON fixtures.**

Contains:
- Directory structure (8 JSON files expected)
- How to import fixtures in React components
- Production swap strategy (static → dynamic fetch)
- Data consistency rules (cross-fixture validation)
- Per-fixture details (size, refresh rate, contents)
- Testing checklist (symbol lists, pending badges, counts match, etc.)
- Prototype team handoff workflow

**Use this to:** Generate fixture data, validate consistency, understand what data each page needs.

---

### 11. **PROTOTYPE_BUILD_CHECKLIST.md** (15 KB)
**Roadmap for the prototype team.**

Contains:
- Build phases (Setup → Global Components → Pages → Interactions → Polish)
- Page-by-page checklist (50+ items across all 8 pages)
- Cross-page validation (pending badges on all 5 surfaces, deep links work)
- Responsive design testing (375px, 640px, 1024px, 1440px)
- Acceptance criteria (final "success looks like" list)
- Timeline estimate (13–18 days for 1–2 developers)
- Known limitations (V1 prototype is read-only)
- Escalation & questions path

**Use this to:** Track progress, understand build phases, know what "done" looks like.

---

## File Sizes & Organization

```
Docs/
  UI_DESIGN_INDEX.md                  12 KB    ← Start here
  UI_DESIGN_DASHBOARD_SPEC.md         14 KB
  UI_DESIGN_WATCHLIST_SPEC.md         9.6 KB
  UI_DESIGN_MYSTOCKS_SPEC.md          25 KB    ← Largest/most complex
  UI_DESIGN_TESTS_SPEC.md             18 KB
  UI_DESIGN_STRATEGIES_SPEC.md        21 KB
  UI_DESIGN_BRAIN_JOURNAL_SPEC.md     21 KB
  UI_DESIGN_BOTS_HUB_SPEC.md          19 KB
  UI_DESIGN_SETTINGS_SPEC.md          15 KB
  UI_DESIGN_DELIVERABLES.md (this)    [~5 KB]
  FIXTURE_FILES_README.md             9 KB     ← Fixture guide
  PROTOTYPE_BUILD_CHECKLIST.md        15 KB    ← Build roadmap

Total: ~172 KB (all Markdown)
```

---

## How to Use This Package

### For Product/Design (You)
1. **Read Index.md** to understand the overall vision
2. **Skim all 8 page specs** to see layouts and components
3. **Reference specific page** when discussing implementation
4. **Use acceptance criteria** to validate prototype quality

### For Prototype Frontend Team
1. **Start with Index.md** (understand architecture)
2. **Read PROTOTYPE_BUILD_CHECKLIST.md** (build plan)
3. **Pick a page** (e.g., Dashboard)
4. **Read that page's spec** (layout, component tree, data shape, interactions)
5. **Grab the fixture file** (fixtures/dashboard.json) and import it
6. **Build components** against the checklist
7. **Test interactions** (click, modal, filter, responsive)
8. **Check acceptance criteria** before moving to next page

### For Backend Team (Later)
1. **Read Index.md** (understand data needs)
2. **Review each page's "data shape"** section (see fixture excerpt)
3. **Build API endpoints** that return same shape as fixtures
4. **Swap fixture import for API call** in frontend (mostly code reuse)

---

## Decisions Locked In This Spec

✅ **Navigation**: 8 header items, no sidebar  
✅ **Pending decisions**: Visible on 5 surfaces (Dashboard, Watchlist, Position, Evidence, Banner)  
✅ **Tabs**: Position/Research (My Stocks), Graph/Journal/Research/Test Viz (Brain)  
✅ **Charts**: Clean price (My Stocks Position) vs TA chart (My Stocks Research)  
✅ **Graphs**: 2D network in prototype (3D in production)  
✅ **Real-time**: Fast interval (5–15 min) for live panels, slow (5 min) for AI content  
✅ **Forms**: Completeness validation on journal entries (required fields + check passing)  
✅ **Modals**: Medium size, SymbolModal reused everywhere  
✅ **Responsive**: 375px minimum (single column, hamburger sidebars)  
✅ **Guardrails**: No BUY/SELL, no execution language, no fabricated numbers  

**None of these can be changed without consensus.** If you find an issue during prototype build, flag it and discuss before changing the spec.

---

## Known Descopes (Intentional)

These are **NOT IN V1** but will come in production:

- **3D/cinematic graphs** → 2D network in prototype, 3D in production design phase
- **Particle swarm visualization** → 2D nodes-and-edges in prototype, particle system in production
- **Full cost/usage analytics** → Brief ops health in V1, full analytics once real LLM cost data exists
- **Inline vault editing** → Read-only mirror in V1, edit-in-place in V1.1 (after Obsidian sync tested)
- **Multi-user auth** → Single user "anant" for V1, multi-user deferred to V2
- **Strategy proposer LLM** → Human-created specs only in V1, LLM proposer in V1.1 after card quality validated
- **Export/PDF reports** → No bulk export in V1
- **Advanced charting** (candlestick, volume, etc.) → Clean price lines in V1, enhanced charts in V1.1

These are **not failures** — they're intentional scope boundaries to keep V1 shippable.

---

## Cross-References

Quick lookup for common questions:

**"How do I refresh data?"**  
→ See Index.md → Data Flow & Real-Time Strategy section

**"What should the Evidence Card look like?"**  
→ See My Stocks spec → Research Tab layout section

**"How do pending decisions propagate?"**  
→ See Index.md → Pending Decision Visibility section

**"What's the SymbolModal?"**  
→ See Dashboard spec or Watchlist spec → SymbolModal section (reusable component)

**"What fixture files do I need?"**  
→ See FIXTURE_FILES_README.md → Fixture Files section

**"When should I use 2D graph vs 3D?"**  
→ See Brain-Journal or Bots-Hub spec → Production descopes note

**"How do I test pending badges work?"**  
→ See PROTOTYPE_BUILD_CHECKLIST.md → Cross-Page Validation section

---

## Handoff Protocol

**Before handing to prototype team:**

1. ✅ Generate fixture files (or provide template JSON)
2. ✅ Copy all 11 spec docs to `Docs/` folder (already done)
3. ✅ Create `fixtures/` folder with 8 JSON files
4. ✅ Provide this deliverables list + PROTOTYPE_BUILD_CHECKLIST.md as orientation
5. ✅ Brief the team on the 3 key concepts:
   - Pending decisions visible on 5 surfaces
   - My Stocks is the hub for deep dives
   - 2D graphs in prototype (3D later)
6. ✅ Clarify: **Prototype is read-only** — no actual trades, approvals, mutations
7. ✅ Set expectation: **13–18 days** for full build

**Go/no-go for backend:**  
- Once prototype is stable, backend team can start building API endpoints
- Each page spec shows data shape → backend implements those endpoints
- Swap fixture imports for real API calls (code mostly stays same)

---

## Questions?

### During Spec Creation (Already Answered)
- ✅ Navigation: 8 header items (no sidebar) — confirmed
- ✅ Pending decisions: 5 visible surfaces — confirmed
- ✅ My Stocks: One symbol at a time, sidebar to pick symbol — confirmed
- ✅ Charts: Clean price (Position) vs TA (Research) — confirmed
- ✅ Graphs: 2D in prototype, 3D in production — confirmed
- ✅ Completeness: Required fields block journal entry from appearing — confirmed
- ✅ Refresh: Fast (live), slow (AI), static (manual) — confirmed

### During Prototype Build (TBD)
- See PROTOTYPE_BUILD_CHECKLIST.md → Escalation Path section
- If spec is ambiguous, implement most sensible interpretation and document it
- Do **not** change spec unilaterally

### During Production Build (Future)
- Architect will document how to port from prototype to production
- Expect data shape to stay mostly same; presentation may polish

---

## Version History

| Date | Status | Author | Notes |
|------|--------|--------|-------|
| 2026-07-29 | 🔒 LOCKED | You + AI | Complete IA + 8 page specs + fixture guide + build checklist |
| — | (next cycle) | (TBD) | Post-prototype learnings, updates for V1.1 |

---

## Quick Reference URLs

- **Dashboard**: `/` or `/dashboard`
- **Watchlist**: `/watchlist`
- **My Stocks (Portfolio)**: `/my-stocks`
- **My Stocks (Symbol)**: `/my-stocks/{SYMBOL}` or `/my-stocks/{SYMBOL}/research`
- **Tests**: `/tests`
- **Strategies**: `/strategies`
- **Brain-Journal**: `/brain-journal`
- **Bots-Hub**: `/bots-hub`
- **Settings**: `/settings`

(Exact routing can vary in Next.js; these are semantic paths from the spec.)

---

## Final Checklist Before Handoff

- [ ] All 11 spec documents written and reviewed
- [ ] Fixture files created (8 JSON files) or template provided
- [ ] No broken links between spec documents
- [ ] All component names consistent across specs
- [ ] All data shapes match between specs (symbol, date formats, etc.)
- [ ] Acceptance criteria realistic for prototype team
- [ ] Color palette/design tokens noted (even if placeholders)
- [ ] 8 page specs have working links to each other
- [ ] Index.md reviewed as entry point
- [ ] PROTOTYPE_BUILD_CHECKLIST.md reviewed as roadmap
- [ ] Team briefing scheduled (agenda: 3 key concepts + scope + timeline)

---

**Status: ✅ READY FOR PROTOTYPE BUILD**

All specifications locked. No further changes without consensus.

Let's build this. 🚀

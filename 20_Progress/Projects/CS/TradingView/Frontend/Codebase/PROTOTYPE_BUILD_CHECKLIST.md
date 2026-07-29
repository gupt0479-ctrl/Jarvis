# Prototype Build Checklist

> **Freezepoint document:** All specs locked. This is the contract for the prototype frontend team.  
> **Status:** Ready for build (2026-07-29)

---

## What Is the Prototype?

A **fully interactive, read-only frontend** in Next.js/React that demonstrates the complete UI/UX vision. All data comes from static JSON fixtures (no backend connection). The prototype proves the layout and interaction patterns work before the production backend touches it.

**Not the prototype:**
- Backend API integration (comes later)
- 3D/cinematic graph (descoped to 2D network)
- Real data persistence (no actual trades, approvals, edits)
- Actual CLI command execution

**Is the prototype:**
- 8 fully functional page layouts
- All routing and navigation patterns
- Modals, sidebars, tabs, filters working
- Pending decision badges propagating across 5 surfaces
- Real-time refresh simulation (UI updates from fixture data)
- Responsive design down to 375px width

---

## Spec Documents

All locked and ready. Read in this order:

1. **[UI_DESIGN_INDEX.md](./UI_DESIGN_INDEX.md)** ← **START HERE**
   - Navigation structure
   - Global components
   - Data flow & refresh strategy
   - Design tokens (placeholders)

2. **Page Specs** (one per page, read in nav order):
   - [Dashboard](./UI_DESIGN_DASHBOARD_SPEC.md)
   - [Watchlist](./UI_DESIGN_WATCHLIST_SPEC.md)
   - [My Stocks](./UI_DESIGN_MYSTOCKS_SPEC.md)
   - [Tests](./UI_DESIGN_TESTS_SPEC.md)
   - [Strategies](./UI_DESIGN_STRATEGIES_SPEC.md)
   - [Brain-Journal](./UI_DESIGN_BRAIN_JOURNAL_SPEC.md)
   - [Bots-Hub](./UI_DESIGN_BOTS_HUB_SPEC.md)
   - [Settings](./UI_DESIGN_SETTINGS_SPEC.md)

3. **[FIXTURE_FILES_README.md](./FIXTURE_FILES_README.md)**
   - How to use the JSON fixtures
   - Data consistency rules
   - When/how to refresh

---

## Fixture Files

**Location:** `fixtures/` directory (create if doesn't exist)  
**8 files total:**

```
fixtures/
  dashboard.json              # ~1 KB
  watchlist.json              # ~3 KB
  my-stocks-nvda.json         # ~6 KB (example; create for ≥2–3 symbols)
  my-stocks-msft.json         # ~6 KB (example)
  my-stocks-aapl.json         # ~6 KB (example)
  tests.json                  # ~8 KB (≥10 test runs)
  strategies.json             # ~6 KB (≤5 specs)
  brain-journal.json          # ~10 KB (≥20 nodes, ≥40 edges)
  bots-hub.json               # ~5 KB (6 agents)
  settings.json               # ~3 KB
```

**Status:** Not yet generated (you'll create these before handing off to team)

---

## Build Phases

### Phase 1: Setup & Structure (1–2 days)
- [ ] Create Next.js/React boilerplate (TypeScript)
- [ ] Set up folder structure (`pages/`, `components/`, `fixtures/`)
- [ ] Create stub pages for all 8 routes
- [ ] Implement Header (persistent nav)
- [ ] Implement routing (next/router or next/navigation)

### Phase 2: Global Components (2–3 days)
- [ ] `SymbolModal` (reusable modal)
- [ ] `PendingDecisionBanner` (reusable banner)
- [ ] `FactorPanel` (reusable)
- [ ] `EvidenceCard` (reusable)
- [ ] `GatePanel` (reusable)
- [ ] `PortfolioChart` (reusable, uses recharts or chart.js)
- [ ] `TA_Chart` (reusable, with indicators)
- [ ] `LogRow` (reusable log entry)
- [ ] `JournalEntry` (reusable)

### Phase 3: Page Implementation (5–7 days)
- [ ] **Dashboard** (all sections, next-steps clickable)
- [ ] **Watchlist** (table, search, modal on click)
- [ ] **My Stocks** (symbol sidebar + Position/Research tabs)
- [ ] **Tests** (table, expandable rows, gate diagnostics)
- [ ] **Strategies** (cards, grid/compare toggle, detail view)
- [ ] **Brain-Journal** (2D graph + journal section with folders)
- [ ] **Bots-Hub** (2D swarm + floating sidebar with tabs + logs)
- [ ] **Settings** (sections, form inputs, no save)

### Phase 4: Interactions & Responsiveness (3–4 days)
- [ ] Modal open/close on all entry points
- [ ] Deep link navigation (Dashboard → Watchlist → My Stocks)
- [ ] Pending decision badges on all 5 surfaces
- [ ] Tab switching (Position/Research, Ingestion/Analysis/Testing/Paper Trading)
- [ ] Filter/search functionality
- [ ] Hover states on all interactive elements
- [ ] Mobile responsive down to 375px (test on device)
- [ ] Keyboard navigation (Tab, Enter, Arrow keys)

### Phase 5: Polish & Testing (2–3 days)
- [ ] Dark mode (if not done in Phase 1)
- [ ] Accessibility review (ARIA labels, screen reader testing)
- [ ] Console errors: zero
- [ ] Broken links: zero
- [ ] All buttons clickable (feedback visible, even if no-op)
- [ ] Screenshot each page for handoff docs

---

## Checklist by Page

### Dashboard
- [ ] Top-6 trades render as buttons (1 starred, 5 by confidence)
- [ ] Click button opens SymbolModal
- [ ] Watchlist mini shows top 5 + "View Full"
- [ ] Ingest status shows 3 providers, timestamp on hover
- [ ] Next steps list is clickable (each jumps to relevant page)
- [ ] Paper trading stats display correctly (today, MTD, vs VOO)
- [ ] Backend ops status shows (API keys, secrets, active specs)
- [ ] All sections render, no layout breaks

### Watchlist
- [ ] All 14 symbols in table
- [ ] Search filters by symbol/company (case-insensitive)
- [ ] Click row opens SymbolModal (same modal as Dashboard)
- [ ] "View Full Watchlist" link works (likely just hides itself, showing all 14)
- [ ] Status badges correct colors
- [ ] Quality badges correct icons
- [ ] Pending badge shows on applicable rows
- [ ] Sort order: starred first, rest by confidence

### My Stocks
- [ ] Symbol sidebar shows all 14, search works
- [ ] Click sidebar symbol switches main view
- [ ] Current symbol is highlighted
- [ ] Favorite toggle works (stars symbol, no persistence needed)
- [ ] Pending decision banner shows with countdown
- [ ] Position tab: clean price chart, buy/sell markers, open/closed position tables
- [ ] Research tab: TA chart with indicators, evidence card, critic review, gate panel
- [ ] Data quality badges show correct status
- [ ] "Last updated" timestamp visible, refresh button functional
- [ ] Responsive: sidebar collapses on mobile

### Tests
- [ ] All test runs render in table, most-recent-first
- [ ] Filters work (status, gate, symbol, date)
- [ ] Click row expands to show gate diagnostics
- [ ] Gate panels show all 4 gates with metrics
- [ ] Status badges correct colors (PASS/FAIL)
- [ ] Decision badges show when applicable
- [ ] Journal entry panel shows excerpt + link
- [ ] Promotion decision panel shows decision, reasoning, timestamp
- [ ] Pagination works (or fixture <25 runs)
- [ ] Responsive: table becomes card layout on mobile

### Strategies
- [ ] All ≤5 specs render as cards in grid
- [ ] Status filters work
- [ ] View toggle (Grid | Compare) works
- [ ] Click [View] navigates to per-strategy detail page
- [ ] Status badge correct color
- [ ] Portfolio stats display (return %, Sharpe, drawdown)
- [ ] Gate panel shows 4 gates with pass/fail
- [ ] Action buttons appear (context-sensitive per status)
- [ ] Portfolio chart renders with entry/exit markers
- [ ] Compare view shows side-by-side table
- [ ] Back button returns to grid

### Brain-Journal
- [ ] 2D graph renders with ≥20 nodes, mixed colors
- [ ] Click node shows 5-second detail popup
- [ ] Pan/zoom works on graph
- [ ] Sidebar toggle hides/shows sidebar
- [ ] Journal view: left panel shows folder hierarchy (PARA + templates)
- [ ] Right panel shows recent entries feed
- [ ] Search filters entries real-time
- [ ] Template filter works
- [ ] Date range filter works
- [ ] [+ New entry] dropdown shows all 6 templates
- [ ] Entry card expands to show full content
- [ ] Completeness check legend is expandable
- [ ] Entry must pass completeness check to appear in recent feed
- [ ] Failed/incomplete entries show in folder but not in feed

### Bots-Hub
- [ ] Swarm renders as 2D network with ≥6 agent nodes
- [ ] Node colors reflect state (green/yellow/blue)
- [ ] Edges show between connected agents
- [ ] Pan/zoom works
- [ ] Sidebar toggle hides/shows sidebar
- [ ] Sidebar tabs swap content (Ingestion | Analysis | Testing | Paper Trading | Logs)
- [ ] Ingestion tab: 3 providers + next-run countdown + [Run now] buttons
- [ ] Analysis tab: analyst status + queued symbols
- [ ] Testing tab: active/queued tests
- [ ] Paper Trading tab: pending theses + active positions
- [ ] Logs tab: unified timeline with filters (agent, status, date)
- [ ] [Run now], [Analyze symbol], [Run test] buttons clickable (no-op in prototype)
- [ ] Confirm dialogs appear for long-running triggers

### Settings
- [ ] Account section: identity display, read-only
- [ ] UI preferences: dark mode toggle (immediate effect)
- [ ] Auto-refresh dropdowns functional
- [ ] Sidebar behavior options visible
- [ ] API key status shows for all 4 providers
- [ ] [Check now] button clickable
- [ ] System health shows database, backend, LLM, disk status
- [ ] [Run diagnostics] button clickable
- [ ] About section shows version, author, links
- [ ] All links are safe (may be placeholder URLs)

---

## Cross-Page Validation

### Pending Decision Badges

Verify pending decisions appear on **all 5 surfaces:**

- [ ] Dashboard top-6 button (if symbol is present)
- [ ] Watchlist row (if symbol is present)
- [ ] My Stocks: Position tab pending line
- [ ] My Stocks: Evidence Card inline mention
- [ ] My Stocks: Top banner (always visible)

**Test case:** Set one symbol (e.g., NVDA) to have `is_pending: true` in multiple fixture files. Verify badge/countdown appear everywhere.

### Deep Links

Verify all navigation paths work:

- [ ] Dashboard "View Full Watchlist" → `/watchlist`
- [ ] Dashboard "View My Stocks" → `/my-stocks` (portfolio view)
- [ ] Dashboard next-steps items → relevant pages
- [ ] Watchlist row click → SymbolModal → "View Full Analysis" → `/my-stocks/{SYMBOL}/research`
- [ ] My Stocks sidebar symbol click → URL changes, data swaps
- [ ] Tests "View full entry" → journal entry (if route exists)
- [ ] Strategies "View" → detail page; "View logs" → `/tests` filtered
- [ ] Brain-Journal node click → 5-sec popup → returns to graph
- [ ] Brain-Journal entry click → expands or opens detail
- [ ] Bots-Hub sidebar content → no page changes, just tab swap

### Responsive Design

Test at these breakpoints:

- [ ] **375px** (mobile, smallest target)
- [ ] **640px** (tablet/small landscape)
- [ ] **1024px** (desktop)
- [ ] **1440px+** (large desktop, max width if applicable)

**Checklist per breakpoint:**
- [ ] All text readable (no cutoff)
- [ ] Buttons/inputs reachable by touch (≥44px height)
- [ ] Sidebars collapse or scroll (no horizontal scroll)
- [ ] Tables convert to cards or scroll (no horizontal scroll breaking layout)
- [ ] Images/charts scale proportionally

---

## Prototype Acceptance Criteria (Final)

- [ ] **All 8 pages exist and render without errors**
- [ ] **No console errors** (run dev tools, check console tab)
- [ ] **No broken links** (click every link, should navigate or show modal)
- [ ] **All buttons are clickable** (even if no-op, visual feedback visible: hover, active state)
- [ ] **Modals work** (open on click, close on X/click-outside, background dimmed)
- [ ] **Tabs work** (click tab, content swaps, active tab highlighted)
- [ ] **Filters work** (change filter value, UI updates in real-time)
- [ ] **Search works** (type, table/feed filters, "no results" shows if empty)
- [ ] **Pending decision badges visible on all 5 surfaces** (Dashboard, Watchlist, Position tab, Evidence Card, Banner)
- [ ] **Deep links work** (navigate across pages, URL reflects current page)
- [ ] **Responsive at 375px** (sidebar collapses, tables convert to cards, no horizontal scroll)
- [ ] **Dark mode works** (toggle in Settings, site-wide theme changes)
- [ ] **Accessibility baseline** (Tab key navigates, Escape closes modals, forms have labels)
- [ ] **Screenshot each page** (for handoff docs and README)

---

## Handoff to Backend Team

Once prototype is done:

1. **Build production fixtures** from current backend state (DuckDB export)
2. **Swap fixture imports** for API calls (most of the code stays same)
3. **Add auth/user session** (if multi-user needed later)
4. **Add form submission** (create entry, approve spec, trigger ingest, etc.)
5. **Add real-time updates** (websocket for live price updates, agent status)
6. **Scale 2D graphs to 3D** (if production design requires)

---

## Known Limitations (V1 Prototype)

- No actual data mutations (can't really approve a spec, edit entry, run ingest)
- 2D graphs only (3D comes in production)
- No websocket real-time (simulated with fixed-interval refresh)
- Settings changes don't persist (just UI-level, no backend)
- No multi-symbol comparison views (My Stocks shows one symbol at a time)

These are **by design** — prototype is read-only, focusing on layout and interaction patterns.

---

## Questions During Build?

1. **Layout not matching spec?** Re-read the spec's layout diagram and component tree.
2. **Data shape unclear?** Check the fixture excerpt in that spec.
3. **Color/token not defined?** Use placeholder (pick from spec colors or standard palette; exact values come in production design phase).
4. **Component reuse not clear?** See Index doc's Component Inventory.
5. **Responsive breakpoint unclear?** Test at 375px / 640px / 1024px / 1440px; that covers most cases.

---

## Success Looks Like

A fully interactive, single-page application where:

- You can click through all 8 pages without any broken navigation
- Every interaction feels responsive (buttons have hover/active states, modals open smoothly)
- The pending decision badge for NVDA shows on the Dashboard button, in the Watchlist, and in all three places on the My Stocks page
- You can search the Watchlist and see results filter in real-time
- You can toggle dark mode and the whole site changes theme
- You can view the strategy detail, see the portfolio chart with trade markers, and understand how the four gates passed
- You can click into the Brain-Journal graph, see a node popup for 5 seconds, and understand how notes are connected
- You can scroll the entire site on a 375px phone without any horizontal scroll breaking the layout

**If all of that works, the prototype is ready for handoff to backend team.**

---

## Timeline Estimate

- **Setup & global components**: 3–4 days
- **Page implementation**: 5–7 days
- **Interactions & responsiveness**: 3–4 days
- **Polish & testing**: 2–3 days

**Total: 13–18 days** (assuming 1–2 full-time developers)

(Your mileage may vary depending on team size, Next.js experience, and Recharts/charting library familiarity.)

---

## Escalation Path

If you find an issue that contradicts the spec:

1. **Double-check the spec** (re-read the relevant section)
2. **Check the fixture data** (is the data actually present? formatted correctly?)
3. **If spec is ambiguous**, flag it in a comment and implement the most sensible interpretation
4. **Document your interpretation** in case the spec needs clarification later

Do **not** change the spec yourself — it's locked until the next planning session (if needed).

---

Good luck! The vision is clear; now it's time to build it. 🚀

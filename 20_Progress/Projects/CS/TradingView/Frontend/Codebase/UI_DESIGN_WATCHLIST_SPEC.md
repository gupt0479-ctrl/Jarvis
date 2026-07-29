# Watchlist Spec

> Full 14-symbol universe table. Entry point to deep research on any symbol.
> Reference: `fixtures/watchlist.json`

---

## Purpose

Show **all 14 symbols in the universe** with their current recommendation status:
- Action (WATCH/HOLD/ACCUMULATE/REDUCE/AVOID)
- Confidence
- Data quality
- Last review date
- Search/filter to find symbols quickly
- Click → full analysis (`/my-stocks/{SYMBOL}/research`)

---

## Layout

```
┌──────────────────────────────────────────────────────────┐
│ research_data | Dashboard | Watchlist | ...   [⚙ Settings] │
├──────────────────────────────────────────────────────────┤
│                                                           │
│ Watchlist — All 14 Symbols                              │
│                                                           │
│ [Search by symbol/company...________]                   │
│                                                           │
│ ┌─────────────────────────────────────────────────────┐│
│ │ Symbol │ Company │ Action │ Confidence │ Quality │ Last │
│ ├─────────────────────────────────────────────────────┤│
│ │ ★ AAPL │ Apple Inc. │ Accum │ 82% │ Usable │ Jul 20│
│ │ MSFT   │ Microsoft  │ Hold  │ 73% │ Usable │ Jul 20│
│ │ NVDA   │ Nvidia     │ Watch │ 55% │ Usable │ Jul 20│
│ │ GOOGL  │ Alphabet   │ Hold  │ 65% │ Usable │ Jul 19│
│ │ AMZN   │ Amazon     │ Accum │ 89% │ Partial│ Jul 19│
│ │ META   │ Meta       │ Watch │ 54% │ Usable │ Jul 19│
│ │ VOO    │ Vanguard S&P│Hold  │ 71% │ Usable │ Jul 20│
│ │ VTI    │ Vanguard Total│Hold │ 68% │ Usable │ Jul 19│
│ │ SPY    │ SPDR S&P 500│ Hold  │ 70% │ Usable │ Jul 20│
│ │ QQQ    │ Invesco QQQ│ Accum │ 76% │ Usable │ Jul 20│
│ │ BRKB   │ Berkshire B │ Avoid │ 42% │ Stale  │ Jul 18│
│ │ JPM    │ JP Morgan  │ Watch │ 58% │ Usable │ Jul 19│
│ │ COST   │ Costco     │ Hold  │ 64% │ Usable │ Jul 20│
│ │ TSLA   │ Tesla      │ Reduce│ 47% │ Missing│ Jul 17│
│ └─────────────────────────────────────────────────────┘│
│                                                           │
│ Showing 14 of 14                                        │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

---

## Component Tree

```
WatchlistPage
├── Header (global)
├── PageTitle: "Watchlist — All 14 Symbols"
├── SearchInput
│   └── Filters by: symbol (case-insensitive), company name
├── Table
│   ├── TableHeader (Symbol | Company | Action | Confidence | Quality | Last Reviewed)
│   └── TableRow × 14
│       ├── StarIcon (if pinned)
│       ├── SymbolCell (clickable → SymbolModal on hover, click opens modal)
│       ├── CompanyCell
│       ├── ActionBadge (color-coded by action)
│       ├── ConfidenceCell (percentage)
│       ├── QualityBadge (color-coded by quality status)
│       ├── LastReviewedCell (date)
│       └── PendingBadge (if applicable)
└── Pagination info (e.g., "Showing 14 of 14" or "Showing 10 of 14")
```

---

## Data Shape (Fixture Excerpt)

```json
{
  "watchlist": {
    "as_of": "2026-07-20T14:30:00Z",
    "symbols": [
      {
        "symbol": "AAPL",
        "company_name": "Apple Inc.",
        "action": "ACCUMULATE",
        "confidence": 0.82,
        "data_quality": "USABLE",
        "last_reviewed": "2026-07-20",
        "is_starred": true,
        "is_pending": false,
        "pending_logic": null,
        "momentum_rank": 3,
        "quality_rank": 5,
        "safety_rank": 8,
        "valuation_rank": 6
      },
      {
        "symbol": "MSFT",
        "company_name": "Microsoft Corp.",
        "action": "HOLD",
        "confidence": 0.73,
        "data_quality": "USABLE",
        "last_reviewed": "2026-07-20",
        "is_starred": false,
        "is_pending": true,
        "pending_logic": "Entry pending: Monday 9:30 AM ET",
        "momentum_rank": 4,
        "quality_rank": 2,
        "safety_rank": 3,
        "valuation_rank": 4
      },
      // 12 more...
    ],
    "total_count": 14,
    "displayed_count": 14
  }
}
```

---

## Interactions

### Search Input

**Behavior:**
- Filters by symbol (e.g., "AA" matches "AAPL")
- Filters by company name (e.g., "micro" matches "Microsoft")
- Case-insensitive
- Real-time (as you type, table updates)
- Clears results if no matches (shows "No symbols found")

**Example:**
- Type "AAPL" → shows only AAPL row
- Type "micro" → shows only MSFT row
- Type "tech" → shows multiple tech-heavy symbols (if filtering by sector is added later)

### Row Click

**Primary click behavior:**
- Opens `SymbolModal` (medium overlay)
- Modal shows: action, confidence, 1-line summary, top 2–3 factor ranks
- "View Full Analysis" inside modal → `/my-stocks/{SYMBOL}/research`

**Alternate interaction:**
- Hover reveals more details (optional: show first line of evidence summary)

### Star Icon

**Click behavior:**
- Toggles pinned state (UI only — prototype doesn't persist; production will save to user prefs)
- Starred symbol always appears first in Dashboard's top-6

### Badges

**Action badge** (colored button-like):
- WATCH = gray
- HOLD = blue
- ACCUMULATE = green
- REDUCE = orange
- AVOID = red

**Quality badge** (small label):
- USABLE = green checkmark
- PARTIAL = yellow warning
- STALE = orange warning
- MISSING = red X
- CONTRADICTORY = red X

**Pending badge** (if applicable):
- Shows as small icon next to action or confidence
- Indicates thesis awaiting execution

### Sorting

**Default sort:**
- Starred first (if any), then by confidence descending

**Future (not in V1):**
- Click column headers to sort by confidence, quality, last reviewed, etc.

---

## Refresh Strategy

- **Initial load**: Render from fixture (prototype) or fetch all 14 symbols (production)
- **Manual refresh**: Button in header
- **Auto-refresh**: Every 5 minutes (confidence/quality may change as market moves)
- **Search**: Real-time (no refresh needed, filters existing data)

---

## Edge Cases

### Search returns empty
- Show: "No symbols found for '[search term]'. [Clear search]"

### No starred symbols
- Star column still shows, just empty for all rows

### Symbol with INSUFFICIENT_DATA
- Action shows as "INSUFFICIENT_DATA" (action vocab)
- Confidence shows as "0.0"
- Quality shows as "MISSING"

### All symbols have same confidence
- Secondary sort by symbol name (alphabetical) for stability

---

## Accessibility & Mobile

- **Tab order**: Search input → table rows (each row is tab-stop)
- **Keyboard**: Arrow keys to move between rows, Enter to open modal, Escape to clear search
- **Mobile (<640px)**: 
  - Search input spans full width
  - Table becomes scrollable horizontally
  - Or: Convert to card layout (Symbol | Company | Action | Confidence on each card)
- **Screen reader**: Each row announced as "AAPL, Apple Inc., Accumulate, 82% confidence, Usable data quality, reviewed July 20"

---

## SymbolModal (Reusable Component)

Appears when clicking any watchlist row. Same modal used on Dashboard top-6 buttons.

```
┌──────────────────────────────────┐
│ AAPL - Apple Inc.          [X]   │
├──────────────────────────────────┤
│                                  │
│ Action: ACCUMULATE               │
│ Confidence: 82% (max by quality) │
│                                  │
│ "Cloud & AI infrastructure       │
│  segment continues compound     │
│  at high quality score."         │
│                                  │
│ Top factors:                     │
│ • Momentum (12-1): Rank 3 / 14   │
│ • Quality (FCF): Rank 5 / 14     │
│                                  │
│ [View Full Analysis →]           │
│                                  │
└──────────────────────────────────┘
```

**Data for modal:**
- Symbol, company name
- Action, confidence
- 1–2 sentence summary (from evidence card)
- Top 2–3 factor scores with ranks
- Button: "View Full Analysis" (→ `/my-stocks/{SYMBOL}/research`)

---

## Prototype Acceptance Criteria

- [ ] All 14 symbols display in table
- [ ] Search filters by symbol and company (case-insensitive)
- [ ] Click row opens SymbolModal with correct data
- [ ] "View Full Analysis" navigates to `/my-stocks/{SYMBOL}/research`
- [ ] Action badges show correct colors
- [ ] Quality badges show correct icons
- [ ] Star toggle works (UI only, no persistence required)
- [ ] Pending badge shows on applicable rows
- [ ] Table responsive on mobile (scrollable or card layout)
- [ ] Sort order correct (starred first, then by confidence)

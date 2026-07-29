# Brain-Journal Spec

> Two main interfaces: (1) 3D/2D graph visualization of how notes connect (neurons), (2) Journal section with folder hierarchy, searchable entries, and automatic completeness validation.
> Reference: `fixtures/brain-journal.json`

---

## Purpose

**Visual learning loop**: See how notes and journal entries interconnect:
- **Graph view**: 2D interactive network (prototype) showing all journal entries as nodes, frontmatter connections as edges
- **Click a node** → 5-second detail popup → returns to graph
- **Journal section**: Full CRUD on entries, organized by PARA (Projects/Areas/Resources/Archives) + template type

---

## Layout (Two Modes)

### MODE 1: Graph View (Default)

```
┌──────────────────────────────────────────────────────────┐
│ research_data | Dashboard | ... Brain-Journal [⚙ Settings]│
├──────────────────────────────────────────────────────────┤
│                                                            │
│ Brain — Knowledge Graph                                  │
│ [Graph] [Journal] [Research] [Test Viz]                 │
│ [← Sidebar toggle]                                        │
│                                                            │
│ ┌──────────────────────────────────────────────────────┐│
│ │                                                      ││
│ │       [Node: Test Success]                           ││
│ │              |                                       ││
│ │    [Momentum/Quality]--[OOS Gate Results]            ││
│ │              |                  |                    ││
│ │        [NVDA Entry]          [Promotion]             ││
│ │              |                  |                    ││
│ │      [Paper Position]----[Risk Assessment]           ││
│ │              |                  |                    ││
│ │           [\  /]---- [Feature Review]                ││
│ │                                                      ││
│ │ (2D network, click node for 5-sec detail, hover pan) ││
│ │                                                      ││
│ │ Node colors:                                         ││
│ │ 🟢 Success | 🔴 Failure | 🟡 Evergreen | 🔵 Research ││
│ │                                                      ││
│ └──────────────────────────────────────────────────────┘│
│                                                            │
│ Sidebar (floating, click ← to toggle):                   │
│ ┌──────────────────────┐                                 │
│ │ [Graph Nodes: 24]    │                                 │
│ │                      │                                 │
│ │ View: [Graph]        │                                 │
│ │       [Journal]      │                                 │
│ │       [Research]     │                                 │
│ │       [Test Viz]     │                                 │
│ │                      │                                 │
│ │ Connections: 47      │                                 │
│ │ Last entry: 2h ago   │                                 │
│ └──────────────────────┘                                 │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

### MODE 2: Journal View (Click [Journal] tab)

```
┌──────────────────────────────────────────────────────────┐
│ research_data | Dashboard | ... Brain-Journal [⚙ Settings]│
├──────────────────────────────────────────────────────────┤
│                                                            │
│ Brain — Journal                                          │
│ [Graph] [Journal] [Research] [Test Viz]                 │
│                                                            │
│ [← Sidebar]  [Search: ___________________]               │
│              [Templates ▼] [Date range ▼]                │
│                                                            │
│ ┌─────────────────────┐ ┌──────────────────────────────┐ │
│ │ FOLDER HIERARCHY    │ │ RECENT ENTRIES               │ │
│ │ (left 30% - read)   │ │ (right 70% - read-only feed)│ │
│ ├─────────────────────┤ ├──────────────────────────────┤ │
│ │ ▼ Projects          │ │ [📌 PINNED]                 │ │
│ │   ► Quality+Momt    │ │ Test Success: quality_momt  │ │
│ │   ► Momentum Only   │ │ 2026-07-20 | #promotion     │ │
│ │                     │ │ "Spec passed all gates..."  │ │
│ │ ▼ Areas             │ │                             │ │
│ │   ► Research        │ │ [📊 RESEARCH]               │ │
│ │   ► Learning        │ │ Factor Correlation Study    │ │
│ │   ► Paper Trading   │ │ 2026-07-19 | #research      │ │
│ │                     │ │ "Analyzed 12m correlation..." │ │
│ │ ▼ Resources         │ │                             │ │
│ │   ► Concepts        │ │ [⚠️ FAILURE]                │ │
│ │   ► References      │ │ Monte Carlo Gate Failed     │ │
│ │                     │ │ 2026-07-19 | #failure       │ │
│ │ ▼ Templates         │ │ "5th-percentile return..."  │ │
│ │   ✓ Test Success    │ │                             │ │
│ │   ⚠ Test Failure    │ │ [+ Create new entry]        │ │
│ │   ✓ Ingestion       │ │                             │ │
│ │   ✓ Paper Trading   │ │ [Show more ↓]               │ │
│ │   🔔 Evergreen      │ │                             │ │
│ │   📚 MOC             │ │                             │ │
│ │                     │ │                             │ │
│ │ [+ New folder]      │ │ Showing 5 of 24 entries     │ │
│ │ [+ New entry ▼]     │ │                             │ │
│ │ (pick template)     │ │                             │ │
│ └─────────────────────┘ └──────────────────────────────┘ │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

---

## Component Tree

```
BrainJournalPage
├── Header (global)
├── PageTitle: "Brain — Knowledge Graph"
├── TabBar ([Graph] [Journal] [Research] [Test Viz])
├── SidebarToggle (← arrow)
├── MainView (tab-dependent)
│   ├── IF Graph:
│   │   └── InteractiveGraph (2D network)
│   │       └── Nodes × N
│   │           └── OnClick: DetailPopup (5 sec)
│   │
│   └── IF Journal:
│       ├── SearchBar (tags, dates, content)
│       ├── FilterButtons (Templates, Date range)
│       ├── TwoColumnLayout
│       │   ├── LeftPanel: FolderHierarchy
│       │   │   ├── PARAFolders (Projects, Areas, Resources, Archives)
│       │   │   ├── TemplateFolders (Test Success, Failure, Ingestion, etc.)
│       │   │   ├── CreateNewFolder (interactive)
│       │   │   └── CreateNewEntry (dropdown to pick template)
│       │   │
│       │   └── RightPanel: RecentEntryFeed
│       │       ├── PinnedSection
│       │       ├── EntryCards (template-colored badges)
│       │       │   ├── Title + date
│       │       │   ├── Tags
│       │       │   ├── Excerpt (first 2 lines)
│       │       │   └── OnClick: ExpandInline or Modal
│       │       └── ShowMorePagination
│       │
│       └── Sidebar (floating, triggered by toggle)
│           └── Tabs (same structure as Bots-Hub: replace content)
│               ├── Ingestion Log
│               ├── Paper Trading Log
│               ├── Research Findings
│               └── Test Results Log
│
└── Sidebar (always floating on left, collapsible)
    ├── ViewToggle (Graph | Journal | Research | Test Viz)
    ├── Stats (Total nodes, connections, last entry time)
    └── Quick actions
```

---

## Data Shape (Fixture Excerpt)

```json
{
  "brain_journal": {
    "as_of": "2026-07-20T14:30:00Z",
    "graph": {
      "nodes": [
        {
          "node_id": "entry-nvda-test-success-001",
          "title": "quality_momentum_tilt_top3 passed all gates",
          "template_type": "TEST_SUCCESS",
          "date": "2026-07-20T06:45:00Z",
          "tags": ["promotion", "nvda", "quality-momentum"],
          "excerpt": "Spec passed OOS/MC/WF/DSR. Outperformance vs VOO solid...",
          "color": "success_green",
          "position": { "x": 100, "y": 150 }
        },
        {
          "node_id": "entry-jpm-test-failure-001",
          "title": "momentum_only failed at Monte Carlo gate",
          "template_type": "TEST_FAILURE",
          "date": "2026-07-19T19:00:00Z",
          "tags": ["failure", "jpm", "momentum-only"],
          "excerpt": "5th-percentile return came in negative (-3.2%)...",
          "color": "failure_red",
          "position": { "x": 300, "y": 200 }
        }
        // 22 more...
      ],
      "edges": [
        {
          "from_node_id": "entry-nvda-test-success-001",
          "to_node_id": "entry-nvda-promotion-decision-001",
          "relationship": "leads_to",
          "weight": 1
        },
        {
          "from_node_id": "entry-jpm-test-failure-001",
          "to_node_id": "entry-jpm-critic-review-001",
          "relationship": "causes",
          "weight": 1
        }
        // 45 more...
      ]
    },
    "journal": {
      "folder_hierarchy": {
        "projects": [
          {
            "folder_id": "proj-quality-momentum",
            "name": "Quality + Momentum Tilt",
            "entries": [
              {
                "entry_id": "entry-nvda-test-success-001",
                "title": "quality_momentum_tilt_top3 passed all gates",
                "template_type": "TEST_SUCCESS",
                "date": "2026-07-20T06:45:00Z",
                "tags": ["promotion", "nvda", "quality-momentum"],
                "excerpt": "...",
                "completeness_check_passed": true,
                "required_fields": ["test_result", "gate_diagnostics"],
                "missing_fields": []
              }
              // more entries
            ]
          }
          // more projects
        ],
        "areas": [
          {
            "folder_id": "area-research",
            "name": "Research",
            "entries": []
          }
        ],
        "resources": [],
        "archives": []
      },
      "templates": {
        "TEST_SUCCESS": {
          "required_fields": ["spec_name", "all_gates_passed", "demo_eligible"],
          "optional_fields": ["strategy_notes", "next_steps"],
          "completeness_rule": "all required fields filled"
        },
        "TEST_FAILURE": {
          "required_fields": ["spec_name", "failed_gate", "reason"],
          "optional_fields": ["diagnostics", "suggested_fix"],
          "completeness_rule": "all required fields filled + reason non-empty"
        },
        "PAPER_TRADING": {
          "required_fields": ["symbol", "entry_date", "exit_date", "pnl"],
          "optional_fields": ["lessons", "next_entry_logic"],
          "completeness_rule": "entry/exit dates filled"
        },
        "INGESTION": {
          "required_fields": ["provider", "symbols_count", "status"],
          "optional_fields": ["issues", "resolution"],
          "completeness_rule": "all required fields filled"
        },
        "EVERGREEN": {
          "required_fields": ["concept", "status"],
          "optional_fields": ["related_entries", "last_reviewed"],
          "completeness_rule": "status is 'sprout' or higher"
        },
        "MOC": {
          "required_fields": ["topic", "entry_links"],
          "optional_fields": ["narrative"],
          "completeness_rule": "entry_links non-empty"
        }
      },
      "recent_entries": [
        {
          "entry_id": "entry-nvda-test-success-001",
          "title": "quality_momentum_tilt_top3 passed all gates",
          "template_type": "TEST_SUCCESS",
          "date": "2026-07-20T06:45:00Z",
          "tags": ["promotion", "nvda", "quality-momentum"],
          "excerpt": "Spec passed OOS/MC/WF/DSR. Outperformance vs VOO solid...",
          "folder": "proj-quality-momentum",
          "is_pinned": true,
          "content": "Full markdown content here...",
          "frontmatter": {
            "spec_id": "5f003778-42bc-4d8a-ac12-839699d98a02",
            "status": "promotion",
            "related_tests": ["test-run-001"],
            "links": ["entry-nvda-promotion-decision-001"]
          },
          "completeness_check_passed": true
        },
        {
          "entry_id": "entry-jpm-test-failure-001",
          "title": "momentum_only failed at Monte Carlo gate",
          "template_type": "TEST_FAILURE",
          "date": "2026-07-19T19:00:00Z",
          "tags": ["failure", "jpm", "momentum-only"],
          "excerpt": "5th-percentile return came in negative (-3.2%)...",
          "folder": "proj-momentum-only",
          "is_pinned": false,
          "completeness_check_passed": true
        }
        // 22 more...
      ]
    }
  }
}
```

---

## Interactions

### Graph View

**Click a node:**
- Pops up a 5-second detail card above/beside the node
- Shows: template type, title, date, tags, excerpt
- Automatically collapses after 5 seconds (no manual close needed)
- Or: User can click another node to dismiss and jump to new detail

**Hover a node:**
- Slight glow/highlight
- Tooltip: title + date

**Hover an edge:**
- Highlights the edge and both connected nodes
- Shows relationship label (leads_to, causes, etc.)

**Pan/zoom:**
- Drag to pan
- Scroll to zoom in/out
- Double-click to reset view

**Sidebar toggle:**
- Click ← arrow to hide/show sidebar
- Sidebar shows at 30% width when visible, floats over graph

### Journal View (Left Panel: Folder Hierarchy)

**Expand/collapse folders:**
- Click folder name to expand/collapse
- Shows entries under that folder

**Click folder:**
- Highlights it, filters right panel to show only entries in that folder

**Drag entries (future):**
- Prototype: read-only (no drag)
- Production: drag to move between folders

**Create new folder:**
- Click [+ New folder] → modal with name input
- Creates under selected parent or root

**Create new entry:**
- Click [+ New entry ▼] → dropdown to pick template
- Opens form based on template (with required/optional field validation)
- On submit: entry goes to the selected folder if one is highlighted
- Entry must pass completeness check to appear in recent feed

### Journal View (Right Panel: Recent Entries)

**Search:**
- Real-time filter by tags, dates, content
- Example: type "nvda" → shows only entries with "nvda" in title/content/tags

**Filter buttons:**
- [Templates ▼] → show only entries of selected template type(s)
- [Date range ▼] → filter by date (Last 7d, 30d, All)

**Entry card:**
- Click to expand inline (shows full content + frontmatter)
- Or: Click title link to open in modal or detail view
- Hover: show edit/delete icons (prototype: read-only, no actual edits)

**Pinned entries:**
- Show at top in a separate "Pinned" section
- Click star icon to pin/unpin
- Appears in graph as highlighted nodes

**Show more pagination:**
- "Show more ↓" at bottom to load next 10 entries
- Or: Infinite scroll

### Completeness Validation

**When creating/editing entry:**
- Form shows expandable "Completeness Check" legend:
  ```
  TEST_SUCCESS template requires:
  ✓ Spec name (filled)
  ✗ All gates passed (required, not filled)
  ✗ Demo eligible (required, not filled)
  ```
- Fields marked as required are highlighted
- Submit button disabled until all required fields filled
- If template has "rule", show it (e.g., "All required fields must be filled")

**After entry saved:**
- If passes check: entry appears in recent feed immediately
- If fails check: entry saved as draft, visible in folder but not in recent feed
- A banner shows: "Entry saved as draft — missing X required fields. [Complete now]"

### Sidebar (Floating, Toggled by Arrow)

Similar to Bots-Hub: tab-based
- Tabs: Ingestion Log | Paper Trading Log | Research Findings | Test Results Log
- Each tab shows a log/list related to that section
- Click tab to swap content (not stack)

---

## Refresh Strategy

- **Graph view**: No refresh (static until new entries added)
- **Journal view**: No auto-refresh (entries are append-only)
- **Recent entries feed**: Manual refresh button only (re-fetches to show new entries from other sources)
- **Search/filters**: Real-time (client-side filtering on loaded data)

---

## Edge Cases

### No entries yet
- Graph shows: "No entries yet. Create your first journal entry to start building the brain."
- Journal shows: "No entries. [Create first entry →]"

### Entry with broken frontmatter link
- Graph still shows node, but edge to missing node is grayed out with "?" label
- Right panel shows warning: "This entry links to a missing entry (id: xxxx). [Restore link]"

### Search matches zero entries
- Recent feed shows: "No entries found for '[search]'. [Clear search]"

### Entry fails completeness check
- Appears in folder tree but not in recent feed
- Tag or badge shows "DRAFT" or "INCOMPLETE"
- User can filter by "[Show drafts]" to find them

### Template definition changes
- Entries created under old template version still appear with old schema
- Warning banner (future): "This entry uses an old template version. [Migrate]"

---

## Accessibility & Mobile

- **Tab order**: Search bar → template filters → left folder panel → right entry feed
- **Keyboard**: Arrow keys to navigate folders/entries, Enter to expand/collapse, Escape to close detail popup
- **Graph controls**: Keyboard zoom (+ / -), drag with mouse
- **Mobile (<640px)**:
  - Sidebar always collapsed (toggle on hamburger)
  - Graph takes full width (touch-friendly pan/zoom)
  - Journal view: single column (folders above, entries below, stack vertically)
  - Folder tree becomes accordion (easier to navigate)
- **Screen reader**: 
  - Graph: "Node: quality_momentum_tilt_top3 passed all gates, test success template, July 20. Connected to 2 other nodes."
  - Entry: "quality_momentum_tilt_top3 passed all gates, test success, July 20, pinned, tags: promotion, nvda, quality-momentum"

---

## Prototype Acceptance Criteria

- [ ] Graph renders as 2D network with ≥5 nodes
- [ ] Nodes have correct colors per template type
- [ ] Click node shows 5-second detail popup
- [ ] Pan/zoom works on graph (drag, scroll)
- [ ] Sidebar toggle hides/shows sidebar
- [ ] Journal view shows folder hierarchy (PARA + templates)
- [ ] Click folder highlights it and filters right panel
- [ ] Recent entries feed shows 5–10 entries, rest via "Show more"
- [ ] Search filters entries real-time
- [ ] Template filter works (shows only selected types)
- [ ] Date range filter works
- [ ] [+ New entry] dropdown shows all 6 templates
- [ ] Create entry form shows required/optional fields per template
- [ ] Form shows completeness check legend (expandable)
- [ ] Entry card expands to show full content
- [ ] Pinned badge shows on pinned entries
- [ ] Completeness check validates before allowing create (button disabled if incomplete)
- [ ] Failed entry shows as draft in folder, not in recent feed
- [ ] Sidebar (floating) has tabs that swap content
- [ ] Responsive down to 375px (single column, accordion folders)
- [ ] No broken links between entries

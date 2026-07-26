Perfect! This is **much** clearer and more focused. I can see the vision now - you want an operational dashboard with a minimal, header-driven interface. Let me make sure I understand correctly by asking some clarifying questions, then we can map out each page in detail.

## **Clarifications & Questions**

### **1. Information Architecture / Header Navigation**

You mentioned these sections:
- **Dashboard** (landing, operational overview)
- **Tests** (gate results / strategy backtests?)
- **Brain - Journal** (vault notes with frontmatter)
- **Ingestion/Agents/Bots Hub** (LLM operations, ingest logs)
- **Strategies** (4-gate loop visualization + logs)
- **My Stocks** (paper trading positions + indicators)

**Questions:**
- Should **Watchlist** be part of Dashboard, or its own header item?
- For **Tests** — is this showing the 4-gate promotion flow (OOS → MC → WF → DSR) with pass/fail status?
- For **Strategies** — should this show *all tested specs* or just *active/promoted specs*?
- Are there any other sections you're thinking of that aren't listed?

---

### **2. Dashboard - "Today's Section" / Watchlist**

You said:
> "Today's section - lists each and every possible trade that needs to be made based on the AI suggestions. These are going to be the most crucial ones."

**Questions:**
- Does "today's section" mean trades recommended for *today specifically*, or the *next N days*?
- Should this list be sorted by: confidence? urgency? Sharpe projection? something else?
- For the **top 5 trades** shown as "short buttons" — what info is in the button? Just `[AAPL - Accumulate]` or `[AAPL - Accumulate - 73% conf]`?
- On hover, what summary do you want? Just action + confidence, or also momentum/quality scores?

---

### **3. Watchlist (on Dashboard)**

You said:
> "Watchlist suggested would be for the top 5 trades to take place but visible in detail only when clicked on... symbol should not be a separate header, it comes under watchlist when clicked on."

**Questions:**
- Should the watchlist **always show top 5**, or is it configurable (show top 10? show all 14)?
- When you click a watchlist item, does it **modal-overlay** the evidence card, or does it **replace the dashboard view** (full page)?
- Should the watchlist show: `Symbol | Company | Action | Confidence | Last Reviewed`? Or different columns?
- Should there be a **"View Full Watchlist"** link that shows all 14 symbols beyond the top 5?

---

### **4. Dashboard - Operational Metrics**

You said the dashboard shows:
- What have bots been up to?
- What ingestion was completed?
- What human steps are required?
- Paper trading P&L
- Strategies tested/running
- Cost/plans/bots/agents tracking

**Questions:**
- **"What bots/ingestion was completed?"** — should this show last ingest timestamp + status (e.g., "Polygon: 3 hours ago ✓ | Tiingo: 5 hours ago ⚠️")?
- **"Human steps required"** — is this like "5 specs awaiting approval" or "3 lessons to journal"?
- **"Paper trading P&L"** — should this show: total unrealized? today's? month-to-date? vs VOO?
- **"Cost/plans/bots tracking"** — is this tracking API costs? Subscription costs? Something else?
- Should the dashboard have **real-time updates**, or is it refreshed on page load?

---

### **5. "My Stocks" Page (Paper Trading Hub)**

You said:
> "Paper trades being taken place at what specific stocks time/pov. I want this to have indicators/etc. This should be working for each and any stock that I want to take a view at."

**Questions:**
- Should this show: open positions + closed positions + all positions?
- For each position, what do you want: entry date/price? exit date/price? P&L? Spec ID? Related strategy?
- **"Indicators/etc"** — do you mean: price chart with SMA/RSI/Bollinger? Or just price context?
- Should there be a **filter** (e.g., "Show only NVDA")?
- Should this sync with the **Brain - Journal** (i.e., click a position → see related lessons)?

---

### **6. Brain - Journal Page**

You said:
> "Visualization of all the notes existing inside & a way to interact with each in a small way: frontmatter"

**Questions:**
- Should this be a **timeline** of vault notes (like Discord history), or a **card grid**?
- By "interact with frontmatter" — do you mean: edit title/tags inline? Or just view them?
- Should you be able to **create new journal entries** from the UI, or is it read-only vault mirror?
- Should this be **searchable/filterable** by tag or date?

---

### **7. Ingestion/Agents/Bots Hub**

You said this is the **"main AI operations"** page.

**Questions:**
- Should this show:
  - Live ingest status (Polygon/Tiingo running now?)
  - LLM analyst/critic activity (last card generated when?)
  - Factor calculation progress?
  - Gate test runs (which specs are mid-test?)
- Should there be **logs** or just **status summaries**?
- Can you **trigger actions** from this page (e.g., "Run ingest now")?

---

### **8. Strategies Page**

You said:
> "The 4-step loop taken place and what passed in detail - logs"

**Questions:**
- Should this show **one strategy at a time** or **compare multiple strategies**?
- For a single strategy, should the view be:
  - A **diagram** of the 4 gates with pass/fail status?
  - A **table** of test runs with dates/Sharpe scores?
  - **Both** (diagram + expandable logs)?
- Should logs be **collapsible** (too much noise?) or always visible?

---

### **9. Data Freshness & Interactivity**

**Questions:**
- Should the dashboard auto-refresh (e.g., every 5 minutes)?
- Can you **manually trigger** ingest/analysis from the UI, or is it CLI-only?
- Should you be able to **pause/stop** running processes?
- Should **errors block the UI** or show as warnings?

---

## **What I'm Starting to See**

Based on your feedback, I'm picturing:

```
┌──────────────────────────────────────────────────────────────────┐
│ research_data │ Dashboard │ Tests │ Brain-Journal │ Bots-Hub │  │
│               │           │       │               │          │  │
│ [Logo/Title]  [Nav items above]                        [Settings] │
└──────────────────────────────────────────────────────────────────┘
│                                                                    │
│ MAIN DASHBOARD VIEW (scrollable)                                 │
│                                                                    │
│ ┌─ TODAY'S CRITICAL TRADES ──────────────────────────────────┐  │
│ │                                                             │  │
│ │ [AAPL - Accumulate]  [MSFT - Hold]  [NVDA - Watch]        │  │
│ │ [GOOGL - Reduce]     [AMZN - Avoid]                       │  │
│ │                                                             │  │
│ └─────────────────────────────────────────────────────────────┘  │
│                                                                    │
│ ┌─ WATCHLIST (Top 5) ────────────────────────────────────────┐   │
│ │ Symbol │ Company │ Action │ Confidence │ Last Review     │   │
│ │ AAPL   │ Apple   │ Hold   │ 82%        │ Jul 20, 2026    │   │
│ │ MSFT   │ Microsoft│ Accum  │ 73%        │ Jul 20, 2026    │   │
│ │ [etc]                                                    │   │
│ │ [View Full Watchlist →]                                 │   │
│ └────────────────────────────────────────────────────────────┘   │
│                                                                    │
│ ┌─ BOT/INGEST STATUS ────────────────────────────────────────┐   │
│ │ Polygon: Last 3h ago ✓ │ Tiingo: Last 5h ago ⚠️ │ FMP: 1h  │   │
│ │ Paper trades: P&L +$2,430 (vs VOO: +$1,850)               │   │
│ │ Pending human: 3 specs awaiting approval                  │   │
│ └────────────────────────────────────────────────────────────┘   │
│ [etc.]                                                             │
```

**Is this directionally correct?**

Once you clarify these questions, I can map out **each page** in detail with actual component layouts, data flows, and interactions.
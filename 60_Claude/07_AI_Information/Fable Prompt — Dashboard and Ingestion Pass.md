---
type: project
status: active
created: 2026-07-04
tags:
  - fable
  - dashboard
  - ingestion
next: "Send to Fable 5 — this is the second execution pass"
---
# Fable Execution Prompt — Pass 2: Dashboard Visual Rebuild + Ingestion Completion

Self-contained prompt for Fable 5 (`claude-fable-5`). Read every section before touching a file.

---

## ORIENT FIRST (same six files, same order)

1. `60_Claude/07_AI_Information/Jarvis OS — North Star.md`
2. `AGENTS.md`
3. `60_Claude/07_AI_Information/AI_CONTEXT.md`
4. `60_Claude/07_AI_Information/Session Logs/log.md` — tail of last 4 entries
5. `HUMAN_WRITING.md`
6. `00_Dashboard.md` — read the current state before touching it

---

## WHAT WAS DONE IN PASS 1 (do not redo)

- Write guard updated: allowlist (daily notes, plans, templates, skills, agents, dashboard, session log, Claude OS, clippings board) + new denials (.cursor, .kiro, .git, 05_Clippings). Verified.
- `00_Dashboard.md`: rebuilt with Meta Bind inputs, frontmatter targets, weekly DataviewJS. DataviewJS `.reduce()` bug fixed in this session (now uses `.values.reduce()`). `cssclasses: [dashboard]` added to frontmatter.
- `dashboard.css`: written and enabled. Classes: `.card`, `.card-accent`, `.stat-grid`, `.stat-tile`, `.stat-label`, `.stat-value`, `.stat-delta`, `.driver-row`, `.section-label`, `.focus-headline`. Missing: progress bar styles, multi-column support.
- `/startday` and `/closeday`: directory skills, command pointers updated.
- 5 agents: proper frontmatter.
- 10_Areas/AI/: 4 platform guides.
- Life OS.md: created (69 lines, honest stubs, needs expansion).
- Ingestion Pass 1: 21 PDFs + 11 web clips done. See below for what remains.
- `60_Claude/05_Clippings/Clippings board.md`: now in write guard allowlist. Update it after each ingestion.

---

## TASK 1 — Expand dashboard.css (via PowerShell, never Write tool)

The `.obsidian/` directory is blocked by the write guard. Use PowerShell to append to `.obsidian/snippets/dashboard.css`. Add these blocks after the existing content:

```css
/* ── Progress bar (Daily Drivers completion) ── */
.progress-wrap { margin: 6px 0 14px; }
.progress-label {
  font-size: 0.72rem;
  color: var(--text-muted);
  margin-bottom: 5px;
  font-weight: 500;
}
.progress-bar-bg {
  background: var(--background-modifier-border);
  border-radius: 4px;
  height: 7px;
  overflow: hidden;
}
.progress-bar-fill {
  background: var(--color-green);
  height: 100%;
  border-radius: 4px;
}

/* ── Multi-column tweaks (Multi-Column Markdown plugin) ── */
.columnParent {
  gap: 20px !important;
}
.columnParent .columnContent {
  padding: 0 4px;
}

/* ── Stat tile color states ── */
.stat-tile.green .stat-value { color: var(--color-green); }
.stat-tile.red .stat-value   { color: var(--color-red); }
.stat-tile.yellow .stat-value { color: var(--color-yellow); }

/* ── Section divider line ── */
.dashboard-divider {
  border: none;
  border-top: 1px solid var(--background-modifier-border);
  margin: 14px 0;
}

/* ── Callout overrides for summary/todo ── */
.callout[data-callout="summary"] {
  background: var(--background-secondary);
  border-color: var(--background-modifier-border);
}
```

Verify the file saves correctly, then reload Obsidian snippets.

---

## TASK 2 — Rebuild 00_Dashboard.md (full replace)

Replace the entire file. Keep the existing frontmatter exactly (including `cssclasses: [dashboard]`, all Meta Bind bind targets). Only replace the body.

The Multi-Column Markdown plugin is installed. Use this exact syntax for two-column layout:

```
=== start-multi-column: ID
```column-settings
Number of Columns: 2
Largest Column: left
Border: off
Shadow: off
```
[left content]
=== end-column ===
[right content]
=== end-multi-column
```

### Required body structure (top to bottom):

**1. Live date line** (full width):
```
# Jarvis — `$= moment().format("dddd, D MMMM YYYY")`
```

**2. Today's Focus callout** (full width, spans both columns):
```
> [!focus] CURRENT FOCUS
> **`INPUT[text:today_focus]`**
> `INPUT[text:today_80]`
> `INPUT[text:today_20]`
> *Patched by `/startday`, cleared by `/closeday`.*
```

**3. Multi-column section starts here:**

```
=== start-multi-column: JarvisDash
```column-settings
Number of Columns: 2
Largest Column: left
Border: off
Shadow: off
```
```

**LEFT COLUMN content:**

`## Today's Numbers` heading, then a DataviewJS block that renders actual HTML stat tiles:

```dataviewjs
const curr = dv.current();
const lc = curr.lc_today ?? 0;
const wins = curr.wins_done ?? 0;
const study = curr.study_today ?? 0;
const lcClass = lc >= 5 ? 'green' : lc > 0 ? 'yellow' : '';
const winsClass = wins >= 5 ? 'green' : wins >= 3 ? 'yellow' : '';
const container = dv.el('div', '', {cls: 'stat-grid'});
container.innerHTML = `
  <div class="stat-tile ${lcClass}">
    <div class="stat-label">LeetCode Today</div>
    <div class="stat-value">${lc}</div>
    <div class="stat-delta ${lc >= 5 ? 'positive' : 'neutral'}">target ≥5</div>
  </div>
  <div class="stat-tile ${winsClass}">
    <div class="stat-label">5-Wins</div>
    <div class="stat-value">${wins}<span style="font-size:0.85rem;opacity:0.6">/5</span></div>
    <div class="stat-delta ${wins >= 5 ? 'positive' : wins >= 3 ? 'neutral' : 'negative'}">${wins >= 5 ? '✓ GREEN' : wins >= 3 ? 'in progress' : 'behind'}</div>
  </div>
  <div class="stat-tile">
    <div class="stat-label">Study Hours</div>
    <div class="stat-value">${study}h</div>
    <div class="stat-delta neutral">today</div>
  </div>
`;
```

`## This Week` heading, then the fixed weekly totals block:

```dataviewjs
const folder = '"10_Areas/Life/Enumerate/Daily"';
const pages = dv.pages(folder).where(p => {
  if (!p.file.day) return false;
  const today = dv.date("today");
  const monday = today.minus({days: today.weekday - 1});
  return p.file.day >= monday && p.file.day <= today;
});
const lcTotal = pages.values.reduce((a,p) => a + (p.lc_count || 0), 0);
const studyTotal = pages.values.reduce((a,p) => a + (p.study_today || 0), 0);
const winsTotal = pages.values.reduce((a,p) => a + (p.wins_done || 0), 0);
const clippings = dv.pages('"60_Claude/10_Source_Summaries"')
  .where(p => {
    const monday = dv.date("today").minus({days: dv.date("today").weekday - 1});
    return p.file.ctime >= monday;
  }).length;
dv.paragraph(`**LC:** ${lcTotal}/35 · **Study:** ${studyTotal}h · **Wins:** ${winsTotal} · **Clippings this week:** ${clippings}`);
```

`## Today's Priorities` heading, then:
```dataview
TASK
FROM "10_Areas/Life/Enumerate/Daily"
WHERE file.day = date(today) AND !completed
LIMIT 8
```

`## Active Projects` heading, then:
```dataview
TABLE status, deadline, next, file.mtime AS "Updated"
FROM "20_Progress"
WHERE type = "project" AND status != "archived" AND status != "complete"
SORT deadline ASC
LIMIT 8
```

**Column separator:**
```
=== end-column ===
```

**RIGHT COLUMN content:**

`## Daily Drivers` heading, then a DataviewJS block rendering the progress bar AND habit list:

```dataviewjs
const todayStr = dv.date("today").toFormat("yyyy-MM-dd");
const todayPage = dv.pages('"10_Areas/Life/Enumerate/Daily"')
  .where(p => p.file.name === todayStr).first();
const done = (todayPage && Array.isArray(todayPage.habits_done)) ? todayPage.habits_done.length : 0;
const total = 5;
const pct = Math.round((done / total) * 100);
const wrap = dv.el('div', '', {cls: 'progress-wrap'});
wrap.innerHTML = `
  <div class="progress-label">${done} / ${total} complete · ${pct}%</div>
  <div class="progress-bar-bg"><div class="progress-bar-fill" style="width:${pct}%"></div></div>
`;
```

Then the habit callout:
```
> [!todo] Habits — check off in today's note
> - [ ] Gym (or MVP workout)
> - [ ] LeetCode ≥5
> - [ ] CSCI 2033 (30–45 min)
> - [ ] Course step (4041 / 2230 / 1103)
> - [ ] Review — run `/closeday`
```

`## Internship Pipeline` heading, then:
```dataview
TABLE status, next
FROM "10_Areas/Career/Internships"
SORT file.mtime DESC
LIMIT 5
```

`## Clippings Queue` heading, then a DataviewJS count:
```dataviewjs
const remaining = dv.pages('"60_Claude/05_Clippings"')
  .where(p => !p.file.name.includes("board") && !p.file.name.includes("README")).length;
dv.paragraph(`**${remaining}** items awaiting distillation`);
```

`## Vault Health` heading, then:
```dataview
TABLE file.folder AS Folder, file.mtime AS "Updated"
FROM "10_Areas" OR "20_Progress" OR "40_Resources" OR "60_Claude"
WHERE !type OR !status
SORT file.mtime DESC
LIMIT 8
```

**End multi-column:**
```
=== end-multi-column
```

**4. Navigation row** (full width, after the multi-column):
```
---
**System:** [[CLAUDE.md]] · [[AGENTS.md]] · [[Jarvis OS — North Star]] · [[AI_CONTEXT]] · [[HUMAN_WRITING]]
**Claude OS:** [[Claude OS]] · [[20_Progress/AI/Claude OS Dashboard|Claude OS Dashboard]] · [[10_Areas/Excalidraw/Claude OS Map|OS Map]]
**AI platforms:** [[10_Areas/AI/Claude Code|Claude Code]] · [[10_Areas/AI/Cursor|Cursor]] · [[10_Areas/AI/Kiro|Kiro]] · [[10_Areas/AI/Codex|Codex]]
**Life:** [[Life OS]] · [[10_Areas/Life/Tracking/Health Tracker|Health]] · [[10_Areas/Life/Tracking/Finance Tracker|Finance]] · [[10_Areas/Life/Plans/Summer/01 - Daily Operating System|Daily OS]]
```

### After writing, verify:
- Grep the file: confirm no `10_UMN` strings remain
- Grep for `reduce` — confirm the `.values.reduce()` form is used
- Confirm `cssclasses: [dashboard]` is still in frontmatter
- Open in Obsidian via MCP (if available) to confirm no DataviewJS render errors

---

## TASK 3 — Rebuild Claude OS Dashboard (20_Progress/AI/Claude OS Dashboard.md)

The current version is a basic markdown note with one Dataview table. Rebuild it as an actual registry dashboard. Full replace.

Frontmatter: keep existing. Add `cssclasses: [dashboard]`.

### Required structure:

**Header:**
```
# Claude OS — Operational Registry
*Last verified: `$= moment().format("YYYY-MM-DD")`*
```

**Health panel** (use the existing health check data from the note — it's accurate as of 2026-07-03):

```dataviewjs
const checks = [
  {name: 'jarvis-memory MCP',    status: '✅', detail: '8,124 notes indexed'},
  {name: 'Semantic search',       status: '❌', detail: 'chunks/embeddings unpopulated'},
  {name: 'Write guard',           status: '✅', detail: 'allowlist + denials verified, 14 payloads'},
  {name: 'Homepage plugin',       status: '✅', detail: 'opens [[00_Dashboard]] on startup'},
  {name: 'Skills on dir standard',status: '⚠️', detail: '3 of 14 (startday, closeday, ingesting-clipping)'},
  {name: 'Agents with frontmatter',status: '✅', detail: '5 of 5'},
  {name: 'Scheduled loop (Move 4)',status: '❌', detail: 'still requires manual /startday + /closeday'},
];
const container = dv.el('div', '', {cls: 'stat-grid'});
container.innerHTML = checks.map(c => `
  <div class="stat-tile">
    <div class="stat-label">${c.name}</div>
    <div class="stat-value" style="font-size:1.2rem">${c.status}</div>
    <div class="stat-delta neutral" style="font-size:0.65rem">${c.detail}</div>
  </div>
`).join('');
```

**Platform inventory table** (from existing note — preserve the verified data):

```
=== start-multi-column: ClaudeOS
```column-settings
Number of Columns: 2
Largest Column: left
Border: off
Shadow: off
```
```

LEFT: Platform inventory table (Claude Code, Cursor, Kiro, Codex — same content as existing note, properly formatted)

RIGHT: Open actions checklist (same as existing open actions)

```
=== end-column ===
[right content]
=== end-multi-column
```

**Recent setup changes** (keep existing Dataview TABLE for recently modified files in 20_Progress/AI/).

**Marketplace evaluation** (keep existing second-brain-claudekit comparison and everything-claude-code triage from Claude OS.md — link to it rather than duplicate: "Full triage in [[Claude OS]] → Marketplace Evaluation").

**Navigation:**
```
[[Claude OS]] · [[10_Areas/AI/Claude Code|Claude Code guide]] · [[10_Areas/AI/Cursor|Cursor guide]] · [[10_Areas/AI/Kiro|Kiro guide]] · [[10_Areas/AI/Codex|Codex guide]] · [[00_Dashboard]]
```

---

## TASK 4 — Life OS Expansion

Current `10_Areas/Life/Life OS.md` is 69 lines — well-written but thin. Expand each section without inventing numbers. The goal is depth and specificity in the known parts, honest stubs for the unknown.

Read `10_Areas/Life/Plans/Summer/01 - Daily Operating System.md`, `02 - Weekly Operating System.md`, `03 - Monthly & Phase Map.md`, `08 - Anti-Drift Rules.md` before expanding. Pull real content from those files rather than generalizing.

### Sections to expand:

**Physical health** — add the actual gym structure from the OS plans: which days are designated, what the MVP threshold is, what "streaks" means in practice. Add the smoking harm-reduction detail: what "frictioned, not eliminated" means as a daily protocol, not just a label.

**Finances** — expand the card setup detail and the five-bucket system. Add concrete targets: what the emergency fund target is, what "automatic recurring buys" means in execution, what the monthly review checklist looks like. The tracker format note should match `Finance Tracker.md`.

**Relationships and mentors** — don't invent names. Instead: describe the structure of what Relationship Log.md will contain once filled. What cadence looks like for a mentor vs a collaborator. The give/get framing in concrete terms.

**Career trajectory** — expand the "3 months" and "1 year" sections with the actual mechanism: what "portfolio bullet" means (format, where it lives), what "internship pipeline actively fed" means in weekly terms (number of applications, which boards). Pull from the Career plans in 10_Areas/Career/ if they exist.

**Learning arc** — expand each course with the actual subtopic sequence currently active. Read `06 - ML Fundamentals (2033 + 2230).md` and `06a - ML Fundamentals Progress.md` to get the current unit. Read `05 - LeetCode & CSCI 4041.md` + `05a - LeetCode Tracker.md` for the LC rotation.

**Rules** — expand to include the WHY behind each rule, not just the rule. Anti-Drift Rules already has this — pull the rationale into Life OS so it's complete without requiring a cross-read.

Target: 300–500 lines. Honest about what's unknown; specific about what's known.

---

## TASK 5 — Complete Remaining Ingestion

Read `.claude/skills/ingesting-clipping/SKILL.md` before starting. Output: PDFs → `60_Claude/10_Source_Summaries/PDF Ingestion/[Title].md`, web → `.../Web Ingestion/[Title].md`. Mark each processed item in `60_Claude/05_Clippings/Clippings board.md` (now allowlisted — direct write OK).

### What was already ingested (do NOT re-ingest):

**PDFs done (21):** MIT Quant Bible, BASWE 15 AI Projects, How to Pivot into AI/ML 2026, DeepThinksFinance AI Portfolio Optimizer, DeepThinksFinance Quant Prompt Guide v2, TRIBE v2 (in-silico neuroscience), Quant Foundations, AI Prediction Market Bot, Outreach Manual, 20 Free AI Certifications, 5 Best Claude Code MCPs, AI Generalist Roadmap (Outskill), Claude Code Free Ollama, Claude Code Status Bar, Free AI Receptionist Workflow, GitNexus Codebase Map, LinkedIn Search URL Cheatsheet, Maverick Prompt Shortcuts + Viral Prompts, MavGPT AI Resume Guide, Obsidian + Claude Code Codebook 12 Commands, Student Travel Discounts.

**Web clips done (11):** AI Engineer Roadmap (roadmap.sh), AI Engineering from Scratch, Claude Council Path A, Gurwinder Substack Index, Hall of Hacks Hackathon Archive, NextWork Automate AI Second Brain, Relevance AI Agents for Sales GTM, The Agent-Ready Roadmap, Hidden Operating System Behind Income Ceiling, The New Coding Interview 5 Resources, The Output Audit.

### PDFs still to ingest (in 60_Claude/05_Clippings/PDFs/):

| PDF | Signal tier | Notes |
|-----|------------|-------|
| Clone Setup Guide (June 2026).pdf | Medium | Setup guide for a dev tool — key claims + full config steps |
| Free Claude Cowork Skills.pdf | Medium | Key skills listed, actual prompt templates if any |
| Pre-Reads Kit _ Generative AI Mastermind.pdf | Medium | Extract the actual pre-read list and frameworks |
| Ultimate Guide to Winning Hackathons.pdf | Medium | Different from the web clip (that was an archive, this is a how-to) |
| Find profitable startup ideas using reddit.pdf | Low | One-paragraph summary + top 3 methods |
| Road Map.pdf | Low | Quick check first — if it's the same as "AI Generalist Roadmap — Outskill" already ingested, skip. Otherwise low-signal summary. |
| CodeRabbit_Install_Guide.pdf | Low | 2-sentence summary + install command |
| Workbooks_AI Mastermind - Links.pdf | Low | Extract the actual links list; skip boilerplate |
| @fatimahs.guide Junior Year Extracurriculars List.pdf | Low | Brief summary of extracurricular categories listed |

### Web clips still to ingest (in 60_Claude/05_Clippings/Web/):

| Clip | Signal tier | Notes |
|-----|------------|-------|
| fintech early programs that actually pay.md | Medium | Career-relevant: extract specific program names, deadlines, eligibility |
| The 2027 Internship Calendar.md | Medium | Career-relevant: extract the timeline predictions that are actionable |
| the underclassmen internship list.md | Medium | Career-relevant: extract the specific programs for CS underclassmen |
| 4 Ways to Make Money With the Hermes Agent.md | Medium | Extract the actual four methods with mechanisms |
| Where teams and agents work together.md | Medium | Read both copies — if identical, ingest once; extract the key framework |
| Where teams and agents work together 1.md | Medium | (See above) |
| Naive - Quickstart.md | Low | Read first — identify what "Naive" is; if it's a tool quickstart, 1-para + install command |
| Maverick AI Resource Hub.md | Low | Extract resource links list only; skip the pitch |
| Maverick AI Resource Hub 2.md | Low | Same |
| Maverick AI Resource Hub 3.md | Low | Same |

### Clips to SKIP entirely:
- `Magic Fretboard.md` — unrelated to any vault domain
- Any AI Conversations/ subfolder contents — internal records, not clippings

After each batch, append a checkpoint to the session log and update `Clippings board.md`.

---

## HARD CONSTRAINTS (unchanged from Pass 1)

- Never touch `60_Claude/40_Project_Briefs/TradingView/` or `50_Archive/`
- `.obsidian/` changes via PowerShell only (never Write tool)
- No hand-authored `.excalidraw` JSON
- Read `HUMAN_WRITING.md` before writing any note body
- Wikilinks: Grep before writing any `[[target]]` to confirm the file exists

---

## QUALITY GATE

Before marking any task done:
- Dashboard: open in Obsidian, confirm no DataviewJS console errors, confirm stat tiles render as visual cards (not plain text), confirm two-column layout renders correctly
- CSS: verify PowerShell write succeeded by reading the file back and checking the added classes exist
- Life OS: confirm it reads like Anant's actual situation, not a template with filled slots
- Ingestion: every source note has `## Flashcards` section with `#cards/[track]`, valid frontmatter, and is marked in Clippings board

---

## SESSION END PROTOCOL

After each task block, append to `60_Claude/07_AI_Information/Session Logs/log.md`:

```markdown
## [YYYY-MM-DD] [operation] | [deliverable]
- Files changed (specific paths)
- What works now that didn't before
- Open gaps or decisions needed
- Next action
```

At session end: update `00_Dashboard.md` `updated:` date and write a final summary log entry.

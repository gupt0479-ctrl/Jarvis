# ops

**Description:** Daily vault operations dispatcher — health checks, triage, capability audits, cadence management. Orchestrates existing skills into coherent workflows without duplicating their logic.

**Usage:** `/ops [operation]` where operation is one of: `morning-start`, `health-check`, `triage`, `ingest-batch`, `capability-audit`, `evening-close`, `full-cycle`. Invoke `/ops` alone for a time-aware suggestion.

---

## Instructions

### 1. Before Any Operation

1. Read `AI_CONTEXT.md` for the shared cross-tool manifest.
2. Read `HUMAN_WRITING.md` — all prose output follows that standard. No filler, no AI slop, concrete and compressed.
3. Read the 5 most recent entries from `60_Claude/10_Session_Logs/log.md` for carryover context.
4. If the session log does not exist, create it with frontmatter (`type: log`, `created: YYYY-MM-DD`) before appending.

### 2. Operation Menu

When `/ops` is invoked, present the available operations:

| Operation | Cost | What it does |
|-----------|------|-------------|
| `morning-start` | Standard | `/context` + `/today` + health-check + top triage + top drills |
| `health-check` | Lightweight | CLI baseline + MCP spot-checks → Ops Report |
| `capability-audit` | Lightweight | MCP search for track/drill/evidence fields → capability section |
| `triage` | Standard | Present queue, route fixes to existing skills |
| `ingest-batch` | Heavyweight | List clippings, user selects, sequential `/ingest-clipping` |
| `evening-close` | Standard | `/closeday` + capability audit summary + session log |
| `full-cycle` | Heavyweight | morning-start + evening-close bookends |

**Cost labels explained:**
- **Lightweight** — CLI summaries, Dataview-style counts, short report sections. Minimal MCP reads. Prefer paths and counts over full note bodies.
- **Standard** — Reads live context files plus notes referenced by the current triage queue. Moderate MCP usage.
- **Heavyweight** — Sequential multi-note processing, full-cycle scans, batch ingestion. Reserve for dedicated sessions. When a heavyweight operation cannot complete due to budget, suggest the next best lightweight command.

### 3. Time-of-Day Detection

When `/ops` is invoked without a subcommand:
- **Before noon:** Suggest `morning-start` — "It's morning. Run `morning-start` to get today's briefing?"
- **After noon:** Suggest `evening-close` — "It's afternoon. Run `evening-close` to wrap up the day?"
- Always let the user override with any operation.

### 4. Operation Dispatch

#### `morning-start` (Standard)

1. Run `/context` to gather current vault state.
2. Run `/today` to build the day's plan.
3. Run the Health Check (see §Health Check Engine below).
4. Run the Capability Audit (see §Capability Audit below).
5. Extract top 3 triage items and top 3 overdue drills.
6. Produce a Morning Briefing note at `60_Claude/50_Reviews/Morning Briefing - YYYY-MM-DD.md`:
   - Frontmatter: `type: plan`, `status: active`, `created: YYYY-MM-DD`, tags: `plan`, `daily`, `ops`
   - Sections: Today's Plan, Vault Health Summary, Top 3 Triage Items, Top 3 Overdue Drills
   - Link to previous day's closeday note via wikilink for continuity chain.
7. Append session log entry.

#### `health-check` (Lightweight)

1. Run the Health Check Engine (see §Health Check Engine below).
2. Generate the Ops Report (see §Report Generator below).
3. Append session log entry.

#### `capability-audit` (Lightweight)

1. Run the Capability Audit (see §Capability Audit below).
2. Output the capability health section.
3. Append session log entry.

#### `triage` (Standard)

1. Run the Health Check and Capability Audit if no current-day Ops Report exists.
2. Generate or load the Triage Queue (see §Triage Queue below).
3. Present the queue to the user.
4. For each item the user selects, route to the appropriate skill:
   - Broken links → `/connect-notes`
   - Unprocessed clippings → `/ingest-clipping` or `/ops ingest-batch`
   - Claude layer issues → `/lint-claude-layer`
   - Stale projects → present project path for manual review
   - Overdue drills → present note links for drill session
   - Encoding damage → targeted cleanup (requires user approval)
   - Missing concepts → `/connect-notes` or `/distill-note`
5. Append session log entry.

#### `ingest-batch` (Heavyweight)

1. List all files in `60_Claude/05_Clippings/`.
2. Skip files that already have a corresponding source summary (check `60_Claude/30_Source_Summaries/` for matching `source_note` links).
3. Present the list to the user. Let them select which to process and choose depth per clipping: quick summary, standard distillation, or deep analysis.
4. Process selected clippings sequentially via `/ingest-clipping`.
5. Stop after a user-configurable batch limit (default: 5) to protect context budget.
6. When backlog exceeds 10 items, group by likely topic before presenting.
7. Route produced summaries through existing promotion logic: source summary first, then concept/project/output only when the idea is reusable.
8. Append session log entry.

#### `evening-close` (Standard)

1. Run `/closeday` to create the day's closeday note.
2. Run the Capability Audit (see §Capability Audit below).
3. Append an "Evening Close" section to the day's Closeday note (do not create a separate file):
   - Capability audit summary
   - Triage items completed vs remaining (compare against morning briefing if one exists)
   - One-line vault health delta from morning
4. Append session log entry.

#### `full-cycle` (Heavyweight)

1. Run `morning-start`.
2. Inform the user: "Work session open. Re-invoke `/ops full-cycle` or `/ops evening-close` when ready to close."
3. On re-invocation, run `evening-close`.


### 5. CLI Integration

The jarvis-cli at `30_Order/System/jarvis-cli/jarvis.ps1` is the primary scan tool. It reads every `.md` file, parses frontmatter, and produces deterministic counts in seconds at zero token cost.

**Available CLI commands:**
- `jarvis.ps1 health` — metadata gaps, inbox counts, project health
- `jarvis.ps1 links` — broken and ambiguous wikilinks
- `jarvis.ps1 dates` — future-dated metadata fields
- `jarvis.ps1 encoding` — mojibake and text corruption
- `jarvis.ps1 context` — first-pass context pack
- `jarvis.ps1 projects` — project status and missing `next` actions
- `jarvis.ps1 report` — full CLI report
- `jarvis.ps1 enrich-candidates` — notes eligible for Capability Engine enrichment
- Add `--include-tools` to scan `.claude/`, `.cursor/`, `.kiro/` folders

**CLI-first policy:**
1. Always attempt CLI before MCP for baseline scans.
2. Parse CLI output as diagnostic input — never treat it as permission to auto-rewrite notes.
3. Use MCP only for the semantic layer the CLI cannot provide: content search, Capability Engine field interpretation, note reading for context, and vault writes.

**CLI fallback:**
- If `jarvis.ps1` fails or is unavailable (e.g., no Python, no shell access), fall back to MCP-based scanning.
- Log the fallback reason to the session log: "CLI unavailable: [reason]. Falling back to MCP search."
- MCP fallback uses `obsidian_global_search` for metadata gaps, `obsidian_list_notes` for folder counts, and `obsidian_read_note` for targeted checks.
- Note in the Ops Report that CLI was not used so the user knows the scan was MCP-only.

### 6. MCP Retry Policy

When an Obsidian MCP tool call fails:
1. If the error is a connection or timeout error, retry once.
2. If the retry also fails, log the failure to the session log: "MCP call failed: [tool_name] — [error]. Skipped after retry."
3. Continue with remaining operations. Do not abort the entire workflow for a single MCP failure.
4. Note any skipped dimensions in the Ops Report.

### 7. Error Handling

If any sub-skill or sub-operation fails during a composite workflow:
1. Log the error to `60_Claude/10_Session_Logs/log.md` with the operation name and error description.
2. Skip the failed step.
3. Continue with remaining operations.
4. Include a "Skipped Steps" note in the final output so the user knows what was missed.
5. When a heavyweight operation cannot complete, suggest the next best lightweight command as a fallback.

### 8. Skill References

This skill orchestrates existing skills by name. It does not duplicate their logic.

| Skill | When ops invokes it |
|-------|-------------------|
| `/context` | morning-start (vault state gathering) |
| `/today` | morning-start (day plan) |
| `/closeday` | evening-close (daily summary) |
| `/ingest-clipping` | ingest-batch (per-clipping processing) |
| `/connect-notes` | triage (broken link fixes, missing concepts) |
| `/lint-claude-layer` | triage (Claude layer issues) |
| `/distill-note` | triage (missing concept creation) |
| `/weekly-review` | referenced in evening-close for weekly context |

---

## Health Check Engine

The health check scans seven dimensions. CLI provides the deterministic baseline; MCP fills the semantic gaps the CLI cannot reach.

### Scan Dimensions

| Dimension | Primary Source | Fallback |
|-----------|---------------|----------|
| Frontmatter completeness | CLI `health` (metadata gaps count) | MCP search for notes missing `type`/`status`/`created` |
| Link integrity | CLI `links` (broken + ambiguous counts) | MCP search for `[[` patterns |
| Inbox/clippings backlog | CLI `health` or MCP `list_notes` on `00_Inbox/` and `60_Claude/05_Clippings/` | Direct folder listing |
| Project staleness | CLI `projects` (missing `next`, stale dates) | MCP search in `20_Progress/` |
| Capability Engine gaps | MCP search for `track` field, check `next_drill` dates | Read Capability Dashboard |
| Date consistency | CLI `dates` (future-dated fields) | MCP frontmatter reads |
| Encoding integrity | CLI `encoding` (mojibake hits) | Skipped if CLI unavailable |

### Execution Sequence

1. Run CLI commands for the deterministic baseline. Parse output as diagnostic input — do not paste it verbatim into reports.
   - `jarvis.ps1 health` → metadata gaps, inbox counts, project health
   - `jarvis.ps1 links` → broken and ambiguous wikilinks
   - `jarvis.ps1 dates` → future-dated metadata fields
   - `jarvis.ps1 encoding` → mojibake and text corruption
2. Parse CLI output into per-dimension counts.
3. Run MCP searches for dimensions the CLI cannot cover:
   - Search for notes missing `type`/`status`/`created` fields (supplements CLI metadata gaps).
   - Check Capability Engine fields: `track`, `mastery_level`, `next_drill`, `evidence`.
   - Read specific notes for context when CLI flags them.
4. Combine CLI + MCP findings into a structured findings object.
5. Pass findings to the Report Generator (see §Report Generator).

### CLI-to-Ops Field Mapping

Map CLI output fields to Ops Report dimensions and priority:

| CLI output field | Ops Report dimension | Priority mapping |
|-----------------|---------------------|-----------------|
| Metadata gaps | Frontmatter Drift | Critical if `type`/`status` missing |
| Future-dated fields | Date Consistency | High if in active notes |
| Missing project `next` | Project Health | High |
| Broken wikilinks | Link Health | Critical for active notes, low for archive |
| Ambiguous wikilinks | Link Health | Medium |
| Duplicate filenames | Knowledge Graph Quality | Medium for durable, low for course notes |
| Encoding hits | Encoding Integrity | High for contracts/dashboards, low for archive |

### Date Consistency Check

Compare `created`, `updated`, `reviewed`, `last_drilled`, and `next_drill` against the actual current date.

- Future-dated `updated` → flag as metadata drift. This makes stale notes look fresh to dashboards and Dataview queries.
- Future-dated `next_drill` alone → not an error. This is scheduled future work. Only flag if the paired `last_drilled` is also in the future or inconsistent (e.g., `last_drilled` after `next_drill`, or `last_drilled` after today).
- Session log entries dated after the actual current date → surface as "timeline inconsistency" in the Ops Report.
- Distinguish scheduled future work (legitimate `next_drill`, planned review dates) from impossible history (future `created`, future `updated`, future `last_drilled`).

### Encoding Integrity Check

Scan for mojibake sequences: broken smart punctuation (`â€™`, `â€œ`), broken arrows (`â†`), UTF-8 marker artifacts (`Â`, `Ã`), and similar corruption patterns.

Rank findings by hit count and folder sensitivity:
- **High priority:** contracts (`CLAUDE.md`, `AI_CONTEXT.md`), dashboards, templates, active project notes in `20_Progress/`. These affect daily retrieval and AI behavior.
- **Low priority:** `50_Archive/`, `60_Claude/05_Clippings/` — unless the damaged file is actively linked from a current dashboard or project note.

Never auto-repair encoding damage. Report only. Targeted cleanup requires explicit user request and routes through the triage queue.

### Backlog Threshold

- Flag when `00_Inbox/` exceeds 10 items.
- Flag when `60_Claude/05_Clippings/` exceeds 10 items.
- When either backlog exceeds the threshold, the triage queue groups items by likely topic rather than listing every file.

### Project Staleness Check

- Flag active projects with no `next:` action defined.
- Flag active projects not modified in 30+ days (by file mtime).
- Archived projects are excluded from staleness checks.

### Clean Bill of Health

When zero issues are found across all seven dimensions, report:

> ✅ Clean bill of health — all dimensions clear as of [timestamp]

Skip the per-dimension breakdown. One line is enough when nothing is wrong.

---

## Capability Audit

Queries Capability Engine state through MCP. This is a Lightweight operation — keep MCP calls minimal, use `obsidian_global_search` with targeted queries, batch reads where possible.

### MCP Search Queries

Use these targeted searches instead of reading every note:

| Query | Purpose |
|-------|---------|
| `obsidian_global_search` for `track:` | Find all tracked concepts |
| `obsidian_global_search` for `next_drill:` | Find drill-scheduled notes |
| `obsidian_global_search` for `type: output` | Find output notes |
| `obsidian_list_notes` in `60_Claude/60_Indexes/Field OS/` | Question bank state |

### Audit Checks

Run these six checks in order:

1. **Total tracked concepts** — Count notes with a non-empty `track` field. This is the engine's coverage number.

2. **Mastery distribution** — Count by `mastery_level`: novice, familiar, proficient, expert. Heavy clustering at novice means the engine is capturing but not drilling.

3. **Overdue drills** — Notes where `next_drill` < today. Sort by days overdue descending. For each, extract: note title, track, days overdue. These are the highest-signal items for the triage queue.

4. **Evidence gaps** — Notes with `track` set but `evidence` field empty or missing. Knowledge without proof artifacts — the concept exists but nothing demonstrates understanding.

5. **Stalled outputs** — Notes in `60_Claude/45_Outputs/` with `type: output` and `status: seed` where `created` is older than 14 days. Seeds that never germinated.

6. **Underseeded question banks** — For each track, check its question bank in `60_Claude/60_Indexes/Field OS/`. Flag tracks with fewer than 3 open questions. A track with no questions has no drill fuel.

### Capability Health Section Format

Output this section for inclusion in the Ops Report:

**Drill queue** — Top 5 overdue, each line: note title, track, days overdue.

```markdown
### Drill Queue
| Note | Track | Days Overdue |
|------|-------|-------------|
| [[Note Title]] | track-name | 14 |
```

**Evidence gaps** — Top 5 concepts missing evidence, each line: note title, track.

```markdown
### Evidence Gaps
| Note | Track |
|------|-------|
| [[Note Title]] | track-name |
```

**Stalled outputs** — All stalled seeds with title, status, age in days.

```markdown
### Stalled Outputs
| Note | Status | Age (days) |
|------|--------|-----------|
| [[Output Title]] | seed | 21 |
```

**Underseeded question banks** — Tracks below the 3-question threshold with track name and open question count.

```markdown
### Underseeded Question Banks
| Track | Open Questions |
|-------|---------------|
| track-name | 1 |
```

When all checks pass (no overdue drills, no evidence gaps, no stalled outputs, all banks seeded), output:

> ✅ Capability Engine healthy — all tracks active, no overdue drills as of [timestamp]

---

## Triage Queue

Converts health check and capability audit findings into a capped, prioritized action list. Each item routes to an existing skill or presents a manual action.

### Priority Levels

| Priority | Criteria | Examples |
|----------|----------|---------|
| Critical | Broken required fields, encoding in active contracts | Missing `type` on dashboard note, mojibake in `CLAUDE.md` |
| High | Stale projects, overdue drills, broken links in active notes | Project with no `next` for 30+ days, drill 14+ days overdue |
| Medium | Inbox backlog, unprocessed clippings, weak links | >10 inbox items, >10 unprocessed clippings |
| Low | Orphan notes, archive encoding, cosmetic issues | Orphan in `50_Archive/`, duplicate filename in course notes |

### Queue Cap

Maximum 15 items. When more exist, select highest-priority items first. Lower-priority items that didn't make the cut are noted as a count at the bottom of the queue ("+ N lower-priority items omitted").

### Routing Rules

Each issue type maps to a specific skill or action:

| Issue Type | Route |
|-----------|-------|
| Broken links | `/connect-notes` |
| Unprocessed clippings | `/ingest-clipping` or `/ops ingest-batch` |
| Claude layer issues | `/lint-claude-layer` |
| Stale projects | Manual review — present the project path |
| Overdue drills | Drill session — present note links |
| Encoding damage | Targeted cleanup — requires explicit user approval |
| Missing concepts | `/connect-notes` or `/distill-note` — never auto-create empty stubs |

### Stable Identifiers

Every triage item gets a stable identifier for cross-report matching: `{category}:{relative_path}:{issue_type}`

Examples:
- `frontmatter:20_Progress/UROP/index.md:missing_next`
- `drill:40_Resources/CS/AI/RAG.md:overdue_14d`
- `clippings:60_Claude/05_Clippings/:backlog_12`

Use these identifiers to match items across consecutive reports. The identifier stays the same as long as the underlying issue persists.

### Carry-Forward Logic

1. Compare current triage identifiers against the previous Ops Report's triage section.
2. Items present in both → mark as "carried forward" with a consecutive-report count.
3. Items in the previous report but not the current scan → add to the "Resolved Since Last Report" list.
4. Items appearing in **3+ consecutive reports** get priority bumped by one level (medium → high, high → critical) unless the user has explicitly deferred them.
5. Deferred items keep their original priority and are marked `[deferred]`.

### Triage Item Format

Each item is a task checkbox with priority tag, stable identifier, description, and suggested action:

```markdown
- [ ] **[critical]** `frontmatter:20_Progress/UROP/index.md:missing_next` — Project missing `next` action → review and add next step
- [ ] **[high]** `drill:40_Resources/CS/AI/RAG.md:overdue_14d` — Drill 14 days overdue → schedule drill session
- [ ] **[medium]** `clippings:60_Claude/05_Clippings/:backlog_12` — 12 unprocessed clippings → `/ops ingest-batch`
```

### Duplicate and Link Classification

Risk tiers for duplicate filenames:
- **High risk** — durable notes (evergreen, concept, project in active folders). These cause real wikilink ambiguity.
- **Medium risk** — active project notes. Path context usually disambiguates, but worth flagging.
- **Low risk** — course-week patterns (`Week - N.md`) and archive patterns where folder path is the disambiguator.

Link classification rules:
- Template placeholder wikilinks (e.g., `[[Note A]]`, `[[Related Note]]` in `.claude/skills/` or `30_Order/Templates/`) are **not** real broken links. Skip them.
- When a duplicate pair includes one enriched Capability Engine note and one feeder-layer course note, prefer linking the feeder to the enriched note over merging.
- For missing concepts, suggest `/connect-notes` or `/distill-note` rather than auto-creating empty stubs.
- Before labeling a broken link as a missing note, check common attachment locations: `attachments/`, `assets/`, and the same folder as the linking note.

### Clipping Backlog Grouping

When the clippings backlog exceeds the threshold (>10 items):

1. **Group by likely topic** before presenting. Don't dump a flat file list.
2. **Distinguish processing depth** per clipping: quick summary, standard distillation, or deep analysis.
3. **Process sequentially** with a configurable batch limit (default: 5). Stop after the limit to protect context budget.
4. **Skip already-processed clippings** — check `60_Claude/30_Source_Summaries/` for existing `source_note` links that match.
5. **Route through existing promotion logic:** source summary first, then concept/project/output only when the idea is reusable. Don't promote everything to durable knowledge.

---

## Report Generator

Produces three report types: Ops Report, Morning Briefing, and Evening Close. All output follows HUMAN_WRITING.md — tables and bullets over prose, decisions and next actions over audit narration.

### Ops Report

**File:** `60_Claude/50_Reviews/Ops Health - YYYY-MM-DD.md`

**Frontmatter:**

```yaml
---
type: review
status: complete
created: YYYY-MM-DD
tags:
  - review
  - ops-health
notes:
  - "[[60_Claude/50_Reviews/Ops Reports/latest CLI report]]"
cli_used: true/false
scan_dimensions: 7
critical_count: N
high_count: N
carry_forward_count: N
---
```

**Sections in order:**

1. **Summary Table** — One row per scan dimension: dimension name, status emoji, issue count.
2. **Frontmatter Drift** — Notes missing required fields (`type`, `status`, `created`).
3. **Link Health** — Broken and ambiguous wikilinks, classified by risk tier.
4. **Date Consistency** — Future-dated `updated`/`created`/`last_drilled` fields. Distinguish impossible history from scheduled future work.
5. **Inbox/Clippings Backlog** — Counts for `00_Inbox/` and `60_Claude/05_Clippings/`. Flag when either exceeds 10.
6. **Project Health** — Active projects missing `next:` or not modified in 30+ days.
7. **Capability Engine Health** — Drill queue, evidence gaps, stalled outputs, underseeded question banks (from §Capability Audit).
8. **Encoding Integrity** — Mojibake hits ranked by folder sensitivity.
9. **Triage Queue** — Prioritized action list (from §Triage Queue).
10. **Comparison** — Only when a prior Ops Report exists. See §Comparison Section Logic below.
11. **Resolved Since Last Report** — Items from the previous report no longer detected.

### Status Emojis

| Emoji | Meaning | Threshold |
|-------|---------|-----------|
| ✅ | Healthy | 0 issues in dimension |
| ⚠️ | Warning | 1–5 issues |
| ❌ | Critical | 6+ issues, or any broken required field (`type`/`status` missing) |

### Cross-Linking

- Every Ops Report links to the most recent CLI-generated report under `60_Claude/50_Reviews/Ops Reports/` via the `notes:` frontmatter field.
- The two report families (CLI-generated and ops-generated) cross-link but do not duplicate findings. The CLI report has raw scan output; the Ops Report adds semantic interpretation, capability audit, and triage routing.

### Morning Briefing

**File:** `60_Claude/50_Reviews/Morning Briefing - YYYY-MM-DD.md`

**Frontmatter:**

```yaml
---
type: plan
status: active
created: YYYY-MM-DD
tags:
  - plan
  - daily
  - ops
notes:
  - "[[Closeday - previous date]]"
  - "[[Ops Health - YYYY-MM-DD]]"
---
```

**Sections:**

1. **Today's Plan** — Pulled from `/today` output.
2. **Vault Health Summary** — Condensed from the health check: summary table only, no per-dimension detail unless something is critical.
3. **Top 3 Triage Items** — Highest-priority items from the triage queue with routing suggestions.
4. **Top 3 Overdue Drills** — From the capability audit, each with note title, track, and days overdue.
5. **Previous Day Link** — Wikilink to the previous day's closeday note for continuity chain.

### Evening Close

Not a separate file. Appended as a section to the day's Closeday note (created by `/closeday`).

**Sections appended:**

1. **Capability Audit Summary** — Condensed output from the evening capability audit.
2. **Triage Status** — Items completed vs remaining, compared against the morning briefing if one exists.
3. **Health Delta** — One line: what changed since the morning check. Example: "Link health improved (807→801 broken), 2 new clippings added to backlog."

### Daily Cadence Chain

Every morning briefing links to the previous day's closeday note via wikilink in the `notes:` frontmatter field. This creates a continuous chain: Morning Briefing → previous Closeday → that day's Morning Briefing → and so on. The chain is the primary continuity mechanism between sessions.

### Comparison Section Logic

When a previous Ops Report exists (search for the most recent note tagged `ops-health`):

1. **Dimension comparison** — For each scan dimension, show whether it improved (↓ fewer issues), worsened (↑ more issues), or stayed the same (→).
2. **Carried-forward items** — Triage items present in both reports, matched by stable identifier. Show the consecutive-report count.
3. **Resolved since last report** — Items in the previous report's triage queue that no longer appear in the current scan. List them as completed.

When no previous Ops Report exists, skip the Comparison section entirely. Don't fabricate a baseline.

### Report Registry

Surface the most recent of each report type so they're findable without searching:

| Report Type | Location Pattern |
|-------------|-----------------|
| Ops Report | `60_Claude/50_Reviews/Ops Health - YYYY-MM-DD.md` |
| Morning Briefing | `60_Claude/50_Reviews/Morning Briefing - YYYY-MM-DD.md` |
| Evening Close | Appended section in `60_Claude/50_Reviews/Closeday - YYYY-MM-DD.md` |
| CLI Report | `60_Claude/50_Reviews/Ops Reports/` (latest by date) |

The dashboard integration (§Dashboard Integration in `60_Claude/60_Indexes/`) uses Dataview queries against the `ops-health`, `plan`, and `daily` tags to surface these automatically. No manual registry file needed.

### Output Style

- Tables and bullet lists over paragraphs.
- Paths and counts over full note bodies.
- One-line summaries per dimension in the summary table; detail only in the per-dimension sections.
- Follow HUMAN_WRITING.md: no filler, no audit prose, decisions and next actions only.
- When all dimensions are clean, use the single-line clean bill of health from §Health Check Engine instead of generating empty sections.

---

## Session Log

Every ops operation appends a structured entry to `60_Claude/10_Session_Logs/log.md` on completion. This is the primary continuity mechanism between sessions.

### Log Entry Format

```markdown
## [YYYY-MM-DD] ops | [operation-name]

- Created: [[Ops Health - YYYY-MM-DD]], [[Morning Briefing - YYYY-MM-DD]]
- Modified: [[Closeday - YYYY-MM-DD]]
- Health: [one-line summary, e.g., "3 critical, 7 high, 12 medium — link health worst dimension"]
- Triage: [X items queued, Y carried forward]
- CLI: used/not used (jarvis.ps1 health + links + dates)
- Duration: ~N min scan + report generation
```

Adapt bullets per operation — omit lines that don't apply. A `capability-audit` entry won't have a `Created: [[Morning Briefing]]` line.

### Append Behavior

- Append to the end of the file. Never overwrite existing entries.
- Use the heading convention `## [YYYY-MM-DD] ops | [operation-name]` followed by bullet points.
- Every operation appends exactly one entry on completion, even if the operation partially failed (note what was skipped).

### Morning-Start Context Reading

- `morning-start` reads the 5 most recent session log entries before producing the briefing.
- Extract carryover items: unfinished triage, recent changes, open questions, skipped steps from prior runs.
- Include relevant carryover in the Morning Briefing under a "Carryover" subsection when items exist.

### Session Log Creation

If `60_Claude/10_Session_Logs/log.md` does not exist, create it with this frontmatter before appending:

```yaml
---
type: log
status: active
created: YYYY-MM-DD
tags:
  - log
  - session
---
# Session Log
```

---

## Tool Layer Awareness

### Kiro Specs as Planning Artifacts

Treat `.kiro/specs/` files as planning artifacts, not ordinary vault notes. They are not part of the regular vault health scan. Do not apply frontmatter drift checks, link health checks, or encoding checks to spec files.

### Tool-Layer Audit (Optional)

When `--include-tools` or equivalent is invoked, or when the user explicitly asks to audit the tool layer:

1. Scan `.kiro/specs/` for each spec folder.
2. Report whether each spec has: `requirements.md`, `design.md`, `tasks.md`.
3. Flag specs with missing files as incomplete.
4. Flag specs where `tasks.md` has all tasks completed but no recent vault changes as potentially stale.
5. Link to the spec folder in the report.

### No Mutation During Normal Ops

Do not mutate `.kiro/specs/` during normal daily ops (`health-check`, `morning-start`, `evening-close`, `triage`). Only modify spec files when the user explicitly asks to update a Kiro plan. When the user asks to improve a Kiro plan, add content to the relevant spec and preserve existing text unless explicitly told to refactor.

### Implementation Handoff

When Kiro-generated plans mention implementation work already covered by local tooling (e.g., a task that says "create a health check" when `/ops health-check` already exists), point to the local tool instead of duplicating. This prevents the ops layer from re-implementing what Kiro specs describe.

---

## Safety Constraints

### Read-Only by Default

- **Scan** and **suggest** modes are strictly read-only. They inspect vault state and present findings.
- **Fix** mode requires explicit user approval before any write operation.
- When in doubt, suggest rather than fix.

### Protected Paths — Never Modify

These paths are off-limits during normal operations:
- `60_Claude/05_Clippings/` — raw source captures are immutable unless the user explicitly asks for cleanup
- `50_Archive/` — historical reference, read-only unless the task is archival cleanup
- `.obsidian/` — plugin data, settings, config files
- MCP credential files and local settings files (`.claude/settings.local.json`, `.mcp.json` secrets)

### Batch Fix Threshold

- Fixes touching **more than 5 notes** require a batch plan presented to the user before execution.
- The plan lists every note to be modified, the proposed change, and the reason.

### Tree-Status Protection

- Notes with `status: tree` are mature, durable knowledge. Before modifying any tree-status note:
  1. Show the proposed change.
  2. Wait for user approval.
  3. Only then apply.

### Write Behavior

- Prefer appending reports and patching narrow sections over rewriting whole notes.
- Preserve frontmatter on all edits.
- Follow frontmatter conventions from `CLAUDE.md` and `Vault Operating System.md`.
- Search before creating — prefer extending an existing note over making duplicates.
- Use Obsidian wikilinks for internal references.
- Update `updated:` field when a note changes meaningfully.

### Context and Prose Quality

- Read `AI_CONTEXT.md` before operations — it is the cross-tool manifest.
- Read `HUMAN_WRITING.md` before generating prose — no filler, no AI slop, concrete and compressed.
- Treat CLI output as diagnostic input, not as content to paste verbatim into reports.

---

## Cost Profiles

| Operation | Cost | Token Budget | Primary Tools |
|-----------|------|-------------|---------------|
| `morning-start` | Standard | Moderate | CLI health + context, MCP reads for triage/drills, `/context`, `/today` |
| `health-check` | Lightweight | Low | CLI baseline (health, links, dates, encoding), MCP spot-checks |
| `capability-audit` | Lightweight | Low | MCP `global_search` with targeted queries |
| `triage` | Standard | Moderate | Health check results + MCP reads for routing |
| `ingest-batch` | Heavyweight | High | Sequential `/ingest-clipping` calls, MCP reads/writes per clipping |
| `evening-close` | Standard | Moderate | `/closeday`, MCP for capability audit, session log append |
| `full-cycle` | Heavyweight | High | morning-start + evening-close combined |

**Budget guidance:**
- Lightweight ops read CLI output and do ≤5 MCP calls. Safe for constrained sessions.
- Standard ops read live context files plus triage-referenced notes. ~10-20 MCP calls typical.
- Heavyweight ops process multiple notes sequentially. Reserve for dedicated sessions with budget headroom.
- When budget is tight, prefer `health-check` over `morning-start`, and `capability-audit` over `full-cycle`.

---

## Usage Examples

### Quick health check
```
/ops health-check
```
Runs CLI baseline scan + MCP spot-checks. Produces an Ops Report at `60_Claude/50_Reviews/Ops Health - YYYY-MM-DD.md`. Lightweight — good for a fast vault pulse.

### Morning startup
```
/ops morning-start
```
Gathers context, builds today's plan, runs health check, surfaces top triage items and overdue drills. Produces a Morning Briefing note. Standard cost — the recommended daily opener.

### End of day
```
/ops evening-close
```
Creates the closeday summary, runs capability audit, appends evening close section with health delta and triage status. Standard cost — the recommended daily closer.

### Process clippings backlog
```
/ops ingest-batch
```
Lists unprocessed clippings, lets you select which to ingest and at what depth. Processes sequentially via `/ingest-clipping`. Heavyweight — use when you have budget for batch processing.

### Work through maintenance queue
```
/ops triage
```
Presents the prioritized triage queue from the latest health check. Select items to fix — each routes to the right skill (`/connect-notes`, `/ingest-clipping`, `/lint-claude-layer`, etc.). Standard cost.

### Check capability engine health
```
/ops capability-audit
```
Searches for tracked concepts, overdue drills, evidence gaps, stalled outputs. Lightweight — quick check on learning system state.

### Full day cycle
```
/ops full-cycle
```
Runs morning-start, then waits. Re-invoke to run evening-close. Heavyweight — covers the complete daily cadence.

### No subcommand (time-aware)
```
/ops
```
Before noon → suggests `morning-start`. After noon → suggests `evening-close`. Always lets you pick any operation instead.

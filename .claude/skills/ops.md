---
name: running-ops
description: Daily vault operations dispatcher — health checks, triage, capability audits, cadence management; orchestrates existing skills into coherent workflows.
---
# ops

**Usage:** `/ops [operation]` where operation is one of: `health-check`, `capability-audit`, `triage`, `ingest-batch`, `full-cycle`. For daily planning use `/startday` (morning) and `/closeday` (evening). Invoke `/ops` alone for a time-aware suggestion.

---

## Instructions

### 1. Before Any Operation

1. Read `AI_CONTEXT.md` for the shared cross-tool manifest.
2. Read `HUMAN_WRITING.md` — all prose output follows that standard. No filler, no AI slop, concrete and compressed.
3. Read the 5 most recent entries from `60_Claude/07_AI_Information/Session Logs/log.md` for carryover context.
4. If the session log does not exist, create it with frontmatter (`type: log`, `created: YYYY-MM-DD`) before appending.

### 2. Operation Menu

When `/ops` is invoked, present the available operations:

| Operation | Cost | What it does |
|-----------|------|-------------|
| `morning-start` | **Deprecated** | Use `/startday` instead — fills your periodic daily note directly |
| `health-check` | Lightweight | CLI baseline + MCP spot-checks → Ops Report |
| `capability-audit` | Lightweight | MCP search for track/drill/evidence fields → capability section |
| `triage` | Standard | Present queue, route fixes to existing skills |
| `ingest-batch` | Heavyweight | List clippings, user selects, sequential `/ingest-clipping` |
| `evening-close` | **Deprecated** | Use `/closeday` instead — appends scorecard to the same daily note |
| `full-cycle` | Heavyweight | `/startday` + `/closeday` bookends |

**Cost labels explained:**
- **Lightweight** — CLI summaries, Dataview-style counts, short report sections. Minimal MCP reads. Prefer paths and counts over full note bodies.
- **Standard** — Reads live context files plus notes referenced by the current triage queue. Moderate MCP usage.
- **Heavyweight** — Sequential multi-note processing, full-cycle scans, batch ingestion. Reserve for dedicated sessions. When a heavyweight operation cannot complete due to budget, suggest the next best lightweight command.

### 3. Time-of-Day Detection

When `/ops` is invoked without a subcommand:
- **Before noon:** Suggest `/startday` — "It's morning. Run `/startday` to fill today's plan in your periodic note."
- **After noon:** Suggest `/closeday` — "It's afternoon. Run `/closeday` to score the day."
- Always let the user override with any `/ops` operation.

### 4. Operation Dispatch

#### `morning-start` (Deprecated)

> **Use `/startday` instead.** It fills your periodic note at `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` with the plan from your summer OS files, reads session history, and surfaces carryover. `/ops morning-start` no longer runs the day plan.

If you want vault health data alongside your start: run `/startday` then `/ops health-check`.

#### `health-check` (Lightweight)

1. Run the Health Check Engine (see `ops-reference.md` §Health Check Engine).
2. Generate the Ops Report (see `ops-reference.md` §Report Generator).
3. Append session log entry.

#### `capability-audit` (Lightweight)

1. Run the Capability Audit (see `ops-reference.md` §Capability Audit).
2. Output the capability health section.
3. Append session log entry.

#### `triage` (Standard)

1. Run the Health Check and Capability Audit if no current-day Ops Report exists.
2. Generate or load the Triage Queue (see `ops-reference.md` §Triage Queue).
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
2. Skip files that already have a corresponding source summary (check `60_Claude/10_Source_Summaries/` for matching `source_note` links).
3. Present the list to the user. Let them select which to process and choose depth per clipping: quick summary, standard distillation, or deep analysis.
4. Process selected clippings sequentially via `/ingest-clipping`.
5. Stop after a user-configurable batch limit (default: 5) to protect context budget.
6. When backlog exceeds 10 items, group by likely topic before presenting.
7. Route produced summaries through existing promotion logic: source summary first, then concept/project/output only when the idea is reusable.
8. Append session log entry.

#### `evening-close` (Deprecated)

> **Use `/closeday` instead.** It writes the Summer Ops Scorecard and day status directly into the same periodic note that `/startday` filled. No separate file is created.

#### `full-cycle` (Heavyweight)

1. Invoke `/startday` to fill today's periodic note.
2. Inform the user: "Work session open. Re-invoke `/ops full-cycle` or `/closeday` when ready to close."
3. On re-invocation, invoke `/closeday`.


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
- If `jarvis.ps1` fails or is unavailable, fall back to MCP-based scanning.
- Log the fallback reason to the session log: "CLI unavailable: [reason]. Falling back to MCP search."
- Note in the Ops Report that CLI was not used.

### 6. MCP Retry Policy

When an Obsidian MCP tool call fails:
1. If the error is a connection or timeout error, retry once.
2. If the retry also fails, log the failure: "MCP call failed: [tool_name] — [error]. Skipped after retry."
3. Continue with remaining operations. Do not abort the entire workflow for a single MCP failure.
4. Note any skipped dimensions in the Ops Report.

### 7. Error Handling

If any sub-skill or sub-operation fails during a composite workflow:
1. Log the error to the session log with the operation name and error description.
2. Skip the failed step.
3. Continue with remaining operations.
4. Include a "Skipped Steps" note in the final output.
5. When a heavyweight operation cannot complete, suggest the next best lightweight command as a fallback.

### 8. Skill References

This skill orchestrates existing skills by name. It does not duplicate their logic.

| Skill | When ops invokes it |
|-------|-------------------|
| `/context` | triage (vault state gathering) |
| `/startday` | full-cycle (day plan — replaces morning-start) |
| `/closeday` | full-cycle (daily close — replaces evening-close) |
| `/ingest-clipping` | ingest-batch (per-clipping processing) |
| `/connect-notes` | triage (broken link fixes, missing concepts) |
| `/lint-claude-layer` | triage (Claude layer issues) |
| `/distill-note` | triage (missing concept creation) |
| `/weekly-review` | referenced in evening-close for weekly context |

> **Engine specs** — For full Health Check Engine, Capability Audit, Triage Queue, Report Generator, Session Log, Safety, and Cost Profile specs, read `.claude/skills/ops-reference.md`.

---

## Usage Examples

### Quick health check
```
/ops health-check
```
Runs CLI baseline scan + MCP spot-checks. Produces an Ops Report at `60_Claude/50_Reviews/Ops Health - YYYY-MM-DD.md`. Lightweight — good for a fast vault pulse.

### Start the day (use this, not /ops morning-start)
```
/startday
```
Fills your periodic note at `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md` with today's plan: loads summer OS plans, reads 10 sessions of history, surfaces carryover, fills the Summer OS Checklist and Academic Stack.

### Close the day (use this, not /ops evening-close)
```
/closeday
```
Writes the Summer Ops Scorecard and day status into the same daily note. GREEN/RED verdict, friction fix if RED, preview for tomorrow.

### Process clippings backlog
```
/ops ingest-batch
```
Lists unprocessed clippings, lets you select which to ingest and at what depth. Processes sequentially via `/ingest-clipping`. Heavyweight — use when you have budget for batch processing.

### Work through maintenance queue
```
/ops triage
```
Presents the prioritized triage queue from the latest health check. Select items to fix — each routes to the right skill. Standard cost.

### Check capability engine health
```
/ops capability-audit
```
Searches for tracked concepts, overdue drills, evidence gaps, stalled outputs. Lightweight — quick check on learning system state.

### Full day cycle
```
/ops full-cycle
```
Invokes `/startday`, then waits. Re-invoke to run `/closeday`. Heavyweight — covers the complete daily cadence.

### No subcommand (time-aware)
```
/ops
```
Before noon → suggests `/startday`. After noon → suggests `/closeday`. Always lets you pick any `/ops` operation instead.

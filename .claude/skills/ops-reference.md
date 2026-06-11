---
name: ops-reference
description: Detailed engine specifications for the /ops skill — Health Check Engine, Capability Audit, Triage Queue, Report Generator, Session Log, Tool Layer Awareness, Safety Constraints, and Cost Profiles.
---
# ops-reference

*Companion reference for `.claude/skills/ops`. Read when running `health-check`, `capability-audit`, `triage`, or report generation.*

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
   - Search for notes missing `type`/`status`/`created` fields.
   - Check Capability Engine fields: `track`, `mastery_level`, `next_drill`, `evidence`.
   - Read specific notes for context when CLI flags them.
4. Combine CLI + MCP findings into a structured findings object.
5. Pass findings to the Report Generator.

### CLI-to-Ops Field Mapping

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

- Future-dated `updated` → flag as metadata drift. Makes stale notes look fresh to dashboards.
- Future-dated `next_drill` alone → not an error. Only flag if `last_drilled` is also in the future or inconsistent.
- Session log entries dated after actual current date → surface as "timeline inconsistency."
- Distinguish scheduled future work (legitimate `next_drill`) from impossible history (future `created`, future `updated`).

### Encoding Integrity Check

Scan for mojibake sequences: broken smart punctuation (`â€™`, `â€œ`), broken arrows (`â†`), UTF-8 marker artifacts (`Â`, `Ã`).

Rank findings by hit count and folder sensitivity:
- **High priority:** contracts (`CLAUDE.md`, `AI_CONTEXT.md`), dashboards, templates, active project notes in `20_Progress/`.
- **Low priority:** `50_Archive/`, `60_Claude/05_Clippings/` — unless the damaged file is actively linked from a current dashboard.

Never auto-repair encoding damage. Report only. Targeted cleanup requires explicit user request.

### Backlog Threshold

- Flag when `00_Inbox/` exceeds 10 items.
- Flag when `60_Claude/05_Clippings/` exceeds 10 items.
- When either backlog exceeds the threshold, the triage queue groups items by likely topic.

### Project Staleness Check

- Flag active projects with no `next:` action defined.
- Flag active projects not modified in 30+ days (by file mtime).
- Archived projects are excluded from staleness checks.

### Clean Bill of Health

When zero issues are found across all seven dimensions, report:

> ✅ Clean bill of health — all dimensions clear as of [timestamp]

Skip the per-dimension breakdown.

---

## Capability Audit

Queries Capability Engine state through MCP. Lightweight — keep MCP calls minimal, use `obsidian_global_search` with targeted queries.

### MCP Search Queries

| Query | Purpose |
|-------|---------|
| `obsidian_global_search` for `track:` | Find all tracked concepts |
| `obsidian_global_search` for `next_drill:` | Find drill-scheduled notes |
| `obsidian_global_search` for `type: output` | Find output notes |
| `obsidian_list_notes` in `60_Claude/60_Indexes/Field OS/` | Question bank state |

### Audit Checks

1. **Total tracked concepts** — Count notes with a non-empty `track` field.
2. **Mastery distribution** — Count by `mastery_level`: novice, familiar, proficient, expert.
3. **Overdue drills** — Notes where `next_drill` < today. Sort by days overdue descending.
4. **Evidence gaps** — Notes with `track` set but `evidence` field empty or missing.
5. **Stalled outputs** — Notes in `60_Claude/45_Outputs/` with `type: output` and `status: seed` where `created` is older than 14 days.
6. **Underseeded question banks** — For each track, flag if fewer than 3 open questions in its Field OS board.

### Capability Health Section Format

**Drill queue** — Top 5 overdue:
```markdown
### Drill Queue
| Note | Track | Days Overdue |
|------|-------|-------------|
| [[Note Title]] | track-name | 14 |
```

**Evidence gaps** — Top 5:
```markdown
### Evidence Gaps
| Note | Track |
|------|-------|
| [[Note Title]] | track-name |
```

**Stalled outputs:**
```markdown
### Stalled Outputs
| Note | Status | Age (days) |
|------|--------|-----------|
| [[Output Title]] | seed | 21 |
```

**Underseeded question banks:**
```markdown
### Underseeded Question Banks
| Track | Open Questions |
|-------|---------------|
| track-name | 1 |
```

When all checks pass, output:

> ✅ Capability Engine healthy — all tracks active, no overdue drills as of [timestamp]

---

## Triage Queue

Converts health check and capability audit findings into a capped, prioritized action list.

### Priority Levels

| Priority | Criteria | Examples |
|----------|----------|---------| 
| Critical | Broken required fields, encoding in active contracts | Missing `type` on dashboard note, mojibake in `CLAUDE.md` |
| High | Stale projects, overdue drills, broken links in active notes | Project with no `next` for 30+ days, drill 14+ days overdue |
| Medium | Inbox backlog, unprocessed clippings, weak links | >10 inbox items, >10 unprocessed clippings |
| Low | Orphan notes, archive encoding, cosmetic issues | Orphan in `50_Archive/`, duplicate filename in course notes |

### Queue Cap

Maximum 15 items. Lower-priority items that didn't make the cut are noted as a count at the bottom ("+ N lower-priority items omitted").

### Routing Rules

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

Every triage item gets a stable identifier: `{category}:{relative_path}:{issue_type}`

Examples:
- `frontmatter:20_Progress/UROP/index.md:missing_next`
- `drill:40_Resources/CS/AI/RAG.md:overdue_14d`
- `clippings:60_Claude/05_Clippings/:backlog_12`

### Carry-Forward Logic

1. Compare current triage identifiers against the previous Ops Report's triage section.
2. Items present in both → mark as "carried forward" with a consecutive-report count.
3. Items in the previous report but not the current scan → add to "Resolved Since Last Report."
4. Items appearing in 3+ consecutive reports get priority bumped by one level unless explicitly deferred.
5. Deferred items keep their original priority and are marked `[deferred]`.

### Triage Item Format

```markdown
- [ ] **[critical]** `frontmatter:20_Progress/UROP/index.md:missing_next` — Project missing `next` action → review and add next step
- [ ] **[high]** `drill:40_Resources/CS/AI/RAG.md:overdue_14d` — Drill 14 days overdue → schedule drill session
- [ ] **[medium]** `clippings:60_Claude/05_Clippings/:backlog_12` — 12 unprocessed clippings → `/ops ingest-batch`
```

### Duplicate and Link Classification

Risk tiers for duplicate filenames:
- **High risk** — durable notes (evergreen, concept, project in active folders).
- **Medium risk** — active project notes.
- **Low risk** — course-week patterns (`Week - N.md`) and archive patterns.

Link classification rules:
- Template placeholder wikilinks in `.claude/skills/` or `30_Order/Templates/` are **not** real broken links. Skip them.
- Before labeling a broken link as a missing note, check `attachments/`, `assets/`, and the same folder as the linking note.

---

## Report Generator

Produces three report types: Ops Report, Morning Briefing, and Evening Close. All output follows HUMAN_WRITING.md — tables and bullets over prose.

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
1. Summary Table — one row per scan dimension: name, status emoji, issue count.
2. Frontmatter Drift — notes missing required fields.
3. Link Health — broken and ambiguous wikilinks, by risk tier.
4. Date Consistency — future-dated fields; distinguish impossible history from scheduled future work.
5. Inbox/Clippings Backlog — counts. Flag when either exceeds 10.
6. Project Health — active projects missing `next:` or not modified in 30+ days.
7. Capability Engine Health — drill queue, evidence gaps, stalled outputs, underseeded question banks.
8. Encoding Integrity — mojibake hits ranked by folder sensitivity.
9. Triage Queue — prioritized action list.
10. Comparison — only when a prior Ops Report exists.
11. Resolved Since Last Report — items from the previous report no longer detected.

### Status Emojis

| Emoji | Meaning | Threshold |
|-------|---------|-----------|
| ✅ | Healthy | 0 issues |
| ⚠️ | Warning | 1–5 issues |
| ❌ | Critical | 6+ issues, or any broken required field |

### Morning Briefing

**File:** `60_Claude/50_Reviews/Morning Briefing - YYYY-MM-DD.md`

**Sections:**
1. Today's Plan — from `/startday` output.
2. Vault Health Summary — summary table only, no per-dimension detail unless critical.
3. Top 3 Triage Items — with routing suggestions.
4. Top 3 Overdue Drills — note title, track, days overdue.
5. Previous Day Link — wikilink to previous day's closeday note.

### Evening Close

Not a separate file. Appended to the day's Closeday note (created by `/closeday`).

**Sections appended:**
1. Capability Audit Summary.
2. Triage Status — items completed vs remaining.
3. Health Delta — one line: what changed since the morning check.

### Daily Cadence Chain

Every morning briefing links to the previous day's closeday note via `notes:` frontmatter. This chain is the primary continuity mechanism between sessions.

### Comparison Section Logic

When a previous Ops Report exists:
1. **Dimension comparison** — For each dimension, show ↓ (improved), ↑ (worsened), or → (same).
2. **Carried-forward items** — Matched by stable identifier. Show consecutive-report count.
3. **Resolved since last report** — Items no longer detected.

When no previous Ops Report exists, skip the Comparison section entirely.

---

## Session Log

Every ops operation appends a structured entry to `60_Claude/07_AI_Information/Session Logs/log.md` on completion.

### Log Entry Format

```markdown
## [YYYY-MM-DD] ops | [operation-name]

- Created: [[Ops Health - YYYY-MM-DD]], [[Morning Briefing - YYYY-MM-DD]]
- Modified: [[Closeday - YYYY-MM-DD]]
- Health: [one-line summary]
- Triage: [X items queued, Y carried forward]
- CLI: used/not used
- Duration: ~N min
```

Adapt bullets per operation — omit lines that don't apply.

### Session Log Creation

If the log doesn't exist, create it with this frontmatter before appending:
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

Treat `.kiro/specs/` files as planning artifacts, not ordinary vault notes. Do not apply frontmatter drift, link health, or encoding checks to spec files.

### Tool-Layer Audit (Optional)

When `--include-tools` is invoked:
1. Scan `.kiro/specs/` for each spec folder.
2. Report whether each spec has: `requirements.md`, `design.md`, `tasks.md`.
3. Flag specs with missing files as incomplete.
4. Flag specs where `tasks.md` has all tasks completed but no recent vault changes as potentially stale.

### No Mutation During Normal Ops

Do not mutate `.kiro/specs/` during normal daily ops. Only modify spec files when the user explicitly asks.

---

## Safety Constraints

### Read-Only by Default

- Scan and suggest modes are strictly read-only.
- Fix mode requires explicit user approval before any write operation.
- When in doubt, suggest rather than fix.

### Protected Paths — Never Modify

- `60_Claude/05_Clippings/` — raw source captures are immutable unless the user explicitly asks for cleanup
- `50_Archive/` — historical reference, read-only unless the task is archival cleanup
- `.obsidian/` — plugin data, settings, config files
- MCP credential files and local settings files (`.claude/settings.local.json`, `.mcp.json` secrets)

### Batch Fix Threshold

Fixes touching more than 5 notes require a batch plan presented to the user before execution.

### Tree-Status Protection

Notes with `status: tree` are mature, durable knowledge. Before modifying any tree-status note:
1. Show the proposed change.
2. Wait for user approval.
3. Only then apply.

### Write Behavior

- Prefer appending reports and patching narrow sections over rewriting whole notes.
- Preserve frontmatter on all edits.
- Search before creating — prefer extending an existing note over making duplicates.
- Update `updated:` field when a note changes meaningfully.

---

## Cost Profiles

| Operation | Cost | Token Budget | Primary Tools |
|-----------|------|-------------|---------------|
| `morning-start` | Deprecated | — | Use `/startday` instead |
| `health-check` | Lightweight | Low | CLI baseline (health, links, dates, encoding), MCP spot-checks |
| `capability-audit` | Lightweight | Low | MCP `global_search` with targeted queries |
| `triage` | Standard | Moderate | Health check results + MCP reads for routing |
| `ingest-batch` | Heavyweight | High | Sequential `/ingest-clipping` calls, MCP reads/writes per clipping |
| `evening-close` | Deprecated | — | Use `/closeday` instead |
| `full-cycle` | Heavyweight | High | `/startday` + `/closeday` bookends |

**Budget guidance:**
- Lightweight ops read CLI output and do ≤5 MCP calls. Safe for constrained sessions.
- Standard ops read live context files plus triage-referenced notes. ~10-20 MCP calls typical.
- Heavyweight ops process multiple notes sequentially. Reserve for dedicated sessions.
- When budget is tight, prefer `health-check` over `full-cycle`, and `capability-audit` over `triage`.

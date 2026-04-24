# Implementation Plan: Claude Code Operations Layer

## Overview

Build the `/ops` dispatcher skill and its supporting components — health check engine, capability audit, triage queue, report generator, session log integration, vault-curator enhancement, CLAUDE.md update, and dashboard integration. Each task creates or modifies actual files in `.claude/skills/`, `.claude/agents/`, `60_Claude/60_Indexes/`, and `CLAUDE.md`. The jarvis-cli at `30_Order/System/jarvis-cli/jarvis.ps1` handles deterministic scans; the skill orchestrates it alongside Obsidian MCP for semantic queries.

## Tasks

- [x] 1. Create the Ops Dispatcher skill file
  - [x] 1.1 Create `.claude/skills/ops.md` with the full skill structure: title, description, usage, instructions, safety constraints, and cost profiles
    - Include the operation menu: `morning-start`, `health-check`, `triage`, `ingest-batch`, `capability-audit`, `evening-close`, `full-cycle`
    - Define cost labels per operation (lightweight, standard, heavyweight) per the design Component 1 table
    - Include usage examples for each operation mode
    - Reference existing skills by slash-command name (`/context`, `/today`, `/closeday`, `/ingest-clipping`, `/connect-notes`, `/lint-claude-layer`, `/distill-note`) — do not duplicate their logic
    - Include the safe mutation policy: scan/suggest modes are read-only, fix mode requires user approval, never modify `60_Claude/05_Clippings/`, `50_Archive/`, `.obsidian/`, or MCP config files
    - Include batch-fix threshold: fixes touching >5 notes require a plan; notes with `status: tree` get proposed changes shown first
    - Include the time-of-day detection: suggest `morning-start` before noon, `evening-close` after noon when `/ops` is invoked without a subcommand
    - Document that the skill reads `AI_CONTEXT.md` and `HUMAN_WRITING.md` before generating prose output
    - Include error handling: log failures to session log, skip failed steps, continue with remaining operations
    - Include CLI fallback: prefer `jarvis.ps1` for baseline scans, fall back to MCP if CLI unavailable, log the fallback reason
    - Include MCP retry policy: retry once on connection/timeout error, then log and continue
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 4.4, 6.1, 6.2, 6.3, 6.4, 6.5, 11.1, 11.2, 11.3, 11.4, 11.5, 12.1, 12.2, 12.5, 12.6, 15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.7, 21.1, 21.2, 21.3, 21.4, 21.5, 21.6_

- [x] 2. Implement Health Check Engine instructions within the ops skill
  - [x] 2.1 Add the Health Check section to `.claude/skills/ops.md` covering the six-dimension scan
    - Define the scan dimensions: frontmatter completeness, link integrity, inbox/clippings backlog, project staleness, Capability Engine gaps, date consistency, encoding integrity
    - Specify CLI-first approach: run `jarvis.ps1 health`, `jarvis.ps1 links`, `jarvis.ps1 dates`, `jarvis.ps1 encoding` for deterministic baselines
    - Specify MCP semantic layer: search for notes missing `type`/`status`/`created`, check Capability Engine fields, read specific notes for context
    - Map CLI output fields to Ops Report dimensions per the design's CLI-to-Ops Field Mapping table
    - Include the date consistency check: compare `created`, `updated`, `reviewed`, `last_drilled`, `next_drill` against actual current date; flag future-dated `updated` as drift; only flag future `next_drill` if paired `last_drilled` is also future/inconsistent
    - Include encoding integrity check: scan for mojibake sequences, rank by hit count and folder sensitivity, high priority for contracts/dashboards/active notes, low for archive
    - Include the backlog threshold: flag when `00_Inbox/` or `60_Claude/05_Clippings/` exceeds 10 items
    - Include project staleness check: no `next:` action or not modified in 30+ days
    - Include clean bill of health output when zero issues found
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 12.1, 12.3, 13.1, 13.2, 13.3, 13.4, 13.5, 14.1, 14.2, 14.3, 14.4, 14.5_

- [x] 3. Implement Capability Audit instructions within the ops skill
  - [x] 3.1 Add the Capability Audit section to `.claude/skills/ops.md`
    - Define MCP search queries: search for `track:` field, `next_drill:` field, `type: output`, question bank state in `60_Claude/60_Indexes/Field OS/`
    - Specify audit checks: total tracked concepts, mastery distribution by level, overdue drills (sorted by days overdue descending with title/track/days), evidence gaps, stalled outputs (`status: seed` older than 14 days), underseeded question banks (<3 open questions)
    - Define the "Capability Health" section format for the Ops Report: drill queue (top 5 overdue), evidence gaps (top 5), stalled outputs, underseeded question banks
    - Use MCP `global_search` with targeted queries rather than reading every note
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 11.2_

- [x] 4. Implement Triage Queue Generator instructions within the ops skill
  - [x] 4.1 Add the Triage Queue section to `.claude/skills/ops.md`
    - Define priority levels: critical (broken required fields, encoding in active contracts), high (stale projects, overdue drills, broken links in active notes), medium (inbox backlog, unprocessed clippings), low (orphan notes, archive encoding)
    - Cap queue at 15 items, selecting highest-priority when more exist
    - Define routing rules: broken links → `/connect-notes`, clippings → `/ingest-clipping` or `/ops ingest-batch`, Claude layer issues → `/lint-claude-layer`, stale projects → manual review, overdue drills → drill session, encoding → targeted cleanup with approval
    - Define stable identifier format: `{category}:{relative_path}:{issue_type}` for cross-report matching
    - Define carry-forward logic: items in 3+ consecutive reports get priority bumped by one level unless deferred
    - Define triage item format: task checkbox with priority tag, description, and suggested skill command
    - Include duplicate/link classification: high risk for durable notes, medium for active project notes, low for course-week/archive patterns; template placeholder wikilinks treated differently from real broken links; prefer linking feeder notes to enriched notes over merging; suggest `/connect-notes` or `/distill-note` for missing concepts rather than auto-creating stubs; check attachment locations before labeling broken links as missing notes
    - Include clipping backlog grouping: group by likely topic when backlog exceeds threshold; distinguish quick summaries, standard distillations, and deep analyses; sequential processing with configurable batch limit; skip already-processed clippings; route through existing promotion logic
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 19.1, 19.2, 19.3, 19.4, 19.5, 20.1, 20.2, 20.3, 20.4, 20.5_

- [x] 5. Implement Report Generator instructions within the ops skill
  - [x] 5.1 Add the Report Generator section to `.claude/skills/ops.md` covering Ops Report, Morning Briefing, and Evening Close formats
    - Define Ops Report structure: frontmatter (`type: review`, `status: complete`, `created: YYYY-MM-DD`, tags `ops-health` and `review`), Summary Table, Frontmatter Drift, Link Health, Date Consistency, Inbox/Clippings Backlog, Project Health, Capability Engine Health, Encoding Integrity, Triage Queue, Comparison (if prior report exists), Resolved Since Last Report
    - Define status emojis: ✅ healthy (0 issues), ⚠️ warning (1-5), ❌ critical (6+ or broken required fields)
    - Define cross-linking: every Ops Report links to most recent CLI report under `60_Claude/50_Reviews/Ops Reports/`
    - Define Morning Briefing format: today's plan (from `/today`), vault health summary, top 3 triage items, top 3 overdue drills, link to previous day's closeday note
    - Define Evening Close format: appended section to day's Closeday note with capability audit summary, triage completed vs remaining, one-line health delta from morning
    - Define daily cadence chain: every morning briefing links to previous day's closeday note via wikilinks
    - Include Comparison section logic: compare against most recent prior Ops Report, show dimensions improved/worsened/stayed same, mark recurring items as "carried forward", include "resolved since last report" list
    - Include report registry: surface most recent Ops Report, Morning Briefing, Evening Close, and CLI report via dashboard or index
    - Prefer concise structured output (tables, bullet lists) over verbose prose
    - _Requirements: 4.1, 4.2, 4.3, 4.5, 8.1, 8.2, 8.3, 8.4, 8.5, 9.3, 11.3, 17.1, 17.2, 17.3, 17.4, 17.5_

- [x] 6. Implement Session Log Integration instructions within the ops skill
  - [x] 6.1 Add the Session Log section to `.claude/skills/ops.md`
    - Define log entry format: `## [YYYY-MM-DD] ops | [operation-name]` followed by bullets for created files, modified files, key findings, triage count, CLI usage
    - Specify that every ops operation appends a structured entry on completion
    - Specify morning-start reads 5 most recent entries for carryover context
    - Include session log creation: if `60_Claude/10_Session_Logs/log.md` doesn't exist, create it with appropriate frontmatter before appending
    - _Requirements: 9.1, 9.2, 9.3, 9.4_

- [x] 7. Checkpoint — Review ops skill completeness
  - Ensure all tests pass, ask the user if questions arise.
  - Verify `.claude/skills/ops.md` contains all 9 sections: menu/dispatcher, health check, capability audit, triage queue, report generator, session log, safety constraints, cost profiles, usage examples
  - Verify the skill references existing skills by name without duplicating their logic
  - Verify CLI-first approach is documented with MCP fallback

- [x] 8. Implement Kiro spec and tool-layer awareness in the ops skill
  - [x] 8.1 Add a "Tool Layer Awareness" section to `.claude/skills/ops.md`
    - Treat `.kiro/specs/` files as planning artifacts, not ordinary vault notes
    - Include Kiro specs in tool-layer audit when `--include-tools` or equivalent runs: report stale/incomplete specs, link to spec folder, summarize whether requirements/design/tasks files exist
    - Do not mutate `.kiro/specs/` during normal daily ops unless user explicitly asks
    - Point to local tools instead of duplicating implementation when Kiro plans mention covered work
    - _Requirements: 16.1, 16.2, 16.3, 16.4, 16.5, 16.6_

- [x] 9. Update the vault-curator agent file
  - [x] 9.1 Update `.claude/agents/vault-curator.md` with three additions while preserving all existing content
    - Add Ops Report awareness: read most recent Ops Report before scanning to avoid re-discovering known issues
    - Add "Capability Engine Maintenance" section to Curator Report: notes with conflicting property types, tracks with no enriched notes in 30 days, synthesis notes with broken concept links
    - Add enrichment-aware deduplication: when duplicates found, prefer preserving the note with Capability Engine fields (`track`, `mastery_level`, `evidence`)
    - _Requirements: 7.1, 7.2, 7.3, 7.4_

- [x] 10. Update CLAUDE.md with operations layer documentation
  - [x] 10.1 Add `/ops` to the Available Skills table in `CLAUDE.md`
    - Description: "Daily vault operations — health checks, triage, cadence management"
    - _Requirements: 10.1_
  - [x] 10.2 Add a "Daily Operations Cadence" section under Core Rules in `CLAUDE.md`
    - Describe the morning-start → work → evening-close rhythm in ~5 lines
    - Link to `.claude/skills/ops.md` for full documentation
    - Keep total file under 200 lines
    - Preserve all existing content, frontmatter, and formatting
    - _Requirements: 10.2, 10.3, 10.4_

- [x] 11. Create Dashboard Integration
  - [x] 11.1 Add an ops dashboard entry to `60_Claude/60_Indexes/` or update an existing dashboard
    - Add Dataview query linking to latest Ops Report (notes with tag `ops-health`)
    - Add link to latest Morning Briefing
    - Add link to latest CLI report under `60_Claude/50_Reviews/Ops Reports/`
    - Use Dataview queries for dynamic content — no unsupported plugins
    - _Requirements: 18.1, 18.2, 18.4_
  - [x] 11.2 Create the Ops Reports Base file at `60_Claude/60_Indexes/Bases/Ops Reports.base` if Bases plugin supports it
    - Query notes with tag `ops-health`
    - Columns: name, created, top issue count, carry-forward count
    - _Requirements: 18.3_
  - [x] 11.3 Document any new metadata fields in `Vault Operating System.md` or an ops-specific system note
    - Document `cli_used`, `scan_dimensions`, `critical_count`, `high_count`, `carry_forward_count` frontmatter fields used by Ops Reports
    - _Requirements: 18.5_

- [x] 12. Checkpoint — Full integration review
  - Ensure all tests pass, ask the user if questions arise.
  - Verify `.claude/skills/ops.md` exists and contains all required sections
  - Verify `.claude/agents/vault-curator.md` has the three new sections without losing existing content
  - Verify `CLAUDE.md` has `/ops` in the skills table and the cadence section, stays under 200 lines
  - Verify dashboard entry exists with Dataview queries
  - Verify no files were modified in `60_Claude/05_Clippings/`, `50_Archive/`, `.obsidian/`, or MCP config files

- [x] 13. Verification and acceptance
  - [x] 13.1 Create a verification checklist entry in the session log documenting the final command sequence
    - Verify `/ops health-check` instructions would produce an Ops Report with all required sections
    - Verify `/ops morning-start` instructions would create a Morning Briefing and append a Session_Log entry
    - Verify `/ops evening-close` instructions would update the day's closeday note and append a Session_Log entry
    - Verify report generation instructions do not modify protected paths (`60_Claude/05_Clippings/`, `50_Archive/`, `.obsidian/`, MCP config)
    - Verify fallback behavior is documented for when Obsidian MCP or CLI is unavailable
    - Append the verification summary to `60_Claude/10_Session_Logs/log.md`
    - _Requirements: 22.1, 22.2, 22.3, 22.4, 22.5, 22.6_

## Notes

- All deliverables are Markdown files (skill definitions, agent updates, dashboard entries, contract updates) — no traditional compiled code
- The jarvis-cli at `30_Order/System/jarvis-cli/jarvis.ps1` handles deterministic scans; the ops skill orchestrates it
- Obsidian MCP handles semantic queries and vault writes
- Existing skills are referenced by name, never duplicated
- Reports should be short enough to scan — decisions and next actions, not audit prose
- The two report families (CLI-generated under `Ops Reports/` and ops-generated `Ops Health - YYYY-MM-DD.md`) cross-link but don't duplicate

---
type: review
status: complete
created: 2026-05-28
week: 2026-W22
tags:
  - review
  - weekly
notes:
  - "[[60_Claude/50_Reviews/Weekly Synthesis/Weekly Synthesis Index]]"
  - "[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]"
  - "[[Jarvis]]"
---

# Weekly Synthesis — 2026-W22

The infrastructure got its missing nervous system this week — Claude Pro workflow was wired in and session-continuity hooks were built — but the execution gap in the three-month build spine is now undeniable and quantified.

## What Was Built

**May 26 — Claude Pro workflow spine:**
- `40_Resources/Obsidian/Claude Pro Workflow.md` — full operating guide for strict-budget summer AI workflow
- `30_Order/System/claude-workflow/` — README, `jarvis-session-continuity.ps1` hook, Desktop config example
- `.mcp.json` — MCP configuration for Obsidian, context7, playwright, openaiDeveloperDocs
- Global Claude Code `SessionStart` / `SessionEnd` hooks live
- Claude Desktop config with `obsidian-jarvis` MCP server confirmed connected

**May 28 — Claude Optimization Master Setup audit:**
- `60_Claude/40_Project_Briefs/Claude Optimization Master Setup.md` — full vault + external link audit
- Key findings: AI Workflow.md and MCPs.md are outdated (March 2026); mattpocock/skills confirmed 108k stars but not installed; conversation capture folders designed but never created; 223-note enrichment queue idle since April 27
- Weekly review system: enhanced `weekly-review.md` skill (plan-aware), this review note, Cowork scheduled task registered

## Three-Month Plan Status

**Current position:** End of Month 1 / entering Month 2 (plan started April 24 — this is approximately Week 5 of 12).

| Deliverable | Expected | Status |
|------------|----------|--------|
| `20_Progress/Projects/Jarvis.md` as project hub | Week 1 | ✅ exists |
| `jarvis status` command | Week 1 | ⚠️ `jarvis_ops.py` has `health`/`projects`; no `status` sub-command yet |
| Registry schema as standalone file | Week 1 | ⚠️ schema defined in master plan only |
| Conversation capture folders | Week 2 | ❌ `60_Claude/05_Clippings/AI Conversations/` does not exist |
| Conversation import + registry | Week 2 | ❌ not started |
| Context pack builder | Week 3 | ❌ `jarvis context-pack` does not exist |
| `jarvis index` + `jarvis note-profile` | Week 4 | ❌ not started |
| 25 notes enriched (Week 4 target) | Week 4 | ✅ 24 enriched in W17; 223-note queue still open |
| Semantic search (Month 2) | Week 5 | ❌ not started |

**Verdict:** Month 1 spine is ~30% complete. The enrichment seeding was done but the four structural pieces — conversation capture, registry, context pack builder, semantic index — are all at zero. The plan is approximately 4 weeks behind. Month 2 brain work should not start until Week 2 capture and Week 3 context pack exist.

## Enrichment and Drills

- Notes enriched this week: 0
- Overdue drills: first drills were seeded for 2026-05-02 — 26 days overdue. Run `next_drill < date(today)` in Dataview to get exact count.
- Enriched-to-date: ~24 notes vs. 100-note end-of-three-months target — 24% done with ~7 weeks remaining
- At 10 notes/week (plan target), 94 total by Week 12. Currently at 0/week for 5 consecutive weeks.

## Vault Health

**Orphaned notes:** Estimated 10–15 in `40_Resources/` and `60_Claude/20_Distilled_Notes/` with zero backlinks. Check `60_Claude/60_Indexes/Vault Health Dashboard.md` for the live query.

**Projects missing next actions:** 7+ active projects had no `next:` field as of the April 24 baseline audit. Run `.\30_Order\System\jarvis-cli\jarvis.ps1 projects` for current count.

**Metadata gaps:** Unknown count of notes missing `type` or `status` in `10_Areas/` and `20_Progress/`. Run `jarvis health` to get the number.

**New notes without links:** `40_Resources/Obsidian/Claude Pro Workflow.md` — verify it links to `AI_CONTEXT`, `CLAUDE.md`, `00_Dashboard.md`. `60_Claude/40_Project_Briefs/Claude Optimization Master Setup.md` — should link to the Three-Month Master Plan.

## Suggested Links

1. `[[60_Claude/40_Project_Briefs/Claude Optimization Master Setup]]` → `[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]` — the audit directly scores the master plan's execution; they should cross-reference.
2. `[[40_Resources/Obsidian/Claude Pro Workflow]]` → `[[60_Claude/7_AI_Information/AI_CONTEXT]]` — workflow doc is the operational layer for the context manifest.
3. `[[20_Progress/Projects/Jarvis]]` → `[[40_Resources/Obsidian/Claude Pro Workflow]]` — the Jarvis project note should reflect the Claude Pro workflow as an infrastructure milestone.
4. `[[60_Claude/20_Distilled_Notes/AI-Assisted Trading]]` ↔ `[[60_Claude/20_Distilled_Notes/Index Fund Investing]]` — both seeded in W17 with zero backlinks; they should link to each other and to any trading-track project note.
5. `[[60_Claude/60_Indexes/Vault Health Dashboard]]` → `[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]` — the health dashboard is the operational view of the spine's progress.

## Cleanup Candidates

1. **`60_Claude/7_Al_Information/`** (typo folder — capital `Al` not `AI`) — session log says it was left untouched. If empty or duplicate of `60_Claude/7_AI_Information/`, delete it.
2. **`50_Archive/UMN/Classes/CSCI 2041/`** — created as archive dump May 8; live notes now exist in `10_Areas/Degree/UMN/Classes/CSCI 2041/`. Confirm no unique content before deleting.
3. **`40_Resources/CS/AI/AI Workflow.md` and `MCPs.md`** — confirmed outdated (March 2026, pre-Claude-subscription). Either update with "superseded by Claude Pro Workflow" + forward link, or archive. Leaving them active misleads future agents.
4. **Duplicate log entry (2026-05-28)** — `log.md` has two identical `[2026-05-28] audit | Claude Optimization Master Setup` entries. Remove one.

## Next Week Priorities

**Priority 1: Create conversation capture folders and import schema.**
Why now: This is Week 2 of Month 1 — 5 weeks overdue. Every week it doesn't exist, AI conversation decisions disappear.
Output: `60_Claude/05_Clippings/AI Conversations/` and `60_Claude/30_Source_Summaries/AI Conversations/` exist; schema file at `30_Order/System/jarvis-memory/schema.md`; one test conversation imported.

**Priority 2: Restart enrichment — enrich 10 notes, reset overdue drills.**
Why now: The 223-note queue has been idle 5 weeks. Drills seeded in W17 are 26+ days overdue. The learning system cannot activate while enrichment is paused.
Output: 10 notes updated with `enrichment_status: enriched`; all overdue `next_drill` dates reset forward.

**Priority 3: Fix the three stale/misleading files.**
Why now: AI Workflow.md and MCPs.md actively mislead future Claude sessions. The duplicate log entry corrupts the continuity record. These take 20 minutes to fix.
Output: Both outdated files either updated with a "superseded" notice + forward link or moved to `50_Archive/`; duplicate log entry removed.

## Open Questions

1. **Install mattpocock/skills now or after conversation capture is built?** Audit confirmed it's relevant and ready (`npx skills@latest add mattpocock/skills`). But installing more tooling before the capture spine exists might be distraction. This needs a decision.
2. **Extend `jarvis_ops.py` first, or create conversation capture at the folder/template level manually?** The master plan assumes CLI commands, but manual folder creation could unblock Week 2 without any Python work.
3. **Are the CSCI 2041 archive notes in `50_Archive/` serving any purpose now that live notes exist in `10_Areas/`?** If not, deleting them reduces maintenance surface. But unique source-grounded content might exist only in the archive.

---

*Generated by /weekly-review — Cowork weekly scheduled task*

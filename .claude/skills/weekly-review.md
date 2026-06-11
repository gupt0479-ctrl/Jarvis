---
name: reviewing-weekly
description: Full weekly vault review aligned with the Jarvis Three-Month Research Engine Master Plan; tracks what was built, what's overdue, what needs linking, and what next week should prioritize.
---
# weekly-review

**Usage:** `/weekly-review` or invoked automatically by the Cowork weekly scheduled task.

---

## Pre-flight: Read These First

Before touching anything else, read these files in order:

1. `60_Claude/7_AI_Information/AI_CONTEXT.md`
2. `60_Claude/07_AI_Information/Session Logs/log.md` — tail: last 100 lines
3. `00_Dashboard.md`
4. `60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan.md` — sections: "Three-Month Build Map" and "The Weekly Operating Rhythm"
5. The most recent weekly synthesis: `60_Claude/50_Reviews/Weekly Synthesis/` — list directory, read the latest file

Determine the current ISO week number from today's date. Format: `YYYY-WXX`.

---

## Step 1: Find Recent Vault Activity

Calculate the date 7 days ago. Then search for recently modified notes:

- Use `mcp__jarvis-fs__search_files` or `mcp__jarvis__search_simple` to find notes modified in the past 7 days
- Search across: `10_Areas/`, `20_Progress/`, `40_Resources/`, `60_Claude/`
- Exclude: `50_Archive/`, `60_Claude/05_Clippings/`, `.obsidian/`, `.claude/`, `.kiro/`, `.cursor/`

Group what you find by area:

- **Coursework** (`10_Areas/`): course notes, concept notes, lab/project notes
- **Projects + Career** (`20_Progress/`): project notes, career notes, UROP progress
- **Resources** (`40_Resources/`): enriched concept notes, reference material
- **Claude layer** (`60_Claude/`): distillations, summaries, project briefs, outputs, reviews

For each group, note: what was created vs. what was updated, and whether the work has a clear `next:` or outcome.

---

## Step 2: Summer Execution Audit

Check four execution tracks against the targets in `10_Areas/Life/Plans/`.

Do not re-read all plan files — use these specific checks:

### LeetCode
- Read `10_Areas/Life/Plans/05a - LeetCode Tracker.md` — find this week's total
- Target: ≥35 problems/week
- Flag if < 35: how far behind, which days had zero

### Courses
- Read `10_Areas/Life/Plans/04 - Summer Courses Ops.md` — deadline table
- Did any deadline pass this week? If so, what was it and was it met?
- Read `10_Areas/Life/Plans/06a - ML Fundamentals Progress.md` — how many units completed vs. planned?

### Projects
- Check `20_Progress/` — any project notes modified in the past 7 days?
- From `10_Areas/Life/Plans/07 - Projects & Hackathons Queue.md` — did any flagship project advance?
- What shipped this week? (code pushed, document finalized, demo done — concrete artifacts only)

### Career Pipeline
- Any LeetCode company-tagged problems this week? (track from 05a)
- Any applications submitted, outreach sent, or interviews scheduled?
- Check if `20_Progress/` has any career-related notes touched this week

For each track mark: ✅ on target, ⚠️ partial, ❌ missed. One line per track explaining the verdict.

---

## Step 3: Enrichment Queue Health

Check the enrichment pipeline status:

1. Count notes where `enrichment_status` is missing or not `"enriched"` — these are candidates
2. Check for notes where `next_drill < today` — these are overdue drills
3. Identify which tracks (ai, systems, algorithms, career, trading) are most behind
4. Note how many notes were enriched this week vs. the target of 10/week

Key enrichment locations:
- `40_Resources/CS/AI/` — AI track
- `40_Resources/CS/` — algorithms/systems track
- `60_Claude/20_Distilled_Notes/` — distilled knowledge layer
- `20_Progress/UROP/` — UROP/BOOM/systems track

---

## Step 4: Structural Health Check

Check four things:

**Orphans:** Notes in `40_Resources/` or `60_Claude/20_Distilled_Notes/` with zero backlinks (`length(file.inlinks) = 0`). These are knowledge islands. List the top 5 by age.

**Missing next actions:** Project notes in `20_Progress/` where `type = "project"`, `status != "archived"`, and `next` is missing. A project without a next action is stalled.

**Metadata gaps:** Notes in active areas missing `type` or `status`. These break Dataview queries.

**New notes without outbound links:** Notes created this week with no wikilinks in their content. New notes should connect to at least one existing note.

---

## Step 5: Session Log Summary

Extract from `60_Claude/07_AI_Information/Session Logs/log.md` all entries from the past 7 days.

Summarize:
- Sessions run: how many, what types (build/enrich/distill/review/setup/audit)
- Notes created this week: count
- Notes enriched: count
- Conversations captured or distilled: count (0 is worth flagging)
- Whether any session lacked a clear `next:` action

---

## Step 6: Write the Review Note

Create `60_Claude/50_Reviews/Weekly Synthesis/Weekly Synthesis — YYYY-WXX.md` using this template.

After creating it, also patch the weekly periodic note at `10_Areas/Life/Enumerate/Weekly/YYYY-Www.md` (where `YYYY-Www` matches the ISO week, e.g. `2026-W24`). If the note doesn't exist, create it using `30_Order/Templates/Enumerate/Better Weekly.md`. Patch its `> [!NOTE] Summary:` callout with a one-sentence summary of the week, and fill the Goals and Fixes sections with the top items from the synthesis note. Keep it brief — the weekly periodic note is a quick-glance record, not a duplicate of the full synthesis.

```markdown
---
type: review
status: complete
created: YYYY-MM-DD
week: YYYY-WXX
tags:
  - review
  - weekly
notes:
  - "[[60_Claude/50_Reviews/Weekly Synthesis/Weekly Synthesis Index]]"
---

# Weekly Synthesis — YYYY-WXX

[One sentence: the defining theme of this week. Not a list — a statement.]

## What Was Built

[Describe actual completed work. Be specific: file names, note counts, which skill/agent/command now works. Skip anything that was just planned but not done.]

## Three-Month Plan Status

[Current month and week in the plan. Table of this month's milestones with ✅ / ⚠️ / ❌ status. One sentence on whether the plan is on track, ahead, or behind, and what the main blocker is.]

## Enrichment and Drills

[How many notes enriched this week. Overdue drills if any. Which track needs the most attention next week. Total enriched-to-date vs. the 100-note end-of-three-months target.]

## Vault Health

[Orphaned notes count. Projects missing next actions (list them). Metadata gaps. Any new notes created this week that have zero links.]

## Suggested Links

[3–5 concrete link suggestions: "[[Note A]] should link to [[Note B]] because..." Only suggest links that don't already exist and that would add genuine navigational value.]

## Cleanup Candidates

[2–4 notes that should be deleted, merged, or archived. Must state the specific reason — duplicate, stale, superseded, orphan that nobody will ever read.]

## Next Week Priorities

[Exactly 3 priorities, tied to the master plan. Each one is a specific action, not a vague theme. Format: "Priority: [what]. Why now: [reason tied to plan]. Output: [what file or command exists when it's done]."]

## Open Questions

[2–3 genuine unresolved questions this week surfaced — about the build plan, the vault, or Anant's direction. Not rhetorical. Things that need a decision or more information before proceeding.]
```

**Writing rules:** Follow `HUMAN_WRITING.md`. Every sentence in this note must carry information. No filler. If a section has nothing meaningful to say, write one honest sentence saying so ("No conversations were captured this week. The capture folders still don't exist.") rather than padding.

---

## Step 7: Update the Weekly Synthesis Index

Read `60_Claude/50_Reviews/Weekly Synthesis/Weekly Synthesis Index.md`. Add the new review to the index table.

---

## Step 8: Log the Session

Append to `60_Claude/07_AI_Information/Session Logs/log.md`:

```
## [YYYY-MM-DD] review | Weekly Synthesis YYYY-WXX

[2–3 sentences: what the review surfaced, what's most behind, what next week's top priority is.]
```

---

## Execution Notes for Future Claude

- This skill is called by a Cowork scheduled task every Monday morning. You start cold with no prior context. The pre-flight reads are not optional.
- The three-month plan started April 24, 2026. Use that anchor to calculate which phase and week you're in.
- The master plan's "Weekly Operating Rhythm" section defines the expected weekly cadence. Compare actual vault activity against it honestly.
- If conversation capture folders (`60_Claude/05_Clippings/AI Conversations/` and `60_Claude/30_Source_Summaries/AI Conversations/`) don't exist yet, flag this every week until they're created. This is the most critical missing piece of the build spine.
- If it's the last week of a month, also check whether a monthly review note belongs in `60_Claude/50_Reviews/`.
- Do not modify raw clippings, archive notes, `.obsidian/`, `.claude/`, `.kiro/`, or `.cursor/` directories.
- Prefer patching existing notes (vault_patch by heading) over full rewrites.

---
type: evergreen
status: sprout
created: 2026-08-11
updated: 2026-08-11
tags:
  - system
  - standards
notes:
  - "[[30_Order/Templates/Capability/AI Tools Weekly Review Template]]"
  - "[[30_Order/Templates/Capability/AI Tools Monthly Review Template]]"
  - "[[60_Claude/30_Reviews/AI/Tools/Tool log]]"
  - "[[20_Progress/AI/Claude Code/Write Log]]"
  - "[[20_Progress/AI/Claude Code/_All-Projects-Sync-Log]]"
  - "[[HUMAN_WRITING]]"
---
# Review Standard
==A review cites the actual log rows it read — Tool log, Sync-Log, Write Log — it never summarizes from memory or impression.==
This is the content standard for `60_Claude/30_Reviews/AI/Scheduled/{Weekly,Monthly}/` reviews — how Claude Code, Cowork, and the sync layer are actually being used and whether anything synced/captured is drifting. It governs a different subject than [[30_Order/Templates/Capability/Weekly Synthesis Template|Weekly Synthesis Template]]/`Monthly Synthesis Template.md`, which review concept mastery (the Capability Engine) — do not conflate the two folders or reuse one template for the other's job.
## Maps To
- Templates: [[30_Order/Templates/Capability/AI Tools Weekly Review Template|AI Tools Weekly Review Template]], [[30_Order/Templates/Capability/AI Tools Monthly Review Template|AI Tools Monthly Review Template]]
## Used By Workflow
- Manual, human-triggered — no cron job writes a review. A review is produced by opening the relevant template and working through it against the real logs, the same session or shortly after the period it covers. Nothing here auto-generates from the logs; a human (or an agent explicitly asked to) reads them and writes the review.
## Per-Heading Standard
### Period Covered
The exact date range, matched to the template's own cadence (calendar week for Weekly, calendar month for Monthly). No partial or rolling windows without saying so explicitly.
### Sources Reviewed
Name every log actually opened this pass: [[60_Claude/30_Reviews/AI/Tools/Tool log|Tool log]] (skill/tool use), [[20_Progress/AI/Claude Code/_All-Projects-Sync-Log|_All-Projects-Sync-Log]] (sync health across every project mirror), [[20_Progress/AI/Claude Code/Write Log|Write Log]] (structural changes to the sync layer itself), and the raw `AI Conversations/` session notes for anything the Tool log flags as worth a closer look.
> [!WARNING]
> Listing a log here that wasn't actually opened. If a log wasn't checked this pass, say so — "Sync-Log not reviewed this week" is honest; a missing citation for a claim about sync health is not.
### What Ran This Period
Which skills/agents/commands were used, how often, on what — pulled from Tool log rows in the period, not re-derived from raw sessions. A table or short list, not prose paragraphs.
*Density:* as long as the Tool log actually has rows for the period. An empty Tool log for the period is itself a finding, not something to pad around.
### Sync & Capture Health
Real numbers from the actual logs: how many sync runs, how many failures/skips and why, whether conversation capture produced a note for every real session in the period (cross-check against `~/.claude/projects/` session counts where feasible, not assumed from the Tool log alone).
> [!WARNING]
> "Sync looked fine" without a number. State the actual OK/failed count from `_All-Projects-Sync-Log.md` for the period.
### Findings
Named, specific problems — a stale note, a tool that hasn't been used since promotion, a sync gap, a title bug, a session that never got captured. Each finding names the exact file/log row it comes from.
*Density:* real findings only. "Nothing to report" is a valid, honest finding — do not invent one to fill the section.
### Decided Fixes
Only items where the fix is unambiguous *and* the review has 100% clarity on what happened — per `_docs/Design.md`'s sequencing rule, already adopted for this vault (2026-08-10): a review surfacing a problem is not itself authorization to auto-fix it. An item lands here only when the reviewer is certain, and even then the fix is applied by hand or flagged for the next build session — never by an automated process this review triggers.
> [!WARNING]
> Moving a finding here just because it's annoying, not because it's actually understood. If the root cause isn't confirmed, it belongs in Open Questions, not here.
### Open Questions
Findings that need more evidence before a fix is safe to name — the honest default for anything not 100% clear. Carries forward to the next review if still unresolved; deleting an open question without resolving it is not allowed.
### Next Period's Watch List
What to specifically check next time — a tool recently promoted, a sync leg recently changed, a capture gap recently fixed and now needs confirming it held.
## Done Conditions
- Every claim in Sync & Capture Health traces to a real log row, cited by file and (where the log has one) date/line.
- Decided Fixes contains only items with 100% clarity; anything less stays in Open Questions.
- No `---` in the body; zero blank lines except after a callout; no duplicate frontmatter keys.
- Passes [[HUMAN_WRITING]]'s core test: no sentence that could be pasted into a generic status-report template unchanged.
## Gold Standard Example
None yet — the first real Weekly review against this Standard becomes the example once written.

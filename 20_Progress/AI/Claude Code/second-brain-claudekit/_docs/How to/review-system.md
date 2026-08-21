# How to — Jarvis's review system

Source: `_docs/Jarvis.md`'s "`60_Claude/30_Reviews/AI/` — the review layer" section (confirmed 2026-08-19, citing a direct 2026-08-10/11 build). Not re-researched here — this doc restates it in operating-instructions form and adds the one open question `_docs/Jarvis.md` flags: what this repo's own pipeline activity should feed into it.

## What actually exists

- **Governing standard:** `30_Order/Standards/Review Standard.md` (Jarvis-side). A review must cite the real log rows it read — Tool log, Sync-Log, Write Log — "it never summarizes from memory or impression."
- **Templates:** `30_Order/Templates/Capability/AI Tools Weekly Review Template.md` and `.../AI Tools Monthly Review Template.md`. Sections: Period Covered, Sources Reviewed, What Ran This Period, Sync & Capture Health, Findings, Decided Fixes, Open Questions, Next Period's Watch List. Monthly adds a Tool Map Health Check flagging anything stuck at one pipeline stage for over a month.
- **Data source:** `60_Claude/30_Reviews/AI/Tools/Tool log.md` — one row per skill/command/agent invocation (`Date | Project | Skill/Command | What It Did | Outcome | Source`), written only by `/export-ai-session`, never hand-edited. **Zero data rows as of 2026-08-19** — nothing has run `/export-ai-session` against a real session yet.

## Trigger: manual, human-triggered, by design

`Review Standard.md`'s own `Used By Workflow` field states this explicitly: **"Manual, human-triggered — no cron job writes a review."** This is a deliberate design decision, not a gap — see `_docs/Jarvis.md`. There is no scheduling mechanism for the review-writing step itself; what's actually missing (per `_docs/Jarvis.md` / `10_Areas/AI/Setup/Gaps.md`) is a *cadence reminder* (something that prompts a human to sit down and write the next review), not an auto-generator.

## The 100%-clarity gate

`Review Standard.md`'s `Decided Fixes` section: *"a review surfacing a problem is not itself authorization to auto-fix it... even then the fix is applied by hand or flagged for the next build session — never by an automated process this review triggers."* A review can name a finding; it cannot itself cause a change. This mirrors `_docs/Design.md`'s self-improvement sequencing rule for this repo — evidence accumulates, decisions happen later, separately, deliberately.

## What's real vs. what's still missing (as of 2026-08-19)

| Built | Missing |
|---|---|
| Standard, both templates, `Tool log.md` schema | `Tool log.md` has zero rows |
| — | No review has ever been written under the new Standard ("Gold Standard Example" field: "none yet") |
| — | `Conversations/` subfolder is untouched, no defined purpose distinct from `Tools/` |
| — | No cadence-reminder mechanism for the review-writing step |

## What this repo's own pipeline activity should feed into it

Not yet decided, and this doc doesn't decide it — `_docs/Jarvis.md`'s own table ("What goes where, concretely") already flags this as open: a `tested-tools/_future/<repo>/` promotion has "no Jarvis-side row shape decided" and `tests/` has "no Jarvis-side equivalent... likely referenced from the same `Tool Map.md` row... not yet decided." The mechanical link that *would* close this gap: every real pipeline-stage change this repo makes (a `sandbox/` clone, a `tested-tools/` promotion, a verdict like the CPR blend decision) is exactly the kind of dated, evidenced event `Tool log.md` or a future review's "What Ran This Period" section is built to cite — but nothing here writes to `Tool log.md` automatically, and per the 100%-clarity gate above, nothing should without a human deciding to build that link deliberately. Flagging the shape of the gap, not building it.

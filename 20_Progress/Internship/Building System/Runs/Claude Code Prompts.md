---
type: project
status: active
created: 2026-07-26
updated: 2026-08-28
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts —
    Archive]]"
tags:
  - internship
  - automation
  - prompts
next: "Prompts 20/21 archived 2026-08-28 — both completed (0 deadline matches in
  the 08-28→08-31 window, real deadlines exist but are all months out). A real
  cross-session bug happened and was fixed: Prompt 21 wrongly deleted 6
  legitimate no-deadline links Prompt 20 had added; restored directly in No
  Deadline.md's \"External sources (Prompt 20)\" section. Prompts 22/23 are
  follow-ups meant to continue in the SAME two sessions (not fresh ones) since
  both need context already built this cycle. Prompt 22: deep individual-posting
  dive into the big aggregator repos
  (speedyapply/jobright-ai/sharunkumar/InternDock drops), output as a flat link
  list in _Today/New Internships Listings.md. Prompt 23: three parts — re-verify
  the 279 no-deadline dossiers via a different method (company-wide program
  pages, grouped by company), populate Tracker/Deadline Tracker.md (skeleton
  already exists) with every dossier that has a real deadline, and write
  20_Progress/Internship/Building System/Dossier Corrections — an audit of
  what's wrong with the dossiers found during the deep read (likely-duplicate
  pairs already spotted, misclassification, dead postings)."
---
# Claude Code Prompts — Internship Research Loop
This file holds the next prompt(s) to run, and only that — it gets wiped and rewritten every build cycle, not accumulated. When a prompt finishes and its result is reviewed, its full text and result move into [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]] and get deleted from here.

## Prompting Guide In Use
[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) — re-apply on every prompt.
- Front-load everything, literal scope, explicit Task Order/Files Touched, `high` effort, generous `max_tokens`.
- Hand over verified facts, instruct re-checking them.
- **A hypothesis this file itself wrote can turn out wrong — say so plainly when it does, don't quietly drop it.** Prompt 14 v2's own JGCL hypothesis (a `SOURCES`-tuple tie-break bug) was checked and found wrong; the real cause was three specific already-deleted scholarship postings. That's now the record, not the guess that preceded it — every doc touched below corrects to the real finding, not a hedge between the two.
- **An alarming-sounding fact ("46 deletions") is worth one direct check before treating it as a problem.** It resolved in one search — a real, already-tracked session (auto-captured, per this vault's own conversation-export layer), not an untracked gap. Cheap to verify, expensive to leave as a nagging unresolved worry across future prompts.
- **When a real source count changes, every doc that states a specific number becomes a small, precise lie until corrected.** Lever going live makes "eight sources" wrong wherever it's written — treat this the same as any other now-stale claim, not a footnote.

---

- **A local git checkout goes stale fast on this project — the pipeline auto-commits hourly.** Read state files via `git show origin/master:<path>`, or `git fetch` + confirm local `HEAD` matches `origin/master` (pull/rebase if not) before trusting any local working-tree read of anything `run_pipeline.py`/`recheck.py` touches. Caught live 2026-08-27: a local `git show`-free read of `state/debate_losses.json` showed 6 entries where `origin/master`'s real, current file had 271 — a local clone can sit dozens of commits behind within a single day.

- **A session sharing a file with a parallel session must only ever append or fix its own entries — never remove something it didn't write because it looks unfamiliar or out of scope.** Real incident, 2026-08-28: Prompt 21's session found 6 legitimate links Prompt 20's session had added to a shared `No Deadline.md` (companies with no existing dossier, correctly out of Prompt 21's own 320-dossier scope) and deleted them as presumed noise during its own cleanup pass. Caught and restored by the coordinating session, not by either prompt session itself. If something in a shared file looks wrong, say so in the report — don't unilaterally remove it.
- **When a follow-up genuinely needs the same deep context a session just built (e.g., re-checking its own just-completed work), tell the human to continue in the SAME session, not paste into a fresh one.** Re-deriving 320 already-read dossiers from scratch in a new session would re-burn the exact token cost being complained about — this project's usual "fresh session per prompt" default is a good default, not an absolute rule, when continuity itself is the point.

# Jarvis
### Prompt 22: New Internships Listings — Deep Individual-Posting Dive Into The Big Aggregators
**Paste as a follow-up in the SAME session that ran Prompt 20 — do not start fresh.** That session already has the full context (which repos were checked, what's already in `No Deadline.md`, why speedyapply/jobright-ai/sharunkumar's table formats have no deadline column) — re-deriving that in a new session burns tokens for nothing. If that session is gone, the essential carry-over context is in Prompt 20's archived result (`Claude Code Prompts — Archive.md`) — read that first.

```
**Context — the actual gap Prompt 20 left, don't re-litigate what it already found:** Prompt 20 confirmed 4 table-shaped repos (speedyapply/2026-AI-College-Jobs ~1526+ rows, speedyapply/2026-SWE-College-Jobs, jobright-ai/2026-Software-Engineer-Internship, sharunkumar/Summer-Internships ~6876 lines, northwesternfintech/2026QuantInternships) have NO deadline column — only "Date Posted"/"Age." That finding stands, don't re-check it. What Prompt 20 did NOT do: open the individual postings inside these lists (and the two main InternDock drops, 650+ listings each) to see whether their own pages state a deadline the table doesn't, and — separately — to find genuinely new, eligible postings this project doesn't have yet, deadline or not.

**The actual ask now (the human's own words): search for filtered deadlines, but also just find internships that pass profile eligibility, regardless of deadline. Every one that passes gets a link pasted into `10_Areas/Career/Internships/List/Dossiers/_Today/New Internships Listings.md` (currently empty) — that's it, a flat list of links, not per-posting dossier notes, not deadline-based routing.**

**Eligibility gate — the same 4 hard gates Prompt 20 already used** (from `Source of Truth.md`, permissive-by-default): Summer 2027 / Winter 2027 (Dec 2026-Jan 2027) / Spring 2027 timing; US location (ambiguous/remote passes); OPT-eligible (rejected only on explicit citizenship/clearance/no-CPT language); genuinely CS/software-engineering-relevant. A posting passing this bar is "extremely useful/relevant" enough to list — no separate second-tier judgment call needed on top of it.

**Make this tractable — don't open 1526+6876+650+650 postings one at a time.** Prefilter first: grep/scan each list's title column for CS/SWE-shaped keywords (software, developer, engineer, SWE, backend, frontend, full stack, machine learning, AI, data science, devops, infrastructure) before opening anything — most of these lists cover every major, and the bulk can be excluded by title alone, cheaply. Within the CS/SWE-shaped subset, prioritize by the list's own "Date Posted"/"Age" column — newest first, since those are most likely still open and most likely to actually need this deadline check. Only open a posting's real page (for deadline + final eligibility confirmation) once it's cleared the keyword prefilter.

**Dedup, twice over:** (1) against the 320 existing vault dossiers (search company+title before listing anything) — many of these aggregator repos re-list postings already covered by SimplifyJobs/vanshb03/zshah101; (2) against what's already in `_Today/No Deadline.md` and `_Today/New Internships Listings.md` itself, including the "External sources (Prompt 20)" section restored there 2026-08-28 (Maximor AI, GlossGenius, Amazon, Apple, Whop, Ancestry — don't re-list these).

**Priority order:** InternDock's two main drops first (already-known real, high-volume ongoing sources), then speedyapply's two lists, then jobright-ai/2026-Software-Engineer-Internship, then the rest as time allows. Given the real scale here, you almost certainly won't finish everything — stop and report exactly what you covered and what's left, don't silently truncate.

**Shared-file discipline (a real mistake happened here once already — see Prompt 21's archived result):** `_Today/New Internships Listings.md` and `_Today/No Deadline.md` are also being touched by the parallel session running Prompt 23 right now. Use `vault_patch` `operation: append` only. **Never delete or "clean up" an entry in either file that you didn't personally add in this exact session — even if it looks unfamiliar or out of scope to you. If something looks wrong, say so in your report; don't unilaterally remove it.**

### Report back
Per source: postings scanned / passed keyword prefilter / passed eligibility (now linked in New Internships Listings.md) / real deadline found among those (call it out specifically, even though the window itself is likely still empty) / duplicates skipped. What's left unchecked, named plainly.
```

### Prompt 23: Deeper No-Deadline Re-Verification + Deadline Tracker + Dossier Corrections
**Paste as a follow-up in the SAME session that ran Prompt 21 — do not start fresh.** It already read all 320 dossiers in depth this cycle; re-deriving that from a new session would re-burn the exact token cost the human is objecting to. If that session is gone, the essential carry-over is in Prompt 21's archived result — read that first, and re-read the actual dossier content directly (not from memory) before writing anything below, since this task is explicitly checking your own prior work.

```
**Context — the human is explicitly skeptical of the "279 confirmed no-deadline" result and wants a real, differently-angled re-check, not a re-statement.** Three real tasks, in this order:

### Task 1 — Re-verify the no-deadline claim with a genuinely different method
The original pass checked each dossier's stored text, then (if nothing) the individual posting's own URL. That leaves one real gap: many companies publish a blanket "applications close [date]" or "priority deadline [date]" on their **general internship-program landing page**, not on each individual req page — a per-req check would miss this entirely. Group the 279 no-deadline dossiers by company (this cuts real work a lot — ByteDance, American Express, Zipline, Optiver, Jane Street, Microsoft, DRW, AMD, and Akuna Capital alone account for a large share of the 279 across multiple dossiers each). For each unique company, find and check its actual internship-program landing/careers page (not the specific req) for a program-wide deadline. If found, it applies to every one of that company's dossiers in the 279 — update all of them at once. If a company genuinely has no program-wide deadline stated either, that company's dossiers are now doubly-confirmed, cite both checks in your report. Budget discipline: same as before — if you can't finish every company, stop and report exactly which are done and which remain, don't guess the rest as re-confirmed.

### Task 2 — Populate `10_Areas/Career/Internships/Tracker/Deadline Tracker.md`
The human already created the skeleton — use it as-is: `# Already Over`, `# Upcoming` with `## Soon` / `## Next Week` / `## Next Month`. Populate with every dossier that has a REAL, confirmed deadline — both the 41 already found in Prompt 21's sweep (outside the 08-28→08-31 window: Manhattan Associates, Deloitte ×2, KeyBank, Booz Allen, Honeywell, LPL Financial, Walleye Quantic ×2, JPMorgan ×3, CACI, Fifth Third Bank, Castleton CCI ×3, Ameren, WEC Energy ×2, Medtronic, Western Digital ×4, Google ×2, DTCC, Walleye Investment, GE Vernova, Amex Financial Crimes, Moog, RTX, Regions Bank, and others — re-confirm the full list from the archived report rather than assuming this exact list is complete) and any new ones Task 1 surfaces. Each entry: a real `[[wikilink]]` to the actual dossier note plus its real deadline date, sorted into the bucket it actually falls into relative to 2026-08-28 (define your own cutoffs if the given buckets don't cleanly fit something months out like Deloitte's 12/1/26 — add a `## Later` bucket rather than force a bad fit, and say you did so).

### Task 3 — Write `20_Progress/Internship/Building System/Dossier Corrections`
You just read all 320 dossiers in real depth for this sweep — capture what you noticed wrong along the way, not just deadlines. Real, already-spotted seeds to verify and expand on (don't stop at just these): (1) likely duplicate pairs from near-identical titles for the same company — e.g. `AI Network Automation Engineer Intern - Global Physical Network Infrastructure - ByteDance.md` vs. `AI Network Automation Engineer Intern, Global Physical Network Infra - ByteDance.md`; `Applied Machine Learning Production Engineer Intern - AML Production Engineer - ByteDance.md` vs. `Applied Machine Learning Production Engineer Intern - ByteDance.md`; `Data Lake Infrastructure & Data Analytics Research Engineer Intern...` vs. `...and Data Analytics...` (same company) — check whether these are genuinely the same posting duplicated or genuinely two different reqs, and say which; (2) any dossier your deep read found misclassified into the wrong priority bucket (an adjacent-field or business/finance role sitting in AI/ML or Fullstack without real software content, the same failure class this project's 2026-08-23 audit already found and partially fixed); (3) any dossier whose posting is now visibly closed/expired/redirected (beyond the 2 dead links Prompt 21 already found) that a human would waste time screening; (4) any dossier that clearly doesn't fit the human's real profile once you've actually read the full posting text (PhD-only, clearance-required, or otherwise miscategorized as eligible). Cite the real dossier filename and the specific reason for every finding — this project's own convention (see `CLAUDE.md`), no vague claims. This is a report-only audit — don't fix anything in this pass, just document it with enough specificity that a future prompt can act on it.

### Shared-file discipline
Same as Prompt 22 — `No Deadline.md`/`_Today/` are shared with the parallel session. Append-only. **Never remove an entry you didn't personally add — if something looks out of scope, say so in your report instead of deleting it.** (This is the exact mistake this session made last round with Prompt 20's 6 restored links — don't repeat it in the other direction.)

### Report back
Task 1: how many companies re-checked, how many surfaced a new deadline, how many remain unchecked. Task 2: total entries added to Deadline Tracker, by bucket. Task 3: the full corrections list, cited.
```


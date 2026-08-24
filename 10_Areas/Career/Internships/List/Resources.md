---
type: evergreen
status: active
created: 2026-07-26
updated: 2026-08-24
notes:
  - "[[20_Progress/Internship/Building System/Research Loop - Resources]]"
  - "[[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]]"
tags:
  - internship
  - automation
  - resources
next: "Update the table below whenever a source is checked for exhaustion or a new run's numbers land."
---
# Resources — Live Usage Tracker
## Overview
==A visualization and numeric explanation of the resources used to get internships — the operational companion to [[20_Progress/Internship/Building System/Research Loop - Resources]], which plans what exists and what's next.== Track, per resource: how close to maxed out is it, how many finds were actually useful vs. not, and whether waiting for the next update is worth it based on what the last few updates actually produced. The goal is that discovery never truly ends — a source running dry always has a named next alternative, not a dead stop.
## How To Read "Exhaustion" Here
A source isn't exhausted when its raw entry count is low — SimplifyJobs has 14,900+ entries and still rejects almost all of them on eligibility. It's exhausted when the **rate of new eligible candidates per run** drops toward zero for a sustained stretch, not when the feed itself is small. Check this before assuming a quiet week means nothing left to find — it might just mean nothing new was posted.
## Per-Source Table
| Source | Last checked | Raw scale | Eligible-match trend | Exhaustion signal? | Alternative if exhausted |
| --- | --- | --- | --- | --- | --- |
| SimplifyJobs | 2026-08-24 | 290K+ fetched, 1.5% match rate, **137 live dossiers** | High volume, most rejected on category/timing, not scarcity — match rate stayed near this low all along, it's the source's normal shape, not new decay | No | — |
| Jose-Gael-Cruz-Lopez | 2026-08-24 | **0 live dossiers**, despite 76 real matches logged over the last 20 runs | **Resolved 2026-08-24, not a bug.** Its entire currently-matching pool is three non-software scholarship/fellowship postings (MLH Fellowship, White House HBCU Scholars Program, UNCF Scholarships Portal), correctly deleted by a human during the 2026-08-23 audit and sitting in `seen_ids.json`, which by design never re-offers them. The feed is just thin toward non-CS content for this persona | No — resolved, not exhaustion | Already de-prioritized relative to the other sources |
| vanshb03 | 2026-08-24 | 26.6% match rate, **74 live dossiers** | Steady producer, second-highest match rate of the nine sources | No | — |
| zshah101 | 2026-08-24 | 12.1% match rate, **68 live dossiers** | Steady | No | — |
| Greenhouse (7 tokens) | 2026-08-24 | 53.6% match rate (small pre-curated set), **16 live dossiers** | Fixed seed list — ceiling is the token list, not the API | **Yes, structurally** — bounded by hand-verified tokens | Task F: verified-live token expansion (see Runs/Claude Code Prompts) |
| Ashby (5 tokens) | 2026-08-24 | **0 live dossiers** | Same structural ceiling as Greenhouse | **Yes, structurally** | Same — Task F |
| freehire | 2026-08-24 | 28.6% match rate but only **2 live dossiers** — tiny absolute volume | **Resolved 2026-08-24, working as designed, not an open question.** `FREEHIRE_COMPANIES` is deliberately just `{google, uber}` by design (documented, not an oversight); a live fetch returned 6 postings, mostly non-US/non-eng, correctly filtered downstream by the existing gates | No — low volume by deliberate scope, not decay | — |
| artificialintelligencejobs.co (AIJobs) | 2026-08-24 | 25.6% match rate, **11 live dossiers** | Steady | No | — |
> [!IMPORTANT]
> This table is hand-updated from real checks (`gh api`, live fetches, a `loop-verifier` run) — never estimated. If a number here hasn't been refreshed in over two weeks, treat it as stale, not current.
## Real Backlog Event (2026-07-25)
Adding the four newer sources produced a one-time backlog of 186 new candidates, 171 clearing the write gate on the first dry run — not exhaustion, the opposite problem (an oversupply spike from newly-added coverage). Handled by `MAX_NEW_WRITES_PER_RUN = 18` throttling and deferring the rest, confirmed firing in production the same day (`written_count: 13`, `deferred_count: 166` on the first real run). Worth remembering this pattern: adding a new source can spike supply before it settles into a steady rate — don't mistake a backlog for exhaustion in either direction.
## Useful vs. Not — Quality Signal
Once the priority-classification code (Task B, `Runs/Claude Code Prompts.md`) is live, this section tracks, per source: how many of its dossiers survived the fit test into a Program note vs. sat unpromoted past a reasonable review window. A source that produces volume but never survives screening is a lower-value resource than its raw count suggests, no matter how large the feed is — update this once real promotion data exists to compare against.

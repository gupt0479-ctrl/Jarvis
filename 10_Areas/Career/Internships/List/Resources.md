---
type: evergreen
status: active
created: 2026-07-26
updated: 2026-07-26
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
| SimplifyJobs | 2026-07-25 | 14,900+ entries | High volume, most rejected on category/timing, not scarcity | No | — |
| Jose-Gael-Cruz-Lopez | 2026-07-25 | ~112 entries | Small and thin by design | Watch — smallest source | Already de-prioritized relative to the other five |
| vanshb03 | 2026-07-25 | 274 entries | Re-checked live, unchanged count from prior check | No | — |
| zshah101 | 2026-07-25 | 214 entries | Re-checked live, unchanged count from prior check | No | — |
| Greenhouse (7 tokens) | 2026-07-25 | 7 verified-live company boards | Fixed seed list — ceiling is the token list, not the API | **Yes, structurally** — bounded by hand-verified tokens | Task F: verified-live token expansion (see Runs/Claude Code Prompts) |
| Ashby (5 tokens) | 2026-07-25 | 5 verified-live company boards | Same structural ceiling as Greenhouse | **Yes, structurally** | Same — Task F |
| freehire | 2026-07-26 | 4,270,639 postings, 187,542 companies | **Confirmed live** as of 2026-07-26 — not yet in `recheck.py`'s `FEEDS`, worth confirming why | No | Lever, if this ever thins out |
| artificialintelligencejobs.co | 2026-07-26 | 17,507 jobs, 184 explicit `Intern` | **Confirmed live**, in `recheck.py`'s `FEEDS` | No | — |
> [!IMPORTANT]
> This table is hand-updated from real checks (`gh api`, live fetches, a `loop-verifier` run) — never estimated. If a number here hasn't been refreshed in over two weeks, treat it as stale, not current.
## Real Backlog Event (2026-07-25)
Adding the four newer sources produced a one-time backlog of 186 new candidates, 171 clearing the write gate on the first dry run — not exhaustion, the opposite problem (an oversupply spike from newly-added coverage). Handled by `MAX_NEW_WRITES_PER_RUN = 18` throttling and deferring the rest, confirmed firing in production the same day (`written_count: 13`, `deferred_count: 166` on the first real run). Worth remembering this pattern: adding a new source can spike supply before it settles into a steady rate — don't mistake a backlog for exhaustion in either direction.
## Useful vs. Not — Quality Signal
Once the priority-classification code (Task B, `Runs/Claude Code Prompts.md`) is live, this section tracks, per source: how many of its dossiers survived the fit test into a Program note vs. sat unpromoted past a reasonable review window. A source that produces volume but never survives screening is a lower-value resource than its raw count suggests, no matter how large the feed is — update this once real promotion data exists to compare against.

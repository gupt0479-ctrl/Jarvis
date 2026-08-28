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
next: "Prompts 18/19 archived 2026-08-28 (both landed cleanly — 778f531
  committed locally, unpushed; full suite 444 passed; process note in Prompt
  18's result about how the two sessions' overlapping WIP got reconciled).
  Prompts 20/21 (both Jarvis, run in parallel, real web access required) are the
  human's urgent pivot away from more infra work: deadline-triage everything
  into 10_Areas/Career/Internships/List/Dossiers/_Today/ (deadline = 2026-08-28
  through 08-31) or _Today/No Deadline.md (genuinely no deadline found). Prompt
  20 covers ~40 newly pasted external links + a PDF's worth of job-board
  aggregator repos, none yet in the vault. Prompt 21 covers all 309 existing
  live dossiers. Both are large, likely-incomplete-in-one-pass tasks by design —
  explicitly told to stop and report what's left rather than silently truncate.
  Still real and unwritten: a Jarvis prompt for the 2026-08-26 postmortem's
  review-system-tightening + full Source of Truth/Build Log staleness pass
  (deferred again this round for the same reason as last time — not what the
  human asked for right now). Also still pending: pushing 778f531 to origin —
  not done, wasn't asked for this round either."
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

# Jarvis
## Prompt 20: New External Sources — Deadline Triage (Pasted Links + Job-Board Aggregators)
**Run inside the Jarvis vault directly** (Windows, Sonnet 5, high effort, real web access required — WebFetch/WebSearch, not just vault tools). Runs in parallel with Prompt 21 in a separate session — both write into the same vault. The only real shared-file risk: both sessions append to `_Today/No Deadline.md`. Use `vault_patch` with `operation: append` for that file (never a full overwrite) — appends from two sessions landing in either order is harmless; a full rewrite from one session could silently discard the other's work mid-run.

```
**Context — what this is and isn't, verified 2026-08-28, don't re-derive:** `10_Areas/Career/Internships/List/Dossiers/_Today/` exists, currently holding only one file: `No Deadline.md` (a bare link-collector note, 28 bytes, just a heading — not a folder of individual notes). The human wants ONE thing done, fast: for every real internship posting reachable through the sources below, find its application deadline. If the deadline is 2026-08-28, 08-29, 08-30, or 08-31: create a real dossier-style note for it (schema below) and place it directly in `_Today/`. If no deadline is findable anywhere after a genuine search (posting page, company careers site, a direct web search for "[Company] [Title] internship application deadline"): add ONLY a wikilink to it under `_Today/No Deadline.md` — don't create a separate note for it, just interlink. Anything with a deadline outside that 4-day window: skip entirely, don't file it anywhere (out of scope this round).

**Eligibility gate — apply before doing any deadline work on a posting, so this doesn't flood the vault with irrelevant entries.** This project's existing 4 hard gates (from `Source of Truth.md`, permissive-by-default — keep on ambiguity, reject only on an explicit negative signal): (1) Summer 2027 / Winter 2027 (Dec 2026-Jan 2027) / Spring 2027 timing; (2) US location (an explicit foreign-only posting rejects, ambiguous/remote passes); (3) OPT-eligible (rejected only on explicit citizenship/clearance/no-CPT language — "no visa sponsorship" alone is NOT a rejection signal); (4) genuinely CS/software-engineering-relevant (adjacent fields like hardware/robotics pass only with real software content). Skip (create nothing for) anything that clearly fails one of these on its face.

**Dedup — check before creating anything.** Many of these aggregator repos re-list postings already in the vault via SimplifyJobs/vanshb03/zshah101/etc. Search the vault (company + title, or the posting URL) before writing a new note — if a dossier for it already exists anywhere under `List/Dossiers/` (including `Viewed/`), don't duplicate it; if IT has a deadline in the 4-day window, copy that existing dossier's content into `_Today/` instead of writing a fresh one.

**New-note schema** (mirror the existing dossier frontmatter exactly, `vault_get_document_map` any existing dossier under `List/Dossiers/1 - AI & ML/` to confirm the shape fresh): `company, title, url, source, terms, locations, target_year, date_posted, date_found, matched_reason, status: unreviewed, next: null, tags: [internship, auto-discovered]`. Body: the real fetched posting content, same style as existing dossiers (a short `> [!NOTE]` callout citing what matched, then the posting text). Set `source` to the real origin (e.g. "InternDock", "ApplyGuy-manual", the repo name) — don't reuse an existing source name that doesn't apply.

**Sources, in priority order — work top-down, real individual postings first (cheap, high-confidence), bulk aggregator repos last (each is its own large sub-task). Given the realistic scale here, you will very likely not finish everything — that's expected. STOP and report exactly what you covered and what's left untouched if you run low on time/budget. Do not silently truncate or guess at what you didn't reach.**

1. Direct posting URLs (one deadline check each):
   - https://jobs.smartrecruiters.com/WesternDigital/744000138727213
   - https://jobs.ashbyhq.com/Deepgram/dc8693b5-72ce-4ca3-ab15-9c8434d35da1
   - https://job-boards.greenhouse.io/embed/job_app?for=nuro&token=7351061
   - https://www.zipline.com/open-roles?gh_jid=7974897003
   - https://jobs.ashbyhq.com/maximor/3ff6e57d-5430-4836-b6f0-19044d8ee6d8
   - https://job-boards.greenhouse.io/glossgenius/jobs/7978666003
   - https://careers.qtsdatacenters.com/us/en/job/QDCQDCUSR20261881EXTERNALENUS/Summer-2027-Internship-Technical-Project-Management
   - https://careers.qtsdatacenters.com/us/en/job/QDCQDCUSR20261907EXTERNALENUS/Summer-2027-Internship-Process-Analytics-Technology-Delivery-Team
   - https://egup.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/20278594/
   - https://ehzq.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/115681/
   - https://www.amazon.jobs/en/jobs/10517567/software-development-engineer-intern-annapurna-labs-2027
   - https://jobs.apple.com/en-us/details/200673612-0836/applied-data-solutions-program-internships-summer-2027
   - https://apply.deloitte.com/en_US/careers/JobDetail/Consultative-Offerings-Summer-Scholar-Software-Engineering/364670
   - https://jobs.ashbyhq.com/whop/1d904ce7-a18d-4dc1-ad05-d4854ceac2a0
   - https://salesforce.wd12.myworkdayjobs.com/en-US/External_Career_Site/job/California---San-Francisco/Summer-2027-Intern---Software-Engineer_JR340771-1
   - https://ancestry.wd501.myworkdayjobs.com/en-US/careers/job/Draper-Utah/Software-Engineer---Observability--Co-op_R003434
   - https://job-boards.greenhouse.io/archer56/jobs/7977707003
   - (Tesla and Rippling links given were an event-signup page and a generic careers-list page, not single postings — treat like the misc board links in step 3, not a single-posting check.)

2. The 4 InternDock guide pages (each lists many postings — treat each as its own mini-source, same shape as the 2 InternDock drops already known to this project). Use the URLs exactly as given, including the query-string token — they won't resolve without it:
   - https://www.interndock.com/tracker/guides/summer-2027-internship-drop-august-2026?mcp_token=eyJwaWQiOjUwOTEwOTcsInNpZCI6NTE1MTQ4Mjc0LCJheCI6ImQ4N2ZlNTAyMmJkYjFiMWFhODg3MmNjNGZlODU3MTVlIiwidHMiOjE3ODYzMzI2MTcsImV4cCI6MTc4ODc1MTgxN30.TjdAKsS_-neVRQo-hRVevJxD3y036wU8qPYKqAjMbN8
   - https://www.interndock.com/tracker/guides/fresh-internship-drop-summer-2027-fall-2026?mcp_token=eyJwaWQiOjUwOTEwOTcsInNpZCI6NTE1MTQ4Mjc0LCJheCI6ImZhMWE2YjUxZDE3YjhjODc3MTk4ODhlYTRmNDAwOTU2IiwidHMiOjE3ODI5NDE3NjYsImV4cCI6MTc4NTM2MDk2Nn0.BEoRmgNt7u0wVlZAoTLxQZIrMgT78TK7TfLmrtuoA0w
   - https://www.interndock.com/tracker/guides/pre-internship-programs-early-insight-college-students?mcp_token=eyJwaWQiOjUwOTEwOTcsInNpZCI6NTE1MTQ4Mjc0LCJheCI6IjA3MWQwODk1NTBmNmFiMGJjZDdjZTE0MjcxMjlhMzlmIiwidHMiOjE3ODU0ODEzODUsImV4cCI6MTc4NzkwMDU4NX0.rnxjpDmzycQb7k90v5_8Pvj0Z8NhdnJHkTxyLxtcTr4
   - https://www.interndock.com/tracker/guides/campus-ambassador-programs-open-now?mcp_token=eyJwaWQiOjUwOTEwOTcsInNpZCI6NTE1MTQ4Mjc0LCJheCI6IjNlZjYyMGQ2MzBhNzQzY2Q4MTc4ZGM1MWEyMzhhNmQwIiwidHMiOjE3ODYyMTk3MzUsImV4cCI6MTc4ODYzODkzNX0.JHpaa5kED4mnFDIsxIsJAeIOQ9g5hxfpxPX2DXxzEqI
   (The last two — "Early Insight" pre-internship programs and "Campus Ambassador" programs — are very likely to fail the CS/software-relevance gate outright; check quickly and skip if so, don't force them through.)

3. Misc board/dashboard links — each may itself list many postings, treat as its own mini-source: rippling.com/careers/open-roles, synk.today/intern, app.dataannotation.tech (a sign-in page — likely nothing to extract, check quickly and skip if so), the Google Sheet (docs.google.com/spreadsheets/.../htmlview), intern-list.com, dataannotation.tech/job-board/software-engineer, tesla.com/event/ncch-resume (an event signup, not a listing — check quickly and skip if so).

4. The PDF's aggregator repos — deprioritize categories almost certainly irrelevant to this persona (Marketing/Design/Sales/Creative; Education/Public Sector/HR/Legal — check last or skip with a one-line note why, given time). Prioritize these first:
   - github.com/vanshb03/Summer2026-Internships (note: this repo's dev README is already this project's live `vanshb03` source at a different URL/year-branch — check whether this is genuinely the same feed already covered before treating it as new)
   - github.com/speedyapply/2026-AI-College-Jobs
   - github.com/speedyapply/2026-SWE-College-Jobs
   - github.com/jobright-ai/2026-Software-Engineer-Internship
   - github.com/jobright-ai/2026-Engineer-Internship
   - github.com/jobright-ai/2026-Data-Analysis-Internship
   - github.com/jobright-ai/2026-Product-Management-Internship
   - github.com/jobright-ai/2026-Business-Analyst-Internship
   - github.com/northwesternfintech/2026QuantInternships
   - github.com/sharunkumar/Summer-Internships (README-Off-Season.md)
   - (Lower priority, check last if time allows: jobright-ai's Consultant/Marketing/Design/Sales/Art/Education/Public-Sector/HR/Legal Internship repos — SimplifyJobs's own Product-Management-role section is likely already covered by the existing SimplifyJobs source, verify before re-processing.)
   Note: `speedyapply`/`sndsh404` were already checked twice this project (2026-08-23, 2026-08-24) and found "structurally blocked — private Supabase backend, README + binary .xlsx only." Re-verify this is still true for the two URLs above before assuming the old finding still holds — a repo can change shape.

### Report back
Per source: real postings found / how many passed the eligibility gate / how many got a deadline match (now in `_Today/`) / how many went to `No Deadline.md` / how many skipped as ineligible or duplicate (with why). Anything not reached due to time, named plainly, not silently dropped.
```

## Prompt 21: Existing Vault Dossier — Deadline Triage (All ~309 Live Dossiers)
**Run inside the Jarvis vault directly** (Windows, Sonnet 5, high effort, real web access for the fallback step). Runs in parallel with Prompt 20 in a separate session. Same shared-file note: append-only (`vault_patch`, `operation: append`) to `_Today/No Deadline.md`, never a full overwrite.

```
**Context — verified fresh 2026-08-28, don't re-derive:** 309 live dossiers exist across `List/Dossiers/{1 - AI & ML (137), 2 - Fullstack (42), 3 - CyS & Finance (49), Other (81)}/` — `Viewed/` is explicitly out of scope (already closed/screened out, not a candidate for `_Today`). These already passed the pipeline's eligibility gates when they were written — **no eligibility re-check needed here, this is purely a deadline pass.** Dossiers carry no `deadline` frontmatter field at all (confirmed — the schema is `company, title, url, source, terms, locations, target_year, date_posted, date_found, matched_reason, status, next, tags`); any deadline information that exists is buried in the posting text already fetched into each note's body.

**Method, in this order (cheap check first):**
1. Read the dossier's own stored body content first (free, no web call) — look for explicit deadline language: "apply by," "deadline," "applications close/due," "priority deadline," a specific date near words like "review" or "close." **Distinguish a real application deadline from an unrelated date** — e.g. Appian's dossier says only "we will officially begin reviewing applications... starting August 2026," which is a review-start date, not a deadline; don't misread one as the other.
2. If nothing explicit in the stored text: do a live `WebFetch` of the dossier's real `url` field. The live page may show a deadline that wasn't there (or wasn't captured) at the original fetch — postings often add a firm close date later as a bucket fills. If the URL is now dead/expired/redirected-away: that's a real, distinct finding — **don't file a dead posting as "no deadline"** (it's not an open no-deadline job, it's closed) — note it separately in your report instead.
3. If still nothing after both checks: append a wikilink to `_Today/No Deadline.md` (only for genuinely-checked, genuinely-unfound cases — see the budget note below).
4. If a real deadline of 2026-08-28, 08-29, 08-30, or 08-31 is found: **copy** (do not move) the dossier's full content into a new note of the identical filename under `_Today/`, leaving the original in its priority-bucket folder untouched. Copy, not move, because several existing dossiers already have real backlinks from `Programs/`/`Tracker/Each One/` notes from prior promotion work (e.g. Appian) — moving the file risks breaking those. Anything with a deadline outside the 4-day window: leave alone, don't file anywhere.

**Budget discipline — 309 is a lot. Work newest-`date_posted`-first (most likely to carry a real, still-current deadline), oldest last. If you can't finish all 309, STOP and report exactly which you checked and which remain untouched — do not guess the rest into "no deadline" or skip silently. An unchecked dossier is not the same as a confirmed-no-deadline one; don't conflate them in `No Deadline.md`.**

### Report back
Total dossiers checked / deadline-matched (now copied into `_Today/`, cite company+title for each) / no-deadline (linked, cite count) / dead-link findings (cite which, separately from no-deadline) / not-yet-checked remainder (exactly which are left, so a future prompt can pick up from there without re-checking what's done).
```


---
type: project
status: active
created: 2026-07-17
updated: 2026-07-18
deadline:
related_progress:
  - "[[20_Progress/Internship/Building System/Internship System — Build Log]]"
  - "[[20_Progress/Internship/Building System/Research Loop — Implementation Plan]]"
tags:
  - internship
  - automation
  - system-design
next: "Check Run Log.md on Mon 2026-07-20 for the first real Sunday 23:00 UTC rollup; evaluate cadence tightening on/after 2026-07-24 (one week of clean runs since 2026-07-17 11:21 UTC). Layer 5 needs a FIRECRAWL_API_KEY before its first live run — it has never executed end-to-end."
---
# Phases 1–3 Run
==Phases 1 through 3 of the internship research loop are complete and live: the automation runs hourly against the real `gupta-builds/Jarvis` vault, has written 137 real dossiers, and has completed six consecutive real runs (three manual, three scheduled) with zero duplicates and zero filed issues.== This note is the single build record across all three phases — what got built, what was verified correct, what broke during live verification and how it was fixed, and what is explicitly still missing. [[20_Progress/Internship/Building System/Research Loop — Implementation Plan]] is the forward spec this was built against; [[20_Progress/Internship/Building System/Internship System — Build Log]] is the folder-structure design this automation writes into. Read this note when picking the work back up — it should answer "what already exists" without reopening the repo.
## What This Automation Does
A GitHub Actions workflow in the public repo `gupta-builds/internship-research-loop` runs hourly: fetches three internship-listing sources, filters against a profile (rising junior, Summer 2027, SWE/AI/data roles), dedups against a persistent seen-set, validates each candidate through a four-check write gate, and writes the ones that pass as thin dossier notes into `10_Areas/Career/Internships/List/Dossiers/` in the real Jarvis vault. ==No LLM call exists anywhere in this loop== — every layer is deterministic field-matching and mechanical checks, by design, per the plan's Layer descriptions.
## Repo And Layer Map
```
internship-research-loop/
├── ingestion/          # Layer 1 — fetch + normalize each source's raw shape
│   ├── sources.py
│   └── normalize.py
├── core/
│   ├── profile.yaml     # filter config
│   ├── filter.py         # Layer 2 — profile match, no LLM
│   ├── identity.py        # Layer 3 — compute_uid()
│   ├── schema_drift.py     # phase 3 — halt-before-fetch drift check
│   ├── git_ops.py           # phase 3 — push with retry-once
│   └── run_log.py            # phase 3 — two-tier run log
├── vault_writer/
│   ├── templates/dossier.md.j2
│   ├── validate.py       # Layer 4 — the four-check write gate
│   └── writer.py           # renders + writes, idempotent on uid
├── run_pipeline.py    # phase 3 — orchestrates all of the above
├── tests/                # 87 tests total, one file per module above
├── state/seen_ids.json  # dedup state, committed after confirmed push only
├── logs/runs.jsonl        # raw per-run log, committed every run
└── .github/workflows/
    ├── run.yml            # hourly cron + workflow_dispatch
    └── test.yml             # pytest on every push
```
## Phase 1 — Ingestion, Filter, Identity (2026-07-16)
*Built:* `ingestion/sources.py` (HTTP fetch per source), `ingestion/normalize.py` (maps each source's raw JSON/markdown shape into one shared `Listing` dataclass), `core/filter.py` (Layer 2 profile matching — a separate `_matches_*` function per source since each source's schema and eligibility signal differs), `core/identity.py` (Layer 3 — stable `compute_uid()`), `core/profile.yaml` (grad year 2028, rising junior, `terms: ["Summer 2027"]`).
*Tests:* `test_filter.py` (13), `test_identity.py` (7), `test_sources.py` (4) — 24 tests, run against saved fixture data, no live network calls, per the plan's build order (prove filter/dedup logic correct by hand before touching Actions or the vault).
*Done correctly:* the `Listing` dataclass and per-source matching split; the uid scheme (`source:raw_id` for the two JSON sources, a content hash of `company|title|url` for zapplyjobs, which carries no upstream id).
*Wrong at the time, corrected in phase 3 step 0:* `profile.yaml`'s `categories` list used the plan's original four generic values (`Software Engineering, Data Science, Machine Learning, Artificial Intelligence`) — these matched almost nothing in live SimplifyJobs data, which actually uses a ten-value taxonomy with two naming eras per relevant category.
## Phase 2 — Vault Writer And Write Gate (2026-07-16)
*Built:* `vault_writer/writer.py` (renders the fixed Jinja2 template, writes idempotently keyed on uid — rewriting the same uid overwrites the same file instead of duplicating it), `vault_writer/validate.py` (the four-check write gate: `required_fields`, `url_liveness`, `not_duplicate`, `format_compliance`), `vault_writer/templates/dossier.md.j2` (the one-line-body dossier shape from the plan — deliberately thin, enrichment is a deferred future layer, not built here).
*Tests:* `test_writer.py` (4), `test_validate.py` (21) — written against a throwaway local test vault copy (`tests/fixtures/throwaway_vault/`), not the real Jarvis repo, per the plan's build order.
*Done correctly:* each write-gate check is independently callable, so a rejection can be logged with exactly which check failed and why; checks run in a fixed fail-closed order with real short-circuiting (no HEAD request fires if required fields are already missing); `format_compliance` uses a custom YAML loader (`_DupeKeyLoader`) that raises on duplicate frontmatter keys instead of silently keeping the last one, a class of bug plain `yaml.safe_load` can't catch.
*Follow-up verification pass:* dropped `locations_allow` from `profile.yaml` entirely rather than leaving it wired to a guessed matching rule — the plan never specified how it should match (substring vs. exact, multi-location arrays, sources with no location data at all), and a wrong guess would have silently dropped real matches with no error to show for it. Also pinned dependencies and closed test gaps found during review.
## Phase 3 — Scheduled Pipeline Against The Real Vault (2026-07-17)
### Step 0: Reconciling The Build Review
Before writing any workflow code, three items flagged in the plan's "Phase 1-2 Build Review" section were checked directly against live data rather than trusted from either side's prior claim.

| Item                        | Build review flagged                                                                                                    | Re-checked against live data                                                                                  | Outcome                                                                                                                                                        |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SimplifyJobs categories** | Original `categories` list matched only 1 of 10 real values                                                             | Fetched live `listings.json`, pulled the actual distinct `category` values                                    | **Corrected** to `["Software", "Software Engineering", "AI/ML/Data", "Data Science, AI & Machine Learning"]` — both naming eras of the two relevant categories |
| **zapply Year matching**    | Plan's literal `"All student(s)"` string doesn't exist in real data                                                     | Grepped live README: `All student` / `All Student` / `All Students`, three casing variants                    | **Corrected** to a normalized `.strip().lower().rstrip('s')` comparison in `_matches_zapply`                                                                   |
| **JGCL listings.json path** | Build report said the path was wrong; a fresh check said it was right — flagged for reconciliation, not silently picked | Re-fetched `.../Jose-Gael-Cruz-Lopez/underclassmen-opportunities/main/.github/scripts/listings.json` directly | **Confirmed already correct** — no code change needed, the build report was the stale side                                                                     |
Investigating the zapply item surfaced a real, previously-undiscovered bug: `parse_zapply_readme` read table columns by fixed position, but the README's "Special Programs & Resources" table is 3-column (`Name | Year | Note`, no Status column) while every other table is 4-column — the fixed-position parser was silently reading Note text into the Year field for that one table. Rewritten to detect `name_idx`/`year_idx` from each table's own header row, with a regression fixture added.
### Four Non-Optional Hardening Requirements
Specified in the original plan as scheduled-run requirements but never built in phases 1-2 — phase 3's actual scope, not just wiring existing pieces together.
1. **Dependency pinning**
	`requirements.txt` pinned to exact versions (`requests==2.34.2`, `pyyaml==6.0.3`, `pytest==9.1.1`, `jinja2==3.1.6`) — unattended operation for months can't tolerate an upstream release breaking mid-cycle.
2. **Push race handling**
	`core/git_ops.py` — the Jarvis vault has its own independent auto-commit-and-push cycle running locally every ~2 hours against the same `origin/master`. `commit_and_push_with_retry()` does `git pull --rebase` before every push, retries exactly once on a rejected push, and raises `GitPushError` (never force-pushes) if the retry also fails. Tested against real local git repos, not mocked — including a genuine injected race and a genuine unresolvable conflict — and mutation-tested by reducing `max_attempts` to 1 to confirm the test actually catches a broken retry.
3. **Seen-state ordering guarantee**
	`run_pipeline.py`'s `run_once()` only calls `seen_ids.update(written_uids)` after `push_fn()` returns successfully, never before:
	```python
	if written_uids and not pushed:
	    pass  # push failed — do NOT mark seen, retried next run
	else:
	    seen_ids.update(written_uids)
	```
	A failed push after marking seen would mean that dossier is gone forever — never in the vault, never retried, because dedup thinks it already landed. Proven by `test_run_once_does_not_mark_seen_when_push_fails` and mutation-tested by removing the guard (confirmed 10 items incorrectly marked seen without it).
4. **Schema drift, auto-filed issues, two-tier log**
	`core/schema_drift.py` fetches one real entry per source before the pipeline touches feeds for real and halts, writing nothing, if an expected field vanished or got renamed — catches the case where a renamed field wouldn't crash the normalizer (it falls back to `.get(..., "")`) but would silently reject everything downstream instead. `run_pipeline.py` calls `gh issue create` in this repo on schema drift, on a push failure, and on a *systemic* write-gate rejection (`required_fields`/`format_compliance` — our own bug), deliberately not on routine ones (`url_liveness`/`not_duplicate` — normal upstream noise that would spam an issue every run). `core/run_log.py` writes the raw per-run JSONL here and appends a weekly markdown rollup into `10_Areas/Career/Internships/List/Run Log.md` in Jarvis, gated to fire once at Sunday 23:00 UTC.
### Workflow And Auth
`.github/workflows/run.yml` runs `cron: '0 * * * *'` (hourly to start, deliberately more conservative than the sources' actual ~30-minute update cadence) plus `workflow_dispatch` for manual triggering. Explicit `permissions: {contents: write, issues: write}` — the default `GITHUB_TOKEN` permission on this repo was confirmed "read", so this had to be stated, not assumed. The workflow checks out this repo, then checks out `gupta-builds/Jarvis` separately into `jarvis-checkout/` using a fine-grained **PAT** (`JARVIS_PUSH_TOKEN` repo secret) scoped only to that one repo with `contents: write` and nothing broader — not the existing broad `gh` CLI token.
## Bugs Found During Live Verification
Both of these surfaced only once the workflow ran against real GitHub infrastructure — neither was reachable by local testing.
### Empty PAT Secret
The first `gh secret set JARVIS_PUSH_TOKEN` attempt (run with no `--body` flag and no piped input) completed with no output and silently set an empty value. The first `workflow_dispatch` run failed immediately at the Jarvis checkout step (`Input required and not supplied: token`) — before touching any real data. Fixed by setting the token directly through the GitHub web UI, confirmed via `gh secret list` showing an updated timestamp.
### Gitlink Pollution From The Nested Checkout
> [!WARNING]
> This one took two attempts — the first fix looked correct in review but wasn't actually staged, and the same warning recurred on the next run.

`jarvis-checkout/` (the second checkout, a full nested git repo living inside this repo's own workspace) got recorded by `git add -A` as a **gitlink** (mode 160000) in this repo's own history, since there's no `.gitmodules` backing it. Harmless to Jarvis itself, but corrupted this repo's history and broke `actions/checkout`'s post-job submodule cleanup. First fix attempt added `jarvis-checkout/` to `.gitignore` and ran `git rm --cached jarvis-checkout`, but only the `rm` got staged — the `.gitignore` edit itself was never `git add`ed, so the committed content didn't actually change (misread `git status --short`'s " M .gitignore", a leading-space *unstaged* marker, as already staged). The warning recurred on the next triggered run. The correct fix staged both changes together, verified via `git diff --cached --stat` before committing, and a re-triggered run confirmed clean.
## Verified Live State (as of 2026-07-17 17:00 UTC)
- **137 real dossiers** written into `10_Areas/Career/Internships/List/Dossiers/` in Jarvis — the first live run wrote all 137, every run since has correctly recognized them as already-seen and written zero duplicates
- **6 consecutive successful runs** against the real vault (3 manual `workflow_dispatch`, 3 scheduled `cron` at 13:05, 15:06, and 17:00 UTC) — the hourly schedule is confirmed actually firing and completing cleanly, not just configured
- **18 persistent rejections** every run, all `url_liveness` failures on genuinely dead/malformed URLs (404/410/403/405, plus one known-malformed Paragon One link) — correctly retried each run since they were never marked seen, correctly never written since the underlying URLs are actually dead
- **0 GitHub issues filed** — schema drift, push failures, and systemic write-gate rejections have not occurred in any of the six real runs
- **Exactly one commit from "internship-research-loop bot"** in Jarvis's history — no duplicate commits, no force-pushes, no collision yet observed with the vault's own independent ~2-hour auto-commit cycle
- **87/87 local tests passing**, CI (`test.yml`) green on every push
- Repo confirmed public via `gh repo view` — unlimited standard-runner Actions minutes per the plan's cost analysis, cadence isn't minutes-constrained
## What's Not Built — Explicit Gaps
- **`locations_allow` filtering** — dropped from `profile.yaml` entirely rather than guessed at, see Phase 2. Revisit now that live runs have produced real `locations` field data to write fixtures against.
- **Weekly rollup into `Run Log.md`, untested against real data** — `should_run_weekly_rollup()` only fires at Sunday 23:00 UTC; the rollup code is unit-tested in isolation but has never actually executed inside a real scheduled run, since no run has yet landed on that exact hour. Its first real firing is the next thing to watch for, not something already confirmed working end to end.
- **Layer 5 enrichment** (company/contact research on promotion) — dossiers are deliberately thin (one auto-generated line, no prose) per the plan; enrichment only happens on-demand once a dossier is promoted through [[30_Order/Workflows/Internship Pipeline]], and that promotion path itself is outside this automation's scope.
- **Layer 6 Resume Grader** — a keyword-overlap scorer for tailoring `Resumes/Main Resume.md` against a JD, explicitly deferred in the plan as a separate local tool, not started.
- **Cadence still hourly**, not tightened to the sources' actual ~30-minute update rate — deliberate, per the plan's build order: watch a full week of clean runs before trusting a tighter schedule.
## Open Questions
- [ ] Confirm the first real Sunday 23:00 UTC weekly rollup actually appends correctly into `10_Areas/Career/Internships/List/Run Log.md` — first opportunity is 2026-07-19
- [ ] Once a week of clean hourly runs has passed, decide whether to tighten cadence toward the sources' real ~30-minute update rate
- [ ] Revisit `locations_allow` now that real `locations` data exists in dossiers written by actual live runs
- [ ] Watch for whether the vault's own ~2-hour auto-commit cycle and this hourly cron ever actually collide on `origin/master` — the retry-once logic is tested against synthetic conflicts but hasn't yet hit a real one
## Vault Cleanup And Root-Cause Findings (2026-07-18)
Folder audit found 110 of 137 dossiers didn't belong — cross-referenced every stored ID against the live upstream JSON feeds (no webpage visits needed) rather than trusting local frontmatter. Deleted, not archived: 79 SimplifyJobs (76 marked `active: false` upstream, 3 grad-only with no Bachelor's eligibility), 11 of 13 JGCL (7 closed upstream, 4 wrong-cycle by their own filename), all 20 zapplyjobs (none are actual deadline-bearing postings — program/resource landing pages, structurally the wrong fit for this folder). 27 remain, all verified Summer 2027, active, Bachelor's-eligible.
Root causes, not yet fixed in code — will recur without a pipeline change:
1. No recheck after a dossier is written — a posting closing upstream is never noticed.
2. `degrees` eligibility was never checked (same class of gap as the earlier `locations_allow` miss).
3. ~~JGCL's real `target_year` data never reaches the written dossier frontmatter~~ — **wrong, corrected 2026-07-18.** Checked git history directly: `target_year` was genuinely populated at the one and only commit for these files. The claim was an artifact of an anchored grep (`^target_year:`) that captured a multi-line YAML list's key but not its indented values below. The real bug: JGCL's `season` field is never mapped, so `terms:` is always empty on every JGCL dossier (confirmed real, this part held up) and no cycle/term check runs for this source at all — that's what let the 4 wrong-cycle dossiers through.
4. No cross-source dedup — the same program can land as separate files from two sources (MLH Fellowship appeared via both zapplyjobs and JGCL).
5. zapplyjobs should stop feeding this pipeline entirely per this session's decision.
## Phase 4 Scope Decision (2026-07-17)
Reversed the plan's original "on-demand only" boundary for what counts as "finishing" this project — Layer 5 (company/contact enrichment) and Layer 6 (resume grader), previously scoped as separate future tools outside the automation, are now in scope to actually build. Trigger semantics are not reversed: Layer 5 stays promotion-triggered (a script run explicitly when a dossier is promoted through [[30_Order/Workflows/Internship Pipeline]]), not automatic on every dossier — this wasn't re-confirmed explicitly when the scope decision was made, flagged for the build prompt to state plainly rather than assume silently. PRD.md's own NEEDS WORK sections (Success Metrics, Risks) are explicitly a separate prompt, not folded into this one.
## Phase 4 — Locations Filter, Enrichment, Resume Grader (2026-07-18)
Built and verified 2026-07-18; everything below is from an evidence pass (fresh test runs, live dry-runs, real transcripts), not a build summary. ==Closes three of the five "What's Not Built" gaps: `locations_allow`, Layer 5 (built, not yet run live), Layer 6. The rollup and cadence gaps are time-gated, unchanged, with check dates below.== Test suite: **131/131 passing** (was 87 — +36 locations tests on verbatim live strings, +5 enrich, +3 grader). Shipped as commit `697c110` on master, pushed through `commit_and_push_with_retry()` — which did real work on the way out: rebased over `c31c51c`, that morning's automation commit, the exact two-writer race it was built for. CI (`test.yml`) green on the pushed commit.
### `locations_allow` — built from live data, live on the loop
Fetched both live `listings.json` feeds (14,900 + 112 entries, **1,216 distinct location strings**; zapplyjobs carries no location data at all) before writing any rule. `location_eligible()` in `core/filter.py`, enabled by `locations_allow: us_remote` in `profile.yaml`: a US signal always wins (state-code suffix tolerant of real dirt like `Carlsbad, Ca` / `Dallas. TX`; full state names checked *before* the foreign denylist so `New Mexico` survives its `mexico` token), an affirmative foreign token loses (`canada|can|uk|germany|india|…`, word-bounded), and everything ambiguous **passes** — `Multiple Locations`, `Virtual`, bare `Remote`, no data at all. Permissive by design: the denylist can't name every country, but a US signal is never falsely rejected.
*Dry-run against all 137 real dossiers:* 20 have no locations data (pass as unrestricted); **exactly 13 would reject**, every one via an explicit `canada`/`uk` denylist token (Kroll, CIBC, DRW, RTX — Toronto/Montreal/Mississauga; 3× Motorola — Ontario/Remote in Canada; Confluent + Crowdstrike — Remote in UK; Voleon, Marshall Wace, IMC — London; Scottish Water — Edinburgh/Glasgow), zero rejected for merely lacking a US signal.
*Decision on record:* the 13 existing non-US dossiers are **permanently grandfathered** — the filter is Layer 2, prospective only; nothing in the automation re-evaluates, edits, or deletes an existing dossier, and their uids stay in `seen_ids.json` so they can't be rewritten. They sit at `status: unreviewed` for manual archiving or ignoring.
### Layer 5 — `enrich.py`: built and unit-tested, **never run live**
Manual CLI run at Step 2 (Commit) of [[30_Order/Workflows/Internship Pipeline]] — deliberately **not** called from `run_pipeline.py`, never automatic on discovery-loop writes (the trigger design the scope decision flagged for explicit statement — stated, confirmed, built that way). Firecrawl scrape of company site/engineering blog (verbatim trimmed text, zero LLM calls), contacts from public sources only — GitHub org public members, blog author bylines, pattern-inferred `first.last@domain` validated against MX records via DNS-over-HTTPS (no new dependency; this machine has no `dig`). Appends a replaceable `## Enrichment` section to the dossier (re-runs replace, never duplicate). Hard line honored: no LinkedIn, no CAPTCHA bypass, no cookie injection, no stealth browser, no login walls.
> [!WARNING]
> No `FIRECRAWL_API_KEY` exists anywhere in this environment (env, shell configs, repo secrets all checked) — the full path has **never executed end-to-end** and is not claimed as done. The script fails fast with a clear message until a key is exported. The keyless halves *were* verified live 2026-07-18: GitHub org discovery resolved Confluent → `confluentinc` with 5 real public members, `mx_ok('confluent.io')` → True, garbage domain → False, inference produced `ansh.jain@confluent.io`.
### Layer 6 — `grade_resume.py`: built, tested, run against a real JD
Keyword-overlap scorer over Main Resume.md's `#skill/*`-tagged bullets — local, zero network, zero LLM, per the near-zero-cost design. Real transcript 2026-07-18: fetched the actual Anthropic Fellows Program JD (2,594 words, via the Greenhouse API, from a real dossier's URL) and graded the real bullet bank — top bullet scored 5 (the BOOM APIs/data-ingestion bullet), tag emphasis ranked `#skill/ai` 17 > `#skill/infra` 12 > `#skill/soft` 8, matching the JD's actual emphasis. Known ceiling, deliberate: naive token overlap counts generic words (`via`, `other`) as matches — the stopword list in `grade_resume.py` is the knob if it starts annoying.
### Verified state after phase 4
- Ingestion, filter (now including locations), dedup, write-gate: **built, tested, live** — hourly runs still green through 2026-07-18 (`a38aefc`, `5deddd4`)
- Layer 5: built, unit-tested, **soft** — blocked on a Firecrawl key for its first real run
- Layer 6: built, tested, verified against a real JD — local tool, "live" doesn't apply
- Weekly rollup: **time-gated, not a gap** — first fires Sun 2026-07-19 23:00 UTC; check `Run Log.md` on Mon 2026-07-20
- Cadence tightening: **time-gated, not a gap** — evaluable on/after 2026-07-24 (one week of clean runs since 2026-07-17 11:21 UTC)
## Phase 5 — Bloat Root-Cause Fixes (2026-07-18)
All five root causes from the vault audit shipped as commit `7a84be1` (pushed via `commit_and_push_with_retry()`, again rebasing over that day's automation commit). **148/148 tests passing** (was 131: −8 zapply, +25 new). Every rule below was built against freshly-fetched live feed data, not the audit's numbers re-quoted.
1. **Post-write liveness recheck** — `recheck.py` + `.github/workflows/recheck.yml` (daily 06:30 UTC cron + workflow_dispatch, deliberately separate from hourly discovery). Scans the dossier **files actually in the checkout** (not seen_ids.json — the two diverged permanently at the cleanup), cross-refs each uid against its source's live feed, removes on `active: false` or absent-from-feed, logs to `logs/rechecks.jsonl`, never touches seen_ids. A failed source fetch skips that source's dossiers entirely (never read as "everything absent"), and a mass-deletion brake (> max(5, half the vault)) halts and files an issue instead of deleting. *Verified live via dry-run against the real vault: 28 dossiers scanned, 2 would be removed, both `active: false` upstream — postings that closed after the morning audit.* **Discovery side too:** `matches()` now rejects `active: false` at write time — 71 of 103 then-passing SimplifyJobs listings were already closed upstream (their ATS URLs still return 200, so `url_liveness` can't catch this).
2. **`degrees` gate** — `degrees_allow: ["Bachelor's"]` in profile.yaml, permissive on empty (4,676 of 14,907 live entries carry no degrees data). Real apostrophe-form values confirmed by fetch; regression fixture is the real TikTok PhD-only Research Scientist entry, which passes every other check.
3. **JGCL `season` mapped** (the audit's original target_year claim was corrected in the findings section above — a grep artifact). `normalize_josegael` now maps `season` → `Listing.terms`; wrong cycles reject (exclude_terms hits like "Summer 2026", year-less Spring/Fall/Winter), year-less "Summer"/"Multiple"/"Year-Round" pass permissively. Regression tests use the real Partiful (Spring) and WomenTech ("Summer 2026") entries verbatim, calling `_matches_josegael` directly since every wrong-season live entry is also `active: false` (the active gate would mask the season rule).
4. **Cross-source dedup** — fifth write-gate check `cross_source_duplicate` on normalized company+title (`cross_source_key()` in core/identity.py), keyed off the dossier files actually present plus same-run writes; first source in write order wins (SimplifyJobs → JGCL). Runs before `url_liveness` — it's free, the HEAD request isn't.
5. **zapplyjobs removed entirely** — fetcher, README parser, `_matches_zapply`, dispatch branch, uid content-hash fallback (both remaining sources guarantee upstream ids; `compute_uid` now raises on a missing one), schema check, fixture, and 8 tests all deleted, not bypassed.
Also: the schema-drift check now guards `active`/`degrees`/`season` — renamed upstream, those fields would silently turn their filters permissive rather than crash, exactly the drift class the check exists for.
*Net filter effect against the live feeds at ship time: SimplifyJobs 14,907 fetched → 29 match (was 103 before the active+degrees gates); JGCL 112 → 5 (was 17). Survivors are all active, Bachelor's-eligible, US/Remote, right-cycle.*
> [!WARNING]
> First scheduled recheck timing: the vault's local working copy holds the audit's 110 deletions **uncommitted**. Until the vault's own auto-commit cycle pushes them, origin still has all 137 dossiers — a recheck run against that state would want to remove ~90 and the mass-deletion brake would halt it (harmless but noisy: one GitHub issue). Let the vault push first; the daily 06:30 UTC cron takes it from there.

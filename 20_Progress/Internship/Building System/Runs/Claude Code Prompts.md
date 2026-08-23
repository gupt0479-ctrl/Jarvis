---
type: project
status: active
created: 2026-07-26
updated: 2026-08-24
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]"
tags:
  - internship
  - automation
  - prompts
next: "Prompt 14 was refined in place before ever being run — the human brought two real InternDock URLs plus a request to review actual per-source yield, and both changed the prompt materially. Prompt 15 (Jarvis) is unchanged, still not yet run, still correctly scoped to not describe Prompt 14's sources as shipped."
---
# Claude Code Prompts — Internship Research Loop
This file holds the next prompt(s) to run, and only that — it gets wiped and rewritten every build cycle, not accumulated. When a prompt finishes and its result is reviewed, its full text and result move into [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]] and get deleted from here.

## Prompting Guide In Use
[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) — re-apply on every prompt.
- Front-load everything, literal scope, explicit Task Order/Files Touched, `high` effort, generous `max_tokens`.
- Hand over verified facts, instruct re-checking them.
- **A prompt can be worth refining before it's even run.** Prompt 14 (below) was rewritten in place after real new information arrived — two actual InternDock URLs and a request to check real per-source yield, not more planning-doc reading. Don't treat "the prompt is already written" as a reason to ship a now-outdated version; the file's whole design (wipe and rewrite, no accumulation) exists exactly to make this cheap to do.
- **A search-engine summary is a lead, not a fact.** This round surfaced a claim (via web search) that `zshah101`'s repo offers "a live dashboard, RSS feed, and JSON API" beyond the file already integrated — plausible, uncited, not something to act on without checking the real repo directly. Same discipline as every other claim in this project: verify against the primary source before building on it.
- **A personal/tracking token in a URL is not the same as an access requirement.** The two InternDock URLs the human provided carried an `mcp_token` and (on one) an `fbclid` — checked directly: the page loads identically without either. Don't assume a link needs its query params just because they're there; check, and never let a personal, expiring, user-specific token find its way into an automated pipeline's config even if it happens to work today.

---

# Codebase
## Prompt 14 (v2 — refined 2026-08-24 before first run): New Discovery Sources
**Fresh session**, `gupta-builds/internship-research-loop`. Read `CLAUDE.md` first. As of 2026-08-24: 372 tests passing, latest commits `3b99251`/`23e52db`/`288b390` — verify `HEAD` matches `origin/master` before starting.

**This is explicitly the harder of two options the human was offered — "each new source is effectively a mini version of the original Phase 1-3 build: real schema-drift handling, real fixture-based tests, real filter/dedup integration, not a quick add." Hold every new source to exactly that bar, including the ones below that weren't in the first draft of this prompt. The zero-scraping-charade, real-data-only discipline in `CLAUDE.md` applies in full — a source with no accessible structured data is not a source, however useful its content looks, matching this project's own precedent (zapplyjobs removed for exactly this reason). This round adds a second discipline worth naming explicitly: a source that's real and accessible but only produces a one-time snapshot is not automatically "constantly finding new internships" just because it's real — check whether it can actually be re-checked for new content before treating it as an ongoing source.**

**Part of this prompt is now "investigate why an existing source underperforms," not just "add new ones" — real yield data (below) raised questions nobody had looked at yet. Do this work with the same rigor as adding something new; a source silently producing nothing is exactly the kind of finding this project's history (Task 7's audit, the Zipline leak) has repeatedly shown is worth chasing down rather than assuming is fine.**

**Pre-verified findings, re-check every one before building on it:**
- **Real yield, last 20 runs (`logs/runs.jsonl`), fetched → matched:** SimplifyJobs 290,240 → 4,477 (1.5%); Jose-Gael-Cruz-Lopez 2,240 → 76 (3.4%); vanshb03 9,351 → 2,490 (26.6%); zshah101 9,858 → 1,197 (12.1%); Greenhouse 1,120 → 600 (53.6%, expected — pre-curated per-company boards); Ashby 80 → 16 (20%, but only 4 matched/run — tiny absolute volume); Freehire 140 → 40 (28.6%, only 2/run); AIJobs 4,763 → 1,220 (25.6%).
- **Real current live-dossier count by source** (vault, today): SimplifyJobs 138, vanshb03 77, zshah101 68, Greenhouse 16, AIJobs 11, manual 4, Freehire 2, **Jose-Gael-Cruz-Lopez 0**. JGCL matched 76 real candidates over the last 20 runs and contributed zero live dossiers — this is new, not the same "feed is just quiet" finding from two prior audits (which only checked whether JGCL was *fetching*, not what happened to what it *matched*). The likely cause: `SOURCES` tuple order in `run_pipeline.py` determines which source wins a cross-source-duplicate tie, and if JGCL sits after SimplifyJobs/vanshb03/zshah101 in that tuple, every genuine duplicate it finds loses automatically to whichever of those three already wrote it first. That's a real, checkable hypothesis — Task 1 below is to actually check it, not assume it.
- **InternDock** (two real pages the human provided, both independently fetched and confirmed this session): `interndock.com/tracker/guides/summer-2027-internship-drop-august-2026` and `.../fresh-internship-drop-summer-2027-fall-2026`. Confirmed: static HTML, no API/JSON/GraphQL endpoint anywhere in the page. ~650-658 real postings per page, consistently structured (`- [Title](URL) *Company, Location*`), grouped by category (Software Engineering, Marketing/Sales, Supply Chain/Operations, Banking/Finance, Quant/Trading, Accounting/Audit/Tax). **Confirmed loads identically with no query parameters at all** — the `mcp_token`/`fbclid` in the URLs the human pasted are personal referral/tracking params, not authentication; do not use them, hardcode them, or store them anywhere in this pipeline. The page's own text describes itself as "a fresh sweep... that were live on August 8, 2026" — **this is an explicit point-in-time snapshot, not a live feed**. Two different dated URLs existing (an "August 2026" drop and a separate "Summer 2027/Fall 2026" drop) suggests InternDock publishes these periodically, which matters for Task 3 below.
- **Unverified, check before acting**: a web search surfaced a claim that `zshah101`'s repo offers "a live dashboard, RSS feed, and JSON API" beyond the `data/jobs.json` file this pipeline already reads — this is search-summary text, not a checked fact. Verify directly against the real repo (README, repo file listing) before treating it as true.
- `api.lever.co/v0/postings/<company>?mode=json` is a real, live, public JSON API — confirmed against `palantir`. `boards-api.greenhouse.io/v1/boards/linkedin/jobs` is live, 53 real jobs, but a title-only scan found zero literally "intern"-titled roles (not the same as zero relevance — LinkedIn's early-talent program is named "First Play"). Naive single-word token guesses for Two Sigma/Citadel/MLH/Capital One/Bloomberg/Microsoft/NASA on Greenhouse and Ashby mostly 404'd — not evidence no real token exists, evidence blind guessing is the wrong method (use the company's real careers page or a real dossier URL instead, per `sources.py`'s own comment above `GREENHOUSE_COMPANIES`).
- `core/schema_drift.py`'s `check_all()` deliberately excludes per-company sources (Greenhouse, Ashby) — a new Lever module follows that same per-company pattern (`fetch_greenhouse`/`normalize_greenhouse`'s shape), not the single-feed pattern.

### Task 1 — Resolve the JGCL zero-yield question
Check `run_pipeline.py`'s `SOURCES` tuple order. If JGCL sits after SimplifyJobs/vanshb03/zshah101, sample several of its recent real matches (from `logs/runs.jsonl`'s `filter_match_counts`/rejection records) and confirm directly whether they're genuine duplicates of postings those earlier sources already caught (expected, correct behavior — JGCL is redundant coverage, not broken) or genuinely unique postings being wrongly crowded out by tie-break order alone (a real bug, worth fixing — e.g. by not needlessly favoring earlier `SOURCES` order for a source that specifically targets underclassmen and rarely overlaps by design). **Do not reorder `SOURCES` without first confirming which case this is** — it's a shared tie-break used by every other source too, and a blind reorder could shift outcomes well beyond JGCL.

### Task 2 — Ashby and Freehire: why so little makes it to the vault
Ashby: only ~4 matches/run from a 9-company curated seed list — is this genuinely just a small, low-turnover set of boards, or is something dropping real matches downstream? Freehire: indexes 4.27M postings but surfaces only ~2/run — check whether `lookup_company_on_freehire()` is only being queried for a narrow company set (in which case: is that deliberate, and should it be widened?) or whether it's broadly querying and most results are getting deduped/rejected downstream (in which case: which check, and is it correct?). Report real numbers either way — this task is diagnostic; only change code if you find an actual bug, not a "could theoretically be broader" wish.

### Task 3 — InternDock: build it only if it can be an ongoing source, not a one-time import
Check whether a guides index/archive page exists (try `interndock.com/tracker/guides/` or similar, and check the site's own navigation) that lists every published "drop" post — that's the actual precondition for treating this as a real discovery source rather than a single snapshot import. **If a real, checkable index exists**: build a Firecrawl-based periodic fetch of that index (zero-LLM, same fetch technique already used for individual posting-page content elsewhere in this pipeline) to detect new drop posts, plus a regex parser for the confirmed `- [Title](URL) *Company, Location*` structure — with real fixture tests built from the actual content of both drop pages already fetched this session (don't re-fetch for the fixtures, the real content is already captured in this conversation's history if you don't have live access; re-fetch only to confirm it's still current). **If no index exists** (each drop's URL has to be found manually, e.g. shared via social media with no predictable pattern) — say so plainly and do not build a "guess the next URL" mechanism; that would produce exactly the kind of silent, unverifiable behavior this codebase's own discipline exists to prevent. In that case, a one-time import of the ~650-658 postings from the two pages already fetched may still be worth doing as a manual, one-off enrichment — flag this as a separate, smaller option rather than folding it into the "new source" decision.

### Task 4 — Verify the zshah101 RSS/API claim
Check the real repo directly. If a genuinely richer feed than `data/jobs.json` exists, evaluate whether it's worth switching to or supplementing the current integration. If the claim doesn't hold up against the actual repo, say so and move on — don't build against search-summary text.

### Task 5 — Lever: find a real second company, then build it
Unchanged from the original plan. Resources.md's own stated condition for revisiting Lever was a second real Lever-hosted target company beyond Palantir. Find one — check real dossier URLs already in the vault for a `jobs.lever.co/<company>` pattern first, then confirm live via the API pattern above. Build `fetch_lever()`/`normalize_lever()` mirroring `fetch_greenhouse`/`normalize_greenhouse`'s per-company structure, wire into `SOURCES`/`FEEDS`, fixture tests from both confirmed companies' real data.

### Task 6 — LinkedIn Greenhouse board + the other 7 named-priority companies
Unchanged. Investigate the LinkedIn board properly (department/team names, whether "First Play" surfaces anywhere) before adding the token — don't add it just because the URL resolves. For Two Sigma, Citadel, MLH, NASA, Capital One, Bloomberg, Microsoft: use the real method (company careers page, or a matching ATS domain pattern in existing dossier URLs), not more guessing.

### Task 7 — Re-verify speedyapply and sndsh404 fresh, and a wider repo sweep
Unchanged. Both were characterized 2026-07-26 as structurally blocked (private Supabase backend; README + binary `.xlsx` only) — re-check, only build if something genuinely changed. Separately, sweep for new community-maintained listing repos in the SimplifyJobs/vanshb03/zshah101 shape that may have appeared since — verify a real accessible data file before considering one further.

### Discipline
Separate commits per source/finding, real citations, fixture-based tests, full suite green at every step. The local pre-push hook will block a broken commit.

### Report back
Per task: what was found, what was built (real verified counts, not estimates), what was checked and came back empty — name it, don't omit a dead end silently. Task 1/2 are diagnostic — report the real numbers and your conclusion even if the answer is "working as intended, no bug." Task 3's index-page finding determines whether InternDock becomes a real ongoing source or a one-time manual import — state which, clearly, before describing any code built around it.

---

# Jarvis
## Prompt 15: Refresh Both Resources Docs, Close The Removed Dossiers MOC Gap
**Run inside the Jarvis vault directly** (Windows, Sonnet 5, high effort). Vault-note work only. **Prompt 14 (now v2) is running in parallel in a different session — don't describe any specific new source as shipped; if you reference the source-expansion effort at all, say "in progress as of 2026-08-24, see this file's Prompt 14 entry," not a finished state.**

### Task 1 — Refresh `10_Areas/Career/Internships/List/Resources.md`
Stale since 2026-07-26 despite its own instruction to update "whenever a source is checked for exhaustion" and its own callout that a number unrefreshed for two weeks should be treated as stale. Real current per-source numbers (fetched/matched over recent runs, and current live-dossier counts) are already available — pull from `logs/runs.jsonl` via the repo, or ask for them if this session lacks direct repo access: SimplifyJobs 138 live dossiers (1.5% match rate on 290K+ fetched), vanshb03 77 (26.6%), zshah101 68 (12.1%), Greenhouse 16 (53.6%, small pre-curated set), AIJobs 11 (25.6%), Freehire 2 (28.6% but tiny absolute volume — worth noting as a real open question, see Prompt 14's Task 2), Jose-Gael-Cruz-Lopez 0 despite 76 real matches over the last 20 runs (also an open question, Prompt 14's Task 1 — note it as under investigation, not resolved either way yet). Update the table with these real, dated figures.

### Task 2 — Refresh the Named-Program Coverage Check in `Research Loop - Resources.md`
Unchanged from before — still a month stale, real numbers have moved (Jane Street 11, Microsoft 6 as of the last real check). Re-check current real dossier coverage per named company and update.

### Task 3 — Build `Viewed/Removed Dossiers MOC.md` for real
Unchanged — still empty, still required by `Internship Notes Standard.md` §1/§4, still dozens of real dossiers pointing at it.

### Explicitly out of scope
No code changes to `internship-research-loop`. No describing Prompt 14's in-progress source work (including InternDock, Lever, or anything else still being investigated) as finished. No unilateral decisions on anything ambiguous.

### Report back
Task 1/2: what changed, with real numbers cited. Task 3: confirmation the MOC is real and populated.

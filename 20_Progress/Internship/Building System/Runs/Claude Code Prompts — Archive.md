---
type: reference
status: tree
created: 2026-08-22
updated: 2026-08-27
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts]]"
tags:
  - internship
  - automation
  - prompts
  - archive
next: null
---
# Claude Code Prompts — Archive
Every prompt ever run against `gupta-builds/internship-research-loop`, in order, verbatim, with what actually happened when it ran. [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]] is the live counterpart — it holds only the guide plus whatever prompt runs next, and gets overwritten every build cycle; this note is where that content lands once a prompt is done, so nothing is lost. Read [[System - Build Log]] for the narrative/decision history around these; read this note for the prompts' exact text and exact results.

## Prompts 1-3 — Done, Confirmed Live (2026-07-26)
Persona/timing config, CS-relevance gate + priority classification, and the promote-dossier skill/agents all shipped and verified live via direct `gh api` checks the same day. Full detail in [[System - Build Log]] (this summary is all that ever lived in the prompts file for these three — never expanded here).

## Prompting Guide In Use (as of Prompts 4-5)
[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5). Effort: `xhigh`. Front-load everything; each prompt assumes no memory of the conversation that wrote it. Two points applied specifically from Prompt 4 onward: literal instruction-following (an explicit Task Order + Files Touched table so nothing has to be inferred), and generous `max_tokens` headroom at `xhigh` effort so a long task doesn't truncate mid-response.

## Prompt 4 — Revised 2026-07-29, Run 2026-07-30, Reviewed In Detail 2026-07-30
**Executed for real** — 303/303 tests pass (258 baseline + 45 new). Independently re-verified 2026-07-30 by reading every diff directly and executing the trickiest pieces by hand: Tasks A, B, C, E, F, G, I confirmed genuinely correct. **Two real, reproducible gaps found in Tasks D and H** (Fix 1 / Fix 2 below, folded into Prompt 5's own "Fix First" section rather than re-run separately). Nothing was committed at the time this note originally described (later resolved — see Prompt 6 below, which finally committed both Prompt 4 and Prompt 5's work together on 2026-08-21).

```
You are working in gupta-builds/internship-research-loop. Context: Prompts 1-3 already shipped (core/relevance.py, core/classify.py, the priority-folder routing in vault_writer/writer.py, the /promote-dossier skill) — all confirmed live on master. This prompt was originally written 2026-07-26 and never executed (confirmed via git log — zero commits against it). A follow-up live audit on 2026-07-29 found the same bug classes recurring on new real postings plus one new bug class, and the user specified additional vault-side requirements. Read `30_Order/Standards/Internship Notes Standard.md` in the Jarvis vault before starting — it's the real, concrete contract for dossier notes (frontmatter, body structure, interlinking, removal handling, resource limits) that this whole prompt implements; it did not exist (empty file) until this revision. This prompt covers nine tasks — five real, evidence-based bugs (A-E, A also carries a design revision) plus four new requirements (F-I). Fixture files/real examples are named throughout; use the real content, don't write synthetic test data.

Before starting, confirm the assumed-live pieces actually exist — `core/relevance.py` (`stage1_reject`/`stage2_confirm`), `core/classify.py` (`classify`/`BUCKET_FOLDERS`), and the priority-folder routing in `vault_writer/writer.py`. If any of them are missing, stop and report that rather than building Tasks B/C/F/G/I on top of a false assumption — this exact failure mode (building on an unverified "already shipped" claim) is why Prompt 4 sat unexecuted for three days; don't repeat it in the other direction by assuming Prompts 1-3 landed exactly as described without a fresh check.

### Task Order
No task strictly blocks another except two real dependencies — respect these, the rest can run in any order:
1. G before H. Task H's move-to-Viewed/ logic appends to the notes: frontmatter field that Task G creates. Building H first means building it against a field that doesn't exist yet.
2. E before I. Task E fixes what gets fetched from Google's careers site (currently the wrong page); Task I improves how fetched content gets formatted. Doing I first means polishing the formatting of content Task E is about to replace anyway.
Suggested full order: B, C, D, F (independent gate/dedup fixes — any order among these four) → E → I → G → H → A (fully independent of everything else, do it whenever convenient). This is a suggestion for a sane single pass, not a hard requirement beyond the two dependencies above.

### Files Touched, By Task
| File | Tasks |
| --- | --- |
| run_pipeline.py | A |
| core/relevance.py | B, C |
| core/classify.py | C |
| core/identity.py | D |
| vault_writer/validate.py | D (tie-break reference only, no edit), G (add notes to REQUIRED_FRONTMATTER_FIELDS) |
| ingestion/posting_page.py | E, F, I |
| vault_writer/writer.py | G, H (build_frontmatter, load_dossier_uids/save_dossier_uids) |
| recheck.py | H |
core/relevance.py (B, C) and ingestion/posting_page.py (E, F, I) each get touched by multiple tasks — read the file fresh before each task on it rather than working from a stale in-memory copy of what an earlier task in this same session already changed.

## Task A — Dossier count-limit, as a NOTIFICATION not a hard write-refusal (revised 2026-07-29)
Currently run_pipeline.py:66 has MAX_NEW_WRITES_PER_RUN = 18 with no per-bucket split and no ceiling on total accumulated dossiers — still true, checked directly 2026-07-29. Live counts right now, checked 2026-07-29: 1 - AI & ML 53, 2 - Fullstack 21, 3 - CyS & Finance 54, Other 11 — two buckets are already past the original 50 design number, so this is not theoretical anymore. Original design (Dossiers-to-Create.md, Source of Truth.md) said "refuse to write into a bucket already at 50" — the user explicitly overrode that framing: this is a notification mechanism, not a silent gate that drops a real eligible posting the way an exclusion rule does (that asymmetry — a false exclusion loses an opportunity for nothing, a false inclusion costs one screening read — is this codebase's founding design principle everywhere else; a hard-refusal cap violates it for no reason, since the actual scarce resource is human review attention, not vault storage). Implement:
1. A per-bucket count check before writing (still count real files in the vault checkout per bucket, same mechanism originally planned) — but do not refuse the write when a bucket is at/over 50. Keep writing; a full bucket is a signal to review more urgently, not a reason to lose a real posting.
2. A per-run write budget, still capped at roughly 10 total but split by bucket: something like 3 AI/ML, 3 Fullstack, 3 CyS & Finance, 1 Other — implement as a tunable dict, not hardcoded magic numbers spread through the function; this pacing exists to protect Firecrawl budget and review throughput, independent of the notification question above.
3. Run-record field: when a bucket's post-write count is >= 50, the run record carries an explicit bucket_at_capacity list naming which bucket(s). File a GitHub issue the first time a given bucket crosses 50 (track "already notified" per bucket in state/ so it doesn't refile every run — reuse the existing file_github_issue pattern, don't build a second notification path) and again if the global total (excluding Viewed/) crosses 190 or 200 (150/170 stay informational-only in the run log). Since 1 - AI & ML and 3 - CyS & Finance are already over 50 as of this writing, the very first run after this ships should file both bucket-crossing issues immediately if the "already notified" state starts empty — expected, not a bug.
4. Do not touch 10_Areas/Career/Internships/List/Dossiers MOC.md in the vault — a live dataviewjs capacity table was already added there directly 2026-07-29 (reads real folder counts at render time, no code needs to maintain it). Task A only needs the codebase-side run-log/issue half described above.
5. Keep the existing most-recently-posted-first prioritization within each bucket's per-run allocation — don't replace that logic, just scope it per-bucket instead of globally.
Tests: fixture-based, covering a bucket at exactly 49/50/51 (assert the write still happens at 50/51, only the notification fires), the global total at 189/190/200/201, the per-bucket run-budget split respecting bucket boundaries (a bucket with 0 eligible candidates this run shouldn't consume another bucket's slots), and the "notify once per bucket" state actually suppressing a second issue on a subsequent run where the bucket is still >= 50.

## Task B — CS-relevance gate: Product/rotational/business-analyst roles slip through (real bug, recurring)
core/relevance.py's _STAGE1_REJECT_RE has no pattern for product/program management OR business-rotational-program roles — confirmed as a recurring bug class, not a one-off:
- Databricks "Product Management Intern (Summer 2027)" (AIJobs source, found 2026-07-26) — the actual role is explicitly PM work despite listing "computer science" as an acceptable major. Passed both stages, classified AI/ML purely because "Machine Learning" appears in a list of Databricks' internal team names, not because the role does ML work.
- Conagra Brands "Demand Science Rotational Analyst" (SimplifyJobs, found 2026-07-27, still live in the vault at the time) — a 2-year business rotational program with zero programming/software content anywhere in the real posting text. Passed both stages and landed in Other purely because it cleared the CS-relevance gate on no real signal at all.
Add patterns to _STAGE1_REJECT_RE catching: "product management intern," "product manager intern," "program management intern," "technical program manager intern," and separately "rotational (analyst|program)," "demand (planning|science) (analyst|rotational)," "business analyst intern" — verify against both real fixtures that genuine engineering roles which happen to mention "product" or "rotational" in passing still pass — check this distinction explicitly in a test, don't just add blunt keywords.

## Task C — CS-relevance gate: "threat" is too broad a keyword (real bug)
Mosaic (The Mosaic Company) "Operations & Automation Engineering Co-op/Intern" — a chemical-plant industrial-automation role — matched on the word "threat" appearing in a workplace-safety disclaimer, nothing to do with cybersecurity. Two real fixes needed: (1) this listing should fail stage 1 or stage 2 of the relevance gate outright (verify against the real fixture: no Python/Java/C++/git/algorithm mentions anywhere); (2) separately, _CYS_FINANCE_RE's bare threat pattern is too permissive regardless — require it to co-occur with a real security-context word (e.g. threat.{0,30}(model|actor|intelligence|detection)) rather than matching the bare word anywhere in scraped content.

## Task D — Cross-source dedup misses company-name AND title-string variants (real bug, recurring — four confirmed pairs now)
cross_source_key() (core/identity.py) keys on normalized company+title, which breaks whenever either string varies across sources for the same real posting. Four real duplicate incidents: Aquatic vs Aquatic Capital Management (company-name variant), Google BS/MS track same job ID via two sources (title-string variant), Virtu Financial triple duplicate (same Greenhouse job ID, three different title strings), Palantir "Intel" role duplicated across two different buckets (same Lever job ID via two sources, classified two different ways). Fix: prefer matching on a normalized ATS-derived identity — extract the Greenhouse/Ashby/Lever/Workday job ID or numeric ID embedded in the URL, when present, as a stronger identity signal than company+title text, falling back to the existing normalized-company+title key only when no such ID can be extracted.

## Task E — Google's own careers site: content-extraction bug (real, distinct from the earlier Ashby one)
Both Google dossiers sourced via Freehire contain a scraped Google Careers search-results listing page instead of the specific posting's own detail content — classify() fired on an unrelated listed job's title. Fix the extraction; add a regression fixture from the real content captured in this session's audit.

## Task F — Degree-requirement content check (new bug class, 2026-07-29)
Optiver "Quantitative Research Intern, PhD" (Greenhouse) resurfaced after a prior manual deletion. Add a content-level check, same shape and same permissive-by-default posture as the existing opt_exclusion() check: reject only on an explicit "PhD required," "PhD only," "doctoral candidates only," or equivalent phrasing — never on "PhD preferred," never on a degree merely appearing in a list of several acceptable ones. Do not build a feedback-loop-from-past-rejections mechanism for this now — Research Loop - Improvement Plan.md's Priority 4 already covers that gap and is deliberately gated on real rejection data existing first.

## Task G — Dossier interlinking (new, per 30_Order/Standards/Internship Notes Standard.md §1)
Add a notes: list field (YAML list of wikilink strings) to every dossier's frontmatter, always containing "[[10_Areas/Career/Internships/List/Dossiers MOC]]" — insert immediately after next and before tags. Add a company/<slug> tag to the existing tags: list. Update vault_writer/validate.py's REQUIRED_FRONTMATTER_FIELDS to include notes (fail-closed enforcement).

## Task H — recheck.py: move to Viewed/, don't delete (new, per Standard §4)
Replace Path(r["path"]).unlink() with a move to .../Dossiers/Viewed/ (create if absent). On move: append the Removed Dossiers MOC link to notes:, add removed_date/removed_reason, set status: removed, update state/dossier_uids.json to the new path. Same mass-deletion brake, now scoped to move counts.

## Task I — Readable, structured dossier body content (new, per Standard §2)
Stay zero-LLM. Fix: duplicate-paragraph stripping, ATS-chrome line-splitting (labels jammed against values with no separator), preserve real section structure as ### headings where the source text already states section names, strip additional known chrome (Read More markers, repeated Follow Us/social-link lists).

## Verification
Run the full test suite, report the exact pass count. Report Tasks A-I individually, re-running the real fixture cases rather than just asserting the logic looks right.
```

## Prompt 5 — Company Niche Preference, Competitive Selection Per Push, Loss-Tracked Exclusion
Written after Prompt 4's review surfaced two real gaps (Fix 1: `extract_ats_job_id()`'s Google pattern had no domain anchor; Fix 2: `move_dossier_to_viewed()` had no filename-collision handling). Both fixes were required before Prompt 5's own work.

```
You are working in gupta-builds/internship-research-loop. Context: Prompt 4 (Tasks A-I) has been run and independently code-reviewed — 303/303 tests pass, nothing committed yet. Two real, reproducible gaps were found in that review; fix both FIRST, before any of Prompt 5's own work, and confirm the fix with a real repro before moving on.

### Fix First — Two Real Gaps From The Prompt 4 Review
Fix 1 — extract_ats_job_id()'s Google pattern has no domain anchor (core/identity.py). Unlike the Greenhouse/Lever/Ashby patterns, the Google pattern matches that path shape on ANY domain. Fix: anchor to google.com. Add a regression test using an unrelated-domain URL.
Fix 2 — move_dossier_to_viewed() has no filename-collision handling (vault_writer/writer.py). Two dossiers with the identical filename can legitimately exist in two different bucket folders; moving both into flat Viewed/ silently overwrites the first. Fix: reuse dossier_filename()'s existing (2), (3)-style suffixing. Add a regression test with a constructed collision.

### Task Order
K before L (the debate comparator in L reads the preference weights K adds). L before M (M wires the comparator into Prompt 4's per-bucket budget).

### Files Touched, By Task
| File | Task |
| --- | --- |
| core/identity.py | Fix 1 |
| vault_writer/writer.py | Fix 2 |
| core/profile.yaml | K |
| core/classify.py or a new core/niche.py | K, L |
| run_pipeline.py | L, M, N |
| Dossiers MOC.md (vault) | N (Dataview sort only) |

## Task J — Where the real preference data comes from
Do not invent a FAANG/Fortune-100/YC-backed list. Research Loop - Resources.md's "Named-Program Coverage Check (2026-07-29)" section names 11 real target companies the human already identified: Jane Street (FTTP), Two Sigma (First-Year), D.E. Shaw, Citadel (Launch), Google (ASDI), Microsoft (Explore), LinkedIn (First Play), MLH Fellowship, NASA OSTEM, Capital One, Bloomberg — only 3 of 11 had any dossier coverage at the time. Use this real list as the K seed, cite the source, treat it as a human-editable starting point.

## Task K — preferred_companies in core/profile.yaml
Add a dict field (company → tier, all "high" for now). Write company_matches_preference(company, preferred) -> tier|None in core/identity.py, normalized the same way cross_source_key()'s norm() is.

## Task L — The "debate": a deterministic pairwise comparator, replacing _prioritize_and_cap's recency-only sort
Zero-LLM, no exception. debate_compare(a, b, preferred_companies) -> int via functools.cmp_to_key(), three stages each only breaking ties left by the stage above: (1) preferred-company tier, (2) bucket fill-need (cross-bucket only), (3) recency.

## Task M — Per-push limit stays Prompt 4's existing mechanism — don't build a second one

## Task N — Loss tracking and the excluded list
Track consecutive-loss count per uid in state/debate_losses.json. At 5 losses, move to state/excluded_uids.json, skip in fetch_and_filter()/dedup_new(), and append one line to a new Excluded — Losing The Debate.md log (never a silent permanent exclusion — a human can still promote by hand).

## Task O — Niche visibility, without another folder migration
Do not restructure BUCKET_FOLDERS. Add preference_tier frontmatter field (required, like every other field). In the vault, add SORT preference_tier DESC, company ASC to Dossiers MOC.md's existing Dataview tables.

## Task P — Resource check: this feature needs none, state that plainly
Confirm zero new network calls / API usage / Firecrawl fetches.

## Verification
Run the full test suite, report the exact pass count. Report both Fix-First items with real before/after repros. Report Tasks J-P individually. Nothing should be committed without being asked first.
```

**What actually happened:** Prompt 5 was executed 2026-07-30 (same session as Prompt 4's fixes) but the resulting work was never committed or pushed — it sat as an uncommitted working-tree diff on an increasingly stale local checkout for three weeks. Discovered 2026-08-21 during a full pipeline status review: local `HEAD` was 413 commits behind `origin/master` (all 413 being automated `logs/`/`state/` commits, zero code overlap), with this complete, tested (329/329 passing) Prompt 4+5 work sitting on top uncommitted. See Prompt 6 below for how that got resolved.

## Prompt 6 — Git/CI Reconciliation (written 2026-08-21, run 2026-08-21)
Written after discovering the stranded Prompt 4+5 work above. Goal: commit it safely, in a clean dependency-ordered sequence, and confirm the CI/GitHub Actions side was actually healthy (the user suspected a "broken GitHub Action," attributed to a region change while flying).

```
You're picking up internship-research-loop (/home/anant_gupta/projects/work/internship-research-loop), a zero-LLM GitHub Actions pipeline that discovers internship postings and writes them as dossiers into an Obsidian vault (a separate repo, gupta-builds/Jarvis, reached via gh/git push, not filesystem access from here). Read CLAUDE.md in this repo first — it states the load-bearing conventions (zero-LLM in the unattended path, permissive-by-default filtering, fail-closed write-gate ordering, cite-real-data-in-comments) that this task must not violate.

Your job this session is exclusively git hygiene and CI health — a clean, well-sequenced commit history and a verified-working pipeline. Do not touch dossier content, core/profile.yaml's filter thresholds beyond what's already staged, or anything in the Jarvis vault. That work is scoped to separate follow-up sessions.

## Situation
The local checkout is 413 commits behind origin/master and also has substantial uncommitted work sitting on that stale base [file list omitted here, see the original diff]. Pre-verified facts to re-confirm before acting: git merge-base HEAD origin/master equals local HEAD (3fd4b88) — pure ancestor, fast-forward-safe; origin's 413 commits touch only logs/ and state/, zero file overlap with the uncommitted diff; pytest passes 329/329 against the full uncommitted tree as-is; the per-bucket 50/global 201 capacity design is a deliberate notification-not-refusal decision, don't change it; the 3 open GitHub issues are 429/connection-reset blips against raw.githubusercontent.com from 2026-08-17/18, self-resolved, not a region/flying-related cause (Actions runs on GitHub's cloud, not the user's device) — re-verify fresh rather than trusting this.

## Steps, in order
1. Get current: git fetch, confirm merge-base claim, git pull (clean fast-forward expected).
2. Commit the staged work as 5 separate, dependency-ordered commits, running the full test suite after staging each one and before committing — never commit a state where tests don't fully pass:
   - Commit 1 — "Dedup & relevance accuracy fixes": core/classify.py, core/relevance.py, posting_page.py's phd_only_exclusion only, identity.py's ATS-job-id/cross_source_key pieces only, validate.py's cross_source_key call-site only.
   - Commit 2 — "Posting content extraction: dedup, ATS-label splitting, chrome stripping": the rest of posting_page.py, the new Google fixture.
   - Commit 3 — "Preference-tier frontmatter + Dossiers MOC interlinking": profile.yaml, identity.py's company_matches_preference, writer.py's DOSSIERS_MOC_LINK/company_slug/dump_frontmatter/build_frontmatter pieces, validate.py's REQUIRED_FRONTMATTER_FIELDS addition.
   - Commit 4 — "Dossier resource-limit notifications + debate-based write prioritization + debate-loss exclusion": core/debate.py (new), run_pipeline.py (whole diff — genuinely interleaved, don't force a split), run_log.py. Depends on commit 3.
   - Commit 5 — "recheck.py: move closed dossiers to Viewed/, never delete": recheck.py, writer.py's move_dossier_to_viewed piece. Depends on commit 3.
   Use git add -p for the four files needing intra-file splits; if a hunk doesn't separate cleanly, fold it into the better-fit commit rather than forcing it.
3. Push, handling the race with the hourly automated commits — pull again immediately before push, retry once on rejection, never force-push.
4. Verify the shipped code works live: trigger gh workflow run run.yml, watch it, confirm the new fields (bucket_at_capacity, dossier_total, newly_excluded_count) appear correctly.
5. Close the 3 stale GitHub issues (after re-verifying they're genuinely resolved) with a comment pointing at a specific successful run since.

## Explicitly out of scope
Dossier content, filter/eligibility rules beyond what's staged, new features, rebasing/rewriting history, force-push, vault documentation updates.

## Report back
Final git log --oneline -10, confirmation push matches origin/master, the live workflow run's result, the state of the 3 issues, and anything your own re-verification found that contradicted what I told you above.
```

**Result, as reported back:**
```
Everything's done. Final summary:

Git log — 5 commits landed in dependency order, HEAD matches origin/master exactly (9703416, after one more automated logs/state commit landed post-push):
3ece859 recheck.py: move closed dossiers to Viewed/, never delete
080e8aa Dossier resource-limit notifications + debate-based write prioritization + debate-loss exclusion
c50792b Preference-tier frontmatter + Dossiers MOC interlinking
484b1ef Posting content extraction: dedup, ATS-label splitting, chrome stripping
722ca4d Dedup & relevance accuracy fixes

Live workflow run — triggered run.yml manually, succeeded in 1m; the new run record shows halted: false, errors: [], dossier_total: 393, bucket_at_capacity: ["AI/ML", "CyS & Finance", "Other"], newly_excluded_count: 0, written_count: 4 — all new fields present and working, and writes still happened despite buckets being over capacity (confirming the notify-not-refuse design held).

Issues #1–3 (stale HTTPError/ConnectionError) — closed with comments pointing at a specific successful run since.

New issues #4–8 — the newly-shipped capacity-notification code correctly fired for real (3 buckets over their 50-dossier threshold, global count crossing 190 and 200). This is the intended notification behavior firing for the first time, not a bug — left open since they're informational by design and closing/resolving the underlying condition is outside this session's scope.

Three findings that contradicted your brief, both fixed before landing:
1. vault_writer/writer.py's diff didn't need forcing into just commits 3/5 — it split cleanly along its own 4 hunks, no forcing needed.
2. tests/test_validate.py's entire diff was actually Task G/O preference_tier-required-field tests, not commit-1 material as listed — folded the whole file into commit 3 instead of forcing a split, per the fallback rule.
3. Real bug found via per-commit isolation testing: commit 1's ATS-job-id dedup change broke cross-source dedup between commits 1-3, because run_pipeline.py's own two dossier_keys-building call sites weren't updated to pass listing.url until commit 4's full diff — while vault_writer/validate.py's check (already in commit 1) expected the new signature. Caught when isolating commit 1 with git stash. Fixed by pulling just those 2 line-level changes into commit 1 (amended before push), keeping every commit boundary genuinely green — 282/288/301/326/329 passing at each step respectively.
```

**Follow-up — a sync error hit and fixed in the same session:**
```
Fixed and pushed — HEAD matches origin/master again, working tree clean, 329/329 tests passing.

Root cause: the CI side already handles this correctly — core/git_ops.py's commit_and_push_with_retry (used by both run_pipeline.py and the Jarvis vault push) does git pull --rebase + retry-once before every automated push, so the bot's own hourly commits never collide with each other. The gap was purely this local checkout: it has no pull.rebase/pull.ff strategy configured, so whenever a local commit sits unpushed across even one bot cycle (~40-60 min), a plain git pull in VS Code hits Git's "divergent branches, pick a strategy" refusal. That's exactly what happened — a graphify-out/ tracking commit (a128625, from an earlier session, not this one) sat unpushed while 16 bot commits landed on origin.

Resolved the immediate stuck state with a one-off git pull --rebase origin master (no config change) and pushed clean.

One thing I can't do myself: under a hard rule to never modify git config, even on request. To stop this recurring: git config pull.rebase true (local, not --global, so it won't touch other repos) — mirrors exactly what core/git_ops.py already does for the bot, keeps history linear.
```

**Independently re-verified 2026-08-22** (fresh session, all claims checked against live state, not trusted from the report): all 5 commits confirmed present with exact matching messages and correct order; `git log --oneline -1 HEAD` / `origin/master` both `89fd543` (one further commit landed since, from a separate graphify-integration session — see [[../../../../.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/memory/graphify-jarvis-sync|graphify-jarvis-sync memory]] for that one, unrelated to this pipeline); working tree clean; 329/329 tests pass right now; the exact claimed run record (`written_count: 4`, `dossier_total: 393`, `bucket_at_capacity: ['AI/ML', 'CyS & Finance', 'Other']`, `newly_excluded_count: 0`, `halted: False`, `errors: []`) confirmed byte-for-byte against `logs/runs.jsonl`; issues #1-3 confirmed closed, #4-8 confirmed open with matching titles/timestamps; every scheduled run since (`run.yml`, `recheck.yml`, `test.yml`) succeeded, most recent about an hour before this check. `git config pull.rebase` confirmed still unset locally — the one item genuinely left undone, correctly, since no coding agent (this session included) is permitted to touch git config. See Prompt 7 in the live prompts file for what's next.


## Prompt 7 — Git/CI Hardening + Documentation Sync (written 2026-08-22, run 2026-08-22)
Written after Prompt 6 landed the stranded Prompt 4+5 work. What was left wasn't a bug — no local safety net against a broken commit reaching `master` (no PR gate by design), and three documents still describing the pre-Prompt-6 state.

```
You are working in gupta-builds/internship-research-loop (/home/anant_gupta/projects/work/internship-research-loop). Read CLAUDE.md first. Context: single-branch, direct-to-master convention (no PR flow) — confirm via git log. As of 2026-08-22: working tree clean, HEAD matches origin/master, 329/329 tests passing, 5 commits (722ca4d through 3ece859, 2026-08-21) shipped a per-bucket dossier capacity-notification system, a "debate" write-prioritization comparator, debate-loss exclusion, and recheck-to-Viewed (never delete). Re-verify all of this yourself before proceeding.

This session is git/CI hygiene and documentation accuracy only. Do not touch dossier content, core/profile.yaml's filter/eligibility rules, or add any new pipeline feature.

Task Q — Local pre-push test gate: scripts/hooks/pre-push (pytest gate), installed to .git/hooks/pre-push, documented in README.md's Local dev section. Verify it actually blocks (break a test, confirm push refuses; fix it, confirm it proceeds).

Task R — Sync stale documentation: Source of Truth.md's next: field and Resource Limits section (still said "not yet implemented"), System - Build Log.md (add 2026-08-21/22 entries), PRD.md (Current Status/Open Backlog/Risks — add a dated manual-check note for PAT/API-key expiry since it's not API-introspectable; check GH Actions minutes usage, report what's actually accessible).

Task S — Confirm the new pre-push hook doesn't interact badly with the existing graphify post-commit/post-checkout/post-merge hooks (different hook type, but verify with a real timed commit+push, not just on paper).

Explicitly out of scope: dossier content, profile.yaml, new features, git config changes, rebasing, force-push.

Report back: Task Q's real block/pass test results, what changed in each of the three documents, what you observed running the full hook chain, anything that contradicted this brief.
```

**Result, as reported back:**
```
All verification complete. Pre-flight: single-branch convention confirmed, working tree clean, HEAD matched origin/master, 329/329 tests, all 5 commits present as described.

Task Q: scripts/hooks/pre-push tracked, executable, committed (2e9ba00); installed copy byte-identical; README documents the cp setup. Block verified real (broke test_classify_ai_ml_from_real_bosch_content's assertion, git push --dry-run ran all 329 tests, refused with exit 1); pass verified real (fixed it back, all green, proceeded). Pushed for real, confirmed live.

Task R: Source of Truth.md next:/Resource Limits rewritten to the real shipped state, cited the 2026-08-21 run.yml trigger and issues #4-8 as evidence. System - Build Log.md got ## 2026-08-21 and ## 2026-08-22 entries matching the existing style. PRD.md Current Status/Open Backlog/Risks rewritten with real 2026-08-22 numbers; contradiction found and corrected — the prompt said Open Backlog "still lists the count-limit spec as pending," it didn't (never was); updated what actually was stale instead. Actions billing API 404'd (token lacks scope, gupta-builds is a user account) — reported as genuinely unmonitored, not guessed.

Vault push incomplete, flagged plainly: two vault-note edits committed locally (369e79af) in the Jarvis checkout but could not push — mid-reconciliation found 887 files of unrelated large-scale churn from other independent sync tools (the graphify live-sync) plus one file (Excluded — Losing The Debate.md) with local uncommitted changes blocking a clean merge. Merge attempt failed ("strategy ort failed"), git safely auto-aborted, no damage done. Stopped rather than force further action into a vault-wide conflict landscape outside this session's scope.

Task S: real timed commit+push with all four hooks present — commit 0.66s (graphify hook confirmed detached/non-blocking), push 3.69s including the full pytest run inside pre-push. No hang, no interaction between hook types.
```

**Follow-up prompt — resolving the vault push** (same session, continuation, written after independently verifying the "vault push incomplete" flag was real: GitHub's copy of `gupta-builds/Jarvis` still had the *old* stale `Source of Truth.md` text, confirmed by fetching raw content directly — the report's own content was correct and live locally, just never reached GitHub. New information supplied: `gupta-builds/Jarvis` has the `obsidian-git` plugin installed (a scheduled, independent sync mechanism unrelated to this pipeline) — almost certainly what the manual merge collided with, on top of the graphify churn. Instructed: do not retry the local merge; push the two files directly via GitHub's Contents API instead, bypassing local git state entirely.)

**Result:**
```
Both files fully verified, byte-for-byte matching the local copies (sizes: 11583 and 32016 bytes, matching the API response's size fields exactly). Local checkout confirmed as /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis — the only path ever used; no git operations run against it this time, only plain filesystem reads.

Source of Truth.md — sha 742a6ab..., PUT succeeded on second attempt (first blocked by the session's own auto-mode permission classifier, not GitHub), new commit dcf2314c. Read-back confirms the next: field now reads the updated text.

System - Build Log.md — sha f1ed61c..., PUT succeeded first attempt, new commit 6151e778. Read-back confirms both new dated entries present in full.

Local checkout state, described not touched: it still sits one commit ahead of GitHub for these two files (369e79af predates the API pushes, now superseded). Working tree still has the unrelated churn. Left for the human to decide.
```

**Independently re-verified 2026-08-22** (fresh review, direct filesystem access to `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis` confirmed available from this session too): `git diff 369e79af origin/master` for both files is **empty** — byte-identical content, zero future merge-conflict risk. `git log 369e79af..origin/master` shows exactly 3 commits ahead (one routine pipeline commit, the two API pushes) — no surprise drift. `369e79af` touches only the two target files, nothing hidden. Main repo (`internship-research-loop`): `HEAD` == `origin/master`, 329/329 tests, all recent CI runs green including the hook-add and PRD-sync commits' own checks. `git config pull.rebase` confirmed `true` locally (the human ran it; silent output on a `git config` set is normal, not an error). Issues #4-8 confirmed still open and correct (the counts really are still over cap). Nothing left outstanding from this phase.


## Prompt 8 — Jarvis: Internship Note-Writing System — Standards, Templates, Workflow Doc (written 2026-08-22, run inside the vault directly)
Full prompt text: see the live file's history / the conversation that produced it — condensed here to preserve space, since the result below carries the substance. Scope: extend `Internship Notes Standard.md` (without rewriting its existing 5 sections) with date_posted/date_found semantics, target_year-empty-is-expected, the `next` chain, `matched_reason` richness; fix dead Templater syntax across all 9 Career templates; write `Tracking Standard.md` for real; investigate whether Program/Contact/Applying need their own Standards; refresh `Internship Pipeline.md`; investigate `2026-07 Found.md`'s dataview; flag (don't resolve) the `Viewed/` semantic conflict and the "review" note-type ambiguity.

**Result, as reported back:**
```
All six tasks done. §6 added to Internship Notes Standard (date semantics, target_year-empty confirmed expected via 200/200 real dossiers sampled + accept_unrestricted: true, the next chain, matched_reason richness — loop-discovered dossiers still carry the bare literal "matched", confirmed live). All 9 templates fixed — confirmed via real Appian Program/Contact/Tracker notes that Templater's <% %> syntax is genuinely dead (every real note is written directly by the promote-dossier skill, never through Obsidian's Templater engine, even though Templater is installed) — dead tags replaced with plain placeholders. Tracking Standard.md written for real (field semantics, Current/Applied/Result lifecycle) — surfaced a real live gap: Internship - Dashboard.md never queries Tracker/Each One/ at all, so a pre-application tracker note is currently invisible to the Dashboard. Program/Contact/Applying Standards: recommended NOT building them yet — low volume, human-authored not code-generated, templates already carry embedded explanatory prose, the one real Program/Contact pair shows no defects; revisit if real examples accumulate defects the way dossiers did. Internship Pipeline.md refreshed (was stale since 2026-07-29) — added the debate comparator, capacity notifications, recheck-to-Viewed; corrected the closing section's promotion count (Appian plus Uber/Western Digital/Deepgram manual finds, all still pre-application). 2026-07 Found.md dataview checked empirically: query syntax is sound; swept all 395 live date_found values, found exactly one format inconsistency (Software Engineer - Ellipsis Labs.md, unquoted date, a leftover from a manual edit) — isolated, unlikely to explain a systemically broken view on its own, query left untouched.

Flagged, not resolved: the Viewed/ conflict is real — What was Viewed.md describes "applied for", the shipped system uses it for closed-never-applied. Tracker/Each One/Applied+Result/ and Applying/Now.md already exist to serve the need What was Viewed.md describes — they're just unpopulated (zero real applications yet). Likely fix is rewriting What was Viewed.md to point at those; Viewed/ itself left untouched. "Review" note type has no match anywhere in the live internship system or CLAUDE.md's type guide — Step 2 (Screen) is the one pipeline step with no note artifact, but not asserted as the answer, just flagged.

Everything in the pre-verified context held up under independent checking — nothing turned out wrong. Session logged in 60_Claude/07_AI_Information/Session Logs/log.md. No code, no git, no dossier/Program/Contact/Tracker notes touched.
```

## Prompt 9 — Codebase: Dossier Audit — What Fails, Why, and Root Cause (Research Only) (written 2026-08-22, run 2026-08-23)
Full prompt text: see the conversation that produced it — condensed here, substance preserved in the result below. Scope: re-derive the real current filter/relevance/classify rules from code fresh; audit all live dossiers against them (six parallel background forks — one per dossier bucket, one on `Viewed/`, one on the `Excluded — Losing The Debate.md` log including a direct Citadel preference-matching trace and the TikTok volume question); report only — remove, edit, and commit nothing.

**Execution notes:** run via six background forks in parallel; two stalled on the watchdog (AI & ML, CyS & Finance) and were resumed successfully; the "Other" bucket fork's first pass was recognized as insufficient (8 tool calls in 99s, nowhere near enough to read ~140 dossiers) and re-run properly; the Excluded-log fork's first notification was mislabeled (described the AI & ML bucket's findings) and was sent back to do its actual assigned task. Full audit took roughly 45 minutes wall-clock. The AI & ML fork went further than scoped and re-ran the current rules against all 390 live dossiers, which helped reconcile several cross-bucket findings.

**Result — the full Task 7 structured report:**

What in the pre-verified starting material turned out wrong: the dossier count (393 → 390 live that day, expected hourly drift), the 57-title-flag list (real, but a floor that misses most of the actual problem), and the root-cause theory itself — "AIJobs has no category field" is real but is *not* why Zipline's 49 dossiers are bad; the actual cause is a separate, still-live extraction bug (below).

**(a) Fails an unambiguous rule — candidates for 100% removal**
1. **Zipline/AIJobs content-extraction bug — 49 dossiers, Other bucket, still live.** Zipline's URLs are a client-rendered SPA; Firecrawl can only fetch the generic `/open-roles` board-index page, so all 49 Zipline dossiers share identical fetched content — the full unfiltered job board, which happens to contain real unrelated titles like "Embedded Software Engineer, Validation." `stage2_confirm()` finds a software-signal hit on that shared page regardless of the actual role, so every one passes with the generic "genuine software engineering role, no bucket-specific signal matched" callout. Confirmed independently by two forks reading full content.
2. **Cross-source duplicates that should have deduped and didn't — ~53 dossiers in ~23 groups.** Almost all predate commit 722ca4d (2026-08-21 21:13), which correctly switched `cross_source_key()` to URL-embedded ATS job ids — no new duplicate has appeared since. Groups: Virtu Financial (×3 job-id groups), PDT Partners, Replit, General Matter, Quadrillion, Notion, Continental Resources, American Express (×4 location variants), HPR, Chicago Trading Co., Aquatic Capital Management, Freeform, DV Trading, Atoms, Melius, Appian (2 identical Excluded-log entries — a dedup gap in the exclusion path specifically). Two mechanisms remain live and unfixed: Workday postings have zero ATS-job-id coverage (FTI Consulting, Medtronic, Continental Resources duplicate pairs, defeated the text-key fallback via trivial title wording); Quadrillion/General Matter's pairs have byte-identical extractable job ids that should have caught them — points at a checkout-freshness race between writing runs, not an identity-logic bug.
3. **`location_eligible()`'s `_NON_US` denylist has real gaps**: Netherlands, Hong Kong, Poland, Israel, bare city names. Concrete passes that shouldn't have: Marshall Wace "Technology Intern - Hong Kong"/"- London", Optiver "FPGA Internship"/"Quantitative Trading Internship" (Amsterdam), plus 3 more in AI & ML.
4. **Non-technical roles passed on weak signal, confirmed by full-text read**: UHY Data Operations Intern, Continental Resources Geoscience Intern (mistagged category), Walleye Capital Finance & Accounting Intern, CNO Financial Reporting Analyst Intern, Dimensional Fund "...Data and Tools" (its sibling "...Insights..." genuinely requires SQL/Python and correctly passes), Vertiv Product Management Intern ×2, Planning Analytics Intern, Sales Data Analytics Intern ×2, Thermal Application Engineer Intern, KeyBank Data Intern, FTI Technology Intern ×2 (bucketed on a bare keyword inside a majors list, real duties are Excel/e-discovery). Root cause: `_ADJACENT_FIELD_COMPANY_HINT_RE` doesn't cover generic business/finance/BI roles, so `stage2_confirm` short-circuits to pass without ever content-checking them.

**(b) Borderline — needs human judgment, do not remove**
AVEVA "Drexel Co-op" (Drexel-only, no university-eligibility gate exists); Teledyne NHRC (classified-facility, US-citizenship-required, no citizenship gate exists); HP Enterprise Operations (overwhelmingly Supply Chain content, "software" in one closing paragraph); Optiver FPGA ×3, Jane Street Cybersecurity Analyst, Appian InfoSec Engineer (flagged by an automated re-check as stage2 failures but are real hardware/security roles on inspection — false positives from a too-broad hint regex, tighten it, don't remove these); Two Sigma "AI Research Scientist" and TMEIC Engineer Intern (fetched content is garbage — a sign-up page / raw Workday form — functionally unevaluated; "AI Research Scientist" also doesn't match any classify.py AI/ML regex literally); GuideWell Enterprise Analytics, GE Vernova Application Engineer Co-op, IMEG Innovation Services, Dimensional Fund "...Operations Insights..." (genuine judgment calls); 3 Microsoft/Google Fullstack dossiers with a dumped ~487KB careers-search page instead of real content (one already manually caught 2026-07-26).

**(c) Viewed/ findings**
Only 4 real dossiers (not "many"): Capital One SWE Intern, Capital One Cyber Security Intern, CNO Financial Cyber Security IT Intern, JP Morgan Chase Data Internship — all moved 2026-08-23, all `removed_reason: "active: false upstream"`, all corroborated by a matching `logs/rechecks.jsonl` entry. All 4 substantively correct. Real bug found instead: all 4 carry a `(2)` filename-collision suffix — `recheck.py`'s `plan_removals()` re-sweeps `Viewed/` itself (never checking `status == "removed"`), so a dossier that stays closed gets re-moved every day forever, `(2)`, `(3)`... — a re-processing bug, not a misclassification one.

**(d) Excluded-log findings, including the Citadel trace and TikTok**
Recount confirmed exact: 304 entries, 86 companies, pre-verified tallies all exactly right. **Citadel**: the mechanism is not broken — `company_matches_preference()` correctly resolves `preference_tier: high` on the bare string "Citadel". Real cause: the preference tier is a binary gate (all "high" tier ties at rank 0), recency is the only real tiebreaker among tied preferred companies; the posting (never fetched, since excluded candidates never reach `validate_and_write`) almost certainly classified into "Other" — the smallest budget (1/run) — where it lost 5 straight hourly recency ties to fresher preferred-company arrivals. A design gap (undifferentiated tier + tiny bucket budget), not a matching bug. **TikTok/volume**: sharper than gradual crowding — 287 of 304 exclusions (94%), including 106 of TikTok's 107, happened in a single day, 2026-08-21 — a burst, not a trickle. Spot-checked 20+ TikTok lines: genuinely distinct postings, not re-logged duplicates. Real mechanism: a large batch of new candidates across many companies arrived "new" in the same window, all lost fixed per-bucket budgets to each other for 5 consecutive hourly runs, all crossed `MAX_DEBATE_LOSSES` together in one run — the system can't distinguish "genuinely undesirable" from "the queue is temporarily backed up," and converts a transient backlog into permanent exclusion within ~5 hours. Per-company breakdown: American Express (18), RTX (11), The Nuclear Company (8) — genuine volume-crowding of real distinct postings, not a leak. **Zipline (13), Varda Space Industries (13), Astranis (6) are the important exception** — genuinely non-technical titles mixed in (Zipline "Sales Operations Analyst"; Varda "Biologics Formulation Research," "Environmental Health & Safety"; Astranis "Mechanical Engineer," "CAD Engineer-Librarian") that were never content-checked, because excluded/losing candidates never reach the Firecrawl fetch — the same latent failure mode as (a)#1/#4, just hidden by losing the volume race instead of being caught by a gate. Uline (5), Springs Window Fashions (5) show the identical pattern.

**(e) Date/target_year empirical findings**
Both behave exactly as the code predicts, no evidence of guessing or dropped data. `date_posted`: real ISO date in every dossier except the 2 `source: manual` entries (expected — manual entries skip `normalize_*`/`_iso_date()`, and `_iso_date()` returns `None` on a falsy epoch, never a placeholder). `target_year`: empty `[]` on all 390 live dossiers, zero exceptions, matching `ingestion/normalize.py` (only `normalize_josegael` ever populates it) — more interesting: **zero live dossiers currently come from source "Jose-Gael-Cruz-Lopez" at all**, across all four buckets — not itself a rule violation, but worth checking `logs/runs.jsonl`'s `filter_match_counts["Jose-Gael-Cruz-Lopez"]` directly for silent degradation. Separately (a content-quality bug, not a filter bug): Microsoft ×2 and a Google/Freehire Fullstack dossier contain a dumped ~487KB generic careers-search-results page instead of the actual posting.

**(f) Recommended profile.yaml/filter changes (described, not implemented)**
1. Detect SPA-board-index-shaped fetched content (link-dominated, not prose) and treat as thin/unconfirmed rather than a real stage2 pass — fixes the Zipline leak.
2. Tighten `_ADJACENT_FIELD_COMPANY_HINT_RE` (space/defense too broad; extend to generic business/finance/BI families) — same co-occurrence-window pattern as the 722ca4d threat fix.
3. Add Netherlands, Hong Kong, Poland, Israel to `_NON_US`; consider a bare-city fallback.
4. Extend `_ATS_JOB_ID_PATTERNS` to Workday's `myworkdayjobs.com` shape (strip trailing `-N`).
5. Un-tie the preference tier — a graded/ranked scheme or a diversity tiebreaker so one preferred company can't be crowded out by another preferred company's fresher posting in the same tiny bucket budget.
6. Reconsider `MAX_DEBATE_LOSSES=5` (~5 hours) relative to real arrival burstiness.
7. One-time retroactive re-sweep of pre-722ca4d dossiers against current rules — flag, don't auto-delete (a couple of true positives, Optiver FPGA / Jane Street / Appian security, would be wrongly killed by a naive re-run).

**(g) Recommended GitHub Actions/pipeline enhancements (described, not implemented)**
1. A periodic re-validation job that re-checks existing vault dossiers against current code and files a digest issue for anything that would now fail.
2. Fix `recheck.py`'s `plan_removals()` to skip files already under `Viewed/` (or check `status != "removed"`) — stops the daily re-move/`(N)`-suffix bug in (c).
3. A per-run alert when debate-loss exclusions spike well above the normal trickle (e.g. >20 in one run) — would have surfaced the 2026-08-21 burst as it happened.
4. A direct check of whether Jose-Gael-Cruz-Lopez is still returning candidates in recent runs.


## Prompt 10 — Codebase: Act On The Task 7 Audit (written 2026-08-23, run 2026-08-23)
Full text: see the conversation that produced it. Four phases: fix the 5 root-cause bugs (Zipline SPA-detection, `recheck.py` Viewed/ re-sweep, `_NON_US` gaps, adjacent-field hint tightening with regression protection for known false positives, Workday ATS-id pattern), then act on affected dossiers (re-evaluate Zipline, remove confirmed non-technical/non-US, dedupe legacy duplicate groups, touch nothing borderline), one cheap JGCL health check, two new GitHub Actions features. Two items explicitly left for a human decision: preference-tier grading, `MAX_DEBATE_LOSSES` retuning.

**Result:**
```
367 tests passing (up from 329), 7 commits, full suite green throughout.

Phase 1 (5 commits, 38 new tests): Zipline SPA board-index bug (ceeea7d, 4 tests), recheck.py Viewed/ re-sweep bug (2eb6bab, 1 test), _NON_US denylist gaps (c397413, 6 tests), space/defense false-positive fix + business/finance/BI hints (fbf934a, 15 tests), Workday ATS-id pattern (084e3da, 3 tests). Notable finding: a company-wide gate for Walleye Capital would have wrongly failed a genuine "Data Science Intern" role with no signal-word match in real content — kept narrow. KeyBank/Truist's bad dossiers still pass even post-fix because their real content literally mentions Python/SQL as a tool-list/team-name aside, not a real requirement — a documented limitation of the keyword-only check, not something this fix closes.

Phase 2 (44 dossiers removed, recoverable): 13 confirmed non-technical (UHY, CNO Financial, Vertiv ×5, Walleye Finance, Continental Resources Geoscience, Dimensional Fund "Data and Tools", FTI ×2), 7 non-US (Optiver ×2 Netherlands, Google ×2 Israel, Marshall Wace ×3 Hong Kong/London), 24 legacy cross-source duplicates (Virtu ×3 groups — 7 removed, one extra duplicate found during verification not in the original audit — plus PDT Partners, Replit, Notion, Melius, Deepgram, Chicago Trading Co. cross-bucket, Freeform, Atoms, DV Trading/Group, HPR, General Matter, Quadrillion cross-bucket 3-way, Medtronic, Continental Resources Data Analyst). Explicitly not removed, correcting the earlier audit's over-broad characterization: Vertiv "Operations Intern - Summer 2027" (real Python/SQL/data-pipeline requirements, genuinely fine). Left borderline, not removed: KeyBank/Truist (documented false-pass above). American Express's ~20 entries explicitly skipped — too much risk of conflating legitimately-different postings without individually verifying each URL, flagged for follow-up. Zipline's 49 dossiers untouched — the code fix shipped and tested, but re-evaluating existing dossiers needs a real Firecrawl fetch, and this session reported FIRECRAWL_API_KEY unavailable to it (later found to be a session environment-sourcing gap, not a real absence — it's in ~/.bashrc).

Phase 3: Jose-Gael-Cruz-Lopez not degraded — fetches 4-5 real candidates on nearly every recent run; zero live dossiers today is explained by the already-documented 2026-07-18 manual vault cleanup (13 JGCL uids sit in seen_ids.json with no corresponding live file). Correctly a no-op.

Phase 4 (2 commits): revalidate.py + .github/workflows/revalidate.yml (weekly re-validation against current rules, files a digest issue). should_alert_on_exclusion_spike() in run_pipeline.py, fires when exclusions exceed 20 in one run, citing the 2026-08-21 burst.

Flagged, not implemented: preference-tier grading (Citadel's mechanism isn't broken, it's undifferentiated — a graded scheme vs. a diversity tiebreaker is a real design choice); MAX_DEBATE_LOSSES retuning (5 consecutive losses converts backlog into permanent exclusion fast, as the burst showed — the right number or a different mechanism is a design call).
```

## Prompt 11 — Jarvis: Sync Building System, 30_Order, Graphify Mirror (written 2026-08-23, run 2026-08-23)
Full text: see the conversation that produced it. Five tasks: record the Task 7 audit in `System - Build Log.md`/`Source of Truth.md`; cross-reference Building System/30_Order docs against the graphify mirror for drift Prompt 9 wouldn't have caught; confirm the graphify-deletion incident stays closed; re-check whether Program/Contact/Applying Standards are still not needed; re-flag the still-open `Viewed/` conflict and "review" ambiguity.

**Result:**
```
Task 1: System - Build Log.md got a ## 2026-08-23 entry with the audit's headline findings, full detail pointed at the Archive note. Source of Truth.md corrected only what the audit actually contradicts — Hard Gate §2 (location) and §4 (CS-relevance) each got a cited caveat that the design is right but the implementation has real gaps; Resource Limits got the debate-comparator design-gap paragraph and dedup status; Priority Classification got the Viewed/ re-sweep bug. The closing "What Closing The Loop Means Here" section was rewritten to say verification is stale as of 2026-08-23 rather than still claiming discovery is "independently verified solid." Everything else left untouched — nothing else was contradicted. Internship Pipeline.md got one added line so it doesn't read as already-fixed either.

Task 2: Confirmed the graphify mirror is a pure structural mirror (function/file/test call-graph, no source text), static at 89fd543/f75662ac. Spot-checked names cited in Standards/Source of Truth docs — build_frontmatter(), opt_exclusion(), extract_content() (plus its real regression tests), validate.py, plan_removals(), debate.py/debate_compare(), location_eligible() all confirmed real nodes. A handful of cited constants (REQUIRED_FRONTMATTER_FIELDS, _NON_US, _ADJACENT_FIELD_COMPANY_HINT_RE, BUCKET_CAPACITY, MAX_DEBATE_LOSSES, dossier_uids.json) have no node — consistent with the mirror never node-ifying bare constants/JSON state, not a doc inaccuracy. Nothing further found beyond Prompt 9's own audit.

Task 3: Deletion incident confirmed closed — verified f75662ac directly, content matches its message exactly. Exactly one commit has touched that folder since (f6e056e7), and it only rewrote graph.canvas (visual layout) — zero new node files added or removed. No new orphans. The underlying graphify manifest-writer bug still unfixed but flagged only, not touched.

Task 4: Program/Contact/Applying Standard recommendation stands — Prompt 9's audit scope never touched those note types, no new evidence either way.

Task 5: Both items re-flagged, no new decision given at the time — the Viewed/ semantic conflict and the "review" note-type ambiguity. (Both resolved by the human immediately after this report — see Prompts 12/13.)
```


## Prompt 12 — Codebase: Ship The Two Decided Design Changes, Finish The Deferred Cleanup (written 2026-08-23, run 2026-08-23)
Full text: see the conversation. Reserved additive preferred-company slot per bucket, `MAX_DEBATE_LOSSES` 5→48, American Express individual verification, Zipline 49-dossier re-fetch (confirmed unblocked — `FIRECRAWL_API_KEY` was in `~/.bashrc` all along).

**Result:**
```
All committed separately, pre-existing unrelated CLAUDE.md/graphify-out changes left untouched. 372 tests passing throughout.

Task A (288b390): additive reserved slot in _prioritize_and_cap, never carved from existing budget. 3 tests: losing preferred candidate wins via reserved slot; no-preferred bucket unchanged; 3-way preferred recency tie-break.

Task B (23e52db): MAX_DEBATE_LOSSES 5→48, citing comment updated with the 2026-08-21 287-exclusion burst. Existing tests rewritten to reference the constant, not hardcoded values.

Task C (3b99251): American Express — 18 entries (not ~20), 15 distinct, 3 genuine duplicate pairs (same numeric job ID under egug.fa.us2.oraclecloud.com, differently punctuated titles). Added an Oracle Cloud HCM ATS-id pattern, domain+path anchored, 2 tests.

Task D (vault-only, no commit): Zipline's 49 dossiers fully re-verified with live Firecrawl content. 12 kept (genuine SWE-relevant — Computational Physics, Controls Engineer ×2, Enterprise Systems SWE ×2, Long Range Platform Embedded Firmware, Perception, Software Engineer Intern (Sp), Software Systems Validation ×2, System Test Automation ×2), 37 removed (confirmed non-technical by real content, moved to Obsidian trash not permanently deleted).
```

## Prompt 13 — Jarvis: Implement The Two Decided Vault Changes (written 2026-08-23, run 2026-08-23)
Full text: see the conversation. Rewrite `Viewed/What was Viewed.md` per the "keep existing design" decision; build a real, lightweight Step 2 (Screen) artifact per the "yes, real lightweight artifact" decision, choice of implementation left to the executing session weighed against the `company/<slug>`-tag precedent.

**Result:**
```
Task 1: Viewed/What was Viewed.md rewritten — Viewed/ holds closed-never-applied postings (Standard §4, recheck.py's real behavior), points at Applying/Now.md + Tracker/Each One/Applied+Result/ for the "have I applied" need, both empty since zero real applications exist yet. Cited Prompts 8 and 9 (Archive) as the two independent sources for this read. Added a live dataview of Viewed/'s real contents; kept the original "organize by month once big" instinct, redirected at the correct purpose.

Task 2: Chose frontmatter fields (screened_date/screened_decision/screened_reason on the dossier), not a separate note type. Explicit reasoning: the company/<slug>-tag-over-hub-note precedent applies with more force here (per-dossier, potentially hundreds of times, vs. per-company). A Screen call is a short state-transition fact (same shape as §4's removed_date/removed_reason), not a growing research artifact the way a Program note is. status left untouched (Screen is orthogonal to unreviewed/removed/promoted, not merged in). Contact reachability deliberately gets no field, matching Pipeline Step 2's existing "noted, never a gate" rule.

Task 3: New §7 in Internship Notes Standard.md (field spec + the precedent-weighing reasoning + "not retroactive"/"not yet automated"). Internship Pipeline.md's Step 2 now points at the real fields.

Flagged, not touched (per scope): Viewed/Removed Dossiers MOC.md — the note every removed dossier's notes: field is required to link to — is itself still empty. Noted for a later prompt. Nothing from Prompt 12 described as shipped anywhere in this work.
```


## Prompt 14 v2 — Codebase: New Discovery Sources, Refined With Real Yield Data + InternDock (written 2026-08-24, run 2026-08-24)
Full text: see the conversation. Refined before ever running with real per-source yield numbers (fetched vs. matched over the last 20 runs) and two real InternDock URLs the human provided. Seven tasks: resolve JGCL's zero-yield question, diagnose Ashby/Freehire's low yield, evaluate InternDock as an ongoing source (contingent on a real discoverable index existing), verify a web-search claim about zshah101 having a richer API, build Lever if a second real company is found, investigate LinkedIn's Greenhouse board + 7 other named-priority companies, re-verify speedyapply/sndsh404 and sweep for new repos.

**Result:**
```
2 commits, 372+ tests passing throughout (exact new count not restated in the summary — see the repo directly).

Task 1 — JGCL: the SOURCES-tuple-tie-break hypothesis in the prompt was WRONG. Real cause, confirmed by live replay: JGCL's entire currently-matching pool is 3 postings (MLH Fellowship, White House HBCU Scholars Program, UNCF Scholarships Portal) — non-software scholarship/fellowship programs, already in seen_ids.json because they were written once then manually deleted during the 2026-08-23 dossier-audit session (46 vault_delete calls, auto-captured as "08-23 Internship dossier audit and filter-rule reconciliation," 241 min) — a human judged them not real matches, and seen_ids' own semantics mean they never get re-offered. Two more (TMCF, AAUW, also scholarships) already hit MAX_DEBATE_LOSSES and sit in excluded_uids.json. Conclusion: not a bug, JGCL's feed is just thin and skews toward non-CS scholarships for this persona. No code change.

Task 2 — Ashby/Freehire: both confirmed working as designed. Ashby: live-checked all 9 seeded companies, genuinely only ~4 have open roles right now. Freehire: FREEHIRE_COMPANIES is deliberately just {google, uber} by design (documented, not an oversight); live fetch returned 6 postings, mostly non-US/non-eng, correctly filtered downstream. No bugs, no changes.

Task 3 — InternDock: interndock.com/sitemap.xml is a real, live, plain-HTTP index with more drop-shaped slugs than the 2 originally found — this is a real ongoing source, not a one-time snapshot. Built ingestion/interndock.py: sitemap-based candidate detection + a posting parser built from real verbatim text (the actual link text is always "Apply", not the title — the original guessed format was wrong). Slug shape alone is unreliable (one drop-shaped slug is actually a prose article, not a listing) — the real gate is structural match-count within the fetched page. 6 new tests, all passing. Scope deliberately stopped at detection+parsing — full SOURCES wiring (id strategy, state file, cadence) flagged as needing its own design pass, not built yet.

Task 4 — zshah101 RSS/API claim: confirmed TRUE (real RSS feed, docs/api/jobs.json, live dashboard) — but a prior session had already evaluated this exact tradeoff and deliberately chose data/jobs.json (497 raw entries, full truth) over the pre-filtered API (243 entries, someone else's filter applied first). That reasoning still holds today, gap is bigger not smaller. No change.

Task 5 — Lever: found real dossier URLs for a second genuine Lever-hosted company (Belvedere Trading, plus Hermeus/Xsolla candidates surfaced, one ruled out as a nonprofit not a tech employer). Built fetch_lever/normalize_lever mirroring Greenhouse/Ashby's per-company pattern, wired into SOURCES and recheck.py's FEEDS. Live-verified end-to-end: 61 postings fetched, 3 real matches, cross-source dedup against existing Palantir dossiers confirmed working via the existing write gate.

Task 6 — LinkedIn's Greenhouse board confirmed real but 0 intern postings anywhere in it — genuinely nothing there, not a detection failure. None of Two Sigma/Citadel/Capital One/Bloomberg/Microsoft/NASA/MLH have a reachable Greenhouse/Ashby/Lever token (confirmed via direct API probes) — all enterprise-scale, almost certainly on Workday-class ATSes this pipeline has no connector for. Correctly not built.

Task 7 — speedyapply/sndsh404 both still structurally blocked (private Supabase backend; README + binary .xlsx only — re-confirmed, not stale). Found SuryaHarikrishnan/2027-internship-tracker (13,180 entries) but it's 100% re-aggregated from SimplifyJobs+vanshb03 already-integrated data — zero unique value, correctly skipped. Two genuinely new, real, structured candidates surfaced and NOT yet built: ApplyGuy/2027-Internships (real JSON, e.g. "Toyota of Cedar Park Keating LLC — Software Developer Intern," posted today) and dreamworkhq/Tech-Internships-2027 (real JSON, 720 entries, e.g. Fannie Mae Data Science Intern) — flagged for a future round.
```

## Prompt 15 — Jarvis: Refresh Both Resources Docs, Close The Removed Dossiers MOC Gap (written 2026-08-23, run 2026-08-24)
Full text: see the conversation (unchanged from its original write-up). Three tasks: refresh `List/Resources.md`'s operational per-source table with real numbers, refresh `Research Loop - Resources.md`'s Named-Program Coverage Check, build `Viewed/Removed Dossiers MOC.md` for real.

**Result:**
```
Task 1: List/Resources.md refreshed with real 2026-08-24 numbers — SimplifyJobs 137 live dossiers (was 138 pre-removal-batch, 1.5% match rate), vanshb03 74 (was 77, 26.6%), zshah101 68 (12.1%), Greenhouse 16 (53.6%, structurally capped), AIJobs 11 (25.6%), Freehire 2 (28.6% but tiny volume, flagged open), Ashby 0 live (structurally capped), Jose-Gael-Cruz-Lopez 0 live despite 76 real matches over 20 runs — flagged explicitly as "under investigation" at the time, pointing at Prompt 14 (since resolved — see above, not a bug).

Task 2: Research Loop - Resources.md's Named-Program Coverage Check re-checked against real frontmatter. Coverage moved 3/11 → 5/11: Jane Street still 11 (unchanged), D.E. Shaw still 1, Google still 3 (no ASDI mention), Microsoft 0→6 (checked for "Explore" — only false-positive JS chrome matched, still unconfirmed as the named program), Two Sigma 0→1 (no "First-Year" mention, generic). Capital One actually dropped 2→0 (both closed, moved to Viewed/ on 2026-08-23 — noted as churn, not a real gain). Citadel, LinkedIn, MLH, NASA, Bloomberg remain uncovered (since resolved — see Prompt 14 v2 Task 6 above: no viable connector exists for any of these, not a discovery gap).

Task 3: Viewed/Removed Dossiers MOC.md was a real 0-byte file despite 4 live dossiers linking to it. Built for real per the MOC Standard (Purpose → Map → Status → Dataview): documents the one real removal batch (4 dossiers, all 2026-08-23, all active: false upstream), including the Capital One same-day double-closure as a hiring-cadence signal. Corrected the prompt's own stale estimate ("dozens" of dossiers pointing here) to the real current count (4).
```

### Prompt 16 — Jarvis: Sync Building System To The Real Post-Prompt-14v2 State (written 2026-08-24, run 2026-08-24, archived 2026-08-27)
No execution report was ever pasted back for this session — archived here from independent verification of live vault state against all 4 tasks, not from a human-provided report, per the explicit ask to clean this up before adding new content.

Full text:
```
**Run inside the Jarvis vault directly** (Windows, Sonnet 5, high effort). Vault-note work only.

**Context — what actually changed, verified, not to be re-derived:** Lever shipped live (`fetch_lever`/`normalize_lever`, wired into `SOURCES`/`recheck.py`, 2 real companies — Palantir plus Belvedere Trading — 61 postings fetched, 3 real matches at build time). InternDock got real detection+parsing code (`ingestion/interndock.py`, sitemap-based, 6 tests) but is **explicitly not wired into `SOURCES` yet** — a partial build, not a live source; don't describe it as one. The JGCL zero-yield question is **resolved**: not a bug, three specific scholarship postings (MLH Fellowship, White House HBCU Scholars, UNCF Scholarships Portal) already correctly excluded via `seen_ids`/`excluded_uids`, the feed is just thin toward non-CS content for this persona. LinkedIn's Greenhouse board and the other 7 named-priority companies (Two Sigma, Citadel, Capital One, Bloomberg, Microsoft, NASA, MLH) are **confirmed dead ends for direct-ATS coverage**. Two new, real, unbuilt repo candidates exist (`ApplyGuy/2027-Internships`, `dreamworkhq/Tech-Internships-2027`). The 2026-08-23 "46 `vault_delete` calls" is a real, already-tracked session, not an untracked event.

Task 1 — `System - Build Log.md`: add a `## 2026-08-24` entry recording Lever, InternDock's partial build, the JGCL resolution, the LinkedIn/7-company dead-end finding, the two new unbuilt repo candidates, and confirmation the 2026-08-23 deletions are accounted for. Point at the Archive note rather than duplicating detail inline.

Task 2 — `Source of Truth.md`: fix now-wrong claims. At minimum: any "eight sources" claim is now wrong (nine, with Lever) — a partial InternDock build should not count as a tenth live source. Correct the JGCL/LinkedIn-7-company framing if referenced with the older, vaguer wording.

Task 3 — `Research Loop - Resources.md`: move Lever to the live sources table with real numbers; add InternDock as its own in-between status; re-confirm speedyapply/sndsh404 stay deliberately-not-built and add ApplyGuy/dreamworkhq as found-but-not-yet-evaluated; correct the JGCL entry to the real specific finding; rewrite the Named-Program Coverage Check framing — the month-old open question is now answered (no, none of the 8 named companies post through Greenhouse/Ashby).

Task 4 — `10_Areas/Career/Internships/List/Resources.md`: resolve the JGCL "under investigation" flag to the real, closed finding.

Explicitly out of scope: no code changes to internship-research-loop; no describing InternDock/ApplyGuy/dreamworkhq as more done than they were at the time.

Report back: per task, what changed and where, with the specific old-vs-new claim for anything corrected.
```

**Result** (reconstructed 2026-08-27 from direct comparison of live vault state against all 4 tasks — no report was ever reviewed for this session, matching the handoff's own flag):
```
Task 1 — System - Build Log.md: a matching entry exists ("2026-08-24 — Prompt 14 v2: Lever Shipped, InternDock Partial, JGCL Resolved, LinkedIn/7-Company Dead End Confirmed"), covering the exact content this task asked for. Confirmed present via document-map heading check.

Task 2 — Source of Truth.md: confirmed done at the time — the doc's sources section read "Nine Sources" as of 2026-08-24, per that section's own later self-correction ("the 'Nine' heading... was stale within a day of being written," added 2026-08-27 once Lever+InternDock+ApplyGuy pushed the real count to eleven). The eight→nine correction is confirmed as this task's real output; its own later staleness (nine→eleven) is expected drift already caught and fixed by a subsequent pass, not a failure of this task.

Task 3 — Research Loop - Resources.md: confirmed done — live headings match exactly: "Live, Committed... (Lever added 2026-08-24)", "InternDock — Built, Not Yet Wired (2026-08-24)", "Found, Not Yet Evaluated For Build (2026-08-24)" (ApplyGuy/dreamworkhq), "Named-Program Coverage Check (refreshed 2026-08-24) — Coverage Gap Remains, Connector Question Now Closed".

Task 4 — List/Resources.md: confirmed done — the JGCL flag is resolved; cross-referenced via this Archive's own Prompt 15 result text, which already carries a "(since resolved — see above, not a bug)" annotation reflecting this correction.

All 4 tasks show real, matching artifacts in the live vault; nothing found contradicting the prompt's asks. Treated as fully executed.
```

### Prompt 17 — Codebase: Finish InternDock's Wiring, Evaluate The Two New Repo Candidates (written 2026-08-24, run 2026-08-24, archived 2026-08-27)
No execution report was ever pasted back for this session either — archived here from direct git log/diff inspection of commit `1d27f5b` (2026-08-24 02:41), which carries its own detailed reasoning in the commit message.

Full text:
```
**Fresh session**, `gupta-builds/internship-research-loop`. Read `CLAUDE.md` first. `ingestion/interndock.py` exists (sitemap-based detection + parser, 6 tests) but is not wired into `SOURCES` — verify this yourself before starting.

Task 1 — Design and ship InternDock's SOURCES wiring. Real open questions to resolve, not guess at: identity/uid strategy (no native id the way Greenhouse/Ashby/Lever have — check the real `href` URLs for a stable identifier, or fall back to a content-hash approach, naming that explicitly as a real limitation if so); cadence/state (sitemap-based detection cadence is a real design decision — InternDock's own two known drops were ~6 weeks apart, don't assume hourly); volume/capacity interaction (a single drop is ~650-658 postings, far more than one run's write budget — confirm the existing per-bucket budget/deferred mechanism handles this gracefully). Build it, wire into SOURCES, add to recheck.py's FEEDS if applicable, fixture-based tests, full suite green.

Task 2 — Evaluate ApplyGuy/2027-Internships (confirmed real JSON, example: "Toyota of Cedar Park Keating LLC — Software Developer Intern"). Verify the schema fresh, check scale/update frequency, decide with the same rigor as every existing source's original evaluation whether it's worth building. Build if yes; say so plainly if not.

Task 3 — Evaluate dreamworkhq/Tech-Internships-2027 (confirmed real JSON, 720 entries, richer schema with salaryMin/salaryMax/aiRoleKind/postedAt/firstIndexedAt). Same evaluation discipline as Task 2.

Discipline: separate commits per source, real citations, fixture-based tests, full suite green at every step.

Report back: Task 1's identity/cadence/state decisions and why, confirmation InternDock is genuinely live in SOURCES, real numbers from a live test run. Task 2/3: built or not, with real reasoning either way.
```

**Result** (reconstructed 2026-08-27 from direct git inspection):
```
Task 1 — InternDock wired end-to-end, confirmed live via `grep fetch_interndock run_pipeline.py`. Real design decisions made: identity = the posting's own real Apply URL (not a content hash — every InternDock entry carries a real employer ATS link; `cross_source_key` already collapses these against direct Greenhouse/Ashby/Lever copies via its existing ATS-URL job-id regexes, no changes needed). Cadence/state: event-driven, not fixed — `state/interndock_seen_guides.json` persists which sitemap guide URLs have been Firecrawl-fetched, fetching each new one exactly once (real drops are ~6 weeks apart, so hourly sitemap.xml polling is free and the one paid Firecrawl call only fires when something's genuinely new). Doesn't fit the uniform SOURCES tuple (needs Firecrawl + persisted state) — it's a separate step in `run_once()`, inserted last so cross-source-duplicate ties resolve toward direct per-company sources; not wired into recheck.py's FEEDS (re-verifying would mean re-Firecrawling every seen drop page for marginal value). Volume-tested: a live-simulated 650-posting spike drains gracefully through the existing budget/debate mechanism (this_run=4, deferred=646, no crash, no silent drop) — but surfaced a real, separate finding not fixed here: 14/15 real fixture titles land in the "Other" bucket (budget 1/run) because `classify()` doesn't recognize generic "Software Engineering Intern" titles as Fullstack/AI-ML/CyS&Finance, a real future bottleneck flagged for a separate decision.

Task 2 — ApplyGuy built and shipped. Confirmed live 2026-08-24: 202 real entries, own-sourced (not a re-scrape, unlike SuryaHarikrishnan/2027-internship-tracker, checked and rejected same-day), updates ~every 15 minutes, reaches Workday/Workable/Paylocity ATSes with zero other coverage. ~39% of entries (78/202) carry a literal "Not specified" season placeholder, deliberately mapped to empty terms at normalize time. Live-verified: 200 fetched, 137 real matches at build time — notably higher yield than every other source. Not wired into recheck.py's FEEDS (left open, no evidence either way on absence-from-feed reliability). 385 → 401 tests, full suite green.

Task 3 — dreamworkhq/Tech-Internships-2027 evaluation: **never executed.** No commit, no code, no test, no mention anywhere in git history. Confirmed by direct search (`git log --all --grep`, grep across `ingestion/` and `tests/`) — this is a real, honest gap, not a "evaluated and declined" result. Still a real, open candidate (720 real entries, richer schema) if a future session wants it — not urgent given the write-starvation bottleneck this project is currently prioritizing over new source growth (see the 2026-08-26 postmortem and Prompts 18/19).
```

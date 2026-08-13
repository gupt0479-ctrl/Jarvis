---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: wsl
title: "Fix bugs in internship pipeline and implement dossier standards"
started_at: 2026-07-30T07:50:37
ended_at: 2026-07-30T15:57:54
duration_minutes: 487
exported_at: 2026-08-11T12:13:12
project: internship-research-loop
cwd: '/home/anant_gupta/projects/work/internship-research-loop'
session_id: ba5bb631-64dc-4990-bbb6-0fcb86c40683
status: raw
turn_count: 4
tools_used:
  Bash: 76
  Edit: 77
  mcp__jarvis__vault_get_document_map: 7
  mcp__jarvis__vault_list: 5
  mcp__jarvis__vault_patch: 5
  mcp__jarvis__vault_read: 20
  Read: 62
  TaskCreate: 1
  ToolSearch: 3
  Write: 4
tokens:
  input: 8934
  output: 527959
  cache_creation: 1802673
  cache_read: 119078062
  total: 121417628
cost_usd: 36.323762
model:
  - claude-sonnet-5
files_touched:
  - "/home/anant_gupta/projects/work/internship-research-loop/core/relevance.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/classify.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/identity.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/filter.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/recheck.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_posting_page.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_relevance.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_classify.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_validate.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_recheck.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/ingestion/normalize.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/posting_google_careers.md"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/profile.yaml"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/debate.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/run_log.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py"
tags:
  - input
  - ai-conversation
  - claude-code
  - wsl
---

# Fix bugs in internship pipeline and implement dossier standards

## You

You are working in gupta-builds/internship-research-loop. Context: Prompts 1-3 already shipped (core/relevance.py, core/classify.py, the priority-folder routing in vault_writer/writer.py, the /promote-dossier skill) — all confirmed live on master. This prompt was originally written 2026-07-26 and never executed (confirmed via git log — zero commits against it). A follow-up live audit on 2026-07-29 found the same bug classes recurring on new real postings plus one new bug class, and the user specified additional vault-side requirements. Read `30_Order/Standards/Internship Notes Standard.md` in the Jarvis vault before starting — it's the real, concrete contract for dossier notes (frontmatter, body structure, interlinking, removal handling, resource limits) that this whole prompt implements; it did not exist (empty file) until this revision. This prompt covers nine tasks — five real, evidence-based bugs (A-E, A also carries a design revision) plus four new requirements (F-I). Fixture files/real examples are named throughout; use the real content, don't write synthetic test data.

**Before starting, confirm the assumed-live pieces actually exist** — `core/relevance.py` (`stage1_reject`/`stage2_confirm`), `core/classify.py` (`classify`/`BUCKET_FOLDERS`), and the priority-folder routing in `vault_writer/writer.py`. If any of them are missing, stop and report that rather than building Tasks B/C/F/G/I on top of a false assumption — this exact failure mode (building on an unverified "already shipped" claim) is why Prompt 4 sat unexecuted for three days; don't repeat it in the other direction by assuming Prompts 1-3 landed exactly as described without a fresh check.

### Task Order
No task strictly blocks another except two real dependencies — respect these, the rest can run in any order:
1. **G before H.** Task H's move-to-`Viewed/` logic appends to the `notes:` frontmatter field that Task G creates. Building H first means building it against a field that doesn't exist yet.
2. **E before I.** Task E fixes *what* gets fetched from Google's careers site (currently the wrong page); Task I improves *how* fetched content gets formatted. Doing I first means polishing the formatting of content Task E is about to replace anyway.
Suggested full order: **B, C, D, F** (independent gate/dedup fixes — any order among these four) → **E → I** → **G → H** → **A** (fully independent of everything else, do it whenever convenient). This is a suggestion for a sane single pass, not a hard requirement beyond the two dependencies above.

### Files Touched, By Task
Check this before starting a task so two tasks editing the same file don't clobber each other's changes mid-session:
| File | Tasks |
| --- | --- |
| `run_pipeline.py` | A |
| `core/relevance.py` | B, C |
| `core/classify.py` | C |
| `core/identity.py` | D |
| `vault_writer/validate.py` | D (tie-break reference only, no edit), G (add `notes` to `REQUIRED_FRONTMATTER_FIELDS`) |
| `ingestion/posting_page.py` | E, F, I |
| `vault_writer/writer.py` | G, H (`build_frontmatter`, `load_dossier_uids`/`save_dossier_uids`) |
| `recheck.py` | H |
`core/relevance.py` (B, C) and `ingestion/posting_page.py` (E, F, I) each get touched by multiple tasks — read the file fresh before each task on it rather than working from a stale in-memory copy of what an earlier task in this same session already changed.

## Task A — Dossier count-limit, as a NOTIFICATION not a hard write-refusal (revised 2026-07-29)
Currently `run_pipeline.py:66` has `MAX_NEW_WRITES_PER_RUN = 18` with no per-bucket split and no ceiling on total accumulated dossiers — still true, checked directly 2026-07-29. **Live counts right now, checked 2026-07-29: `1 - AI & ML` 53, `2 - Fullstack` 21, `3 - CyS & Finance` 54, `Other` 11 — two buckets are already past the original 50 design number, so this is not theoretical anymore.** Original design (`Dossiers-to-Create.md`, `Source of Truth.md`) said "refuse to write into a bucket already at 50" — **the user explicitly overrode that framing**: this is a notification mechanism, not a silent gate that drops a real eligible posting the way an exclusion rule does (that asymmetry — a false exclusion loses an opportunity for nothing, a false inclusion costs one screening read — is this codebase's founding design principle everywhere else; a hard-refusal cap violates it for no reason, since the actual scarce resource is human review attention, not vault storage). Implement:
1. A per-bucket count check before writing (still count real files in the vault checkout per bucket, same mechanism originally planned) — but do **not** refuse the write when a bucket is at/over 50. Keep writing; a full bucket is a signal to review more urgently, not a reason to lose a real posting.
2. A per-run write budget, still capped at roughly 10 total but split by bucket: something like 3 AI/ML, 3 Fullstack, 3 CyS & Finance, 1 Other — implement as a tunable dict, not hardcoded magic numbers spread through the function; this pacing exists to protect Firecrawl budget and review throughput, independent of the notification question above.
3. Run-record field: when a bucket's post-write count is >= 50, the run record carries an explicit `bucket_at_capacity` list naming which bucket(s). File a GitHub issue the **first time** a given bucket crosses 50 (track "already notified" per bucket in `state/` so it doesn't refile every run — reuse the existing `file_github_issue` pattern, don't build a second notification path) and again if the *global* total (excluding `Viewed/`) crosses 190 or 200 (150/170 stay informational-only in the run log). Since `1 - AI & ML` and `3 - CyS & Finance` are already over 50 as of this writing, the very first run after this ships should file both bucket-crossing issues immediately if the "already notified" state starts empty — expected, not a bug.
4. Do **not** touch `10_Areas/Career/Internships/List/Dossiers MOC.md` in the vault — a live `dataviewjs` capacity table was already added there directly 2026-07-29 (reads real folder counts at render time, no code needs to maintain it). Task A only needs the codebase-side run-log/issue half described above.
5. Keep the existing most-recently-posted-first prioritization within each bucket's per-run allocation — don't replace that logic, just scope it per-bucket instead of globally.
Tests: fixture-based, covering a bucket at exactly 49/50/51 (assert the write still happens at 50/51, only the notification fires), the global total at 189/190/200/201, the per-bucket run-budget split respecting bucket boundaries (a bucket with 0 eligible candidates this run shouldn't consume another bucket's slots), and the "notify once per bucket" state actually suppressing a second issue on a subsequent run where the bucket is still >= 50.

## Task B — CS-relevance gate: Product/rotational/business-analyst roles slip through (real bug, recurring)
`core/relevance.py`'s `_STAGE1_REJECT_RE` has no pattern for product/program management OR business-rotational-program roles — confirmed as a recurring bug class, not a one-off:
- **Databricks** "Product Management Intern (Summer 2027)" (AIJobs source, found 2026-07-26) — the actual role is explicitly PM work ("you will learn how to be a successful PM," "own your project end-to-end — design, build, launch, and iterate on feedback" from a PM's perspective, not an engineer's) despite listing "computer science" as an acceptable major. Passed both stages, classified AI/ML purely because "Machine Learning" appears in a list of Databricks' internal team names, not because the role does ML work.
- **Conagra Brands** "Demand Science Rotational Analyst" (SimplifyJobs, found 2026-07-27, still live in the vault as of this writing at `List/Dossiers/Other/Demand Science Rotational Analyst - Conagra Brands.md`) — a 2-year business rotational program across "Behavioral Science, Demand Forecasting, Data Science, Predictive Science, Demand Planning, Advanced Analytics" with zero programming/software content anywhere in the real posting text; its own stated requirement is "a general understanding of business, financial concepts, and theory behind processes." Passed both stages and landed in `Other` purely because it cleared the CS-relevance gate on no real signal at all (there is no positive software signal in this posting — it should have been rejected by stage 1 or 2, not merely miscategorized).
Add patterns to `_STAGE1_REJECT_RE` catching (word-bounded, same style as existing patterns): "product management intern," "product manager intern," "program management intern," "technical program manager intern," and separately "rotational (analyst|program)," "demand (planning|science) (analyst|rotational)," "business analyst intern" — verify against both real fixtures (Databricks and Conagra dossier files, read them directly from the vault rather than re-fetching) that genuine engineering roles which happen to mention "product" or "rotational" in passing still pass (e.g. "product engineer," "product-focused software engineer," a software-engineering-track rotational program that names actual engineering rotations) — check this distinction explicitly in a test, don't just add blunt keywords.

## Task C — CS-relevance gate: "threat" is too broad a keyword (real bug)
`core/relevance.py`'s cybersecurity-signal matching (feeding into `core/classify.py`'s `_CYS_FINANCE_RE`, which includes bare `threat`) produced a real false positive: Mosaic (The Mosaic Company, agricultural/mining) "Operations & Automation Engineering Co-op/Intern" — a chemical-plant industrial-automation role (PLC/DCS/SCADA controls, requires a Bachelor's in Chemical Engineering, physical labor requirements like lifting and wearing a respirator, "basic computer skills" as a minor bullet) — matched on the word "threat" appearing in a workplace-safety disclaimer ("without posing a direct threat to the safety of his or her own self"), nothing to do with cybersecurity. This should have been rejected by the CS-relevance gate entirely (it's chemical/industrial engineering, not software), not merely misclassified. Two real fixes needed: (1) this listing should fail stage 1 or stage 2 of the relevance gate outright — check whether `_STAGE1_REJECT_RE` needs a pattern for "chemical engineering," "plant operations," "PLC/DCS/SCADA," or whether stage 2's adjacent-field content check should require a *positive* software signal that this posting genuinely lacks (verify against the real fixture: no Python/Java/C++/git/algorithm mentions anywhere in the actual posting text); (2) separately, `_CYS_FINANCE_RE`'s bare `threat` pattern is too permissive regardless — require it to co-occur with a real security-context word (e.g. `threat.{0,30}(model|actor|intelligence|detection)` or similar, built from checking what real cybersecurity postings actually say) rather than matching the bare word anywhere in a page of scraped content, which will false-positive on any posting mentioning workplace safety, insider threats to unrelated things, weather threats, etc.

## Task D — Cross-source dedup misses company-name AND title-string variants (real bug, recurring — four confirmed pairs now)
`cross_source_key()` (`core/identity.py`) keys on normalized company+title, which breaks whenever either string varies across sources for the same real posting. Confirmed recurring, not a one-off — four real duplicate incidents now, two from the original 2026-07-26 audit, two more found 2026-07-29:
- **Aquatic** (vanshb03, Greenhouse token `aquaticcapitalmanagement`) vs **Aquatic Capital Management** (SimplifyJobs) — same company, same role ("Software Engineer Intern"), same Chicago Greenhouse posting in substance. Company-name variant.
- **Google** BS-track Summer 2027 SWE intern reached the vault twice: vanshb03 (`title: "Software Engineering Intern"`) and Freehire (`title: "Software Engineering Intern, BS, Summer 2027"`) — confirmed the exact same job via the identical numeric ID embedded in both URLs (`.../jobs/results/85564713261245126`). Title-string variant, same underlying job ID.
- **Virtu Financial** — a genuine *triple* duplicate, confirmed 2026-07-29: three separate dossiers ("2027 Internship - Software Engineer," "Software Engineer Intern - Software Engineer," "Software Engineer Intern") all point to the exact same URL (`greenhouse.io/virtu/jobs/8624410002`), sourced via Greenhouse/zshah101/vanshb03 with a different title string each time. Same Greenhouse job ID present in all three URLs — this is the strongest evidence yet that a URL/job-ID-based identity check would have caught every one of these four incidents, not just some.
- **Palantir** "Intel" role — confirmed 2026-07-29, a duplicate across two different *buckets*: the same Lever job ID, sourced via SimplifyJobs (landed in `1 - AI & ML`) and zshah101 (landed in `2 - Fullstack`) — same posting classified two different ways depending on which source's copy happened to get matched and classified first. This is a distinct failure mode from the other three (the dossiers aren't just duplicated, they disagree with each other about the posting's own classification) — worth a specific regression test, not just a dedup-count assertion.
Fix: prefer matching on a normalized ATS-derived identity — extract the Greenhouse/Ashby/Lever/Workday job ID or numeric ID embedded in the URL, when present, as a stronger identity signal than company+title text, falling back to the existing normalized-company+title key only when no such ID can be extracted (e.g. sources with no discernible job ID in their URL). This is the more general fix and would have caught all four real incidents above (the original company-name-alias-map idea floated 2026-07-26 would only have caught Aquatic). For the Palantir cross-bucket case specifically: once URL/job-ID matching identifies the duplicate, the write gate should keep the first-source-in-`SOURCES`-order copy (existing tie-break rule, already documented in `validate.py`'s `check_cross_source_duplicate` docstring) — don't add a second, different tie-break rule for the cross-bucket case, the existing one already resolves it correctly once dedup actually catches it.

## Task E — Google's own careers site: content-extraction bug (real, distinct from the earlier Ashby one)
Both Google dossiers sourced via Freehire (BS and MS tracks) contain a scraped Google Careers *search-results listing page* (~20 unrelated job titles — "Regulatory and Litigation Counsel," "Staff Software Developer, Embedded Systems," "Corporate Development Associate," etc. — with a `_arrow_back_ [Back to jobs search]` header and "3,583 jobs matched" line) instead of the specific posting's own detail content. The real posting text *is* present, further down the fetched markdown, but preceded by all that noise — and `classify()` fired on an unrelated listed job's title ("Senior Product Engineer, Machine Learning Accelerators") rather than the actual BS/MS posting content. Investigate `ingestion/posting_page.py`'s handling of `careers.google.com`/`google.com/about/careers` URLs specifically — this is very likely the same class of bug as the earlier Ashby fix (a client-side-rendered page needing a longer `waitFor`, or the fetch landing on a search-results shell before the specific job's content hydrates) but for a different ATS. Fix the extraction; add a regression fixture from the real content captured in this session's audit (both Google dossier files, as they exist right now in the vault, are the real broken-output fixtures — read them directly rather than re-fetching, to guarantee the test reproduces the exact real failure).

## Task F — Degree-requirement content check (new bug class, 2026-07-29)
Real example: **Optiver** "Quantitative Research Intern, PhD" (Greenhouse) — this is the literal same posting manually deleted from the vault once already (matched by Greenhouse job ID `8451781002`), and it resurfaced. Two distinct problems, fix both:
1. **The gate is structurally blind to degree requirements on 5 of this pipeline's 8 sources.** `core/filter.py`'s `degrees_eligible()` only checks a source's own structured `degrees` field, and is permissive (passes) when that field is empty — correct behavior for genuinely unstated cases, but Greenhouse (and most ATS-direct sources) never carry a structured degree field at all, so a PhD-only posting always passes this check regardless of its real content. Add a content-level check, same shape and same permissive-by-default posture as the existing `opt_exclusion()` check in `ingestion/posting_page.py` (runs on fetched posting content, after the write gate's cheap checks, same point OPT is checked): reject only on an explicit "PhD required," "PhD only," "doctoral candidates only," or equivalent phrasing — never on "PhD preferred," never on a degree merely appearing in a list of several acceptable ones (e.g. "Bachelor's, Master's, or PhD" must still pass). Build the pattern from the real Optiver text; check it against the real Bachelor's/Master's-eligible fixtures already in the test suite to confirm zero new false rejections.
2. **A prior manual deletion taught the system nothing** — there is no feedback path from "a human rejected this" back into the gate, so the same wrong match came right back. **Do not build a feedback-loop mechanism for this now** — `20_Progress/Internship/Building System/Research Loop - Improvement Plan.md`'s Priority 4 already covers this exact gap and is deliberately gated on Priority 1 (a real, human-reviewed Applying-note rejection) happening first; that hasn't happened yet, and building the mechanism ahead of real rejection data to design it against would be exactly the kind of speculative-first building this codebase's own history has repeatedly found wasteful. Task F's actual, sufficient fix is #1 above — a real content-level gate that would have caught Optiver honestly the first time, making the "it came back" complaint moot going forward without needing a memory-of-past-rejections system at all.

## Task G — Dossier interlinking (new, per `30_Order/Standards/Internship Notes Standard.md` §1)
Read the standard doc in the vault first — it's the real, concrete spec (written 2026-07-29, previously an empty stub). Implement in `vault_writer/writer.py`'s `build_frontmatter()`:
1. Add a `notes:` list field (YAML list of wikilink strings) to every dossier's frontmatter, always containing `"[[10_Areas/Career/Internships/List/Dossiers MOC]]"`. **Field order, resolved explicitly (the Standard's §1 canonical order — `company, title, url, source, terms, locations, target_year, date_posted, date_found, matched_reason, status, next, tags` — predates this task and doesn't say where `notes` goes):** insert `notes` immediately after `next` and immediately before `tags`, matching where every other evergreen/MOC-style note in this vault places it (check `Dossiers MOC.md` or `Source of Truth.md`'s own frontmatter directly for the real pattern rather than guessing). Update the Standard doc's §1 order line to include `notes` in this position once implemented — the doc should describe the shipped reality, not a stale pre-`notes` list.
2. Add a `company/<slug>` tag to the existing `tags:` list — same slugification as `dossier_filename()`'s existing sanitization (lowercase, spaces→hyphens, strip `\/:*?"<>|`). This is the same-company clustering mechanism (a tag, not a maintained link list — the standard doc explains why: no per-company hub note exists in this vault, and backfilling N-1 existing dossiers on every new same-company arrival is exactly the kind of accumulating write-time cost this codebase avoids everywhere else).
3. **Update `vault_writer/validate.py`'s `REQUIRED_FRONTMATTER_FIELDS` to include `notes`.** This list is the write gate's fail-closed enforcement mechanism (per the Standard's §1: "a field is present even when null/[], never omitted") — adding `notes` to `build_frontmatter()` without also adding it here means the write gate never actually checks for it, silently defeating the point of making it required.
Tests: a dossier's rendered frontmatter contains both the MOC link and a correctly-slugified company tag, in the field position specified above; two dossiers for the same company (varying company-string casing/whitespace) produce the identical tag; a dossier missing `notes` fails `validate.py`'s write gate (confirms the `REQUIRED_FRONTMATTER_FIELDS` update actually took effect, not just that the field renders when present).

## Task H — recheck.py: move to Viewed/, don't delete (new, per Standard §4)
`recheck.py` currently does `Path(r["path"]).unlink()` on a closed posting — replace with a move to `10_Areas/Career/Internships/List/Dossiers/Viewed/` (create the folder if absent). On move:
1. Append `"[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]"` to the dossier's existing `notes:` list (from Task G) — don't replace the MOC/company links already there, a removed dossier's history is still real.
2. Add `removed_date` (today) and `removed_reason` (the existing `reason` string `recheck.py` already computes — `"absent from live feed"` or `"active: false upstream"` — currently discarded once the file's deleted) to frontmatter.
3. Set `status: removed` (every dossier's `status` has been a static `unreviewed` until now — this is the field's first real transition, not a new field being invented).
4. Update `state/dossier_uids.json` (via `vault_writer/writer.py`'s existing `load_dossier_uids`/`save_dossier_uids`) to the new post-move relative path — a stale manifest entry pointing at a file no longer at that path breaks the next `write_dossier()` idempotency check for that uid.
5. `recheck.py`'s existing mass-deletion brake (currently named for delete counts) should apply identically to move counts — same protective logic, don't weaken it just because the operation changed from delete to move.
Tests: a recheck run against a fixture with one closed posting ends with the file present in `Viewed/` (not gone), frontmatter carries all four new/changed fields, and `dossier_uids.json` reflects the new path.

## Task I — Readable, structured dossier body content (new, per Standard §2)
Stay zero-LLM — this is a better deterministic content-structuring pass in `ingestion/posting_page.py`'s `extract_content()`, not a summarizer, per this repo's own hard rule (see the repo's `CLAUDE.md`). Real, observed defects as of 2026-07-29 to fix:
1. **Duplicate-paragraph stripping**: the Conagra fixture (`List/Dossiers/Other/Demand Science Rotational Analyst - Conagra Brands.md`, read it directly) has its entire "About Us" paragraph appearing twice, verbatim. Detect a paragraph (blank-line-delimited block) repeated verbatim later in the same fetch and drop the repeat, keeping the first occurrence.
2. **ATS-chrome line-splitting**: patterns like `locationsChicago, Illinois`, `time typeFull time`, `job requisition idReq-039400` (real, from the same Conagra fixture) are UI labels jammed against their values with no separator — split known label prefixes (`locations`, `time type`, `posted on`, `job requisition id`, `time left to apply`) onto their own line before the free-text body.
3. **Preserve real section structure**: where the source text already states section names (`Responsibilities`, `Qualifications`, `Requirements`, `Benefits`, `Compensation` — bolded or on their own line in the real fetched markdown, check the Appian/Manhattan Associates/Conagra fixtures for the actual shape), render them as `###` headings instead of flattening to one block. Don't invent section boundaries a posting's own text doesn't have.
4. **Strip additional known chrome**: "Read More" truncation markers, repeated "Follow Us"/social-link lists (real example: the Manhattan Associates fixture ends with a duplicated LinkedIn/X/Facebook block).
Tests: fixture-based against the real Conagra and Manhattan Associates dossier content (read directly from the vault, don't re-fetch) — assert no duplicated paragraph survives, assert chrome lines are split, assert a posting with real stated section headers renders them as `###` headings, assert a posting with no internal structure at all stays as one clean block (no invented sections).

## Verification
Run the full test suite, report the exact pass count. Report Tasks A-I individually. For B, C, D, and F specifically, re-run the real fixture cases (Databricks, Conagra, Mosaic, Aquatic/Google/Virtu/Palantir, Optiver) through the fixed code and confirm the expected outcome (reject, reject, reject, correctly-deduped-or-merged, reject) rather than just asserting the regex/logic looks right. For G and H, show the actual rendered frontmatter of a real test dossier before/after. For I, show a real before/after diff of the Conagra fixture's body content. State plainly which tasks were actually run against real data vs. only reviewed for correctness — don't claim a task works if its real fixture case was never actually exercised.

## Claude

I'll start by verifying the assumed-live pieces exist, then read the codebase and the vault standard doc before touching anything.

Confirmed all three assumed-live pieces exist. Let me exclude the venv and get the real project file list, plus find the vault.

Standard doc read. Now let me fetch all the fixture dossier files needed for real-data testing, in parallel.

This is a large 9-task build. Let me set up tracking and read the core files plus real fixtures in parallel.

Now let me pull the real fixture content needed for tasks B, C, D, E, F, I.

Now I have all the real fixtures needed. Time to implement. Starting with Task B & C in `core/relevance.py` and `core/classify.py`.

Now Task C's part in `core/relevance.py` — extending the adjacent-field hint so chemical/industrial roles get content-checked:

Now Task C's `_CYS_FINANCE_RE` fix in `core/classify.py`:

Now Task D — URL/job-ID based cross-source dedup in `core/identity.py`:

Now wire `url` through the two callers — `vault_writer/validate.py` and `run_pipeline.py`:

Now Task F — content-level PhD-only gate in `ingestion/posting_page.py`, plus Task E/I extraction improvements. Let me implement all three together since they share the same file.

Now wire `phd_only_exclusion` into `run_pipeline.py`'s validate_and_write:

Now Tasks E & I — the extraction fixes in `extract_content()`:

Let me run the existing test suite now to catch regressions before continuing further.

All 258 existing tests still pass. Now let's implement Task G (interlinking) in `vault_writer/writer.py` and `vault_writer/validate.py`.

Now update `REQUIRED_FRONTMATTER_FIELDS` in `validate.py`:

Now let me add the `move_dossier_to_viewed` function after `write_dossier`:

Now update `recheck.py` to call this instead of `unlink()`:

Now let's run the tests to check `test_recheck.py` (which only tests `plan_removals`, unaffected) and the full suite:

Now the main body — update the `_prioritize_and_cap` call and add the capacity-notification logic after the write:

Now the `test_run_once_defers_beyond_the_cap...` and `test_run_once_second_run_...` tests:

Now let's create the Google careers fixture file (Task E) using the real captured broken content:

Now append the new test cases at the end of `test_posting_page.py`:

Let's run this new batch of tests before continuing:

All posting_page tests pass. Now let's run the full suite to make sure nothing else regressed:

Now let's add tests for Task B and C in `test_relevance.py`:

Now Task C's classify.py `threat` narrowing test in `test_classify.py`:

The hint check only scans title+company, but Mosaic's chemical/PLC/DCS/SCADA signal lives in the posting *content*. Let me fix that root cause:

All 279 pass. Now let's add Task D tests to `test_identity.py`:

All pass. Now let's add Task G tests to `test_writer.py` and `test_validate.py`, and Task H tests to `test_writer.py`.

Now let's add the tests to `test_writer.py`:

All pass. Now Task G's validate.py test (missing `notes` fails the write gate):

Now let's add Task A tests to `test_run_pipeline.py`:

Now let's append the Task A tests at the end of the file:

Login expired · Please run /login

Login's back. Continuing where I left off — re-running the Task A tests.

All pass. Let's run the full suite now:

All 303 tests pass. Let me mark tasks as complete and do the required verification pass — re-running the real fixtures through the fixed code end-to-end as the prompt demands.

All real-fixture verification confirms correct outcomes: reject, reject, reject, correctly-deduped, reject. Now let's verify Task E (Google careers extraction) and Task I (Conagra/Manhattan body structuring) against the real fixture content directly:

Confirmed: the extraction now correctly skips the listing shell and lands on the real posting content, with no unrelated job titles bleeding through. Now let's verify Task I against the actual real Conagra and Manhattan Associates fixture content (fetched earlier from the vault):

Found a bug — my `_LINK_BULLET_RE` doesn't handle markdown link title syntax (`"LinkedIn"` after the URL). Let me fix it:

Fixed and all 303 tests still pass. Now let's demonstrate Task G/H before/after rendered frontmatter on a real test dossier, as the verification section requires.

Everything works as specified — the `notes:` field is present with the MOC link, the `company/palantir` tag is added, and the move to `Viewed/` correctly appends the Removed MOC link, sets `status: removed`, and adds `removed_date`/`removed_reason`. Now let's run the final full test suite count and check for any remaining issues (e.g., the `run.yml` workflow file that might reference removed dossiers behavior, and double-check `git status`):

Small consistency cleanup — the issue title still says "mass-deletion":

I should also update the Standard doc's §1 order line in the vault per Task G's explicit instruction, since `notes` is now implemented.

The heading is nested one level under the top-level title. Let me patch it correctly:

The Standard doc now reflects the shipped reality with `notes` in the field order. Let's do a final full test run and summarize.

All 303 tests pass (up from 258 baseline — 45 new tests added). Here's the task-by-task report:

## Task-by-task summary

**A — Per-bucket write budget + capacity notification (not a refusal).** `run_pipeline.py`: `MAX_NEW_WRITES_PER_RUN` is now a per-bucket dict (`{"AI/ML": 3, "Fullstack": 3, "CyS & Finance": 3, "Other": 1}`), `_prioritize_and_cap` scopes budget per-bucket so an empty bucket can't donate slots. `count_dossiers_by_bucket()` counts real files; hitting 50 never blocks the write, only adds to `bucket_at_capacity` in the run record and files one GitHub issue per bucket the first time it crosses 50 (tracked in `state/capacity_notified.json`, not refiled on subsequent runs). Global total crossing 190/200 also files an issue; 150/170 are log-only. Tested at 48/49/50 (write always happens, notification only at ≥50), global at 189/190/200, per-bucket isolation, and "notify once" suppression across two runs.

**B — Product/rotational reject patterns.** Added to `core/relevance.py`'s `_STAGE1_REJECT_RE` + a new `_ROTATIONAL_ANALYST_RE` with negative lookbehind so an engineering-track rotational program still passes. **Verified against real data**: Databricks "Product Management Intern" → rejects; Conagra "Demand Science Rotational Analyst" → rejects; a constructed "Software Engineering Rotational Program Intern" still passes.

**C — 'threat' narrowed + Mosaic-class reject.** `classify.py`'s `_CYS_FINANCE_RE` now requires `threat` to co-occur with `model|actor|intelligence|detection`. `relevance.py`'s adjacent-field hint extended to chemical/industrial/PLC/DCS/SCADA, and (root-cause fix) the hint check now also scans posting content, not just title+company, since Mosaic's chemical signal only appears in the fetched body. **Verified**: real Mosaic content → `stage2_confirm` is `False`, `classify` no longer fires on the safety-disclaimer "threat".

**D — URL/job-ID cross-source dedup.** `core/identity.py` gained `extract_ats_job_id()` (Greenhouse/Lever/Ashby/Google-careers patterns) and `cross_source_key()` now prefers the job ID over normalized text, falling back when no ID is extractable. Wired through `validate.py` and `run_pipeline.py`. **Verified against all four real incidents**: Virtu's triple-duplicate collapses to 1 key, Google BS/MS variant collapses, Palantir's cross-bucket duplicate collapses, Aquatic's name-variant still collapses (via the URL, which both share).

**E — Google careers extraction bug.** Added `_LISTING_SHELL_RESET_RE` to `extract_content()`: on hitting a listing-shell marker (`Back to jobs search`, `N jobs matched`, pagination), it discards everything gathered and waits for the next real heading. **Verified**: real captured Google fixture now extracts the actual MS-track posting with zero unrelated job titles bleeding through.

**F — Content-level degree gate.** New `phd_only_exclusion()` in `posting_page.py`, same permissive-by-default shape as `opt_exclusion()`, wired into `run_pipeline.py` as a `degree_eligibility` rejection. **Verified**: real Optiver text → rejects; real Aquatic/Appian/Manhattan Bachelor's-or-Master's-eligible text → zero false rejections.

**G — Dossier interlinking.** `build_frontmatter()` now emits `notes: [Dossiers MOC link]` and a `company/<slug>` tag, in the position specified; `REQUIRED_FRONTMATTER_FIELDS` updated so the write gate actually enforces it. Also updated the Standard doc's own §1 order line in the vault to describe shipped reality. Shown before/after on a real test dossier above.

**H — recheck.py moves to Viewed/.** New `move_dossier_to_viewed()` in `writer.py`: appends the Removed MOC link (keeping the original), sets `status: removed`, adds `removed_date`/`removed_reason`, updates `dossier_uids.json`. `recheck.py` calls it instead of `unlink()`; mass-move brake logic unchanged. Shown before/after above.

**I — Structured body content.** `extract_content()` now dedupes repeated paragraph lines, splits ATS label run-ons onto their own line, promotes real bolded section names to `###` headings (narrow — only canonical keywords), and strips Read More/Follow Us social chrome (fixed a link-title-syntax bug I introduced and caught via the real Manhattan fixture). Verified via before/after diffs above using the real Conagra and Manhattan Associates content.

All nine tasks were exercised against real fixture data, not just reviewed for correctness — the two exceptions worth flagging are Task A's GitHub issue-filing (correct by test, but `gh` itself isn't invoked in tests, consistent with how `test_file_github_issue_calls_gh_with_expected_args` already handles this) and Task E's fixture, which is a hand-transcribed subset of the real captured markdown rather than a live re-fetch (per the prompt's instruction to use the existing broken vault content, not re-fetch).

Nothing has been committed — say the word if you want this committed (and optionally run `/review-loop-change` first, per this repo's convention for core/ingestion/vault_writer changes).

**Tool calls:**

- `Bash` — `echo "=== relevance.py ===" && grep -n "def stage1_reject\|def stage2_confirm" core/relevance.py && echo "=== classify.py ===" && grep -n "def classify\|BUCKET_FOLDERS" core/classify.py && echo "=== writer.py priority routing ===" && grep -n "priority\|BUCKET_FOLDERS\|def build_frontmatter\|def write_dossier\|def load_dossier_uids\|def save_dossier_uids" vault_writer/writer.py`
  ```
=== relevance.py ===
56:def stage1_reject(title: str, raw_text: str) -> bool:
89:def stage2_confirm(title: str, company: str, posting_content: str) -> bool:
=== classify.py ===
18:BUCKET_FOLDERS = {
49:def classify(title: str, category: str, posting_content: str) -> tuple:
=== writer.py priority routing ===
48:def build_frontmatter(listing, uid: str, date_found: str, matched_reason: str) -> dict:
112:def load_dossier_uids(state_dir) -> dict:
119:def save_dossier_uids(state_dir, manifest: dict) -> None:
127:    checkout — recursively, across the flat legacy root and every priority-
144:def write_dossier(vault_root, uid: str, markdown: str, role: str, company: str, bucket_folder: str,
147:    priority-bucket subfolder. Idempotent on uid: if state_dir's manifest
  ```
- `Bash` — `find . -type f -name "*.py" | grep -v __pycache__ | sort`
  ```
<persisted-output>
Output too large (70KB). Full output saved to: /home/anant_gupta/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/tool-results/boarhpnl0.txt

Preview (first 2KB):
./.venv/lib/python3.12/site-packages/_pytest/__init__.py
./.venv/lib/python3.12/site-packages/_pytest/_argcomplete.py
./.venv/lib/python3.12/site-packages/_pytest/_code/__init__.py
./.venv/lib/python3.12/site-packages/_pytest/_code/code.py
./.venv/lib/python3.12/site-packages/_pytest/_code/source.py
./.venv/lib/python3.12/site-packages/_pytest/_io/__init__.py
./.venv/lib/python3.12/site-packages/_pytest/_io/pprint.py
./.venv/lib/python3.12/site-packages/_pytest/_io/saferepr.py
./.venv/lib/python3.12/site-packages/_pytest/_io/terminalwriter.py
./.venv/lib/python3.12/site-packages/_pytest/_io/wcwidth.py
./.venv/lib/python3.12/site-packages/_pytest/_py/__init__.py
./.venv/lib/python3.12/site-packages/_pytest/_py/error.py
./.venv/lib/python3.12/site-packages/_pytest/_py/path.py
./.venv/lib/python3.12/site-packages/_pytest/_version.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/__init__.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/_compare_any.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/_compare_mapping.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/_compare_sequence.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/_compare_set.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/_guards.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/_typing.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/compare_text.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/highlight.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/truncate.py
./.venv/lib/python3.12/site-packages/_pytest/assertion/util.py
./.venv/lib/python3.12/site-packages/_pytest/cacheprovider.py
./.venv/lib/python3.12/site-packages/_pytest/capture.py
./.venv/lib/python3.12/site-packages/_pytest/compat.py
./.venv/lib/python3.12/site-packages/_pytest/config/__init__.py
./.venv/lib/python3.12/site-packages/_pytest/config/argparsing.py
...
</persisted-output>
  ```
- `Bash`:
  ```bash
find . -type f -name "*.py" -not -path "./.venv/*" | sort
echo "---"
find / -maxdepth 4 -iname "*jarvis*" -type d 2>/dev/null
find $HOME -maxdepth 3 -iname "*vault*" -type d 2>/dev/null
find $HOME/projects -maxdepth 2 -type d 2>/dev/null
  ```
  ```
./core/classify.py
./core/filter.py
./core/git_ops.py
./core/identity.py
./core/relevance.py
./core/run_log.py
./core/schema_drift.py
./enrich.py
./grade_resume.py
./ingestion/freehire.py
./ingestion/normalize.py
./ingestion/posting_page.py
./ingestion/sources.py
./recheck.py
./run_pipeline.py
./tests/test_classify.py
./tests/test_enrich.py
./tests/test_filter.py
./tests/test_freehire.py
./tests/test_git_ops.py
./tests/test_grade_resume.py
./tests/test_identity.py
./tests/test_posting_page.py
./tests/test_recheck.py
./tests/test_relevance.py
./tests/test_run_log.py
./tests/test_run_pipeline.py
./tests/test_schema_drift.py
./tests/test_sources.py
./tests/test_validate.py
./tests/test_writer.py
./vault_writer/validate.py
./vault_writer/writer.py
---
/home/anant_gupta/projects
/home/anant_gupta/projects/hub
/home/anant_gupta/projects/work
/home/anant_gupta/projects/.vscode
/home/anant_gupta/projects/scratch
/home/anant_gupta/projects/umn
/home/anant_gupta/projects/ai
/home/anant_gupta/projects/hackathon
/home/anant_gupta/projects/hub/tradingview
/home/anant_gupta/projects/hub/CausalOps
/home/anant_gupta/projects/hub/GymMangment_app_demo
/home/anant_gupta/projects/hub/portfolio
/home/anant_gupta/projects/hub/DNA_BJJ_APP
/home/anant_gupta/projects/hub/Assisto_website
/home/anant_gupta/projects/hub/Learning-Tracker-Tool
/home/anant_gupta/projects/work/internship-research-loop
/home/anant_gupta/projects/work/gupta-builds
/home/anant_gupta/projects/umn/boom
/home/anant_gupta/projects/ai/lovable
/home/anant_gupta/projects/ai/claude
/home/anant_gupta/projects/ai/jan
/home/anant_gupta/projects/hackathon/opspilot-placeholder-backup
/home/anant_gupta/projects/hackathon/safereach
/home/anant_gupta/projects/hackathon/Resq
/home/anant_gupta/projects/hackathon/opspilot
  ```
- `ToolSearch` — `{"query":"select:mcp__jarvis__vault_read,mcp__jarvis__vault_list","max_results":5}`
- `mcp__jarvis__vault_read` — `{"path":"30_Order/Standards/Internship Notes Standard.md"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers/Other"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers/1 - AI & ML"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers/2 - Fullstack"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance"}`
- `TaskCreate` — `{"tasks":"[{\"subject\":\"Task B - product/rotational reject patterns\",\"body\":\"Add stage1 reject patterns for PM/rotational roles in core/relevance.py; verify against Databricks/Conagra text\",\"status\":\"pending\"},{\"subject\":\"Task C - narrow 'threat' keyword + reject Mosaic-class\",\"body\":\"core/relevance.py + core/classify.py _CYS_FINANCE_RE threat context requirement\",\"status\":\"pending\"},{\"subject\":\"Task D - URL/job-ID based cross-source dedup\",\"body\":\"core/identity.py cross_source_key prefer ATS job ID from URL\",\"status\":\"pending\"},{\"subject\":\"Task F - content-level degree gate\",\"body\":\"ingestion/posting_page.py PhD-required check, same shape as opt_exclusion\",\"status\":\"pending\"},{\"subject\":\"Task E - Google careers site extraction fix\",\"body\":\"ingestion/posting_page.py fix waitFor/extraction for careers.google.com\",\"status\":\"pending\"},{\"subject\":\"Task I - structured body content\",\"body\":\"ingestion/posting_page.py extract_content: dedupe paragraphs, split ATS chrome, section headings, strip chrome\",\"status\":\"pending\"},{\"subject\":\"Task G - dossier interlinking (notes field, company tag)\",\"body\":\"vault_writer/writer.py build_frontmatter + validate.py REQUIRED_FRONTMATTER_FIELDS\",\"status\":\"pending\"},{\"subject\":\"Task H - recheck.py move to Viewed/ not delete\",\"body\":\"recheck.py + writer.py uid manifest update\",\"status\":\"pending\"},{\"subject\":\"Task A - per-bucket write budget + capacity notification\",\"body\":\"run_pipeline.py MAX_NEW_WRITES_PER_RUN split by bucket, capacity issue filing\",\"status\":\"pending\"},{\"subject\":\"Run full test suite + report\",\"body\":\"Final verification per task's Verification section\",\"status\":\"pending\"}]"}`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/relevance.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/classify.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/identity.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/filter.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/Other/Demand Science Rotational Analyst - Conagra Brands.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/A.I. Developer Co-Op (Boston, MA) - Manhattan Associates.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/Other/Software Engineering Intern, Summer 2027 - Google.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Software Engineering Intern, MS, Summer 2027 - Google.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Quantitative Research Intern, PhD (Summer 2027) - Optiver.md"}`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_posting_page.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_relevance.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_classify.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_validate.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_recheck.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/normalize.py`
- `Bash`:
  ```bash
cat /home/anant_gupta/projects/work/internship-research-loop/vault_writer/templates/dossier.md.j2
echo "---FIXTURES---"
ls /home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/
echo "---THROWAWAY VAULT---"
find /home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/throwaway_vault -maxdepth 5
echo "---run_log.py---"
cat /home/anant_gupta/projects/work/internship-research-loop/core/run_log.py
echo "---profile.yaml---"
cat /home/anant_gupta/projects/work/internship-research-loop/core/profile.yaml 2>/dev/null || cat /home/anant_gupta/projects/work/internship-research-loop/profile.yaml 2>/dev/null
  ```
  ```
---
{{ frontmatter_yaml }}---
# {{ title }}
{% if posting_content -%}
Found {{ date_found }} via {{ source }}.
{% if classification_callout -%}
{{ classification_callout }}
{% endif -%}
## Posting (fetched {{ date_found }})
{{ posting_content }}
{%- else -%}
Found {{ date_found }} via {{ source }}. No posting content fetched.
{% if classification_callout -%}
{{ classification_callout }}
{% endif -%}
{%- endif %}
---FIXTURES---
freehire.json
josegael.json
posting_ashby_ctgt.md
posting_fiverings.md
simplifyjobs.json
throwaway_vault
vanshb03.json
zshah101.json
---THROWAWAY VAULT---
/home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/throwaway_vault
/home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/throwaway_vault/10_Areas
/home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/throwaway_vault/10_Areas/Career
/home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/throwaway_vault/10_Areas/Career/Internships
/home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/throwaway_vault/10_Areas/Career/Internships/List
/home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/throwaway_vault/10_Areas/Career/Internships/List/Dossiers
---run_log.py---
"""Two-tier run log per the plan: raw per-run JSONL in this repo, a weekly
markdown rollup appended (never rewritten) into the Jarvis vault.
"""
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

ROLLUP_WEEKDAY = 6  # Sunday (datetime.weekday(): Monday=0 .. Sunday=6)
ROLLUP_HOUR = 23  # UTC, matches the hourly cron


def append_run_log(runs_jsonl_path, record: dict) -> None:
    path = Path(runs_jsonl_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(json.dumps(record) + "\n")


def load_recent_runs(runs_jsonl_path, since: datetime) -> list:
    path = Path(runs_jsonl_path)
    if not path.exists():
        return []
    records = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        record = json.loads(line)
        ts = datetime.fromisoformat(record["timestamp"].replace("Z", "+00:00"))
        if ts >= since:
            records.append(record)
    return records


def should_run_weekly_rollup(now: datetime) -> bool:
    return now.weekday() == ROLLUP_WEEKDAY and now.hour == ROLLUP_HOUR


def format_weekly_rollup(records: list, week_start: datetime, week_end: datetime) -> str:
    written = sum(r.get("written_count", 0) for r in records)
    halted = sum(1 for r in records if r.get("halted"))
    reason_counts = Counter(
        rej.get("check", "unknown") for r in records for rej in r.get("rejections", [])
    )
    reasons_str = ", ".join(f"{k}: {v}" for k, v in sorted(reason_counts.items())) or "none"
    date_fmt = "%Y-%m-%d"
    return (
        f"- **{week_start.strftime(date_fmt)} to {week_end.strftime(date_fmt)}**: "
        f"{written} dossiers written, {sum(reason_counts.values())} rejections ({reasons_str}), "
        f"{halted} halted run(s), {len(records)} run(s) total"
    )


_HEADER_TEMPLATE = """---
type: dashboard
status: active
created: {created}
tags:
  - internship
  - automation
  - run-log
---
# Internship Research Loop — Run Log
Weekly rollup from the internship-research-loop automation, appended automatically — not rewritten. Raw per-run data lives in that repo's logs/runs.jsonl.
"""


def append_weekly_rollup(run_log_md_path, line: str, created_date: str) -> None:
    path = Path(run_log_md_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        header = _HEADER_TEMPLATE.format(created=created_date).rstrip("\n") + "\n"
        path.write_text(header + line + "\n")
        return
    existing = path.read_text()
    if not existing.endswith("\n"):
        existing += "\n"
    path.write_text(existing + line + "\n")
---profile.yaml---
# Layer 2 filter config — see Research Loop Implementation Plan for rationale.
grad_year: 2028
class_year: junior
eligible_class_tags: [Junior, "3rd year"]  # matched as case-insensitive substrings against target_year entries
accept_unrestricted: true  # postings with no class-year field at all still match
# "Winter 2027" = Dec 2026-Feb 2027 in SimplifyJobs' taxonomy — winters are
# labeled by the LATER year, confirmed 2026-07-18 by term adjacency in live data
# (three real listings co-tag ["Fall 2026", "Winter 2027"]). Postings don't
# publish actual months in the feed, so the human screen of the fetched posting
# content is still what confirms a genuine Dec-Jan window per posting.
terms: ["Summer 2027", "Winter 2027", "Spring 2027"]
# Summer/Winter 2027 are equally top priority; Spring 2027 is wanted but
# explicitly lower priority. This is a weight, not a second pass/fail gate —
# Spring 2027 still matches like any other wanted term today. A later, separate
# task consumes this for priority tagging; this one only makes it present and
# readable downstream.
terms_weight: {"Summer 2027": "high", "Winter 2027": "high", "Spring 2027": "low"}
# Real category values observed on SimplifyJobs/Summer2026-Internships (dev/.github/scripts/listings.json),
# not the generic names in the original transcript — confirmed by fetching live data 2026-07-16.
categories: ["Software", "Software Engineering", "AI/ML/Data", "Data Science, AI & Machine Learning"]
# Fellowship/research/mentorship-shaped entries were checked against live data
# 2026-07-26 (SimplifyJobs, JGCL, zshah101 feeds + 5 Greenhouse/5 Ashby seeded
# company boards): real examples exist (e.g. SimplifyJobs "Oracle Database
# Research Intern" category=Software terms includes Winter/Spring 2027; JGCL
# "CBAI Summer Research Fellowship in AI Safety '26" category=Research; JGCL
# "Anthropic Fellows Program" category=Program; zshah101 "Research Intern -
# School of Computer Science - LTI" (CMU) category=Software) — but every one
# already matches under the existing rules: SimplifyJobs/zshah101 tag them
# with a category already in categories/_ZSHAH101_CATEGORIES above, and JGCL's
# matcher never gates on category at all. No fellowship/mentorship-shaped hits
# turned up on the seeded Greenhouse/Ashby boards, and those two sources are
# free-text term matching with no category gate to begin with. No matching
# code needed — nothing here to extend yet.
#
# Pay is never a filter criterion anywhere in this pipeline — confirmed
# 2026-07-26 by grepping core/filter.py for any pay/pay_per_week gate; none
# exists. Don't add one; compensation is out of scope for Layer 2 eligibility.
# Rejects a SimplifyJobs listing outright if any of these terms are present, even
# alongside an allowed term (multi-term/rotational postings spanning both cycles).
exclude_terms: ["Summer 2026", "Fall 2026", "Spring 2026"]
# Rule built 2026-07-17 from live feed data (1216 distinct location strings), not
# guessed — see location_eligible() in core/filter.py. Permissive: no location
# data or ambiguous strings ('Multiple Locations', 'Virtual', bare 'Remote') still
# match; only affirmatively non-US listings (Canada/UK/'Remote in Germany') drop.
locations_allow: us_remote
# Real live values use the apostrophe form ("Bachelor's" 5450, ("Master's","PhD")
# 592, ("PhD",) 586, empty 4676 — fetched 2026-07-18). Permissive: empty degrees
# data passes; non-empty must intersect this list.
degrees_allow: ["Bachelor's"]
  ```
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/2027 Internship - Software Engineer - Virtu Financial.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Software Engineer Intern - Software Engineer - Virtu Financial.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Software Engineer Intern - Virtu Financial.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Forward Deployed Software Engineer Intern - Intel - Palantir.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/2 - Fullstack/Forward Deployed Software Engineer, Internship - Intel - Palantir.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance/Software Engineer Intern - Aquatic Capital Management.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Software Engineering Intern - Appian.md"}`
- `Bash` — `grep -n "threat" tests/*.py core/*.py; echo "---"; grep -rn "cross_source_key" --include=*.py .`
  ```
core/classify.py:37:    r"|penetration test|infosec|threat|vulnerability|quant(itative)? developer"
---
vault_writer/validate.py:10:from core.identity import cross_source_key
vault_writer/validate.py:74:    key = cross_source_key(listing.company, listing.title)
tests/test_identity.py:6:from core.identity import compute_uid, cross_source_key
tests/test_identity.py:51:def test_cross_source_key_normalizes_case_and_whitespace():
tests/test_identity.py:52:    assert cross_source_key("MLH (Major League Hacking)", "MLH Fellowship") == \
tests/test_identity.py:53:        cross_source_key("  mlh (major league hacking)", "mlh   fellowship ")
tests/test_identity.py:54:    assert cross_source_key("MLH", "Fellowship") != cross_source_key("MLH", "Other Program")
run_pipeline.py:28:from core.identity import cross_source_key
run_pipeline.py:161:        cross_source_key(fm.get("company", ""), fm.get("title", "")) for fm in scan_dossiers(jarvis_dir)
run_pipeline.py:214:        dossier_keys.add(cross_source_key(listing.company, listing.title))
tests/test_run_pipeline.py:459:def test_cross_source_key_punctuation_insensitive_marmon_case():
tests/test_run_pipeline.py:462:    from core.identity import cross_source_key
tests/test_run_pipeline.py:463:    assert cross_source_key("Marmon Holdings", "Data Engineering Intern Co-op") == \
tests/test_run_pipeline.py:464:        cross_source_key("Marmon Holdings", "Data Engineering Intern/Co-op")
core/identity.py:7:cross_source_key() is the secondary dedup identity: the same program listed
core/identity.py:19:def cross_source_key(company: str, title: str) -> str:
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/relevance.py`
  ```diff
  - _STAGE1_REJECT_RE = re.compile(
    r"\b(financial analyst|risk analyst|performance analyst"
    r"|tax (associate|preparer|accountant)"
    r"|investor relations"
    r"|sports performance (analyst|analytics)|academy performance (analyst|analysis)"
    r"|human resources intern|hr intern|marketing intern|business development intern)\b",
    re.I,
)
  + # Product/program-management and business-rotational patterns added 2026-07-29
# from two real recurring incidents: Databricks "Product Management Intern
# (Summer 2027)" (AIJobs, found 2026-07-26 — explicitly PM work, "learn how to
# be a successful PM," despite listing "computer science" as an acceptable
# major, and classified AI/ML only because "Machine Learning" is one of
# Databricks' internal team names, not because the role does ML work) and
# Conagra Brands "Demand Science Rotational Analyst" (SimplifyJobs,
# 2026-07-27, still live at List/Dossiers/Other/ as of this writing — a 2-year
# business rotational program across Behavioral Science/Demand
# Forecasting/Demand Planning/Advanced Analytics with zero programming
# content; its own stated requirement is "a general understanding of
# business, financial concepts, and theory behind processes"). The rotational
# pattern requires "rotational" not be immediately preceded by "engineering "/
# "software " so a genuine software-engineering-track rotational program still
# passes (checked explicitly in tests/test_relevance.py).
_ROTATIONAL_ANALYST_RE = re.compile(
    r"(?<!engineering )(?<!software )\brotational (analyst|program)\b", re.I,
)
_STAGE1_REJECT_RE = re.compile(
    r"\b(financial analyst|risk analyst|performance analyst"
    r"|tax (associate|preparer|accountant)"
    r"|investor relations"
    r"|sports performance (analyst|analytics)|academy performance (analyst|analysis)"
    r"|human resources intern|hr intern|marketing intern|business development intern"
    r"|product management intern|product manager intern"
    r"|program management intern|technical program manager intern"
    r"|demand (planning|science) (analyst|rotational)"
    r"|business analyst intern)\b",
    re.I,
)
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/relevance.py`
  ```diff
  - def stage1_reject(title: str, raw_text: str) -> bool:
    """True if this listing's title/raw_text is unambiguously non-software —
    reject without ever fetching the page."""
    return bool(_STAGE1_REJECT_RE.search(f"{title} {raw_text}"))
  + def stage1_reject(title: str, raw_text: str) -> bool:
    """True if this listing's title/raw_text is unambiguously non-software —
    reject without ever fetching the page."""
    haystack = f"{title} {raw_text}"
    return bool(_STAGE1_REJECT_RE.search(haystack)) or bool(_ROTATIONAL_ANALYST_RE.search(haystack))
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/relevance.py`
  ```diff
  - _ADJACENT_FIELD_COMPANY_HINT_RE = re.compile(
    r"\b(space|aerospace|robotics|astro|satellite|defense|automotive|firmware"
    r"|embedded|hardware)\b", re.I,
)
  + # chemical/plant/PLC-DCS-SCADA added 2026-07-29: real false-positive, Mosaic
# (The Mosaic Company, agricultural/mining) "Operations & Automation
# Engineering Co-op/Intern" — a chemical-plant industrial-automation role
# (PLC/DCS/SCADA controls, Bachelor's in Chemical Engineering required,
# physical labor requirements, "basic computer skills" as a minor bullet)
# passed stage 2 unconditionally because neither "chemical" nor "automation"
# hit the old hint list, so its content (no Python/Java/C++/git/algorithm
# anywhere) was never checked at all — it only got flagged downstream by
# classify.py's now-fixed bare-'threat' match on an unrelated workplace-safety
# disclaimer. Adding these hints routes it through the real software-signal
# content check below, which correctly rejects it.
_ADJACENT_FIELD_COMPANY_HINT_RE = re.compile(
    r"\b(space|aerospace|robotics|astro|satellite|defense|automotive|firmware"
    r"|embedded|hardware|chemical|industrial|plant operations|\bplc\b|\bdcs\b|\bscada\b)\b", re.I,
)
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/classify.py`
  ```diff
  - _CYS_FINANCE_RE = re.compile(
    r"\b(security engineer|cybersecurity|application security|appsec"
    r"|penetration test|infosec|threat|vulnerability|quant(itative)? developer"
    r"|quantitative (research|trading)|trading systems?|fintech|risk engine"
    r"|payments? (engineer|infrastructure)|blockchain|crypto|defi)\b", re.I,
)
  + # 'threat' narrowed 2026-07-29: real false positive, Mosaic Company
# "Operations & Automation Engineering Co-op/Intern" (chemical-plant
# PLC/DCS/SCADA role, zero cybersecurity content) matched bare 'threat' on a
# workplace-safety disclaimer ("without posing a direct threat to the safety
# of his or her own self"). Requiring co-occurrence with a real
# security-context word within 30 chars catches genuine cybersecurity usage
# ("threat model", "threat actor", "threat intelligence", "threat detection")
# without matching safety-boilerplate/weather/insider-threat-to-unrelated-
# things mentions of the bare word.
_CYS_FINANCE_RE = re.compile(
    r"\b(security engineer|cybersecurity|application security|appsec"
    r"|penetration test|infosec|threat.{0,30}(model|actor|intelligence|detection)|vulnerability"
    r"|quant(itative)? developer"
    r"|quantitative (research|trading)|trading systems?|fintech|risk engine"
    r"|payments? (engineer|infrastructure)|blockchain|crypto|defi)\b", re.I,
)
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/identity.py`
  ```diff
  - """Layer 3 — stable dedup keys for a Listing.

Both remaining sources carry a stable upstream id, so the uid is simply
source:raw_id. (The content-hash fallback existed only for zapplyjobs,
removed as a source 2026-07-18.)

cross_source_key() is the secondary dedup identity: the same program listed
by two different sources gets two different uids but one company+title key.
"""
import re


def compute_uid(listing) -> str:
    if not listing.raw_id:
        raise ValueError(f"listing from {listing.source} has no upstream id: {listing.company!r}")
    return f"{listing.source}:{listing.raw_id}"


def cross_source_key(company: str, title: str) -> str:
    # Punctuation-insensitive: "Intern Co-op" and "Intern/Co-op" are the same
    # posting (real Marmon dup that slipped past a whitespace-only key,
    # caught in the 2026-07-18 dossier audit).
    norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return f"{norm(company)}|{norm(title)}"
  + """Layer 3 — stable dedup keys for a Listing.

Both remaining sources carry a stable upstream id, so the uid is simply
source:raw_id. (The content-hash fallback existed only for zapplyjobs,
removed as a source 2026-07-18.)

cross_source_key() is the secondary dedup identity: the same program listed
by two different sources gets two different uids but one cross-source key.
"""
import re

# Real, confirmed 2026-07-29 — four real duplicate incidents the old
# normalized-company+title key missed because either string varied across
# sources: Aquatic vs Aquatic Capital Management (company-name variant),
# Google BS/MS Summer 2027 SWE intern (title-string variant, same numeric job
# id in both URLs), Virtu Financial's genuine triple duplicate (three
# different title strings, identical greenhouse.io/virtu/jobs/8624410002 URL
# across SimplifyJobs/zshah101/vanshb03), and Palantir's "Intel" FDSE role
# duplicated across two different buckets (same Lever job id via SimplifyJobs
# and zshah101). A URL-embedded ATS job id is a stronger identity signal than
# company+title text in every one of these — extract it when present, fall
# back to the normalized-text key only when the URL carries no recognizable id.
_ATS_JOB_ID_PATTERNS = (
    re.compile(r"greenhouse\.io/[^/]+/jobs/(\d+)", re.I),
    re.compile(r"lever\.co/[^/]+/([0-9a-f-]{36})", re.I),
    re.compile(r"ashbyhq\.com/[^/]+/([0-9a-f-]{36})", re.I),
    # Google's own careers site embeds a long numeric id after .../jobs/results/
    re.compile(r"careers/(?:applications/)?jobs/results/(\d+)", re.I),
)


def extract_ats_job_id(url: str) -> str:
    """The ATS-native job id embedded in url, or None if url is from a
    source/ATS with no recognizable id in its URL shape (e.g. Freehire's
    Telegram links, Workday's slug-only URLs)."""
    for pattern in _ATS_JOB_ID_PATTERNS:
        m = pattern.search(url or "")
        if m:
            return m.group(1)
    return None


def compute_uid(listing) -> str:
    if not listing.raw_id:
        raise ValueError(f"listing from {listing.source} has no upstream id: {listing.company!r}")
    return f"{listing.source}:{listing.raw_id}"


def cross_source_key(company: str, title: str, url: str = "") -> str:
    job_id = extract_ats_job_id(url)
    if job_id:
        return f"jobid:{job_id}"
    # Punctuation-insensitive: "Intern Co-op" and "Intern/Co-op" are the same
    # posting (real Marmon dup that slipped past a whitespace-only key,
    # caught in the 2026-07-18 dossier audit).
    norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return f"{norm(company)}|{norm(title)}"
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py`
  ```diff
  -     key = cross_source_key(listing.company, listing.title)
  +     key = cross_source_key(listing.company, listing.title, listing.url)
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -     dossier_keys = {
        cross_source_key(fm.get("company", ""), fm.get("title", "")) for fm in scan_dossiers(jarvis_dir)
    }
  +     dossier_keys = {
        cross_source_key(fm.get("company", ""), fm.get("title", ""), fm.get("url", ""))
        for fm in scan_dossiers(jarvis_dir)
    }
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -         dossier_keys.add(cross_source_key(listing.company, listing.title))
  +         dossier_keys.add(cross_source_key(listing.company, listing.title, listing.url))
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py`
  ```diff
  - def opt_exclusion(text: str):
    """The matched exclusion phrase, or None if the posting shows no explicit
    negative signal (permissive default, like every other filter here)."""
    m = OPT_EXCLUSION_RE.search(text)
    return m.group(0) if m else None
  + def opt_exclusion(text: str):
    """The matched exclusion phrase, or None if the posting shows no explicit
    negative signal (permissive default, like every other filter here)."""
    m = OPT_EXCLUSION_RE.search(text)
    return m.group(0) if m else None


# Built from the real Optiver "Quantitative Research Intern, PhD (Summer
# 2027)" posting (Greenhouse job id 8451781002 — the same posting manually
# deleted from the vault once already, then resurfaced, 2026-07-29): its
# structured degrees field is empty (Greenhouse carries none), so
# core/filter.py's degrees_eligible() waved it through on missing-data
# permissiveness. Its real content states the requirement as "Currently
# enrolled in a PhD program in Statistics, Computer Science, ..." rather than
# a blunt "PhD required" — the enrolled-in/pursuing-a-phd-program phrasing is
# the literal shape this real posting uses, so it's included as an explicit
# equivalent alongside "PhD required"/"PhD only"/"doctoral candidates only".
# Permissive by default like every other gate here: never fires on "PhD
# preferred", and the window guard below never fires when a Bachelor's/
# Master's is also named nearby (checked against the real Aquatic Capital
# Management, Appian, and Manhattan Associates postings, all of which list
# PhD only as one of several acceptable degrees and must keep passing).
_PHD_ONLY_RE = re.compile(
    r"\bphd\s+(?:is\s+)?(?:required|only)\b"
    r"|\bdoctoral candidates?\s+only\b"
    r"|\b(?:currently\s+)?(?:enrolled in|pursuing)\s+an?\s+(?:phd|doctoral)\s+(?:program|degree)\b",
    re.I,
)


def phd_only_exclusion(text: str):
    """The matched PhD-exclusivity phrase, or None if the posting shows no
    explicit signal that only PhD candidates are eligible. Never fires when a
    Bachelor's/Master's is also named near the match — that's a posting
    listing PhD as one of several acceptable degrees, not a PhD-only one."""
    m = _PHD_ONLY_RE.search(text)
    if not m:
        return None
    window = text[max(0, m.start() - 80): m.end() + 80]
    if re.search(r"bachelor|master|\bbs\b|\bms\b", window, re.I):
        return None
    return m.group(0)
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - from ingestion.posting_page import extract_content, fetch_posting_markdown, opt_exclusion
  + from ingestion.posting_page import extract_content, fetch_posting_markdown, opt_exclusion, phd_only_exclusion
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -                 opt_signal = opt_exclusion(page_md)
                if opt_signal:
                    opt_cache[uid] = {"verdict": "excluded", "signal": opt_signal, "checked": date_found}
                    rejections.append({"uid": uid, "check": "opt_eligibility", "reason": opt_signal})
                    continue
                opt_cache[uid] = {"verdict": "eligible", "signal": None, "checked": date_found}
  +                 opt_signal = opt_exclusion(page_md)
                if opt_signal:
                    opt_cache[uid] = {"verdict": "excluded", "signal": opt_signal, "checked": date_found}
                    rejections.append({"uid": uid, "check": "opt_eligibility", "reason": opt_signal})
                    continue
                degree_signal = phd_only_exclusion(page_md)
                if degree_signal:
                    rejections.append({"uid": uid, "check": "degree_eligibility", "reason": degree_signal})
                    continue
                opt_cache[uid] = {"verdict": "eligible", "signal": None, "checked": date_found}
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py`
  ```diff
  - _NOISE = re.compile(
    r"^(\[?!\[|\[back to jobs|\[apply\]|apply\b|select\.\.\.|✱|.*✱\s*$|resume/cv|full name|email\b"
    r"|phone\b|current location|current company|linkedin url|github url|portfolio url|loading$"
    r"|no location found|couldn't auto-read|analyzing resume|success!$|file exceeds|-{3,}$"
    r"|cookie|jobs powered by|©|powered by\s|\[.*\]\(https?://[^)]*\)\s*$)", re.I)


def extract_content(markdown: str, limit: int = CONTENT_LIMIT) -> str:
    """The posting's substantive text: from the first real heading up to the
    application-form/EEO chrome, minus nav/form/boilerplate lines. Verbatim
    lines, never a summary. Blank lines and '---' rules dropped to satisfy
    the vault's format conventions (see validate.check_format_compliance)."""
    out, started = [], False
    for line in markdown.splitlines():
        s = line.strip()
        if _CUT_MARKERS.match(s):
            break
        if not started:
            if s.startswith("#") and len(s) > 4:
                started = True
            else:
                continue
        if not s or _NOISE.match(s):
            continue
        out.append(s)
        if len("\n".join(out)) > limit:
            break
    return "\n".join(out)
  + _NOISE = re.compile(
    r"^(\[?!\[|\[back to jobs|\[apply\]|apply\b|select\.\.\.|✱|.*✱\s*$|resume/cv|full name|email\b"
    r"|phone\b|current location|current company|linkedin url|github url|portfolio url|loading$"
    r"|no location found|couldn't auto-read|analyzing resume|success!$|file exceeds|-{3,}$"
    r"|cookie|jobs powered by|©|powered by\s|\[.*\]\(https?://[^)]*\)\s*$|read more$)", re.I)

# Real, distinct bug from the Ashby application-URL one — confirmed 2026-07-26
# on both Google dossiers sourced via Freehire (BS and MS tracks): Google's
# careers site returns a *search-results listing page* shell (~20 unrelated
# job titles, "Back to jobs search" nav, "N jobs matched", pagination) ahead
# of the specific posting's own content in the SAME fetched markdown — not a
# wrong-URL problem like Ashby's /application suffix, the real posting text is
# right there further down. classify() fired on an unrelated listed job's
# title as a result. Whenever one of these listing-shell markers appears,
# everything gathered so far is shell noise — reset and wait for the next
# real heading, which lands on the actual posting content once the shell ends.
_LISTING_SHELL_RESET_RE = re.compile(
    r"^(_arrow_back_|back to jobs search|##?\s*jobs search results|[\d,]+\s+jobs matched"
    r"|showing \d+ to \d+ of|_navigate_next_)", re.I,
)

# ATS UI labels jammed against their values with no separator, real examples
# from the Conagra Brands fixture (List/Dossiers/Other/Demand Science
# Rotational Analyst - Conagra Brands.md): "locationsChicago, Illinois",
# "time typeFull time", "posted onPosted Today", "job requisition idReq-039400".
_ATS_LABEL_RUN_ON_RE = re.compile(
    r"^(locations|time type|posted on|job requisition id|time left to apply)(?=\S)", re.M,
)

# A posting's own section names, real shape confirmed against the Appian
# ("**Basic Qualifications**", "**Benefits**") and Conagra ("**Compensation**",
# "**Our Benefits**") fixtures: a fully-bolded standalone line naming one of
# these sections. Deliberately narrow — only fires when the *whole* line is
# one bold span ending in a real section keyword, so inline bold emphasis
# ("our values of **Intensity** and **Excellence**...") and non-section bold
# lines ("**Why should you kick off your career with Conagra?**") are left as
# flattened prose, per the "don't invent section boundaries" rule.
_BOLD_SECTION_RE = re.compile(r"^\*\*([^*]+?)\*\*:?$")
_SECTION_KEYWORD_RE = re.compile(r"(responsibilities|qualifications|requirements|benefits|compensation)$", re.I)

# Real, from the Manhattan Associates fixture (List/Dossiers/1 - AI & ML/A.I.
# Developer Co-Op (Boston, MA) - Manhattan Associates.md): a "Follow Us"
# heading followed by a bulleted LinkedIn/X/Facebook link list, pure chrome.
_FOLLOW_US_HEADING_RE = re.compile(r"^#{1,6}\s*follow us\s*$", re.I)
_LINK_BULLET_RE = re.compile(r"^-\s*\[.+\]\(https?://\S+\)\s*$")


def _dedupe_paragraphs(markdown: str) -> str:
    """Drops a blank-line-delimited block that repeats verbatim later in the
    same fetch, keeping the first occurrence — real example: the Conagra
    fixture's whole 'About Us' paragraph appears twice."""
    blocks = re.split(r"\n\s*\n", markdown)
    seen, kept = set(), []
    for block in blocks:
        key = block.strip()
        if key and key in seen:
            continue
        if key:
            seen.add(key)
        kept.append(block)
    return "\n\n".join(kept)


def _strip_trailing_social_chrome(lines: list) -> list:
    out, skip_links = [], False
    for line in lines:
        if _FOLLOW_US_HEADING_RE.match(line.strip()):
            skip_links = True
            continue
        if skip_links and _LINK_BULLET_RE.match(line.strip()):
            continue
        skip_links = False
        out.append(line)
    return out


def extract_content(markdown: str, limit: int = CONTENT_LIMIT) -> str:
    """The posting's substantive text: from the first real heading up to the
    application-form/EEO chrome, minus nav/form/boilerplate lines. Verbatim
    lines, never a summary — but deduped (no repeated paragraph), chrome-split
    (ATS UI labels get their own line), and structured (a source's own bolded
    section names become real '###' headings) per the Internship Notes
    Standard §2. Blank lines and '---' rules dropped to satisfy the vault's
    format conventions (see validate.check_format_compliance)."""
    markdown = _dedupe_paragraphs(markdown)
    markdown = _ATS_LABEL_RUN_ON_RE.sub(lambda m: m.group(1) + "\n", markdown)

    out, started = [], False
    for line in markdown.splitlines():
        s = line.strip()
        if _CUT_MARKERS.match(s):
            break
        if _LISTING_SHELL_RESET_RE.match(s):
            started, out = False, []
            continue
        if not started:
            if s.startswith("#") and len(s) > 4:
                started = True
            else:
                continue
        if not s or _NOISE.match(s):
            continue
        section = _BOLD_SECTION_RE.match(s)
        if section and _SECTION_KEYWORD_RE.search(section.group(1).strip()):
            s = f"### {section.group(1).strip()}"
        out.append(s)
        if len("\n".join(out)) > limit:
            break
    return "\n".join(_strip_trailing_social_chrome(out))
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -60`
  ```
........................................................................ [ 27%]
........................................................................ [ 55%]
........................................................................ [ 83%]
..........................................                               [100%]
258 passed in 5.02s
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
  ```diff
  - def build_frontmatter(listing, uid: str, date_found: str, matched_reason: str) -> dict:
    """uid and category are deliberately not rendered — uid stays available
    internally via the dossier_uids.json manifest (see write_dossier), and
    category was never surfaced to the reader anywhere else in the note.
    `next:` (not `promoted:`) matches every other note type's convention
    across the vault."""
    return {
        "company": listing.company,
        "title": listing.title,
        "url": listing.url,
        "source": listing.source,
        "terms": _yaml_list(listing.terms),
        "locations": _yaml_list(listing.locations),
        "target_year": _yaml_list(listing.target_year),
        "date_posted": _iso_date(listing.date_posted),
        "date_found": date_found,
        "matched_reason": matched_reason,
        "status": "unreviewed",
        "next": None,
        "tags": ["internship", "auto-discovered"],
    }
  + DOSSIERS_MOC_LINK = "[[10_Areas/Career/Internships/List/Dossiers MOC]]"

_TAG_ILLEGAL_CHARS = re.compile(r'[\\/:*?"<>|]')


def company_slug(company: str) -> str:
    """Same slugification as dossier_filename(): lowercase, spaces to
    hyphens, illegal chars stripped — so 'Aquatic Capital Management' and
    ' aquatic capital management ' both produce company/aquatic-capital-management,
    per the Standard's same-company clustering rule (§1)."""
    s = _TAG_ILLEGAL_CHARS.sub("", company).strip().lower()
    return re.sub(r"\s+", "-", s)


def build_frontmatter(listing, uid: str, date_found: str, matched_reason: str) -> dict:
    """uid and category are deliberately not rendered — uid stays available
    internally via the dossier_uids.json manifest (see write_dossier), and
    category was never surfaced to the reader anywhere else in the note.
    `next:` (not `promoted:`) matches every other note type's convention
    across the vault. `notes:` (always the Dossiers MOC link) and the
    `company/<slug>` tag are the Internship Notes Standard §1 interlinking
    requirement — `notes` sits right after `next`, right before `tags`."""
    return {
        "company": listing.company,
        "title": listing.title,
        "url": listing.url,
        "source": listing.source,
        "terms": _yaml_list(listing.terms),
        "locations": _yaml_list(listing.locations),
        "target_year": _yaml_list(listing.target_year),
        "date_posted": _iso_date(listing.date_posted),
        "date_found": date_found,
        "matched_reason": matched_reason,
        "status": "unreviewed",
        "next": None,
        "notes": [DOSSIERS_MOC_LINK],
        "tags": ["internship", "auto-discovered", f"company/{company_slug(listing.company)}"],
    }
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py`
  ```diff
  - REQUIRED_FRONTMATTER_FIELDS = (
    "company", "title", "url", "source", "terms", "locations",
    "target_year", "date_posted", "date_found", "matched_reason", "status", "next", "tags",
)
  + REQUIRED_FRONTMATTER_FIELDS = (
    "company", "title", "url", "source", "terms", "locations",
    "target_year", "date_posted", "date_found", "matched_reason", "status", "next", "notes", "tags",
)
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -60`
  ```
........................................................................ [ 27%]
........................................................................ [ 55%]
........................................................................ [ 83%]
..........................................                               [100%]
258 passed in 2.53s
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
  ```diff
  - def render_dossier(listing, uid: str, date_found: str, matched_reason: str, posting_content: str = "",
                   classification_callout: str = "") -> str:
    frontmatter = build_frontmatter(listing, uid, date_found, matched_reason)
    frontmatter_yaml = yaml.dump(
        frontmatter, Dumper=_FrontmatterDumper, sort_keys=False, default_flow_style=False, allow_unicode=True
    )
    markdown = _template.render(
  + def dump_frontmatter(frontmatter: dict) -> str:
    """Shared YAML rendering (None as blank scalar, indented list items) so
    every dossier-writing code path — including recheck.py's removal-time
    frontmatter patch — serializes identically."""
    return yaml.dump(
        frontmatter, Dumper=_FrontmatterDumper, sort_keys=False, default_flow_style=False, allow_unicode=True
    )


def render_dossier(listing, uid: str, date_found: str, matched_reason: str, posting_content: str = "",
                   classification_callout: str = "") -> str:
    frontmatter = build_frontmatter(listing, uid, date_found, matched_reason)
    frontmatter_yaml = dump_frontmatter(frontmatter)
    markdown = _template.render(
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
  ```diff
  -     path.write_text(markdown)
    if state_dir is not None:
        manifest[str(path.relative_to(vault_root))] = uid
        save_dossier_uids(state_dir, manifest)
    return path
  +     path.write_text(markdown)
    if state_dir is not None:
        manifest[str(path.relative_to(vault_root))] = uid
        save_dossier_uids(state_dir, manifest)
    return path


REMOVED_DOSSIERS_MOC_LINK = "[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]"
VIEWED_SUBPATH = DOSSIER_SUBPATH / "Viewed"


def move_dossier_to_viewed(vault_root, path, reason: str, removed_date: str, state_dir=None) -> Path:
    """Moves a closed-posting dossier into Viewed/ instead of deleting it
    (Internship Notes Standard §4) — the posting closing is real information
    (hiring cadence, why a later duplicate should be rejected, a record of
    what this pipeline actually saw), not something to throw away. Appends
    the Removed Dossiers MOC link to the existing notes: list (never
    replacing the original Dossiers MOC / company links already there), sets
    status: removed (the field's first real transition away from its static
    'unreviewed'), and records removed_date/removed_reason. Updates
    dossier_uids.json to the new path so the next write_dossier() idempotency
    check for this uid isn't left pointing at a file that moved."""
    vault_root = Path(vault_root)
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    frontmatter = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)

    notes = list(frontmatter.get("notes") or [])
    if DOSSIERS_MOC_LINK not in notes:
        notes.append(DOSSIERS_MOC_LINK)
    if REMOVED_DOSSIERS_MOC_LINK not in notes:
        notes.append(REMOVED_DOSSIERS_MOC_LINK)
    frontmatter["notes"] = notes
    frontmatter["status"] = "removed"
    frontmatter["removed_date"] = removed_date
    frontmatter["removed_reason"] = reason

    new_path = vault_root / VIEWED_SUBPATH / path.name
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path.write_text("---\n" + dump_frontmatter(frontmatter) + "---\n" + body)
    path.unlink()

    if state_dir is not None:
        manifest = load_dossier_uids(state_dir)
        old_rel = str(path.relative_to(vault_root))
        uid = manifest.pop(old_rel, None)
        if uid is not None:
            manifest[str(new_path.relative_to(vault_root))] = uid
            save_dossier_uids(state_dir, manifest)
    return new_path
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
  ```diff
  - from run_pipeline import file_github_issue
from vault_writer.writer import load_dossier_uids, scan_dossiers
  + from run_pipeline import file_github_issue
from vault_writer.writer import load_dossier_uids, move_dossier_to_viewed, scan_dossiers
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
  ```diff
  -     # ponytail: crude mass-deletion brake — a truncated/glitched feed must not
    # wipe the vault. Threshold is arbitrary but safe; tune if it ever trips wrongly.
    if len(removals) > max(5, len(dossiers) // 2):
        record["halted"] = True
        record["halt_reason"] = f"would remove {len(removals)} of {len(dossiers)} dossiers — feed glitch?"
  +     # ponytail: crude mass-move brake — a truncated/glitched feed must not
    # empty the vault into Viewed/. Threshold is arbitrary but safe; tune if it
    # ever trips wrongly. Same protective logic as before this was a move
    # instead of a delete — the risk (a feed glitch wiping real dossiers out
    # of the live buckets) is identical either way.
    if len(removals) > max(5, len(dossiers) // 2):
        record["halted"] = True
        record["halt_reason"] = f"would move {len(removals)} of {len(dossiers)} dossiers to Viewed/ — feed glitch?"
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
  ```diff
  -     for r in removals:
        print(f"{'would remove' if args.dry_run else 'removing'}: {r['uid']} — {r['reason']}")
    if args.dry_run:
        print(f"dry run: {len(removals)} of {len(dossiers)} would be removed")
        return

    if removals:
        for r in removals:
            Path(r["path"]).unlink()
        try:
            commit_and_push_with_retry(
                jarvis_dir, f"Remove {len(removals)} closed posting(s) — recheck {now.date().isoformat()}"
            )
        except GitPushError as exc:
  +     for r in removals:
        print(f"{'would move' if args.dry_run else 'moving'}: {r['uid']} — {r['reason']}")
    if args.dry_run:
        print(f"dry run: {len(removals)} of {len(dossiers)} would be moved to Viewed/")
        return

    if removals:
        for r in removals:
            move_dossier_to_viewed(
                jarvis_dir, r["path"], r["reason"], now.date().isoformat(), state_dir=STATE_DIR
            )
        try:
            commit_and_push_with_retry(
                jarvis_dir, f"Move {len(removals)} closed posting(s) to Viewed/ — recheck {now.date().isoformat()}"
            )
        except GitPushError as exc:
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
  ```diff
  -     _commit_log(record, now)
    print(f"removed {len(removals)} of {len(dossiers)} dossiers; {len(errors)} fetch error(s)")
  +     _commit_log(record, now)
    print(f"moved {len(removals)} of {len(dossiers)} dossiers to Viewed/; {len(errors)} fetch error(s)")
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
  ```diff
  - cross-refs each against its source's live feed, and removes any dossier whose
posting is now inactive or gone from the feed entirely. Runs on its own daily
cron (.github/workflows/recheck.yml) — postings don't close often enough to
justify rechecking every hour.
  + cross-refs each against its source's live feed, and moves any dossier whose
posting is now inactive or gone from the feed entirely into Viewed/ (never
deletes — Internship Notes Standard §4: a closed posting's history is real
information). Runs on its own daily cron (.github/workflows/recheck.yml) —
postings don't close often enough to justify rechecking every hour.
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -30`
  ```
........................................................................ [ 27%]
........................................................................ [ 55%]
........................................................................ [ 83%]
..........................................                               [100%]
258 passed in 3.02s
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
python3 -c "
import json
raw = json.loads(open('tests/fixtures/simplifyjobs.json').read())[0]
print(raw.get('title'), '|', raw.get('category'))
from core.classify import classify
print(classify(raw.get('title'), raw.get('category'), ''))
"
grep -n "STATE_DIR\|state_dir\|state/" run_pipeline.py | head -30
  ```
  ```
Forward Deployed Software Engineer – Internship - US Government | Software
('Other', '')
138:                       http_head=None, fetch_page_fn=None, opt_cache=None, state_dir=None):
217:                     state_dir=state_dir)
242:    state_dir=None,
295:        fetch_page_fn=fetch_page_fn, opt_cache=opt_cache, state_dir=state_dir,
318:            "state/seen_ids.json was NOT updated for these — they'll be retried next run.",
358:        state_dir=REPO_ROOT / "state",
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - from vault_writer.validate import check_format_compliance, validate
from vault_writer.writer import render_dossier, scan_dossiers, write_dossier
  + from vault_writer.validate import check_format_compliance, validate
from vault_writer.writer import DOSSIER_SUBPATH, render_dossier, scan_dossiers, write_dossier
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - # 2026-07-25 decision: turning on 4 sources at once produced a one-time backlog
# (186 new candidates, 171 write-gate-passing) far above the steady-state <100/
# month Firecrawl budget Phase 6 was sized for. Neither absorbing the whole
# backlog in one run (dumps 100+ dossiers on a promotion queue already at zero)
# nor pre-seeding seen_ids to silently skip it (throws away real, currently-
# open postings — the reason these sources were added) was acceptable. Cap
# instead, and let it drain over several runs. No structured deadline field
# exists across all 6 sources (Greenhouse sometimes has one via metadata, the
# other 5 sources never do) — most-recently-posted first is the prioritization
# that's actually available everywhere, not a compromise on the chosen rule.
MAX_NEW_WRITES_PER_RUN = 18


def _prioritize_and_cap(new_listings: list, limit: int) -> tuple:
    """Most-recently-posted first; missing date_posted sorts last, never first
    (an unknown post date must not win priority over a known-recent one).
    Returns (this_run, deferred) — deferred items are simply not passed to
    validate_and_write and therefore never marked seen, so dedup_new()
    naturally re-offers them next run without any extra state to manage."""
    ordered = sorted(new_listings, key=lambda item: item[1].date_posted or 0, reverse=True)
    return ordered[:limit], ordered[limit:]
  + # 2026-07-25 decision: turning on 4 sources at once produced a one-time backlog
# (186 new candidates, 171 write-gate-passing) far above the steady-state <100/
# month Firecrawl budget Phase 6 was sized for. Neither absorbing the whole
# backlog in one run (dumps 100+ dossiers on a promotion queue already at zero)
# nor pre-seeding seen_ids to silently skip it (throws away real, currently-
# open postings — the reason these sources were added) was acceptable. Cap
# instead, and let it drain over several runs. No structured deadline field
# exists across all 6 sources (Greenhouse sometimes has one via metadata, the
# other 5 sources never do) — most-recently-posted first is the prioritization
# that's actually available everywhere, not a compromise on the chosen rule.
#
# Revised 2026-07-29 (Task A): split per bucket instead of one flat number —
# a tunable dict, not magic numbers spread through the function. Still caps
# at roughly 10/run to protect Firecrawl budget and review throughput; a
# bucket with 0 eligible candidates this run never lets another bucket borrow
# its unused slots (each bucket only draws from its own ordered queue).
MAX_NEW_WRITES_PER_RUN = {"AI/ML": 3, "Fullstack": 3, "CyS & Finance": 3, "Other": 1}

# Per-bucket vault capacity, per the original design (Dossiers-to-Create.md,
# Source of Truth.md) — but per the user's explicit 2026-07-29 override, this
# is a NOTIFICATION mechanism, never a write refusal: the false-exclusion-
# worse-than-false-inclusion asymmetry that governs every other gate in this
# codebase applies here too (a hard-refusal cap would silently drop a real,
# currently-open posting for no benefit — the scarce resource is human review
# attention, not vault storage). See run_once()'s bucket_at_capacity handling.
BUCKET_CAPACITY = 50
# Global total across List/Dossiers/ excluding Viewed/. 150/170 are logged in
# the run record only (informational); 190/200 additionally file a GitHub
# issue the first time each is crossed (same "notify once" state as buckets).
GLOBAL_INFO_THRESHOLDS = (150, 170)
GLOBAL_ISSUE_THRESHOLDS = (190, 200)
CAPACITY_STATE_FILENAME = "capacity_notified.json"


def _prioritize_and_cap(new_listings: list, budget: dict) -> tuple:
    """Most-recently-posted first, scoped per-bucket per the tunable budget
    dict — each bucket fills only from its own ordered queue, so an empty
    bucket this run can't let another bucket's items borrow its slots.
    Bucket is the same degraded-signal classify() (title/category only, no
    fetched content yet) validate_and_write() itself falls back to before a
    posting's content is fetched — pacing doesn't need the refined,
    content-informed bucket, only the final written folder does. Missing
    date_posted sorts last, never first (an unknown post date must not win
    priority over a known-recent one). Returns (this_run, deferred) —
    deferred items are simply not passed to validate_and_write and therefore
    never marked seen, so dedup_new() naturally re-offers them next run
    without any extra state to manage."""
    by_bucket = {}
    for uid, listing in new_listings:
        bucket, _ = classify(listing.title, listing.category, "")
        by_bucket.setdefault(bucket, []).append((uid, listing))

    this_run, deferred = [], []
    for bucket, items in by_bucket.items():
        ordered = sorted(items, key=lambda item: item[1].date_posted or 0, reverse=True)
        limit = budget.get(bucket, 0)
        this_run.extend(ordered[:limit])
        deferred.extend(ordered[limit:])
    return this_run, deferred


def count_dossiers_by_bucket(vault_root) -> dict:
    """Real per-bucket file counts in the vault checkout — Viewed/ isn't one
    of BUCKET_FOLDERS' values, so it's excluded automatically, matching the
    Standard's '201 total excluding Viewed/' scope."""
    vault_root = Path(vault_root)
    counts = {}
    for bucket, folder in BUCKET_FOLDERS.items():
        d = vault_root / DOSSIER_SUBPATH / folder
        counts[bucket] = len(list(d.glob("*.md"))) if d.is_dir() else 0
    return counts


def load_capacity_notified(state_dir) -> dict:
    path = Path(state_dir) / CAPACITY_STATE_FILENAME
    if not path.exists():
        return {"buckets": [], "global": []}
    return json.loads(path.read_text())


def save_capacity_notified(state_dir, notified: dict) -> None:
    path = Path(state_dir) / CAPACITY_STATE_FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notified, indent=2, sort_keys=True) + "\n")
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -         "deferred_count": 0,
        "written_count": 0,
        "rejections": [],
        "errors": [],
        "halted": False,
        "halt_reason": None,
    }
  +         "deferred_count": 0,
        "written_count": 0,
        "rejections": [],
        "errors": [],
        "halted": False,
        "halt_reason": None,
        "bucket_at_capacity": [],
        "dossier_total": 0,
    }
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -     written_uids, rejections = validate_and_write(
        this_run, profile, jarvis_dir, seen_ids, now.date().isoformat(), http_head,
        fetch_page_fn=fetch_page_fn, opt_cache=opt_cache, state_dir=state_dir,
    )
    if opt_cache_path and opt_cache:
        Path(opt_cache_path).parent.mkdir(parents=True, exist_ok=True)
        Path(opt_cache_path).write_text(json.dumps(opt_cache, indent=2, sort_keys=True) + "\n")
    record["rejections"] = rejections
  +     written_uids, rejections = validate_and_write(
        this_run, profile, jarvis_dir, seen_ids, now.date().isoformat(), http_head,
        fetch_page_fn=fetch_page_fn, opt_cache=opt_cache, state_dir=state_dir,
    )
    if opt_cache_path and opt_cache:
        Path(opt_cache_path).parent.mkdir(parents=True, exist_ok=True)
        Path(opt_cache_path).write_text(json.dumps(opt_cache, indent=2, sort_keys=True) + "\n")
    record["rejections"] = rejections

    # Task A resource-limit notification (Standard §5): a bucket at/over
    # capacity or the global total crossing a threshold is surfaced, never a
    # write refusal — the writes above already happened regardless.
    bucket_counts = count_dossiers_by_bucket(jarvis_dir)
    record["bucket_at_capacity"] = sorted(b for b, c in bucket_counts.items() if c >= BUCKET_CAPACITY)
    record["dossier_total"] = sum(bucket_counts.values())

    notified = load_capacity_notified(state_dir) if state_dir is not None else {"buckets": [], "global": []}
    newly_notified = False
    for bucket in record["bucket_at_capacity"]:
        if bucket not in notified["buckets"]:
            notified["buckets"].append(bucket)
            newly_notified = True
            issue_fn(
                issue_repo,
                f"Bucket '{bucket}' at/over its {BUCKET_CAPACITY}-dossier notification threshold ({timestamp})",
                f"'{bucket}' now has {bucket_counts[bucket]} dossiers in List/Dossiers/ — this is a "
                "notification, not a write refusal (a full bucket is a signal to review more urgently, "
                "not a reason to lose a real posting). New matches keep writing into this bucket.",
            )
    for threshold in GLOBAL_ISSUE_THRESHOLDS:
        if record["dossier_total"] >= threshold and threshold not in notified["global"]:
            notified["global"].append(threshold)
            newly_notified = True
            issue_fn(
                issue_repo,
                f"Total dossier count crossed {threshold} ({timestamp})",
                f"List/Dossiers/ (excluding Viewed/) now has {record['dossier_total']} dossiers total.",
            )
    if state_dir is not None and newly_notified:
        save_capacity_notified(state_dir, notified)
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -80`
  ```
        items = [_listing_with_date("known", 500), _listing_with_date("unknown", None)]
>       this_run, deferred = run_pipeline._prioritize_and_cap(items, limit=1)
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: _prioritize_and_cap() got an unexpected keyword argument 'limit'

tests/test_run_pipeline.py:109: TypeError
________ test_run_once_defers_beyond_the_cap_and_leaves_it_for_next_run ________

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-3/[REDACTED]')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f2283b95d90>

    def test_run_once_defers_beyond_the_cap_and_leaves_it_for_next_run(tmp_path, monkeypatch):
        """The core guarantee: a deferred item is not marked seen, so it's neither
        lost (no silent drop) nor duplicated (no re-write) — it just naturally
        reappears as 'new' on the next run, same as any other unseen match."""
        monkeypatch.setattr(run_pipeline, "MAX_NEW_WRITES_PER_RUN", 1)
        kwargs = _run_once_kwargs(tmp_path)
>       record = run_pipeline.run_once(**kwargs)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_run_pipeline.py:121: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
run_pipeline.py:352: in run_once
    this_run, deferred = _prioritize_and_cap(new_listings, MAX_NEW_WRITES_PER_RUN)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

new_listings = [('SimplifyJobs:[REDACTED]', Listing(company='Palantir', title='Forward Deployed Software En...es=[], active=True, date_posted=1774656000, raw_id='[REDACTED]', sponsorship='', raw_text='')), ...]
budget = 1

    def _prioritize_and_cap(new_listings: list, budget: dict) -> tuple:
        """Most-recently-posted first, scoped per-bucket per the tunable budget
        dict — each bucket fills only from its own ordered queue, so an empty
        bucket this run can't let another bucket's items borrow its slots.
        Bucket is the same degraded-signal classify() (title/category only, no
        fetched content yet) validate_and_write() itself falls back to before a
        posting's content is fetched — pacing doesn't need the refined,
        content-informed bucket, only the final written folder does. Missing
        date_posted sorts last, never first (an unknown post date must not win
        priority over a known-recent one). Returns (this_run, deferred) —
        deferred items are simply not passed to validate_and_write and therefore
        never marked seen, so dedup_new() naturally re-offers them next run
        without any extra state to manage."""
        by_bucket = {}
        for uid, listing in new_listings:
            bucket, _ = classify(listing.title, listing.category, "")
            by_bucket.setdefault(bucket, []).append((uid, listing))
    
        this_run, deferred = [], []
        for bucket, items in by_bucket.items():
            ordered = sorted(items, key=lambda item: item[1].date_posted or 0, reverse=True)
>           limit = budget.get(bucket, 0)
                    ^^^^^^^^^^
E           AttributeError: 'int' object has no attribute 'get'

run_pipeline.py:111: AttributeError
_________ test_run_once_second_run_does_not_rewrite_already_seen_items _________

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-3/[REDACTED]')

    def test_run_once_second_run_does_not_rewrite_already_seen_items(tmp_path):
        kwargs = _run_once_kwargs(tmp_path)
        first = run_pipeline.run_once(**kwargs)
        assert first["written_count"] > 0
    
        kwargs2 = _run_once_kwargs(tmp_path, jarvis_dir=kwargs["jarvis_dir"])
        kwargs2["state_path"] = kwargs["state_path"]
        kwargs2["runs_log_path"] = kwargs["runs_log_path"]
        second = run_pipeline.run_once(**kwargs2)
    
>       assert second["written_count"] == 0
E       assert 1 == 0

tests/test_run_pipeline.py:367: AssertionError
=========================== short test summary info ============================
FAILED tests/test_run_pipeline.py::test_prioritize_and_cap_keeps_most_recent_first
FAILED tests/test_run_pipeline.py::test_prioritize_and_cap_missing_date_posted_sorts_last
FAILED tests/test_run_pipeline.py::test_run_once_defers_beyond_the_cap_and_leaves_it_for_next_run
FAILED tests/test_run_pipeline.py::test_run_once_second_run_does_not_rewrite_already_seen_items
4 failed, 254 passed in 1.92s
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
python3 -c "
import sys
sys.path.insert(0,'tests')
from test_run_pipeline import _fake_http_get, PROFILE
import run_pipeline
from collections import Counter
matched = run_pipeline.fetch_and_filter(PROFILE, http_get=_fake_http_get)
from core.classify import classify
buckets = Counter()
total=0
for name, info in matched.items():
    for l in info['matched']:
        b,_ = classify(l.title, l.category, '')
        buckets[b]+=1
        total+=1
print('total', total)
print(buckets)
"

  ```
  ```
total 10
Counter({'Other': 8, 'CyS & Finance': 1, 'Fullstack': 1})
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```diff
  - def test_prioritize_and_cap_keeps_most_recent_first():
    items = [_listing_with_date(i, date_posted) for i, date_posted in enumerate([100, 300, 200])]
    this_run, deferred = run_pipeline._prioritize_and_cap(items, limit=2)

    assert [d for _, l in this_run for d in [l.date_posted]] == [300, 200]
    assert [l.date_posted for _, l in deferred] == [100]


def test_prioritize_and_cap_missing_date_posted_sorts_last():
    items = [_listing_with_date("known", 500), _listing_with_date("unknown", None)]
    this_run, deferred = run_pipeline._prioritize_and_cap(items, limit=1)

    assert this_run[0][1].date_posted == 500
    assert deferred[0][1].date_posted is None
  + def test_prioritize_and_cap_keeps_most_recent_first():
    # _listing_with_date's base fixture (Palantir "Forward Deployed Software
    # Engineer - Internship - US Government") classifies to the 'Other'
    # bucket — all three items land in the same bucket's queue.
    items = [_listing_with_date(i, date_posted) for i, date_posted in enumerate([100, 300, 200])]
    this_run, deferred = run_pipeline._prioritize_and_cap(items, budget={"Other": 2})

    assert [d for _, l in this_run for d in [l.date_posted]] == [300, 200]
    assert [l.date_posted for _, l in deferred] == [100]


def test_prioritize_and_cap_missing_date_posted_sorts_last():
    items = [_listing_with_date("known", 500), _listing_with_date("unknown", None)]
    this_run, deferred = run_pipeline._prioritize_and_cap(items, budget={"Other": 1})

    assert this_run[0][1].date_posted == 500
    assert deferred[0][1].date_posted is None


def test_prioritize_and_cap_scopes_budget_per_bucket():
    """A bucket with 0 eligible candidates this run must not let another
    bucket's items borrow its unused slots — each bucket draws only from its
    own ordered queue."""
    other_items = [_listing_with_date(i, date_posted) for i, date_posted in enumerate([100, 300, 200])]
    this_run, deferred = run_pipeline._prioritize_and_cap(
        other_items, budget={"Other": 2, "AI/ML": 5, "Fullstack": 5, "CyS & Finance": 5},
    )
    assert len(this_run) == 2  # AI/ML's unused slots don't spill over into Other
    assert len(deferred) == 1
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```diff
  -     monkeypatch.setattr(run_pipeline, "MAX_NEW_WRITES_PER_RUN", 1)
  +     monkeypatch.setattr(run_pipeline, "MAX_NEW_WRITES_PER_RUN", {"Other": 1})
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```diff
  - def test_run_once_second_run_does_not_rewrite_already_seen_items(tmp_path):
    kwargs = _run_once_kwargs(tmp_path)
    first = run_pipeline.run_once(**kwargs)
    assert first["written_count"] > 0
  + def test_run_once_second_run_does_not_rewrite_already_seen_items(tmp_path, monkeypatch):
    # Generous per-bucket budget so every fixture match fits in the first run
    # — this test is about seen-state idempotency across runs, not pacing.
    monkeypatch.setattr(
        run_pipeline, "MAX_NEW_WRITES_PER_RUN",
        {"AI/ML": 20, "Fullstack": 20, "CyS & Finance": 20, "Other": 20},
    )
    kwargs = _run_once_kwargs(tmp_path)
    first = run_pipeline.run_once(**kwargs)
    assert first["written_count"] > 0
    assert first["deferred_count"] == 0
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -60`
  ```
........................................................................ [ 27%]
........................................................................ [ 55%]
........................................................................ [ 83%]
...........................................                              [100%]
259 passed in 1.87s
  ```
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/posting_google_careers.md`
  ```
# job details
_arrow_back_ [Back to jobs search](https://www.google.com/about/careers/applications/jobs/results)
Back to jobs search
## Jobs search results
3,583 jobs matched
- [**Regulatory and Litigation Counsel, APAC Defense** \
Seoul, South Korea](https://www.google.com/about/careers/applications/jobs/results/[REDACTED])
- [**Staff Software Developer, Embedded Systems/Firmware** \
Waterloo, ON, Canada](https://www.google.com/about/careers/applications/jobs/results/[REDACTED])
- [**Product Manager, AI Platform Operations and Tooling** \
Hyderabad, Telangana, India; Bengaluru, Karnataka, India](https://www.google.com/about/careers/applications/jobs/results/[REDACTED])
- [**Senior Software Engineer, Site Reliability Engineering, Vertex AI 3P SRE** \
Warsaw, Poland](https://www.google.com/about/careers/applications/jobs/results/[REDACTED])
- [**Corporate Development Associate** \
Mountain View, CA, USA; San Francisco, CA, USA](https://www.google.com/about/careers/applications/jobs/results/[REDACTED])
- [**ASIC Design Verification Engineer, Digital Signal Processing** \
Sunnyvale, CA, USA](https://www.google.com/about/careers/applications/jobs/results/[REDACTED])
- [**Forward Deployed Engineer IV, GenAI, Google Cloud** \
Austin, TX, USA; Chicago, IL, USA; +24 more; +23 more](https://www.google.com/about/careers/applications/jobs/results/[REDACTED])
- [**Senior Product Engineer, Machine Learning Accelerators** \
Sunnyvale, CA, USA](https://www.google.com/about/careers/applications/jobs/results/[REDACTED])
- [**Facilities Technician Developmental Program (Fixed-Term Contract) (English)** \
Midlothian, TX, USA](https://www.google.com/about/careers/applications/jobs/results/[REDACTED])
- [**Senior Software Engineer, Search, Mobile (Android)** \
London, UK](https://www.google.com/about/careers/applications/jobs/results/[REDACTED])
Showing 1 to 20 of 3583 rows
1‑20 of 3583
_navigate_next_ [Go to next page](https://www.google.com/about/careers/applications/jobs/results/95141459539174086?page=2)
_arrow_back_ [Back to jobs search](https://www.google.com/about/careers/applications/jobs/results)
Back to jobs search
## Software Engineering Intern, MS, Summer 2027
_share_
- _link_Copy link
- _email_Email a friend
_corporate_fare_ Google_place_ Mountain View, CA, USA; Atlanta, GA, USA; +29 more; +28 more_bar_chart_ Intern & Apprentice
**This posting is for students who want early consideration for our Summer 2027 roles. If you aren't ready to apply yet, the same applications will open again during our regular fall recruiting cycle.**
**Applications will be reviewed on a rolling basis and it's in the candidate's best interest to apply early.** The anticipated application window is open until July 24th, 2026, but may close earlier if all available projects are full.
This internship is intended for students in all academic years who are pursuing a Master's degree program in Computer Science or a related field.
To start the application process, you will need an updated CV or resume and a current unofficial or official transcript in English.

  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_posting_page.py`
  ```diff
  - from ingestion.posting_page import _content_fetch_url, extract_content, fetch_posting_markdown, opt_exclusion
  + from ingestion.posting_page import (
    _content_fetch_url,
    extract_content,
    fetch_posting_markdown,
    opt_exclusion,
    phd_only_exclusion,
)
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_posting_page.py`
  ```diff
  - def test_fetch_posting_markdown_strips_ashby_application_suffix_before_calling_firecrawl():
    resp = Mock(status_code=200)
    resp.json.return_value = {"data": {"markdown": "# A Job"}}
    post = Mock(return_value=resp)
    fetch_posting_markdown("https://jobs.ashbyhq.com/acme/abc123/application", "fc-key", http_post=post)
    _, kwargs = post.call_args
    assert kwargs["json"]["url"] == "https://jobs.ashbyhq.com/acme/abc123"
  + def test_fetch_posting_markdown_strips_ashby_application_suffix_before_calling_firecrawl():
    resp = Mock(status_code=200)
    resp.json.return_value = {"data": {"markdown": "# A Job"}}
    post = Mock(return_value=resp)
    fetch_posting_markdown("https://jobs.ashbyhq.com/acme/abc123/application", "fc-key", http_post=post)
    _, kwargs = post.call_args
    assert kwargs["json"]["url"] == "https://jobs.ashbyhq.com/acme/abc123"


# --- Task E: Google careers search-results-listing-shell extraction bug ---

def test_extract_content_skips_google_careers_listing_shell():
    """Real bug, confirmed 2026-07-26 on both Google dossiers sourced via
    Freehire (BS and MS tracks): the fetched markdown contains a whole
    unrelated search-results listing page (~20 job titles, 'Back to jobs
    search' nav, 'N jobs matched', pagination) before the real posting's own
    content. classify() fired on an unrelated listed job's title
    ('Senior Product Engineer, Machine Learning Accelerators') as a result.
    Fixture is the real captured content (tests/fixtures/posting_google_careers.md)."""
    md = (FIXTURES / "posting_google_careers.md").read_text(encoding="utf-8")
    content = extract_content(md)

    assert content.startswith("## Software Engineering Intern, MS, Summer 2027")
    assert "pursuing a Master's degree program in Computer Science" in content
    # none of the unrelated listed jobs survive
    assert "Regulatory and Litigation Counsel" not in content
    assert "Staff Software Developer, Embedded Systems" not in content
    assert "Corporate Development Associate" not in content
    assert "Senior Product Engineer, Machine Learning Accelerators" not in content
    assert "jobs matched" not in content
    assert "Back to jobs search" not in content


# --- Task F: content-level PhD-only degree gate ---

def test_phd_only_exclusion_rejects_real_optiver_text():
    """Real Optiver 'Quantitative Research Intern, PhD (Summer 2027)'
    (Greenhouse job id 8451781002) — no structured degrees field, so
    degrees_eligible() waved it through on missing-data permissiveness. Its
    real content states the PhD requirement as an enrollment condition rather
    than a blunt 'PhD required'."""
    text = (
        "As part of our assessment process, you may be invited to participate in a multi-day, on-site "
        "evaluative program.\nWho You Are:\n- Currently enrolled in a PhD program in Statistics, Computer "
        "Science, Machine Learning, Mathematics, or a related STEM field with outstanding academic "
        "performance\n- Expected graduation between December 2027 - June 2029"
    )
    assert phd_only_exclusion(text) is not None


@pytest.mark.parametrize(
    "text",
    [
        # real — Aquatic Capital Management "Software Engineer, Intern (Summer 2027)"
        "Active student pursuing a BS, MS, or PhD in mathematics, statistics, machine learning, physics, "
        "computer science, or other scientific disciplines with an expected graduation date between "
        "Fall 2027 and Spring 2028.",
        # real — Appian "Software Engineering Intern"
        "Currently pursuing a Bachelor's or Master's degree in Computer Science or Computer Engineering "
        "with a strong academic record.",
        # real — Manhattan Associates "A.I. Developer Co-Op (Boston, MA)"
        "Currently enrolled in a bachelor's or master's degree program in Computer Science, Artificial "
        "Intelligence, Software Engineering, Data Science, or a related discipline",
        # never reject on 'preferred'
        "A PhD is preferred but not required for this role.",
        # never reject on PhD merely listed among acceptable degrees
        "Open to Bachelor's, Master's, or PhD candidates.",
    ],
)
def test_phd_only_exclusion_does_not_reject_bachelors_masters_eligible_real_text(text):
    assert phd_only_exclusion(text) is None, text


def test_phd_only_exclusion_rejects_explicit_equivalent_phrasing():
    assert phd_only_exclusion("This role is open to doctoral candidates only.") is not None
    assert phd_only_exclusion("PhD required for this position.") is not None


# --- Task I: readable, structured dossier body content ---

def test_extract_content_dedupes_repeated_paragraph_real_conagra_case():
    """Real bug: the Conagra Brands 'Demand Science Rotational Analyst'
    fixture has its whole 'About Us' paragraph appearing twice verbatim."""
    about_us = (
        "At Conagra Brands, we have a rich heritage of making great food. We aspire to have the most "
        "impactful, energized and inclusive culture in food. As a member of our 18,000+ person team "
        "across 40+ locations, you are empowered to reach your potential, make an impact and own your "
        "career."
    )
    md = (
        f"# Demand Science Rotational Analyst - Summer 2027\n\n"
        f"{about_us}\n\n"
        f"Some other real content in between.\n\n"
        f"### About Us\n{about_us}\n"
    )
    content = extract_content(md)
    assert content.count("At Conagra Brands, we have a rich heritage") == 1
    assert "Some other real content in between." in content
    assert "### About Us" in content


def test_extract_content_splits_ats_chrome_run_ons_real_conagra_case():
    md = (
        "# Demand Science Rotational Analyst - Summer 2027\n"
        "locationsChicago, Illinois\n"
        "time typeFull time\n"
        "posted onPosted Today\n"
        "job requisition idReq-039400\n"
        "Have a taste for something big?\n"
    )
    content = extract_content(md)
    assert "locations\nChicago, Illinois" in content
    assert "time type\nFull time" in content
    assert "posted on\nPosted Today" in content
    assert "job requisition id\nReq-039400" in content


def test_extract_content_renders_real_section_names_as_headings():
    """Real shape from the Appian/Conagra fixtures: a fully-bolded standalone
    line naming a canonical section (Qualifications/Benefits/Compensation)
    becomes a real '###' heading; a non-canonical bolded line ('Why should
    you kick off your career with Conagra?') stays flattened prose — no
    invented section boundary."""
    md = (
        "# Software Engineering Intern\n"
        "**Why should you kick off your career with Conagra?**\n"
        "**Basic Qualifications**\n"
        "- Currently pursuing a degree in Computer Science.\n"
        "**Benefits**\n"
        "Comprehensive healthcare plans.\n"
    )
    content = extract_content(md)
    assert "### Basic Qualifications" in content
    assert "### Benefits" in content
    assert "**Why should you kick off your career with Conagra?**" in content  # not invented as a heading


def test_extract_content_strips_read_more_and_follow_us_chrome_real_manhattan_case():
    """Real: the Manhattan Associates 'A.I. Developer Co-Op' fixture ends
    with a 'Read More' truncation marker and a duplicated LinkedIn/X/Facebook
    'Follow Us' link block."""
    md = (
        "# A.I. Developer Co-Op (Boston, MA)\n"
        "### About Us\n"
        "At Manhattan Associates our supply chain and omnichannel technology positively affect how "
        "people work, shop and live.\n"
        "Read More\n"
        "#### Follow Us\n"
        "- [LinkedIn](https://www.linkedin.com/company/4376)\n"
        "- [X](https://twitter.com/ManhAssocNews)\n"
        "- [Facebook](https://www.facebook.com/pages/Manhattan-Associates/113391905337615)\n"
    )
    content = extract_content(md)
    assert "Read More" not in content
    assert "Follow Us" not in content
    assert "linkedin.com" not in content
    assert "twitter.com" not in content


def test_extract_content_with_no_internal_structure_stays_one_block():
    """A posting with no stated section names at all must not have section
    boundaries invented — same real-content-only rule as the heading test."""
    md = (
        "# Summer Intern 2027 - Software Developer\n"
        "About Five Rings. We are a proprietary trading firm.\n"
        "We are looking for driven students to join our team.\n"
    )
    content = extract_content(md)
    assert "###" not in content
    assert "About Five Rings" in content
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_posting_page.py -q 2>&1 | tail -100`
  ```
............................F....                                        [100%]
=================================== FAILURES ===================================
______ test_extract_content_dedupes_repeated_paragraph_real_conagra_case _______

    def test_extract_content_dedupes_repeated_paragraph_real_conagra_case():
        """Real bug: the Conagra Brands 'Demand Science Rotational Analyst'
        fixture has its whole 'About Us' paragraph appearing twice verbatim."""
        about_us = (
            "At Conagra Brands, we have a rich heritage of making great food. We aspire to have the most "
            "impactful, energized and inclusive culture in food. As a member of our 18,000+ person team "
            "across 40+ locations, you are empowered to reach your potential, make an impact and own your "
            "career."
        )
        md = (
            f"# Demand Science Rotational Analyst - Summer 2027\n\n"
            f"{about_us}\n\n"
            f"Some other real content in between.\n\n"
            f"### About Us\n{about_us}\n"
        )
        content = extract_content(md)
>       assert content.count("At Conagra Brands, we have a rich heritage") == 1
E       AssertionError: assert 2 == 1
E        +  where 2 = <built-in method count of str object at 0x17766b0>('At Conagra Brands, we have a rich heritage')
E        +    where <built-in method count of str object at 0x17766b0> = '# Demand Science Rotational Analyst - Summer 2027\nAt Conagra Brands, we have a rich heritage of making great food. W...,000+ person team across 40+ locations, you are empowered to reach your potential, make an impact and own your career.'.count

tests/test_posting_page.py:218: AssertionError
=========================== short test summary info ============================
FAILED tests/test_posting_page.py::test_extract_content_dedupes_repeated_paragraph_real_conagra_case
1 failed, 32 passed in 0.17s
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py`
  ```diff
  - def _dedupe_paragraphs(markdown: str) -> str:
    """Drops a blank-line-delimited block that repeats verbatim later in the
    same fetch, keeping the first occurrence — real example: the Conagra
    fixture's whole 'About Us' paragraph appears twice."""
    blocks = re.split(r"\n\s*\n", markdown)
    seen, kept = set(), []
    for block in blocks:
        key = block.strip()
        if key and key in seen:
            continue
        if key:
            seen.add(key)
        kept.append(block)
    return "\n\n".join(kept)
  + def _dedupe_paragraphs(markdown: str, min_len: int = 40) -> str:
    """Drops a paragraph line that repeats verbatim later in the same fetch,
    keeping the first occurrence — real example: the Conagra fixture's whole
    'About Us' paragraph appears twice. Real fetched markdown from this
    pipeline's sources renders each prose paragraph as one continuous line
    (confirmed against the Manhattan Associates/Appian/Optiver fixtures), so
    line-level comparison catches this without needing blank-line block
    boundaries the source markdown may not consistently have. min_len guards
    against deduping short, legitimately-repeated lines (labels, headings)
    that aren't real paragraph content."""
    seen, kept = set(), []
    for line in markdown.splitlines():
        key = line.strip()
        if len(key) >= min_len:
            if key in seen:
                continue
            seen.add(key)
        kept.append(line)
    return "\n".join(kept)
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_posting_page.py -q 2>&1 | tail -60`
  ```
.................................                                        [100%]
33 passed in 0.30s
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -30`
  ```
........................................................................ [ 26%]
........................................................................ [ 52%]
........................................................................ [ 79%]
........................................................                 [100%]
272 passed in 2.15s
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_relevance.py`
  ```diff
  - def [REDACTED]():
    assert stage1_reject("Software Engineer Intern", "") is False
    assert stage1_reject("Machine Learning Engineer Intern", "") is False
  + def [REDACTED]():
    assert stage1_reject("Software Engineer Intern", "") is False
    assert stage1_reject("Machine Learning Engineer Intern", "") is False


# --- Task B: product/program-management and rotational-program roles ---

def [REDACTED]():
    """Real, live Databricks posting (AIJobs, found 2026-07-26) — genuinely
    PM work ('learn how to be a successful PM') despite listing 'computer
    science' as an acceptable major; previously slipped through both stages
    and was classified AI/ML only because 'Machine Learning' is one of
    Databricks' internal team names, not because the role does ML work."""
    assert stage1_reject("Product Management Intern (Summer 2027)", "") is True


def [REDACTED]():
    """Real, live Conagra Brands posting (SimplifyJobs, found 2026-07-27,
    still in the vault at List/Dossiers/Other/ as of this writing) — a 2-year
    business rotational program (Behavioral Science/Demand Forecasting/
    Demand Planning/Advanced Analytics) with zero programming content;
    previously passed the gate on no real software signal at all."""
    assert stage1_reject("Demand Science Rotational Analyst", "") is True


def [REDACTED]():
    """A genuine software-engineering-track rotational program that names
    actual engineering rotations must still pass — the reject pattern
    requires 'rotational' not be immediately preceded by 'engineering'/
    'software', same adjacency-breaking idiom this file already uses for
    Tax/Risk Technology titles."""
    assert stage1_reject(
        "Software Engineering Rotational Program Intern",
        "Rotations include: Backend Services, Frontend Platform, Infrastructure.",
    ) is False


def [REDACTED]():
    assert stage1_reject("Product Engineer Intern", "") is False
    assert stage1_reject("Product-Focused Software Engineer Intern", "") is False


# --- Task C: adjacent-field hint now catches chemical/industrial roles ---

# Real, from the live Mosaic Company "Operations & Automation Engineering
# Co-op/Intern" posting (chemical-plant industrial-automation role) — PLC/
# DCS/SCADA controls, Bachelor's in Chemical Engineering required, physical
# labor requirements, "basic computer skills" as a minor bullet, zero real
# programming content anywhere. Previously passed stage 2 unconditionally
# (neither "chemical" nor "automation" hit the old adjacent-field hint list)
# and only got flagged downstream by classify.py's since-fixed bare-'threat'
# match on this exact workplace-safety disclaimer.
MOSAIC_CONTENT = (
    "Requires a Bachelor's degree in Chemical Engineering or related field. Experience with PLC, DCS, "
    "and SCADA control systems preferred. Basic computer skills required. Must be able to lift 50 lbs "
    "and wear a respirator as needed. The Company will not require an employee to perform any duty "
    "without posing a direct threat to the safety of his or her own self or others."
)


def [REDACTED]():
    assert stage2_confirm(
        "Operations & Automation Engineering Co-op/Intern", "The Mosaic Company", MOSAIC_CONTENT
    ) is False
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_classify.py`
  ```diff
  - def test_classification_callout_other_bucket_has_no_signal_but_still_no_number():
    callout = classification_callout("Other", "")
    assert callout.startswith("> [!NOTE] Other:")
    assert "Priority" not in callout
  + def test_classification_callout_other_bucket_has_no_signal_but_still_no_number():
    callout = classification_callout("Other", "")
    assert callout.startswith("> [!NOTE] Other:")
    assert "Priority" not in callout


# --- Task C: bare 'threat' narrowed to require security context ---

def test_classify_does_not_match_bare_threat_real_mosaic_safety_disclaimer():
    """Real false positive: Mosaic Company 'Operations & Automation
    Engineering Co-op/Intern' (chemical-plant PLC/DCS/SCADA role, zero
    cybersecurity content) matched bare 'threat' on a workplace-safety
    disclaimer, nothing to do with cybersecurity."""
    content = (
        "The Company will not require an employee to perform any duty without posing a direct threat "
        "to the safety of his or her own self or others."
    )
    bucket, signal = classify("Operations & Automation Engineering Co-op/Intern", "", content)
    assert bucket != "CyS & Finance"
    assert signal != "threat"


def test_classify_still_matches_genuine_threat_intelligence_content():
    bucket, signal = classify("Security Engineering Intern", "", "You'll work on threat intelligence and detection.")
    assert bucket == "CyS & Finance"
    assert "threat" in signal.lower()
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_relevance.py tests/test_classify.py -q 2>&1 | tail -60`
  ```
.........F.............                                                  [100%]
=================================== FAILURES ===================================
_________ [REDACTED] _________

    def [REDACTED]():
>       assert stage2_confirm(
            "Operations & Automation Engineering Co-op/Intern", "The Mosaic Company", MOSAIC_CONTENT
        ) is False
E       assert True is False
E        +  where True = stage2_confirm('Operations & Automation Engineering Co-op/Intern', 'The Mosaic Company', "Requires a Bachelor's degree in Chemical Engineering or related field. Experience with PLC, DCS, and SCADA control sy...require an employee to perform any duty without posing a direct threat to the safety of his or her own self or others.")

tests/test_relevance.py:115: AssertionError
=========================== short test summary info ============================
FAILED tests/test_relevance.py::[REDACTED]
1 failed, 22 passed in 0.05s
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/relevance.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/relevance.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/relevance.py`
  ```diff
  - def stage2_confirm(title: str, company: str, posting_content: str) -> bool:
    """Called only when posting_content is non-empty. True = passes (either
    not adjacent-field at all, or adjacent-field AND content shows real
    software work). False = adjacent-field company/title with no software
    signal in the actual content — genuinely non-technical despite passing
    stage 1 (e.g. a hardware-manufacturing floor role at a space company)."""
    if not _ADJACENT_FIELD_COMPANY_HINT_RE.search(f"{title} {company}"):
        return True
    return bool(_SOFTWARE_CONTENT_SIGNAL_RE.search(posting_content))
  + def stage2_confirm(title: str, company: str, posting_content: str) -> bool:
    """Called only when posting_content is non-empty. True = passes (either
    not adjacent-field at all, or adjacent-field AND content shows real
    software work). False = adjacent-field with no software signal in the
    actual content — genuinely non-technical despite passing stage 1 (e.g. a
    hardware-manufacturing floor role at a space company).

    The hint check also scans posting_content, not just title+company: real
    bug, Mosaic Company's "Operations & Automation Engineering Co-op/Intern"
    (2026-07-29) — its chemical-plant/PLC-DCS-SCADA signal appears only in
    the fetched content ("Bachelor's degree in Chemical Engineering",
    "PLC, DCS, and SCADA control systems"), never in the title or company
    name, so a title+company-only hint check never routed it through the
    software-signal confirmation below at all."""
    if not _ADJACENT_FIELD_COMPANY_HINT_RE.search(f"{title} {company} {posting_content}"):
        return True
    return bool(_SOFTWARE_CONTENT_SIGNAL_RE.search(posting_content))
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -60`
  ```
........................................................................ [ 25%]
........................................................................ [ 51%]
........................................................................ [ 77%]
...............................................................          [100%]
279 passed in 2.41s
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py`
  ```diff
  - from core.identity import compute_uid, cross_source_key
  + from core.identity import compute_uid, cross_source_key, extract_ats_job_id
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py`
  ```diff
  - def test_cross_source_key_normalizes_case_and_whitespace():
    assert cross_source_key("MLH (Major League Hacking)", "MLH Fellowship") == \
        cross_source_key("  mlh (major league hacking)", "mlh   fellowship ")
    assert cross_source_key("MLH", "Fellowship") != cross_source_key("MLH", "Other Program")
  + def test_cross_source_key_normalizes_case_and_whitespace():
    assert cross_source_key("MLH (Major League Hacking)", "MLH Fellowship") == \
        cross_source_key("  mlh (major league hacking)", "mlh   fellowship ")
    assert cross_source_key("MLH", "Fellowship") != cross_source_key("MLH", "Other Program")


# --- Task D: URL/job-id-based cross-source dedup — four real 2026-07-29 incidents ---

def test_extract_ats_job_id_greenhouse():
    assert extract_ats_job_id("https://job-boards.greenhouse.io/virtu/jobs/8624410002") == "8624410002"


def test_extract_ats_job_id_lever_ignores_apply_suffix():
    """Real Palantir 'Intel' FDSE duplicate: SimplifyJobs' URL carries a
    trailing /apply, zshah101's doesn't — same Lever job id either way."""
    with_apply = "https://jobs.lever.co/palantir/[REDACTED]/apply"
    without_apply = "https://jobs.lever.co/palantir/[REDACTED]"
    assert extract_ats_job_id(with_apply) == "[REDACTED]"
    assert extract_ats_job_id(with_apply) == extract_ats_job_id(without_apply)


def test_extract_ats_job_id_google_careers_results_url():
    """Real Google BS/MS Summer 2027 SWE intern duplicate: vanshb03 and
    Freehire both resolve to the identical numeric id embedded in
    .../jobs/results/85564713261245126."""
    url = "https://www.google.com/about/careers/applications/jobs/results/85564713261245126"
    assert extract_ats_job_id(url) == "85564713261245126"


def test_extract_ats_job_id_none_when_no_recognizable_id():
    assert extract_ats_job_id("https://t.me/getjobss/7795") is None


def test_cross_source_key_prefers_job_id_over_text_real_virtu_triple():
    """Real, confirmed 2026-07-29 — a genuine TRIPLE duplicate: three
    different title strings (SimplifyJobs, zshah101, vanshb03), identical
    greenhouse.io/virtu/jobs/8624410002 URL. Company+title text alone would
    have produced three different keys; the job-id key collapses all three."""
    url = "https://job-boards.greenhouse.io/virtu/jobs/8624410002"
    keys = {
        cross_source_key("Virtu Financial", "2027 Internship - Software Engineer", url),
        cross_source_key("Virtu Financial", "Software Engineer Intern - Software Engineer", url),
        cross_source_key("Virtu Financial", "Software Engineer Intern", url),
    }
    assert len(keys) == 1


def test_cross_source_key_prefers_job_id_over_text_real_google_case():
    """Real Google BS vs MS title-string variant, same numeric job id."""
    url = "https://www.google.com/about/careers/applications/jobs/results/85564713261245126"
    assert cross_source_key("Google", "Software Engineering Intern", url) == \
        cross_source_key("Google", "Software Engineering Intern, BS, Summer 2027", url)


def test_cross_source_key_prefers_job_id_over_text_real_palantir_cross_bucket_case():
    """Real Palantir 'Intel' FDSE duplicate across two different buckets
    (SimplifyJobs landed it in AI/ML, zshah101 in Fullstack) — same Lever
    job id either way, distinct from the other three incidents in that the
    dossiers also disagreed with each other about classification."""
    assert cross_source_key(
        "Palantir", "Forward Deployed Software Engineer Intern - Intel",
        "https://jobs.lever.co/palantir/[REDACTED]/apply",
    ) == cross_source_key(
        "Palantir", "Forward Deployed Software Engineer, Internship - Intel",
        "https://jobs.lever.co/palantir/[REDACTED]",
    )


def test_cross_source_key_falls_back_to_text_for_company_name_variant_real_aquatic_case():
    """Real Aquatic vs Aquatic Capital Management: same Greenhouse posting,
    same URL — job id alone already collapses this one, but confirms the
    company-name-variant incident (the one case the original company-alias-
    map idea would have caught) is still covered."""
    url = "https://job-boards.greenhouse.io/aquaticcapitalmanagement/jobs/8489233002"
    assert cross_source_key("Aquatic", "Software Engineer Intern", url) == \
        cross_source_key("Aquatic Capital Management", "Software Engineer Intern", url)


def test_cross_source_key_falls_back_to_normalized_text_when_no_job_id():
    """A source/ATS with no recognizable job id in its URL shape (e.g.
    Freehire's Telegram links) must still fall back to the original
    normalized-company+title key rather than losing dedup entirely."""
    assert cross_source_key("MLH", "Fellowship", "https://t.me/getjobss/7795") == \
        cross_source_key("MLH", "Fellowship", "https://t.me/getjobss/9999")
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_identity.py -q 2>&1 | tail -60`
  ```
...............                                                          [100%]
15 passed in 0.03s
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
  ```diff
  - from ingestion.normalize import normalize_simplify
from vault_writer.writer import dossier_filename, load_dossier_uids, render_dossier, write_dossier
  + from ingestion.normalize import normalize_simplify
from vault_writer.writer import (
    DOSSIERS_MOC_LINK,
    REMOVED_DOSSIERS_MOC_LINK,
    build_frontmatter,
    company_slug,
    dossier_filename,
    load_dossier_uids,
    move_dossier_to_viewed,
    render_dossier,
    write_dossier,
)
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
  ```diff
  - def test_write_dossier_without_state_dir_records_no_manifest(vault_root, listing, tmp_path):
    uid = f"{listing.source}:{listing.raw_id}"
    md = render_dossier(listing, uid, "2026-07-17", "reason")

    write_dossier(vault_root, uid, md, listing.title, listing.company, "Other")

    assert not (tmp_path / "state" / "dossier_uids.json").exists()
  + def test_write_dossier_without_state_dir_records_no_manifest(vault_root, listing, tmp_path):
    uid = f"{listing.source}:{listing.raw_id}"
    md = render_dossier(listing, uid, "2026-07-17", "reason")

    write_dossier(vault_root, uid, md, listing.title, listing.company, "Other")

    assert not (tmp_path / "state" / "dossier_uids.json").exists()


# --- Task G: dossier interlinking (Internship Notes Standard §1) ---

def test_build_frontmatter_includes_moc_link_and_company_tag(listing):
    fm = build_frontmatter(listing, f"{listing.source}:{listing.raw_id}", "2026-07-17", "reason")

    assert fm["notes"] == [DOSSIERS_MOC_LINK]
    assert f"company/{company_slug(listing.company)}" in fm["tags"]
    # field order: notes immediately after next, immediately before tags
    keys = list(fm.keys())
    assert keys.index("next") + 1 == keys.index("notes")
    assert keys.index("notes") + 1 == keys.index("tags")


def test_company_slug_matches_real_standard_examples():
    assert company_slug("Appian") == "appian"
    assert company_slug("Aquatic Capital Management") == "aquatic-capital-management"


def test_company_slug_normalizes_case_and_whitespace_for_same_company_clustering():
    """Two dossiers for the same company (varying casing/whitespace) must
    produce the identical tag — Obsidian's tag pane clusters on exact string
    match, per the Standard's §1 same-company clustering rule."""
    assert company_slug("Aquatic Capital Management") == company_slug("  aquatic capital management  ")
    assert company_slug("Aquatic Capital Management") == company_slug("AQUATIC CAPITAL MANAGEMENT")


def test_render_dossier_frontmatter_contains_moc_link_and_company_tag(listing):
    uid = f"{listing.source}:{listing.raw_id}"
    md = render_dossier(listing, uid, "2026-07-17", "reason")
    assert DOSSIERS_MOC_LINK in md
    assert f"company/{company_slug(listing.company)}" in md


# --- Task H: recheck.py moves closed postings to Viewed/, doesn't delete ---

def test_move_dossier_to_viewed_moves_file_and_updates_frontmatter(vault_root, listing, state_dir):
    uid = f"{listing.source}:{listing.raw_id}"
    md = render_dossier(listing, uid, "2026-07-17", "reason")
    path = write_dossier(vault_root, uid, md, listing.title, listing.company, "Other", state_dir=state_dir)

    new_path = move_dossier_to_viewed(
        vault_root, path, "absent from live feed", "2026-07-30", state_dir=state_dir
    )

    assert not path.exists()
    assert new_path.exists()
    assert new_path.parent == vault_root / DOSSIERS_SUBPATH / "Viewed"

    text = new_path.read_text()
    assert "status: removed" in text
    assert "removed_date: '2026-07-30'" in text or "removed_date: 2026-07-30" in text
    assert "removed_reason: absent from live feed" in text
    assert DOSSIERS_MOC_LINK in text
    assert REMOVED_DOSSIERS_MOC_LINK in text


def test_move_dossier_to_viewed_updates_uid_manifest(vault_root, listing, state_dir):
    uid = f"{listing.source}:{listing.raw_id}"
    md = render_dossier(listing, uid, "2026-07-17", "reason")
    path = write_dossier(vault_root, uid, md, listing.title, listing.company, "Other", state_dir=state_dir)

    new_path = move_dossier_to_viewed(
        vault_root, path, "active: false upstream", "2026-07-30", state_dir=state_dir
    )

    manifest = load_dossier_uids(state_dir)
    assert manifest[str(new_path.relative_to(vault_root))] == uid
    assert str(path.relative_to(vault_root)) not in manifest
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_writer.py -q 2>&1 | tail -100`
  ```
................                                                         [100%]
16 passed in 0.12s
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_validate.py`
  ```diff
  - def test_validate_rejects_duplicate_uid(listing, uid):
    md = render_dossier(listing, uid, "2026-07-17", "reason")
    head = Mock(return_value=_ok_response(200))
    result = validate(listing, uid, md, seen_ids={uid}, http_head=head)
    assert result.passed is False
    assert result.check == "not_duplicate"
  + def test_validate_rejects_duplicate_uid(listing, uid):
    md = render_dossier(listing, uid, "2026-07-17", "reason")
    head = Mock(return_value=_ok_response(200))
    result = validate(listing, uid, md, seen_ids={uid}, http_head=head)
    assert result.passed is False
    assert result.check == "not_duplicate"


# --- Task G: notes: field is fail-closed required, like every other field ---

def test_format_compliance_rejects_missing_notes_field(listing, uid):
    """Confirms REQUIRED_FRONTMATTER_FIELDS actually enforces notes: — adding
    it to build_frontmatter() without also adding it here would mean the
    write gate never checks for it, silently defeating the point of the
    Internship Notes Standard §1 'always present, even null/[]' rule."""
    md = render_dossier(listing, uid, "2026-07-17", "reason")
    lines = [l for l in md.splitlines() if not l.startswith("notes:") and l.strip() != '  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"']
    broken = "\n".join(lines) + "\n"
    result = check_format_compliance(broken)
    assert result.passed is False
    assert "notes" in result.reason
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_validate.py -q 2>&1 | tail -60`
  ```
......................                                                   [100%]
22 passed in 0.31s
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Bash` — `grep -n "^def _run_once_kwargs" -A 20 /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```
282:def _run_once_kwargs(tmp_path, **overrides):
283-    kwargs = dict(
284-        jarvis_dir=tmp_path / "jarvis",
285-        state_path=tmp_path / "state" / "seen_ids.json",
286-        runs_log_path=tmp_path / "logs" / "runs.jsonl",
287-        now=datetime(2026, 7, 17, 15, 0, tzinfo=timezone.utc),  # a Friday, not rollup time
288-        profile=PROFILE,
289-        http_get=_fake_http_get,
290-        http_head=_fake_http_head_all_live,
291-        push_fn=lambda repo_dir, message: True,
292-        issue_fn=Mock(),
293-    )
294-    kwargs.update(overrides)
295-    (tmp_path / "jarvis").mkdir(parents=True, exist_ok=True)
296-    return kwargs
297-
298-
299-def test_run_once_happy_path_marks_seen_and_writes_dossiers(tmp_path):
300-    kwargs = _run_once_kwargs(tmp_path)
301-    record = run_pipeline.run_once(**kwargs)
302-
  ```
- `Bash` — `tail -5 /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```
    """Real dup from the 2026-07-18 audit: same Workday req via two routes,
    titled 'Intern Co-op' vs 'Intern/Co-op'."""
    from core.identity import cross_source_key
    assert cross_source_key("Marmon Holdings", "Data Engineering Intern Co-op") == \
        cross_source_key("Marmon Holdings", "Data Engineering Intern/Co-op")
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```diff
  -     """Real dup from the 2026-07-18 audit: same Workday req via two routes,
    titled 'Intern Co-op' vs 'Intern/Co-op'."""
    from core.identity import cross_source_key
    assert cross_source_key("Marmon Holdings", "Data Engineering Intern Co-op") == \
        cross_source_key("Marmon Holdings", "Data Engineering Intern/Co-op")
  +     """Real dup from the 2026-07-18 audit: same Workday req via two routes,
    titled 'Intern Co-op' vs 'Intern/Co-op'."""
    from core.identity import cross_source_key
    assert cross_source_key("Marmon Holdings", "Data Engineering Intern Co-op") == \
        cross_source_key("Marmon Holdings", "Data Engineering Intern/Co-op")


# --- Task A: per-bucket write budget + capacity notification (not a refusal) ---

DOSSIERS_SUBPATH = Path("10_Areas/Career/Internships/List/Dossiers")


def _seed_bucket(jarvis_dir, bucket_folder, count):
    d = Path(jarvis_dir) / DOSSIERS_SUBPATH / bucket_folder
    d.mkdir(parents=True, exist_ok=True)
    for i in range(count):
        (d / f"seed-{i}.md").write_text("placeholder\n")


def test_count_dossiers_by_bucket_counts_real_files(tmp_path):
    _seed_bucket(tmp_path, "Other", 5)
    _seed_bucket(tmp_path, "1 - AI & ML", 2)
    counts = run_pipeline.count_dossiers_by_bucket(tmp_path)
    assert counts["Other"] == 5
    assert counts["AI/ML"] == 2
    assert counts["Fullstack"] == 0


@pytest.mark.parametrize("seed_count,expect_at_capacity", [(48, False), (49, True), (50, True)])
def test_run_once_reports_bucket_at_capacity_without_refusing_writes(tmp_path, seed_count, expect_at_capacity):
    """Real fixture set writes exactly 1 'Other'-bucket item per run under the
    default budget — seeding N existing files means the post-write count is
    N+1. The write must happen either way (49 -> 50, or 50 -> 51); only
    whether the notification fires differs."""
    _seed_bucket(tmp_path, "Other", seed_count)
    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
    record = run_pipeline.run_once(**kwargs)

    assert record["written_count"] > 0  # the write happened regardless
    assert ("Other" in record["bucket_at_capacity"]) is expect_at_capacity


def test_run_once_files_issue_once_per_bucket_crossing_capacity(tmp_path):
    _seed_bucket(tmp_path, "Other", 49)
    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
    first = run_pipeline.run_once(**kwargs)
    assert "Other" in first["bucket_at_capacity"]
    capacity_issue_calls = [c for c in kwargs["issue_fn"].call_args_list if "at/over" in c.args[1]]
    assert len(capacity_issue_calls) == 1

    kwargs2 = _run_once_kwargs(
        tmp_path, jarvis_dir=kwargs["jarvis_dir"], state_path=kwargs["state_path"],
        runs_log_path=kwargs["runs_log_path"], state_dir=kwargs["state_dir"],
    )
    second = run_pipeline.run_once(**kwargs2)
    assert "Other" in second["bucket_at_capacity"]  # still at/over capacity
    capacity_issue_calls_2 = [c for c in kwargs2["issue_fn"].call_args_list if "at/over" in c.args[1]]
    assert len(capacity_issue_calls_2) == 0  # not refiled — already notified


@pytest.mark.parametrize(
    "seed_total,expect_dossier_total,expect_issue",
    [(186, 189, False), (187, 190, True), (197, 200, True)],
)
def test_run_once_global_total_thresholds(tmp_path, seed_total, expect_dossier_total, expect_issue):
    """150/170 stay informational-only (logged via dossier_total, no issue);
    190/200 additionally file a GitHub issue the first time each is crossed.
    The fixture set writes exactly 3 dossiers/run under the default budget
    (1 Other + 1 Fullstack + 1 CyS & Finance), so seed_total + 3 lands on the
    exact milestone under test."""
    _seed_bucket(tmp_path, "Other", seed_total)
    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
    record = run_pipeline.run_once(**kwargs)

    assert record["dossier_total"] == expect_dossier_total
    global_issue_calls = [c for c in kwargs["issue_fn"].call_args_list if "Total dossier count crossed" in c.args[1]]
    assert bool(global_issue_calls) is expect_issue
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_run_pipeline.py -q 2>&1 | tail -150`
  ```
............................FFFFFF                                       [100%]
=================================== FAILURES ===================================
__ test_run_once_reports_bucket_at_capacity_without_refusing_writes[49-True] ___

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-8/[REDACTED]')
seed_count = 49, expect_at_capacity = True

    @pytest.mark.parametrize("seed_count,expect_at_capacity", [(48, False), (49, True), (50, True)])
    def test_run_once_reports_bucket_at_capacity_without_refusing_writes(tmp_path, seed_count, expect_at_capacity):
        """Real fixture set writes exactly 1 'Other'-bucket item per run under the
        default budget — seeding N existing files means the post-write count is
        N+1. The write must happen either way (49 -> 50, or 50 -> 51); only
        whether the notification fires differs."""
        _seed_bucket(tmp_path, "Other", seed_count)
        kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
        record = run_pipeline.run_once(**kwargs)
    
        assert record["written_count"] > 0  # the write happened regardless
>       assert ("Other" in record["bucket_at_capacity"]) is expect_at_capacity
E       AssertionError: assert ('Other' in []) is True

tests/test_run_pipeline.py:521: AssertionError
__ test_run_once_reports_bucket_at_capacity_without_refusing_writes[50-True] ___

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-8/[REDACTED]')
seed_count = 50, expect_at_capacity = True

    @pytest.mark.parametrize("seed_count,expect_at_capacity", [(48, False), (49, True), (50, True)])
    def test_run_once_reports_bucket_at_capacity_without_refusing_writes(tmp_path, seed_count, expect_at_capacity):
        """Real fixture set writes exactly 1 'Other'-bucket item per run under the
        default budget — seeding N existing files means the post-write count is
        N+1. The write must happen either way (49 -> 50, or 50 -> 51); only
        whether the notification fires differs."""
        _seed_bucket(tmp_path, "Other", seed_count)
        kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
        record = run_pipeline.run_once(**kwargs)
    
        assert record["written_count"] > 0  # the write happened regardless
>       assert ("Other" in record["bucket_at_capacity"]) is expect_at_capacity
E       AssertionError: assert ('Other' in []) is True

tests/test_run_pipeline.py:521: AssertionError
_________ test_run_once_files_issue_once_per_bucket_crossing_capacity __________

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-8/[REDACTED]')

    def test_run_once_files_issue_once_per_bucket_crossing_capacity(tmp_path):
        _seed_bucket(tmp_path, "Other", 49)
        kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
        first = run_pipeline.run_once(**kwargs)
>       assert "Other" in first["bucket_at_capacity"]
E       AssertionError: assert 'Other' in []

tests/test_run_pipeline.py:528: AssertionError
_____________ test_run_once_global_total_thresholds[186-189-False] _____________

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-8/[REDACTED]')
seed_total = 186, expect_dossier_total = 189, expect_issue = False

    @pytest.mark.parametrize(
        "seed_total,expect_dossier_total,expect_issue",
        [(186, 189, False), (187, 190, True), (197, 200, True)],
    )
    def test_run_once_global_total_thresholds(tmp_path, seed_total, expect_dossier_total, expect_issue):
        """150/170 stay informational-only (logged via dossier_total, no issue);
        190/200 additionally file a GitHub issue the first time each is crossed.
        The fixture set writes exactly 3 dossiers/run under the default budget
        (1 Other + 1 Fullstack + 1 CyS & Finance), so seed_total + 3 lands on the
        exact milestone under test."""
        _seed_bucket(tmp_path, "Other", seed_total)
        kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
        record = run_pipeline.run_once(**kwargs)
    
>       assert record["dossier_total"] == expect_dossier_total
E       assert 3 == 189

tests/test_run_pipeline.py:556: AssertionError
_____________ test_run_once_global_total_thresholds[187-190-True] ______________

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-8/[REDACTED]')
seed_total = 187, expect_dossier_total = 190, expect_issue = True

    @pytest.mark.parametrize(
        "seed_total,expect_dossier_total,expect_issue",
        [(186, 189, False), (187, 190, True), (197, 200, True)],
    )
    def test_run_once_global_total_thresholds(tmp_path, seed_total, expect_dossier_total, expect_issue):
        """150/170 stay informational-only (logged via dossier_total, no issue);
        190/200 additionally file a GitHub issue the first time each is crossed.
        The fixture set writes exactly 3 dossiers/run under the default budget
        (1 Other + 1 Fullstack + 1 CyS & Finance), so seed_total + 3 lands on the
        exact milestone under test."""
        _seed_bucket(tmp_path, "Other", seed_total)
        kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
        record = run_pipeline.run_once(**kwargs)
    
>       assert record["dossier_total"] == expect_dossier_total
E       assert 3 == 190

tests/test_run_pipeline.py:556: AssertionError
_____________ test_run_once_global_total_thresholds[197-200-True] ______________

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-8/[REDACTED]')
seed_total = 197, expect_dossier_total = 200, expect_issue = True

    @pytest.mark.parametrize(
        "seed_total,expect_dossier_total,expect_issue",
        [(186, 189, False), (187, 190, True), (197, 200, True)],
    )
    def test_run_once_global_total_thresholds(tmp_path, seed_total, expect_dossier_total, expect_issue):
        """150/170 stay informational-only (logged via dossier_total, no issue);
        190/200 additionally file a GitHub issue the first time each is crossed.
        The fixture set writes exactly 3 dossiers/run under the default budget
        (1 Other + 1 Fullstack + 1 CyS & Finance), so seed_total + 3 lands on the
        exact milestone under test."""
        _seed_bucket(tmp_path, "Other", seed_total)
        kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
        record = run_pipeline.run_once(**kwargs)
    
>       assert record["dossier_total"] == expect_dossier_total
E       assert 3 == 200

tests/test_run_pipeline.py:556: AssertionError
=========================== short test summary info ============================
FAILED tests/test_run_pipeline.py::test_run_once_reports_bucket_at_capacity_without_refusing_writes[49-True]
FAILED tests/test_run_pipeline.py::test_run_once_reports_bucket_at_capacity_without_refusing_writes[50-True]
FAILED tests/test_run_pipeline.py::test_run_once_files_issue_once_per_bucket_crossing_capacity
FAILED tests/test_run_pipeline.py::test_run_once_global_total_thresholds[186-189-False]
FAILED tests/test_run_pipeline.py::test_run_once_global_total_thresholds[187-190-True]
FAILED tests/test_run_pipeline.py::test_run_once_global_total_thresholds[197-200-True]
6 failed, 28 passed in 1.44s
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```diff
  - def test_count_dossiers_by_bucket_counts_real_files(tmp_path):
    _seed_bucket(tmp_path, "Other", 5)
    _seed_bucket(tmp_path, "1 - AI & ML", 2)
    counts = run_pipeline.count_dossiers_by_bucket(tmp_path)
    assert counts["Other"] == 5
    assert counts["AI/ML"] == 2
    assert counts["Fullstack"] == 0


@pytest.mark.parametrize("seed_count,expect_at_capacity", [(48, False), (49, True), (50, True)])
def test_run_once_reports_bucket_at_capacity_without_refusing_writes(tmp_path, seed_count, expect_at_capacity):
    """Real fixture set writes exactly 1 'Other'-bucket item per run under the
    default budget — seeding N existing files means the post-write count is
    N+1. The write must happen either way (49 -> 50, or 50 -> 51); only
    whether the notification fires differs."""
    _seed_bucket(tmp_path, "Other", seed_count)
    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
    record = run_pipeline.run_once(**kwargs)

    assert record["written_count"] > 0  # the write happened regardless
    assert ("Other" in record["bucket_at_capacity"]) is expect_at_capacity


def test_run_once_files_issue_once_per_bucket_crossing_capacity(tmp_path):
    _seed_bucket(tmp_path, "Other", 49)
    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
    first = run_pipeline.run_once(**kwargs)
    assert "Other" in first["bucket_at_capacity"]
    capacity_issue_calls = [c for c in kwargs["issue_fn"].call_args_list if "at/over" in c.args[1]]
    assert len(capacity_issue_calls) == 1

    kwargs2 = _run_once_kwargs(
        tmp_path, jarvis_dir=kwargs["jarvis_dir"], state_path=kwargs["state_path"],
        runs_log_path=kwargs["runs_log_path"], state_dir=kwargs["state_dir"],
    )
    second = run_pipeline.run_once(**kwargs2)
    assert "Other" in second["bucket_at_capacity"]  # still at/over capacity
    capacity_issue_calls_2 = [c for c in kwargs2["issue_fn"].call_args_list if "at/over" in c.args[1]]
    assert len(capacity_issue_calls_2) == 0  # not refiled — already notified


@pytest.mark.parametrize(
    "seed_total,expect_dossier_total,expect_issue",
    [(186, 189, False), (187, 190, True), (197, 200, True)],
)
def test_run_once_global_total_thresholds(tmp_path, seed_total, expect_dossier_total, expect_issue):
    """150/170 stay informational-only (logged via dossier_total, no issue);
    190/200 additionally file a GitHub issue the first time each is crossed.
    The fixture set writes exactly 3 dossiers/run under the default budget
    (1 Other + 1 Fullstack + 1 CyS & Finance), so seed_total + 3 lands on the
    exact milestone under test."""
    _seed_bucket(tmp_path, "Other", seed_total)
    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
    record = run_pipeline.run_once(**kwargs)

    assert record["dossier_total"] == expect_dossier_total
    global_issue_calls = [c for c in kwargs["issue_fn"].call_args_list if "Total dossier count crossed" in c.args[1]]
    assert bool(global_issue_calls) is expect_issue
  + def test_count_dossiers_by_bucket_counts_real_files(tmp_path):
    _seed_bucket(tmp_path, "Other", 5)
    _seed_bucket(tmp_path, "1 - AI & ML", 2)
    counts = run_pipeline.count_dossiers_by_bucket(tmp_path)
    assert counts["Other"] == 5
    assert counts["AI/ML"] == 2
    assert counts["Fullstack"] == 0


@pytest.mark.parametrize("seed_count,expect_at_capacity", [(48, False), (49, True), (50, True)])
def test_run_once_reports_bucket_at_capacity_without_refusing_writes(tmp_path, seed_count, expect_at_capacity):
    """Real fixture set writes exactly 1 'Other'-bucket item per run under the
    default budget — seeding N existing files means the post-write count is
    N+1. The write must happen either way (49 -> 50, or 50 -> 51); only
    whether the notification fires differs."""
    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
    _seed_bucket(kwargs["jarvis_dir"], "Other", seed_count)
    record = run_pipeline.run_once(**kwargs)

    assert record["written_count"] > 0  # the write happened regardless
    assert ("Other" in record["bucket_at_capacity"]) is expect_at_capacity


def test_run_once_files_issue_once_per_bucket_crossing_capacity(tmp_path):
    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
    _seed_bucket(kwargs["jarvis_dir"], "Other", 49)
    first = run_pipeline.run_once(**kwargs)
    assert "Other" in first["bucket_at_capacity"]
    capacity_issue_calls = [c for c in kwargs["issue_fn"].call_args_list if "at/over" in c.args[1]]
    assert len(capacity_issue_calls) == 1

    kwargs2 = _run_once_kwargs(
        tmp_path, jarvis_dir=kwargs["jarvis_dir"], state_path=kwargs["state_path"],
        runs_log_path=kwargs["runs_log_path"], state_dir=kwargs["state_dir"],
    )
    second = run_pipeline.run_once(**kwargs2)
    assert "Other" in second["bucket_at_capacity"]  # still at/over capacity
    capacity_issue_calls_2 = [c for c in kwargs2["issue_fn"].call_args_list if "at/over" in c.args[1]]
    assert len(capacity_issue_calls_2) == 0  # not refiled — already notified


@pytest.mark.parametrize(
    "seed_total,expect_dossier_total,expect_issue",
    [(186, 189, False), (187, 190, True), (197, 200, True)],
)
def test_run_once_global_total_thresholds(tmp_path, seed_total, expect_dossier_total, expect_issue):
    """150/170 stay informational-only (logged via dossier_total, no issue);
    190/200 additionally file a GitHub issue the first time each is crossed.
    The fixture set writes exactly 3 dossiers/run under the default budget
    (1 Other + 1 Fullstack + 1 CyS & Finance), so seed_total + 3 lands on the
    exact milestone under test."""
    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
    _seed_bucket(kwargs["jarvis_dir"], "Other", seed_total)
    record = run_pipeline.run_once(**kwargs)

    assert record["dossier_total"] == expect_dossier_total
    global_issue_calls = [c for c in kwargs["issue_fn"].call_args_list if "Total dossier count crossed" in c.args[1]]
    assert bool(global_issue_calls) is expect_issue
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_run_pipeline.py -q 2>&1 | tail -150`
  ```
claude-sonnet-5[1m] is temporarily unavailable, so auto mode cannot determine the safety of Bash right now. Wait briefly and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_run_pipeline.py -q 2>&1 | tail -150`
  ```
..................................                                       [100%]
34 passed in 1.12s
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -30`
  ```
........................................................................ [ 23%]
........................................................................ [ 47%]
........................................................................ [ 71%]
........................................................................ [ 95%]
...............                                                          [100%]
303 passed in 1.85s
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 << 'EOF'
from core.relevance import stage1_reject, stage2_confirm
from core.classify import classify
from core.identity import cross_source_key
from ingestion.posting_page import phd_only_exclusion, extract_content

print("=== Task B: Databricks Product Management Intern ===")
print("stage1_reject:", stage1_reject("Product Management Intern (Summer 2027)", ""))

print("=== Task B: Conagra Demand Science Rotational Analyst ===")
print("stage1_reject:", stage1_reject("Demand Science Rotational Analyst", ""))

print("=== Task C: Mosaic Operations & Automation Engineering ===")
mosaic_content = (
    "Requires a Bachelor's degree in Chemical Engineering or related field. Experience with PLC, DCS, "
    "and SCADA control systems preferred. Basic computer skills required. Must be able to lift 50 lbs "
    "and wear a respirator as needed. The Company will not require an employee to perform any duty "
    "without posing a direct threat to the safety of his or her own self or others."
)
print("stage2_confirm:", stage2_confirm("Operations & Automation Engineering Co-op/Intern", "The Mosaic Company", mosaic_content))
bucket, signal = classify("Operations & Automation Engineering Co-op/Intern", "", mosaic_content)
print("classify bucket:", bucket, "signal:", repr(signal))

print("=== Task D: real dedup incidents ===")
virtu_url = "https://job-boards.greenhouse.io/virtu/jobs/8624410002"
keys = {
    cross_source_key("Virtu Financial", "2027 Internship - Software Engineer", virtu_url),
    cross_source_key("Virtu Financial", "Software Engineer Intern - Software Engineer", virtu_url),
    cross_source_key("Virtu Financial", "Software Engineer Intern", virtu_url),
}
print("Virtu triple-dup collapses to", len(keys), "key(s)")

google_key_a = cross_source_key("Google", "Software Engineering Intern", "https://www.google.com/about/careers/applications/jobs/results/85564713261245126")
google_key_b = cross_source_key("Google", "Software Engineering Intern, BS, Summer 2027", "https://www.google.com/about/careers/applications/jobs/results/85564713261245126")
print("Google BS/MS dup collapses:", google_key_a == google_key_b)

pal_a = cross_source_key("Palantir", "Forward Deployed Software Engineer Intern - Intel", "https://jobs.lever.co/palantir/9e40d77f-b07c-437b-98e7-def9b0184d89/apply")
pal_b = cross_source_key("Palantir", "Forward Deployed Software Engineer, Internship - Intel", "https://jobs.lever.co/palantir/9e40d77f-b07c-437b-98e7-def9b0184d89")
print("Palantir cross-bucket dup collapses:", pal_a == pal_b)

aq_url = "https://job-boards.greenhouse.io/aquaticcapitalmanagement/jobs/8489233002"
print("Aquatic name-variant dup collapses:", cross_source_key("Aquatic", "Software Engineer Intern", aq_url) == cross_source_key("Aquatic Capital Management", "Software Engineer Intern", aq_url))

print("=== Task F: Optiver PhD-only real content ===")
optiver_text = (
    "As part of our assessment process, you may be invited to participate in a multi-day, on-site "
    "evaluative program.\nWho You Are:\n- Currently enrolled in a PhD program in Statistics, Computer "
    "Science, Machine Learning, Mathematics, or a related STEM field with outstanding academic "
    "performance\n- Expected graduation between December 2027 - June 2029"
)
print("phd_only_exclusion:", phd_only_exclusion(optiver_text))

print("=== Task F: false-positive check on real BS/MS eligible fixtures ===")
aquatic_text = "Active student pursuing a BS, MS, or PhD in mathematics, statistics, machine learning, physics, computer science, or other scientific disciplines with an expected graduation date between Fall 2027 and Spring 2028."
appian_text = "Currently pursuing a Bachelor's or Master's degree in Computer Science or Computer Engineering with a strong academic record."
print("Aquatic (should be None):", phd_only_exclusion(aquatic_text))
print("Appian (should be None):", phd_only_exclusion(appian_text))
EOF
  ```
  ```
=== Task B: Databricks Product Management Intern ===
stage1_reject: True
=== Task B: Conagra Demand Science Rotational Analyst ===
stage1_reject: True
=== Task C: Mosaic Operations & Automation Engineering ===
stage2_confirm: False
classify bucket: Other signal: ''
=== Task D: real dedup incidents ===
Virtu triple-dup collapses to 1 key(s)
Google BS/MS dup collapses: True
Palantir cross-bucket dup collapses: True
Aquatic name-variant dup collapses: True
=== Task F: Optiver PhD-only real content ===
phd_only_exclusion: Currently enrolled in a PhD program
=== Task F: false-positive check on real BS/MS eligible fixtures ===
Aquatic (should be None): None
Appian (should be None): None
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 << 'EOF'
from ingestion.posting_page import extract_content

print("=== Task E: Google careers listing-shell extraction ===")
md = open("tests/fixtures/posting_google_careers.md", encoding="utf-8").read()
content = extract_content(md)
print(content[:300])
print("...")
print("Contains unrelated job 'Senior Product Engineer, Machine Learning Accelerators':", "Senior Product Engineer, Machine Learning Accelerators" in content)
print("Contains real posting content:", "pursuing a Master's degree" in content)
EOF
  ```
  ```
=== Task E: Google careers listing-shell extraction ===
## Software Engineering Intern, MS, Summer 2027
_share_
- _link_Copy link
- _email_Email a friend
_corporate_fare_ Google_place_ Mountain View, CA, USA; Atlanta, GA, USA; +29 more; +28 more_bar_chart_ Intern & Apprentice
**This posting is for students who want early consideration for our Summer 2027
...
Contains unrelated job 'Senior Product Engineer, Machine Learning Accelerators': False
Contains real posting content: True
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 << 'PYEOF'
from ingestion.posting_page import extract_content

# Real Conagra raw markdown reconstructed from the actual vault dossier content
# (the part after "## Posting (fetched ...)" in the dossier IS extract_content's
# prior output already run through the OLD buggy code — to test the NEW code
# we need the underlying raw fetched markdown shape, which the dossier no longer
# has since it was already processed. We approximate using the real duplicated
# structure that's visible: the About Us paragraph appears twice in the existing
# dossier body itself, which is proof enough since extract_content is idempotent-ish
# on already-partially-cleaned text for the dedup check.)

conagra_body = open("/tmp claude-test-conagra.txt") if False else None
PYEOF
  ```
  ```
(Bash completed with no output)
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 << 'PYEOF'
from ingestion.posting_page import extract_content

# Real content, copied verbatim from the Conagra Brands dossier's existing
# "## Posting (fetched 2026-07-27)" body (that body IS the old extract_content's
# broken output, since it was never deduped/split/sectioned) — using it as the
# raw input to the NEW extract_content demonstrates the fix on the real bug.
conagra_raw = """## Demand Science Rotational Analyst - Summer 2027
locationsChicago, Illinois
time typeFull time
posted onPosted Today
job requisition idReq-039400
Have a taste for something big? Launch your career at Conagra Brands, one of North America's leading branded food companies!
**Is the Demand Science Rotational Program right for you?**
Are you excited by data and translating analytics into marketplace predictions?
**Compensation**
Pay Range:$59,000-$79,000
### About Us
At Conagra Brands, we have a rich heritage of making great food. We aspire to have the most impactful, energized and inclusive culture in food. As a member of our 18,000+ person team across 40+ locations, you are empowered to reach your potential, make an impact and own your career. We're in the business of building champions - within our people and our iconic brands like Birds Eye, Slim Jim and Reddi-Wip.
Our focus on innovation extends beyond making great food, it also reflects our commitment to embracing new solutions.
### About Us
At Conagra Brands, we have a rich heritage of making great food. We aspire to have the most impactful, energized and inclusive culture in food. As a member of our 18,000+ person team across 40+ locations, you are empowered to reach your potential, make an impact and own your career. We're in the business of building champions - within our people and our iconic brands like Birds Eye, Slim Jim and Reddi-Wip.
"""

before = conagra_raw
after = extract_content(conagra_raw)
print("=== BEFORE (raw, as old extract_content would have left it) ===")
print(before)
print("=== AFTER (new extract_content) ===")
print(after)
print()
print("Duplicate paragraph count in AFTER:", after.count("As a member of our 18,000+ person team"))
print("ATS chrome split:", "locations\nChicago, Illinois" in after)
print("Compensation as heading:", "### Compensation" in after)
PYEOF
  ```
  ```
=== BEFORE (raw, as old extract_content would have left it) ===
## Demand Science Rotational Analyst - Summer 2027
locationsChicago, Illinois
time typeFull time
posted onPosted Today
job requisition idReq-039400
Have a taste for something big? Launch your career at Conagra Brands, one of North America's leading branded food companies!
**Is the Demand Science Rotational Program right for you?**
Are you excited by data and translating analytics into marketplace predictions?
**Compensation**
Pay Range:$59,000-$79,000
### About Us
At Conagra Brands, we have a rich heritage of making great food. We aspire to have the most impactful, energized and inclusive culture in food. As a member of our 18,000+ person team across 40+ locations, you are empowered to reach your potential, make an impact and own your career. We're in the business of building champions - within our people and our iconic brands like Birds Eye, Slim Jim and Reddi-Wip.
Our focus on innovation extends beyond making great food, it also reflects our commitment to embracing new solutions.
### About Us
At Conagra Brands, we have a rich heritage of making great food. We aspire to have the most impactful, energized and inclusive culture in food. As a member of our 18,000+ person team across 40+ locations, you are empowered to reach your potential, make an impact and own your career. We're in the business of building champions - within our people and our iconic brands like Birds Eye, Slim Jim and Reddi-Wip.

=== AFTER (new extract_content) ===
## Demand Science Rotational Analyst - Summer 2027
locations
Chicago, Illinois
time type
Full time
posted on
Posted Today
job requisition id
Req-039400
Have a taste for something big? Launch your career at Conagra Brands, one of North America's leading branded food companies!
**Is the Demand Science Rotational Program right for you?**
Are you excited by data and translating analytics into marketplace predictions?
### Compensation
Pay Range:$59,000-$79,000
### About Us
At Conagra Brands, we have a rich heritage of making great food. We aspire to have the most impactful, energized and inclusive culture in food. As a member of our 18,000+ person team across 40+ locations, you are empowered to reach your potential, make an impact and own your career. We're in the business of building champions - within our people and our iconic brands like Birds Eye, Slim Jim and Reddi-Wip.
Our focus on innovation extends beyond making great food, it also reflects our commitment to embracing new solutions.
### About Us

Duplicate paragraph count in AFTER: 1
ATS chrome split: True
Compensation as heading: True
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 << 'PYEOF'
from ingestion.posting_page import extract_content

manhattan_raw = """## A.I. Developer Co-Op (Boston, MA)
locationsUS - Home Office
time typeFull time
posted onPosted 15 Days Ago
We are seeking a motivated AI Developer Co-op who is currently pursuing a degree in Computer Science, Artificial Intelligence, Data Science, or a related field.
### About Us
At Manhattan Associates our supply chain and omnichannel technology positively affect how people work, shop and live - every single day.
Read More
#### Follow Us
- [LinkedIn](https://www.linkedin.com/company/4376?trk=tyah "LinkedIn")
- [X](https://twitter.com/ManhAssocNews "X")
- [Facebook](https://www.facebook.com/pages/Manhattan-Associates/113391905337615?fref=ts "Facebook")
"""
before = manhattan_raw
after = extract_content(manhattan_raw)
print("=== BEFORE ===")
print(before)
print("=== AFTER ===")
print(after)
print()
print("Read More stripped:", "Read More" not in after)
print("Follow Us stripped:", "Follow Us" not in after)
print("LinkedIn link stripped:", "linkedin.com" not in after)
PYEOF
  ```
  ```
=== BEFORE ===
## A.I. Developer Co-Op (Boston, MA)
locationsUS - Home Office
time typeFull time
posted onPosted 15 Days Ago
We are seeking a motivated AI Developer Co-op who is currently pursuing a degree in Computer Science, Artificial Intelligence, Data Science, or a related field.
### About Us
At Manhattan Associates our supply chain and omnichannel technology positively affect how people work, shop and live - every single day.
Read More
#### Follow Us
- [LinkedIn](https://www.linkedin.com/company/4376?trk=tyah "LinkedIn")
- [X](https://twitter.com/ManhAssocNews "X")
- [Facebook](https://www.facebook.com/pages/Manhattan-Associates/113391905337615?fref=ts "Facebook")

=== AFTER ===
## A.I. Developer Co-Op (Boston, MA)
locations
US - Home Office
time type
Full time
posted on
Posted 15 Days Ago
We are seeking a motivated AI Developer Co-op who is currently pursuing a degree in Computer Science, Artificial Intelligence, Data Science, or a related field.
### About Us
At Manhattan Associates our supply chain and omnichannel technology positively affect how people work, shop and live - every single day.
- [LinkedIn](https://www.linkedin.com/company/4376?trk=tyah "LinkedIn")
- [X](https://twitter.com/ManhAssocNews "X")
- [Facebook](https://www.facebook.com/pages/Manhattan-Associates/113391905337615?fref=ts "Facebook")

Read More stripped: True
Follow Us stripped: True
LinkedIn link stripped: False
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py`
  ```diff
  - _LINK_BULLET_RE = re.compile(r"^-\s*\[.+\]\(https?://\S+\)\s*$")
  + # Real Manhattan Associates link shape includes a markdown title after the
# URL ('[LinkedIn](https://...4376?trk=tyah "LinkedIn")') — the optional
# quoted-title group handles that, not just a bare '(url)'.
_LINK_BULLET_RE = re.compile(r'^-\s*\[.+\]\(https?://\S+?(?:\s+"[^"]*")?\)\s*$')
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 << 'PYEOF'
from ingestion.posting_page import extract_content

manhattan_raw = """## A.I. Developer Co-Op (Boston, MA)
locationsUS - Home Office
### About Us
At Manhattan Associates our supply chain and omnichannel technology positively affect how people work, shop and live - every single day.
Read More
#### Follow Us
- [LinkedIn](https://www.linkedin.com/company/4376?trk=tyah "LinkedIn")
- [X](https://twitter.com/ManhAssocNews "X")
- [Facebook](https://www.facebook.com/pages/Manhattan-Associates/113391905337615?fref=ts "Facebook")
"""
after = extract_content(manhattan_raw)
print(after)
print("LinkedIn stripped:", "linkedin.com" not in after)
PYEOF
python -m pytest tests/ -q 2>&1 | tail -20
  ```
  ```
## A.I. Developer Co-Op (Boston, MA)
locations
US - Home Office
### About Us
At Manhattan Associates our supply chain and omnichannel technology positively affect how people work, shop and live - every single day.
LinkedIn stripped: True
........................................................................ [ 23%]
........................................................................ [ 47%]
........................................................................ [ 71%]
........................................................................ [ 95%]
...............                                                          [100%]
303 passed in 1.07s
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 << 'PYEOF'
import json, tempfile
from pathlib import Path
from ingestion.normalize import normalize_simplify
from vault_writer.writer import render_dossier, write_dossier, move_dossier_to_viewed

raw = json.loads(Path("tests/fixtures/simplifyjobs.json").read_text())[0]
listing = normalize_simplify(raw)
uid = f"{listing.source}:{listing.raw_id}"
md = render_dossier(listing, uid, "2026-07-30", "reason")
print("=== BEFORE (Task G): rendered frontmatter ===")
print(md.split("---")[1])

with tempfile.TemporaryDirectory() as tmp:
    vault = Path(tmp) / "vault"
    state_dir = Path(tmp) / "state"
    path = write_dossier(vault, uid, md, listing.title, listing.company, "Other", state_dir=state_dir)
    print("=== Task H: AFTER move_dossier_to_viewed ===")
    new_path = move_dossier_to_viewed(vault, path, "absent from live feed", "2026-07-30", state_dir=state_dir)
    print(new_path.read_text().split("---")[1])
    print("File now at:", new_path.relative_to(vault))
PYEOF
  ```
  ```
=== BEFORE (Task G): rendered frontmatter ===

company: Palantir
title: Forward Deployed Software Engineer – Internship - US Government
url: https://jobs.lever.co/palantir/[REDACTED]/apply
source: SimplifyJobs
terms:
  - Winter 2027
  - Spring 2027
  - Summer 2027
  - Fall 2027
locations:
  - Honolulu, HI
target_year: []
date_posted: '2025-12-12'
date_found: '2026-07-30'
matched_reason: reason
status: unreviewed
next:
notes:
  - '[[10_Areas/Career/Internships/List/Dossiers MOC]]'
tags:
  - internship
  - auto-discovered
  - company/palantir

=== Task H: AFTER move_dossier_to_viewed ===

company: Palantir
title: Forward Deployed Software Engineer – Internship - US Government
url: https://jobs.lever.co/palantir/[REDACTED]/apply
source: SimplifyJobs
terms:
  - Winter 2027
  - Spring 2027
  - Summer 2027
  - Fall 2027
locations:
  - Honolulu, HI
target_year: []
date_posted: '2025-12-12'
date_found: '2026-07-30'
matched_reason: reason
status: removed
next:
notes:
  - '[[10_Areas/Career/Internships/List/Dossiers MOC]]'
  - '[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]'
tags:
  - internship
  - auto-discovered
  - company/palantir
removed_date: '2026-07-30'
removed_reason: absent from live feed

File now at: 10_Areas/Career/Internships/List/Dossiers/Viewed/Forward Deployed Software Engineer – Internship - US Government - Palantir.md
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python -m pytest tests/ -q 2>&1 | tail -10
echo "---"
git status --short | head -30
  ```
  ```
........................................................................ [ 23%]
........................................................................ [ 47%]
........................................................................ [ 71%]
........................................................................ [ 95%]
...............                                                          [100%]
303 passed in 2.19s
---
 M core/classify.py
 M core/identity.py
 M core/relevance.py
 M ingestion/posting_page.py
 M recheck.py
 M run_pipeline.py
 M tests/test_classify.py
 M tests/test_identity.py
 M tests/test_posting_page.py
 M tests/test_relevance.py
 M tests/test_run_pipeline.py
 M tests/test_validate.py
 M tests/test_writer.py
 M vault_writer/validate.py
 M vault_writer/writer.py
?? tests/fixtures/posting_google_careers.md
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
  ```diff
  -             file_github_issue(
                ISSUE_REPO,
                f"Recheck halted: mass-deletion brake at {now.isoformat()}",
                f"{record['halt_reason']}\n\nNothing was removed. Removal list:\n"
                + "\n".join(f"- `{r['uid']}`: {r['reason']}" for r in removals),
            )
  +             file_github_issue(
                ISSUE_REPO,
                f"Recheck halted: mass-move brake at {now.isoformat()}",
                f"{record['halt_reason']}\n\nNothing was moved. Removal list:\n"
                + "\n".join(f"- `{r['uid']}`: {r['reason']}" for r in removals),
            )
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -10`
  ```
........................................................................ [ 23%]
........................................................................ [ 47%]
........................................................................ [ 71%]
........................................................................ [ 95%]
...............                                                          [100%]
303 passed in 4.31s
  ```
- `ToolSearch` — `{"query":"select:mcp__jarvis__vault_patch","max_results":3}`
- `mcp__jarvis__vault_read` — `{"path":"30_Order/Standards/Internship Notes Standard.md","targetType":"heading","target":"1. Frontmatter — required fields"}`
- `mcp__jarvis__vault_read` — `{"path":"30_Order/Standards/Internship Notes Standard.md","targetType":"heading","target":["1. Frontmatter — required fields"]}`
- `ToolSearch` — `{"query":"select:mcp__jarvis__vault_get_document_map","max_results":3}`
- `mcp__jarvis__vault_get_document_map` — `{"path":"30_Order/Standards/Internship Notes Standard.md"}`
- `mcp__jarvis__vault_patch` — `{"path":"30_Order/Standards/Internship Notes Standard.md","targetType":"heading","target":["Internship Notes Standard","1. Frontmatter — required fields"],"operation":"replace","ifMatch":"0afb4d","content":"Every dossier carries exactly the fields `vault_writer/writer.py`'s `build_frontmatter()` produces, in this order: `company, title, url, source, terms, locations, target_year, date_posted, date_found, matched_reason, status, next, notes, tags`. Fail-closed, same as everywhere else in this codebase (`vault_writer/validate.py`'s `REQUIRED_FRONTMATTER_FIELDS`) — a field is present even when `null`/`[]`, never omitted.\n\n**Shipped 2026-07-30 — `notes:` interlink field.** Every dossier carries a `notes:` list (the same convention every other evergreen/MOC-style note in this vault already uses — see `Dossiers MOC.md`, `Source of Truth.md`, `System - Build Log.md`) containing:\n- **Always:** `\"[[10_Areas/Career/Internships/List/Dossiers MOC]]\"` — a dossier that doesn't point back to the MOC is exactly the \"floating note\" problem this rule exists to close.\n- **If this dossier is a removal** (moved to `Viewed/` — see §4): also `\"[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]\"`, appended, never replacing the first link — a removed dossier is still a dossier that was once live, its MOC membership is historical fact, not something removal erases.\n\n**Same-company clustering.** No per-company hub note exists anywhere in this vault (Program notes carry a plain `company:` string, not a link — checked directly against the real `Programs/Considering/Software Engineering Intern - Appian.md` note, 2026-07-29) and creating N-1 backfill edits every time a new same-company dossier lands is exactly the kind of accumulating maintenance cost this codebase's zero-LLM/deterministic ethos avoids elsewhere. **Use a tag, not a link list**: `company/<slugified-company-name>` is added to the existing `tags:` array (e.g. `company/appian`, `company/aquatic-capital-management` — same slugification rule as filenames: lowercase, spaces to hyphens, strip `\\/:*?\"<>|`). Obsidian's tag pane and a `FROM #company/x` Dataview query both cluster same-company dossiers for free, with no write-time lookup of \"what else exists for this company\" and no risk of a stale link list. If a real need for direct company-to-company wikilinks surfaces later (not hypothetical — an actual workflow that needs it), revisit; don't build the link-list version preemptively."}`
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -10`
  ```
........................................................................ [ 23%]
........................................................................ [ 47%]
........................................................................ [ 71%]
........................................................................ [ 95%]
...............                                                          [100%]
303 passed in 3.00s
  ```

## You

You are working in gupta-builds/internship-research-loop. Context: Prompt 4 (Tasks A-I: per-bucket capacity notification, product/rotational-role rejection, narrowed cybersecurity keyword matching, URL/job-ID cross-source dedup, Google careers-page extraction fix, PhD-only content gate, dossier MOC/company interlinking, move-to-Viewed on removal, structured readable body content) has been run and independently code-reviewed — 303/303 tests pass, nothing committed yet. Two real, reproducible gaps were found in that review; fix both FIRST, before any of Prompt 5's own work, and confirm the fix with a real repro before moving on — this is not optional preamble, it's the literal instruction: verify Prompt 4, fix what's broken, only then start Prompt 5's real work.

### Fix First — Two Real Gaps From The Prompt 4 Review

**Fix 1 — `extract_ats_job_id()`'s Google pattern has no domain anchor (`core/identity.py`).** Unlike the Greenhouse/Lever/Ashby patterns (each scoped to their own domain string), the Google pattern `r"careers/(?:applications/)?jobs/results/(\d+)"` matches that path shape on ANY domain. Reproduce it yourself first: `extract_ats_job_id("https://random-startup.com/careers/jobs/results/12345")` currently returns `"12345"` — a real, unrelated company's posting with a coincidentally-matching numeric ID collapses into the identical `cross_source_key` as a real Google posting and would be silently rejected as a duplicate. Fix: anchor the pattern to Google's actual domain (`google\.com` appears before the `careers/` segment in every real example seen — `www.google.com/about/careers/applications/jobs/results/...`), matching the domain-scoping discipline the other three patterns already follow. Add a regression test using the exact unrelated-domain URL above, asserting it no longer extracts a job id (or extracts one only when the domain is actually google.com).

**Fix 2 — `move_dossier_to_viewed()` has no filename-collision handling (`vault_writer/writer.py`).** `dossier_filename()` already solves exactly this problem for the original per-bucket write path (`(2)`, `(3)` suffixing on a name collision) — but bucket-scoped collision checks at write time only look within one bucket folder, so two dossiers with the identical filename can legitimately exist in two different bucket folders simultaneously (a pre-Fix-1 duplicate, or two genuinely different postings that happen to share a company+title string). If `recheck.py` later moves both into the single flat `Viewed/` folder, the second move currently overwrites the first silently — real, if narrow, data loss with zero test coverage. Fix: before writing to `vault_root / VIEWED_SUBPATH / path.name`, check for an existing file at that path and apply the same `(2)`, `(3)`-style suffixing `dossier_filename()` already implements (reuse that logic/helper directly, don't duplicate it) rather than overwriting. Add a regression test: two dossiers named identically (construct this directly, don't rely on a real collision existing in the current vault), moved to `Viewed/` in sequence, both end up present with distinct filenames.

Report both fixes with a before/after repro (the exact failing case above, now passing) before moving to Task J.

### Task Order
No task strictly blocks another except: **K before L** (the debate comparator in L reads the preference weights K adds to `core/profile.yaml`) and **L before M** (M wires the comparator into the existing per-bucket budget from Prompt 4's Task A, so the comparator needs to exist first). Suggested order: Fix 1, Fix 2 → J → K → L → M → N → O, but only K→L and L→M are hard dependencies.

### Files Touched, By Task
| File | Task |
| --- | --- |
| `core/identity.py` | Fix 1 |
| `vault_writer/writer.py` | Fix 2 |
| `core/profile.yaml` | K |
| `core/classify.py` or a new `core/niche.py` (your call — see Task K) | K, L |
| `run_pipeline.py` | L, M, N (comparator wiring, loss-tracking state, MOC-sort field) |
| `10_Areas/Career/Internships/List/Dossiers MOC.md` (vault) | N (Dataview sort only, not a code file) |

## Task J — Where the real preference data comes from (read this before K)
**Do not invent a FAANG/Fortune-100/YC-backed list.** A real, human-vetted starting point already exists in the vault: `20_Progress/Internship/Building System/Research Loop - Resources.md`'s "Named-Program Coverage Check (2026-07-29)" section names 11 real target companies/programs the human has already identified as worth prioritizing — Jane Street (FTTP), Two Sigma (First-Year), D.E. Shaw, Citadel (Launch), Google (ASDI), Microsoft (Explore), LinkedIn (First Play), MLH Fellowship, NASA OSTEM, Capital One, Bloomberg — and states plainly that only 3 of 11 have any dossier coverage at all, none confirmed as the specific named program. **Use this real list as the seed for `preferred_companies` in Task K, cite this exact source in the code comment (same citation discipline as every other rule in this codebase), and treat it as a starting point the human will edit directly in `core/profile.yaml`, not a final answer.** Read the vault CLAUDE.md's `[[30_Order/Workflows/Internship Pipeline]]` Step 2 ("Screen") reasoning too — company preference is explicitly named there as a human judgment call, never automated; this task is building the *plumbing* for that judgment to take effect at write-priority time, not automating the judgment itself.

## Task K — `preferred_companies` in `core/profile.yaml`
Add a new field, same style/shape as the existing `terms_weight` (a dict, not a flat list, so it's ready for tiered weighting from the start — matching this file's existing convention of "a weight, not a second pass/fail gate"):
```yaml
preferred_companies:
  "Jane Street": high
  "Two Sigma": high
  "D.E. Shaw": high
  "Citadel": high
  "Google": high
  "Microsoft": high
  "LinkedIn": high
  "MLH": high
  "NASA": high
  "Capital One": high
  "Bloomberg": high
```
(Seeded from Task J's real source, all at one tier for now — the human will re-tier or add/remove entries directly; don't invent a multi-tier scheme not asked for.) Write a `company_matches_preference(company: str, preferred: dict) -> str | None` helper (returns the matched preference tier or `None`) in `core/identity.py` (alongside the other identity/matching helpers) — normalize the same way `cross_source_key()`'s `norm()` does (case/punctuation-insensitive), so "D.E. Shaw" and "DE Shaw" both match. This is a **pure string match against an already-fetched field** (`listing.company`) — no new network call, no new API, nothing to verify live before building, unlike every *source* addition this project has previously required real-data verification for (this is config wiring, not a new data source).

## Task L — The "debate": a deterministic pairwise comparator, replacing `_prioritize_and_cap`'s recency-only sort
**This must stay zero-LLM — no exception, this is the single easiest place in this whole feature to reach for an actual model call ("have Claude judge which is better") and it is explicitly forbidden here, same rule as everywhere else in this codebase's unattended path (see the repo's own `CLAUDE.md`).** "Debating between two internships" is implemented as a real comparator function taking exactly two candidates and returning which one wins — used via `functools.cmp_to_key()` to produce a full deterministic ranking in one efficient sort, which is mathematically the same outcome as running every pairwise comparison, just without the wasted O(n²) redundant comparisons a literal round-robin would do. Write `debate_compare(a, b, preferred_companies: dict) -> int` (standard `cmp` semantics: negative if `a` should rank first) with this exact priority order, each stage only breaking ties left by the stage above it — do not blend them into one weighted numeric score, keep them as clearly separable comparison stages so a human reading the function can see exactly why any two candidates were ordered the way they were:
1. **Preferred-company tier** — a `"high"`-tier match ranks above no match (ties within the same tier fall through to the next stage). Uses Task K's `company_matches_preference()`.
2. **Bucket fill-need** — if two candidates are headed for different buckets, the bucket further from filling this run's per-bucket budget (Prompt 4 Task A's `MAX_NEW_WRITES_PER_RUN`) ranks first, so a bucket that's about to go unfilled this run doesn't lose its only strong candidate to another bucket's tie-break. (Same-bucket comparisons skip this stage entirely — it only matters cross-bucket.)
3. **Recency** — most-recently-posted-first, the existing rule, unchanged, as the final tie-break.
Replace `_prioritize_and_cap`'s current `sorted(items, key=lambda item: item[1].date_posted or 0, reverse=True)` with the comparator-based sort, per bucket, keeping everything else about that function's structure (per-bucket budget scoping, deferred list) unchanged. Tests: construct at least one real-shaped pairwise case for each of the three stages independently (a preferred-vs-non-preferred pair with identical dates; two same-tier candidates in different buckets where one bucket's budget is nearly exhausted; two candidates with everything else equal except date), asserting the comparator orders each pair correctly in isolation before testing it inside the full per-bucket sort.

## Task M — Per-push limit stays Prompt 4's existing mechanism — don't build a second one
The "strict limit for per push to Jarvis" already exists: Prompt 4 Task A's per-bucket `MAX_NEW_WRITES_PER_RUN` dict. Task L's comparator changes *which* candidates fill those slots — it does not need, and should not get, a second/parallel limit mechanism layered on top. If real data after this ships suggests the per-bucket numbers themselves (currently 3/3/3/1) need retuning now that preference is part of selection, that's a one-line constant change to make later against real observed data, not something to redesign speculatively now.

## Task N — Loss tracking and the excluded list
A candidate that loses this run's per-bucket comparator sort (falls outside the top-N budget slots) is already "deferred" under Prompt 4's existing mechanism (never marked seen, naturally re-offered next run — no new state needed for that part). New for this task: track how many consecutive runs a given uid has been deferred, in `state/debate_losses.json` (uid → count, same load/save pattern as `state/capacity_notified.json` from Prompt 4 Task A). Each run: increment the counter for every deferred uid still in the candidate pool; a uid that gets written this run (it won its comparison) is removed from this file entirely (it's in `seen_ids.json` now, moot). **When a uid's counter reaches 5** (tunable constant, named clearly — chosen to give a real posting several genuine chances across multiple hourly runs before conceding it structurally can't out-rank the field, not an arbitrary guess dressed as one; retune from real data once this has run for a while, same as every other tunable in this codebase), move its uid to `state/excluded_uids.json` and remove it from `state/debate_losses.json`. `fetch_and_filter()`/`dedup_new()` should skip any uid already in the excluded set entirely (saves the Firecrawl content-fetch too, not just the write) — but **this is not a silent, permanent, unrecoverable exclusion**: append one line to a plain markdown log the first time a uid is excluded (new file, `10_Areas/Career/Internships/List/Excluded — Losing The Debate.md`, same append-only pattern as `Run Log.md`'s weekly rollup — company, title, url, date excluded, why) so a human can review what got excluded and manually decide to promote one by hand if they disagree — this codebase's whole design philosophy is that a human makes the final call on genuinely borderline cases, and losing a deterministic comparator five times in a row is exactly the kind of thing that should stay reviewable, not final. Tests: a uid deferred 4 times is still in the candidate pool on run 5; a uid deferred 5 times is excluded and skipped on run 6 (never fetched, confirm via a mock that the fetch function isn't even called for it); a uid that wins on attempt 3 never gets excluded.

## Task O — Niche visibility, without another folder migration
**Do not restructure `BUCKET_FOLDERS` or add a fifth priority subfolder for this.** The four-bucket system just stabilized after Prompt 4 and a manual vault reorg — re-migrating it again this soon for a feature that can be expressed as a field is not worth the churn. Instead: add a `preference_tier` frontmatter field to `build_frontmatter()` (the matched tier from Task K's `company_matches_preference()`, or `null`) — required field like every other one (add to `vault_writer/validate.py`'s `REQUIRED_FRONTMATTER_FIELDS`, same fail-closed discipline as the rest of this file). In the vault (not code — a direct markdown edit to `10_Areas/Career/Internships/List/Dossiers MOC.md`, same as the capacity notification added 2026-07-29), add `SORT preference_tier DESC, company ASC` to each bucket's existing Dataview table so preferred-company dossiers surface first within their existing bucket, no new folder needed. If a real, later need for a dedicated folder surfaces (not hypothetical), that's an explicit separate ask to the human, not something to build ahead of that need.

## Task P — Resource check: this feature needs none, state that plainly
Confirm explicitly in your final report: Tasks K-O introduce zero new network calls, zero new API usage, and zero new Firecrawl fetches — the entire mechanism is string-matching an already-fetched `company` field against a human-maintained config dict, plus bookkeeping in two small JSON state files. If a future ask wants live company-tier lookup (e.g. auto-detecting "is this company YC-backed" instead of a human-curated list), that is a materially different, higher-cost feature requiring its own real-data verification pass (same discipline as every source addition in this project's history) — explicitly out of scope here, don't fold it in silently.

## Verification
Run the full test suite, report the exact pass count. Report the two Fix-First items with real before/after repros. Report Tasks J-P individually — for K, show the actual `core/profile.yaml` diff; for L, show all three comparator-stage test cases passing in isolation plus the full per-bucket sort test; for N, show the 4-losses-still-in-pool / [REDACTED] / [REDACTED] cases explicitly; for O, show the real rendered frontmatter of a test dossier with a preference match. State plainly which parts were exercised against real data (the real Task J company list, a real comparator run) versus synthetic test fixtures — this feature has less "real broken data" to point at than Prompt 4 did (nothing has failed live yet, by design, since this is new behavior), so be explicit about what "real" means for each task here specifically. Nothing should be committed without being asked first, same as always.

## Claude

Let's start with the two required fixes. First, let me look at the current `core/identity.py` and `vault_writer/writer.py`.

Let me reproduce Fix 1's bug first, then fix it.

Confirmed the bug — returns `12345` for an unrelated domain. Now fix it:

Fix 1 confirmed working. Now let's run the existing test suite to make sure nothing regressed, then add the regression test:

Good, no regressions. Now let's add the regression test to `test_identity.py`:

Now Fix 2 — filename collision in `move_dossier_to_viewed()`. Let me reproduce the bug first:

Confirmed — silent overwrite, real data loss. Now let's fix it, reusing `dossier_filename()`'s collision logic:

Let me simplify the logic — `dossier_filename()` already guarantees no collision internally, so that follow-up check is dead code:

Now let's re-run the repro:

Fix 2 confirmed working — both files now coexist with distinct names, no data loss. Let's run the full suite and add the regression test.

Now let's add the regression test for Fix 2 to `test_writer.py`:

Both fixes confirmed and tested. Now on to Task J and reading the vault's real source data before Task K.

Now let's implement Task K — `preferred_companies` in `profile.yaml` and the matching helper.

Now the `company_matches_preference()` helper in `core/identity.py`:

Real bug — my normalization doesn't actually make "D.E. Shaw" and "DE Shaw" match. Let me verify and think through the right fix:

`cross_source_key`'s space-preserving norm doesn't satisfy the D.E. Shaw/DE Shaw example — I need full alnum-only folding (no space) for company-name matching specifically, since these are short identifiers, not multi-word text needing word-boundary preservation:

Now confirmed working correctly. Let's add tests for Task K:

All pass. Now Task L — the deterministic pairwise comparator. Let's look at `_prioritize_and_cap` and `classify` again:

This is a genuinely ambiguous spec point — the "bucket fill-need" stage needs cross-bucket comparisons, but `_prioritize_and_cap` sorts strictly within same-bucket groups (unchanged per instruction), so that stage can never actually fire in production. Let me verify this architecturally before implementing, so I don't build against a wrong assumption.

Now let's implement `core/debate.py` with the comparator:

Now wire it into `_prioritize_and_cap` in `run_pipeline.py`:

Now update `run_once` to pass `preferred_companies` from the profile:

Now let's run the full suite to check for regressions:

All 309 pass. Now let's write the Task L test cases per the spec — each stage tested in isolation, plus the full per-bucket sort.

Let's create a dedicated test file for the debate comparator instead of cluttering `test_run_pipeline.py`:

All 7 pass, exercising every stage in isolation. Now let's add the full per-bucket sort integration test to `test_run_pipeline.py`:

All pass. Now let's run the full suite before moving to Task N:

Now let's implement Task N — loss tracking and the excluded list. First, add the append-log helper to `core/run_log.py`:

Let's check the existing `test_run_log.py` still passes with this refactor:

Good. Now let's implement the debate-loss tracking mechanism in `run_pipeline.py`:

Now let's add the constants and helper functions after the capacity-notification block:

Now let's update `fetch_and_filter` and `dedup_new` to skip excluded uids:

Now let's wire this into `run_once`:

Now let's add the debate-loss bookkeeping after `written_uids` is computed:

Now let's run the full suite to check for regressions:

All 318 still pass. Now let's write the Task N tests — the pure-function tests for the counting/exclusion logic, plus the integration test for skip-and-no-fetch behavior.

No `__init__.py` in tests/ — relative import will fail. Let me fix to a plain absolute import instead:

Let me also clean up the leftover placeholder assertion in the integration test:

Also remove the now-unused `pytest` import check and run the tests:

All 7 pass, including the integration test confirming the excluded uid is never fetched. Let's run the full suite:

Let me clean up the unused `pytest` import in the new test file:

Now Task O — the `preference_tier` frontmatter field. Let's look at how `render_dossier`/`build_frontmatter` are called from `run_pipeline.py`:

Now update `REQUIRED_FRONTMATTER_FIELDS` in `validate.py`:

Now wire `preferred_companies` through `validate_and_write` in `run_pipeline.py`:

`profile` is already threaded through — let's use `profile.get("preferred_companies")` directly instead of adding a new parameter:

Now let's run the full test suite to check for regressions from adding a required frontmatter field:

That test's assertion is now stale since `preference_tier` sits between `notes` and `tags`. Let me update it to reflect the new field order:

All 325 pass. Now let's add tests for Task O — a real dossier with a preference match, and a validate.py test for `preference_tier` field enforcement:

Let's add Task O tests right after the Task G test we just fixed:

Now let's add the `validate.py` test for `preference_tier` fail-closed enforcement:

All 329 tests pass. Now let's update the vault MOC's Dataview sort per Task O's explicit vault-edit instruction:

All four bucket tables updated with the preference sort. Let's verify the final state:

All four bucket tables correctly show `preference_tier` and sort by it. Let's run the full test suite one final time to confirm everything is still green:

Let's produce clean demonstrations for the report — Task L's isolated stage tests, Task N's three named scenarios, and Task O's real frontmatter:

All demonstrations confirmed. Let's do a final full-suite run and git diff summary for the report.

329/329 tests pass. Here's the full report.

## Fix First — both confirmed broken, fixed, and re-verified

**Fix 1** (`core/identity.py`): the Google job-ID pattern had no domain anchor. Repro before: `extract_ats_job_id("https://random-startup.com/careers/jobs/results/12345")` → `"12345"`. Anchored to `google\.com/.*?careers/...`. After: returns `None` for the unrelated domain, still extracts correctly from real Google URLs. Regression test added.

**Fix 2** (`vault_writer/writer.py`): `move_dossier_to_viewed()` had no collision handling. Repro before: two distinct dossiers sharing a filename across two bucket folders → second move silently overwrote the first (`p1 == p2`, one file survived). Now reuses `dossier_filename()`'s `(2)`/`(3)`-suffixing logic. After: both files coexist with distinct names, both bodies intact. Regression test added.

## Tasks J–P

- **J**: Read the real vault source (`Research Loop - Resources.md`'s Named-Program Coverage Check) and the Internship Pipeline's Step 2 reasoning — cited directly in the `profile.yaml` comment.
- **K**: `preferred_companies` added to `core/profile.yaml` (diff shown above), seeded from the real 11-company list, all `"high"`. `company_matches_preference()` added to `core/identity.py` — required a different normalization than `cross_source_key()`'s (full alnum-fold, not space-preserving) to actually satisfy the "D.E. Shaw" / "DE Shaw" example; caught and fixed this via a real repro before writing tests.
- **L**: `core/debate.py`'s `debate_compare()` — 3 stages, all tested in isolation (7/7 pass) plus the full per-bucket sort (5/5 pass, shown above). **Important caveat, stated plainly**: stage 2 (bucket fill-need) is specified and correctly tested in isolation, but `_prioritize_and_cap` partitions by bucket before sorting (kept unchanged per instruction), so every comparator call it actually makes is same-bucket — stage 2 has no live effect in the current call path. It's real, correct, and would activate immediately if a future architecture ever compared cross-bucket candidates directly; it isn't dead code, just not currently reachable in production.
- **M**: Confirmed — no second limit mechanism. `MAX_NEW_WRITES_PER_RUN` remains the sole budget; the comparator only reorders within it.
- **N**: Loss tracking (`state/debate_losses.json`) + exclusion (`state/excluded_uids.json`) + reviewable markdown log, all in `run_pipeline.py`/`core/run_log.py`. All three named scenarios pass (shown above): 4-losses-still-in-pool, 5th-loss-excludes, wins-never-excluded (tested as pure-function scenarios — deliberately decomposed from the full multi-round pipeline for determinism, plus one integration test with pre-seeded excluded state confirming a mocked `fetch_page_fn` is never called for the excluded URL).
- **O**: `preference_tier` added to `build_frontmatter()`/`REQUIRED_FRONTMATTER_FIELDS`; real rendered frontmatter with a match shown above. Vault's `Dossiers MOC.md` updated directly (all 4 bucket tables) with `SORT preference_tier DESC, company ASC` — no folder restructuring.
- **P**: Confirmed — Tasks K–O add zero new network calls, zero new APIs, zero new Firecrawl fetches. Everything is string-matching an already-fetched `company` field against a human-maintained config dict, plus two small JSON state files and one markdown log.

**What's real vs. synthetic**: Task J's company list and Task K's matching are exercised against real vault data. Task L's stage-1/stage-3 logic and Task O's field wiring are exercised with real fixture listings (mutated company field to demonstrate the match, since no real fixture happens to be a preferred company). Task L's stage-2 and all of Task N are necessarily synthetic — this is genuinely new behavior with no real broken data to point at yet, unlike Prompt 4.

Nothing has been committed.

**Tool calls:**

- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/identity.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
python3 -c "
from core.identity import extract_ats_job_id
print(extract_ats_job_id('https://random-startup.com/careers/jobs/results/12345'))
"
  ```
  ```
12345
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/identity.py`
  ```diff
  -     # Google's own careers site embeds a long numeric id after .../jobs/results/
    re.compile(r"careers/(?:applications/)?jobs/results/(\d+)", re.I),
  +     # Google's own careers site embeds a long numeric id after .../jobs/results/
    # — anchored to google.com (real examples: www.google.com/about/careers/
    # applications/jobs/results/...), matching the domain-scoping discipline
    # the other three patterns already follow. Real bug, confirmed 2026-07-30:
    # without the domain anchor, this pattern matched the same path shape on
    # ANY domain (e.g. a random unrelated company's own careers page happening
    # to use a numeric job id at .../careers/jobs/results/<id>), which would
    # silently collapse an unrelated posting into the same cross_source_key
    # as a real Google posting and reject it as a duplicate.
    re.compile(r"google\.com/[^/]*careers/(?:applications/)?jobs/results/(\d+)", re.I),
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/identity.py`
  ```diff
  -     re.compile(r"google\.com/[^/]*careers/(?:applications/)?jobs/results/(\d+)", re.I),
  +     re.compile(r"google\.com/.*?careers/(?:applications/)?jobs/results/(\d+)", re.I),
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 -c "
from core.identity import extract_ats_job_id
print('unrelated domain (should be None):', extract_ats_job_id('https://random-startup.com/careers/jobs/results/12345'))
print('real Google URL (should extract):', extract_ats_job_id('https://www.google.com/about/careers/applications/jobs/results/95141459539174086'))
print('real Google URL 2 (should extract):', extract_ats_job_id('https://www.google.com/about/careers/applications/jobs/results/85564713261245126'))
"
  ```
  ```
unrelated domain (should be None): None
real Google URL (should extract): 95141459539174086
real Google URL 2 (should extract): 85564713261245126
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -20`
  ```
........................................................................ [ 23%]
........................................................................ [ 47%]
........................................................................ [ 71%]
........................................................................ [ 95%]
...............                                                          [100%]
303 passed in 3.04s
  ```
- `Bash` — `grep -n "google_careers_results_url\|test_extract_ats_job_id" /home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py`
  ```
59:def test_extract_ats_job_id_greenhouse():
63:def test_extract_ats_job_id_lever_ignores_apply_suffix():
72:def test_extract_ats_job_id_google_careers_results_url():
80:def test_extract_ats_job_id_none_when_no_recognizable_id():
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py`
  ```diff
  - def test_extract_ats_job_id_none_when_no_recognizable_id():
    assert extract_ats_job_id("https://t.me/getjobss/7795") is None
  + def test_extract_ats_job_id_none_when_no_recognizable_id():
    assert extract_ats_job_id("https://t.me/getjobss/7795") is None


def test_extract_ats_job_id_google_pattern_is_domain_anchored():
    """Fix 1, Prompt 5 review (2026-07-30): the Google pattern used to have no
    domain anchor, unlike the Greenhouse/Lever/Ashby patterns above — it
    matched the .../careers/jobs/results/<id> path shape on ANY domain, so an
    unrelated company's own careers page with a coincidentally-matching
    numeric id would collapse into the same cross_source_key as a real Google
    posting and get silently rejected as a duplicate."""
    assert extract_ats_job_id("https://random-startup.com/careers/jobs/results/12345") is None
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 -c "
import tempfile
from pathlib import Path
from vault_writer.writer import move_dossier_to_viewed, DOSSIER_SUBPATH

with tempfile.TemporaryDirectory() as tmp:
    vault = Path(tmp)
    a_dir = vault / DOSSIER_SUBPATH / 'Other'
    b_dir = vault / DOSSIER_SUBPATH / '1 - AI & ML'
    a_dir.mkdir(parents=True)
    b_dir.mkdir(parents=True)
    fm = '''---
company: Acme
title: SWE Intern
url: https://acme.example/a
source: SimplifyJobs
terms: []
locations: []
target_year: []
date_posted:
date_found: '2026-07-17'
matched_reason: reason
status: unreviewed
next:
notes:
  - x
tags:
  - internship
---
# SWE Intern
Content A
'''
    fm_b = fm.replace('Content A', 'Content B').replace('acme.example/a', 'acme.example/b')
    (a_dir / 'SWE Intern - Acme.md').write_text(fm)
    (b_dir / 'SWE Intern - Acme.md').write_text(fm_b)

    p1 = move_dossier_to_viewed(vault, a_dir / 'SWE Intern - Acme.md', 'absent from live feed', '2026-07-30')
    p2 = move_dossier_to_viewed(vault, b_dir / 'SWE Intern - Acme.md', 'absent from live feed', '2026-07-30')
    print('p1:', p1)
    print('p2:', p2)
    print('p1 == p2 (collision, data loss):', p1 == p2)
    viewed_dir = vault / DOSSIER_SUBPATH / 'Viewed'
    print('files in Viewed/:', list(viewed_dir.iterdir()))
"

  ```
  ```
p1: /tmp/tmpcgnk4g8w/10_Areas/Career/Internships/List/Dossiers/Viewed/SWE Intern - Acme.md
p2: /tmp/tmpcgnk4g8w/10_Areas/Career/Internships/List/Dossiers/Viewed/SWE Intern - Acme.md
p1 == p2 (collision, data loss): True
files in Viewed/: [PosixPath('/tmp/tmpcgnk4g8w/10_Areas/Career/Internships/List/Dossiers/Viewed/SWE Intern - Acme.md')]
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
  ```diff
  -     new_path = vault_root / VIEWED_SUBPATH / path.name
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path.write_text("---\n" + dump_frontmatter(frontmatter) + "---\n" + body)
    path.unlink()
  +     # Fix 2, Prompt 5 review (2026-07-30): two dossiers with identical
    # filenames can legitimately coexist in two different bucket folders
    # (bucket-scoped collision checks at write time only look within one
    # bucket) — moving both into the single flat Viewed/ folder must not let
    # the second overwrite the first. Reuse dossier_filename()'s existing
    # '(2)', '(3)'-suffixing collision logic rather than duplicating it: it
    # already takes a bare "role - company" base and a set of existing names,
    # so split path.stem back into role/company at the ' - ' this pipeline's
    # own filenames always use.
    viewed_dir = vault_root / VIEWED_SUBPATH
    viewed_dir.mkdir(parents=True, exist_ok=True)
    existing_names = {p.name for p in viewed_dir.glob("*.md")}
    stem = path.stem
    role, _, company = stem.rpartition(" - ")
    new_name = dossier_filename(role or stem, company, existing_names) if role else path.name
    if not role or new_name in existing_names:
        # No ' - ' separator to split on (a hand-renamed or malformed
        # filename) — fall back to suffixing the whole stem directly, same
        # collision-avoidance behavior dossier_filename() provides, just
        # without a role/company split to build on.
        new_name = path.name
        n = 2
        while new_name in existing_names:
            new_name = f"{stem} ({n}){path.suffix}"
            n += 1
    new_path = viewed_dir / new_name
    new_path.write_text("---\n" + dump_frontmatter(frontmatter) + "---\n" + body)
    path.unlink()
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
  ```diff
  -     viewed_dir = vault_root / VIEWED_SUBPATH
    viewed_dir.mkdir(parents=True, exist_ok=True)
    existing_names = {p.name for p in viewed_dir.glob("*.md")}
    stem = path.stem
    role, _, company = stem.rpartition(" - ")
    new_name = dossier_filename(role or stem, company, existing_names) if role else path.name
    if not role or new_name in existing_names:
        # No ' - ' separator to split on (a hand-renamed or malformed
        # filename) — fall back to suffixing the whole stem directly, same
        # collision-avoidance behavior dossier_filename() provides, just
        # without a role/company split to build on.
        new_name = path.name
        n = 2
        while new_name in existing_names:
            new_name = f"{stem} ({n}){path.suffix}"
            n += 1
    new_path = viewed_dir / new_name
  +     viewed_dir = vault_root / VIEWED_SUBPATH
    viewed_dir.mkdir(parents=True, exist_ok=True)
    existing_names = {p.name for p in viewed_dir.glob("*.md")}
    stem = path.stem
    role, sep, company = stem.rpartition(" - ")
    if sep:
        new_name = dossier_filename(role, company, existing_names)
    else:
        # No ' - ' separator to split on (a hand-renamed or malformed
        # filename) — fall back to suffixing the whole stem directly, same
        # collision-avoidance behavior dossier_filename() provides, just
        # without a role/company split to build on.
        new_name = path.name
        n = 2
        while new_name in existing_names:
            new_name = f"{stem} ({n}){path.suffix}"
            n += 1
    new_path = viewed_dir / new_name
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 -c "
import tempfile
from pathlib import Path
from vault_writer.writer import move_dossier_to_viewed, DOSSIER_SUBPATH

with tempfile.TemporaryDirectory() as tmp:
    vault = Path(tmp)
    a_dir = vault / DOSSIER_SUBPATH / 'Other'
    b_dir = vault / DOSSIER_SUBPATH / '1 - AI & ML'
    a_dir.mkdir(parents=True)
    b_dir.mkdir(parents=True)
    fm = '''---
company: Acme
title: SWE Intern
url: https://acme.example/a
source: SimplifyJobs
terms: []
locations: []
target_year: []
date_posted:
date_found: '2026-07-17'
matched_reason: reason
status: unreviewed
next:
notes:
  - x
tags:
  - internship
---
# SWE Intern
Content A
'''
    fm_b = fm.replace('Content A', 'Content B').replace('acme.example/a', 'acme.example/b')
    (a_dir / 'SWE Intern - Acme.md').write_text(fm)
    (b_dir / 'SWE Intern - Acme.md').write_text(fm_b)

    p1 = move_dossier_to_viewed(vault, a_dir / 'SWE Intern - Acme.md', 'absent from live feed', '2026-07-30')
    p2 = move_dossier_to_viewed(vault, b_dir / 'SWE Intern - Acme.md', 'absent from live feed', '2026-07-30')
    print('p1:', p1.name)
    print('p2:', p2.name)
    print('p1 == p2 (should be False now):', p1 == p2)
    viewed_dir = vault / DOSSIER_SUBPATH / 'Viewed'
    print('files in Viewed/:', sorted(p.name for p in viewed_dir.iterdir()))
    print('p1 content preserved:', 'Content A' in p1.read_text())
    print('p2 content preserved:', 'Content B' in p2.read_text())
"

  ```
  ```
p1: SWE Intern - Acme.md
p2: SWE Intern - Acme (2).md
p1 == p2 (should be False now): False
files in Viewed/: ['SWE Intern - Acme (2).md', 'SWE Intern - Acme.md']
p1 content preserved: True
p2 content preserved: True
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -20`
  ```
........................................................................ [ 23%]
........................................................................ [ 47%]
........................................................................ [ 71%]
........................................................................ [ 94%]
................                                                         [100%]
304 passed in 2.35s
  ```
- `Bash` — `grep -n "def test_move_dossier_to_viewed" /home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
  ```
179:def test_move_dossier_to_viewed_moves_file_and_updates_frontmatter(vault_root, listing, state_dir):
200:def test_move_dossier_to_viewed_updates_uid_manifest(vault_root, listing, state_dir):
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
  ```diff
  -     manifest = load_dossier_uids(state_dir)
    assert manifest[str(new_path.relative_to(vault_root))] == uid
    assert str(path.relative_to(vault_root)) not in manifest
  +     manifest = load_dossier_uids(state_dir)
    assert manifest[str(new_path.relative_to(vault_root))] == uid
    assert str(path.relative_to(vault_root)) not in manifest


def test_move_dossier_to_viewed_does_not_overwrite_filename_collision(vault_root):
    """Fix 2, Prompt 5 review (2026-07-30): two dossiers with the identical
    filename can legitimately coexist in two different bucket folders
    (bucket-scoped collision checks at write time only look within one
    bucket folder). Moving both into the single flat Viewed/ folder must not
    let the second move silently overwrite the first — real data loss with
    zero prior test coverage. Constructed directly rather than relying on a
    real collision existing in the current vault."""
    fm_template = """---
company: Acme
title: SWE Intern
url: https://acme.example/{slug}
source: SimplifyJobs
terms: []
locations: []
target_year: []
date_posted:
date_found: '2026-07-17'
matched_reason: reason
status: unreviewed
next:
notes:
  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"
tags:
  - internship
---
# SWE Intern
Content {label}
"""
    a_dir = vault_root / DOSSIERS_SUBPATH / "Other"
    b_dir = vault_root / DOSSIERS_SUBPATH / "1 - AI & ML"
    a_dir.mkdir(parents=True, exist_ok=True)
    b_dir.mkdir(parents=True, exist_ok=True)
    (a_dir / "SWE Intern - Acme.md").write_text(fm_template.format(slug="a", label="A"))
    (b_dir / "SWE Intern - Acme.md").write_text(fm_template.format(slug="b", label="B"))

    p1 = move_dossier_to_viewed(vault_root, a_dir / "SWE Intern - Acme.md", "absent from live feed", "2026-07-30")
    p2 = move_dossier_to_viewed(vault_root, b_dir / "SWE Intern - Acme.md", "absent from live feed", "2026-07-30")

    assert p1 != p2
    assert p1.exists() and p2.exists()
    assert "Content A" in p1.read_text()
    assert "Content B" in p2.read_text()
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_writer.py tests/test_identity.py -q 2>&1 | tail -30`
  ```
.................................                                        [100%]
33 passed in 0.28s
  ```
- `mcp__jarvis__vault_read` — `{"path":"20_Progress/Internship/Building System/Research Loop - Resources.md","targetType":"heading","target":["Named-Program Coverage Check (2026-07-29)"]}`
- `mcp__jarvis__vault_get_document_map` — `{"path":"20_Progress/Internship/Building System/Research Loop - Resources.md"}`
- `mcp__jarvis__vault_read` — `{"path":"20_Progress/Internship/Building System/Research Loop - Resources.md","targetType":"heading","target":["Research Loop — Resources","Named-Program Coverage Check (2026-07-29) — Real Gap, Not Yet Fixed"]}`
- `mcp__jarvis__vault_get_document_map` — `{"path":"30_Order/Workflows/Internship Pipeline.md"}`
- `mcp__jarvis__vault_read` — `{"path":"30_Order/Workflows/Internship Pipeline.md","targetType":"heading","target":["Internship Pipeline","Step 2 — Screen (the fit test)"]}`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/profile.yaml`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/profile.yaml`
  ```diff
  - # Real live values use the apostrophe form ("Bachelor's" 5450, ("Master's","PhD")
# 592, ("PhD",) 586, empty 4676 — fetched 2026-07-18). Permissive: empty degrees
# data passes; non-empty must intersect this list.
degrees_allow: ["Bachelor's"]
  + # Real live values use the apostrophe form ("Bachelor's" 5450, ("Master's","PhD")
# 592, ("PhD",) 586, empty 4676 — fetched 2026-07-18). Permissive: empty degrees
# data passes; non-empty must intersect this list.
degrees_allow: ["Bachelor's"]
# Preference weight for the debate comparator (Prompt 5 Task L), not a filter
# gate — a non-matching company still passes everything above unaffected.
# Seeded from the real, human-vetted target list in the vault's
# `20_Progress/Internship/Building System/Research Loop - Resources.md`
# "Named-Program Coverage Check (2026-07-29)" section: 11 named early-talent
# programs the human already identified as worth prioritizing, of which only
# 3/11 have ANY dossier coverage today and none confirmed as the specific
# named program (Jane Street FTTP, Two Sigma First-Year, D.E. Shaw, Citadel
# Launch, Google ASDI, Microsoft Explore, LinkedIn First Play, MLH
# Fellowship, NASA OSTEM, Capital One, Bloomberg). This is a starting point
# for the human to re-tier or add/remove entries directly, not a final
# answer — company preference is an explicit human judgment call per
# `30_Order/Workflows/Internship Pipeline.md`'s Step 2 ("Screen"), and this
# dict only wires that judgment into write-priority ordering, it doesn't
# automate the judgment itself. All seeded at one tier for now; a
# multi-tier scheme wasn't asked for.
preferred_companies:
  "Jane Street": high
  "Two Sigma": high
  "D.E. Shaw": high
  "Citadel": high
  "Google": high
  "Microsoft": high
  "LinkedIn": high
  "MLH": high
  "NASA": high
  "Capital One": high
  "Bloomberg": high
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/identity.py`
  ```diff
  - def cross_source_key(company: str, title: str, url: str = "") -> str:
    job_id = extract_ats_job_id(url)
    if job_id:
        return f"jobid:{job_id}"
    # Punctuation-insensitive: "Intern Co-op" and "Intern/Co-op" are the same
    # posting (real Marmon dup that slipped past a whitespace-only key,
    # caught in the 2026-07-18 dossier audit).
    norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return f"{norm(company)}|{norm(title)}"
  + def _norm_company(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def cross_source_key(company: str, title: str, url: str = "") -> str:
    job_id = extract_ats_job_id(url)
    if job_id:
        return f"jobid:{job_id}"
    # Punctuation-insensitive: "Intern Co-op" and "Intern/Co-op" are the same
    # posting (real Marmon dup that slipped past a whitespace-only key,
    # caught in the 2026-07-18 dossier audit).
    norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return f"{norm(company)}|{norm(title)}"


def company_matches_preference(company: str, preferred: dict) -> str:
    """The matched preference tier (e.g. 'high'), or None if company isn't in
    preferred. Same punctuation/case-insensitive normalization as
    cross_source_key()'s norm(), so 'D.E. Shaw' and 'DE Shaw' both match —
    preferred_companies (core/profile.yaml) is a human-maintained config dict,
    not derived from live data, so this is a pure string match with no new
    network call or source to verify (Prompt 5 Task K)."""
    target = _norm_company(company)
    for name, tier in (preferred or {}).items():
        if _norm_company(name) == target:
            return tier
    return None
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 -c "
from core.identity import company_matches_preference
from core.filter import load_profile
profile = load_profile()
preferred = profile['preferred_companies']
print(company_matches_preference('D.E. Shaw', preferred))
print(company_matches_preference('DE Shaw', preferred))
print(company_matches_preference('Random Startup', preferred))
"
python -m pytest tests/ -q 2>&1 | tail -10
  ```
  ```
high
None
None
........................................................................ [ 23%]
........................................................................ [ 47%]
........................................................................ [ 70%]
........................................................................ [ 94%]
.................                                                        [100%]
305 passed in 1.12s
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
python3 -c "
import re
norm = lambda s: re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()
print(repr(norm('D.E. Shaw')))
print(repr(norm('DE Shaw')))
"
  ```
  ```
'd e shaw'
'de shaw'
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/identity.py`
  ```diff
  - def _norm_company(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
  + # Not cross_source_key()'s space-preserving norm() reused verbatim: that one
# collapses punctuation to a single space (needed to keep title text
# word-tokenized — "Intern Co-op" vs "Intern/Co-op" must still split into the
# same words). A company name is a short identifier, not sentence-shaped
# text, and the real case this needs to catch ("D.E. Shaw" vs "DE Shaw")
# fails under that space-preserving version — "d e shaw" != "de shaw". Fold
# out all non-alphanumeric characters entirely instead, so both collapse to
# the identical "deshaw".
def _norm_company(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null
cd /home/anant_gupta/projects/work/internship-research-loop
python3 -c "
from core.identity import company_matches_preference
from core.filter import load_profile
profile = load_profile()
preferred = profile['preferred_companies']
print('D.E. Shaw:', company_matches_preference('D.E. Shaw', preferred))
print('DE Shaw:', company_matches_preference('DE Shaw', preferred))
print('Random:', company_matches_preference('Random Startup', preferred))
print('google (lowercase):', company_matches_preference('google', preferred))
"
python -m pytest tests/ -q 2>&1 | tail -10
  ```
  ```
D.E. Shaw: high
DE Shaw: high
Random: None
google (lowercase): high
........................................................................ [ 23%]
........................................................................ [ 47%]
........................................................................ [ 70%]
........................................................................ [ 94%]
.................                                                        [100%]
305 passed in 1.09s
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py`
  ```diff
  - from core.identity import compute_uid, cross_source_key, extract_ats_job_id
  + from core.filter import load_profile
from core.identity import company_matches_preference, compute_uid, cross_source_key, extract_ats_job_id
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py`
  ```diff
  - def test_extract_ats_job_id_google_pattern_is_domain_anchored():
  + # --- Task K: preferred_companies matching ---

PROFILE = load_profile()


def test_company_matches_preference_punctuation_insensitive_real_de_shaw_case():
    """Real profile.yaml entry 'D.E. Shaw' must match the real vault dossier
    company string 'DE Shaw' (Software Developer Intern - DE Shaw.md)."""
    preferred = PROFILE["preferred_companies"]
    assert company_matches_preference("D.E. Shaw", preferred) == "high"
    assert company_matches_preference("DE Shaw", preferred) == "high"


def test_company_matches_preference_case_insensitive():
    preferred = PROFILE["preferred_companies"]
    assert company_matches_preference("google", preferred) == "high"
    assert company_matches_preference("GOOGLE", preferred) == "high"


def test_company_matches_preference_none_for_unlisted_company():
    preferred = PROFILE["preferred_companies"]
    assert company_matches_preference("Random Startup Inc", preferred) is None


def test_company_matches_preference_none_for_empty_preferred_dict():
    assert company_matches_preference("Google", {}) is None


def test_extract_ats_job_id_google_pattern_is_domain_anchored():
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_identity.py -q 2>&1 | tail -30`
  ```
....................                                                     [100%]
20 passed in 0.05s
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/classify.py`
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/core/debate.py`
  ```
"""Layer 3.5 — the "debate": a deterministic pairwise comparator that decides
which of two candidates ranks first when both compete for this run's
per-bucket write budget (Prompt 5 Task L). Zero-LLM by design, same rule as
everywhere else in this codebase's unattended path (see the repo's own
CLAUDE.md) — "debating between two internships" is a real comparator
function, not a model call. Used via functools.cmp_to_key() to produce a
full deterministic ranking in one efficient sort: mathematically the same
outcome as running every pairwise comparison, without the wasted O(n^2)
redundant comparisons a literal round-robin would do.

Three priority stages, each only breaking ties left by the stage above it —
kept as separable comparison stages rather than one blended numeric score,
so a human reading debate_compare can see exactly why any two candidates
were ordered the way they were:
  1. Preferred-company tier (core.identity.company_matches_preference)
  2. Bucket fill-need (cross-bucket only — see the note on bucket_urgency
     below for why this stage has no live effect in the current call site)
  3. Recency (most-recently-posted-first, the pre-existing rule)
"""
from core.classify import classify
from core.identity import company_matches_preference

_TIER_RANK = {"high": 0}


def _preference_rank(company: str, preferred_companies: dict) -> int:
    tier = company_matches_preference(company, preferred_companies)
    return _TIER_RANK.get(tier, 1) if tier else 1


def debate_compare(a, b, preferred_companies: dict, bucket_urgency: dict = None) -> int:
    """Standard cmp semantics: negative if a should rank first, positive if
    b should, 0 if the next stage must decide. a and b are (uid, listing)
    tuples, the same shape _prioritize_and_cap already sorts.

    bucket_urgency (optional): {bucket_name: shortfall_score}, precomputed
    once per run as max(0, budget[bucket] - candidate_count[bucket]) — a
    higher score means that bucket has fewer real candidates this run than
    its budget, i.e. it's at risk of going unfilled even taking every
    candidate it has. Only consulted when a and b are headed for DIFFERENT
    buckets; a same-bucket comparison skips stage 2 entirely, per spec.

    Note on reachability: _prioritize_and_cap (run_pipeline.py) partitions
    candidates by bucket before sorting, so every debate_compare call it
    makes is already same-bucket — stage 2 never actually fires through that
    call path today. It's implemented and tested here as a real, correct,
    independently-callable stage (per Task L's explicit spec and test
    requirements), not dead code: a future architecture change that compares
    candidates across buckets directly would exercise it immediately, and no
    second mechanism would need to be built to support that."""
    uid_a, listing_a = a
    uid_b, listing_b = b

    rank_a = _preference_rank(listing_a.company, preferred_companies)
    rank_b = _preference_rank(listing_b.company, preferred_companies)
    if rank_a != rank_b:
        return rank_a - rank_b

    if bucket_urgency is not None:
        bucket_a, _ = classify(listing_a.title, listing_a.category, "")
        bucket_b, _ = classify(listing_b.title, listing_b.category, "")
        if bucket_a != bucket_b:
            urgency_a = bucket_urgency.get(bucket_a, 0)
            urgency_b = bucket_urgency.get(bucket_b, 0)
            if urgency_a != urgency_b:
                return urgency_b - urgency_a  # higher urgency ranks first

    date_a = listing_a.date_posted or 0
    date_b = listing_b.date_posted or 0
    return date_b - date_a  # more recent ranks first


def compute_bucket_urgency(candidates: list, budget: dict) -> dict:
    """{bucket: max(0, budget[bucket] - candidate_count[bucket])} for every
    bucket present in budget — precomputed once per run from the full
    candidate pool (before any per-bucket slicing), since "at risk of going
    unfilled" is a property of how many real candidates exist this run
    relative to budget, not a running fill-count that changes mid-sort."""
    counts = {}
    for _uid, listing in candidates:
        bucket, _ = classify(listing.title, listing.category, "")
        counts[bucket] = counts.get(bucket, 0) + 1
    return {bucket: max(0, cap - counts.get(bucket, 0)) for bucket, cap in budget.items()}

  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - import json
import os
import subprocess

import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path

from core.classify import BUCKET_FOLDERS, classification_callout, classify
from core.filter import load_profile, matches
from core.git_ops import GitPushError, commit_and_push_with_retry
from core.identity import compute_uid
  + import json
import os
import subprocess
from functools import cmp_to_key

import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path

from core.classify import BUCKET_FOLDERS, classification_callout, classify
from core.debate import compute_bucket_urgency, debate_compare
from core.filter import load_profile, matches
from core.git_ops import GitPushError, commit_and_push_with_retry
from core.identity import compute_uid
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - def _prioritize_and_cap(new_listings: list, budget: dict) -> tuple:
    """Most-recently-posted first, scoped per-bucket per the tunable budget
    dict — each bucket fills only from its own ordered queue, so an empty
    bucket this run can't let another bucket's items borrow its slots.
    Bucket is the same degraded-signal classify() (title/category only, no
    fetched content yet) validate_and_write() itself falls back to before a
    posting's content is fetched — pacing doesn't need the refined,
    content-informed bucket, only the final written folder does. Missing
    date_posted sorts last, never first (an unknown post date must not win
    priority over a known-recent one). Returns (this_run, deferred) —
    deferred items are simply not passed to validate_and_write and therefore
    never marked seen, so dedup_new() naturally re-offers them next run
    without any extra state to manage."""
    by_bucket = {}
    for uid, listing in new_listings:
        bucket, _ = classify(listing.title, listing.category, "")
        by_bucket.setdefault(bucket, []).append((uid, listing))

    this_run, deferred = [], []
    for bucket, items in by_bucket.items():
        ordered = sorted(items, key=lambda item: item[1].date_posted or 0, reverse=True)
        limit = budget.get(bucket, 0)
        this_run.extend(ordered[:limit])
        deferred.extend(ordered[limit:])
    return this_run, deferred
  + def _prioritize_and_cap(new_listings: list, budget: dict, preferred_companies: dict = None) -> tuple:
    """Scoped per-bucket per the tunable budget dict — each bucket fills only
    from its own ordered queue, so an empty bucket this run can't let another
    bucket's items borrow its slots. Bucket is the same degraded-signal
    classify() (title/category only, no fetched content yet)
    validate_and_write() itself falls back to before a posting's content is
    fetched — pacing doesn't need the refined, content-informed bucket, only
    the final written folder does. Returns (this_run, deferred) — deferred
    items are simply not passed to validate_and_write and therefore never
    marked seen, so dedup_new() naturally re-offers them next run without any
    extra state to manage.

    Ordering within each bucket is now the Task L "debate" comparator
    (preferred-company tier -> bucket fill-need -> recency) instead of a bare
    recency sort — preferred_companies=None degrades to the original
    recency-only order (every candidate ties at stage 1, and stage 2 never
    fires within a single bucket's own list regardless, so recency alone
    decides), which is also exactly what every pre-Task-L caller/test gets
    for free."""
    by_bucket = {}
    for uid, listing in new_listings:
        bucket, _ = classify(listing.title, listing.category, "")
        by_bucket.setdefault(bucket, []).append((uid, listing))

    bucket_urgency = compute_bucket_urgency(new_listings, budget)
    cmp_key = cmp_to_key(lambda x, y: debate_compare(x, y, preferred_companies or {}, bucket_urgency))

    this_run, deferred = [], []
    for bucket, items in by_bucket.items():
        ordered = sorted(items, key=cmp_key)
        limit = budget.get(bucket, 0)
        this_run.extend(ordered[:limit])
        deferred.extend(ordered[limit:])
    return this_run, deferred
  ```
- `Bash` — `grep -n "_prioritize_and_cap(new_listings" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```
92:def _prioritize_and_cap(new_listings: list, budget: dict, preferred_companies: dict = None) -> tuple:
363:    this_run, deferred = _prioritize_and_cap(new_listings, MAX_NEW_WRITES_PER_RUN)
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -     this_run, deferred = _prioritize_and_cap(new_listings, MAX_NEW_WRITES_PER_RUN)
    record["deferred_count"] = len(deferred)
  +     this_run, deferred = _prioritize_and_cap(
        new_listings, MAX_NEW_WRITES_PER_RUN, preferred_companies=profile.get("preferred_companies")
    )
    record["deferred_count"] = len(deferred)
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -60`
  ```
........................................................................ [ 23%]
........................................................................ [ 46%]
........................................................................ [ 69%]
........................................................................ [ 93%]
.....................                                                    [100%]
309 passed in 1.13s
  ```
- `Bash` — `grep -n "^from ingestion.normalize\|^def _simplify_raw\|^def _listing_with_date" /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```
13:from ingestion.normalize import normalize_josegael, normalize_simplify
23:def _simplify_raw():
92:def _listing_with_date(uid_suffix, date_posted):
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Bash`:
  ```bash
grep -n "^def _simplify_raw" -A 5 /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py
echo "---"
python3 -c "
import json
raw = json.loads(open('/home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/simplifyjobs.json').read())[0]
print(raw['company_name'], raw['title'], raw['category'])
"
  ```
  ```
23:def _simplify_raw():
24-    return _strip_case_keys(json.loads((FIXTURES / "simplifyjobs.json").read_text()))
25-
26-
27-def _josegael_raw():
28-    return _strip_case_keys(json.loads((FIXTURES / "josegael.json").read_text()))
---
Palantir Forward Deployed Software Engineer – Internship - US Government Software
  ```
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate.py`
  ```
"""Task L — the deterministic pairwise 'debate' comparator. Each stage is
tested in isolation first (a pairwise case where every stage above it ties,
so the stage under test is what actually decides), then the full per-bucket
sort is tested via run_pipeline._prioritize_and_cap."""
from ingestion.normalize import Listing

from core.debate import compute_bucket_urgency, debate_compare
from core.filter import load_profile

PROFILE = load_profile()
PREFERRED = PROFILE["preferred_companies"]


def _candidate(uid, company, title="Software Engineer Intern", category="Software",
               date_posted=1700000000):
    listing = Listing(company=company, title=title, url=f"https://example.com/{uid}",
                      source="SimplifyJobs", category=category, date_posted=date_posted, raw_id=uid)
    return (f"SimplifyJobs:{uid}", listing)


# --- Stage 1: preferred-company tier (identical dates, same bucket) ---

def test_debate_compare_prefers_preferred_company_with_identical_dates():
    preferred = _candidate("a", "Google", date_posted=1700000000)
    non_preferred = _candidate("b", "Random Startup Inc", date_posted=1700000000)
    assert debate_compare(preferred, non_preferred, PREFERRED) < 0
    assert debate_compare(non_preferred, preferred, PREFERRED) > 0


def test_debate_compare_ties_between_two_preferred_companies_falls_through():
    """Two preferred companies with different dates — stage 1 ties (both
    'high'), recency (stage 3) decides."""
    older = _candidate("a", "Google", date_posted=1600000000)
    newer = _candidate("b", "Microsoft", date_posted=1700000000)
    assert debate_compare(newer, older, PREFERRED) < 0


# --- Stage 2: bucket fill-need (cross-bucket only, same preference tier) ---

def test_debate_compare_prefers_bucket_at_risk_of_going_unfilled():
    """Two non-preferred candidates (stage 1 ties), different buckets, one
    bucket's real candidate pool is smaller than its budget (at risk of
    going unfilled even taking every candidate) — that bucket's candidate
    ranks first despite an identical/older date, since bucket_urgency is
    consulted before recency."""
    other_bucket_candidate = _candidate(
        "a", "Random Startup Inc", title="Demand Planning Analyst Intern",
        category="Other", date_posted=1600000000,
    )  # classifies to 'Other' via no bucket-specific signal
    ai_ml_candidate = _candidate(
        "b", "Random Startup Inc", title="Machine Learning Engineer Intern",
        category="AI/ML", date_posted=1700000000,
    )  # classifies to 'AI/ML', more recent
    # 'Other' bucket: budget 1, only 1 real candidate this run -> urgency 0
    # (not actually short) — construct a genuine shortfall instead: budget
    # exceeds the real candidate count for that bucket.
    budget = {"Other": 3, "AI/ML": 3}
    pool = [other_bucket_candidate]  # only 1 candidate for a 3-slot 'Other' budget -> urgency 2
    urgency = compute_bucket_urgency(pool + [ai_ml_candidate], budget)
    assert urgency["Other"] == 2  # 3 budget - 1 real candidate
    assert urgency["AI/ML"] == 2  # 3 budget - 1 real candidate — tied urgency, won't decide this case

    # Make it a genuine, unambiguous case: 'Other' has 1 real candidate
    # against a 3-slot budget (urgency 2); 'AI/ML' has 3 real candidates
    # against its own 3-slot budget (urgency 0, ample supply).
    ai_ml_candidate_2 = _candidate("c", "Random Startup Inc", title="Machine Learning Engineer Intern",
                                   category="AI/ML", date_posted=1650000000)
    ai_ml_candidate_3 = _candidate("d", "Random Startup Inc", title="Machine Learning Engineer Intern",
                                   category="AI/ML", date_posted=1550000000)
    full_pool = [other_bucket_candidate, ai_ml_candidate, ai_ml_candidate_2, ai_ml_candidate_3]
    urgency = compute_bucket_urgency(full_pool, budget)
    assert urgency["Other"] == 2  # 3 - 1
    assert urgency["AI/ML"] == 0  # 3 - 3, ample supply

    # ai_ml_candidate is more recently posted, but 'Other' is at real risk of
    # going unfilled — its candidate must still rank first.
    assert debate_compare(other_bucket_candidate, ai_ml_candidate, PREFERRED, bucket_urgency=urgency) < 0


def test_debate_compare_skips_bucket_fill_need_for_same_bucket_pair():
    """Same bucket for both candidates — stage 2 is explicitly a no-op here
    per spec, so an artificially lopsided urgency dict must not override
    recency."""
    a = _candidate("a", "Random Startup Inc", date_posted=1600000000)  # both 'Other'
    b = _candidate("b", "Random Startup Inc", date_posted=1700000000)  # both 'Other', more recent
    urgency = {"Other": 999}  # would dominate if (incorrectly) applied same-bucket
    assert debate_compare(b, a, PREFERRED, bucket_urgency=urgency) < 0  # recency still decides


def [REDACTED]():
    """bucket_urgency=None (the default) skips stage 2 entirely, falling
    straight through to recency — this is what every pre-Task-L caller gets."""
    other_bucket_candidate = _candidate("a", "Random Startup Inc", title="Demand Planning Analyst Intern",
                                        category="Other", date_posted=1600000000)
    ai_ml_candidate = _candidate("b", "Random Startup Inc", title="Machine Learning Engineer Intern",
                                 category="AI/ML", date_posted=1700000000)
    assert debate_compare(ai_ml_candidate, other_bucket_candidate, PREFERRED) < 0  # recency wins, no urgency info


# --- Stage 3: recency (everything else equal) ---

def test_debate_compare_recency_is_final_tiebreak():
    older = _candidate("a", "Random Startup Inc", date_posted=1600000000)
    newer = _candidate("b", "Random Startup Inc", date_posted=1700000000)
    assert debate_compare(newer, older, PREFERRED) < 0
    assert debate_compare(older, newer, PREFERRED) > 0


def test_debate_compare_missing_date_posted_sorts_last():
    known = _candidate("a", "Random Startup Inc", date_posted=1700000000)
    unknown = _candidate("b", "Random Startup Inc", date_posted=None)
    assert debate_compare(known, unknown, PREFERRED) < 0

  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_debate.py -q 2>&1 | tail -100`
  ```
.......                                                                  [100%]
7 passed in 0.04s
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```diff
  - def test_prioritize_and_cap_scopes_budget_per_bucket():
  + def test_prioritize_and_cap_orders_preferred_company_first_within_bucket():
    """Task L integration: two 'Other'-bucket candidates, non-preferred one
    posted more recently — the debate comparator's preferred-company stage
    must still put the preferred company first when preferred_companies is
    supplied, overriding the bare-recency behavior of the pre-Task-L sort."""
    non_preferred_recent = _listing_with_date("recent", 1700000000)
    non_preferred_recent[1].company = "Random Startup Inc"
    preferred_older = _listing_with_date("older", 1600000000)
    preferred_older[1].company = "Google"

    this_run, deferred = run_pipeline._prioritize_and_cap(
        [non_preferred_recent, preferred_older], budget={"Other": 1},
        preferred_companies={"Google": "high"},
    )
    assert this_run[0][1].company == "Google"
    assert deferred[0][1].company == "Random Startup Inc"


def test_prioritize_and_cap_without_preferred_companies_keeps_recency_only_order():
    """preferred_companies=None (the default) must reproduce the exact
    pre-Task-L recency-only behavior — every existing caller/test that
    doesn't pass it should see no change."""
    items = [_listing_with_date(i, date_posted) for i, date_posted in enumerate([100, 300, 200])]
    this_run, deferred = run_pipeline._prioritize_and_cap(items, budget={"Other": 2})
    assert [l.date_posted for _, l in this_run] == [300, 200]
    assert [l.date_posted for _, l in deferred] == [100]


def test_prioritize_and_cap_scopes_budget_per_bucket():
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_run_pipeline.py -q 2>&1 | tail -100`
  ```
....................................                                     [100%]
36 passed in 1.25s
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -20`
  ```
........................................................................ [ 22%]
........................................................................ [ 45%]
........................................................................ [ 67%]
........................................................................ [ 90%]
..............................                                           [100%]
318 passed in 2.55s
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/run_log.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/run_log.py`
  ```diff
  - _HEADER_TEMPLATE = """---
type: dashboard
status: active
created: {created}
tags:
  - internship
  - automation
  - run-log
---
# Internship Research Loop — Run Log
Weekly rollup from the internship-research-loop automation, appended automatically — not rewritten. Raw per-run data lives in that repo's logs/runs.jsonl.
"""


def append_weekly_rollup(run_log_md_path, line: str, created_date: str) -> None:
    path = Path(run_log_md_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        header = _HEADER_TEMPLATE.format(created=created_date).rstrip("\n") + "\n"
        path.write_text(header + line + "\n")
        return
    existing = path.read_text()
    if not existing.endswith("\n"):
        existing += "\n"
    path.write_text(existing + line + "\n")
  + _HEADER_TEMPLATE = """---
type: dashboard
status: active
created: {created}
tags:
  - internship
  - automation
  - run-log
---
# Internship Research Loop — Run Log
Weekly rollup from the internship-research-loop automation, appended automatically — not rewritten. Raw per-run data lives in that repo's logs/runs.jsonl.
"""


def _append_markdown_line(path, line: str, header: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(header.rstrip("\n") + "\n" + line + "\n")
        return
    existing = path.read_text()
    if not existing.endswith("\n"):
        existing += "\n"
    path.write_text(existing + line + "\n")


def append_weekly_rollup(run_log_md_path, line: str, created_date: str) -> None:
    _append_markdown_line(run_log_md_path, line, _HEADER_TEMPLATE.format(created=created_date))


_EXCLUDED_LOG_HEADER_TEMPLATE = """---
type: dashboard
status: active
created: {created}
tags:
  - internship
  - automation
  - debate
---
# Excluded — Losing The Debate
A posting lands here the first time it loses the per-bucket debate comparator's sort {max_losses} consecutive runs — not a silent, permanent exclusion, a reviewable one. If you disagree with the comparator's call on any of these, promote the posting by hand; this log exists so that decision has something concrete to look at. Appended automatically, never rewritten.
"""


def append_excluded_log(excluded_log_md_path, line: str, created_date: str, max_losses: int) -> None:
    """Task N (Prompt 5) — one line per uid the first time it's excluded,
    same append-only pattern as append_weekly_rollup above."""
    _append_markdown_line(
        excluded_log_md_path, line, _EXCLUDED_LOG_HEADER_TEMPLATE.format(created=created_date, max_losses=max_losses)
    )
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_run_log.py -q 2>&1 | tail -30`
  ```
.........                                                                [100%]
9 passed in 0.06s
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - from core.run_log import (
    append_run_log,
    append_weekly_rollup,
    format_weekly_rollup,
    load_recent_runs,
    should_run_weekly_rollup,
)
  + from core.run_log import (
    append_excluded_log,
    append_run_log,
    append_weekly_rollup,
    format_weekly_rollup,
    load_recent_runs,
    should_run_weekly_rollup,
)
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - def save_capacity_notified(state_dir, notified: dict) -> None:
    path = Path(state_dir) / CAPACITY_STATE_FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notified, indent=2, sort_keys=True) + "\n")

RUN_LOG_MD_SUBPATH = Path("10_Areas/Career/Internships/List/Run Log.md")
  + def save_capacity_notified(state_dir, notified: dict) -> None:
    path = Path(state_dir) / CAPACITY_STATE_FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notified, indent=2, sort_keys=True) + "\n")

RUN_LOG_MD_SUBPATH = Path("10_Areas/Career/Internships/List/Run Log.md")

# Task N (Prompt 5) — a candidate that loses the debate comparator's sort
# (falls outside its bucket's budget, i.e. ends up in _prioritize_and_cap's
# "deferred" list) accumulates a loss count across runs. 5 was chosen to give
# a real posting several genuine chances across multiple hourly runs before
# conceding it structurally can't out-rank the field — not an arbitrary
# guess dressed as one, but still a tunable to retune from real data once
# this has run for a while, same as every other tunable in this codebase.
MAX_DEBATE_LOSSES = 5
DEBATE_LOSSES_FILENAME = "debate_losses.json"
EXCLUDED_UIDS_FILENAME = "excluded_uids.json"
EXCLUDED_LOG_SUBPATH = Path("10_Areas/Career/Internships/List/Excluded — Losing The Debate.md")


def load_debate_losses(state_dir) -> dict:
    path = Path(state_dir) / DEBATE_LOSSES_FILENAME
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def save_debate_losses(state_dir, losses: dict) -> None:
    path = Path(state_dir) / DEBATE_LOSSES_FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(losses, indent=2, sort_keys=True) + "\n")


def load_excluded_uids(state_dir) -> set:
    path = Path(state_dir) / EXCLUDED_UIDS_FILENAME
    if not path.exists():
        return set()
    return set(json.loads(path.read_text()))


def save_excluded_uids(state_dir, excluded: set) -> None:
    path = Path(state_dir) / EXCLUDED_UIDS_FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(sorted(excluded), indent=2) + "\n")


def update_debate_losses(losses: dict, deferred: list, written_uids: list) -> tuple:
    """Returns (updated_losses, newly_excluded: [(uid, listing), ...]).
    Increments the loss count for every deferred uid (a candidate that lost
    this run's per-bucket comparator sort); removes any uid that won (got
    written) this run entirely — it's in seen_ids.json now, its loss history
    is moot. A uid whose count reaches MAX_DEBATE_LOSSES is returned in
    newly_excluded and removed from losses — callers add it to the excluded
    set and log it; this function only does the counting."""
    losses = dict(losses)
    for uid in written_uids:
        losses.pop(uid, None)
    newly_excluded = []
    for uid, listing in deferred:
        losses[uid] = losses.get(uid, 0) + 1
        if losses[uid] >= MAX_DEBATE_LOSSES:
            newly_excluded.append((uid, listing))
            del losses[uid]
    return losses, newly_excluded
  ```
- `Bash` — `grep -n "^def fetch_and_filter\|^def dedup_new" -A 15 /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```
242:def fetch_and_filter(profile: dict, http_get=None) -> dict:
243-    """Returns {source_name: {"fetch_count": int, "matched": [Listing, ...]}}."""
244-    results = {}
245-    for name, fetch_fn in SOURCES:
246-        listings = fetch_fn(http_get)
247-        results[name] = {
248-            "fetch_count": len(listings),
249-            "matched": [l for l in listings if matches(l, profile) and not stage1_reject(l.title, l.raw_text)],
250-        }
251-    return results
252-
253-
254:def dedup_new(matched_by_source: dict, seen_ids: set):
255-    """Returns ([(uid, listing), ...] for genuinely new items, already_seen_count)."""
256-    new = []
257-    already_seen = 0
258-    seen_this_run = set()
259-    for _name, info in matched_by_source.items():
260-        for listing in info["matched"]:
261-            uid = compute_uid(listing)
262-            if uid in seen_ids or uid in seen_this_run:
263-                already_seen += 1
264-                continue
265-            seen_this_run.add(uid)
266-            new.append((uid, listing))
267-    return new, already_seen
268-
269-
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - def fetch_and_filter(profile: dict, http_get=None) -> dict:
    """Returns {source_name: {"fetch_count": int, "matched": [Listing, ...]}}."""
    results = {}
    for name, fetch_fn in SOURCES:
        listings = fetch_fn(http_get)
        results[name] = {
            "fetch_count": len(listings),
            "matched": [l for l in listings if matches(l, profile) and not stage1_reject(l.title, l.raw_text)],
        }
    return results


def dedup_new(matched_by_source: dict, seen_ids: set):
    """Returns ([(uid, listing), ...] for genuinely new items, already_seen_count)."""
    new = []
    already_seen = 0
    seen_this_run = set()
    for _name, info in matched_by_source.items():
        for listing in info["matched"]:
            uid = compute_uid(listing)
            if uid in seen_ids or uid in seen_this_run:
                already_seen += 1
                continue
            seen_this_run.add(uid)
            new.append((uid, listing))
    return new, already_seen
  + def fetch_and_filter(profile: dict, http_get=None, excluded_ids: frozenset = frozenset()) -> dict:
    """Returns {source_name: {"fetch_count": int, "matched": [Listing, ...]}}.
    excluded_ids (Task N, Prompt 5) drops a uid that already lost the debate
    comparator MAX_DEBATE_LOSSES consecutive times here, before it's even
    counted as matched — the earliest seam available, so an excluded uid
    never reaches the Firecrawl content-fetch in validate_and_write either."""
    results = {}
    for name, fetch_fn in SOURCES:
        listings = fetch_fn(http_get)
        results[name] = {
            "fetch_count": len(listings),
            "matched": [
                l for l in listings
                if matches(l, profile) and not stage1_reject(l.title, l.raw_text)
                and compute_uid(l) not in excluded_ids
            ],
        }
    return results


def dedup_new(matched_by_source: dict, seen_ids: set, excluded_ids: frozenset = frozenset()):
    """Returns ([(uid, listing), ...] for genuinely new items, already_seen_count).
    excluded_ids is also checked here (belt-and-suspenders with
    fetch_and_filter's own check above) so nothing slips through if a caller
    ever builds matched_by_source some other way."""
    new = []
    already_seen = 0
    seen_this_run = set()
    for _name, info in matched_by_source.items():
        for listing in info["matched"]:
            uid = compute_uid(listing)
            if uid in excluded_ids:
                continue
            if uid in seen_ids or uid in seen_this_run:
                already_seen += 1
                continue
            seen_this_run.add(uid)
            new.append((uid, listing))
    return new, already_seen
  ```
- `Bash` — `grep -n "def run_once\|seen_ids = load_seen_ids\|matched_by_source = fetch_and_filter\|new_listings, already_seen_count\|this_run, deferred\|written_uids, rejections = validate_and_write\|record\[.rejections.\]\|record\[.bucket_at_capacity.\]" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```
100:    the final written folder does. Returns (this_run, deferred) — deferred
120:    this_run, deferred = [], []
126:    return this_run, deferred
374:def run_once(
410:        seen_ids = load_seen_ids(state_path)
411:        matched_by_source = fetch_and_filter(profile, http_get)
431:    new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids)
435:    this_run, deferred = _prioritize_and_cap(
443:    written_uids, rejections = validate_and_write(
450:    record["rejections"] = rejections
456:    record["bucket_at_capacity"] = sorted(b for b, c in bucket_counts.items() if c >= BUCKET_CAPACITY)
461:    for bucket in record["bucket_at_capacity"]:
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -         "bucket_at_capacity": [],
        "dossier_total": 0,
    }

    try:
        check_schema_drift(http_get)
        seen_ids = load_seen_ids(state_path)
        matched_by_source = fetch_and_filter(profile, http_get)
    except (SchemaDriftError, requests.RequestException) as exc:
  +         "bucket_at_capacity": [],
        "dossier_total": 0,
        "newly_excluded_count": 0,
    }

    excluded_ids = load_excluded_uids(state_dir) if state_dir is not None else set()

    try:
        check_schema_drift(http_get)
        seen_ids = load_seen_ids(state_path)
        matched_by_source = fetch_and_filter(profile, http_get, excluded_ids=excluded_ids)
    except (SchemaDriftError, requests.RequestException) as exc:
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -     new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids)
    record["new_count"] = len(new_listings)
  +     new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids, excluded_ids=excluded_ids)
    record["new_count"] = len(new_listings)
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -     if opt_cache_path and opt_cache:
        Path(opt_cache_path).parent.mkdir(parents=True, exist_ok=True)
        Path(opt_cache_path).write_text(json.dumps(opt_cache, indent=2, sort_keys=True) + "\n")
    record["rejections"] = rejections

    # Task A resource-limit notification (Standard §5): a bucket at/over
  +     if opt_cache_path and opt_cache:
        Path(opt_cache_path).parent.mkdir(parents=True, exist_ok=True)
        Path(opt_cache_path).write_text(json.dumps(opt_cache, indent=2, sort_keys=True) + "\n")
    record["rejections"] = rejections

    # Task N (Prompt 5): count this run's debate loss for every deferred
    # candidate; a uid that won (got written) has its loss history dropped
    # entirely. A uid crossing MAX_DEBATE_LOSSES moves to the excluded set
    # and gets one line in a reviewable markdown log — not a silent,
    # permanent exclusion.
    if state_dir is not None:
        debate_losses = load_debate_losses(state_dir)
        debate_losses, newly_excluded = update_debate_losses(debate_losses, deferred, written_uids)
        save_debate_losses(state_dir, debate_losses)
        record["newly_excluded_count"] = len(newly_excluded)
        if newly_excluded:
            excluded_ids = load_excluded_uids(state_dir)
            excluded_ids.update(uid for uid, _listing in newly_excluded)
            save_excluded_uids(state_dir, excluded_ids)
            for uid, listing in newly_excluded:
                line = (
                    f"- **{listing.company}** — {listing.title} — [{listing.url}]({listing.url}) — "
                    f"excluded {now.date().isoformat()} — lost the debate {MAX_DEBATE_LOSSES} consecutive runs"
                )
                append_excluded_log(
                    Path(jarvis_dir) / EXCLUDED_LOG_SUBPATH, line, created_date=now.date().isoformat(),
                    max_losses=MAX_DEBATE_LOSSES,
                )

    # Task A resource-limit notification (Standard §5): a bucket at/over
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -60`
  ```
........................................................................ [ 22%]
........................................................................ [ 45%]
........................................................................ [ 67%]
........................................................................ [ 90%]
..............................                                           [100%]
318 passed in 1.31s
  ```
- `Bash` — `grep -n "^def _run_once_kwargs" -A 20 /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```
310:def _run_once_kwargs(tmp_path, **overrides):
311-    kwargs = dict(
312-        jarvis_dir=tmp_path / "jarvis",
313-        state_path=tmp_path / "state" / "seen_ids.json",
314-        runs_log_path=tmp_path / "logs" / "runs.jsonl",
315-        now=datetime(2026, 7, 17, 15, 0, tzinfo=timezone.utc),  # a Friday, not rollup time
316-        profile=PROFILE,
317-        http_get=_fake_http_get,
318-        http_head=_fake_http_head_all_live,
319-        push_fn=lambda repo_dir, message: True,
320-        issue_fn=Mock(),
321-    )
322-    kwargs.update(overrides)
323-    (tmp_path / "jarvis").mkdir(parents=True, exist_ok=True)
324-    return kwargs
325-
326-
327-def test_run_once_happy_path_marks_seen_and_writes_dossiers(tmp_path):
328-    kwargs = _run_once_kwargs(tmp_path)
329-    record = run_pipeline.run_once(**kwargs)
330-
  ```
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py`
  ```
"""Task N (Prompt 5) — consecutive-loss tracking and the excluded-uid list.

update_debate_losses is tested as a pure function first (deterministic,
easy to construct exact "4 losses"/"5th loss"/"wins before excluded"
scenarios) — decomposed this way rather than grinding through 5-6 sequential
full run_once() calls with mutable per-round HTTP fixtures, since the three
named behaviors (still-in-pool, excluded-at-threshold, win-resets-count) are
properties of the counting arithmetic itself, not of the surrounding fetch/
validate machinery. A separate, focused integration test then covers the
"skip an already-excluded uid entirely, never even fetch it" guarantee
against the real run_once() pipeline, using pre-seeded state (an uid already
at the exclusion threshold) rather than manufacturing 5 real prior runs.
"""
import json
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock

import pytest

import run_pipeline
from core.identity import compute_uid
from ingestion.normalize import Listing

from .test_run_pipeline import PROFILE, _fake_http_get, _fake_http_head_all_live, _run_once_kwargs, _simplify_raw
from ingestion.normalize import normalize_simplify


def _candidate(uid, company="Acme", title="Software Engineer Intern", url=None):
    listing = Listing(company=company, title=title, url=url or f"https://acme.example/{uid}",
                      source="SimplifyJobs", raw_id=uid, date_posted=1700000000)
    return (f"SimplifyJobs:{uid}", listing)


# --- update_debate_losses: pure-function tests ---

def [REDACTED]():
    losses = {}
    deferred = [_candidate("x")]
    for _ in range(4):
        losses, newly_excluded = run_pipeline.update_debate_losses(losses, deferred, written_uids=[])
        assert newly_excluded == []
    assert losses["SimplifyJobs:x"] == 4


def [REDACTED]():
    losses = {}
    deferred = [_candidate("x")]
    for _ in range(4):
        losses, _ = run_pipeline.update_debate_losses(losses, deferred, written_uids=[])
    losses, newly_excluded = run_pipeline.update_debate_losses(losses, deferred, written_uids=[])
    assert [uid for uid, _listing in newly_excluded] == ["SimplifyJobs:x"]
    assert "SimplifyJobs:x" not in losses  # removed once excluded, not left at 5


def [REDACTED]():
    """Loses twice (deferred), then wins (written) on the third attempt —
    its loss count must be wiped, not merely paused, so a LATER unrelated
    deferral starts counting from zero rather than resuming near threshold."""
    uid, listing = _candidate("x")
    losses = {}
    losses, excluded_1 = run_pipeline.update_debate_losses(losses, [(uid, listing)], written_uids=[])
    losses, excluded_2 = run_pipeline.update_debate_losses(losses, [(uid, listing)], written_uids=[])
    assert losses[uid] == 2
    assert excluded_1 == [] and excluded_2 == []

    # Attempt 3: wins (written), not deferred.
    losses, excluded_3 = run_pipeline.update_debate_losses(losses, deferred=[], written_uids=[uid])
    assert uid not in losses
    assert excluded_3 == []

    # Confirm it never gets excluded even after this reset: 4 more real
    # losses (fewer than MAX_DEBATE_LOSSES) leave it un-excluded.
    for _ in range(4):
        losses, excluded_n = run_pipeline.update_debate_losses(losses, [(uid, listing)], written_uids=[])
        assert excluded_n == []
    assert losses[uid] == 4


def test_written_uid_not_in_losses_is_a_no_op_pop():
    """A uid that wins without ever having lost before (the common case)
    must not error on the pop — dict.pop(uid, None) already handles this,
    this test just pins the behavior."""
    losses, newly_excluded = run_pipeline.update_debate_losses({}, deferred=[], written_uids=["SimplifyJobs:never-lost"])
    assert losses == {}
    assert newly_excluded == []


# --- fetch_and_filter / dedup_new: excluded uids are skipped ---

def test_fetch_and_filter_skips_excluded_uid():
    real_uid = compute_uid(normalize_simplify(_simplify_raw()[0]))
    results = run_pipeline.fetch_and_filter(PROFILE, http_get=_fake_http_get, excluded_ids=frozenset({real_uid}))
    all_matched_uids = {
        compute_uid(l) for info in results.values() for l in info["matched"]
    }
    assert real_uid not in all_matched_uids


def test_dedup_new_skips_excluded_uid():
    real_uid = compute_uid(normalize_simplify(_simplify_raw()[0]))
    matched_by_source = run_pipeline.fetch_and_filter(PROFILE, http_get=_fake_http_get)
    new_listings, _ = run_pipeline.dedup_new(matched_by_source, seen_ids=set(), excluded_ids=frozenset({real_uid}))
    assert real_uid not in [uid for uid, _listing in new_listings]


# --- integration: an already-excluded uid is never fetched via run_once ---

def test_run_once_never_fetches_an_already_excluded_uid(tmp_path):
    real_uid = compute_uid(normalize_simplify(_simplify_raw()[0]))
    state_dir = tmp_path / "state"
    state_dir.mkdir(parents=True)
    (state_dir / run_pipeline.EXCLUDED_UIDS_FILENAME).write_text(json.dumps([real_uid]))

    def fetch_page_fn(url):
        assert "acme" not in url.lower() or True  # placeholder, real assertion below
        raise AssertionError(f"must not fetch an already-excluded uid's URL: {url}")

    # Use a fetch_page_fn that raises for ANY call — if the excluded uid is
    # truly never reached, no call happens at all and the run completes
    # normally (other, non-excluded candidates may still legitimately fetch,
    # so scope the assertion to the specific excluded listing's URL).
    from ingestion.normalize import normalize_simplify as _ns
    excluded_listing = _ns(_simplify_raw()[0])
    calls = []

    def guarded_fetch(url):
        calls.append(url)
        if url == excluded_listing.url:
            raise AssertionError("fetched the excluded uid's URL — exclusion did not take effect")
        return ""

    kwargs = _run_once_kwargs(tmp_path, state_dir=state_dir, fetch_page_fn=guarded_fetch)
    record = run_pipeline.run_once(**kwargs)

    assert excluded_listing.url not in calls
    assert record["errors"] == []

  ```
- `Bash`:
  ```bash
ls -la /home/anant_gupta/projects/work/internship-research-loop/tests/ | grep -i init
cat /home/anant_gupta/projects/work/internship-research-loop/pytest.ini 2>/dev/null || cat /home/anant_gupta/projects/work/internship-research-loop/setup.cfg 2>/dev/null || cat /home/anant_gupta/projects/work/internship-research-loop/pyproject.toml 2>/dev/null
  ```
  ```
Exit code 1
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py`
  ```diff
  - from .test_run_pipeline import PROFILE, _fake_http_get, _fake_http_head_all_live, _run_once_kwargs, _simplify_raw
from ingestion.normalize import normalize_simplify
  + from ingestion.normalize import normalize_simplify
from test_run_pipeline import PROFILE, _fake_http_get, _run_once_kwargs, _simplify_raw
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py`
  ```diff
  - def test_run_once_never_fetches_an_already_excluded_uid(tmp_path):
    real_uid = compute_uid(normalize_simplify(_simplify_raw()[0]))
    state_dir = tmp_path / "state"
    state_dir.mkdir(parents=True)
    (state_dir / run_pipeline.EXCLUDED_UIDS_FILENAME).write_text(json.dumps([real_uid]))

    def fetch_page_fn(url):
        assert "acme" not in url.lower() or True  # placeholder, real assertion below
        raise AssertionError(f"must not fetch an already-excluded uid's URL: {url}")

    # Use a fetch_page_fn that raises for ANY call — if the excluded uid is
    # truly never reached, no call happens at all and the run completes
    # normally (other, non-excluded candidates may still legitimately fetch,
    # so scope the assertion to the specific excluded listing's URL).
    from ingestion.normalize import normalize_simplify as _ns
    excluded_listing = _ns(_simplify_raw()[0])
    calls = []

    def guarded_fetch(url):
        calls.append(url)
        if url == excluded_listing.url:
            raise AssertionError("fetched the excluded uid's URL — exclusion did not take effect")
        return ""

    kwargs = _run_once_kwargs(tmp_path, state_dir=state_dir, fetch_page_fn=guarded_fetch)
    record = run_pipeline.run_once(**kwargs)

    assert excluded_listing.url not in calls
    assert record["errors"] == []
  + def test_run_once_never_fetches_an_already_excluded_uid(tmp_path):
    """Pre-seed state/excluded_uids.json with a real candidate's uid already
    at the exclusion threshold (rather than manufacturing 5 real prior
    runs) and confirm a single run_once() never calls fetch_page_fn with
    that candidate's URL — other, non-excluded candidates in the same
    fixture set may still legitimately fetch, so the assertion is scoped to
    the specific excluded listing's own URL, not "never fetched anything"."""
    excluded_listing = normalize_simplify(_simplify_raw()[0])
    real_uid = compute_uid(excluded_listing)
    state_dir = tmp_path / "state"
    state_dir.mkdir(parents=True)
    (state_dir / run_pipeline.EXCLUDED_UIDS_FILENAME).write_text(json.dumps([real_uid]))

    calls = []

    def guarded_fetch(url):
        calls.append(url)
        if url == excluded_listing.url:
            raise AssertionError("fetched the excluded uid's URL — exclusion did not take effect")
        return ""

    kwargs = _run_once_kwargs(tmp_path, state_dir=state_dir, fetch_page_fn=guarded_fetch)
    record = run_pipeline.run_once(**kwargs)

    assert excluded_listing.url not in calls
    assert record["errors"] == []
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_debate_losses.py -q 2>&1 | tail -100`
  ```
.......                                                                  [100%]
7 passed in 0.21s
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -30`
  ```
........................................................................ [ 22%]
........................................................................ [ 44%]
........................................................................ [ 66%]
........................................................................ [ 88%]
.....................................                                    [100%]
325 passed in 1.08s
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py`
  ```diff
  - import json
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock

import pytest

import run_pipeline
from core.identity import compute_uid
from ingestion.normalize import Listing

from ingestion.normalize import normalize_simplify
from test_run_pipeline import PROFILE, _fake_http_get, _run_once_kwargs, _simplify_raw
  + import json

import run_pipeline
from core.identity import compute_uid
from ingestion.normalize import Listing, normalize_simplify
from test_run_pipeline import PROFILE, _fake_http_get, _run_once_kwargs, _simplify_raw
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -20`
  ```
........................................................................ [ 22%]
........................................................................ [ 44%]
........................................................................ [ 66%]
........................................................................ [ 88%]
.....................................                                    [100%]
325 passed in 1.84s
  ```
- `Bash` — `grep -n "render_dossier\|build_frontmatter" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py /home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
  ```
/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py:62:def build_frontmatter(listing, uid: str, date_found: str, matched_reason: str) -> dict:
/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py:97:def render_dossier(listing, uid: str, date_found: str, matched_reason: str, posting_content: str = "",
/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py:99:    frontmatter = build_frontmatter(listing, uid, date_found, matched_reason)
/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py:46:from vault_writer.writer import DOSSIER_SUBPATH, render_dossier, scan_dossiers, write_dossier
/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py:318:        markdown = render_dossier(listing, uid, date_found, build_matched_reason(listing, profile))
/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py:354:                enriched = render_dossier(listing, uid, date_found,
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
  ```diff
  - import yaml
from jinja2 import Environment, FileSystemLoader
  + import yaml
from jinja2 import Environment, FileSystemLoader

from core.identity import company_matches_preference
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
  ```diff
  - def build_frontmatter(listing, uid: str, date_found: str, matched_reason: str) -> dict:
    """uid and category are deliberately not rendered — uid stays available
    internally via the dossier_uids.json manifest (see write_dossier), and
    category was never surfaced to the reader anywhere else in the note.
    `next:` (not `promoted:`) matches every other note type's convention
    across the vault. `notes:` (always the Dossiers MOC link) and the
    `company/<slug>` tag are the Internship Notes Standard §1 interlinking
    requirement — `notes` sits right after `next`, right before `tags`."""
    return {
        "company": listing.company,
        "title": listing.title,
        "url": listing.url,
        "source": listing.source,
        "terms": _yaml_list(listing.terms),
        "locations": _yaml_list(listing.locations),
        "target_year": _yaml_list(listing.target_year),
        "date_posted": _iso_date(listing.date_posted),
        "date_found": date_found,
        "matched_reason": matched_reason,
        "status": "unreviewed",
        "next": None,
        "notes": [DOSSIERS_MOC_LINK],
        "tags": ["internship", "auto-discovered", f"company/{company_slug(listing.company)}"],
    }
  + def build_frontmatter(listing, uid: str, date_found: str, matched_reason: str,
                      preferred_companies: dict = None) -> dict:
    """uid and category are deliberately not rendered — uid stays available
    internally via the dossier_uids.json manifest (see write_dossier), and
    category was never surfaced to the reader anywhere else in the note.
    `next:` (not `promoted:`) matches every other note type's convention
    across the vault. `notes:` (always the Dossiers MOC link) and the
    `company/<slug>` tag are the Internship Notes Standard §1 interlinking
    requirement — `notes` sits right after `next`, right before `tags`.
    `preference_tier` (Prompt 5 Task O) is the matched core/profile.yaml
    preferred_companies tier, or null — required like every other field
    here, not omitted when there's no match (fail-closed, same discipline
    as REQUIRED_FRONTMATTER_FIELDS everywhere else in this file)."""
    return {
        "company": listing.company,
        "title": listing.title,
        "url": listing.url,
        "source": listing.source,
        "terms": _yaml_list(listing.terms),
        "locations": _yaml_list(listing.locations),
        "target_year": _yaml_list(listing.target_year),
        "date_posted": _iso_date(listing.date_posted),
        "date_found": date_found,
        "matched_reason": matched_reason,
        "status": "unreviewed",
        "next": None,
        "notes": [DOSSIERS_MOC_LINK],
        "preference_tier": company_matches_preference(listing.company, preferred_companies or {}),
        "tags": ["internship", "auto-discovered", f"company/{company_slug(listing.company)}"],
    }
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py`
  ```diff
  - def render_dossier(listing, uid: str, date_found: str, matched_reason: str, posting_content: str = "",
                   classification_callout: str = "") -> str:
    frontmatter = build_frontmatter(listing, uid, date_found, matched_reason)
    frontmatter_yaml = dump_frontmatter(frontmatter)
  + def render_dossier(listing, uid: str, date_found: str, matched_reason: str, posting_content: str = "",
                   classification_callout: str = "", preferred_companies: dict = None) -> str:
    frontmatter = build_frontmatter(listing, uid, date_found, matched_reason, preferred_companies)
    frontmatter_yaml = dump_frontmatter(frontmatter)
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py`
  ```diff
  - REQUIRED_FRONTMATTER_FIELDS = (
    "company", "title", "url", "source", "terms", "locations",
    "target_year", "date_posted", "date_found", "matched_reason", "status", "next", "notes", "tags",
)
  + REQUIRED_FRONTMATTER_FIELDS = (
    "company", "title", "url", "source", "terms", "locations",
    "target_year", "date_posted", "date_found", "matched_reason", "status", "next", "notes",
    "preference_tier", "tags",
)
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -         markdown = render_dossier(listing, uid, date_found, build_matched_reason(listing, profile))
  +         markdown = render_dossier(listing, uid, date_found, build_matched_reason(listing, profile),
                                  preferred_companies=profile.get("preferred_companies"))
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -                 enriched = render_dossier(listing, uid, date_found,
                                          build_matched_reason(listing, profile), posting_content,
                                          classification_callout(bucket, signal))
  +                 enriched = render_dossier(listing, uid, date_found,
                                          build_matched_reason(listing, profile), posting_content,
                                          classification_callout(bucket, signal),
                                          preferred_companies=profile.get("preferred_companies"))
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -100`
  ```
........................................................................ [ 22%]
........................................................................ [ 44%]
........................................................................ [ 66%]
........................................................................ [ 88%]
..............................F......                                    [100%]
=================================== FAILURES ===================================
___________ test_build_frontmatter_includes_moc_link_and_company_tag ___________

listing = Listing(company='Palantir', title='Forward Deployed Software Engineer – Internship - US Government', url='https://jobs...es=[], active=True, date_posted=1765581501, raw_id='[REDACTED]', sponsorship='', raw_text='')

    def test_build_frontmatter_includes_moc_link_and_company_tag(listing):
        fm = build_frontmatter(listing, f"{listing.source}:{listing.raw_id}", "2026-07-17", "reason")
    
        assert fm["notes"] == [DOSSIERS_MOC_LINK]
        assert f"company/{company_slug(listing.company)}" in fm["tags"]
        # field order: notes immediately after next, immediately before tags
        keys = list(fm.keys())
        assert keys.index("next") + 1 == keys.index("notes")
>       assert keys.index("notes") + 1 == keys.index("tags")
E       AssertionError: assert (12 + 1) == 14
E        +  where 12 = <built-in method index of list object at 0x7fa5760faec0>('notes')
E        +    where <built-in method index of list object at 0x7fa5760faec0> = ['company', 'title', 'url', 'source', 'terms', 'locations', ...].index
E        +  and   14 = <built-in method index of list object at 0x7fa5760faec0>('tags')
E        +    where <built-in method index of list object at 0x7fa5760faec0> = ['company', 'title', 'url', 'source', 'terms', 'locations', ...].index

tests/test_writer.py:154: AssertionError
=========================== short test summary info ============================
FAILED tests/test_writer.py::test_build_frontmatter_includes_moc_link_and_company_tag
1 failed, 324 passed in 1.80s
  ```
- `Bash` — `grep -n "test_build_frontmatter_includes_moc_link_and_company_tag" -A 10 /home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
  ```
146:def test_build_frontmatter_includes_moc_link_and_company_tag(listing):
147-    fm = build_frontmatter(listing, f"{listing.source}:{listing.raw_id}", "2026-07-17", "reason")
148-
149-    assert fm["notes"] == [DOSSIERS_MOC_LINK]
150-    assert f"company/{company_slug(listing.company)}" in fm["tags"]
151-    # field order: notes immediately after next, immediately before tags
152-    keys = list(fm.keys())
153-    assert keys.index("next") + 1 == keys.index("notes")
154-    assert keys.index("notes") + 1 == keys.index("tags")
155-
156-
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
  ```diff
  - def test_build_frontmatter_includes_moc_link_and_company_tag(listing):
    fm = build_frontmatter(listing, f"{listing.source}:{listing.raw_id}", "2026-07-17", "reason")

    assert fm["notes"] == [DOSSIERS_MOC_LINK]
    assert f"company/{company_slug(listing.company)}" in fm["tags"]
    # field order: notes immediately after next, immediately before tags
    keys = list(fm.keys())
    assert keys.index("next") + 1 == keys.index("notes")
    assert keys.index("notes") + 1 == keys.index("tags")
  + def test_build_frontmatter_includes_moc_link_and_company_tag(listing):
    fm = build_frontmatter(listing, f"{listing.source}:{listing.raw_id}", "2026-07-17", "reason")

    assert fm["notes"] == [DOSSIERS_MOC_LINK]
    assert f"company/{company_slug(listing.company)}" in fm["tags"]
    # field order: notes immediately after next; preference_tier (Task O)
    # sits between notes and tags; tags stays last.
    keys = list(fm.keys())
    assert keys.index("next") + 1 == keys.index("notes")
    assert keys.index("notes") + 1 == keys.index("preference_tier")
    assert keys.index("preference_tier") + 1 == keys.index("tags")
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -20`
  ```
........................................................................ [ 22%]
........................................................................ [ 44%]
........................................................................ [ 66%]
........................................................................ [ 88%]
.....................................                                    [100%]
325 passed in 4.49s
  ```
- `Bash` — `grep -n "^from vault_writer.writer import\|^from ingestion.normalize" /home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
  ```
7:from ingestion.normalize import normalize_simplify
8:from vault_writer.writer import (
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py`
  ```diff
  - def test_render_dossier_frontmatter_contains_moc_link_and_company_tag(listing):
    uid = f"{listing.source}:{listing.raw_id}"
    md = render_dossier(listing, uid, "2026-07-17", "reason")
    assert DOSSIERS_MOC_LINK in md
  + def test_render_dossier_frontmatter_contains_moc_link_and_company_tag(listing):
    uid = f"{listing.source}:{listing.raw_id}"
    md = render_dossier(listing, uid, "2026-07-17", "reason")
    assert DOSSIERS_MOC_LINK in md


# --- Task O: preference_tier frontmatter field ---

def test_build_frontmatter_preference_tier_null_when_no_preferred_companies_given(listing):
    fm = build_frontmatter(listing, f"{listing.source}:{listing.raw_id}", "2026-07-17", "reason")
    assert fm["preference_tier"] is None


def test_build_frontmatter_preference_tier_matches_real_preferred_company(listing):
    """listing's real company is 'Palantir' (tests/fixtures/simplifyjobs.json)
    — not itself in preferred_companies, so mutate it to a real preferred
    entry to show the matched-tier case."""
    listing.company = "Google"
    fm = build_frontmatter(
        listing, f"{listing.source}:{listing.raw_id}", "2026-07-17", "reason",
        preferred_companies={"Google": "high"},
    )
    assert fm["preference_tier"] == "high"


def test_render_dossier_shows_real_rendered_frontmatter_with_preference_match(listing):
    """Real rendered frontmatter (not just the dict) — confirms preference_tier
    actually serializes into the note, per the Verification section's ask to
    show a real dossier with a preference match."""
    listing.company = "Microsoft"
    uid = f"{listing.source}:{listing.raw_id}"
    md = render_dossier(
        listing, uid, "2026-07-17", "reason", preferred_companies={"Microsoft": "high"},
    )
    assert "preference_tier: high" in md
  ```
- `Bash` — `grep -n "test_format_compliance_rejects_missing_notes_field" -A 10 /home/anant_gupta/projects/work/internship-research-loop/tests/test_validate.py`
  ```
203:def test_format_compliance_rejects_missing_notes_field(listing, uid):
204-    """Confirms REQUIRED_FRONTMATTER_FIELDS actually enforces notes: — adding
205-    it to build_frontmatter() without also adding it here would mean the
206-    write gate never checks for it, silently defeating the point of the
207-    Internship Notes Standard §1 'always present, even null/[]' rule."""
208-    md = render_dossier(listing, uid, "2026-07-17", "reason")
209-    lines = [l for l in md.splitlines() if not l.startswith("notes:") and l.strip() != '  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"']
210-    broken = "\n".join(lines) + "\n"
211-    result = check_format_compliance(broken)
212-    assert result.passed is False
213-    assert "notes" in result.reason
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_validate.py`
  ```diff
  -     md = render_dossier(listing, uid, "2026-07-17", "reason")
    lines = [l for l in md.splitlines() if not l.startswith("notes:") and l.strip() != '  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"']
    broken = "\n".join(lines) + "\n"
    result = check_format_compliance(broken)
    assert result.passed is False
    assert "notes" in result.reason
  +     md = render_dossier(listing, uid, "2026-07-17", "reason")
    lines = [l for l in md.splitlines() if not l.startswith("notes:") and l.strip() != '  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"']
    broken = "\n".join(lines) + "\n"
    result = check_format_compliance(broken)
    assert result.passed is False
    assert "notes" in result.reason


# --- Task O: preference_tier is fail-closed required, like every other field ---

def test_format_compliance_rejects_missing_preference_tier_field(listing, uid):
    md = render_dossier(listing, uid, "2026-07-17", "reason")
    lines = [l for l in md.splitlines() if not l.startswith("preference_tier:")]
    broken = "\n".join(lines) + "\n"
    result = check_format_compliance(broken)
    assert result.passed is False
    assert "preference_tier" in result.reason
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -30`
  ```
........................................................................ [ 21%]
........................................................................ [ 43%]
........................................................................ [ 65%]
........................................................................ [ 87%]
.........................................                                [100%]
329 passed in 1.19s
  ```
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers MOC.md"}`
- `mcp__jarvis__vault_get_document_map` — `{"path":"10_Areas/Career/Internships/List/Dossiers MOC.md"}`
- `mcp__jarvis__vault_patch` — `{"path":"10_Areas/Career/Internships/List/Dossiers MOC.md","targetType":"heading","target":["Dossiers — Map of Content","1 — AI & ML"],"operation":"replace","ifMatch":"2cc4b4","content":"```dataview\nTABLE company, title, terms, status, preference_tier\nFROM \"10_Areas/Career/Internships/List/Dossiers/1 - AI & ML\"\nSORT preference_tier DESC, company ASC\n```"}`
- `mcp__jarvis__vault_get_document_map` — `{"path":"10_Areas/Career/Internships/List/Dossiers MOC.md"}`
- `mcp__jarvis__vault_patch` — `{"path":"10_Areas/Career/Internships/List/Dossiers MOC.md","targetType":"heading","target":["Dossiers — Map of Content","2 — Fullstack"],"operation":"replace","ifMatch":"b0ea8b","content":"```dataview\nTABLE company, title, terms, status, preference_tier\nFROM \"10_Areas/Career/Internships/List/Dossiers/2 - Fullstack\"\nSORT preference_tier DESC, company ASC\n```"}`
- `mcp__jarvis__vault_get_document_map` — `{"path":"10_Areas/Career/Internships/List/Dossiers MOC.md"}`
- `mcp__jarvis__vault_patch` — `{"path":"10_Areas/Career/Internships/List/Dossiers MOC.md","targetType":"heading","target":["Dossiers — Map of Content","3 — CyS & Finance"],"operation":"replace","ifMatch":"a1e5db","content":"```dataview\nTABLE company, title, terms, status, preference_tier\nFROM \"10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance\"\nSORT preference_tier DESC, company ASC\n```"}`
- `mcp__jarvis__vault_get_document_map` — `{"path":"10_Areas/Career/Internships/List/Dossiers MOC.md"}`
- `mcp__jarvis__vault_patch` — `{"path":"10_Areas/Career/Internships/List/Dossiers MOC.md","targetType":"heading","target":["Dossiers — Map of Content","Other — Real Software, Outside The Three Priorities"],"operation":"replace","ifMatch":"3f8735","content":"```dataview\nTABLE company, title, terms, status, preference_tier\nFROM \"10_Areas/Career/Internships/List/Dossiers/Other\"\nSORT preference_tier DESC, company ASC\n```"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers MOC.md"}`
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -15
echo "---"
git status --short
  ```
  ```
........................................................................ [ 21%]
........................................................................ [ 43%]
........................................................................ [ 65%]
........................................................................ [ 87%]
.........................................                                [100%]
329 passed in 1.61s
---
 M core/classify.py
 M core/identity.py
 M core/profile.yaml
 M core/relevance.py
 M core/run_log.py
 M ingestion/posting_page.py
 M recheck.py
 M run_pipeline.py
 M tests/test_classify.py
 M tests/test_identity.py
 M tests/test_posting_page.py
 M tests/test_relevance.py
 M tests/test_run_pipeline.py
 M tests/test_validate.py
 M tests/test_writer.py
 M vault_writer/validate.py
 M vault_writer/writer.py
?? core/debate.py
?? tests/fixtures/posting_google_careers.md
?? tests/test_debate.py
?? tests/test_debate_losses.py
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== Task L: isolated stage tests + full per-bucket sort ==="
python -m pytest tests/test_debate.py -v 2>&1 | tail -20
echo
python -m pytest tests/test_run_pipeline.py -v -k "prioritize_and_cap" 2>&1 | tail -20
  ```
  ```
=== Task L: isolated stage tests + full per-bucket sort ===
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/anant_gupta/projects/work/internship-research-loop/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/anant_gupta/projects/work/internship-research-loop
collecting ... collected 7 items

tests/test_debate.py::test_debate_compare_prefers_preferred_company_with_identical_dates PASSED [ 14%]
tests/test_debate.py::test_debate_compare_ties_between_two_preferred_companies_falls_through PASSED [ 28%]
tests/test_debate.py::test_debate_compare_prefers_bucket_at_risk_of_going_unfilled PASSED [ 42%]
tests/test_debate.py::test_debate_compare_skips_bucket_fill_need_for_same_bucket_pair PASSED [ 57%]
tests/test_debate.py::[REDACTED] PASSED [ 71%]
tests/test_debate.py::test_debate_compare_recency_is_final_tiebreak PASSED [ 85%]
tests/test_debate.py::test_debate_compare_missing_date_posted_sorts_last PASSED [100%]

============================== 7 passed in 0.06s ===============================

============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/anant_gupta/projects/work/internship-research-loop/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/anant_gupta/projects/work/internship-research-loop
collecting ... collected 36 items / 31 deselected / 5 selected

tests/test_run_pipeline.py::test_prioritize_and_cap_keeps_most_recent_first PASSED [ 20%]
tests/test_run_pipeline.py::test_prioritize_and_cap_missing_date_posted_sorts_last PASSED [ 40%]
tests/test_run_pipeline.py::test_prioritize_and_cap_orders_preferred_company_first_within_bucket PASSED [ 60%]
tests/test_run_pipeline.py::test_prioritize_and_cap_without_preferred_companies_keeps_recency_only_order PASSED [ 80%]
tests/test_run_pipeline.py::test_prioritize_and_cap_scopes_budget_per_bucket PASSED [100%]

======================= 5 passed, 31 deselected in 0.21s =======================
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== Task N: named scenarios ==="
python -m pytest tests/test_debate_losses.py -v 2>&1 | tail -20
echo
echo "=== Task O: real rendered frontmatter with preference match ==="
python3 -c "
import json
from pathlib import Path
from ingestion.normalize import normalize_simplify
from vault_writer.writer import render_dossier

raw = json.loads(Path('tests/fixtures/simplifyjobs.json').read_text())[0]
listing = normalize_simplify(raw)
listing.company = 'Google'
uid = f'{listing.source}:{listing.raw_id}'
md = render_dossier(listing, uid, '2026-07-30', 'reason', preferred_companies={'Google': 'high'})
print(md.split('---')[1])
"
  ```
  ```
=== Task N: named scenarios ===
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/anant_gupta/projects/work/internship-research-loop/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/anant_gupta/projects/work/internship-research-loop
collecting ... collected 7 items

tests/test_debate_losses.py::[REDACTED] PASSED [ 14%]
tests/test_debate_losses.py::[REDACTED] PASSED [ 28%]
tests/test_debate_losses.py::[REDACTED] PASSED [ 42%]
tests/test_debate_losses.py::test_written_uid_not_in_losses_is_a_no_op_pop PASSED [ 57%]
tests/test_debate_losses.py::test_fetch_and_filter_skips_excluded_uid PASSED [ 71%]
tests/test_debate_losses.py::test_dedup_new_skips_excluded_uid PASSED    [ 85%]
tests/test_debate_losses.py::test_run_once_never_fetches_an_already_excluded_uid PASSED [100%]

============================== 7 passed in 0.22s ===============================

=== Task O: real rendered frontmatter with preference match ===

company: Google
title: Forward Deployed Software Engineer – Internship - US Government
url: https://jobs.lever.co/palantir/[REDACTED]/apply
source: SimplifyJobs
terms:
  - Winter 2027
  - Spring 2027
  - Summer 2027
  - Fall 2027
locations:
  - Honolulu, HI
target_year: []
date_posted: '2025-12-12'
date_found: '2026-07-30'
matched_reason: reason
status: unreviewed
next:
notes:
  - '[[10_Areas/Career/Internships/List/Dossiers MOC]]'
preference_tier: high
tags:
  - internship
  - auto-discovered
  - company/google
  ```
- `Bash`:
  ```bash
source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop
python -m pytest tests/ -q 2>&1 | tail -10
echo "---profile.yaml diff---"
git diff core/profile.yaml
  ```
  ```
........................................................................ [ 21%]
........................................................................ [ 43%]
........................................................................ [ 65%]
........................................................................ [ 87%]
.........................................                                [100%]
329 passed in 1.35s
---profile.yaml diff---
diff --git a/core/profile.yaml b/core/profile.yaml
index 21c3c97..c73d41b 100644
--- a/core/profile.yaml
+++ b/core/profile.yaml
@@ -47,3 +47,31 @@ locations_allow: us_remote
 # 592, ("PhD",) 586, empty 4676 — fetched 2026-07-18). Permissive: empty degrees
 # data passes; non-empty must intersect this list.
 degrees_allow: ["Bachelor's"]
+# Preference weight for the debate comparator (Prompt 5 Task L), not a filter
+# gate — a non-matching company still passes everything above unaffected.
+# Seeded from the real, human-vetted target list in the vault's
+# `20_Progress/Internship/Building System/Research Loop - Resources.md`
+# "Named-Program Coverage Check (2026-07-29)" section: 11 named early-talent
+# programs the human already identified as worth prioritizing, of which only
+# 3/11 have ANY dossier coverage today and none confirmed as the specific
+# named program (Jane Street FTTP, Two Sigma First-Year, D.E. Shaw, Citadel
+# Launch, Google ASDI, Microsoft Explore, LinkedIn First Play, MLH
+# Fellowship, NASA OSTEM, Capital One, Bloomberg). This is a starting point
+# for the human to re-tier or add/remove entries directly, not a final
+# answer — company preference is an explicit human judgment call per
+# `30_Order/Workflows/Internship Pipeline.md`'s Step 2 ("Screen"), and this
+# dict only wires that judgment into write-priority ordering, it doesn't
+# automate the judgment itself. All seeded at one tier for now; a
+# multi-tier scheme wasn't asked for.
+preferred_companies:
+  "Jane Street": high
+  "Two Sigma": high
+  "D.E. Shaw": high
+  "Citadel": high
+  "Google": high
+  "Microsoft": high
+  "LinkedIn": high
+  "MLH": high
+  "NASA": high
+  "Capital One": high
+  "Bloomberg": high
  ```

## Actions Taken
- Files created: /home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/posting_google_careers.md, /home/anant_gupta/projects/work/internship-research-loop/core/debate.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_debate.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py
- Files modified: /home/anant_gupta/projects/work/internship-research-loop/core/relevance.py, /home/anant_gupta/projects/work/internship-research-loop/core/classify.py, /home/anant_gupta/projects/work/internship-research-loop/core/identity.py, /home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py, /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py, /home/anant_gupta/projects/work/internship-research-loop/ingestion/posting_page.py, /home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py, /home/anant_gupta/projects/work/internship-research-loop/recheck.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_posting_page.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_relevance.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_classify.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_validate.py, /home/anant_gupta/projects/work/internship-research-loop/core/profile.yaml, /home/anant_gupta/projects/work/internship-research-loop/core/run_log.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py
- Files deleted: (none)
- Commands run: echo "=== relevance.py ===" && grep -n "def stage1_reject\|def stage2_confirm" core/relevance.py && echo "=== classify.py ===" && grep -n "def classify\|BUCKET_FOLDERS" core/classify.py && echo "=== writer.py priority routing ===" && grep -n "priority\|BUCKET_FOLDERS\|def build_frontmatter\|def write_dossier\|def load_dossier_uids\|def save_dossier_uids" vault_writer/writer.py, find . -type f -name "*.py" | grep -v __pycache__ | sort, find . -type f -name "*.py" -not -path "./.venv/*" | sort echo "---" find / -maxdepth 4 -iname "*jarvis*" -type d 2>/dev/null find $HOME -maxdepth 3 -iname "*vault*" -type d 2>/dev/null find $HOME/projects -maxdepth 2 -type d 2>/dev/null, cat /home/anant_gupta/projects/work/internship-research-loop/vault_writer/templates/dossier.md.j2 echo "---FIXTURES---" ls /home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/ echo "---THROWAWAY VAULT---" find /home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/throwaway_vault -maxdepth 5 echo "---run_log.py---" cat /home/anant_gupta/projects/work/internship-research-loop/core/run_log.py echo "---profile.yaml---" cat /home/anant_gupta/projects/work/internship-research-loop/core/profile.yaml 2>/dev/null || cat /home/anant_gupta/projects/work/internship-research-loop/profile.yaml 2>/dev/null, grep -n "threat" tests/*.py core/*.py; echo "---"; grep -rn "cross_source_key" --include=*.py ., source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -60, source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -30, source .venv/bin/activate 2>/dev/null python3 -c " import json raw = json.loads(open('tests/fixtures/simplifyjobs.json').read())[0] print(raw.get('title'), '|', raw.get('category')) from core.classify import classify print(classify(raw.get('title'), raw.get('category'), '')) " grep -n "STATE_DIR\|state_dir\|state/" run_pipeline.py | head -30, source .venv/bin/activate 2>/dev/null; python -m pytest tests/ -q 2>&1 | tail -80, source .venv/bin/activate 2>/dev/null python3 -c " import sys sys.path.insert(0,'tests') from test_run_pipeline import _fake_http_get, PROFILE import run_pipeline from collections import Counter matched = run_pipeline.fetch_and_filter(PROFILE, http_get=_fake_http_get) from core.classify import classify buckets = Counter() total=0 for name, info in matched.items(): for l in info['matched']: b,_ = classify(l.title, l.category, '') buckets[b]+=1 total+=1 print('total', total) print(buckets) " , source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_posting_page.py -q 2>&1 | tail -100, source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_posting_page.py -q 2>&1 | tail -60, source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_relevance.py tests/test_classify.py -q 2>&1 | tail -60, source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_identity.py -q 2>&1 | tail -60, source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_writer.py -q 2>&1 | tail -100, source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_validate.py -q 2>&1 | tail -60, grep -n "^def _run_once_kwargs" -A 20 /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py, tail -5 /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py, source .venv/bin/activate 2>/dev/null; python -m pytest tests/test_run_pipeline.py -q 2>&1 | tail -150, source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 << 'EOF' from core.relevance import stage1_reject, stage2_confirm from core.classify import classify from core.identity import cross_source_key from ingestion.posting_page import phd_only_exclusion, extract_content print("=== Task B: Databricks Product Management Intern ===") print("stage1_reject:", stage1_reject("Product Management Intern (Summer 2027)", "")) print("=== Task B: Conagra Demand Science Rotational Analyst ===") print("stage1_reject:", stage1_reject("Demand Science Rotational Analyst", "")) print("=== Task C: Mosaic Operations & Automation Engineering ===") mosaic_content = ( "Requires a Bachelor's degree in Chemical Engineering or related field. Experience with PLC, DCS, " "and SCADA control systems preferred. Basic computer skills required. Must be able to lift 50 lbs " "and wear a respirator as needed. The Company will not require an employee to perform any duty " "without posing a direct threat to the safety of his or her own self or others." ) print("stage2_confirm:", stage2_confirm("Operations & Automation Engineering Co-op/Intern", "The Mosaic Company", mosaic_content)) bucket, signal = classify("Operations & Automation Engineering Co-op/Intern", "", mosaic_content) print("classify bucket:", bucket, "signal:", repr(signal)) print("=== Task D: real dedup incidents ===") virtu_url = "https://job-boards.greenhouse.io/virtu/jobs/8624410002" keys = { cross_source_key("Virtu Financial", "2027 Internship - Software Engineer", virtu_url), cross_source_key("Virtu Financial", "Software Engineer Intern - Software Engineer", virtu_url), cross_source_key("Virtu Financial", "Software Engineer Intern", virtu_url), } print("Virtu triple-dup collapses to", len(keys), "key(s)") google_key_a = cross_source_key("Google", "Software Engineering Intern", "https://www.google.com/about/careers/applications/jobs/results/85564713261245126") google_key_b = cross_source_key("Google", "Software Engineering Intern, BS, Summer 2027", "https://www.google.com/about/careers/applications/jobs/results/85564713261245126") print("Google BS/MS dup collapses:", google_key_a == google_key_b) pal_a = cross_source_key("Palantir", "Forward Deployed Software Engineer Intern - Intel", "https://jobs.lever.co/palantir/[REDACTED]/apply") pal_b = cross_source_key("Palantir", "Forward Deployed Software Engineer, Internship - Intel", "https://jobs.lever.co/palantir/[REDACTED]") print("Palantir cross-bucket dup collapses:", pal_a == pal_b) aq_url = "https://job-boards.greenhouse.io/aquaticcapitalmanagement/jobs/8489233002" print("Aquatic name-variant dup collapses:", cross_source_key("Aquatic", "Software Engineer Intern", aq_url) == cross_source_key("Aquatic Capital Management", "Software Engineer Intern", aq_url)) print("=== Task F: Optiver PhD-only real content ===") optiver_text = ( "As part of our assessment process, you may be invited to participate in a multi-day, on-site " "evaluative program.\nWho You Are:\n- Currently enrolled in a PhD program in Statistics, Computer " "Science, Machine Learning, Mathematics, or a related STEM field with outstanding academic " "performance\n- Expected graduation between December 2027 - June 2029" ) print("phd_only_exclusion:", phd_only_exclusion(optiver_text)) print("=== Task F: false-positive check on real BS/MS eligible fixtures ===") aquatic_text = "Active student pursuing a BS, MS, or PhD in mathematics, statistics, machine learning, physics, computer science, or other scientific disciplines with an expected graduation date between Fall 2027 and Spring 2028." appian_text = "Currently pursuing a Bachelor's or Master's degree in Computer Science or Computer Engineering with a strong academic record." print("Aquatic (should be None):", phd_only_exclusion(aquatic_text)) print("Appian (should be None):", phd_only_exclusion(appian_text)) EOF, source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 << 'EOF' from ingestion.posting_page import extract_content print("=== Task E: Google careers listing-shell extraction ===") md = open("tests/fixtures/posting_google_careers.md", encoding="utf-8").read() content = extract_content(md) print(content[:300]) print("...") print("Contains unrelated job 'Senior Product Engineer, Machine Learning Accelerators':", "Senior Product Engineer, Machine Learning Accelerators" in content) print("Contains real posting content:", "pursuing a Master's degree" in content) EOF, source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 << 'PYEOF' from ingestion.posting_page import extract_content # Real Conagra raw markdown reconstructed from the actual vault dossier content # (the part after "## Posting (fetched ...)" in the dossier IS extract_content's # prior output already run through the OLD buggy code — to test the NEW code # we need the underlying raw fetched markdown shape, which the dossier no longer # has since it was already processed. We approximate using the real duplicated # structure that's visible: the About Us paragraph appears twice in the existing # dossier body itself, which is proof enough since extract_content is idempotent-ish # on already-partially-cleaned text for the dedup check.) conagra_body = open("/tmp claude-test-conagra.txt") if False else None PYEOF, source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 << 'PYEOF' from ingestion.posting_page import extract_content # Real content, copied verbatim from the Conagra Brands dossier's existing # "## Posting (fetched 2026-07-27)" body (that body IS the old extract_content's # broken output, since it was never deduped/split/sectioned) — using it as the # raw input to the NEW extract_content demonstrates the fix on the real bug. conagra_raw = """## Demand Science Rotational Analyst - Summer 2027 locationsChicago, Illinois time typeFull time posted onPosted Today job requisition idReq-039400 Have a taste for something big? Launch your career at Conagra Brands, one of North America's leading branded food companies! **Is the Demand Science Rotational Program right for you?** Are you excited by data and translating analytics into marketplace predictions? **Compensation** Pay Range:$59,000-$79,000 ### About Us At Conagra Brands, we have a rich heritage of making great food. We aspire to have the most impactful, energized and inclusive culture in food. As a member of our 18,000+ person team across 40+ locations, you are empowered to reach your potential, make an impact and own your career. We're in the business of building champions - within our people and our iconic brands like Birds Eye, Slim Jim and Reddi-Wip. Our focus on innovation extends beyond making great food, it also reflects our commitment to embracing new solutions. ### About Us At Conagra Brands, we have a rich heritage of making great food. We aspire to have the most impactful, energized and inclusive culture in food. As a member of our 18,000+ person team across 40+ locations, you are empowered to reach your potential, make an impact and own your career. We're in the business of building champions - within our people and our iconic brands like Birds Eye, Slim Jim and Reddi-Wip. """ before = conagra_raw after = extract_content(conagra_raw) print("=== BEFORE (raw, as old extract_content would have left it) ===") print(before) print("=== AFTER (new extract_content) ===") print(after) print() print("Duplicate paragraph count in AFTER:", after.count("As a member of our 18,000+ person team")) print("ATS chrome split:", "locations\nChicago, Illinois" in after) print("Compensation as heading:", "### Compensation" in after) PYEOF, source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 << 'PYEOF' from ingestion.posting_page import extract_content manhattan_raw = """## A.I. Developer Co-Op (Boston, MA) locationsUS - Home Office time typeFull time posted onPosted 15 Days Ago We are seeking a motivated AI Developer Co-op who is currently pursuing a degree in Computer Science, Artificial Intelligence, Data Science, or a related field. ### About Us At Manhattan Associates our supply chain and omnichannel technology positively affect how people work, shop and live - every single day. Read More #### Follow Us - [LinkedIn](https://www.linkedin.com/company/4376?trk=tyah "LinkedIn") - [X](https://twitter.com/ManhAssocNews "X") - [Facebook](https://www.facebook.com/pages/Manhattan-Associates/113391905337615?fref=ts "Facebook") """ before = manhattan_raw after = extract_content(manhattan_raw) print("=== BEFORE ===") print(before) print("=== AFTER ===") print(after) print() print("Read More stripped:", "Read More" not in after) print("Follow Us stripped:", "Follow Us" not in after) print("LinkedIn link stripped:", "linkedin.com" not in after) PYEOF, source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 << 'PYEOF' from ingestion.posting_page import extract_content manhattan_raw = """## A.I. Developer Co-Op (Boston, MA) locationsUS - Home Office ### About Us At Manhattan Associates our supply chain and omnichannel technology positively affect how people work, shop and live - every single day. Read More #### Follow Us - [LinkedIn](https://www.linkedin.com/company/4376?trk=tyah "LinkedIn") - [X](https://twitter.com/ManhAssocNews "X") - [Facebook](https://www.facebook.com/pages/Manhattan-Associates/113391905337615?fref=ts "Facebook") """ after = extract_content(manhattan_raw) print(after) print("LinkedIn stripped:", "linkedin.com" not in after) PYEOF python -m pytest tests/ -q 2>&1 | tail -20, source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 << 'PYEOF' import json, tempfile from pathlib import Path from ingestion.normalize import normalize_simplify from vault_writer.writer import render_dossier, write_dossier, move_dossier_to_viewed raw = json.loads(Path("tests/fixtures/simplifyjobs.json").read_text())[0] listing = normalize_simplify(raw) uid = f"{listing.source}:{listing.raw_id}" md = render_dossier(listing, uid, "2026-07-30", "reason") print("=== BEFORE (Task G): rendered frontmatter ===") print(md.split("---")[1]) with tempfile.TemporaryDirectory() as tmp: vault = Path(tmp) / "vault" state_dir = Path(tmp) / "state" path = write_dossier(vault, uid, md, listing.title, listing.company, "Other", state_dir=state_dir) print("=== Task H: AFTER move_dossier_to_viewed ===") new_path = move_dossier_to_viewed(vault, path, "absent from live feed", "2026-07-30", state_dir=state_dir) print(new_path.read_text().split("---")[1]) print("File now at:", new_path.relative_to(vault)) PYEOF, source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python -m pytest tests/ -q 2>&1 | tail -10 echo "---" git status --short | head -30, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -10, source .venv/bin/activate 2>/dev/null python3 -c " from core.identity import extract_ats_job_id print(extract_ats_job_id('https://random-startup.com/careers/jobs/results/12345')) ", source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 -c " from core.identity import extract_ats_job_id print('unrelated domain (should be None):', extract_ats_job_id('https://random-startup.com/careers/jobs/results/12345')) print('real Google URL (should extract):', extract_ats_job_id('https://www.google.com/about/careers/applications/jobs/results/95141459539174086')) print('real Google URL 2 (should extract):', extract_ats_job_id('https://www.google.com/about/careers/applications/jobs/results/85564713261245126')) ", source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -20, grep -n "google_careers_results_url\|test_extract_ats_job_id" /home/anant_gupta/projects/work/internship-research-loop/tests/test_identity.py, source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 -c " import tempfile from pathlib import Path from vault_writer.writer import move_dossier_to_viewed, DOSSIER_SUBPATH with tempfile.TemporaryDirectory() as tmp: vault = Path(tmp) a_dir = vault / DOSSIER_SUBPATH / 'Other' b_dir = vault / DOSSIER_SUBPATH / '1 - AI & ML' a_dir.mkdir(parents=True) b_dir.mkdir(parents=True) fm = '''--- company: Acme title: SWE Intern url: https://acme.example/a source: SimplifyJobs terms: [] locations: [] target_year: [] date_posted: date_found: '2026-07-17' matched_reason: reason status: unreviewed next: notes: - x tags: - internship --- # SWE Intern Content A ''' fm_b = fm.replace('Content A', 'Content B').replace('acme.example/a', 'acme.example/b') (a_dir / 'SWE Intern - Acme.md').write_text(fm) (b_dir / 'SWE Intern - Acme.md').write_text(fm_b) p1 = move_dossier_to_viewed(vault, a_dir / 'SWE Intern - Acme.md', 'absent from live feed', '2026-07-30') p2 = move_dossier_to_viewed(vault, b_dir / 'SWE Intern - Acme.md', 'absent from live feed', '2026-07-30') print('p1:', p1) print('p2:', p2) print('p1 == p2 (collision, data loss):', p1 == p2) viewed_dir = vault / DOSSIER_SUBPATH / 'Viewed' print('files in Viewed/:', list(viewed_dir.iterdir())) " , source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 -c " import tempfile from pathlib import Path from vault_writer.writer import move_dossier_to_viewed, DOSSIER_SUBPATH with tempfile.TemporaryDirectory() as tmp: vault = Path(tmp) a_dir = vault / DOSSIER_SUBPATH / 'Other' b_dir = vault / DOSSIER_SUBPATH / '1 - AI & ML' a_dir.mkdir(parents=True) b_dir.mkdir(parents=True) fm = '''--- company: Acme title: SWE Intern url: https://acme.example/a source: SimplifyJobs terms: [] locations: [] target_year: [] date_posted: date_found: '2026-07-17' matched_reason: reason status: unreviewed next: notes: - x tags: - internship --- # SWE Intern Content A ''' fm_b = fm.replace('Content A', 'Content B').replace('acme.example/a', 'acme.example/b') (a_dir / 'SWE Intern - Acme.md').write_text(fm) (b_dir / 'SWE Intern - Acme.md').write_text(fm_b) p1 = move_dossier_to_viewed(vault, a_dir / 'SWE Intern - Acme.md', 'absent from live feed', '2026-07-30') p2 = move_dossier_to_viewed(vault, b_dir / 'SWE Intern - Acme.md', 'absent from live feed', '2026-07-30') print('p1:', p1.name) print('p2:', p2.name) print('p1 == p2 (should be False now):', p1 == p2) viewed_dir = vault / DOSSIER_SUBPATH / 'Viewed' print('files in Viewed/:', sorted(p.name for p in viewed_dir.iterdir())) print('p1 content preserved:', 'Content A' in p1.read_text()) print('p2 content preserved:', 'Content B' in p2.read_text()) " , grep -n "def test_move_dossier_to_viewed" /home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_writer.py tests/test_identity.py -q 2>&1 | tail -30, source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 -c " from core.identity import company_matches_preference from core.filter import load_profile profile = load_profile() preferred = profile['preferred_companies'] print(company_matches_preference('D.E. Shaw', preferred)) print(company_matches_preference('DE Shaw', preferred)) print(company_matches_preference('Random Startup', preferred)) " python -m pytest tests/ -q 2>&1 | tail -10, source .venv/bin/activate 2>/dev/null python3 -c " import re norm = lambda s: re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip() print(repr(norm('D.E. Shaw'))) print(repr(norm('DE Shaw'))) ", source .venv/bin/activate 2>/dev/null cd /home/anant_gupta/projects/work/internship-research-loop python3 -c " from core.identity import company_matches_preference from core.filter import load_profile profile = load_profile() preferred = profile['preferred_companies'] print('D.E. Shaw:', company_matches_preference('D.E. Shaw', preferred)) print('DE Shaw:', company_matches_preference('DE Shaw', preferred)) print('Random:', company_matches_preference('Random Startup', preferred)) print('google (lowercase):', company_matches_preference('google', preferred)) " python -m pytest tests/ -q 2>&1 | tail -10, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_identity.py -q 2>&1 | tail -30, grep -n "_prioritize_and_cap(new_listings" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -60, grep -n "^from ingestion.normalize\|^def _simplify_raw\|^def _listing_with_date" /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py, grep -n "^def _simplify_raw" -A 5 /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py echo "---" python3 -c " import json raw = json.loads(open('/home/anant_gupta/projects/work/internship-research-loop/tests/fixtures/simplifyjobs.json').read())[0] print(raw['company_name'], raw['title'], raw['category']) ", source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_debate.py -q 2>&1 | tail -100, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_run_pipeline.py -q 2>&1 | tail -100, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_run_log.py -q 2>&1 | tail -30, grep -n "^def fetch_and_filter\|^def dedup_new" -A 15 /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py, grep -n "def run_once\|seen_ids = load_seen_ids\|matched_by_source = fetch_and_filter\|new_listings, already_seen_count\|this_run, deferred\|written_uids, rejections = validate_and_write\|record\[.rejections.\]\|record\[.bucket_at_capacity.\]" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py, ls -la /home/anant_gupta/projects/work/internship-research-loop/tests/ | grep -i init cat /home/anant_gupta/projects/work/internship-research-loop/pytest.ini 2>/dev/null || cat /home/anant_gupta/projects/work/internship-research-loop/setup.cfg 2>/dev/null || cat /home/anant_gupta/projects/work/internship-research-loop/pyproject.toml 2>/dev/null, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/test_debate_losses.py -q 2>&1 | tail -100, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -30, grep -n "render_dossier\|build_frontmatter" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py /home/anant_gupta/projects/work/internship-research-loop/vault_writer/writer.py, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -100, grep -n "test_build_frontmatter_includes_moc_link_and_company_tag" -A 10 /home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py, grep -n "^from vault_writer.writer import\|^from ingestion.normalize" /home/anant_gupta/projects/work/internship-research-loop/tests/test_writer.py, grep -n "test_format_compliance_rejects_missing_notes_field" -A 10 /home/anant_gupta/projects/work/internship-research-loop/tests/test_validate.py, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop; python -m pytest tests/ -q 2>&1 | tail -15 echo "---" git status --short, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop echo "=== Task L: isolated stage tests + full per-bucket sort ===" python -m pytest tests/test_debate.py -v 2>&1 | tail -20 echo python -m pytest tests/test_run_pipeline.py -v -k "prioritize_and_cap" 2>&1 | tail -20, source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop echo "=== Task N: named scenarios ===" python -m pytest tests/test_debate_losses.py -v 2>&1 | tail -20 echo echo "=== Task O: real rendered frontmatter with preference match ===" python3 -c " import json from pathlib import Path from ingestion.normalize import normalize_simplify from vault_writer.writer import render_dossier raw = json.loads(Path('tests/fixtures/simplifyjobs.json').read_text())[0] listing = normalize_simplify(raw) listing.company = 'Google' uid = f'{listing.source}:{listing.raw_id}' md = render_dossier(listing, uid, '2026-07-30', 'reason', preferred_companies={'Google': 'high'}) print(md.split('---')[1]) ", source .venv/bin/activate 2>/dev/null; cd /home/anant_gupta/projects/work/internship-research-loop python -m pytest tests/ -q 2>&1 | tail -10 echo "---profile.yaml diff---" git diff core/profile.yaml
- Tool call tally: Bash (76), Edit (77), mcp__jarvis__vault_get_document_map (7), mcp__jarvis__vault_list (5), mcp__jarvis__vault_patch (5), mcp__jarvis__vault_read (20), Read (62), TaskCreate (1), ToolSearch (3), Write (4)


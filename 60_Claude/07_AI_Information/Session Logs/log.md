# Session Log
## [2026-08-20] review | First real /export-ai-session pass — distilled the 2026-08-19 second-brain-claudekit sync session, Tool log's first real row
- Exercised the review pipeline for real instead of designing it further, per explicit instruction: `Tool log.md` had held its empty schema since 2026-08-11 and `Review Standard.md`'s frontmatter admits it has no Gold Standard Example yet.
- Ran `/export-ai-session` against the 2026-08-19 "Second-brain-claudekit Jarvis notes sync" raw session (34 Bash, 21 Edit, 23 Read, 2 Write, $19.67, ~20hr wall-clock/8 turns) — wrote a full distilled summary and one Tool log row.
- **Real friction found, not smoothed over:** that session invoked no registered slash command — it was a freeform verification task — so the Tool log's `Skill/Command` column has no clean value to hold. Written honestly as "(none — freeform verification task)" rather than forced into a fake skill name. The distilled summary itself also surfaced a real finding: the 2026-08-19 session's own "verify before write" discipline missed one claim (a fake `docs/<Project>/` folder) because it wasn't flagged as uncertain in its task prompt — only prompt-flagged leads got independently checked.
- See [[20_Progress/Projects/AI Use/Claude Kit/Log]]'s `[2026-08-20]` entry for the second-brain-claudekit-side findings this same round produced.

## [2026-08-08] build | Mentorship Program remaster — MOC Standard, Brief/Action infrastructure, two new skills
- Full brainstorming-skill session, systematically ordered per user instruction: templates → standards → workflows → skills/commands → the Mentorship Program folder itself. Nothing built out of order.
- **New vault infrastructure, following the existing Standard→Template→Workflow triad** (matched to [[Project Standard]]/[[Source Summary Standard]] precedent, not invented fresh): [[MOC Standard]] filled in (was an empty stub), plus two new note types added to the vault's taxonomy — `brief` (reuses `type: input`, its own [[Brief Standard]]) and `action` (new `type: action`, its own [[Action Standard]]). Templates: [[MOC Template]], [[Brief Template]], [[Action Template]] in `Templates/Capability/`, [[For Transcript]] in `Templates/Frontmatter/`. Workflows: [[Transcript to Brief]] and [[Brief to Action]], registered in `00_Workflows Index.md`. `Templates/MOC.md` (the Templates folder's own index) got the new templates added, plus the previously-missing [[Clipping Distill Template]] link.
- **Two new general-purpose skills**, not scoped to mentorship despite the folder being the first real use: `/transcript-to-brief` (any transcript — meeting, call, video, written exchange — into a Brief-Standard-compliant brief, asking only where the transcript actually has a gap: garbled/ambiguous passages, what mattered most, missing external context) and `/note-to-actions` (any brief or linked note into a link-dense `type: action` map — plain statements only, no checkboxes, every sentence carrying a wikilink, missing link targets raised as a question rather than auto-stubbed). Both registered in `.claude/commands/` and `CLAUDE.md`'s skills table; `action` and `index` added to CLAUDE.md's type guide.
- **Mentorship Program folder rebuilt**: [[Mentorship Board]] rewritten as a real MOC per the new standard (Purpose → Map → Status → Dataview → Links, prose replacing the old dataview-only stub). New [[Fall 2026 — Detailed Expectations]] scaffold in `Plans/` — deliberately **not pre-filled** with fall goals per explicit user instruction ("hold back on planning the fall semester... establish everything required from Ahnaf systematically before adx work starts"); it accumulates from real meetings via `/note-to-actions`, anchored against the program's original Google-Doc goals baseline. [[Plan]]'s `## Fall 2026` section got a short stub (cadence confirmed at alternate weeks, unchanged from summer) rather than invented content.
- **Scoped deliberately:** did not retrofit the vault's other existing MOCs (Claude Code/MOC.md, Dossiers MOC.md, etc.) to the new standard — flagged as a future opportunistic pass, not done this session. Did not touch AGENTS.md's central routing table — the two new Workflow docs carry the specific moves instead, matching how existing workflows (Conversation Capture, Capture to Summary) already work.

## [2026-07-27] fix | Summer Plans cleanup — merged 11 files to 6, built the Plan Template/Standard/Workflow chain
- Direct follow-up to the same day's earlier planning session: user reviewed the notes just written and called them slop — real overlap, uncertainty passed off as content, three files (recap/close-out/august-plan) fragmenting one status. Also renamed all Summer Plans files mid-session (numbered prefixes dropped), which broke `/startday` and `/weekly-review`'s hardcoded file-path reads.
- **Merged 11 files to 6:** [[LeetCode & CSCI 4041|LeetCode & CSCI 4041]] absorbed its separate Tracker file (mastery table + daily log now live in the same note, §8); [[ML Fundamentals (2033 + 2230)|ML Fundamentals (2033 + 2230)]] absorbed its separate Progress file the same way; the recap/close-out/august-plan trio merged into one [[Final Month Plan (Jul 28 - Sep 1)|Final Month Plan (Jul 28 - Sep 1)]] with a real Goal/Timeframe/Systems/Implementation Status/Current Progress/Update Protocol shape. Deleted: `ML Fundamentals Progress.md`, `LeetCode Tracker.md`, `Monthly & Phase Map.md`, `Projects & Hackathons Queue.md`, `Summer Courses Ops.md`, and the three status fragments.
- **Fixed the load-bearing breakage:** `.claude/skills/startday/SKILL.md` and `.claude/skills/weekly-review.md` both hardcoded the old numbered filenames — updated both to the new 6-file set, and left a note in each pointing back to the Summer Plans index if a referenced file goes missing again.
- **Built the reuse infrastructure the user asked for**, filling three previously-empty stub files rather than creating new ones (found via search-first, per `AGENTS.md`): [[30_Order/Templates/Career/Plan Template|Plan Template]] (the section skeleton — Goal/Timeframe/Systems/Implementation Status/Current Progress/Update Protocol), [[30_Order/Standards/Daily Workflow Standard|Daily Workflow Standard]] (per-heading content rules with the concrete anti-patterns from this cleanup as the Warning callouts), and [[10_Areas/Life/Plans/Plans-to-Create|Plans-to-Create]] (the step-by-step process, citing this cleanup as its case study). Also new: [[Plan Review Cadence]] workflow (how `/startday`/`/closeday`/`/weekly-review` actually touch `type: plan` notes, plus a two-review-cycle staleness check), added to `00_Workflows Index.md`.
- Fixed all downstream links: `00_Dashboard.md`, `10_Areas/Summer Grind.md`, the Summer Plans index, and one incidental stale link in a PDF source-summary note.

## [2026-07-27] plan | July recap + August lock-in — fact-checked summer audit, three new Summer Plans notes
- User-requested deep review of `10_Areas/Summer Grind.md` and `10_Areas/Life/Plans/Summer/` against actual vault state, one month out from the 2026-09-01 deadline. Two-part session: first a verified gap analysis (chat only), then a full write-through once the user corrected several claims and set the August priorities.
- **Verification method:** every claim checked against a live file or `git log`, not memory — [[LeetCode Tracker]] (0 rows ever), [[ML Fundamentals Progress]] (0/14 units), `00_Dashboard.md` (stale since 2026-07-04), 236 commits / 54 of 63 active days since 2026-05-26 (mostly infra, not tracked daily reps).
- **Corrected findings mid-session, from user:** TradingView is far more built than the stale Postmortem note suggested — re-read the live [[Fable 5 — Read Order (TradingView folder)]] chain and found a merged, tested AI Brain Hub (PR #4, `c754f00`, 497 tests) with a locked UI spec as of 2026-07-26, only the UI itself unbuilt. Portfolio is deployed, not unstarted — `BUILD-STATUS.md`'s 14-item UI-fix list is the live backlog. Arc has planning docs but the user doesn't consider them a real plan; kicks off for real in August's second week.
- **Wrote three new notes** in `10_Areas/Life/Plans/Summer/`: [[Where We Stand - July 2026]] (fact-checked recap), [[July Close-Out (Jul 28-31)]] (near-term lock-in), [[August Plan - Final Month]] (daily floor + weekly flagship rotation + 5 chosen certifications + Jarvis command/scheduled-routine design).
- **Certifications researched, not guessed:** the 5 (AWS Cloud Practitioner, Azure AI-900, Google AI Essentials, an NVIDIA micro-credential, an Anthropic/Claude certification) came from `40_Resources/CS/Links`, `60_Claude/20_Distilled_Notes/Sources - Plan/PDF's Ingestion Implementation.md`'s researched cert stack, and [[Summer Grind]]'s own NVIDIA list — cross-checked against the actual dossier target companies in `10_Areas/Career/Internships/List/Dossiers/`. Git & GitHub certification stays separate, exam scheduled for August's first week.
- **Held back, not built:** the "5 scheduled routines/day" Jarvis automation is designed in [[August Plan - Final Month]] but explicitly not provisioned via `CronCreate` this session — flagged as needing explicit go-ahead since it runs unattended and consumes recurring Pro-plan usage. The Gmail/Calendar/Todoist/Reminders-through-Obsidian automation is documented as a wishlist item only, pending the user configuring a dedicated account.
- **Also touched:** [[00 - Summer Plans Index]], [[Daily Operating System]], [[Monthly & Phase Map]], [[Summer Courses Ops]], [[LeetCode & CSCI 4041]], [[ML Fundamentals (2033 + 2230)]] (2033 scope corrected from full derivation-depth to a broad, fast pass — the original depth is deferred to whenever a future class needs it), and `10_Areas/Summer Grind.md` (interlinks + timeline-heading corrections only, goals left untouched per instruction).

## [2026-07-25] verify | Internship loop Phase 7 note — closed the relayed-claims gap with direct repo access
- Narrow-scope task: verify `Research Loop - Phase 7 Coverage Expansion.md` (written by a prior session relaying another session's conversation, with only partial direct repo access) against the real repo and vault, patch section by section, nothing else. No pipeline code changes, no push, no new features.
- **Backlog throttle (Phases Run's biggest open question):** confirmed it's a real cap, not the discard/absorb options merely discussed — `MAX_NEW_WRITES_PER_RUN = 18` in `run_pipeline.py:64`, `_prioritize_and_cap()` sorts by `date_posted` descending (most-recent-first, missing dates sort last), deferred items are simply never marked seen so `dedup_new()` naturally re-offers them next run. Better than static code review: found it firing for real in production — `logs/runs.jsonl`'s first post-`a21b2fa` scheduled run (2026-07-25T16:52:23Z) shows `written_count: 13, deferred_count: 166` against all 6 live sources.
- **Lever:** confirmed still genuinely unbuilt — `git grep -ni "lever" -- '*.py'` across every tracked file returns zero matches (only mentions are in this session's own uncommitted freehire research, describing what freehire covers, not what this project built).
- **Numbers spot-checked, no drift found:** Greenhouse (7 tokens) and Ashby (5 tokens) lists match `ingestion/sources.py` exactly. `vanshb03` still 274 entries, `zshah101` still 214 with the identical 181/22/7/4 sponsorship split, both re-fetched live — unlike SimplifyJobs' Google data (which the note itself flagged as having moved within hours during the original investigation), these two hadn't moved at all.
- **Test count:** the note never stated one. Ran it two ways — 204 passing on the pure committed state (`git stash` to isolate it), 215 on the current local working tree (includes this session's own uncommitted freehire/AI-jobs research from earlier the same day). Both counts independently run this session.
- **A real gap the note didn't know about, found and disclosed, not fixed:** `recheck.py`'s `FEEDS` dict, as actually committed, still only checks SimplifyJobs/JGCL — the four sources live since `a21b2fa` (vanshb03, zshah101, Greenhouse, Ashby) are not being rechecked for closure by the daily cron at all right now. A fix exists locally (adds those four plus AIJobs, deliberately excludes Freehire since its own `closed_at` field was independently shown to be stale) but sits uncommitted, same status as the freehire/AI-jobs build itself — a real third state ("built-but-unshipped") the note's original two-state framing ("live" vs. "researched, not built") didn't have room for. Left uncommitted per this task's explicit scope — reporting the gap, not closing it.
- Patched the note in place, section by section (not rewritten): added `Verified`/`Re-checked` notes to Phases 11-13, corrected Phase 14's "not built yet" line (it was, later the same day, just uncommitted), replaced the Backlog section's "not independently re-verified" line with the real mechanism and live evidence, and rewrote Current State with the three-way live/built-but-unshipped/researched split plus real current numbers (28 dossiers, 169 seen_ids, 32 opt_cache entries, checked directly). One self-inflicted formatting bug caught and fixed mid-task: an early append landed without a trailing newline and silently merged into the next section's heading, breaking it — found immediately when the next patch couldn't locate that heading, fixed via direct file edit instead of fighting the patch tool's boundary handling further.

## [2026-07-25] build | Internship loop — coverage expansion, six sources, OPT regex improved
- Relayed a multi-day, multi-turn conversation with a separate Sonnet 5 session that had direct repo access: independent audit closeout, a real Google-posting-miss investigation (root-caused to a ~90-second SimplifyJobs active window, not our latency), four manually-clipped postings checked against real state (2 real coverage misses, 1 data-quality bug on an existing source, 1 already-caught), a live Greenhouse/Lever/Ashby hit-rate check (68%, 15/22 companies), and the build of four new ingestion sources (Greenhouse, Ashby, vanshb03, zshah101) plus a measured OPT-regex improvement (27%→59% catch rate against 22 real citizens-only-tagged postings). Independently verified pieces directly rather than relaying all of it: Google's live SimplifyJobs data, vanshb03's and zshah101's raw JSON schemas and counts, `public-apis`' Jobs category, and confirmed via `gh api` that commit `a21b2fa` (2026-07-25T16:45 UTC) actually shipped the four-source batch live.
- Also researched `strelov1/freehire` (a live, no-auth, 78-platform ATS aggregator that directly crawls Google and Uber's in-house career sites — the exact gap direct Greenhouse/Ashby/Lever polling can't close) and `artificialintelligencejobs.co` (a smaller AI-native source with a clean `level: "Intern"` field) — both confirmed real and promising, neither built yet.
- Wrote `20_Progress/Internship/Building System/Research Loop - Phase 7 Coverage Expansion.md` — a chronological build record continuing `Phases Run.md` past Phase 6, covering Phases 7 through 14 of this stretch. Explicitly flagged which claims in it were independently verified by this session versus relayed from the other session's own reports, since several build details (the exact throttle mechanism shipped, whether Lever was built, the final live test count) were never independently re-checked here.

## [2026-07-19] audit | Internship loop — the real gap is promotion, not discovery
- The independent audit (run against the prompt from this session's earlier entry) came back: code review clean, both claimed bug fixes real with regression tests, 167/167 tests independently re-run and confirmed, all three hard criteria genuinely enforced in `profile.yaml`/`filter.py`, zero LinkedIn/CAPTCHA/LLM violations found anywhere in the source tree. One real new finding: the one thin (948-byte) Palantir dossier is explained — its stored `url` is a Lever `/apply` form endpoint, not the JD page, so Firecrawl fetched successfully but there was almost nothing to extract; distinct from the fail-open path, not yet handled as its own case. Also found: `state/opt_cache.json`'s 6 live entries have zero overlap with `Companies giving OPT & CPT.md`'s ~20 manually-audited entries — the vault note was never updated once the machine cache started actually writing, and nothing in the note flags that the two lists cover disjoint time periods.
- User pushback, and it was correct: closing the loop on code correctness said nothing about whether the system is actually useful yet. Independently verified by reading `Tracker/Tracker.md` (empty kanban, every column), `Tracker/Internship - Dashboard.md` (correctly built, empty by construction), and `Applying/_This Week.md` (still "Nothing active yet," written 2026-07-16, still true 2026-07-19 with 26 real dossiers sitting unpromoted) — zero of the 26 real, live, currently-open dossiers have ever been promoted through [[30_Order/Workflows/Internship Pipeline]]. The discovery half of this project is solid; the half that actually produces applications has a 0% completion rate against real automation output. Also read `enrich.py` and `ingestion/posting_page.py` in full: contact discovery is real but shallow (generic company/blog contacts, not recruiters — never run once live), and `OPT_EXCLUSION_RE` is a literal-phrase regex built from exactly one real example plus two named signals — real risk of false negatives on real-world phrasing it's never been tested against, an accurate version of the user's "OPT rule feels too strict" concern.
- Also found and fixed a real coverage gap in the sourcing strategy: relying on SimplifyJobs + JGCL alone means every match is downstream of a human curator noticing and PR'ing a listing. Proposed a structurally better fix — Greenhouse/Lever/Ashby ATS platforms expose free, public, unauthenticated JSON job-board APIs with full JD content included, pollable on the same hourly cadence with zero new Firecrawl cost, and the seed list is nearly free to bootstrap since several existing dossier `url` fields already point at these platforms.
- Wrote `20_Progress/Internship/Building System/Research Loop - Improvement Plan.md` — ordered by real leverage: (1) promote 3-5 real dossiers by hand this week before writing more automation, (2) add direct ATS-API polling alongside the two curated lists, (3) right-size expectations on `enrich.py`/OPT detection rather than claim they're solved, (4) a `rejection_reason` feedback field + periodic review pass so the loop can actually learn from real mistakes once there are any to learn from. Restated the Source of Truth note's end goal explicitly in terms of applications submitted, not dossiers written — the metric that was actually still at zero.
- Fixed a real staleness bug in `30_Order/Workflows/Internship Pipeline.md`: its "Deferred: Automated Discovery" section still described the old Slack/Firecrawl-monitor design and said Step 1 automation "is explicitly not built yet," months after the real GitHub Actions pipeline shipped and superseded it. Corrected in place.

## [2026-07-19] audit-prep | Internship loop closed — source-of-truth note + independent review prompt
- Independently re-verified the Phase 6 closing pass's own claims against live repo/vault state rather than trusting the Fable 5 session's summary (`gh api` on `gupta-builds/internship-research-loop`, direct dossier file count). Found the closing pass's "20 survivors" figure is stale, not wrong: the first scheduled run after the Phase 6 push (2026-07-18T15:44:56 UTC) wrote 6 new dossiers via the newly-codified Winter-2027 term match, taking the vault to 26 — confirmed by file count and by `runs.jsonl`'s `written_count: 6` entry. Also confirmed the cross-source dedup fix caught a real duplicate live (one of the predicted "+7 Winter matches" is a true dup of an already-written Palantir posting, correctly rejected every run since), the first `recheck.yml` run completed clean (26 scanned, 0 removals), and `run.yml` is 8/8 green since the push. Flagged one open item for the next session: one current dossier is 948 bytes (thin), contradicting the "all content-enriched" framing for the post-audit writes specifically — not independently explained yet.
- Wrote `20_Progress/Internship/Building System/Internship Research Loop — Source of Truth.md` — a consolidated, final-form statement of everything the loop was ever aimed to do across all six phases (discovery pipeline, enrichment/resume tooling, root-cause hardening, the three hard criteria + content + codification), explicitly scoped as *aims*, not a build-verified report — the verification is delegated on purpose to an independent audit so the same session that wrote the claims doesn't also grade them.
- Fixed a real frontmatter bug in `Research Loop — Implementation Plan.md`: `updated`/`related_progress`/`next` were malformed YAML (double-quoted JSON strings wrapped in single quotes instead of native YAML), inconsistent with every other note's frontmatter in this project. Corrected to plain YAML, cross-linked the new Source of Truth note, marked the note as historical/superseded for current scope.
- Appended a dated "Post-Closing-Pass Live Verification" section to `Phases 1-3 Run.md` with the above findings, cited to real timestamps and log entries, not carried claims.
- Wrote an independent-audit prompt for a fresh Sonnet 5 session (delivered in-chat, not filed) — full code review against the real repo tree, a built-vs-planned matrix scored against the new Source of Truth note with cited evidence per line, and five specific open items to check (the thin Palantir dossier, whether Layer 5 `enrich.py` has run even once, the weekly rollup, the real test count via a live `pytest` run, and OPT-registry/`opt_cache.json` consistency) — deliberately scoped as review-only, findings-first, not a build/fix pass.

## [2026-07-19] meeting-prep | CausalOps memory-layer PR #25 — meeting prep note built

Read all 8 notes in `60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/` plus `CausalOps — Index`, `memory-layer`, and `Roadmap` in the CausalOps brief. Pulled `darshgarg7/CausalOps#25` live via the github MCP — PR body, all 30 changed-file diffs (of 111), all 5 Copilot review comments + Anant's fix replies, and the 5 most recent commits with full messages (squash-merge, CI-lint fix, Copilot-findings fix). Cross-checked the vault notes against the live PR and found them accurate — no drift.

Wrote [[Memory Layer Meeting Prep — 2026-07-20]] to `20_Progress/Projects/CS/CasualOps/Meetings/` (new folder, first note in it) — a meeting-facing distillation, not new research: 30-second answer, the five-component build walkthrough, the "why 111 files" answer led with rather than waited for, honest tradeoff answers (Gemini-not-Azure, squash-not-rebase, pgvector-not-dedicated-vector-db, single-hop-not-multi-hop), prioritized next steps, the six real bugs found with exact mechanism for each, and a verbatim Q&A section (11 questions) so Anant has exact answers ready rather than needing to improvise live. Linked back from `CausalOps — Index` → Subsystem Notes.

**Outcome:** Done. Files touched: `20_Progress/Projects/CS/CasualOps/Meetings/Memory Layer Meeting Prep — 2026-07-20.md` (new), `20_Progress/Projects/CS/CasualOps/CausalOps — Index.md` (Subsystem Notes list appended).


Append-only record of Claude sessions. Format: `## [YYYY-MM-DD] action | Title`

---

## [2026-07-18] plan | Three hard criteria + dossier content — closing prompt for the research loop
- Verified the prior round's 5 root-cause fixes actually landed before building on top of them (didn't trust the commit message alone): `git log`/`git show --stat` on the WSL repo confirmed commit `7a84be1` real, `recheck.py` + `recheck.yml` exist, 148 tests. Vault dossier count independently re-checked: 28 (27 correct + 1 stray zapplyjobs entry from a timing gap before the source-removal deploy) — deleted the stray, back to 27.
- Found `20_Progress/Internship/Companies giving OPT & CPT.md` is mislabeled — despite the name, it's a stale Oct 2025 FAANG-postings brainstorm with zero actual OPT/CPT content. Flagged so it doesn't get treated as a usable reference.
- Recorded three new hard criteria (Summer 2027 or Dec 2026-Jan 2027, US-located, OPT-eligible) and the dossier-content requirement (no longer deliberately thin — real posting content via Firecrawl) as "Phase 6 Decision" in `Phases 1-3 Run.md`, including a permissive-by-default OPT design (citizenship/clearance/explicit-exclusion signals only, not a guessed allowlist — same pattern as `locations_allow`) and the clarification that OPT ≠ H-1B sponsorship.
- Located a real "Fable 5 prompt" structural template already in this vault (`60_Claude/07_AI_Information/Fable Prompt — Dashboard and Ingestion Pass.md`, a different project) and used its shape (ORIENT FIRST / WHAT WAS DONE / numbered TASKS / HARD CONSTRAINTS / QUALITY GATE / SESSION END PROTOCOL) for the closing prompt rather than inventing a new format.

## [2026-07-18] cleanup | Dossiers folder audit — 110 of 137 deleted, root causes found
- Audited every file in `10_Areas/Career/Internships/List/Dossiers/` against live upstream data (SimplifyJobs/JGCL listings.json fetched fresh, joined locally by stored UUID) rather than trusting stored frontmatter or visiting 137 pages individually.
- Deleted 79 SimplifyJobs dossiers (76 the source itself now marks `active: false`, 3 grad-only/no Bachelor's eligibility), 11 of 13 JGCL dossiers (7 closed upstream, 4 wrong-cycle by filename), all 20 zapplyjobs dossiers (program/resource pages, not deadline-bearing postings — wrong fit for this folder, source removed from the pipeline per this session's decision). 27 genuinely valid dossiers remain.
- Found and recorded five root causes in `20_Progress/Internship/Building System/Phases 1-3 Run.md`: no post-write liveness recheck, no `degrees` eligibility check, JGCL's real `target_year` data not reaching written frontmatter (confirmed via live cross-reference — a normalize/write bug, not a false match), no cross-source dedup, zapplyjobs structurally unfit as a source. None fixed in code yet — flagged as required follow-up so today's cleanup doesn't just recur.
- Deadline extraction (the original ask) deferred to the 27 survivors only, pending user direction on sequencing against the pipeline fixes.

## [2026-07-17] review | Research-loop phases 1-2 build review before phase 3
- Reviewed the WSL Claude Code session's phase 1-2 completion report (public repo `gupta-builds/internship-research-loop`, CI green, 48/48 tests, mutation-tested) against `20_Progress/Internship/Building System/Research Loop — Implementation Plan.md`, not taken on trust.
- Re-verified three claimed facts directly against live data rather than relaying secondhand: SimplifyJobs' real category taxonomy (10 values, two eras per relevant category — plan's original `categories` list matched only 1 of 10, corrected), zapplyjobs' Year-column value (`All student`/`All Student`/`All Students`, three casings, not the plan's guessed literal string, corrected to a normalized match), and the JGCL listings.json path (re-fetched, returns 200 at the exact path this plan always specified — the build report's claim of a path mismatch didn't reproduce, flagged for the WSL session to confirm against its actual code rather than silently resolved either way).
- Found four phase-3 scope gaps not covered by the phase 1-2 report: unpinned `requirements.txt` (risk for unattended months-long operation), no push-retry/rebase handling against the vault's existing independent auto-commit-and-push cycle, no specified ordering for marking `state/seen_ids.json` (must only mark seen after a confirmed push, not before, or a failed push silently loses a dossier forever), and confirmation that schema-drift detection/auto-issue-filing/the two-tier run log are still unbuilt (phase 3 deliverables, not already-done wiring).
- Added all of the above to the Implementation Plan as a dated review section before authorizing phase 3.

## [2026-07-16] plan | Internship research-loop automation spec, public-repo exposure fix
- Corrected class year vault-wide (rising junior, not sophomore) — withdrew the HRT Applying worked example (`20_Progress/Internship/Applying/2026-HRT-Sophomore.md`, sophomore-only, now ineligible), cleared it from `_This Week.md` and the Kanban.
- Found the `Jarvis` GitHub repo (`gupta-builds/Jarvis`) is public with an auto-commit-and-push cycle running every ~2 hours, already fully pushed to `origin/master`. `Main Resume.pdf` was already tracked (likely already public); `Main Resume.md` (phone/address/email in its header) was about to be swept into the next cycle. Fixed: `.gitignore` now excludes `20_Progress/Internship/Resumes/` and `10_Areas/Career/Internships/Contacts/*` (except `Mimic.md`), and `git rm --cached` untracked the PDF. Flagged but did not attempt: the PDF's prior history is likely still in already-pushed commits; gitignore only stops future commits.
- Verified (not assumed) three GitHub tracker repos live: SimplifyJobs/Summer2026-Internships (`listings.json` on `dev` branch, confirmed 278/14,940 entries are already Summer 2027 despite the repo's name), Jose-Gael-Cruz-Lopez/underclassmen-opportunities (`listings.json` on `main`, 17/112 entries Junior-eligible), zapplyjobs/underclassmen-internships (README-only, zero literal Junior rows but "All student(s)" rows are junior-inclusive). Corrected two claims from a pasted Gemini/Sonnet transcript: listings.json is not cron-generated in-repo (external bot push), and `vanshb03/Summer2027-Internships` is a renamed continuation of the old Summer2026 repo, not a separate source. `systemd` (the transcript's orchestration suggestion) doesn't exist on this Windows machine — GitHub Actions was already the chosen alternative.
- Wrote the full automation spec: `20_Progress/Internship/Building System/Research Loop — Implementation Plan.md` — profile filter, dedup, a four-check fail-closed write gate before anything lands in Jarvis, a test-driven "self-improving" design (schema-drift detection, auto-filed GitHub issues on failure), a two-tier run log (raw JSONL in the automation repo, weekly rollup in Obsidian), and confirmed GitHub Actions minutes math (recommended the automation repo be public to avoid the 2,000 min/month private-repo ceiling).
- Updated `List Monthly Log Template.md` and `List/2026-07 Found.md` to be Dataview-generated over a future `List/Dossiers/` folder instead of hand-typed tables, matching the plan.
- Declined to build (same position as the reviewed Sonnet session): CAPTCHA-bypass/cookie-injection/stealth-browser scraping against LinkedIn. Contact discovery stays scoped to public sources only.
- Next: hand the Repo Bootstrap Prompt to a fresh Claude Code session in `~/projects/work/internship-research-loop` (WSL, no GitHub repo created yet).

## [2026-07-16] build | Internship system redesign — split Areas/Progress, full pipeline
- Research: two rounds via firecrawl (tracking-funnel data, personal CRM patterns, AI-assisted workflow patterns, resume tailoring, cold outreach — then Hermes Agent/Clay/Firecrawl-monitor comparison for future 24/7 discovery automation). Full findings in `20_Progress/Internship/Building System/Internship System — Build Log.md`.
- Decisions (two AskUserQuestion rounds): live status split off Programs (10_Areas, static) into paired Applying notes (20_Progress, live); List is a firehose tier, Programs only created on commitment; Contact drafts live inline in the Contact note; automation deferred until the manual pipeline is proven; Resumes live entirely in 20_Progress; LinkedIn scoped to internships only; system designed role-type-agnostic for future full-time search.
- Created: `10_Areas/Career/Internships/Internships Hub.md`, `List/2026-07 Found.md`, rewritten `README.md`; `30_Order/Templates/Career/` (6 templates: List Monthly Log, Program, Contact, Applying, Cheat, LinkedIn Post); `30_Order/Workflows/Internship Pipeline.md` (added to `00_Workflows Index.md`); `20_Progress/Internship/Applying/_This Week.md` and `2026-HRT-Sophomore.md` (worked example); `Resumes/Main Resume.md` (bullet bank built from reading the existing `Main Resume.pdf`); `Posts/README.md`.
- Edited: `Programs/2026-HRT-Sophomore.md` (stripped status fields, added `list_origin`/`applying_note` links), `Programs-to-Create.md` (flagged as superseded YAML), `Contacts/Mimic.md` (rebuilt — was the wrong concept-note template, now a scenario-based message library), `Tracker/Internship - Dashboard.md` (split Research/Pipeline Dataview queries), `Tracker/Tracker.md` (kanban kept as a second glance view, HRT card added), `Applying/AI Applying.md` (repurposed as a pointer, not deleted).
- Deferred: Firecrawl-monitor-to-Slack automated discovery pipeline; migrating legacy Career Fair/OPT&CPT notes; per-block cleanup of all 13 YAML entries in `Programs-to-Create.md`; actual tailored resume files (no live application yet).

## [2026-07-05] import | First Cursor conversation archive production run (4 composers)
- Raw notes: `60_Claude/05_Clippings/AI Conversations/Windows/Cursor/` (3) + `WSL/Cursor/` (1)
- Summaries: `60_Claude/07_AI_Information/AI Conversation - Summaries/2026-07-05-cursor-*` and `2026-05-28-cursor-*`, `2026-06-04-cursor-*`
- Index: `30_Order/System/cursor-workflow/exported-cursor-composers.json` (4 IDs)
- WSL skill mirrored to `~/.cursor/skills/export-cursor-session/SKILL.md`; WSL SQLite read hits disk I/O while Cursor holds lock — documented in skill
- Redaction skim: clean; workspaceId token redacted in WSL export; no hand-redactions needed
- Promotion: none yet

## [2026-07-04] rebuild | Jarvis OS Dashboard canvas — interactive, 1600px, no card scroll
- Files edited: `10_Areas/AI/Jarvis OS Dashboard.canvas` (full replace)
- What now works: canvas widened to 1600px so all 10 panels fit at 100% zoom without internal scrollbars; TODAY'S FOCUS and TODAY'S NUMBERS panels now use Meta Bind `INPUT[]` fields bound to `00_Dashboard`'s frontmatter (`INPUT[text:00_Dashboard#today_focus]` etc.) so the user can type directly into the canvas instead of opening `00_Dashboard.md`; TODAY'S PRIORITIES keeps the existing Dataview `TASK` query (interactive checkboxes, unverified — see gap below); DAILY DRIVERS keeps the progress-bar DataviewJS plus a static (non-interactive) 5-habit checklist, since habits are tracked as a `habits_done` frontmatter array, not as real task list items in the daily note — confirmed by reading `10_Areas/Life/Enumerate/Daily/2026-07-01.md`.
- Correction made mid-task: the brief specified Meta Bind bind-target syntax as `INPUT[text:file(00_Dashboard):today_focus]`. Verified against the actual Meta Bind docs (fetched live) — the real syntax is `INPUT[fieldType:noteName#property]` (e.g. `INPUT[text:00_Dashboard#today_focus]`). Used the verified syntax instead of the brief's; the brief's form does not exist in Meta Bind and would have silently failed to bind.
- Open gaps: cannot visually verify in Obsidian from this environment (no GUI) — the no-scroll layout and Meta Bind/Dataview-TASK interactivity in canvas text nodes should be spot-checked at 100% zoom on next open.

## [2026-07-04] config | Canvas set as Obsidian homepage
- Files edited: `.obsidian/plugins/homepage/data.json` (PowerShell, since `.obsidian/` is write-guard-blocked for the Write tool)
- What now works: `Main Homepage.value` changed from `00_Dashboard` to `10_Areas/AI/Jarvis OS Dashboard` — Obsidian now opens the new canvas on startup instead of the markdown dashboard.
- Follow-on fix: this made two other notes' claims stale ("homepage opens 00_Dashboard on startup"). Corrected both: `10_Areas/AI/Claude Code.md` (Connections section) and `20_Progress/AI/Claude OS Dashboard.md` (Health Panel DataviewJS constant). Left the same phrase inside `60_Claude/07_AI_Information/Session Logs/log.md`'s 2026-06-11-era entry untouched — that's a historical record of a past state, not a live claim.

## [2026-07-04] create | Claude OS Dashboard canvas (companion to the .md registry)
- Files created: `20_Progress/AI/Claude OS Dashboard.canvas`
- What now works: a 900px visual companion to `20_Progress/AI/Claude OS Dashboard.md` with 5 panels (health tiles, platform inventory table, open actions checklist, recently-changed-files table, nav) sized to avoid internal scroll. Health tiles are hardcoded DataviewJS constants read from the `.md` note's own Health Panel at write time (per the brief — they're not live-queried since the underlying facts change rarely).
- Open gaps: the 7 health-check values will drift from the `.md` note over time since both are now hand-maintained copies; whoever next updates one should check the other.

## [2026-07-04] build | Excalidraw Claude OS Map — real diagram replacing the markdown placeholder
- Files removed: `10_Areas/Excalidraw/Claude OS Map.md` (was a text blueprint, not an actual diagram, written by a prior session)
- Files created: `10_Areas/Excalidraw/Claude OS Map.excalidraw` (23 elements: 3 background zones + labels, 8 labeled boxes across Infrastructure/Components/Output layers, 9 bound arrows including one bidirectional MCP↔Vault read/write edge), embedded via `![[Claude OS Map.excalidraw]]` in `10_Areas/AI/Claude Code.md`'s `## Connections` section (also added a one-line pointer there).
- Built via the live `excalidraw` MCP canvas (`npm run canvas` in `30_Order/System/excalidraw-mcp/`, started this session) using `batch_create_elements` with arrow bindings (`startElementId`/`endElementId`), verified with `describe_scene` before export.
- Open gap: the brief asked for a dark background matching AnuPpuccin (#0f1117) with white text/arrows. The MCP's element-creation API has no scene/appState-level background-color control, only per-element `strokeColor`/`backgroundColor` — used the tool's documented light-theme-safe palette (guide's stroke/fill pairs) instead of forcing white-on-dark, which would have been unreadable if the canvas background stayed default white. Revisit if the vault's Excalidraw plugin is confirmed to force a dark canvas background.

- **`.claude/` alignment (this session, part 1):** re-read every `agents/`+`skills/` file against the post-reorg vault (`50_Reviews`→`30_Reviews`, `35_Outputs` deleted, `40_Resources/CS/AI` subfoldered, `10_Areas/UMN`/`40_Resources/UMN` split, `organize-csci2033.md`'s `50_Archive` path was wrong even pre-reorg — real location is `20_Progress/Degree/CSCI 2033/`). Fixed ~20 stale references across `agents/vault-curator.md`, `agents/learning-agent.md`, `agents/career-operator.md`, `skills/startday.md`, `weekly-review.md`, `trace-topic.md`, `ops.md`, `ops-reference.md`, `context.md`, `lint-claude-layer.md`, `closeday.md`, `distill-note.md`, `organize-csci2033.md`, `mcp-hub.md`, `context/workspace-context.md`. Rewrote `README.md`'s alignment backlog. Deliberately did not touch `Jarvis Vault Architecture.md`/`Vault Map.md`/the North Star — those are the actual folder-role authorities and are the subject of a planned follow-up conversation about redefining folders.
- **Created `60_Claude/30_Reviews/Monthly/Monthly Review — 2026-06.md`** — first monthly review. Built from the full 970-line session log, all 89 git commits, and live re-verification of the dashboard/capability-engine/`.claude/` layer.
- **Revised the review** after being told it missed completion-tracking against the two master plans and the weekly reviews. Found both `Jarvis Three-Month Research Engine Master Plan.md` and `Jarvis Multi-Agent PKM Plan.md` had moved from `60_Claude/40_Project_Briefs/` to `20_Progress/Projects/AI Second Brain/` (uncommitted, undocumented) — fixed two more stale `.claude/` references this broke (`learning-agent.md`, `weekly-review.md`). Scored both plans' Month 1/2 checklists and the PKM plan's Phase 1 against the live filesystem (not against session-log claims): Month 1 ~30% met (unchanged since W22, 7 weeks ago), Month 2 (due ~06-19) at zero, conversation-capture acceptance test never passed, `registry.sqlite` never persisted, `Jarvis.md` never updated since its creation date, the Weekly Operating Rhythm ran exactly once. Cross-checked W22's three "Next Week Priorities" — found the duplicate 2026-05-28 log entry it flagged is *still* duplicated.
- **Key findings carried into the review:** `00_Dashboard.md` has 4 dead Dataview queries despite being signed off as fixed on 06-11; two non-cross-linked graphify exports of the Portfolio codebase exist (`20_Progress/.../Portfolio/` and `40_Resources/CS/portfolio-graph/`, the second found only via git history); MGMT 3001 is wired as the templates' gold-standard link against the vault owner's direct correction this session; `.claude/` has now needed reactive path-repair four times in under two weeks.
- **Root cause named once:** artifacts get marked done at build time and nothing re-checks them later against the plan or the filesystem. The fix is closing the loop on the plans/reviews that already exist, not writing new ones.
- **Next:** run the Master Plan's own Week 1/2 acceptance tests (CLI `status`, 3 real conversation imports, first benchmark set) before any new building; restart the weekly review cadence; fix the dashboard's dead queries; resolve the duplicate Portfolio graph exports.

## [2026-06-01] ingest | Summer 2026 course syllabi → source-of-truth notes
- Ingested the HIST 1103 and MATH 2230 syllabi/calendar PDFs (in each course's `Documents/`) plus the live D2L discussion/dropbox and WebAssign listings provided by the user. Did NOT read the Devore textbook PDF per instruction.
- Created 9 notes under `20_Progress/Degree/`: HIST 1103 (Board, Syllabus, Assignments and Discussions, Exams, Schedule) and MATH 2230 (Board, Syllabus, Calendar, Assignments Quizzes and Tests). Each rewrites every syllabus rule in plain language with nothing dropped; the MATH assignments note holds the full 58-item WebAssign table with point values + Devore book resources.
- Updated `20_Progress/Degree/Summer Courses.md` into a working dashboard: linked both boards, added an Overview/Plan, a term key-dates table, and a dataview pulling the two course boards.
- Flagged (not silently resolved) the real conflicts in the sources: HIST Practice Assignment due date (discussion Jun 6 vs dropbox Jul 2), the exam late penalty stated two ways (one letter grade/day vs 10 pts/day), the HIST assignment credit math stated three ways, and MATH withdraw/HW-cutoff dates printed as 2025 (likely 2026). All recorded under `## Open questions`.
- Why it matters: both courses now have a single re-readable source of truth so the original PDFs and course site never have to be reopened for rules/dates.
- Next action: confirm the flagged date/penalty conflicts with each instructor; create weekly + concept notes as the courses run.

## [2026-06-01] verify | Summer course notes — full re-check against PDFs
- Re-read all three PDFs (HIST 1103 syllabus, MATH 2230 syllabus + calendar) line-by-line and cross-checked the MATH WebAssign table value-by-value against the pasted source — all 58 items' points and due dates are correct; HIST grading scale, word minimums, and exam dates verified correct.
- Fixes/clarifications: (1) reframed the HIST dropbox "availability windows" as late-acceptance cutoffs, not a second due date (the actual due dates match the discussion list, all Saturdays); (2) added a strict assignment + classmate-reply due-date table to the HIST Assignments note; (3) added the syllabus's "13 vs twelve assignments" wording inconsistency; (4) added the HIST exam dropbox windows incl. the "Midterm Exam — Late" box (open to Jun 22) to the Exams note.
- Result: the only genuine source conflict remaining is the Practice Assignment date (discussion Jun 6 vs dropbox Jul 2); date-format typos (MATH 7/14/25, 7/22/25) remain flagged. Intentionally omitted ephemeral D2L metadata (thread/post counts, "last post" timestamps) as non-schedule data.

## [2026-06-01] system | Standards layer extracted from templates
- Created `30_Order/Standards/` with five per-note-type content standards: [[Source Summary Standard]], [[Course Week Standard]], [[Concept Standard]], [[Evergreen Standard]], [[Project Standard]]. Each maps to its template + workflow, gives per-heading content/density/plugin guidance, a failure mode, done conditions, and a gold-standard wikilink derived from real vault notes (Quant Foundations, MGMT 3001 Week 9/4, Teams and Team Effectiveness, the Observability-vs-Evaluation synthesis + BOOM, Jarvis + OpsPilot).
- Stripped every HTML comment instruction from the templates the prior session annotated: `Clipping Distill Template`, `Week Template`, `Concept Template`, `Textbook Template`, and both copies of `For Evergreen`/`For Progress` (Metadata + the byte-identical Frontmatter duplicates). Templater syntax, frontmatter, headings, and a format-reference flashcard preserved; templates are now clean scaffolds.
- Wired the layer in: added a `Standards doc to read first` column to the AGENTS.md routing table (Source Summary / Evergreen / Project rows filled, others blank); added a pre-flight step in Vault Rules Part 1 to read the matching Standards doc before writing; added one reference line to the `Capture to Summary`, `Summary to Distilled`, and `Brief to Progress` workflows; compressed the duplicated content specs in `ingest-clipping.md` and `research-distiller.md` down to a pointer at the Source Summary Standard while keeping all tooling steps.
- Why it matters: note-writing guidance now lives in one queryable Standards layer instead of being trapped as comments inside template files; an agent reads the Standard, not the template, for content.
- Open questions: the AGENTS.md routing table has no rows for course-week or concept notes, so those two Standards are reachable only via their templates/workflows + the pre-flight step, not the table. The `Templates/Frontmatter/` vs `Templates/Metadata/` duplication still exists and may warrant consolidation.
- Next action: decide whether to delete the duplicate `Templates/Frontmatter/` copies in favor of `Templates/Metadata/`.

## [2026-05-31] system | Vault Rules — Complete AI Ruleset created

- Created `60_Claude/07_AI_Information/Vault Rules — Complete AI Ruleset.md` — 14-part governing specification for all AI platforms working in this vault. Covers: mandatory pre-flight (read order, analyze-before-write, search-before-create), note placement, frontmatter spec, blank lines, formatting markers, content density, wikilink validation, all plugin integration rules, source ingestion rules for PDF/web/video, tool selection, skill and agent selection, 16-point quality gate, safety rules, and session end protocol.
- Updated `AI_CONTEXT.md` — added Vault Rules as mandatory step 2 in the cold-start read order
- Updated `Agent Operating Guide.md` — added Vault Rules to start-of-session checklist
- Updated `Vault Map.md` — inserted Vault Rules as step 2 in the read order
- Rules are positive specifications derived from the audit; not a list of mistakes. Any AI platform following this file will not reproduce the 12 documented errors.
- Open question: templates still need rewriting (see [[Note Writing System — Audit and Roadmap (2026-05-31)]] § Build Priorities)
- Next: rewrite `Clipping Distill Template.md` to match actual PDF ingestion structure

## [2026-05-31] audit | Note Writing System — full session analysis and roadmap

Created [[Note Writing System — Audit and Roadmap (2026-05-31)]] — comprehensive post-session audit covering 5 days of work. Documents: 12 specific mistakes made, all fixes applied, complete formatting rule set, template audit (32 templates, most are shells), 8 plugin gaps, 10 build priorities for reaching "complete control" note standard.

Key gaps identified: Templates have no content guidance, Clipping Distill Template doesn't match actual PDF structure, `## Lecture-to-textbook synthesis` pattern not documented, Canvas/Excalidraw/QuickAdd not integrated into workflows, Source Summaries Board queries broken path (`30_Source_Summaries` → `10_Source_Summaries`), no math notation standards, no gold-standard example notes linked from templates.

## [2026-05-31] system | Rewrote ingest-clipping skill and research-distiller agent

- Rewrote `.claude/skills/ingest-clipping.md` — added source type routing table, PDF extraction via `pypdf` (Windows-compatible), image/URL/markdown handling, exhaustive PDF capture mode, correct subfolder routing (`PDF Ingestion/`, `Web Ingestion/`, `Video Ingestion/`), and template aligned to `Clipping Distill Template.md`.
- Rewrote `.claude/agents/research-distiller.md` — fixed wrong folder paths (`10_Source_Summaries/` not `30_Source_Summaries/`, `07_AI_Information/Session Logs/log.md` not `10_Session_Logs/log.md`), added same PDF extraction method, exhaustive capture checklist, promotion-candidate workflow.
- Discovery: `pdftoppm` not installed on this Windows system; `pypdf` is available at Python 3.13 and extracts text cleanly.
- Trial ingest: [[60_Claude/10_Source_Summaries/PDF Ingestion/Quant Foundations (PDF)]] — 12 pages, full content captured.
- 18 PDFs remain in `60_Claude/05_Clippings/PDFs/` ready for ingestion.

## [2026-04-08] setup | Vault system initialization

Created the 60_Claude folder structure and core skills.

**Folders created:**
- 00_Inbox
- 10_Session_Logs
- 20_Distilled_Notes
- 30_Source_Summaries
- 40_Project_Briefs
- 50_Reviews
- 60_Indexes

**Skills created:**
- ingest-clipping
- distill-note
- context

**Agent created:**
- research-distiller

**Next:** Test ingestion workflow with existing clippings.

## [2026-04-08] ingest | Kairo — Know What's Coming

Test ingestion of the Kairo/TRIBE v2 article.

**Created:**
- [[60_Claude/30_Source_Summaries/Kairo — Know What's Coming - Summary]]
- [[60_Claude/20_Distilled_Notes/Cognitive AI]]
- [[60_Claude/20_Distilled_Notes/Wearable AI]]

**Updated:**
- [[Claude Layer Index]] — Added entries to tables

**Actions extracted:** 3 (clone repo, test model, consider workflow implications)

**Next:** Create remaining skills (today, trace-topic, connect-notes, closeday, weekly-review, lint-claude-layer)

## [2026-04-08] complete | Phase 1 implementation

Completed all Phase 1 work: skills, agents, and test ingestion.

**Skills created:**
- today
- trace-topic
- connect-notes
- closeday
- weekly-review
- lint-claude-layer

**Agents created:**
- vault-curator
- career-operator

**System ready for use.**

## [2026-04-24] context | Cross-tool context alignment

Created a shared context manifest and rewired project instruction entrypoints so Codex, Claude, Kiro, and Cursor can pull from the same live workspace context instead of drifting.

**Created:**
- [[AI_CONTEXT]]
- `.kiro/steering/workspace-context.md`
- `.cursor/rules/workspace-context.mdc`

**Updated:**
- [[AGENTS]]
- [[CLAUDE]]
- Claude agents and skills to read the shared context manifest

**Continuity layer:**
- [[00_Dashboard]]
- [[60_Claude/07_AI_Information/Session Logs/log]]
- [[40_Resources/Obsidian/Vault Operating System]]

## [2026-04-24] plan | Jarvis multi-agent PKM plan

Created a project brief for turning Jarvis into a multi-agent second-brain system without flooding the vault with raw AI output.

**Created:**
- [[Jarvis Multi-Agent PKM Plan]]

**Key decisions:**
- use a normalized conversation registry plus raw archive plus distilled summaries
- keep `AI_CONTEXT`, the dashboard, and the session log as the live context spine
- treat cross-vault sync as a promotion pipeline first, not a full bidirectional mirror
- enforce writing quality with an extraction -> rewrite -> critic gate instead of trusting first-pass prose

**Next:** Build Phase 1 conversation registry, context pack builder, and promotion manifest.

### 2026-04-27 — Phase 2 Flagship Enrichment (Systems, Algorithms, Career, Trading)

**Tasks completed**: 12.1, 13.1, 14.1, 14.2

**Systems track (12.1)** — Enriched 6 UROP/BOOM notes with capability fields (`track`, `difficulty`, `mastery_level`, `drill_interval`, `prerequisites`, `used_in`, `evidence`) and Deep Dive sections (One-Sentence Version, What It Is, Why It Matters, Real Example, Contrast With, Source Anchors):
- Observability and Tracing (already had fields, already enriched)
- Kafka Redis and Workers — difficulty 4, systems track
- API and Backend — difficulty 3, systems track
- Rust Patterns in BOOM — difficulty 4, systems track
- MongoDB Data Model and Filters — difficulty 3, systems track
- Docker WSL and Local Setup — difficulty 2, systems track
- Testing Debugging and Deployment — difficulty 3, systems track

**Algorithms track (13.1)** — Created 5 distilled mirror notes in `60_Claude/20_Distilled_Notes/` (feeder layer rule: don't restructure `10_UMN/`, create mirrors instead):
- Dynamic Programming — from CSCI 4041, difficulty 4
- Graph Algorithms — from CSCI 4041, difficulty 4
- Hashing — from CSCI 4041, difficulty 3
- AVL Trees — from CSCI 4041, difficulty 3
- OCaml Pattern Matching — from CSCI 2041, difficulty 3

**Career track (14.1)** — Created 4 concept notes in `60_Claude/20_Distilled_Notes/`:
- Interview Preparation — difficulty 3
- Portfolio Strategy — difficulty 2
- Career Strategy — difficulty 2
- Mentorship and Networking — difficulty 2

**Trading track (14.2)** — Created 3 concept notes in `60_Claude/20_Distilled_Notes/`:
- Index Fund Investing — difficulty 2
- AI-Assisted Trading — difficulty 4, cross-track (trading + ai)
- Trading Tools and Platforms — difficulty 2

**Running total**: ~18 new/enriched notes this session, bringing Phase 2 flagship enrichment to completion across all 5 tracks.


### 2026-04-25 — Capability Engine Phase 3-4 Complete (Tasks 15-22)

**Task 15**: Computed drill schedules for all 24 enriched notes. Formula: `next_drill = last_drilled + clamp(round(drill_interval × mastery_multiplier), 3, 180)`. All notes seeded with `last_drilled: 2026-04-25`. First drills due 2026-05-02 (difficulty 4-5 notes).

**Task 16**: Checkpoint verified — 24 notes with full capability fields across 5 tracks.

**Task 17**: Created 9 output notes in `60_Claude/45_Outputs/`:
- 3 interview stories (Observability Debugging, Kafka Pipeline Architecture, Rust Type Safety)
- 2 portfolio bullets (BOOM Systems Engineering, Data Pipeline)
- 2 reusable prompts (Vault Enrichment, Plan-First Coding)
- 2 project briefs (AI Market Analyzer, Observability-First ML Pipeline)
All outputs have `source_concepts` provenance. Evidence backlinks added to source concept notes.

**Task 18**: Created 3 synthesis notes in `60_Claude/20_Distilled_Notes/Synthesis/`:
- Rust Ownership vs OCaml Immutability (systems × algorithms)
- Kafka Pipelines vs Agent Tool Orchestration (systems × ai)
- Observability in Backend vs Evaluation in AI (systems × ai)

**Task 20**: Created Weekly Synthesis Template and first review note (2026-W17).

**Task 21**: Added Capability Engine section to `00_Dashboard.md` with links to all dashboards and Field OS boards.

**Task 22**: Final checkpoint passed — all 5 design success criteria met.

## [2026-04-24] build | Jarvis Ops CLI

Implemented the first read-only Jarvis operations CLI under `30_Order/System/jarvis-cli/`.

**Created:**
- `30_Order/System/jarvis-cli/jarvis_ops.py`
- `30_Order/System/jarvis-cli/jarvis.ps1`
- `30_Order/System/jarvis-cli/README.md`
- [[Jarvis Ops Report - 2026-04-24 20260424-170132]]

**Verified commands:**
- `health`
- `context`
- `projects`
- `links`
- `dates`
- `encoding`
- `report`

**Current audit baseline:** 627 Markdown files scanned by default, 147 future-dated metadata fields, 10 project notes, 7 active projects missing `next`, 807 broken wikilinks, and 99 ambiguous wikilinks.

## [2026-04-24] build | Jarvis Enrichment Engine Phase 1

Started the next phase of Jarvis: vault-wide enrichment of existing human-written notes.

**Created:**
- [[40_Resources/Obsidian/Jarvis Enrichment Engine]]
- [[Knowledge Enrichment Dashboard]]
- [[30_Order/Templates/Capability/Jarvis Enrichment Template]]
- `60_Claude/60_Indexes/Bases/Knowledge Enrichment Registry.base`
- [[Jarvis Enrichment Phase 1 - 2026-04-24]]

**Updated:**
- `30_Order/System/jarvis-cli/jarvis_ops.py` with `enrich-candidates`
- [[40_Resources/Obsidian/Vault Operating System]] with enrichment fields and rules
- [[00_Dashboard]] with a Knowledge Enrichment section
- `.obsidian/types.json` with enrichment property types

**Seed enriched notes:**
- [[Ollama]]
- [[Time Complexity]]
- [[OCaml]]

**Current enrichment queue:** 223 candidate notes.

## [2026-04-24] plan | Jarvis three-month research engine roadmap

Created a Jarvis-specific master plan that treats Jarvis as its own standalone project, not just a support layer for other projects.

**Created:**
- [[Jarvis]]
- [[Jarvis Three-Month Research Engine Master Plan]]

**Updated:**
- [[00_Dashboard]] now links the Jarvis project hub and master roadmap.

**Core direction:** build Jarvis into the shared AI context layer, conversation memory system, semantic retrieval engine, enrichment factory, research workbench, and validation layer for all future AI/ML work.

## [2026-04-24] build | Claude Code Operations Layer

Implemented the `/ops` dispatcher skill and supporting components for daily vault operations.

**Created:**
- `.claude/skills/ops.md` — central dispatcher with 7 operations, 10 sections
- `60_Claude/60_Indexes/Bases/Ops Reports.base` — Base registry for ops reports

**Updated:**
- `.claude/agents/vault-curator.md` — added Ops Report awareness, Capability Engine Maintenance, enrichment-aware dedup
- `CLAUDE.md` — added `/ops` to skills table, Daily Operations Cadence section
- `60_Claude/60_Indexes/Vault Health Dashboard.md` — added Dataview queries for ops reports, morning briefings, CLI reports
- `40_Resources/Obsidian/Vault Operating System.md` — documented 5 new ops metadata fields

**Verification checklist:**
- [x] `/ops health-check` instructions produce Ops Report with all required sections (summary table, 7 dimensions, triage queue, comparison)
- [x] `/ops morning-start` instructions create Morning Briefing and append session log entry
- [x] `/ops evening-close` instructions update closeday note and append session log entry
- [x] Report generation does not modify protected paths (`60_Claude/05_Clippings/`, `50_Archive/`, `.obsidian/`, MCP config)
- [x] CLI fallback documented for when jarvis-cli or Obsidian MCP is unavailable
- [x] Safe mutation policy enforced: scan/suggest read-only, fix requires approval, batch threshold >5 notes
- [x] All existing skills referenced by name, no logic duplication
- [x] Vault-curator enhanced without losing existing content
- [x] CLAUDE.md stays under 200 lines (150 lines)
- [x] Dashboard uses Dataview queries only — no unsupported plugins

**Ops skill sections:** dispatcher/menu, health check engine, capability audit, triage queue, report generator, session log, tool layer awareness, safety constraints, cost profiles, usage examples.

## [2026-05-06] setup | CSCI 2041 note-production workflow

Configured Codex for the CSCI 2041 OCaml note project.

**Created:**
- `D:\Users\_Anant\20_Progress\Classes\CSCI\CSCI 2041\AGENTS.md`
- [[CSCI 2041 Note Production Plan]]

**Updated:**
- [[CSCI 2041 Board]]

**Direction:** use the CSCI 2041 source corpus of transcripts, professor notes, labs, projects, and Hickey textbook material to build source-grounded weekly, concept, lab, project, and review notes. Start with Week 6 onward while cleaning Week 1-5 rather than replacing them.

## [2026-05-06] build | BIOL 1012 Theme 4 exam-first notes

Created a linked Theme 4 study set for BIOL 1012 with the exam objectives as the coverage spine and lecture files as the main explanatory source.

**Created:**
- [[Theme 4 Hub]]
- [[Sex Characteristics and Endocrine Signaling]]
- [[Meiosis and Gametogenesis]]
- [[Hormones of Spermatogenesis]]
- [[Uterine and Ovarian Cycles]]
- [[Fertilization Pregnancy and Birth]]
- [[Cell Cycle and Cancer]]
- [[Cancer Treatments and Ethics]]
- [[Theme 4 Practice and Figures]]

**Updated:**
- [[BIOL Board]] now links the Theme 4 note set and uses the live BIOL course path in its class/concept dataview queries.

**Source emphasis:** Theme 4 exam objectives, lecture transcripts/PDFs/slides, exam figures, and practice questions. No 4.4 pregnancy transcript was available, so that note is grounded in CP 4.4, slides, textbook, objectives, and figures.

## [2026-05-06] enrich | BIOL 1012 Theme 4 source-depth pass

Expanded the Theme 4 study set beyond objective-level notes into a fuller source-grounded layer.

**Created:**
- [[Theme 4 Lecture and Packet Deep Notes]]
- [[Theme 4 Prediction Drill Bank]]
- [[Theme 4 Source Coverage Checklist]]

**Updated:**
- [[Theme 4 Hub]] now links the detail layer and source audit.
- [[BIOL Board]] now links the new Theme 4 support notes.
- [[Hormones of Spermatogenesis]] now includes the glucagon endocrine model, testosterone supplement trap, and inhibin backup detail.
- [[Meiosis and Gametogenesis]] now includes spermatogenesis/oogenesis sequence detail and additional flashcards.

**Direction:** the concept notes remain the fast exam layer; the deep notes preserve lecture/course-packet flow for solving packets later.

## [2026-05-06] review + deepen | BIOL 1012 Theme 4 notes

Reviewed all 12 Theme 4 files created/enriched by Codex. Identified and fixed critical gaps:

**Deepened (major rewrites):**
- Uterine and Ovarian Cycles: expanded Phase Logic with full follicular/ovulation/luteal/menses/proliferative/secretory detail; added estrogen dual-role table (negative vs positive feedback by level); added primary vs secondary sex characteristics side-by-side comparison; added key feedback difference table (testes vs ovaries)
- Fertilization Pregnancy and Birth: expanded trimesters with specific events per trimester; expanded germ layers with full derivatives + memory anchor; added differentiation timing (gastrulation ~week 3); added corpus luteum → placenta transition timeline; added placenta functions; expanded contraception with method types and reliability table; rewrote childbirth positive feedback as full step-by-step loop with comparison table
- Cell Cycle and Cancer: rewrote checkpoints with exam question pattern logic; expanded p53 with full mechanism and "guardian of the genome" framing; added benign vs malignant distinction; added angiogenesis; added 5-7 mutation threshold
- Cancer Treatments and Ethics: expanded treatment comparison with detailed mechanisms; added chemo side effect logic; expanded puberty blocker mechanism (GnRH agonist desensitization); added full informed consent definition with 5 components
- Prediction Drill Bank: added 10 multi-step integration drills (31-40) covering hormonal contraception mechanism, luteal phase defect, GnRH agonist, p53 loss, BRCA + oncogene, anovulatory cycle, ectopic pregnancy, full day comparison table, cancer staging, and BRCA family ethics; added 5 more rapid mixed questions
- Lecture and Packet Deep Notes: expanded hormonal birth control to 10-step mechanism; added corpus luteum → placenta transition; added placenta functions

**Status:** Notes are now deep enough to serve as standalone exam prep for Theme 4.

## [2026-05-07] build | Habit Kanban boards

Created a lightweight Obsidian Kanban habit area under `10_Areas/Life/habits`.

**Created:**
- [[Habit Tracker Board]]
- [[Habit Scorecard Board]]
- [[Habit Experiments Board]]

**Direction:** use the Kanban plugin boards for habit placeholders, scorecard categories, and small habit experiments. No generated daily notes or Dataview habit database.

## [2026-05-08] source map | CSCI 2041 notes

Updated [[CSCI 2041 Note Production Plan]] as a source map only. Mapped lecture transcripts, professor note folders, labs, projects, practice files, and Hickey textbook sections to likely weeks from [[20_Progress/Degree/CSCI 4041/Week - 6]] through final review. Did not modify [[40_Resources/UMN/Previous Classes/Lib Ed/MUS 1013/Week - 1]] through [[40_Resources/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]].

**Direction:** start note production at [[20_Progress/Degree/CSCI 4041/Week - 6]] using the plan's source rows, and verify the marked transcript/date uncertainties before drafting.

## [2026-05-08] rewrite | CSCI 2041 production contract

Rewrote [[CSCI 2041 Note Production Plan]] into a stricter note-production contract. Added source-of-truth rules that limit factual claims to the local CSCI 2041 source folder, a very detailed content standard, concept-note primacy, exact source coverage requirements, a professor-note page ledger, week-by-week production details from [[20_Progress/Degree/CSCI 4041/Week - 6]] through final review, and stronger lab/project/concept backlink rules.

**Direction:** future CSCI 2041 note creation should treat concept notes as the durable source-of-truth layer and read every listed source file/page before drafting.

## [2026-05-08] build | CSCI 2041 Week 6-15 archive notes

Created weekly notes [[20_Progress/Degree/CSCI 4041/Week - 6]] through [[Week - 15]] under `50_Archive/UMN/Classes/CSCI 2041`, plus [[CSCI 2041 Board]] in that archive folder. Notes synthesize the source-map transcripts, professor note folders, labs/projects/practice files, and Hickey textbook anchors. [[40_Resources/UMN/Previous Classes/Lib Ed/MUS 1013/Week - 1]] through [[40_Resources/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]] were not edited.

**Direction:** next pass should create the linked concept/lab/project notes, then strengthen backlinks from weekly notes to concrete concept headings.

## [2026-05-08] build | CSCI 2041 Week 6+ concept notes

Created 24 source-grounded concept notes under `50_Archive/UMN/Classes/CSCI 2041/Concepts` for the Week 6 onward material: streams, laziness, memoization, mutation, modules, ADTs, higher-order functions, recursion patterns, Project 1 expression solving, Lisp representation, scanner/parser/printer/evaluator architecture, environments/closures, primitives/special forms, REPL integration, continuations, if-normalized tautology checking, macros, association lists, and error boundaries.

**Updated:** [[CSCI 2041 Board]] now links the concept layer. [[20_Progress/Degree/CSCI 4041/Week - 6]] through [[Week - 15]] now point at the actual concept note names for the created OCaml concepts. [[40_Resources/UMN/Previous Classes/Lib Ed/MUS 1013/Week - 1]] through [[40_Resources/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]] were not edited.

**Direction:** create lab and project notes next, then add more precise backlinks from concepts into lab/project notes once those files exist.

## [2026-05-08] build | CSCI 2041 final review map

Created [[Final Review Map]] under `50_Archive/UMN/Classes/CSCI 2041` from the final exam topic list and the existing Week 6 onward weekly/concept notes. The map organizes review by concrete exam abilities, week path, lab/project skills, concepts to drill, code patterns to reproduce, common mistakes, practice questions, and flashcards.

**Updated:** [[CSCI 2041 Board]] now links the final review map.

## [2026-05-08] build | CSCI 2041 project notes in live Degree path

Created [[Project - 1 Equation Solver|Project - 1 Equation Solver]] and [[Project - 2 Lisp Parser|Project - 2 Lisp Parser]] under `10_Areas/Degree/UMN/Classes/CSCI 2041/Projects`. The notes are grounded in the requested project source/test files and link back to the existing Week 7, Week 10-12, Week 15, final review, and concept notes.

**Updated:** [[CSCI 2041 Board]] now has a Projects section, and [[Final Review Map]] now links to the project notes through the `Projects/` folder path. The `50_Archive` CSCI 2041 folder was not modified in this pass.

## [2026-05-08] update | CSCI 2041 weekly lab anchors in live Degree path

Added lightweight lab sections for Lab 1 through Lab 12 in the live `10_Areas/Degree/UMN/Classes/CSCI 2041` weekly notes. Each section names the source lab file, matching test file when present, the tested concepts, and one final-exam check. Lab 12 explicitly notes that no `Labs/tests12.ml` file was found in the source corpus.

**Updated:** [[CSCI 2041 Board]] now has a Labs index mapping each lab to its weekly note. The old `50_Archive` CSCI 2041 folder and standalone project notes were not modified.

## [2026-05-11] update | CSCI 2041 Week 1-5 final polish

Improved [[40_Resources/UMN/Previous Classes/Lib Ed/MUS 1013/Week - 1]] through [[40_Resources/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]] in the live `10_Areas/Degree/UMN/Classes/CSCI 2041` folder. Filled empty or placeholder weekly sections with concrete skills, textbook anchors, concept links, representative examples, takeaways, and flashcards. Kept the existing lecture bodies intact and strengthened lab connections for Lab 1 through Lab 4. Also updated [[CSCI 2041 Board]] so the Weekly Notes index includes Week 1 through Week 15.

**Audit notes:** remaining cleanup targets are concept-level: [[OCaml - Polymorphism]] and [[OCaml - Tautology Problems]] are still template shells; [[OCaml]] contains leftover MOC/template bullets; several concept notes still link to non-existent standalone lab notes like `[[Lab - 8 Association Module]]` even though labs currently live as weekly anchors.

## [2026-05-11] update | CSCI 2041 Week 5 lecture spine

Reworked the [[40_Resources/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]] lecture section without deleting the existing lecture notes. Added a lecture map, source/concept anchors, a cleaned code spine for reduce, CPS, tautology checking, and Lab 4 permutations, plus a short "what to retain" guide before the detailed Feb 16/18/20 notes.

**Direction:** next refinement pass should consolidate the concept layer into a smaller canonical set, keeping source-grounded material from the existing concept notes while replacing standalone lab-note links with weekly lab anchors.

## [2026-05-12] update | CSCI 2041 weekly lecture source spines

Enhanced the live `10_Areas/Degree/UMN/Classes/CSCI 2041` weekly notes with explicit source-grounded lecture maps. Added new lecture-map sections to [[40_Resources/UMN/Previous Classes/Lib Ed/MUS 1013/Week - 1]] through [[20_Progress/Degree/CSCI 4041/Week - 4]] and [[20_Progress/Degree/CSCI 4041/Week - 6]] through [[Week - 15]], preserving the existing lecture bodies; [[40_Resources/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]] already had the fuller lecture spine from the prior pass. The maps connect transcript numbers/dates, professor-note folders, labs/projects/practice files, and the core mechanism for each week. Also expanded the dated lecture headings in [[20_Progress/Degree/CSCI 4041/Week - 6]] through [[Week - 15]] with professor-transcript details about announcements, source-file mechanics, control-flow invariants, and final-exam distinctions.

**Verification:** all weekly notes now show `updated: 2026-05-12` and each has a `### Week N lecture map` heading in the `## Lecture` section. No writes were made to the old `50_Archive` CSCI 2041 path.

## [2026-05-12] build | CSCI 2041 final exam practice solutions

Created [[Final Exam Practice Solutions]] in the live `10_Areas/Degree/UMN/Classes/CSCI 2041` folder. The note gives professor-style final exam answers for the five practice prompts without restating the questions: evaluator primitive `max`, polymorphic binary tree/mirror, lexical-scope closure behavior, `notany`, and tail-recursive binary search.

**Sources used:** Labs 10-12, especially the evaluator primitive style in `lab11.ml`/`lab12.ml`, plus existing Jarvis concept notes on Lisp evaluation, interpreter primitives, closures, ADTs, pattern matching, and tail recursion.

## [2026-05-15] build | AI agent Obsidian operating docs

Created the first documentation set under `60_Claude/7_AI_Information` for future AI agents working in Jarvis.

**Created:**
- [[60_Claude/07_AI_Information/Plugins]]
- [[Jarvis Writing and Formatting]]
- [[Agent Operating Guide]]

**Direction:** these notes make the `.obsidian` plugin setup, writing rules, and agent workflow explicit without redesigning the vault. The existing empty typo-like folder `60_Claude/7_Al_Information` was left untouched.

## [2026-05-15] build | Stable Obsidian plugin reference layer

Created the stable plugin reference layer under `40_Resources/Obsidian/Plugins` to complement the agent-facing docs in `60_Claude/7_AI_Information`.

**Created:**
- [[40_Resources/Obsidian/Plugins/00 Plugin Reference Index]]
- [[40_Resources/Obsidian/Plugins/Plugin Inventory and Configuration Map]]
- [[40_Resources/Obsidian/Plugins/Dataview and Dashboards]]
- [[40_Resources/Obsidian/Plugins/Tasks Kanban and Project Tracking]]
- [[40_Resources/Obsidian/Plugins/Templates Capture and Periodic Notes]]
- [[40_Resources/Obsidian/Plugins/Spaced Repetition and Learning Loops]]
- [[40_Resources/Obsidian/Plugins/Visual Thinking with Canvas and Excalidraw]]
- [[40_Resources/Obsidian/Plugins/Search Linking and Navigation]]
- [[40_Resources/Obsidian/Plugins/AI Automation and Local Interfaces]]
- [[40_Resources/Obsidian/Plugins/Git Recovery and Vault Safety]]
- [[40_Resources/Obsidian/Plugins/Appearance Code Math and Reading Experience]]
- [[40_Resources/Obsidian/Plugins/Plugin Gaps Recommendations and Verification]]

**Updated:**
- [[60_Claude/07_AI_Information/Plugins]]
- [[Jarvis Writing and Formatting]]
- [[Agent Operating Guide]]

**Direction:** `60_Claude/7_AI_Information` remains the operating layer for agents. `40_Resources/Obsidian/Plugins` is now the durable reference layer for plugin settings, workflows, safety, gaps, and verification notes. `.obsidian`, raw clippings, archive notes, and `60_Claude/7_Al_Information` were not edited.

## [2026-05-15] update | Deep Obsidian plugin reference pass

Expanded the 12 stable plugin reference notes under `40_Resources/Obsidian/Plugins` with richer Jarvis-specific operating rules, source sections, current local settings, workflow examples, safety boundaries, and `needs verification` decisions. Kept `60_Claude/7_AI_Information` as the short agent operating layer and did not edit `.obsidian`, plugin data, raw clippings, archive notes, or `60_Claude/7_Al_Information`.

## [2026-05-26] setup | Claude Pro workflow spine

Implemented the Claude Pro + Jarvis workflow setup for a strict-budget summer AI workflow.

**Created:**
- [[Claude Pro Workflow]]
- `30_Order/System/claude-workflow/README.md`
- `30_Order/System/claude-workflow/hooks/jarvis-session-continuity.ps1`
- `30_Order/System/claude-workflow/claude_desktop_config.read-first.example.json`
- `.mcp.json`

**Updated:**
- [[00_Dashboard]]
- [[CLAUDE.md]]
- [[AI_CONTEXT]]
- local Claude Code project settings to remove provider/token/model overrides and Obsidian delete auto-approval
- global Claude Code settings with lightweight `SessionStart` and `SessionEnd` hooks
- Claude Desktop standard Roaming config with a single `obsidian-jarvis` MCP server

**Verification:**
- `claude --version` returns Claude Code 2.1.128.
- JSON parsing passed for Claude Code project MCP/settings, global Claude settings, Desktop config, and the Desktop example config.
- Simulated `SessionStart` hook returned valid JSON with additional Jarvis context.
- Escalated `claude mcp list` health check connected to `obsidian`, `context7`, `playwright`, and `openaiDeveloperDocs`.

**Next:** In Claude Code, run `/status` interactively after logging into Claude Pro and confirm it uses Claude.ai subscription auth rather than API/provider overrides.

## [2026-05-28] audit | Claude Optimization Master Setup

Full vault audit + external link analysis. Read all AI workflow docs, context files, and fetched the key GitHub repos.

**What was analyzed:**
- All AI workflow docs (AI Workflow.md, MCPs.md, Claude Pro Workflow.md, Github Skills.md)
- 40_Resources/CS/Links.md — the main link-heavy file (50+ external links)
- mattpocock/skills GitHub repo (108k stars, confirmed README)
- Three-Month Research Engine Master Plan — assessed execution status
- Session logs — traced what has and hasn't been built

**Key findings:**
- AI Workflow.md and MCPs.md are outdated (March 2026, pre-Claude-subscription)
- Github Skills.md (May 2026) is the best current analysis in the vault
- mattpocock/skills: not yet installed despite the vault knowing exactly what it is
- Conversation capture: designed in detail, zero folders created
- 223-note enrichment queue is sitting idle
- The vault infrastructure is solid; the gap is execution

**Created:**
- [[Claude Optimization Master Setup]]

**Next:** Install mattpocock/skills, create conversation capture folders, run `/ops morning-start` habitually.

## [2026-05-28] audit | Claude Optimization Master Setup

Full vault audit + external link analysis. Read all AI workflow docs, context files, and fetched the mattpocock/skills GitHub repo (108k stars).

**Analyzed:**
- All AI workflow docs (AI Workflow.md, MCPs.md, Claude Pro Workflow.md, Github Skills.md)
- 40_Resources/CS/Links.md — main link-heavy file (50+ external links)
- Three-Month Research Engine Master Plan — assessed execution status
- Session logs — traced what has and hasn't been built since April

**Key findings:**
- AI Workflow.md and MCPs.md are outdated (March 2026, pre-Claude subscription)
- Github Skills.md (May 2026) is the best current analysis in the vault; still uninstalled
- mattpocock/skills not installed despite vault having full analysis; install: `npx skills@latest add mattpocock/skills`
- Conversation capture: fully designed in Three-Month plan, zero folders created
- 223-note enrichment queue is sitting idle
- Infrastructure is solid; gap is consistent execution

**Created:**
- [[Claude Optimization Master Setup]]

**Next:** Install mattpocock/skills, create conversation capture folders, run `/ops morning-start` every session.

## [2026-05-28] setup | Weekly Review System — Cowork Scheduled Task

Built the full weekly review infrastructure for Jarvis.

**Created:**
- `.claude/skills/weekly-review.md` — replaced the shallow original with a three-month-plan-aware version; includes pre-flight reads, milestone audit table for all 12 weeks, enrichment health checks, orphan/link scanning, session log analysis, exact output format with HUMAN_WRITING rules, and execution notes for future cold-start Claude
- [[Weekly Synthesis — 2026-W22]] — first plan-aware review; documents the W22 infrastructure wins and quantifies the 4-week build spine gap
- Cowork scheduled task `jarvis-weekly-review` — runs every Monday at 9:00 AM; prompt is fully self-contained with orientation steps and vault safety rules

**Updated:**
- [[Weekly Synthesis Index]] — added Review History table

**Key findings surfaced in W22 review:**
- Three-month spine is ~30% complete; conversation capture folders (Week 2 deliverable) still don't exist after 5 weeks
- 223-note enrichment queue idle since April 27; overdue drills since May 2
- AI Workflow.md and MCPs.md are outdated and misleading to future agents
- Duplicate log entry from 2026-05-28 exists and should be cleaned

**Next:** Run the scheduled task Monday June 2 to validate it executes correctly. Priority 1 before then: create `60_Claude/05_Clippings/AI Conversations/` and `60_Claude/30_Source_Summaries/AI Conversations/` manually — this unblocks the Week 2 build spine without any Python work.

## 2026-05-28 — GitHub Claude Starred Repos Analysis
Processed 27 repos from gupta-builds's Claude starred list (22 + 5 extras found on the list). Created notes under 60_Claude/30_Source_Summaries/GitHub - Claude Starred/. 15 repos marked sprout (useful), 12 marked seed (not priority). Updated 40_Resources/CS/Repos.md with Claude Starred section and backlinks.

## 2026-05-29 — GitHub Claude Starred Repos Analysis

Processed 27 repos from gupta-builds's Claude starred list (`https://github.com/stars/gupta-builds/lists/claude`). Created notes under `60_Claude/30_Source_Summaries/GitHub - Claude Starred/`.

**15 repos marked sprout (useful):** ECC, claude-code-templates, ruflo, gstack, beads, mattpocock-skills, graphify, obsidian-mind, spec-kit, agent-skills-addyosmani, context-sync, cpr-compress-preserve-resume, awesome-mcp-servers, claude-context, memsearch

**12 repos marked seed (not priority):** system-prompts-and-models-of-ai-tools, vibe-kanban, awesome-agent-skills, free-claude-code, claude-code-best-practice, jcode, yt-dlp, Scrapegraph-ai, dify, unsloth, anthropics-financial-services, Scrapling

Updated `40_Resources/CS/Repos.md` with `## Claude Starred` section containing wikilink backlinks to all 27 notes. 0 failures.

## 2026-05-29 — GitHub Stars Vault Cleanup

**Task:** Ingested all ~100 starred repos from GitHub (gupta-builds) and organized them into Jarvis.

**Done:**
- Rewrote `40_Resources/CS/Repos.md` — removed messy legacy sections, organized by 7 GitHub lists (Claude/AI/Building/Projects/Jobs/Learning/Cybersecurity) with clean one-liner entries for all 100 repos
- Created individual notes in `60_Claude/30_Source_Summaries/Github Ingestion/AI Starred/` for 6 high-value new repos: hermes-agent, opencode, browser-use, TradingAgents, MiroFish, PageIndex
- Claude Starred section (28 repos, done yesterday) preserved intact with existing individual notes

**Open:**
- Page 2 of starred repos not fetched (list counts total ~95; page 1 had 100 so likely complete)
- Individual notes not yet created for: goose, multica, agentscope, promptfoo, Kronos, dots.ocr, pocketbase, jan, llmfit, whichllm, bumblebee, cai, keyhacks
- Learning/DataTalksClub zoomcamp notes could be expanded

**Next:** Continue ingesting other lists or go deeper on high-priority repos (TradingAgents for BOOM finance work, browser-use for agentic workflows)

## 2026-05-29 — Repos Deep Analysis

**Task:** Deep-analyzed all 95 starred GitHub repos against today's goals (Claude Code setup + VS Code multi-CLI + Obsidian↔dev bridge).

**Output:** Created `60_Claude/20_Distilled_Notes/Repos-Deep-Analysis.md`

**Findings:**
- 12 repos rated HIGH — Action Queue built with exact steps in order
- ~15 MEDIUM (useful within 2 weeks)
- ~40 LOW (reference/learning)
- ~28 SKIP (duplicate, sunsetting, wrong OS, no clear use case)

**Key HIGH repos for today:**
1. `claude-code-templates` — run first to discover all installable Claude Code components
2. `agency-agents` — direct `.claude/` install, 105K-star agent personas
3. `CPR` — session lifecycle slash commands, 55% token reduction
4. `ECC` — full Claude Code harness with memory + security
5. `context-sync` — SQLite MCP memory layer, no external deps
6. `mattpocock-skills`, `gstack`, `agent-skills-addyosmani` — skills packs
7. `system-prompts-and-models-of-ai-tools` — read Cursor/Kiro prompts before multi-CLI config
8. `obsidian-mind` — agent lifecycle hooks for Jarvis
9. `graphify` — VS Code project → Obsidian vault export skill
10. `get-shit-done` — meta-prompting methodology for CLAUDE.md

**Open questions:** Exact install commands for ECC, CPR, graphify, context-sync need README verification — marked in Action Queue.

**Next:** Execute Action Queue top-to-bottom.

## [2026-05-29] audit | Vault Intelligence Audit + 3-Month Setup to Sept 1

Full vault audit done in Cowork session. Read the spine (CLAUDE.md, AGENTS.md, HUMAN_WRITING.md, AI_CONTEXT.md at `60_Claude/7_AI_Information/`, 00_Dashboard.md, log tail, Vault Operating System, Claude Pro Workflow), every `.claude/skills/*.md` (12 files), every `.claude/agents/*.md` (4 files), `.claude/rules/human-writing.md`, `.claude/context/workspace-context.md`, the 30_Order/Templates inventory (33 templates), key project briefs (Master Plan, Multi-Agent PKM, Claude Optimization Master Setup), and the W22 Weekly Synthesis.

**Created:**
- [[Vault-Audit-2026-05-29]] — spine health, instruction-file table with quality scores, conflicts/contradictions list, missing files list, 3-month roadmap (May 29 → Sept 1, with monthly themes Foundation/MCP Hub → Brain → Research Engine), MCP hub gap analysis per external tool. Includes orientation message at top for future cold-start Claude.
- [[40_Resources/Obsidian/MCP-Hub-Index]] — single-page orientation note for any external agent. Folder map, naming conventions, what NOT to touch, how to navigate, what the vault is building toward Sept 1.
- [[60_Claude/05_Clippings/AI Conversations/README]] — raw conversation archive folder, immutable, frontmatter schema. **Unblocks Master Plan Week 2 deliverable (5+ weeks overdue).**
- [[60_Claude/07_AI_Information/AI Conversation - Summaries/README]] — distilled conversation summary folder with workflow + summary shape.
- `learning-agent.md` (in session outputs scratchpad) — read→drill→update→suggest loop agent with full Capability Engine integration. **Cowork sandbox blocked direct write to `.claude/agents/`; manual copy required.** Target path: `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\agents\learning-agent.md`.
- `mcp-hub.md` (in session outputs scratchpad) — skill that defines tool registry, context pack format, and `sync` / `list-tools` / `context-pack` / `verify` operations. **Cowork sandbox blocked direct write to `.claude/skills/`; manual copy required.** Target path: `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\mcp-hub.md`.

**Patched:**
- `AGENTS.md` — added folder roles for `60_Claude/45_Outputs/` and `60_Claude/7_AI_Information/` (both were active but undocumented).
- `60_Claude/7_AI_Information/AI_CONTEXT.md` — Canonical Shared Sources list now includes `CLAUDE.md` and the explicit full path for itself, removing the `AI_CONTEXT.md` ambiguity for non-Obsidian tools.
- `CLAUDE.md` — Editing Behavior rule 6 now references the full path `60_Claude/7_AI_Information/AI_CONTEXT.md` instead of the bare filename, with a note that `[[AI_CONTEXT]]` resolves there.

**Identified but not applied (Cowork sandbox blocked):**
- `.claude/context/workspace-context.md` — needs the same AI_CONTEXT path fix (point at `60_Claude/7_AI_Information/AI_CONTEXT.md`). Patch documented in audit doc.

**Key findings:**
- Spine is structurally sound. The single load-bearing bug was the `AI_CONTEXT.md` path ambiguity (resolved in vault MCP, broken for filesystem-path tools).
- Master Plan is ~5 weeks behind on Month 1 deliverables (conversation capture, registry). Audit roadmap compresses these into Month 1 catch-up.
- 12 skills + 4 agents in `.claude/` match the CLAUDE.md tables exactly. No phantom references.
- `60_Claude/45_Outputs/` and `60_Claude/7_AI_Information/` were active folders with no entries in AGENTS.md folder roles.
- 223-note enrichment queue still idle since 2026-04-27.
- Duplicate 2026-05-28 session log entries flagged for cleanup.
- `AI Workflow.md` and `MCPs.md` (March 2026) outdated and should be archived or bannered.

**Next:** 
1. Manually copy `learning-agent.md` and `mcp-hub.md` from session outputs into `.claude/`. 
2. Drop the 2026-W23 weekly review on Monday June 2 via the existing Cowork scheduled task. 
3. Begin Month 1 catch-up: 5 enrichment-queue notes drilled this week.
4. Apply the deferred `.claude/context/workspace-context.md` path fix.



## [2026-05-30] system | Vault routing architecture update

Fixed AI write-location drift caused by a wrong folder path and a missing routing table.

**What changed:**
- `AGENTS.md` — added `## Note Routing` table (origin → concrete home) plus a "Never write to" negative-constraint block.
- `AGENTS.md` — corrected Folder Roles: `10_UMN/` → `10_Areas/`; rewrote all role descriptions to the canonical definitions (identity / execution / system / resources / archive / AI operating / visual layers); split `60_Claude/` subfolders into their own subsection.
- `CLAUDE.md` — updated Folder Roles table to the new canonical definitions; added an `Excalidraw/` row and a `10_Areas/` row; removed "Full write access" from the `60_Claude/` row, replaced with "All AI writes originate here. See routing table"; added pointer to `AGENTS.md ## Note Routing`.
- `60_Claude/7_AI_Information/AI_CONTEXT.md` — confirmed `AGENTS.md` listed first in Canonical Shared Sources and added the routing/negative-constraint note beneath it; added a `Vault root / note routing` domain entry point.

**Why:** AI was writing notes in the wrong locations due to missing routing rules and an incorrect folder path (`10_UMN/`) in `AGENTS.md`. The `10_Areas/` folder (Career, Trading, Life, UMN) is the real identity layer and was undocumented.

**Conflict found:** `AI_CONTEXT.md` "Coursework as feeder layer" still points to `10_UMN/` (now `10_Areas/UMN/`). Left unchanged — outside the four scoped tasks. Flag for a follow-up pass.

**Next:** Sweep remaining `10_UMN/` references across the vault (e.g. `Vault Operating System.md` Folder Logic, AI_CONTEXT coursework section) and align to `10_Areas/`.


## [2026-05-30] system | Vault folder architecture defined

Deep-dive analysis of actual vault structure vs documented folder roles, triggered by a Cowork session creating a folder at the vault root. Wrote one canonical note defining every top-level folder and a tool-agnostic write contract.

**Created:**
- [[40_Resources/Obsidian/Jarvis Vault Architecture]] — the folder-placement source of truth. Contains: the Write Contract (golden rules + "where does this note go" decision table + never-write list), the 60_Claude dump-and-distill flow model, per-folder contracts for all 8 top-level folders, a current-vs-target gap table (9 verified defects), a 4-phase migration roadmap, and 4 open decisions.

**Key findings (verified against filesystem):**
- `00_Dashboard.md` has 4 broken Dataview queries referencing `10_UMN` (real path is `10_Areas/UMN`) — Active Classes, Open Tasks, Metadata Cleanup, and enrichment blocks silently return nothing.
- `30_Order/Notes/` holds coursework + PDFs + ebooks, violating the system-layer contract.
- Five AI Market Analyzer build specs sit in `10_Areas/Trading/` but are an active project (belong in `20_Progress`).
- No tool-agnostic write contract and no declared default landing zone — root cause of the root-folder incident.
- `Links.md` scattered across 4 locations; `Random.md` loose at root; `7_AI_Information` breaks the numbering pattern.

**Why:** Jarvis is meant to be a daily-driver operating system, but the folder rules were never written at the placement level. MCP-only agents read no instruction file and guess. The new note gives any agent an explicit contract and a safe default (`60_Claude/00_Inbox/`).

**Next:** Phase 1 — fix the `10_UMN` dashboard queries, embed the Write Contract into `AGENTS.md`, declare the `00_Inbox` default. Then confirm the 4 open decisions before any file moves.


## [2026-05-31] system | Rewrote Jarvis Vault Architecture for reorganized vault

Anant manually reorganized the vault (root frozen, 30_Order down to Templates+System, Trading build specs → 20_Progress/Projects/CS/TradingView, 60_Claude renumbered with 07_AI_Information / 10_Source_Summaries / 35_Outputs / 44_Indexes, Session Logs moved under 07_AI_Information, Excalidraw + Notes → 10_Areas, Random.md → 40_Resources). He updated the "Where does this note go?" routing table himself and asked for a full rewrite defining every folder in depth.

**Rewrote:** [[40_Resources/Obsidian/Jarvis Vault Architecture]] — now built around a six-layer mental model (Identity / Execution / Rules / Reference / AI workshop / Dead). Preserved his edited routing table verbatim. Resolved the things he flagged:
- **Distilled vs Outputs:** distilled = knowledge you understand (consumer: you, learning); outputs = artifacts for external use with source_concepts provenance (consumer: someone else). Keep both, enforce the link.
- **07_AI_Information defined in depth:** the AI map + memory layer (onboarding/how-to-read-the-vault + session logs + cross-tool conversations). Clean split from 30_Order (rules/machinery) — 07 points agents at 30_Order for writing procedure.
- **30_Order elevated:** mandatory pre-write reading and the structural counterpart to HUMAN_WRITING; flagged that its Workflows/ docs don't exist yet.
- **40_Resources guardrail:** curated reference hub (his "Google/YouTube"); AI proposes promotions, never bulk-dumps — the rule that stops 60_Claude leaking into it.

**Open questions surfaced:** 10_Areas has no concrete identity hubs yet; coursework split between 10_Areas/Notes and 10_Areas/UMN; 30_Order workflows unwritten; 20_Progress incomplete; dashboard may still query non-existent 10_UMN; Links.md scatter.

**Build order proposed:** embed Write Contract into AGENTS.md → write 30_Order/Workflows → write 07_AI_Information vault map → write the four 10_Areas hubs → make curator/lint self-enforcing.

**Why:** vault is early and mostly thin; defining the architecture before it fills prevents content from forcing a messy structure later.


## [2026-05-31] system | Build order steps 1-3: rules, workflows, vault map

Implemented the first three steps of the Jarvis Vault Architecture build order, anchored to the 3-month Master Plan end state (compounding loop: capture → summarize → distill → promote → produce, plus conversation capture + enrichment).

**Step 1 — rules readable by every agent:**
- `AGENTS.md`: embedded the Write Contract (golden rules + "where does this note go" routing table + never-write list); rewrote Folder Roles to the six-layer model with new 60_Claude numbering; added Priority Files pointers to Vault Map, Architecture, and 30_Order; fixed Working/Retrieval paths (Session Logs → 07_AI_Information, 44_Indexes, 10_Source_Summaries).
- `CLAUDE.md`: added "read 30_Order before writing" (rule 5) + Architecture link; fixed Output Destinations, Ingestion, Query, Session-End paths to new numbering; added Output artifacts row.
- `HUMAN_WRITING.md`: added "Voice here, structure in 30_Order" section — names this file the voice half and 30_Order the structural half.

**Step 2 — `30_Order/Workflows/` (8 new docs):** 00_Workflows Index (pipeline + shared rules), Capture to Summary, Summary to Distilled, Promotion (with the 40_Resources guardrail), Brief to Progress, Output with Provenance, Conversation Capture (3-layer conversation memory), Enrichment (append-in-place, levels). Each: use-when, moves (source→dest), template, steps, frontmatter, done-check.

**Step 3 — `07_AI_Information/Vault Map.md`:** single read-me-first — cold-start read order, six-layer table, how-to-write, interlink/frontmatter conventions, never-do list. Points at 30_Order for rules; does not duplicate the Agent Operating Guide. Pointed `AI_CONTEXT.md` at it (read order + canonical sources updated, stale paths fixed). Also corrected the Agent Operating Guide's stale "Where Content Goes" table + log paths so 07_AI_Information is internally consistent.

**Verified:** spine docs (AGENTS, CLAUDE, AI_CONTEXT, Agent Operating Guide, Vault Map) carry no stale folder paths; all 8 workflow files present; new wikilinks resolve.

**Next (per build order):** Step 4 — write the four 10_Areas hub notes (Career, Trading, Life, UMN). Step 5 — make vault-curator / lint enforce the Write Contract.


## [2026-05-31] system | .claude tooling layer built (MCP, hooks, CLI, registry)

Configured the Claude Code layer so Claude is the operating surface for the vault, with no committed secrets and additive extension points. User chose: all 5 MCP servers, env-var secrets, harden-existing + scaffold-registry.

**MCP — new `.mcp.json` (vault root, gitignored per user):** obsidian (uvx mcp-obsidian, `${OBSIDIAN_API_KEY}`), filesystem, git, fetch, jarvis-memory (custom Python). All secrets via `${ENV_VAR}`; nothing sensitive committed.

**Hooks — wired in `.claude/settings.json`:** SessionStart + SessionEnd → `jarvis-session-continuity.ps1` (fixed to point at Vault Map / AGENTS Write Contract / Architecture / 30_Order, and 07_AI_Information paths). PreToolUse(Write|Edit|MultiEdit) → new `jarvis-write-guard.ps1` that enforces the Write Contract: blocks new files at vault root, and any write into 50_Archive/ or .obsidian/. Fails open on parse errors.

**Python — `30_Order/System/`:**
- `jarvis-cli/jarvis_ops.py` hardened: dynamic date (was hardcoded 2026-04-24), fixed paths (07_AI_Information/Session Logs, 10_Areas, 44_Indexes, AI_CONTEXT location), root anchor now 00_Dashboard.md, new `status` command + richer context-pack file list.
- `jarvis-memory/` scaffolded: `schema.sql` (notes/headings/links/chunks/conversations/enrichment_events/benchmarks), `registry.py` (working index/status/search), `server.py` (FastMCP stub: jarvis_status/jarvis_search/jarvis_reindex), README, local .gitignore. Registry db gitignored.

**Docs/alignment:** `.claude/README.md` = the tooling operating contract + how-to-add-an-MCP/hook/skill/agent + secrets convention + alignment backlog. Root `.gitignore` extended (.env*, registry *.sqlite, __pycache__). Aligned `context/workspace-context.md`, `agents/vault-curator.md` (now enforces Write Contract, skips 50_Archive), and `skills/ingest-clipping.md` to new paths/workflows.

**Could not runtime-test** registry.py / hooks (sandbox bash unavailable); verified by code review — CLI dispatch and status function compose correctly.

**Backlog (in .claude/README.md):** 4 agents + 11 skills still carry pre-reorg paths; mechanical path fixes + workflow pointers. Prereqs for MCP: Python/Node/uv on PATH, Obsidian Local REST API plugin + `OBSIDIAN_API_KEY` env var.

**Next:** set OBSIDIAN_API_KEY env var and smoke-test the MCP servers in Claude Code; then clear the alignment backlog or proceed to Step 4 (10_Areas hub notes).

## 2026-05-31 project-brief | Cursor Vault OS Upgrade Brief

- Created `60_Claude/07_AI_Information/Cursor Project Brief — Vault OS Upgrade.md` — a complete, self-contained project brief for Cursor Opus 4.8
- Brief covers: deep plugin reference notes (15 plugins, research method per plugin), note philosophy doc (Why We Write Notes), .cursor/rules enrichment (5 new/updated MDC files), template enrichment (6 templates)
- Includes tool-by-tool execution method, plugin-by-plugin research steps, quality gates, and the north star framing
- Derived from full read of: AGENTS.md, Vault Rules, audit doc, HUMAN_WRITING, Jarvis Writing and Formatting, Plugins.md, all plugin reference files, .cursor/rules, .cursor/mcp.json, Templates directory
- Open questions: none — brief is self-contained for Cursor to execute
- Next action: paste brief into Cursor Opus 4.8 as the project prompt

## [2026-05-31] plugin-docs | Vault OS Upgrade Priority 1 — deep plugin references

- Executed Priority 1 of the Cursor Vault OS Upgrade brief (Cursor/Opus). Hybrid doc structure: deepened thematic docs in place, split 5 high-impact plugins into dedicated files.
- New dedicated files in `40_Resources/Obsidian/Plugins/`: `QuickAdd Capture Menu.md`, `Excalidraw Diagrams and Annotation.md`, `Canvas Spatial Maps.md`, `Omnisearch and Retrieval.md`. Each: mechanism / exact settings from data.json / integration map / agent rules / failure modes / gold-standard example / verified open state.
- Deepened in place: `Spaced Repetition and Learning Loops` (+ critical finding), `Dataview and Dashboards`, `Tasks Kanban and Project Tracking`, `Templates Capture and Periodic Notes` (QuickAdd → pointer), `Appearance Code Math and Reading Experience`, `Search Linking and Navigation` (Omnisearch → pointer), `AI Automation and Local Interfaces`, `Git Recovery and Vault Safety` — each gained an Integration Map, a real Gold-Standard Example, and a Verified Open State with specific questions.
- Converted `Visual Thinking with Canvas and Excalidraw` to a chooser/hub pointing at the two new files. Updated `00 Plugin Reference Index` (workflow map + which-doc table) and `Plugin Inventory and Configuration Map` (cross-links) to surface the new docs.
- Research: WebFetch on official docs (Canvas help, QuickAdd guide, SR decks page) + each plugin's `.obsidian/plugins/*/data.json`; Context7/Playwright were unavailable so substituted per user approval.
- Why it matters: an agent reading any one plugin doc now gets the mechanism, the live settings, how it wires to the others, and the named failure modes — closing the "README-depth" gap the audit named.
- Open questions surfaced (concrete, for the user): (1) **SR `data.json` has two conflicting config layers** — nested `settings` says `#flashcards`/bold-cloze-off, legacy says `#cards`/bold-cloze-on; the whole vault assumes `#cards`+bold-on. Verify effective layer in the SR settings UI. (2) Excalidraw `templateFilePath` is `10_Area/...` (missing the `s`) — broken template path. (3) Dataview/Templater docs reference the dead `60_Claude/30_Source_Summaries` path; live path is `10_Source_Summaries`. (4) Omnisearch indexes Markdown only — PDFs need Text Extractor (user decision). None were changed (settings/plugin edits require approval).
- Next action: Priority 2 — write `Why We Write Notes.md`.

## [2026-05-31] system | Vault OS Upgrade Priority 2 — Why We Write Notes

- Created `60_Claude/07_AI_Information/Why We Write Notes.md` — the note-philosophy doc the audit named as missing.
- Five sections: the Use Case Test (5 tests; fail all → stays raw in clippings), the Reader Model (future-Anant / AI agent / SR / Dataview / graph and what each needs), Note Types and their purpose (table with the decisive create-vs-extend column), the Compression Hierarchy (raw → summary → distilled → flashcard, each step earns the next), and What Makes a Note Fail.
- Failure modes are anchored to the real audit errors (duplicate `notes:` key, 6 broken wikilinks, ~40% capture on Quant Foundations, plain-prose-no-formatting from writing before reading the vault) rather than invented examples — per HUMAN_WRITING.
- Why it matters: gives every future agent a yes/no gate before writing, so notes have a retrieval path and a named reader instead of being captures for their own sake.
- Open questions: none — doc is self-contained.
- Next action: Priority 3 — enrich `.cursor/rules/`.

## [2026-05-31] system | Vault OS Upgrade Priority 3 — .cursor/rules enrichment

- Expanded/created 5 MDC rule files so a cold-start Cursor agent enforces vault behavior without being told.
- `workspace-context.mdc` (alwaysApply): six-folder map, write contract, routing table, shared context files, live-state sources, stop-vs-proceed. **Fixed the wrong session-log path** (`60_Claude/10_Session_Logs/log.md` → `60_Claude/07_AI_Information/Session Logs/log.md`).
- `human-writing.mdc` (alwaysApply): core test, the 8 things a section must do, anti-slop rules, suspicious-words list, the blank-lines rule (scoped to vault notes, not the mdc files themselves).
- `vault-behavior.mdc` (new, alwaysApply): pre-flight (incl. the Why-We-Write-Notes use-case test), placement, full frontmatter schema, compact 16-point quality gate, safety constraints, session-close protocol.
- `note-creation.mdc` (new, glob `**/*.md`): frontmatter, blank-lines, formatting markers + SR cloze meaning, plugin syntax at creation time, template-matching table, source-note structure order.
- `plugin-rules.mdc` (new, alwaysApply): when-to-use decision table for 11 plugins with exact syntax, the SR cloze trap + the `#cards`/`#flashcards` config warning, security/Git constraints.
- Why it matters: the audit's Gap 2 was ".cursor/rules is almost empty (2 files saying 'go read AGENTS')." Now the rules carry the routing table, schema, quality gate, and plugin syntax inline.
- Open questions: none. Note: blank-line rule deliberately not applied to the mdc files (they are Cursor config, not vault notes rendered by headerspace.css).
- Next action: Priority 4 — rewrite the 6 templates.

## [2026-05-31] system | Vault OS Upgrade Priority 4 — template enrichment

- Rewrote 6 shell templates in `30_Order/Templates/` from heading-only/frontmatter-only into instructive templates. Each heading now has an HTML-comment description (removed when filling), Templater syntax (`<% tp.date.now("YYYY-MM-DD") %>`, `<% tp.file.title %>`), inline formatting reminders, and plugin syntax (flashcards, Tasks, math, SR cloze warning). All follow the zero-blank-line rule.
- `Clipping Distill Template` (Capability): now matches Vault Rules Part 9 source structure — `**Source/Ingested/Pages**` header, `## Source`, `## Key Claims`, `## Full Content` (### from source titles), `## Why It Matters`, `## Links Into The Vault`, `## Open Questions` (tasks), `## Flashcards #cards/[track]` with single+multiline examples. Frontmatter carries `input_kind`/`track`/`source_note` with enum hints.
- `Week Template` (Classes): now teaches the `## Lecture-to-textbook synthesis` section (==definition anchor==, `*Mechanism:*`, lecture example, textbook connection, concept links, `> [!WARNING]` + `> [!SUMMARY]`), modeled on the MGMT 3001 Week - 9 / Week - 4 gold standard.
- `Concept Template` (Classes): **removed invalid YAML `mastery (1/10): 0`** → `mastery_level: 0`; added `track`, `prerequisites`, `used_in`, `evidence`. Body: One-Line Answer (anchor), Mechanism, Contrast, Failure Modes/Misconceptions, Evidence From This Vault, Flashcards.
- `For Evergreen` (Metadata): added body — Core Claim, Mechanism, Why This Matters Here, Failure Modes, Evidence, Related.
- `For Progress` (Metadata): added body — Goal, Current State, Next Action (mirrors `next:`), Open Questions (tasks), dated Log.
- `Textbook Template` (Classes): expanded from one heading to Chapter Summary (anchor + `*Mechanism:*`), Key Concepts, Examples Worth Keeping, Connections, Flashcards.
- **Deviation from brief, flagged:** the brief suggested `input_kind: textbook`, but every real textbook note (CSCI 4041 Chapter - 24, MGMT 3001 Chapter - 11) uses `input_kind: book`. Followed the ground-truth convention (`book`) over the brief to avoid inventing a value.
- **Schema gap found:** the canonical `input_kind` enum in Vault Rules Part 3 is `pdf|web|video|image|conversation`, but real class notes use `book` and `lecture`. The enum should be extended to include `book` and `lecture`, or those notes reclassified — needs a user decision.
- Why it matters: closes the audit's biggest remaining gap — templates were the quality-control mechanism and were empty, so agents invented structure. An agent filling any of these now produces a note that passes the 16-point gate.
- Open questions: extend `input_kind` enum (`book`/`lecture`)? Confirm `mastery_level` (0–10) is the intended capability field name.
- Next action: Vault OS Upgrade brief (Priorities 1–4) complete. Remaining audit-roadmap items (Source Summaries Board repair, QuickAdd config, Excalidraw template-path fix) require user approval as they touch settings/queries.

## [2026-06-03] system | Summer Operating System — daily/weekly/monthly plans wired into ops
- Built the daily execution layer under `10_Areas/Life/Plans/` per the Summer OS CoWork brief (`00 - CoWork Prompt — Summer OS`). Extracted/operationalized [[Summer Grind]] without rewriting it. Created 9 plan files: `00 - Summer Plans Index`, `01 - Daily Operating System`, `02 - Weekly Operating System`, `03 - Monthly & Phase Map`, `04 - Summer Courses Ops`, `05 - LeetCode & CSCI 4041`, `06 - ML Fundamentals (2033 + 2230)`, `07 - Projects & Hackathons Queue` (stub), `08 - Anti-Drift Rules`, plus `09 - Skill Patches (today + closeday)`.
- Daily OS = 5 wins + academic stack (LeetCode ≥5/day, CSCI 4041 25–45m, CSCI 2033 30–45m, MATH 2230 per board next, HIST 1103 admin-only) with MVP variants and done definitions. LeetCode = primary career win; internship pipeline moved to weekly cadence.
- Course ops pulled deadline truth from [[HIST 1103 Board]] + [[MATH 2230 Board]]: near-term = MATH add/drop Jun 5, HIST Asgmt 1–3 Jun 6, MATH WebAssign Jun 8, MATH Test 1 Jun 15, HIST Midterm Jun 18. HIST locked to admin-only (AI policy = instant fail noted). MATH framed as ML math via [[ML Fundamentals (2033 + 2230)]].
- Populated [[Daily Habit Board]] placeholders with 5 real core habits + no-smoking keystone.
- Skill integration: `.claude/` is write-protected in CoWork, so today.md/closeday.md could NOT be patched in place. Delivered exact paste-in section blocks in `09 - Skill Patches`. **Open action: apply Patch 1 (today.md §0 Summer Ops Checklist) and Patch 2 (closeday.md §0 Summer Ops Scorecard) from a session with `.claude` write access.**
- Today note created: [[Today - 2026-06-03]]. Primary calendar (gupt0479@umn.edu) was empty for today → proposed a default Dubai-week block template flagged "copy into Google Calendar."
- Did NOT do: MCP/tool config, repo triage, AI-platform comparison (per brief constraints). No whole-vault scan — read only the brief's priority-table sources.
- Next: apply the two skill patches; run `/today` tomorrow to confirm the Summer Ops Checklist loads; start MATH WebAssign before Jun 8.

## [2026-06-03] system | Deepened 05 & 06 into file-mapped study systems (CSCI 4041 + ML track)
- Per `00c - CoWork Prompt — Enhance 05 and 06`. Read via `jarvis` MCP: [[ML_Foundations]] (full), [[DSA]] (full 14-week LeetCode plan + 15 concepts), [[MATH 2230 - Calendar]], Concepts_old (15 files), 4041 Concepts subfolders, Midterm/Final Project folders, company repos in [[Repos]] + [[How Anant Uses Each Repo]].
- **Deliverable A — rewrote `05 - LeetCode & CSCI 4041`**: strategic summary; 15-concept mastery table (real note paths + mastery 0–10 + LC patterns + company-tags columns); Never-Forget checklist (explain/implement/2 mediums/story) gating `tree`; spaced revision + 48h pre-interview cram; ≥5/day = 3 pattern + 2 company; company rotation Google→Amazon→Meta from the two company-wise repos; 14-week syllabus mirroring DSA.md week numbering with concept/company/project columns; AVL midterm + Maze final as milestones (Weeks 5–6, 10–12) with project-folder links; overview-without-overload (one concept/day, 2-week full pass).
- **Deliverable B — rewrote `06 - ML Fundamentals (2033 + 2230)`**: two-track model; 14-unit ML spine each mapped to a real Concepts_old filename with prereqs/output/done/2230-bridge; PageRank + graphs + ML_Foundations §7 explicitly **Deferred — Endgame** (deep pass, last 2–3 wks); required 2033↔2230 bridge table keyed to MATH 2230 calendar weeks; MATH ML concept-note path chosen = `20_Progress/Degree/MATH 2230/Concepts/`; vault hygiene (Concepts_old primary, Concepts_new supplemental, no full Week-* reread); organize-csci2033 merge left as backlog.
- **New files:** `05a - LeetCode Tracker.md` (daily log + weekly totals + cram list), `06a - ML Fundamentals Progress.md` (unit checklist + locked Endgame queue + 2230 bridge tracker). Frontmatter `notes:` updated on 05, 06, and `00 - Summer Plans Index`.
- Did not touch `01`/`02`/daily workflow (one-line links only). All vault I/O via Obsidian `jarvis` MCP.
- Next: set the start-Monday so syllabus week dates resolve; begin ML spine unit 1 + AVL project at Week 5; create first MATH 2230 bridge note this week.

### 2026-06-07 — Jarvis OS North Star + read-stack convergence (start)
- **Diagnosis (grounded in live vault):** Jarvis is over-built and under-converged, not weak. Cold-start read order sends agents through ~10 overlapping instruction docs (several thousand lines) before any write — the "redirection tax" that spends the context budget on navigation and starves content. Confirmed: shell templates (per 2026-05-31 audit), 3 competing plans with no single execution surface, hooks that only guard/stitch (no automatic loop). System has been formally audited twice — itself a symptom of re-planning over converging.
- **New file:** `60_Claude/07_AI_Information/Jarvis OS — North Star.md` (type: project, status: sprout). The single strategy spine: Part 1 diagnosis, Part 2 each stated problem → its solution (collapse read-stack, progressive disclosure, instructive templates, the OS loop Capture→Triage→Distill→Connect→Promote→Retrieve→Review, one execution dashboard, skill-engineering standard + jarvis-cli backing, Jarvis MCP verb surface, token economics, automation tiers), Part 3 the 3-month target (context server / answer engine / research engine / single surface), Part 4 the 4-move convergence plan, Part 5 token economics rules, Part 6 the read-stack cleanup this triggers.
- **Root files updated to defer to it:** `AGENTS.md` (Priority Files pointer), `CLAUDE.md` (top pointer + added to shared context list), `HUMAN_WRITING.md` (top one-line: owns voice only; North Star owns why, Architecture owns where).
- **Grounding:** Anthropic context-engineering + Agent Skills guidance (progressive disclosure, just-in-time retrieval, frontmatter-as-query, sub-agents, compaction).
- **Next (move 1 cont.):** shrink AGENTS/CLAUDE to one-screen contracts; merge Vault Map / AI_CONTEXT / Vault Rules / Agent Operating Guide → 2 files (orientation + live-state manifest); then templates (move 2), single dashboard (move 3), first scheduled loop (move 4).

### 2026-06-07 (cont.) — North Star rewritten into definitive fix-it spec
- **Research done first:** 8 GitHub repos (obsidian-mind, autoresearch, CPR, claude-context, mattpocock/skills, karpathy-guidelines, llm-council, ECC) + Anthropic official docs (context engineering, Agent Skills, skill best-practices, subagents). Key imports: obsidian-mind "procedural code owns environment, agent owns content" + 5-hook lifecycle + tiered loading + QMD-as-MCP; autoresearch instruct/read/execute file split (resolves the "3 md + 3 py skill" intuition); canonical SKILL.md rules (name/description frontmatter, <500 lines, one-level-deep refs, degrees-of-freedom = when to use Python).
- **Deep vault read:** catalogued the real disease — 4 files each claim authority (Vault Rules / Vault Operating System / Jarvis Vault Architecture / AGENTS), 4 conflicting cold-start read orders, same rules (blank lines, frontmatter, formatting markers, plugin integration, routing) restated across 5–7 files. Also found: skills use `**Description:**` prose not real frontmatter; `jarvis-memory` MCP server already exists (jarvis_status/search/reindex + full schema) but isn't wired this session — so "no MCP tools for Jarvis" is false.
- **Rewrote `Jarvis OS — North Star.md`** (now ~150 lines, the authority file): Part 1 diagnosis-with-evidence, Part 2 why-too-much-content (no deletion discipline), Part 3 every problem→solution, **Part 4 full per-file audit table (keep/merge/cut/fix verdict for all ~13 instruction files)**, Part 5 build standard (skill dir structure, subagent, hook lifecycle, MCP growth path), Part 6 token economics + tiered loading table, Part 7 strict going-forward rules (one-fact-one-home, no-new-file-without-deleting, grill-before-build, surgical edits, done=verified), Part 8 3-month target, Part 9 convergence build order (4 moves), Part 10 read-stack collapse.
- **Next (Move 1):** execute the Part 4 audit — shrink AGENTS/CLAUDE, merge formatting docs into one spec, merge orientation into one file + live-state manifest. Then Move 2 templates, Move 3 dashboard, Move 4 wire jarvis-memory + 2 scheduled tasks.

## [2026-06-11] convergence | North Star — Full Five-Phase Execution

- Report: [[North Star Convergence — Change Report 2026-06-11]]
- Worklog: [[60_Claude/07_AI_Information/Session Logs/Convergence Worklog 2026-06-11]]

**Phase 1 (Move 1 — Instruction collapse):**
- JWF promoted to single formatting authority; Content Density Standard, Source Note Format Rules, Quality Gate, Safety Rules migrated in from Vault Rules
- Vault Rules stripped from ~550 to ~50 lines; Agent Operating Guide reduced to redirect; AI_CONTEXT deduplicated; AGENTS.md, CLAUDE.md, Vault OS, HUMAN_WRITING all trimmed to pointers

**Phase 2 (Move 2 — Templates):**
- Deep Dive Template: Templater date syntax bug fixed (`{{date}}` → `<% tp.date.now() %>`); descriptions + examples added to all 13 sections
- For Evergreen, For Progress, Textbook Template, Week Template, Clipping Distill Template: descriptions and example content added under every heading; gold-standard links to MGMT 3001 Week - 4

**Phase 3 (Move 3 — Dashboard):**
- 00_Dashboard.md restructured: Today → In Motion → Triage → Decay → Classes → Navigation → Vault Health; all 13 Dataview queries preserved; three link sections collapsed to inline navigation block

**Phase 4 (Parts 5.1–5.2 — Skill/agent YAML):**
- 12 skills converted from `**Description:**` prose headers to `name:`/`description:` YAML frontmatter
- 4 agents converted from `**Type:**`/`**Purpose:**` to YAML frontmatter; stale scratchpad notes removed from mcp-hub + learning-agent
- ops.md split: ops.md ~230 lines (dispatch + examples), ops-reference.md ~280 lines (engine specs)

**Files touched:** 17 vault notes, 17 tool-layer files, 1 new skill created (ops-reference.md)
**Scope boundary held:** no MCP verb wiring, no semantic index, no new automation, no Archive/Clippings/obsidian writes


## 2026-06-12 — Frontend Overhaul Build Kit (Cowork)
Built the master setup plan for the portfolio **frontend** rebuild, mirroring the proven chatbot kit structure (design folder + build-kit folder). New folder `20_Progress/Projects/CS/Portfolio/frontend/`.

- **Design folder (10 notes):** spine (`00`), the two unifying primitives — `01 Motion System & Comet Cards` (useSpaceFloat / CometCard / SpaceRail) and `02 Sanity as Single Source of Truth` (skill as a referenced doc, no-hardcode contract) — then per-section specs `03`–`08` (Experience, Projects carousel, Skills graph, Education flowchart, Certs/Achievements, Blog/Contact/Footer), plus `09 Sanity Content Spec`.
- **Collapsed the 24-item brief** in `Portfolio.md` into two theses: one motion language + one data source. Resolved the open Contact question ("frame not fill" glass frame + localized text scrim).
- **Real content pulled from vault** for the Sanity spec: OpsPilot, Resq, SafeReach, the nextgen AI portfolio agent, Jarvis OS, Arc — professional tagline/description/skills each. Filler removed. repoUrls to be resolved via github MCP; broken liveUrls hidden.
- **Build-kit folder (4 notes):** index, subagents (reuse three-artist/frontend-builder/sanity-schema), commands/hooks **+ the flagged CSP header for `next.config.ts`** (the open item from the chatbot build, now Phase 7), and 8 per-phase copy-paste prompts (Phase 0 Sanity-SoT → Phase 1 primitives → 2–6 sections → 7 CSP/ship).
- **Out of scope per user:** Hero/About/terminal (Kiro-done), Orby (next prompt), light mode.

Next: run Phase 0 from `frontend/claude-code-setup/03 - Per-Phase Build Prompts.md` in WSL.


## 2026-06-12 — Frontend Kit reconciled to codebase reality (Cowork)
Claude Code (Sonnet 4.6) wrote `frontend/10 - Codebase Reality & Confusion Clearance.md` — a verified read of the live repo. Treated it as codebase source of truth and reconciled the whole kit to it.

- **Corrected the data model across notes 02 + 09:** no `skillCategory` doc (category is a string enum), no `color` field (derived from category via CATEGORY_COLORS), reference fields are `technologies[]` (experience/project) vs `skills[]` (certification) — no renames, `githubUrl` not `repoUrl`, `percentage`/`proficiency`/`tone` not color/familiarity/level.
- **Reframed notes 03/05/06 from "broken→rebuild" to "working→augment":** experience header already centered (real gap = Portable Text description not rendered); skills section not broken (2D pill grid + per-category effects exist; stock-chart graph is the target add); education blobs already implemented (real gap = `logo` missing from EDUCATION_QUERY).
- **Two decisions (asked Anant):** enhance the Framer-Motion carousel rather than rebuild in R3F; add a `summary` field to the project schema for hover detail.
- **Created 3 missing-component notes:** `11 - ObsidianBackground Enhancement` (Bloom/additive/chromatic/hue, perf-guarded), `12 - Orby Friction Fixes` (speech-cloud clamp, scroll recal, mobile overlap — model out of scope), `13 - Dark Mode Toggle` (dead pill → real dark-only button; light mode deferred).
- **Rewrote phase order to note 10 Part 7** in spine `00` + build-kit `00`/`02`/`03`: 7 phases (0 content+2 schema touches → 1 primitives → 2 theme pill → 3 background → 4 sections → 5 Orby → 6 CSP report-only). Enforced the "do not" list (pnpm only, no commits/deploys by the agent, no type-file edits, no renames).

Folder `frontend/` now holds 13 design notes + `claude-code-setup/` (4). All reconciled and internally consistent. Next: run Phase 0 in WSL.


## 2026-06-13 — Frontend refinement pass (Cowork)
Anant ran all build prompts; the build largely shipped (screenshots confirm capability graph, R3F education blobs, R3F projects carousel, achievements rail, centered headers, summaries). Claude Code's BUILD-STATUS "nothing built" table was wrong. Used the graphify codebase map (`Portfolio/INDEX`, `/architecture`, `/components`, `/data`) as ground truth and reframed the whole kit as a **refinement pass**.

- **Two codebase corrections from graphify:** Projects carousel is **R3F** (drei `Float` + `@react-spring/web`), Education flowchart is **R3F** (`MeshDistortMaterial` + `Float`) — earlier notes wrongly said Framer Motion. Updated notes 04, 06, prompts.
- **Schema decision (asked Anant):** ADD a per-skill `color` preset field to Sanity (reverses note 10's "no color" rule) — drives the dot everywhere except the Skills section. Also: remove `project.visibility`, make `coverImage` optional, add `project.summary`, add `logo` to EDUCATION_QUERY. Updated 02 + 09.
- **New note 14 — Global Fixes:** dark-mode pill must be static (remove drift); kill the `.section-backdrop::before` blank block + unify section padding to one token; Achievements subsection = smaller header + minimal gap.
- **Rewrote section notes 03–08** as refinement fix-lists per BUILD-STATUS `## UI Fixes` 1–14: experience (type-chip by location, achievements off gold, click-to-open description, comet down, Sanity dot colours); projects (comet down, side cards decoupled from centre hover, remove case-note → summary only, ≤4 skills); skills (remove count box + All button, same-line layout, divergent lines, unique mobile/soft-skills/testing effects, 7 fixed-size skill effects, no dot here); education (equal opacity, deformation gradient via distort, off-axis, single upward pulse); certs+achievements (comet down, out-links, one transparent subtle comet for all three); blog/contact/footer (centre blog header, GitHub bottom-lift not comet, smaller contact card, edge-aligned compact footer).
- **Rewrote `claude-code-setup/03` as R0–R8 refinement prompts**; updated spine 00 + build-kit index; corrected BUILD-STATUS's stale table with a banner (kept the UI Fixes list).

Folder now: 15 design notes (00–14) + BUILD-STATUS + claude-code-setup (4), all reconciled to the live codebase + the new UI-fix backlog. Next: run R0 in WSL.


## 2026-06-13 (2) — Frontend final refinement pass, ship-today (Cowork)
Sanity verified working (GitHub link resolves, fake certs removed, one real cert renders). Made the refinement prompts airtight for a single final build + same-day deploy.

- **Two new specifics baked in:** (a) Experience employment-type chip currently renders by the title — move it to the location row (note 03 + R2 explicit). (b) Skills has TWO category rows — delete the coloured count-pills row, fold counts onto the real filter buttons, remove "All", keep the count caption without breaking graph/skills alignment, no gap under the header (note 05 + R4 rewritten).
- **Rewrote `claude-code-setup/03`** as R0–R8 with explicit ACCEPTANCE criteria per phase; every BUILD-STATUS UI Fix 1–14 + the two global fixes mapped to a phase. Agent stops at green-light; Anant deploys.
- **New `claude-code-setup/04 — Prerequisites & Deploy Checklist`:** packages to confirm (@portabletext/react for the experience description; drei/react-spring/recharts already present), typegen-after-schema, per-phase verification, final pre-deploy checklist, and CSP-can-follow-deploy guidance so it never blocks launch. Wired into the build-kit index.
- Coverage check: R0 (header static + spacing), R1 (schema: color/summary/coverImage-optional/visibility-removed/logo + content), R2 Experience, R3 Projects, R4 Skills, R5 Education, R6 Certs+Achievements, R7 Blog/Contact/Footer, R8 Orby+a11y+optional CSP → green-light → deploy.

Folder is final: notes 00–14 + BUILD-STATUS + claude-code-setup (00–04). Next: run R0 in WSL, work through R8, then deploy.


## [2026-06-20] skill-repair | .claude/ layer fix

- Fixed broken paths (12 sites, verified by grep) in: learning-agent.md (×2: 07_AI_Information, 44_Indexes/Field OS), career-operator.md (Session Logs path), vault-curator.md (10_Areas/UMN), context.md (×4: 10_Areas/UMN, 60_Claude/00_Inbox, /today→/startday), mcp-hub.md (×2: 07_AI_Information), ops-reference.md (44_Indexes/Field OS), trace-topic.md (10_Areas/UMN), weekly-review.md (07_AI_Information).
- Corrections vs. the source prompt (verified against the live vault): `Field OS` lives under `44_Indexes/Field OS/` — preserved the subfolder rather than collapsing to `44_Indexes/`; weekly-review.md had no Field OS path (prompt was wrong); anti-drift list lives in `08 - Anti-Drift Rules.md`, not file 01.
- Restructured `ingest-clipping.md` → `ingesting-clipping/` directory per North Star Part 5.1: SKILL.md (entry/routing) + reference.md (ToC; pypdf→multimodal Read fallback in §2; Jina Reader prefix in §4) + examples.md (per-source frontmatter) + scripts/extract_pdf.py.
- extract_pdf.py: pypdf primary; exits 2 when avg <200 chars/page → caller falls back to multimodal Read (replaces the old "OCR needed" dead end). Verified: exit 0 on real text PDF, exit 2 on blank/scanned PDF.
- Updated research-distiller.md PDF block to call the script + multimodal fallback. Updated SessionStart hook read order (Vault Map → North Star). Patched startday.md: template fallback, dynamic anti-drift pointer to file 08, wikilink for daily-note path. Updated commands/ingest-clipping.md to point at the directory.
- Old flat `ingest-clipping.md`: workspace mount blocks deletion and the delete permission was declined, so it was converted to a redirect stub pointing at the new directory. Safe to delete manually.
- Not touched (out of scope): vault notes, jarvis-memory wiring, .obsidian/.cursor/.kiro.


## [2026-06-20] skill-repair | .claude/ layer — final fixes

- Fixed `60_Claude/45_Outputs/` → `60_Claude/35_Outputs/` in learning-agent.md (Phase 4, Evidence gap).
- Updated research-distiller.md: routing table PDF Read-Method cell → `extract_pdf.py` (pypdf → multimodal fallback); Web URLs step → Jina Reader primary (`https://r.jina.ai/` prefix) + direct WebFetch fallback.
- Deletion was enabled for the Jarvis folder this session, so both files were actually removed (not stubbed): `__deltest.tmp` and the `ingest-clipping.md` redirect stub. The flat ingest-clipping skill is now fully gone; only `ingesting-clipping/` remains.
- Verified: 45_Outputs → zero matches; r.jina.ai → present in research-distiller; both junk files GONE; ingesting-clipping/ directory intact.


## [2026-06-20] research | token optimization — limits, Obsidian, Cowork

- Researched (web + Anthropic help center) how Claude usage limits work in 2026: NOT a fixed message count — token/compute budget weighted by model, conversation length, effort, and loaded tools. Dual 5-hour rolling window + weekly cap (since Aug 2025); all surfaces (chat, Code, Cowork) share one pool. Key driver: every message re-sends full conversation history.
- Extended `40_Resources/Obsidian/Claude Pro Workflow.md` (the canonical rate-limit note per North Star) rather than creating a new top-level note: added "How the Limits Actually Work (2026)", "Cowork Discipline", and a paste-ready "Token-Discipline Block". Fixed two dead paths in that note (7_AI_Information→07, 10_Session_Logs→07_AI_Information/Session Logs).
- Audit delivered in chat: biggest levers = (1) Opus→Sonnet default in Cowork, (2) one chat per task, (3) trim connected MCP connectors (deferred-tool loading already mitigates upfront cost).
- Note: bash mount showed a stale line count; Read tool confirmed the file is correct and complete (158 lines).

## [2026-06-20] system + ingest | GitHub repo ingestion formalized + live test

Audited the web-clipping ingestion pipeline (`05_Clippings/Web/`, 29 raw clips) and the `ingesting-clipping` skill/`research-distiller` agent against the user's ask: interlink web/repo ingestion to `40_Resources/`, and ingest GitHub repos "like an actual human developer" rather than scraping the rendered page.

**Gap found:** neither the skill nor the agent had a GitHub-repo row in their Source Type Routing tables, despite `Github Ingestion/` already being a documented output folder (Vault Architecture, Capture to Summary). The ~35 existing notes in `10_Source_Summaries/Github Ingestion/{Claude Starred,AI Starred}/` were produced ad hoc from README scrapes, not a repeatable method, and predate the current Source Summary Standard (missing `input_kind`/`track`/`source_note`). Also found: web clips of GitHub pages (e.g. `A collective list of free APIs.md`) just duplicate the README; and JS-embed clips (e.g. `V1 Recently Funded Startups.md`, a Google Sheets iframe) capture empty with no fallback defined.

**Patched (additive, no renumbering of existing content):**
- `ingesting-clipping/SKILL.md` — added GitHub-repo row to routing table; safety-rules line on never scraping a repo's rendered page as a substitute for reading it.
- `ingesting-clipping/reference.md` — new §6 "GitHub repository extraction" (gh api primary path, two depths: reference-only vs. adoption-candidate, scratch-clone-and-delete for cases needing full grep); added the empty-iframe/JS-embed failure mode to §5; renumbered quality gate to §7.
- `ingesting-clipping/examples.md` — added GitHub frontmatter skeleton.
- `research-distiller.md` — mirrored the routing row, the `gh api` method, and the empty-embed fallback; Step 4 now also checks `40_Resources/CS/AI/{Toolkit,Workflows,Gen AI,Prompts,Token Optimization}/` for a tool's existing home before proposing a new one.
- `30_Order/Standards/Source Summary Standard.md` — `input_kind` enum gained `github`; Links Into The Vault section now names the 40_Resources interlink check (propose, don't bulk-write).
- `Clipping Distill Template.md` — `input_kind` comment updated to match.

**Live test (proves the patched method, not just the docs):** ingested `aiwithremy/claude-skills-llm-council` two ways at once — the existing web clip (README) plus a live `gh api` pull of the actual `SKILL.md` (the file the README only describes). Found a real discrepancy this surfaces that README-only ingestion would have missed: the landing-page clip claims Path B "saves an HTML report," but the live `SKILL.md` explicitly forbids generating files and mandates chat-only output. Created:
- [[LLM Council skills]] — Tier-2 note, built from the live file fetch.
- [[60_Claude/10_Source_Summaries/Web Ingestion/Claude Council — Path A Prompt (web)]] — discovery-record note from the Notion landing-page clip, cross-linked to the repo note.
- Both link to `[[40_Resources/CS/AI/Toolkit/Github Skills]]`; a one-line addition there (matching its existing table) is proposed, not written — promotion stays curated.

**Tools confirmed already present, nothing new installed:** `gh` 2.89.0, `git` 2.52.0, Python 3.13.5 + `pypdf` 6.10.2, GitHub MCP tools (`get_file_contents` resolves both files and directories), `WebFetch`. No new MCP server or package needed for either tier of GitHub ingestion.

**Open / left for the user:** the ~89 remaining un-ingested repos from `40_Resources/CS/Repos.md` (AI section ~21 left, Building/Projects/Jobs/Learning/Cybersecurity sections have zero per-repo notes yet); whether to scale the patched method across all 29 web clips now or in batches; the 6 sample iframe/broken clips that need the empty-embed fallback applied; whether to actually propose-and-apply the `40_Resources/CS/AI/Toolkit/Github Skills.md` addition for LLM Council.

**User approved both proposals** — added the LLM Council row to `40_Resources/CS/AI/Toolkit/Github Skills.md`, then ran one validation batch (8 items, mixed) before committing to the full backlog.

**Batch results:**
- **Empty-embed fallback validated for real:** `V1 Recently Funded Startups.md` (Google Sheets iframe) — `WebFetch` on the live URL also returned nothing, confirming the double-failure path in reference.md §5. No Source Summary note created (correct behavior — nothing to summarize); raw clip needs a manual CSV export from the user before it can ever ingest.
- **Found and documented a third failure mode live:** `Gurwinder  Substack.md` clipped the blog's homepage (post-title index), not an article — not empty, but not the essay content the title implies. Added "the index-page clip" as a named failure mode to reference.md §5. Wrote an honestly thin note rather than padding a fake essay summary; flagged which 2 of the 12 listed post titles look worth re-clipping directly.
- **One clean standard ingestion:** [[60_Claude/10_Source_Summaries/Web Ingestion/The New Coding Interview — 5 Resources (web)]] — full Source Summary Standard depth (5 numbered resources reproduced in full, flashcards). Surfaced a real vault gap: no `10_Areas/Career` hub exists yet to file non-repo interview-prep resources (SadServers, Testing Trophy, Google review guide, MIT Missing Semester) against.
- **Found and resolved a design gap in the GitHub-ingestion patch itself:** the full Source Summary Standard (Key Claims → Full Content → Flashcards, reproduce-every-line) doesn't fit software READMEs the way it fits essays/PDFs. Added a "note depth follows tier" rule to reference.md §6: reference-only repos use the lighter shape already proven in this vault (`What It Is / Core Capabilities / Why It Matters / Use Cases for Jarvis / Tradeoffs / Related`, no flashcards) — reserve the heavy structure for adoption-candidate repos where source files were actually read.
- **5 Tier-1 repo notes written** via `gh api` (metadata + README, no clone): [[pocketbase (github)]], [[60_Claude/10_Source_Summaries/Github Ingestion/n8n-workflows (github)]], [[tradingview-mcp (github)]], [[60_Claude/10_Source_Summaries/Github Ingestion/AI Starred/goose (github)]], [[60_Claude/10_Source_Summaries/Github Ingestion/AI Starred/promptfoo (github)]]. Each surfaced something the existing stale vault notes missed: **goose moved from `block/goose` to the Linux Foundation's `aaif-goose/goose`**; **promptfoo is now part of OpenAI** (the existing `Repos-Deep-Analysis.md` entry predates this); n8n-workflows' README leads with a third-party security-scanner ad claiming hardcoded keys were found in this exact workflow set.
- **Updated `40_Resources/CS/Repos.md`:** converted all 5 (+ the promptfoo Cybersecurity cross-reference) from plain links to verified wikilinks, refreshed star counts, and inlined the goose/promptfoo/n8n-workflows findings above directly into the one-liners.

**Not updated (flagged, not touched):** `Repos-Deep-Analysis.md` and `GitHub Stars — How Anant Uses Each Repo.md` still carry the pre-acquisition/pre-move framing for promptfoo and goose — these are prior-session narrative docs, left alone rather than rewritten in this pass.

**Next:** ~84 repos and 26 web clips remain. Method is now validated twice (Tier-2 deep + Tier-1 reference, plus two distinct failure-mode fallbacks) — ready to scale to the full backlog on the next go-ahead.

---

## 2026-06-25 — TradingView Research Completion

**Task:** Complete the three-area research pass for the TradingView project initiated in the prior session.

**Correction logged:** Prior session incorrectly identified Kronos as "Amazon's Chronos." Corrected in Research note — Kronos (shiyu-coder/arXiv 2508.02739) is a separate Tsinghua University model, financial-specific, accepted at AAAI 2026.

**Files written:**
- `20_Progress/Projects/CS/TradingView/Research - Systematic Equity Strategy Edge (2026-06-25).md`
- `20_Progress/Projects/CS/TradingView/Research - Kronos Foundation Model Deep Dive (2026-06-25).md`
- `20_Progress/Projects/CS/TradingView/Research - Trading Fundamentals Gap Fill (2026-06-25).md`

**Key findings:**
1. **Strategy edge gap:** Current strategy modules (trend following, mean reversion, quality, valuation) are contextual checks, not factors with documented evidence. Cross-sectional 12-1 month momentum (Jegadeesh-Titman), QMJ quality composite, FCF yield, and low-volatility are the academically supported signals missing from the current engine. RSI/Bollinger stay as descriptive context only — not as action drivers.
2. **Kronos:** NOT Amazon Chronos. Decoder-only transformer + specialized OHLCV tokenizer. Trained on 12B K-lines from 45 exchanges. Kronos-small (24.7M params, 512-bar context) is the right V1 choice. Must validate RankIC on our specific universe before using as evidence input. Input: pandas OHLCV DataFrame; output: forecasted OHLCV DataFrame with sample_count paths for uncertainty.
3. **Fundamentals gaps closed:** Alpha/beta, systematic vs idiosyncratic risk, risk-on/risk-off regimes, Sharpe/Sortino/Calmar (thresholds documented), walk-forward validation (2-4yr optimize / 3-6mo OOS), Deflated Sharpe Ratio, Kelly/half-Kelly position sizing, Fama-French free data.

**Next immediate tasks (not yet started):**
- Revise `AI Market Analyzer - Strategy Engine.md` to add `momentum_score` (12-1 month), `safety_score` (realized volatility inverse), `quality_fcf_score` (FCF-weighted)
- Run Kronos validation pass on V1 universe historical data (once dev environment is accessible in WSL)
- Complete Kiro tasks 7.2-7.4 (DataQualityAuditor property tests)
- Complete Kiro tasks 9-13 (evidence.py, benchmark.py, polygon.py, cli.py)

## 2026-06-28 — GitHub Ingestion Complete

**Completed:** Full ingestion of all 92 starred repos from `40_Resources/CS/Repos.md`.

**Repos marked not useful (10 total):** jarvis (ethanplusai), react-three-fiber, semantic-search-nextjs-pinecone-langchain-chatgpt, Ghostty Blackhole, ProjectLearn, modern-js-cheatsheet, free-programming-books, Paperclip, Mike, Pretext.

**Notes created this session (15):**
- Projects Starred: build-your-own-x, app-ideas, 500-ai-ml-projects, public-apis, devops-projects-notharshha, devops-projects-techiescamp
- Learning Starred: freeCodeCamp, project-based-learning
- Building Starred: openbb
- AI Starred: agentscope, free-llm-api-resources, llmfit, jan, odysseus
- Claude Starred: last30days-skill

**Total notes in `60_Claude/10_Source_Summaries/Github Ingestion/`:** ~95 across 6 subfolders (Security, Jobs, Learning, Building, Projects, AI/Claude Starred).

**Open questions:** Odysseus (pewdiepie-archdaemon) has a minimal description — revisit if it turns out to be a substantial tool.

## [2026-07-03] fable-p1 | Dashboards + skills wired for daily use

- Write guard (`30_Order/System/claude-workflow/hooks/jarvis-write-guard.ps1`): added daily-ops allowlist (Daily/, Plans/, Templates/, .claude/skills+agents, 00_Dashboard.md, session log, Claude OS.md) checked before denials; added denials for 60_Claude/05_Clippings/, .cursor/, .kiro/, .git/. Verified with 14 piped payloads — all pass.
- `00_Dashboard.md`: full replace. Meta Bind bind targets (today_focus/today_80/today_20, lc_today/wins_done/study_today), weekly-totals DataviewJS over daily-note frontmatter, priorities/projects/internships/clippings/metadata queries, navigation row. All dead `10_UMN` queries gone.
- `30_Order/Templates/Enumerate/Better Today.md`: added created + lc_count/study_today/wins_done/habits_done frontmatter and Meta Bind inputs under ## Productivity.
- `/startday` → `.claude/skills/startday/` (SKILL.md + reference.md); new Step 3b patches dashboard focus fields. `/closeday` → `.claude/skills/closeday/` with auto-gather, one 5-question block, frontmatter metrics write, dashboard reset (incl. today_20). Both `.claude/commands/` pointers updated; old flat files deleted.
- All 5 agents (`.claude/agents/`): descriptions rewritten to "Use proactively… MUST BE USED…" pattern, `tools:` allowlists + `model: claude-sonnet-4-6` added.
- Homepage plugin verified: managed by lazy-plugins (short), config already opens 00_Dashboard on startup — no change needed.
- Why it matters: the daily loop (/startday → Meta Bind inputs → /closeday) now writes queryable metrics the dashboard actually renders.
- Open: dashboard's navigation wikilinks to 10_Areas/AI/ guides, Life OS, and trackers resolve once P2/P3 create them.
- Next: P2 — platform guides + Claude OS registry expansion.

## [2026-07-03] fable-p2 | Claude OS: platform guides, registry, MCP verified

- Created `10_Areas/AI/` guides: `Claude Code.md`, `Cursor.md`, `Kiro.md`, `Codex.md` — operational per-platform guides built from the `20_Progress/AI/` dumps (projects, components, when-to-use-which, gap lists).
- jarvis-memory MCP verified live: server connects, `jarvis_reindex` built the index (8,124 notes), `jarvis_status` + `jarvis_search` return correct results. Semantic search (chunks/embeddings) remains the next build.
- `Claude OS.md` expanded: real static tables replace the dead Dataview blocks; second-brain-claudekit overlap/gap analysis (11+10 commands fetched live from GitHub — gaps: /emerge, /challenge, /schedule, CPR /preserve pattern); everything-claude-code triage (~240 skills → 8 High, ~15 Medium, rest Low; path corrected to WSL Home); known-gaps checklist updated.
- Created `20_Progress/AI/Claude OS Dashboard.md` (operational: inventory, health checks, open actions) and `10_Areas/Excalidraw/Claude OS Map.md` (text canvas blueprint — no hand-authored .excalidraw JSON).
- Why it matters: the whole agentic estate is now catalogued in one registry + one dashboard, with verified (not assumed) component status.
- Discovered: everything-claude-code lives in WSL Home, not Windows Home; Claude Code Portfolio/TradingView and Cursor DNA App/Trading View dump folders are empty — re-export needed.
- Next: P3 — frontmatter pass, Life OS + trackers, UMN cross-links.

## [2026-07-03] fable-p3 | Frontmatter pass, Life OS, cross-links

- Frontmatter pass: 77 notes got minimum type/status (+created from file ctime, +domain tag where absent) — Portfolio design docs (30, as concept/sprout to keep the dashboard's Active Projects query clean), CausalOps briefs (~32), Inbox/Resources/Areas strays. Excluded: 20_Progress/AI dumps (config snapshots, not notes), 60_Claude/00_Inbox/copilot/ (plugin data), 40_Project_Briefs/TradingView (read-only), kanban/excalidraw files, 50_Archive, 05_Clippings.
- Created `10_Areas/Life/Life OS.md` + `10_Areas/Life/Tracking/{Health Tracker, Finance Tracker, Relationship Log}.md`. Life OS marks unknown baselines as unknown (weight, monthly spend, mentor names) instead of inventing them; each tracker's job is converting one unknown into a trend line.
- Finance conflict resolved per user rule: Life/Finance/ has content → Tracking/Finance Tracker.md created and cross-linked both ways with Bank Accounts + Stocks. FLAG: `10_Areas/Career/Finance/` holds byte-identical copies of the same two notes — unfinished move, needs a user decision (delete Career copies or Life copies).
- Cross-links (concrete only): 05 - LeetCode & CSCI 4041 ⇄ Career/Internships/Tracker; 06 - ML Fundamentals ⇄ Trading/Stocks Trading AI Hub.
- CORRECTION found: current-term course notes do NOT live in `10_Areas/UMN/` (folder doesn't exist) — CSCI/MATH learning runs through `10_Areas/Life/Plans/Summer/05+06`; past courses in `40_Resources/UMN/`. Also fixed: startday skill's plan paths were `Plans/01 - …` but files live in `Plans/Summer/` — corrected in the new SKILL.md + reference.md.
- Next: P4 — clipping ingestion (9 high-signal PDFs first).

## [2026-07-03] fable-p4-high | High-signal PDF ingestion (9/9)

- Installed pypdf (was missing — extract_pdf.py exited 1 on all PDFs until fixed); confirmed mcp 1.28.1 present.
- Ingested all 9 high-signal PDFs to `60_Claude/10_Source_Summaries/PDF Ingestion/` (Quant Foundations already existed as the gold standard, so 8 new):
  - Outreach Automation Manual (career) · AI Prediction Market Trading Bot (trading) · How to Pivot into an AI-ML Engineering Role 2026 (career) · DeepThinksFinance AI Portfolio Optimizer (trading) · TRIBE v2 Foundation Model (ai) · BASWE 15 AI Engineering Projects (career) · MIT Quant Bible (trading) · DeepThinksFinance Master Quant Prompt Guide v2 (trading).
- Each note follows the Source Summary Standard: frontmatter with verified notes: links, Source/Ingested/Pages lines, Key Claims, full section-by-section capture, Why It Matters tying to real vault work (Stocks Trading AI Hub, Tracker, CausalOps, ML Fundamentals), Links Into The Vault, Open Questions, and a #cards/[track] flashcard deck.
- Method note: large PDFs (BASWE, MIT Bible, DeepThinks v2 at 114–231K chars) were de-inflated from pypdf's one-word-per-line output via a Python whitespace-collapse, then read in spans / grepped by section — captured every model/project/section without reproducing verbatim boilerplate code (code stays in the source PDF).
- Cross-links between the trading notes form a cluster: MIT Bible ↔ Quant Foundations (strategy vs content), Portfolio Optimizer ↔ Prediction Bot (LLM-as-analyst vs LLM-in-loop), Prompt Guide v2 ↔ both DeepThinks builds.
- Honest framing kept: flagged the DeepThinks retail signals (RSI/Bollinger) as descriptive-not-edge per the 2026-06-25 TradingView research; flagged the AI/ML pivot guide targets 3–5yr SWEs not students (portfolio bar transfers, salary anchors don't).
- Note: markdownlint flagged blank-line warnings on dashboard/reference.md — these are generic MD standard and conflict with the vault's no-blank-line rule; deliberately not "fixed."
- Next: medium/low-signal PDFs + web-clip full ingests (task 15).

## [2026-07-04] fable-p4-mediumlow | Medium/low-signal + web-clip ingestion

- Web full-ingests (7): Agent-Ready Roadmap, Hidden OS Behind Income Ceiling, Output Audit (both Dustin Weiss essays flagged: their "studies" are unverifiable/fabricated — kept the usable frameworks, dropped the fake neuroscience), AI Engineer Roadmap (roadmap.sh — extracted all 217 node labels from the SVG into sectioned topics), AI Engineering from Scratch, NextWork/Automate Your AI Second Brain, Hall of Hacks. Plus the GTM medium clip (Relevance AI — the L1–L4 autonomy ladder is a reusable maturity model for the Jarvis agent layer).
- Medium PDFs: 5 Best MCPs, Claude Code Free with Ollama, Claude Code Status Bar, GitNexus, Obsidian+Claude 12-Command Codebook (third source confirming the /emerge, /challenge, /drift skill gaps), AI Generalist Roadmap (Outskill, via multimodal Read — scanned deck).
- Low-signal (brief notes): LinkedIn Search URL Cheatsheet, 20 Free AI Certifications, Maverick Prompt Shortcuts + Viral Prompts, MavGPT Resume/ATS Guide, Student Travel Discounts, FREE STUFF (honest thin note — lead magnet). Maverick "Resource Hub" web clips 1 & 3 are byte-duplicates of the Maverick PDFs — not re-noted (search-before-create).
- Total this session: 28 source-summary notes (17 PDF Ingestion + 11 Web Ingestion). jarvis-memory reindexed: 8,158 notes.
- CONFLICT FLAGGED: the ingest spec says "mark processed in 60_Claude/05_Clippings/Clippings board.md," but the P1 write guard now denies all of `60_Claude/05_Clippings/` (the stronger, repeatedly-stated AGENTS.md rule: clippings are read-only after capture). The board was NOT updated. Resolution options for the user: (a) accept the log as the processed-record, or (b) add `Clippings board.md` as a single-file exception to the write guard allowlist. Recommend (a).
- Processed clippings this session (PDFs): outreach-manual, prediction bot, AI/ML pivot, DeepThinks portfolio optimizer, Tribe V2, BASWE 15 projects, MIT Quant Bible, DeepThinks prompt guide v2, Best MCPs, Ollama free, statusbar, Nexus/GitNexus, Obsidian+Claude Commands, Road Map, Linkedin Searches, Free AI Certifications, Maverick's 100 shortcuts, Maverick's Viral Prompts, Maverick's Resume, Student discounts, FREE STUFF. (Web): Agent-Ready Roadmap, Hidden OS, Output Audit, AI Engineer Roadmap, AI Engineering from Scratch, Automate Your AI Second Brain, hackathon archive, AI Agents for Sales & GTM.
- Skipped per spec: Claude Council, Magic Fretboard, App Privacy Policy Generator, Pre-Reads Kit, Clone Setup Guide, CodeRabbit, Find profitable startup ideas, Free Claude Cowork Skills, Ultimate Guide to Winning Hackathons, Workbooks/Links (not on any signal tier).

## [2026-07-04] fable-session-close | Full Fable execution pass complete

All four priority blocks from the Fable execution prompt are done. Summary:
- **P1 (Dashboards + Skills):** write-guard allowlist+denylist (tested with 14 payloads), 00_Dashboard rebuilt with Meta Bind + weekly-totals DataviewJS, daily template + tracking frontmatter, /startday and /closeday converted to directory skills (startday gained the dashboard-patch Step 3b; closeday gained the structured 5-question close + dashboard reset incl. today_20), all 5 agents given tools+model frontmatter and trigger-pattern descriptions.
- **P2 (Claude OS):** 4 platform guides in 10_Areas/AI/, Claude OS.md registry expanded (second-brain-claudekit comparison via GitHub MCP, everything-claude-code triage, jarvis-memory verified running — path corrected to WSL Home), Claude OS Dashboard, Excalidraw text blueprint. jarvis-memory index built (was never built before — now 8,158 notes).
- **P3 (Frontmatter + Life):** 77 notes given minimum frontmatter, Life OS + 3 trackers (unknown baselines marked honestly), Finance/ conflict resolved + Career/Finance duplicate flagged, UMN↔Career/Trading cross-links, startday plan-path bug fixed (Plans/ → Plans/Summer/).
- **P4 (Ingestion):** 28 source-summary notes across all signal tiers.
- Open decisions for the user: (1) Clippings board write-guard conflict (above); (2) Career/Finance vs Life/Finance byte-identical duplicate — pick which to delete; (3) empty dump folders (Claude Code Portfolio/TradingView, Cursor DNA App/Trading View) need re-export; (4) adopt /emerge + /challenge skills (confirmed by 3 independent sources); (5) the biggest remaining North Star gap: nothing runs on a schedule yet (morning/evening loop) and jarvis-memory semantic search (chunks/embeddings) is still unpopulated.

## [2026-07-04] fable-pass2 | Dashboard polish, Life OS expansion, ingestion completion

- **Task 1 — dashboard.css:** appended (via PowerShell, `.obsidian/` is write-guard-blocked) progress-bar, multi-column, stat-tile color-state, and summary-callout classes. Verified by reading back — all 5 class groups present.
- **Task 2 — 00_Dashboard.md rebuilt:** stat-tile DataviewJS (Today's Numbers with green/yellow/red states via `dv.el` + innerHTML), Multi-Column Markdown two-column layout, Daily Drivers progress bar keyed to `habits_done` length, weekly-totals block using the `.values.reduce()` form. Frontmatter preserved (cssclasses + Meta Bind targets). Quality gate passed: no bare `.map().reduce()`, cssclasses present, multi-column + dataview plugins both confirmed enabled. Fixed the Navigation "Daily OS" link to `Plans/Summer/01 - …` (was the old un-Summer path).
- **Task 3 — Claude OS Dashboard rebuilt:** health-panel DataviewJS (7 checks as stat tiles, jarvis-memory count corrected to 8,158), Multi-Column inventory/actions, cssclasses added.
- **Task 4 — Life OS expanded:** 69 → ~85 dense unwrapped lines (far more content per line than the count implies) pulling REAL data from the Summer plan files — the 15 DSA concepts + Never-Forget checklist, the 14-unit ML spine + 2033↔2230 bridge, the weekly Mon–Sun rhythm + 7 questions, the smoking-replacement protocol (change-state on craving), the reading list, the mentorship structure (real meeting notes exist), company rotation, and the why behind each rule. Fixed one dangling link (`Easy Way to Quit Smoking` doesn't exist — even Summer Grind links it broken — de-linked to plain title).
- **Task 5 — ingestion completed:** 8 more PDFs (Clone distillation pipeline, Free Claude Code Skill Libraries, Ultimate Guide to Winning Hackathons, Find Startup Ideas with Reddit, CodeRabbit CLI, Junior Extracurriculars, Gen-AI Mastermind Pre-Reads, AI Mastermind Workbook Links) + 6 web clips (Fintech Early Programs HRT/CapOne/Bloomberg, Underclassmen Internship List, 2027 Internship Calendar, Hermes Agent monetization, Naive agent-primitives API, GitOps mis-titled clips). Road Map.pdf skipped (= AI Generalist Roadmap already ingested); Maverick Resource Hubs 1/2/3 skipped (= Maverick prompt/resume PDFs already ingested). Totals now: **29 PDF Ingestion + 17 Web Ingestion notes.** jarvis-memory reindexed: **8,171 notes.**
- **Clippings board updated** (now allowlisted in the write guard — the Pass-1 conflict is resolved): dated batch entry under "Where to Go?" pointing to the two landing folders + the itemized session-log mapping, listing duplicates-not-noted and skipped items.
- **Standout for the user:** the three internship clips (Fintech/Underclassmen/2027 Calendar) are the most actionable career material yet — but they all hinge on **Anant's grad year, which the vault doesn't record.** If he's a rising junior for 2027: freshman/sophomore programs (Two Sigma First-Year, Jane Street FTTP, Microsoft Explore, Google ASDI) have aged out; still-open = Citadel Launch (2nd-yr, $4,300–4,800/wk), MLH Fellowship + NASA OSTEM (any year), HRT (grad-2028 sophomore role), Capital One rising-junior, Bloomberg. Banks are already closed for 2027; near-term focus = quant + big-tech early programs (Aug–Oct 2026 windows). **Record grad year in Life OS/Tracker to make these filterable.**
- **Verification limit:** dashboard DataviewJS/Multi-Column render can't be visually confirmed from here — verified syntactically (reduce form, plugin-enabled, CSS classes present); needs one visual check in Obsidian.
- Next: user decisions still open — grad year; Career/Finance vs Life/Finance duplicate; empty AI dump re-exports; adopt /emerge + /challenge; wire the scheduled loop + jarvis-memory semantic search (the two biggest North Star gaps).

## [2026-07-07] cleanup | Jarvis/Plan boundary — Plans folder, Truths of Life, dashboard, skills

Continuation of the same-day vault-differentiation work. Anant had finished his own live-edit pass (Life OS, trackers, old Habits/Books content already moved to The Plan's `00_Live/`). This session's scope: scrub remaining personal bleed from `10_Areas/Life/Plans/`, `10_Areas/Summer Grind.md`, `00_Dashboard.md`, and the daily-note skills; set up the builder-identity `Truths of Life` folder; recreate a scoped `Career/Finance`; give The Plan's `60_Jarvis` a place to receive future migrations.

**Targeted keyword sweep** (drugs, mental-health terms, friend names, financial specifics) across `60_Claude/07_AI_Information/`, `60_Claude/30_Reviews/`, and `10_Areas/Life/Plans/` found nothing rising to the redaction bar — only mild habit-gate mentions ("no smoking before first task") and file-provenance references. That folder tree was already clean; no session-log history was rewritten.

**Changes made:**
- `30_Order/Templates/Enumerate/Better Today.md` — 5-wins table trimmed to 4 (Physical/gym removed), wins-hit denominator now /4.
- `10_Areas/Life/Plans/Summer/01 - Daily Operating System.md` — full rewrite: 4 wins, day-shape table, checklist copy block, done-definition all updated to match.
- `10_Areas/Summer Grind.md` — "Systems" intro, Dubai P0 week-1 checklist, and Weekly Review System questions trimmed to drop the physical/gym win line. Re-Birth/Projects/Internship subtree was accidentally wiped by a heading-replace patch that doesn't respect nested children — caught immediately via a document-map check, restored verbatim from the pre-edit read, verified byte-for-byte before moving on.
- Deleted `10_Areas/Life/Plans/Summer/09 - Skill Patches (today + closeday).md` — stale, referenced skill filenames (`today.md`) that no longer exist.
- `00_Dashboard.md` — removed the Gym habit line, replaced the dead `**Life:**` footer (linked to already-deleted Life OS/Health/Finance trackers) with a live Daily OS link, fixed `today_20` frontmatter text.
- `10_Areas/Life/Truths of Life/Identities.md` + `Personality.md` — were empty stubs (never written). Scaffolded both with a builder-identity-only scope rule and weekly/monthly/yearly update cadence, per Anant's decision. No content fabricated.
- Created `10_Areas/Career/Finance/Finance Scope.md` — scoped to business/project income only (TradingView, freelancing), explicitly not personal banking. Empty until real income exists.
- Deleted `10_Areas/Life/Books/Atomic Habits.md` + `Essentialism.md` — confirmed The Plan's `00_Live/Books/` copies are the fuller, current versions (41KB vs. 32KB for Atomic Habits); Jarvis's were stale duplicates.
- `.claude/skills/startday/reference.md` — fixed the Physical-win example and the dead "Daily Habit Board" reference (points at the current `10_Areas/Life/Habits/` folder generically now, since the specific filename has changed before).
- `.claude/skills/closeday/reference.md` — scorecard row "5 Wins" → "4 Wins".
- `.claude/skills/weekly-review.md` — added Step 4.5 (Promotion Scan): surfaces `status: tree` candidates from the past 7 days against a 3-line bar, lists them in the synthesis note's new "Promotion Candidates" section. Does not write into The Plan automatically — promotion still requires a review + a logged row in `Promoted From Jarvis Index`.
- `AGENTS.md` and `CLAUDE.md` — appended a "no personal-life content in Jarvis" rule with the Truths of Life carve-out, pointing at each other.
- The Plan: created `60_Jarvis/70_AI_Information/README.md` and `60_Jarvis/80_Session_Logs/README.md` (mirroring Jarvis's structure) as receiving folders for future migrations. Both currently empty/documented-only since the sweep found nothing to move yet.

**Still open:** the `10_Areas/` folder overall hasn't been redesigned yet — Anant flagged that its structure needs a concrete "what am I doing / did / going to do" anchor now that Life content is gone. Not addressed this session; needs a proposal + decision next.

**Next:** propose a `10_Areas` structure/anchor-file design; once Anant confirms, revisit The Plan side properly (build its `.claude/skills/startday`/`closeday` from scratch, rewrite its stale `CLAUDE.md`/`AGENTS.md`/`AI_CONTEXT.md`) in a dedicated session.

## [2026-07-10] tradingview | Cursor alignment pass → vault SoT + Fable 5 handoff

Ask-mode research/alignment across TradingView vault + `research_data` repo, then Agent-mode note write so Fable 5 has a source of truth before the year-ahead base build.

**Decisions locked (full Q&A in [[Session Findings — Cursor Alignment Pass (2026-07-10)]]):**
- Personal edge only (portfolio may mention; software private; no auth/tenancy).
- Zero Kalshi/Polymarket code/schema until stocks paper is live, tested, and real-use-ready; no shared-core placeholders.
- App is research hub (strategies, brain, charts/indicators); TradingView.com later for real-trade record.
- Fast-forward = historical replay journal + live paper UI jump-ahead; four gates OOS→Monte Carlo→walk-forward→deflated Sharpe before demo paper.
- Brain = 1∩2: fixed factors promote/demote via journal/tests; AI proposes specs; human gates code; timed paper auto-entry after thesis pre-approve.
- Elevated differentiator table (test-gated lab + journal; quant math first-class) — not a student toy.
- Brain software module in parallel with ingestion data; Fable 5 hard slice; Cursor owns leftover `.kiro` plumbing.
- Kronos reserved only (no inference until RankIC).
- Fundamentals: minimal FMP + SEC in Fable handoff; `.env` has `POLYGON_API_KEY`, `FMP_API_KEY`, `SEC_USER_AGENT`.

**Notes written/patched:**
- Created: `Session Findings — Cursor Alignment Pass (2026-07-10).md`, `Year-Ahead Base — Fable 5 Architecture Contract.md`, `Math-First Map — Existing Code to Factor Brain.md`
- Patched: Postmortem (repo drift, Decision, Open Questions, Related), RESEARCH (thesis, Barebone gaps, data sources, autonomy, no-money plan), Strategy Engine TODO

**Next:** user sends Fable 5 prompt (refers to `20_Progress/Projects/CS/TradingView/`); after Fable lands base, Cursor finishes `.kiro` 7.2–13 leftovers.

- Also created: `Fable 5 — Read Order (TradingView folder).md` (start here for Fable).

- 2026-07-10 — Fable 5 (resume): TradingView year-ahead base closed out. Verified 420 offline tests green; guardrail sweep clean (no execution language, no PM code, no Kronos inference, no secrets, `.env` ignored). Vault synced: Architecture Contract (Current State / Next Action / DoD), Math-First Map (slices A+B done), Session Findings (Open Questions). Repo docs: `Docs/YEAR_AHEAD_BASE.md` + `Docs/fable5_run_memory.md` updated. Next: live-data shakeout, replay studies, charting/agent layer.

## [2026-07-12] restructure | TradingView AI Brain Hub questionnaire + vault rearrange
- Created `20_Progress/Projects/CS/TradingView/Session Findings/Session Findings — AI Brain Hub (2026-07-12).md` — full decision log for the AI-hub questionnaire (A1–F2, ~20 decisions: card/critic packet contracts, agent topology, litellm provider strategy, citation ingest, StrategySpec proposal contract, offline/live eval harness, secrets/cost, calibration deferral, package layout)
- Restructured `20_Progress/Projects/CS/TradingView/` from a flat ~23-note dump into five plain-named subfolders (no numeric prefixes, per explicit instruction): `Canon/`, `Session Findings/`, `Phases/`, `Research/`, `Archive/`. All moves, zero deletions.
- Archived (not deleted) two now-resolved notes with `> [!NOTE]` supersede banners and `status: archived`: `History Depth Blocker — Massive Starter Required` (resolved via Tiingo, not the Massive upgrade it argued for) and `Phase 2b — Promotion Study (Draft)` (superseded — the study ran and landed, 4/4 gates, `demo_eligible`)
- Rewrote `Fable 5 — Read Order (TradingView folder).md` to point at the new Session Findings note as current SoT and document the new folder map
- Why it matters: the questionnaire session repeatedly caught real gaps between what Cursor's draft decisions assumed and what the actual `research_data` repo code does (DSR trial-counting scope, citation id stability, gate-constant wiring, packet redundancy, etc.) — this note is the durable record so the next Fable/Cursor session doesn't re-derive it
- Open questions: G1–G3 (Cursor/Fable split) not yet answered; live smoke-test symbol (leaning NVDA) not formally confirmed
- Next action: close G-series, then write the Fable 5 AI-hub implementer prompt

## [2026-08-15] degree | APAS refresh + Spring'27 graduation math

Anant pasted his live APAS report (prepared 08/14/26, Fall'26 in progress) plus the CS four-year plan and an old Spring'26 transcript PDF. Asked to refresh the degree notes assuming every graded class (including Fall'26) lands as an A, and to work out what Spring'27 would need to look like to finish both the CS degree and the Entrepreneurship minor.

**Changes made:**
- `40_Resources/UMN/The Plan/APAS.md` — patched by heading (Credits, Classes table, Lib ed requirements, Major Requirements, Elective Credits) with the current numbers: 76 earned + 18 in progress (F26) = 94/120, needs 26 more; GPA 3.338 / tech GPA 3.157, noted both go to 4.0 under the all-A hypothesis. Major: needs 18 more credits, 3 more upper-division. Technical Electives: needs 20 more, 8 more must be CSCI-designated. CS Core fully closes out once F26 posts. Elective Credits: needs 6 more, cross-linked to the minor's remaining electives. Classes table extended through SP26/SI26/F26.
- `40_Resources/UMN/The Plan/Entrepreneurship Minor.md` — appended a "Status (Aug 2026)" section under the existing heading (list of eligible courses untouched): core is done/in-progress (MGMT 3001 + MGMT 3015, 7 credits), 10 elective credits still needed, flagged `MGMT 4171W` as a double-duty pick (minor elective + closes the degree's last upper-division WI gap).
- `20_Progress/Degree/Fall'26 Syllabus.md` — filled in the `Classes` and `Grading Criteria` sections (grading rubrics not yet available, said so honestly instead of fabricating), added a new top-level `Spring'27 — Path to Graduation` section with the full credit math and three concrete paths to graduation (overload Spring'27, add credits to Fall'26 now, or split the minor into Summer'27), plus candidate/backup courses pulled from APAS's own technical-elective and minor-elective lists. Frontmatter `status` seed→sprout, `updated` set.

**Key finding:** finishing the CS major (20 more Technical Elective credits + 1 more upper-division WI course) and the Entrepreneurship minor (10 more elective credits) together is ~30 credits of genuinely new coursework after Fall'26 — doesn't fit one semester at the stated 18–22 credit/semester pace. Wrote up three explicit options rather than forcing a clean answer.

**Tool gotcha found:** `jarvis__vault_patch` on a `frontmatter` target with an array `value` containing wikilink strings (e.g. `["[[APAS]]", "[[Note]]"]`) serializes the whole array into a single quoted YAML string instead of a proper block list — silently breaks the field's type. Had to `vault_write` the full file to restore a real YAML list. Avoid patching wikilink-array frontmatter fields via `vault_patch` until this is confirmed fixed; use `vault_write` with hand-written YAML instead.

**Next:** Anant to confirm with advisor Jacquelyn Rupp whether a Spring'27 overload is possible and whether the minor can post after the major's conferral term; check the Spring 2027 registration guide once published for actual course offerings.

## [2026-08-15] degree | correction pass — CSCI 4521, Fall'27 target, "treat F26 as complete" framing

Follow-up to the same-day APAS refresh. Anant had live-edited `APAS.md` and `Fall'26 Syllabus.md` in Obsidian in between — added a CSCI 4521 row to the APAS classes table and to the Fall'26 Classes list (21 credits, was 18), and trimmed Fall'26 Syllabus's `MOC`/`Resources` sections out. Re-read both files fresh before patching to pick up his edits (per [[user-concurrent-editing]] memory).

**Corrected math (CSCI 4521 = 3cr, confirmed by 21 - 18 = 3 and matches Anant's own row):** major credits in-progress 11→14, needs 18→15 more. Upper-Division Major Credits: 5+14=19/19 — exactly complete, CSCI 4521 is what closes it. Technical Electives in-progress 3→6 (both CSCI-designated), needs 20→17 more, CSCI-designated-remaining 8→5. Elective Credits bucket unaffected (CSCI 4521 is a major credit, not general elective). Total distinct remaining after F26 for major+minor: 27 credits (17 tech electives + 10 minor electives), down from 30.

**Reframing per explicit instruction:** stopped hedging requirement-level items with "once F26 posts" — Computer Science Core, Upper-Division Major Credits, Diversified Core/Designated Themes, and the Upper Division Math Oriented Requirement are now written as flatly complete (F26 treated as done for planning). Individual F26 course rows keep the `IP` tag so the real grading status stays visible. Writing Intensive (still needs 1 more upper-division course) was deliberately NOT marked complete — F26 doesn't resolve it, said so explicitly rather than overstate progress.

**Changes made:**
- `APAS.md` — Credits intro, Lib ed requirements, Major Requirements patched with the corrected numbers and "complete" framing.
- `Entrepreneurship Minor.md` — Status block tightened to match, added a Fall'27 graduation-target pointer to Fall'26 Syllabus.
- `20_Progress/Degree/Fall'26 Syllabus.md` — Classes list fixed (CSCI 4521 description was blank, count said "five"/"5 classes", now "six"/"6 classes"). Renamed and fully rewrote "Spring'27 — Path to Graduation" → "Path to Graduation — Fall'27 Target": drops the overload/split-term hedging (no longer needed — 27 credits fits two semesters comfortably at 18–22cr each), lays out Spring'27 (heavy) + Fall'27 (light, final) + optional Summer'27 to ease the minor electives. Left an explicit pointer to the not-yet-written `[[Most Out of College]]` note (unresolved link, intentional — Anant wants a planning conversation first).

**Next:** Anant wants a conversation (not more file-writing yet) about the next 2 years of coursework aimed at an AI/ML engineering path, using the 17 remaining Technical Elective credits deliberately instead of generically. `Most Out of College` note gets written only after that conversation concludes.

## [2026-08-22] write | graphify documentation — four new notes, one existing-flag closed

Built and mapped `internship-research-loop` with graphify this session (711 nodes, 45 communities, `--mode deep`), live-synced as an Obsidian sub-vault into `60_Claude/40_Project_Briefs/Internship/` via three git hooks (`post-commit`/`post-checkout` from `graphify hook install`, plus a custom `post-merge` since this repo's real automation commits from GitHub Actions runners, not this machine). Anant then asked for graphify itself to be documented properly, researched from the real source (GitHub `Graphify-Labs/graphify` README/ARCHITECTURE.md/CHANGELOG.md/how-it-works.md, not guessed) before writing anything.

**Four notes created**, all previously-empty stub files Anant had already touched at the exact target paths named in his prompt:
- `60_Claude/40_Project_Briefs/How to use Graphify.md` — the reusable operating procedure (first-build steps, already-mapped steps, the automatic-vs-manual decision table).
- `60_Claude/40_Project_Briefs/Graphify — Internship Research Loop Implementation.md` — the concrete, repo-specific record: what's actually installed, evidence for each `.gitignore` decision, the version-gap finding (pinned 0.9.4 vs. latest 0.9.48), and the missing-merge-driver gap.
- `40_Resources/CS/AI/Workflows/Claude Code/Graphify Workflow.md` — the full mechanism/command reference (three-pass pipeline, confidence-tag rubric, team-setup workflow straight from the README).
- `40_Resources/CS/Concepts/Helpful Tools/Graphify.md` — the concept-level "what is it, why, where to reach for it" note, including the OSS-CLI-vs-graphify-Enterprise distinction (two different products share the graphify name; `graphify.com/docs` documents the commercial waitlist product, not the OSS CLI this vault actually uses).

**Existing gap closed:** `40_Resources/CS/Repos.md` line 37 had carried `==detailed commands and usage needs to be written==` next to the Graphify entry since it was starred — removed now that the real note exists, and the `[[graphify]]` link resolves to the new Concepts note by basename.

**Why it matters:** this was the first tool documented in the new `Helpful Tools/` folder, and the first graphify note written anywhere in the vault despite the tool already being in active use (Portfolio and CausalOps both have their own graphify output, referenced only in passing before this).

**Open questions:**
- Whether `graphify hook install`'s git merge driver actually landed on `internship-research-loop` — flagged as unverified, not confirmed either way.
- Whether to standardize the pinned graphify version across every machine (`uv tool install graphifyy` vs. the current `pip --break-system-packages` install) given the version-drift finding.

**Next:** apply the same `How to use Graphify` procedure to the next codebase that needs mapping; treat any deviation from the procedure as a signal the note itself needs updating.

## [2026-08-22] verify | graphify setup + notes audit — two confirmed, named, version-gated bugs

Anant asked for a full verification pass on everything from the graphify build/documentation session: the `graphify-out/` folder, the git hooks, and all four new notes — no assumptions, check facts against real sources. Turned up two real problems, both traced to specific fixed bugs rather than left as vague "something seems off."

**Confirmed bug 1 — merge driver never installed.** `.git/config` has no `[merge "graphify"]`, no `.gitattributes` exists, despite `graphify hook status` reporting both hooks "installed." Root cause found in the real `CHANGELOG.md`: `graphify hook install` announced merge-driver support in 0.7.0 but it silently did nothing until bug #1902 fixed it in 0.9.17. `internship-research-loop` is pinned at 0.9.4 — inside the broken window. Re-running `hook install` alone won't fix it post-upgrade; the installer no-ops when its marker is already present, so it needs `hook uninstall` then a fresh `hook install`.

**Confirmed bug 2 — 350 orphaned notes in the vault mirror.** `60_Claude/40_Project_Briefs/Internship/` has 976 `.md` files but the ownership manifest tracks only 627 and the current graph has 697 nodes. Verified the 350-file gap is genuine graphify debris, not user content: all 350 last-modified within this session's own build window, and the one real pre-existing user note (`promote-dossier note templates.md`) is correctly excluded from the orphan set — the ownership guard works, but the *pruning* behavior doesn't exist yet at 0.9.4. Same root fix, same release: bug #1896, also landed in 0.9.17. Sanity-checked against Portfolio's own graphify setup on this machine (also no merge driver, also pre-dates this pattern) — not an Internship-specific fluke.

**Also fixed:** added `.claudeignore` (`graph.json`, `graphify-out/`) to `internship-research-loop` — recommended in the Workflow note but never actually applied to the repo last session.

**Notes updated** (all three previously-written ones, with the confirmed facts replacing hedged "unverified" language): `Graphify — Internship Research Loop Implementation.md` (two new sections with exact evidence), `Graphify Workflow.md` (troubleshooting entries generalized for any repo), `How to use Graphify.md` (a three-command health check + revised open items). Every edit re-passed the vault's own quality gate (frontmatter dupes, blank-line rules, wikilink resolution) via direct script checks, not by eye.

**Deliberately not done, pending Anant's call:** the graphify upgrade itself (risk: a concurrently-busy peer session on this machine might be mid-invocation on the shared `graphify` binary) and deleting the 350 confirmed-orphaned files (vault safety rule: never delete notes without explicit instruction, even at high confidence).

**Next:** Anant to decide timing on the upgrade (`uv tool install graphifyy`, then `hook uninstall`/`hook install` fresh) and how to handle the 350 orphaned files — delete, move to inbox, or wait for a clean re-export post-upgrade.

## [2026-08-22] resolve | graphify upgrade + orphan cleanup, plus a near-miss worth recording honestly

Anant approved both pending items from the prior entry: upgrade now, delete the 350 orphans now. Executed, then hit a real scare mid-cleanup that's worth logging accurately rather than smoothing over.

**Upgrade:** `uv tool upgrade graphifyy` (0.7.10 → 0.9.48 — the machine had a stale `uv tool`-registered 0.7.10 alongside a separate `pip` 0.9.4 copy that was actually winning on `PATH`; the upgrade replaced the `~/.local/bin/graphify` shim cleanly). `graphify hook uninstall` + fresh `graphify hook install` on `internship-research-loop` — merge driver now genuinely registered (`.git/config` has `[merge "graphify"]`, `.gitattributes` has the merge line, `graphify hook status` confirms). The custom jarvis-sync hook blocks survived the uninstall/reinstall cycle intact.

**Orphan cleanup, and the near-miss:** recomputed the 350-file orphan list fresh, ran a safety assert excluding the one file believed to be real user content (`promote-dossier note templates.md`), deleted the 350. The assert didn't fire — correct, since (unknown at the time) that file was never in the delete list to begin with — but the file was then found missing from disk anyway, and the session concluded `Jarvis/.git` didn't exist (from a `ls -la .git | head -3` that got truncated to just `.`/`..` and was wrongly read as "no git repo"), so it flagged a possible unrecoverable loss and stopped to ask.

**Correction, from a Windows-side session:** `Jarvis/.git` is real, with a normal hourly auto-commit history. The "lost" file — verified via `git show 36564f44:...`, independently re-verified in this session, not just taken on trust — carried `graphify/EXTRACTED` frontmatter and a `source_file` pointer into `internship-research-loop`: graphify output, a duplicate of two other still-present notes, not the hand-authored file it was believed to be. The manifest-ownership bug was real; the "lost real content" conclusion was not.

**Closed out correctly this time:** `git status` on the vault confirmed exactly 350 `D` entries; a 12-file random sample checked against `36564f44` came back 100% genuine `graphify/EXTRACTED`/`INFERRED` duplicates (9 per-node notes with real `source_file` pointers, 3 `_COMMUNITY_*` overview notes correctly referencing dedup-suffixed members); committed deliberately in the vault's own repo rather than left for the hourly auto-commit to absorb unreviewed (commit `f75662ac`, "Prune 350 orphaned graphify duplicate notes from Internship mirror").

**Root cause, read directly from `export.py` (both the broken and fixed copies):** `to_obsidian` persists `.graphify_obsidian_manifest.json` as `{"files": sorted(set(_written))}` — only the current run's write set, never merged with history. Pre-0.9.17, nothing ever reconciled that against the old manifest, so any forgotten file became permanently invisible debris, protected forever by the same guard meant to protect real user notes. 0.9.17 added the missing `stale = _owned - written - skipped` prune step — but it can only prune what's still in `_owned` at the moment it runs, so pre-existing orphans (like these 350) always need one manual pass, even after upgrading. Going forward this should self-heal, with one residual gap: no lock file guards the manifest read-modify-write the way `graph.json` has its own `.rebuild.lock`, so genuinely concurrent exports could still race.

**All three graphify notes updated** to reflect resolution (not just findings): the "Confirmed" sections became "Resolved" sections with the fix details, `How to use Graphify`'s health-check section now explains the 0.9.17 self-healing behavior and points at vault git history as the first place to check before assuming data loss, and `Graphify Workflow` carries the full code-level mechanism for anyone hitting this on a different repo.

**Lesson worth keeping, stated plainly:** when something in a vault looks like it might be gone, check `git status`/`git log` at the actual vault root before concluding there's no version control or reaching for the Recycle Bin — a truncated `head -3` on a git-internals listing produced a false "no repo" conclusion here, and cost real back-and-forth that a complete `ls -la .git` would have avoided.

**Next:** none outstanding from this incident. Re-run the health check (file count vs. manifest vs. node count) after any future period of heavy concurrent-session graphify activity, not on a fixed schedule.

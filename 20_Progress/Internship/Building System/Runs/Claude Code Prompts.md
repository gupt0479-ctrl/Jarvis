---
type: project
status: active
created: 2026-07-26
updated: 2026-07-26
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
tags:
  - internship
  - automation
  - prompts
next: Run Prompt 1 and Prompt 2 against gupta-builds/internship-research-loop, then wipe this file and write the next batch.
---
# Claude Code Prompts — Internship Research Loop
==This file holds the next batch of prompts to run against `gupta-builds/internship-research-loop`, and only that — it gets wiped and rewritten every build cycle, not accumulated.== When a batch finishes, delete everything below this line and write the next batch fresh, based on whatever the last run actually revealed. Don't carry stale prompts forward.
## Prompting Guide In Use
[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) — the model-specific guide this batch was written against. Key points actually applied below:
- **Literal, doesn't generalize.** Scope stated explicitly per item ("every source," "all six `_matches_*` functions") rather than implied.
- **Front-load everything in the first turn.** These prompts run as a fresh session with no memory of the design conversation that produced them — every decision, file path, and piece of current-code context needed is included inline, not referenced back to a discussion the agent can't see.
- **Effort:** run both prompts at `xhigh` — coding/agentic tasks against a real repo with a real test suite are exactly the case the guide calls out for it.
- **Coverage over filtering** on the review/verification steps each prompt ends with — list what was actually checked and what broke, don't silently self-filter into a summary.
## Prompt 1 — Persona And Timing Config
```
You are working in gupta-builds/internship-research-loop, a GitHub Actions pipeline that discovers internships and writes screened matches as dossier notes into a separate Obsidian vault (gupta-builds/Jarvis). Layer 2 (core/profile.yaml + core/filter.py) is a deterministic, no-LLM eligibility filter — every rule in it is built from live feed data, cited in a comment, never guessed. This task updates that layer to reflect the actual candidate persona, not the generic "rising junior SWE" framing it currently carries.

Candidate: Anant Gupta, CS undergrad at the University of Minnesota, grad Spring 2028 (rising junior — profile.yaml already has grad_year: 2028, unchanged). Direction: a systems-minded AI engineer — full-stack product engineering combined with observability and applied AI/agentic workflows, not code generation for its own sake. Real evidence of this direction: a Rust/Python event-ingestion middleware for an astronomical alert broker (research role under a UMN professor), a RAG/pgvector-backed learning platform, an agentic system with hardened security (rate limiting, HMAC cookie auth) on his own portfolio site, and a second ML research role doing behavioral-pattern discovery under another UMN professor.

Make these changes to core/profile.yaml:

1. Add "Spring 2027" to `terms`. It is wanted but explicitly lower priority than Summer 2027 and Winter 2027 (which are equally high priority) — encode this as a weight, e.g. a new `terms_weight: {"Summer 2027": "high", "Winter 2027": "high", "Spring 2027": "low"}` mapping, not a second pass/fail gate. Every existing term-matching function in core/filter.py (_matches_simplify, _matches_josegael, _matches_vanshb03, _matches_zshah101, _matches_free_text_source — used by both Greenhouse and Ashby) must be updated consistently so all six sources honor the new term and the weight is available to be read downstream (a later, separate task will use the weight for priority tagging — this task only needs to make it correctly present and correctly matched, not consumed yet).
2. Before writing any category/opportunity-type logic, fetch live data from all six sources' actual current feeds (SimplifyJobs, Jose-Gael-Cruz-Lopez, vanshb03, zshah101, plus spot-check a few live Greenhouse/Ashby company boards) and check whether any of them carry fellowship, mentorship, or standalone-research-shaped entries distinct from internship/co-op postings. If real examples exist, extend matching to include them, citing the real entries found, in a code comment, exactly like every existing rule in this file. If no real examples exist on live data right now, do not invent speculative matching logic — state that finding in your final summary instead and leave this for a future pass once real data exists.
3. Add an explicit comment in profile.yaml stating that pay is never a filter criterion anywhere in this pipeline (confirm this is still true by grepping for any pay_per_week gate in core/filter.py — there shouldn't be one — and note the grep result in your summary).
4. Do not modify degrees_allow, locations_allow, or the OPT-exclusion logic in ingestion/posting_page.py — those are eligibility mechanics unrelated to this persona update.

Update tests/test_filter.py with new fixture-based tests (no live network calls in the test suite, matching the existing pattern) covering: Spring 2027 matching at low weight across all six sources' matching functions, and the terms_weight field being read correctly.

Run the full test suite before finishing and report the pass count (e.g. "173/173"), not just "tests pass." If anything fails, fix it before reporting done — do not report success with failing tests.
```
## Prompt 2 — Priority Classification, CS-Relevance Gate, Dossier Template, Contact Research
```
You are working in gupta-builds/internship-research-loop (see Prompt 1 above for the pipeline's overall shape if you need it — this prompt is self-contained regardless). Current state, verified directly against the live repo before writing this: six sources feed the pipeline (SimplifyJobs, Jose-Gael-Cruz-Lopez, vanshb03, zshah101, Greenhouse, Ashby — see ingestion/sources.py, ingestion/normalize.py, core/filter.py). Three of the six (vanshb03, Greenhouse, Ashby) carry no structured `category` field on their Listing objects — Greenhouse and Ashby route through `_matches_free_text_source` in core/filter.py, matching on `listing.title` + `listing.raw_text` only. GREENHOUSE_COMPANIES and ASHBY_COMPANIES in ingestion/sources.py are hand-seeded token dicts — currently Greenhouse's seed list (fccincinnati, aquaticcapitalmanagement, walleyecapital-external-students, pdtpartners, virtu, mwinternshipprogram, optiverus) is entirely quant/prop-trading firms, and Ashby's (ellipsislabs, quadrillion-labs, circleback, ctgt, pylon-labs) is the only AI-adjacent seed set. This is real, decided design work from a planning session — implement it, do not re-derive or question the decisions below.

## Task A — CS/software-relevance gate (new hard rule, rejects at write time)
A listing must be genuinely Computer Science / software engineering at its core to be written as a dossier at all — this is a new required check alongside the existing OPT/US-location/degree checks, not a priority-tier distinction. Adjacent fields (hardware, robotics, astrophysics, space, embedded/firmware) are not automatically excluded — they pass this gate only if the specific posting's actual content shows real software/CS relevance the candidate is suited for, per the persona in Prompt 1 (reference Main Resume.md's skills/bullets and Engineer Edge Roadmap.md's stated direction — both live in the Jarvis vault at 20_Progress/Internship/Resumes/Main Resume.md and 10_Areas/Career/Engineer Edge Roadmap.md respectively; read them for the real bar before writing keyword rules, don't guess at what counts as "suitable"). Non-software roles (financial/risk analyst, tax, sports performance analytics, pure hardware-manufacturing roles with no software component) fail this gate outright and must not be written anywhere, including the Other bucket in Task B. Implement as a new deterministic function in core/filter.py (or a new core/priority.py module if that's architecturally cleaner — your call, but keep it consistent with this file's existing zero-LLM, keyword/heuristic style), called after the existing matches() checks pass, before the write gate. Add fixture-based tests using real dossier content already in the vault as source material (see Task D for where actual current dossiers live) — do not write synthetic test data if a real example already demonstrates the case.

## Task B — Priority classification (deterministic, runs only on listings that passed Task A)
Classify into exactly one bucket, based on title + category (where present) + fetched posting content:
- AI/ML — LLM, RAG, agents, ML infrastructure, applied AI, deep learning signals
- Fullstack — product/frontend/backend/systems engineering signals
- CyS & Finance — security or finance-adjacent software engineering signals
- Other — genuine software engineering (already confirmed real by Task A) that matches none of the above three

Each classified dossier gets a short callout stating which real signal(s) from the posting drove the classification — do not include a numeric label like "Priority 1/2/3" anywhere in the visible note; the folder location alone encodes the category, a number in the callout text is redundant and was explicitly rejected in design review.

## Task C — Route into vault subfolders
Write each classified dossier into the matching existing subfolder under 10_Areas/Career/Internships/List/Dossiers/ in the Jarvis vault: "1 - AI & ML/", "2 - Fullstack/", "3 - CyS & Finance/", or "Other/" (exact names, spaces and all — verify by listing the actual folder before writing). These folders exist and are currently empty. Do not write into or otherwise touch the "Viewed/" sibling folder — that folder's role is separate from this pipeline (a human triage bin, not a write target for this codebase).

## Task D — Dossier template and identity fixes (vault_writer/writer.py, vault_writer/templates/dossier.md.j2, core/identity.py)
Verified directly against a real hand-edited example the candidate wrote (10_Areas/Career/Internships/List/Dossiers/Software Engineer - Ellipsis Labs.md in the Jarvis vault — read it directly for the exact target shape before implementing):
1. Convert `date_posted` from a raw Unix epoch integer to a real ISO date string at write time.
2. Drop `uid` and `category` from the rendered frontmatter entirely. Keep the raw uid available internally for dedup against state/seen_ids.json without exposing it in the note body or frontmatter.
3. Replace the `promoted:` frontmatter field with `next:` (empty by default), matching every other note type's convention across the Jarvis vault.
4. Change the filename convention to "[Role] - [Company].md". Sanitize filesystem-illegal characters (slashes, colons, quotes — company names with parenthetical aliases like `Fussball Club Cincinnati LLC ("FC Cincinnati")` need real handling, don't just crash or silently truncate). Add a collision tie-breaker for same-role-same-company duplicates (append a short disambiguating suffix rather than overwriting or erroring).
5. Change the header to `# {{ title }}` only — drop the current template's `# {{ company }} — {{ title }}` (company is already in the filename and frontmatter, the current header is redundant).
6. Rewrite the auto-generated intro sentence ("Auto-discovered {{date}} from {{source}}. Posting content below fetched at discovery...") to state something with real information plainly, without templated filler — this vault has a standing rule against generic AI-sounding boilerplate prose (see HUMAN_WRITING.md if you want the actual standard) and the current phrasing was flagged against it directly.
7. Real bug, not a template gap: the Ellipsis Labs example shows an Ashby-sourced posting where the actual job-description prose never made it into the fetched content — only the Qualifications section came through, leaving the Description section genuinely empty. Investigate ingestion/posting_page.py's handling of Ashby-hosted pages specifically (JS-rendered content may need an explicit wait condition on the fetch) and fix the underlying extraction, not by adding a fallback placeholder.

## Task E — Contact-research widening (enrich.py, Layer 5 — stays promotion-triggered only, never called automatically from run_pipeline.py, unchanged)
Add a scoped Firecrawl search step (search, not scrape) per company: queries for "[company] recruiter" and "[company] university recruiting", in addition to the existing GitHub-org-member and engineering-blog-byline discovery already in enrich.py. Explicitly exclude these domains from counting as a valid hit even if returned: Indeed, Glassdoor, SimplifyJobs, and any linkedin.com/jobs/ URL. Separately, add a narrowly-scoped LinkedIn search-snippet lookup: a Firecrawl search (never a fetch or scrape of the actual linkedin.com URL) for site:linkedin.com plus the company name and a recruiting-related term, surfacing only whatever text the search result snippet itself contains (typically a name and title). Do not fetch, scrape, or otherwise load the underlying LinkedIn page at any point in this flow — that would cross this pipeline's standing rule against login-wall automation, which stays in force unchanged. State this ceiling in a code comment so a future session doesn't try to extend past it.

## Task F (optional, flag as optional in your summary, do only if time allows after A-E are done and tested) — Seed list diversification
ASHBY_COMPANIES and GREENHOUSE_COMPANIES in ingestion/sources.py are hand-seeded and currently skew heavily toward quant/prop-trading (7 of 12 total seeded companies). Research and add a handful of real, verified-live Ashby or Greenhouse boards for companies actually doing AI/ML or applied AI work, using the same verification standard already documented in the existing comment above GREENHOUSE_COMPANIES (never add a token that hasn't been confirmed live against real job data — a wrong guess silently returns zero jobs, not an error).

## Verification, all tasks
Run the full test suite and report the exact pass count before declaring anything done. Report every task's outcome individually (A through E, plus F if attempted) rather than one combined summary — if something was skipped or only partially done, say so plainly rather than folding it into an "overall done" statement.
```
## Prompt 3 — Skills, Agents, And Claude Settings For The Loop Repo
```
You are setting up gupta-builds/internship-research-loop's own .claude/ tooling — skills, agents, and settings scoped to this repo, separate from and not to be confused with the Jarvis vault's own .claude/ setup (a different, unrelated piece of work). This prompt assumes Prompt 1 and Prompt 2 (persona config, priority classification, dossier template fixes, contact-research widening) have already run — if core/priority.py, the four vault subfolders, or the widened enrich.py don't exist yet, stop and say so rather than building on top of an assumption.

## Real architectural constraint, resolve explicitly, don't silently assume
The promotion skill below (Task A) needs to read a dossier note and write three new notes — all of which live in the Jarvis vault (a separate GitHub repo, gupta-builds/Jarvis), not in this repo. This repo's own automation never touches the vault interactively (run_pipeline.py writes once, non-interactively, via a scoped PAT). A human-in-the-loop skill is a different shape: it needs a Claude Code session with both this repo and the Jarvis vault present in the same working environment. State this prerequisite plainly in the skill's own instructions file (a session invoking /promote-dossier needs the Jarvis vault checked out locally, sibling to or alongside this repo — document the expected layout, don't assume it silently). Do not attempt to make the skill write across repos via the GitHub API instead — that reintroduces exactly the push-race/token-scope complexity core/git_ops.py already exists to solve for the one automated writer this pipeline has; a second interactive writer using a different mechanism is a real design smell, flag it rather than build around it if you hit this.

## Task A — The promote-dossier skill
Build a Claude Code skill (.claude/skills/promote-dossier/ in this repo, following the standard SKILL.md + reference file pattern) that turns one dossier into a Program note + Contacts/Each One note + Tracker/Each One note, with manual consent at the write step — never auto-writing silently. Behavior, in order:
1. Take a dossier file path (or company/title) as input.
2. Ask two small, concrete questions, not open-ended ones: (a) target folder — Programs/Serious/ or Programs/Considering/; (b) does the dossier's auto-assigned priority/category still hold, or does it need a human override? Offer the current auto-assigned value as the default answer, don't force retyping it.
3. Invoke contact research (this repo's enrich.py, as widened in Prompt 2 Task E) and show the human what was found — company info, any contacts, any LinkedIn search-snippet hits — before writing anything.
4. On explicit go-ahead only, write all three notes together, cross-linked (program field on Applying-adjacent notes, applying_note-equivalent links, etc. — match the existing cross-linking convention documented in 30_Order/Workflows/Internship Pipeline.md in the Jarvis vault; read that file directly for the exact field names before writing the templates below, don't invent new ones).
Write strict, enforced templates for all three note types (Program, Contacts/Each One, Tracker/Each One) as part of this task — not loose prose guidance. Each template's required frontmatter fields and the rule that they must always be present go into this repo's own CLAUDE.md so any future Claude Code session working in this repo (or the paired vault session) knows the contract without re-deriving it.

## Task B — contact-researcher subagent
The contact-pulling step in Task A above is exploratory, not deterministic (unlike everything else in this pipeline) — it's better modeled as a subagent the skill invokes than as a rigid script. Build a Claude Code agent (.claude/agents/contact-researcher.md) whose only job is: given a company name and the widened Firecrawl search scope from Prompt 2 Task E, return whatever real contact signal exists (recruiter, HR, engineering-blog byline, GitHub org member, LinkedIn search-snippet hit) with a source cited for each — never fabricate a plausible-sounding contact, report "nothing found" honestly when that's the real outcome; a wrong guess here is worse than an empty result, same principle as every filter rule in core/filter.py.

## Task C — loop-verifier agent
Build a Claude Code agent (.claude/agents/loop-verifier.md) that can be launched standalone to check the whole pipeline's actual live health in one pass: full test suite pass count, the last N scheduled run.yml / recheck.yml results via gh api, current dossier counts per priority subfolder in the vault against what run logs claim was written, whether seen_ids.json and the vault's actual dossier files have diverged, and whether any GitHub issues have been auto-filed. This is the automated version of the manual audits already run twice in this project's history (2026-07-19, 2026-07-25) — model its output the same way: a dated, evidence-cited verdict, not a vague "looks fine."

## Task D — Code-review skill/agent for this repo
Add a repo-scoped code-review setup: either a .claude/skills/review-loop-change/ skill or a .claude/agents/loop-reviewer.md agent (pick whichever fits this repo's actual size and change frequency better — this is a ~1,500-line repo with a ~1:1 test ratio, not a large codebase, say which you picked and why). It should check any proposed change against this repo's own established conventions before it ships: the zero-LLM-in-the-unattended-path rule, the permissive-by-default / explicit-negative-signal filter design, the fail-closed write-gate ordering, and the requirement that every new rule cites the real live data it was built from in a comment.

## Task E — .claude/settings.json for this repo
Tune permissions for what this repo's actual workflow needs: pytest runs, git operations short of force-push, gh CLI read operations (api, run list, issue list) without prompting every time, and explicit confirmation still required for anything that pushes to origin/master or modifies GitHub Actions secrets. Document in this repo's CLAUDE.md what each skill/agent above is for and when to reach for it instead of writing more Python by hand — the actual question to answer here is which of this repo's remaining manual toil (contact research, promotion, verification, review) is genuinely better solved by an agent than by more deterministic code, and say so explicitly rather than defaulting to "write a script" out of habit.

## Verification
Report each task's outcome individually. For Task A specifically, state clearly whether the skill was tested against a real dossier end-to-end (up to but not including the final write-consent step, which requires a human) or only reviewed for correctness — don't claim it works if it was never actually run.
```

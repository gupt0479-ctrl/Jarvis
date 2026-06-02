# Session Log

Append-only record of Claude sessions. Format: `## [YYYY-MM-DD] action | Title`

---

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
- [[log]]
- [[40_Resources/Obsidian/Vault Operating System]]

## [2026-04-24] plan | Jarvis multi-agent PKM plan

Created a project brief for turning Jarvis into a multi-agent second-brain system without flooding the vault with raw AI output.

**Created:**
- [[60_Claude/40_Project_Briefs/Jarvis Multi-Agent PKM Plan]]

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
- [[60_Claude/50_Reviews/Ops Reports/Jarvis Ops Report - 2026-04-24 20260424-170132]]

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
- [[60_Claude/50_Reviews/Jarvis Enrichment Phase 1 - 2026-04-24]]

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
- [[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]

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

Updated [[CSCI 2041 Note Production Plan]] as a source map only. Mapped lecture transcripts, professor note folders, labs, projects, practice files, and Hickey textbook sections to likely weeks from [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 6]] through final review. Did not modify [[10_Areas/UMN/Previous Classes/Lib Ed/MUS 1013/Week - 1]] through [[10_Areas/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]].

**Direction:** start note production at [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 6]] using the plan's source rows, and verify the marked transcript/date uncertainties before drafting.

## [2026-05-08] rewrite | CSCI 2041 production contract

Rewrote [[CSCI 2041 Note Production Plan]] into a stricter note-production contract. Added source-of-truth rules that limit factual claims to the local CSCI 2041 source folder, a very detailed content standard, concept-note primacy, exact source coverage requirements, a professor-note page ledger, week-by-week production details from [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 6]] through final review, and stronger lab/project/concept backlink rules.

**Direction:** future CSCI 2041 note creation should treat concept notes as the durable source-of-truth layer and read every listed source file/page before drafting.

## [2026-05-08] build | CSCI 2041 Week 6-15 archive notes

Created weekly notes [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 6]] through [[Week - 15]] under `50_Archive/UMN/Classes/CSCI 2041`, plus [[CSCI 2041 Board]] in that archive folder. Notes synthesize the source-map transcripts, professor note folders, labs/projects/practice files, and Hickey textbook anchors. [[10_Areas/UMN/Previous Classes/Lib Ed/MUS 1013/Week - 1]] through [[10_Areas/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]] were not edited.

**Direction:** next pass should create the linked concept/lab/project notes, then strengthen backlinks from weekly notes to concrete concept headings.

## [2026-05-08] build | CSCI 2041 Week 6+ concept notes

Created 24 source-grounded concept notes under `50_Archive/UMN/Classes/CSCI 2041/Concepts` for the Week 6 onward material: streams, laziness, memoization, mutation, modules, ADTs, higher-order functions, recursion patterns, Project 1 expression solving, Lisp representation, scanner/parser/printer/evaluator architecture, environments/closures, primitives/special forms, REPL integration, continuations, if-normalized tautology checking, macros, association lists, and error boundaries.

**Updated:** [[CSCI 2041 Board]] now links the concept layer. [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 6]] through [[Week - 15]] now point at the actual concept note names for the created OCaml concepts. [[10_Areas/UMN/Previous Classes/Lib Ed/MUS 1013/Week - 1]] through [[10_Areas/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]] were not edited.

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

Improved [[10_Areas/UMN/Previous Classes/Lib Ed/MUS 1013/Week - 1]] through [[10_Areas/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]] in the live `10_Areas/Degree/UMN/Classes/CSCI 2041` folder. Filled empty or placeholder weekly sections with concrete skills, textbook anchors, concept links, representative examples, takeaways, and flashcards. Kept the existing lecture bodies intact and strengthened lab connections for Lab 1 through Lab 4. Also updated [[CSCI 2041 Board]] so the Weekly Notes index includes Week 1 through Week 15.

**Audit notes:** remaining cleanup targets are concept-level: [[OCaml - Polymorphism]] and [[OCaml - Tautology Problems]] are still template shells; [[OCaml]] contains leftover MOC/template bullets; several concept notes still link to non-existent standalone lab notes like `[[Lab - 8 Association Module]]` even though labs currently live as weekly anchors.

## [2026-05-11] update | CSCI 2041 Week 5 lecture spine

Reworked the [[10_Areas/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]] lecture section without deleting the existing lecture notes. Added a lecture map, source/concept anchors, a cleaned code spine for reduce, CPS, tautology checking, and Lab 4 permutations, plus a short "what to retain" guide before the detailed Feb 16/18/20 notes.

**Direction:** next refinement pass should consolidate the concept layer into a smaller canonical set, keeping source-grounded material from the existing concept notes while replacing standalone lab-note links with weekly lab anchors.

## [2026-05-12] update | CSCI 2041 weekly lecture source spines

Enhanced the live `10_Areas/Degree/UMN/Classes/CSCI 2041` weekly notes with explicit source-grounded lecture maps. Added new lecture-map sections to [[10_Areas/UMN/Previous Classes/Lib Ed/MUS 1013/Week - 1]] through [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 4]] and [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 6]] through [[Week - 15]], preserving the existing lecture bodies; [[10_Areas/UMN/Previous Classes/Lib Ed/BIOL 1012/Week - 5]] already had the fuller lecture spine from the prior pass. The maps connect transcript numbers/dates, professor-note folders, labs/projects/practice files, and the core mechanism for each week. Also expanded the dated lecture headings in [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 6]] through [[Week - 15]] with professor-transcript details about announcements, source-file mechanics, control-flow invariants, and final-exam distinctions.

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
- [[40_Resources/Obsidian/Claude Pro Workflow]]
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
- [[60_Claude/40_Project_Briefs/Claude Optimization Master Setup]]

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
- [[60_Claude/40_Project_Briefs/Claude Optimization Master Setup]]

**Next:** Install mattpocock/skills, create conversation capture folders, run `/ops morning-start` every session.

## [2026-05-28] setup | Weekly Review System — Cowork Scheduled Task

Built the full weekly review infrastructure for Jarvis.

**Created:**
- `.claude/skills/weekly-review.md` — replaced the shallow original with a three-month-plan-aware version; includes pre-flight reads, milestone audit table for all 12 weeks, enrichment health checks, orphan/link scanning, session log analysis, exact output format with HUMAN_WRITING rules, and execution notes for future cold-start Claude
- [[60_Claude/50_Reviews/Weekly Synthesis/Weekly Synthesis — 2026-W22]] — first plan-aware review; documents the W22 infrastructure wins and quantifies the 4-week build spine gap
- Cowork scheduled task `jarvis-weekly-review` — runs every Monday at 9:00 AM; prompt is fully self-contained with orientation steps and vault safety rules

**Updated:**
- [[60_Claude/50_Reviews/Weekly Synthesis/Weekly Synthesis Index]] — added Review History table

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
- [[60_Claude/40_Project_Briefs/Vault-Audit-2026-05-29]] — spine health, instruction-file table with quality scores, conflicts/contradictions list, missing files list, 3-month roadmap (May 29 → Sept 1, with monthly themes Foundation/MCP Hub → Brain → Research Engine), MCP hub gap analysis per external tool. Includes orientation message at top for future cold-start Claude.
- [[40_Resources/Obsidian/MCP-Hub-Index]] — single-page orientation note for any external agent. Folder map, naming conventions, what NOT to touch, how to navigate, what the vault is building toward Sept 1.
- [[60_Claude/05_Clippings/AI Conversations/README]] — raw conversation archive folder, immutable, frontmatter schema. **Unblocks Master Plan Week 2 deliverable (5+ weeks overdue).**
- [[60_Claude/07_AI_Information/AI Conversations/README]] — distilled conversation summary folder with workflow + summary shape.
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

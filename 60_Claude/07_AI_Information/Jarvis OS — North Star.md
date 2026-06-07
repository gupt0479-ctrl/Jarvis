---
type: project
status: sprout
created: 2026-06-07
updated: 2026-06-07
tags:
  - "#ai"
  - "#ai-infrastructure"
  - jarvis
  - pkm
  - roadmap
  - north-star
related:
  - "[[AGENTS]]"
  - "[[CLAUDE]]"
  - "[[HUMAN_WRITING]]"
  - "[[AI_CONTEXT]]"
  - "[[Vault Map]]"
  - "[[Vault Rules — Complete AI Ruleset]]"
  - "[[Jarvis Three-Month Research Engine Master Plan]]"
  - "[[Jarvis Multi-Agent PKM Plan]]"
  - "[[Note Writing System — Audit and Roadmap (2026-05-31)]]"
next: Execute Move 1 — collapse the instruction layer per the file audit in Part 4.
---
# Jarvis OS — North Star
This is the single authority for what Jarvis is, why it underperforms today, and exactly how to fix it. It does one job no other file does: it ends the "every file claims to be the authority" problem by being the one file that owns strategy, diagnosis, and the build standard. Everything else points here for the *why* and the *target*, and keeps only its one narrow job.
This is a fix-it document, not a feature plan. Nothing below asks you to build a new capability. Every section names something already in this vault and says how to make it actually work. The rule that governs the whole file: **no new structure until the existing structure runs.**
If you are an AI tool: read this file and [[40_Resources/Obsidian/Jarvis Vault Architecture]] (where notes go) and [[HUMAN_WRITING]] (how prose sounds). Those three are the working set. Everything else is loaded only when the task touches it (see Part 6). Do not read the full instruction stack on every cold start — that habit is the disease this file treats.
## Part 1 — The diagnosis, with evidence
The instinct that produced this rewrite is that Jarvis is under-built. The vault proves the reverse. Jarvis is **over-built and under-converged**: the parts exist, were built faster than they were reconciled, and the unconverged redundancy is what starves the content and confuses the agents.
The proof is concrete and countable.
**Four files each claim to be the authority.** `Vault Rules — Complete AI Ruleset` opens "This is the governing specification for all AI behavior." `Vault Operating System` opens "This note is the canonical operating contract for Jarvis." `Jarvis Vault Architecture` calls itself "the placement source of truth." `AGENTS.md` carries "the Write Contract." Four documents, four authority claims, one vault. An agent cannot tell which one wins, so it reads all of them.
**Four different cold-start read orders.** `Vault Map`, `AI_CONTEXT`, `Vault Rules`, and `Agent Operating Guide` each prescribe a different sequence of files to read before writing. They overlap but do not match. The agent either picks one arbitrarily or reads the union — which is most of the instruction layer.
**The same rules are restated in five to seven places.** The blank-line rule, the frontmatter field set, the formatting markers (`==`, `**`, `*`), and the plugin-integration rules appear, in near-identical form, in `HUMAN_WRITING`, `Jarvis Writing and Formatting`, `Vault Rules` (Parts 3–8), `Agent Operating Guide`, and `Vault Operating System`. The routing table appears in `AGENTS.md`, `Jarvis Vault Architecture`, and `Vault Operating System`. Roughly ten instruction documents totalling several thousand lines, most of it duplicated.
This produces the four failures you feel, and now they have mechanisms:
**Thin content is a budget problem.** Before an agent writes one character, the read stack consumes a large share of its context window with rules that mostly repeat each other. Anthropic's own framing: the context window is a public good, and every token a document loads competes with everything else the model needs to hold — including the actual thinking about your material. Spend the budget on navigating ten overlapping files and there is little left for substance. "Too many files to read and redirect to" and "we write thin content" are not two complaints. They are one mechanism.
**Agent confusion is a contradiction problem.** When four files claim authority and four read orders disagree, the agent has no deterministic entry point. It guesses. Different sessions guess differently, so output is inconsistent — which reads as "the AI doesn't work the way I want."
**No implementation surface is a write-once problem.** There are three live plans (the 1,641-line research-engine plan, the multi-agent PKM plan, the Claude optimization setup) and no single board that says *this week, these three things*. Plans are write-once; execution needs a write-often surface they feed into. That surface does not exist, so you re-plan instead of execute — visible in the fact that the system has already been formally audited twice (the 2026-05-31 note-writing audit, the Cursor OS-upgrade brief). Re-auditing is the symptom; converging is the cure.
**Nothing runs automatically is a wiring problem, not an absence problem.** The pieces of an automatic loop already exist (see Part 5): hooks in `settings.json`, a `jarvis-cli` with eight health commands, and a `jarvis-memory` MCP server. They are not wired into a loop that runs on a schedule, so Jarvis only moves when you drive it by hand.
## Part 2 — Why there is too much content in the first place
This matters because if you do not fix the cause, the bloat regrows. The cause is a process habit, not a knowledge gap.
**Every audit added a file instead of merging one.** The vault has a strong instinct to document problems — the 2026-05-31 audit is excellent. But each diagnostic became a *new* note (`Vault Rules`, `Agent Operating Guide`, `Vault Map`, `Jarvis Writing and Formatting`, the audit itself) rather than an edit to an existing one. Documentation accreted; it never compacted. Ten files exist because ten problems were each solved by writing, and writing meant adding.
**There is no deletion discipline.** Nothing in the current rules says "when you write rule X, delete the other copy of rule X." So copies multiply. Redundancy was treated as safety ("better to repeat the blank-line rule everywhere") when it is actually cost (every repeat is loaded again, and when two copies drift, the agent cannot tell which is current).
**Planning is more fun than converging.** Designing a nine-subsystem architecture is satisfying; deleting four redundant files and finishing empty templates is not. So the system kept getting wider (more plans, more docs) instead of deeper (the existing plan, executed). This is the real answer to "maybe I lack the knowledge" — you do not. A nine-subsystem plan with acceptance tests and a working SQLite registry is not the output of someone who lacks knowledge. It is the output of someone who has not yet forced themselves to converge. That is a discipline, and this file installs it.
The strict rule that prevents regrowth, stated once and enforced in Part 7: **one fact, one home. No new instruction file without deleting or merging an old one. When you write a rule, delete every other copy and replace it with a pointer.**
## Part 3 — Every stated problem, as its solution
Ordered by leverage. Earlier fixes unblock later ones.
### 3.1 "The instructions are weak / 07_AI_Information is weak" → Collapse to one spine and three references
The layer is not weak in content; it is weak in agreement. Establish a strict hierarchy with zero duplication. **This file** owns strategy, diagnosis, and the build standard. **[[40_Resources/Obsidian/Jarvis Vault Architecture]]** owns where notes go. **[[HUMAN_WRITING]]** owns how prose sounds. **`30_Order/`** owns how each note type is shaped. Everything else becomes a thin pointer or is merged out of existence. The full per-file verdict is Part 4.
### 3.2 "Too many files to read and redirect to → thin content" → Progressive disclosure, enforced
Adopt the pattern Anthropic uses for Skills and that obsidian-mind uses for vaults: load at the granularity the task needs, never more. At cold start an agent loads a lightweight index (names + one-line descriptions) — not the full text of ten docs. It loads a full document only when the task touches it. The mechanism that makes this real is the **context pack** (the multi-agent plan's Layer A, and `jarvis-cli context`): a small task-scoped bundle assembled on demand. Build the context pack and the redirection tax disappears, because redirection stops being something the agent pays up front.
### 3.3 "30_Order has structure but the content isn't rich enough" → Instructive templates with one gold-standard example each
Highest-leverage content fix; the 2026-05-31 audit already specified it precisely. Every template carries four things, not one: exact frontmatter with correct syntax and no invented fields; a one-line description under each heading saying what goes there and how much; a short block of real example content; and the plugin hooks inline (flashcards, Tasks for open questions, math where relevant). Then link one finished **gold-standard note** per template — the thing the agent pattern-matches against. The MGMT 3001 week notes are already that standard; they only need to be referenced. The shells named in the audit (`For Evergreen`, `For Progress`, `Textbook Template`, `Deep Dive Template`, `Concept Template` with its invalid YAML) get fixed first.
### 3.4 "It's a PKM, I want an operating system" → Define the loop; make capture the start of a pipeline
A PKM stores; an OS runs a loop. Jarvis's loop, stated once so every part can serve it: **Capture → Triage → Distill → Connect → Promote → Retrieve → Review.** Raw material lands in `05_Clippings/` or `00_Inbox/`; a triage pass routes it; summaries go to `10_Source_Summaries/`; links tie new knowledge to old; stable knowledge graduates out of `60_Claude/` to `10_Areas/`, `20_Progress/`, `40_Resources/`; the answer engine reads the matured vault; a weekly pass surfaces decay. The "dump everything in" habit is fine — it is the capture stage — but today it has no downstream, so the dump rots. Everything in Part 5 exists to make one stage of this loop run without you pushing it.
### 3.5 "I plan but can't see what to do this week" → One live execution dashboard; plans become feeders
Stop reading plans to find this week's work. Make `00_Dashboard.md` the single surface you open daily — not another plan, a live Dataview/Bases board answering four questions at a glance: the active focus this week, what is in motion (`20_Progress/` notes with a `next:`), what is queued (inbox + clippings awaiting triage), and what is decaying (orphans, stale notes, projects missing a `next:`). obsidian-mind's `Home.md` embedding Base views is the exact model. The three plans become feeders: each plan's current week writes its concrete tasks into the dashboard's source notes; the dashboard renders them. You plan in the plan; you execute from the dashboard.
### 3.6 "Skills, agents, hooks are bland, written like an amateur, no Python" → A real build standard (Part 5)
This is a structure problem and Part 5 is the full fix. In short: the current skills are prose files using `**Description:**`, not spec-compliant `SKILL.md` files with `name:`/`description:` frontmatter; the deterministic work (frontmatter validation, link checks, blank-line linting) is described in paragraphs instead of being code the skill calls. The standard in Part 5 fixes both — canonical file shapes, the procedural-vs-judgment split, and the answer to "do we need Python?" (yes, but only for the fragile, deterministic steps).
### 3.7 "MCP tools come from the vault but there are none for Jarvis" → Wire the server you already built
This premise is false in a useful way: `30_Order/System/jarvis-memory/` is a working MCP server (`server.py`) exposing `jarvis_status`, `jarvis_search`, `jarvis_reindex`, backed by a SQLite schema that already has tables for chunks, embeddings, links/graph, conversations, enrichment_events, and benchmarks. The tools exist; they are a skeleton, and in this session only the generic Obsidian bridges (`jarvis`, `the-plan`) are connected — the custom server is not wired in. The fix is to wire it and grow it along the path its own README documents (chunk index → semantic search → graph → conversation memory → answer engine). Detail in Part 5.4.
### 3.8 "I don't know how to optimize tokens for the vault" → Retrieve, don't dump (Part 6)
Token economy is a design property, not a setting. The whole of Part 6 is the answer: just-in-time retrieval by path, frontmatter as the query surface, the semantic index as the retrieval engine (claude-context measured ~40% token reduction at equal retrieval quality; obsidian-mind keeps session start at ~2K tokens by loading excerpts, not contents), sub-agents that keep heavy reading out of the main window, and tiered loading.
### 3.9 "Nothing runs automatically" → A small, logged automation layer (Part 5.3)
Three tiers, all already partly present. Hooks (wired) enforce invariants at the moment of action. Scheduled tasks run the loop's slow stages on a clock (a morning context assembly, an evening close that logs and refreshes the health dashboard). On-demand pipelines are the `/ops` and skill commands. The rule that keeps automation trustworthy: every automatic action writes a one-line trace to the session log. Automation here means *scheduled and logged*, never hidden.
### 3.10 "Maybe I lack the knowledge" → The blocker is convergence, not knowledge
Put this down. The vault disproves it (Part 2). What is missing is the unglamorous work after the exciting work: collapse redundancy, finish templates, build the one dashboard, run the loop for a few weeks instead of redesigning it. That is a choice to converge, not a skill you lack.
## Part 4 — The instruction-layer audit (what to keep, merge, cut, fix)
This is the concrete "establish what we built, fix it all" pass. Every current AI-instruction file, with a verdict. Execute this as Move 1. The target end state: an agent's cold-start reading is under ~400 lines total, and no rule lives in two files.

| File | Today | Verdict |
| --- | --- | --- |
| `Jarvis OS — North Star` (this) | new | **Authority.** Owns strategy, diagnosis, build standard. Everything points here for *why* / *target*. |
| `40_Resources/Obsidian/Jarvis Vault Architecture` | placement source of truth | **Keep as authority** for *where notes go*. Strip any prose that restates philosophy or formatting; link here instead. |
| `HUMAN_WRITING` | voice standard | **Keep as authority** for *how prose sounds*. Already pointed at this file. Move its `Vault Formatting Rules` block into the formatting authority (below) and leave a pointer. |
| `30_Order/Templates` + `Workflows` | note shaping | **Keep as authority** for *how each note type is shaped*. Finish the shells (Part 3.3). |
| `AGENTS.md` | root contract + routing | **Shrink** to a one-screen contract: golden write rules, routing pointer to Architecture, negative constraints, link here. Delete the duplicated layer descriptions. |
| `CLAUDE.md` | Claude workflow + folder table | **Shrink** to Claude-specific workflow (skills/commands/session protocol). Delete the folder-roles and routing tables that duplicate Architecture. |
| `Vault Map` | read-me-first orientation | **Merge** into one short orientation file. Keep the six-layer table and "never do this"; drop the duplicated read orders. |
| `AI_CONTEXT` | live-context manifest | **Keep but narrow** to the live-state manifest only (dashboard, log, indexes). Remove the canonical-sources list that duplicates this file. Merge target for `Vault Map`'s orientation so the two become *orientation + live state*. |
| `Vault Rules — Complete AI Ruleset` | governing spec (348 lines) | **Demote and split.** Its Parts 3–9 (frontmatter, blank lines, formatting markers, plugin integration, source ingestion) are the real formatting authority — keep that as the single formatting spec. Its Part 1 read order is superseded by this file. Its Part 2 placement duplicates Architecture — cut. Drop the "governing specification for all AI behavior" claim. |
| `Jarvis Writing and Formatting` | Obsidian formatting (445 lines) | **Merge** with Vault Rules Parts 3–9 into one formatting authority. These two are ~80% the same content; there must be exactly one formatting spec, not two. |
| `Agent Operating Guide` | runbook (232 lines) | **Merge** the unique parts (workflow chooser, stop conditions, plugin safety) into the orientation file; cut the duplicated session checklist and content-routing. |
| `40_Resources/Obsidian/Vault Operating System` | "canonical operating contract" | **Demote.** Keep only the canonical property/field schema table (genuinely useful, queryable). Cut the folder logic / workflows / AI agreements that duplicate Architecture and this file. Drop the authority claim. |
| `40_Resources/Obsidian/Claude Pro Workflow` | Pro-plan discipline | **Keep, trim.** The surface-roles and rate-limit content is unique. Cut the context-pack and MCP sections once those live here / in Part 5. |
| `Note Writing System — Audit (2026-05-31)` | post-mortem | **Keep as history.** It is a dated record, not a standing rule. The standing rules it produced live in the formatting authority. |

The single test after this pass: open any two instruction files; if a sentence is true in both, one copy is wrong and gets deleted in favor of a pointer.
## Part 5 — The build standard for skills, agents, hooks, and MCP
This is the engineering spec the current `.claude/` layer is missing. It is grounded in Anthropic's official Skill and subagent guidance and in the repos you flagged (obsidian-mind, autoresearch, CPR, claude-context, mattpocock/skills). The governing principle, from obsidian-mind, applies to all four: **procedural code owns the environment; the agent owns content.** Deterministic, testable work (classification, validation, indexing, lifecycle) is code that runs the same every time. Judgment (what to write, how to file and link it) stays with the agent. The two meet at small handoffs.
### 5.1 The skill standard
A skill is a **directory**, not a single prose file. This is the shape, and it resolves your "3 markdown + 3 python" intuition into the canonical form. The cleanest mental model is autoresearch's three roles — a file the human edits to instruct, files the agent reads only when needed, and code the agent never reads but executes:
```
.claude/skills/<gerund-name>/
├── SKILL.md          # INSTRUCTS the agent. Human-edited. Frontmatter + overview. <500 lines.
├── reference.md      # Loaded only when the task needs it (the deep detail). One level deep.
├── examples.md       # Gold-standard worked examples. Loaded on demand.
└── scripts/
    ├── validate.py   # EXECUTED, never loaded into context. Deterministic checks.
    └── build.py      # The fragile, must-be-exact steps live here as code.
```
Rules, all from official guidance:
- **Frontmatter is two fields.** `name` (lowercase-hyphens, ≤64 chars, gerund form — `ingesting-clippings`, not `ingest-clipping`) and `description` (third person, ≤1024 chars, says *what it does and when to use it*). The current skills use `**Description:**` in the body — that is not discoverable metadata. Fix every skill to real frontmatter.
- **SKILL.md body under 500 lines.** Past that, split into `reference.md` / `examples.md`, linked **one level deep** from SKILL.md (never a reference that points to another reference — the agent only partially reads nested files).
- **Reference files over 100 lines get a table of contents** at the top, so a partial read still sees the full scope.
- **Match degrees of freedom to fragility** — this is the answer to "do we need Python?":
  - *High freedom* (prose instructions): many valid approaches, decisions depend on context. Example: "review the note for slop." Keep as text.
  - *Medium freedom* (pseudocode / parameterized scripts): a preferred pattern with acceptable variation.
  - *Low freedom* (an exact script, no improvisation): fragile, consistency-critical, must run in sequence. Example: frontmatter validation, duplicate-key detection, wikilink existence checks, blank-line linting, PDF extraction. **These become `scripts/*.py` the skill calls — not paragraphs the agent re-derives each time.** A skill that says "verify every wikilink with Grep" is weaker than one that runs `python scripts/validate.py --wikilinks` and reads the result.
- **Every writing skill ends with a verifiable checklist** (the `ingest-clipping` 15-point list is the model) — that checklist is the skill's test, the red-green loop from mattpocock's `/tdd`.
### 5.2 The agent / subagent standard
A subagent runs in its **own context window** with its own system prompt, tool access, and permissions; it does heavy work and returns only a summary. Use one when a side task would flood the main conversation with reading you will not reference again (a wide vault search, a full-source ingestion, a link audit). File shape: `.claude/agents/<name>.md` with frontmatter `name`, `description` (third person, "Use proactively for… MUST BE USED for…" like the existing `anti-slop-editor`), optional `tools` (restrict to what it needs), and `model`. The current agents use `**Purpose:**` prose — convert to frontmatter and give each a tight tool allowlist. obsidian-mind's roster is the reference set: a librarian (orphans, broken links, stale notes), a cross-linker, a context-loader, a distiller — each isolated so its reading never pollutes the main window. This is also a token mechanism (Part 6).
### 5.3 The hook standard
Hooks are the "runs without being asked" floor, already wired in `settings.json` (SessionStart, PreToolUse on Write|Edit, SessionEnd). The standard, adapted from obsidian-mind's five-hook lifecycle:
- **SessionStart** — inject the live context pack: North Star pointer, active-work excerpts, open tasks, recent changes, vault file listing. Lightweight excerpts, not full notes (~2K tokens).
- **UserPromptSubmit** — classify the message (decision / capture / source / question) and inject a one-line routing hint. ~100 tokens, deterministic.
- **PostToolUse (after .md write)** — validate frontmatter and check for wikilinks; this is `scripts/validate.py` from 5.1, run automatically. A note without links is a bug.
- **PreCompact** — back up the session transcript before compaction so detail is never silently lost (CPR's core lesson).
- **Stop / SessionEnd** — run the close checklist: append the session-log trace, update indexes, flag orphans.
The invariant: **every automatic action logs one line to the session log.** An OS that moves invisibly is a liability, not an upgrade.
### 5.4 The MCP standard
`jarvis-memory` is the answer to "no MCP tools for Jarvis." It exists; wire it and grow it. It is registered in `.mcp.json` as `command: python, args: [server.py]` — confirm it starts, then follow its own documented growth path, which maps one-to-one onto the three-month plan: populate `chunks` → add semantic search (`jarvis_semantic_search`, plan Week 5) → resolve `links` into a graph (`jarvis_neighborhood`, Week 6) → write `conversations` rows from the capture workflow (Week 2) → add `jarvis_ask` with the citation + confidence contract (Week 7). Each capability is "fill a table, add one function, add one `@mcp.tool()`" — never a restructure. The semantic-search tool is the single highest-value addition because it is the retrieval engine the whole token economy (Part 6) depends on; claude-context shows the model — hybrid BM25 + dense vector, incremental indexing, query-by-meaning before reading files. Keep `jarvis-cli` (read-only health: `health`, `context`, `links`, `enrich-candidates`, `report`) as the deterministic backing the skills and hooks call.
## Part 6 — Token economics: how an agent reads this vault cheaply
This is the full answer to "almost no tokens for highly optimized output." Treat the window as scarce and the vault as a database you query, not a pile you load. Six rules, each enforceable in a skill, agent, or hook.
1. **Index first, content on demand.** Load names and one-line descriptions at start; open a full document only when the task touches it. Never read a folder "to get oriented."
2. **Query frontmatter before prose.** `type`, `status`, `track`, `next`, `enrichment_status` are the filter surface. Narrow to the handful of relevant notes by metadata, then read only those. Every queryable fact left only in prose forces a more expensive read later — which is why frontmatter discipline is a performance feature.
3. **Retrieve by path, just in time.** Pass paths and query strings between steps; pull a note into context only at the moment it is needed. The context pack is this rule made concrete.
4. **Use the semantic index as the retrieval engine.** Once `jarvis_semantic_search` exists, query by meaning to find the right five notes instead of grepping fifty. Measured effect elsewhere: ~40% token reduction at equal retrieval quality (claude-context).
5. **Push wide reading into sub-agents.** A search that must read twenty notes to find three runs in a separate agent whose intermediate reading never enters the main window; it returns the conclusion, not the transcript.
6. **Compact deliberately, persist to the log.** Keep recent turns verbose, summarize older ones, and write durable facts to the session log and notes rather than carrying them in-window (CPR's `/preserve` + `/compress` before `/compact`). The art is choosing what to keep; over-aggressive compaction loses the subtle context that matters later.
The tiered-loading target, modeled on obsidian-mind:

| Tier | What | When | Budget |
| --- | --- | --- | --- |
| Always | This file's pointer + SessionStart excerpts (active work, tasks, file listing) | session start | ~2K tokens |
| On-demand | Semantic-search results / a specific note by path | when the task needs it | targeted |
| Triggered | Classification routing hint | every message | ~100 tokens |
| Triggered | PostToolUse frontmatter/link validation | after each `.md` write | ~200 tokens |
| Rare | Full document reads (a whole instruction file, a long source) | only when explicitly needed | variable |

The one sentence to give every agent: **a well-tagged vault is a query target — find the right five notes by metadata or meaning and read only those; do not load the vault to understand the vault.**
## Part 7 — The strict rules going forward
These prevent the bloat from regrowing. They are the standing discipline this file installs.
1. **One fact, one home.** A rule lives in exactly one file. Every other mention is a pointer, not a copy.
2. **No new instruction file without deleting or merging an old one.** Net file count in the instruction layer does not grow without a reason that survives the "could this be a section in an existing file?" test.
3. **Deletion is part of writing.** When you write or move a rule, delete every other copy in the same change. Redundancy is cost, not safety.
4. **Grill before you build.** Before a structural change, state assumptions and ask the questions that resolve them (mattpocock's `/grill-me`). Misalignment is the most expensive failure; a few questions up front are cheaper than a wrong build.
5. **Surgical edits only.** Touch only what the task requires. Do not "improve" adjacent notes, reformat unrelated sections, or refactor what is not broken (karpathy-guidelines). Every changed line traces to the request.
6. **Done means verified.** A writing task is done when its checklist passes (the lint script runs clean), not when the prose looks finished. Define the success check before writing.
7. **No new structure until the existing structure runs.** The stop-rule for the whole system. Finish the convergence (Part 9) before returning to the heavier subsystems of the three-month plan.
## Part 8 — What Jarvis is at the three-month mark
Stated crisply so the target stops drifting. At the end of the build, Jarvis is four things working as one loop.
**A context server.** Before any AI tool helps you — this one, Codex, Cursor, a web chat — it can ask Jarvis what you know, what you are working on, what you have tried, and where the source notes are. The deliverable is the context pack.
**A source-grounded answer engine.** You ask a question; Jarvis answers from *your* notes, links the evidence, labels its confidence, and states what it does not yet know. The last part is non-negotiable: an engine that hides its gaps launders guesses as knowledge.
**A learning and research engine.** Capture flows through the loop into connected, testable knowledge — concepts become flashcards, sources become summaries, summaries become distilled notes, research questions produce briefs pointing at experiments. The output is knowledge you can be tested on, not more storage.
**A single operating surface.** One dashboard answers "what now" every day. Plans feed it; the loop refreshes it; the review pass keeps it honest.
The principle over all four, from the existing plan and worth repeating: **build the spine before the brain, and never let Jarvis fake what it does not know.** A smaller truthful system beats a larger confident-but-wrong one.
## Part 9 — The convergence build order
Not a new architecture — you have one. This is the work that makes it run. Four moves, each finishable and verifiable, each unblocking the next. Do not start one before the previous runs.
**Move 1 — Collapse the instruction layer (this week).** Execute the Part 4 audit. Make this file the authority; shrink AGENTS and CLAUDE to one-screen contracts; merge the formatting docs into one spec; merge orientation into one file plus the live-state manifest. Done means: cold-start reading under ~400 lines, no rule in two files.
**Move 2 — Finish the templates.** Execute the 2026-05-31 audit's list. Each template gets description-per-heading, one example block, inline plugin hooks, and a linked gold-standard note. Done means: an agent handed any template produces a vault-standard note without inventing structure.
**Move 3 — Build the one execution dashboard.** Make `00_Dashboard.md` the single daily surface (active focus, in-motion, triage queue, decay) on live queries; wire the three plans to feed it. Done means: "what do I do this week" is answered by opening one note.
**Move 4 — Wire the first automatic loop.** Confirm `jarvis-memory` starts; convert the skills to the Part 5.1 structure starting with the most-used (`ingest-clipping`); stand up two scheduled tasks (morning context assembly, evening close) backed by `jarvis-cli`. Done means: Jarvis updates its own dashboard and log daily without you driving it, every action logged.
Only after these four run do you return to the plan's heavier subsystems (semantic index, graph, ask-jarvis, research workbench). The plan's own first principle is to build the spine before the brain. Moves 1–4 are the spine.
## Part 10 — What this file changes elsewhere
Writing this file starts Move 1. To keep the system converged, these files change in step (full verdicts in Part 4): `AGENTS.md` and `CLAUDE.md` shrink to one-screen contracts that link here; `HUMAN_WRITING` stays the voice authority and points here; `Vault Map`/`AI_CONTEXT`/`Agent Operating Guide` merge to orientation + live-state manifest; `Vault Rules`/`Jarvis Writing and Formatting` merge to one formatting spec; `Vault Operating System` keeps only its property schema. The principle behind every edit: **one fact, one home.** This file owns strategy and target; each other file owns its one narrow job and points here for the rest.
## Sources and grounding
Vault evidence (read this session): `Vault Rules — Complete AI Ruleset`, `Agent Operating Guide`, `Jarvis Writing and Formatting`, `Vault Map`, `AI_CONTEXT`, `Vault Operating System`, `Jarvis Vault Architecture`, `Claude Pro Workflow`, the 1,641-line [[Jarvis Three-Month Research Engine Master Plan]], [[Jarvis Multi-Agent PKM Plan]], the [[Note Writing System — Audit and Roadmap (2026-05-31)]], the `.claude/` skills and agents, `settings.json`, and `30_Order/System/jarvis-cli` + `jarvis-memory` (code + READMEs).
External research: Anthropic — *Effective context engineering for AI agents*, *Equipping agents for the real world with Agent Skills*, *Skill authoring best practices* (name/description frontmatter, <500-line body, progressive disclosure one level deep, degrees of freedom), and the Claude Code *subagents* docs. Repos: `breferrari/obsidian-mind` (procedural-vs-content split, tiered loading, five-hook lifecycle, QMD semantic search as MCP, isolated subagents, North Star + Bases dashboard), `karpathy/autoresearch` (instruct / read / execute file separation; single file to modify; verifiable metric), `EliaAlberti/cpr-compress-preserve-resume` (preserve/compress/resume; summary-vs-raw log split), `zilliztech/claude-context` (semantic retrieval MCP, ~40% token reduction), `mattpocock/skills` (grill-before-build, shared-language CONTEXT doc, red-green verification, ball-of-mud rescue), `multica-ai/andrej-karpathy-skills` (think-before-coding, simplicity, surgical changes, verifiable success criteria).

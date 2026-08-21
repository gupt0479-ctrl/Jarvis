# Jarvis — how this repo and the vault relate

## Division of labor

This repo does the **technical work**: clone, install, initialize, run, hit real failure modes. Jarvis (the Obsidian vault at `D:\Users\_Anant\10_Areas\Documents\Jarvis`) tracks the **decisions** and hosts the **live mirrors**: which project a tool is useful for, global-vs-project verdict, why, what stage it's currently at, and — for this repo specifically — a synced copy of the actual `.claude/` this repo runs. Neither side duplicates the other's job: this repo doesn't try to be a knowledge base, and Jarvis doesn't try to be a package manager.

This repo is **dual-purpose**, confirmed 2026-08-09, not single-purpose: it is both the external-tool qualification pipeline (`sandbox/` → `tested-tools/` → promoted) *and* an incubator for Jarvis-bound tooling. Several `sandbox/` clones exist specifically to improve Jarvis's own PKM capability, not to feed some other project — `obsidian-mind`, `obsidian-second-brain`, `gbrain`, `graphify`, `claude-mem`, `agentic-inbox` are the confirmed starting set; the full list is explicitly open-ended, still being discovered, not closed.

Live sync exists, but only in one narrow place today. `_docs/Sync.md` covers the mechanism in full. `20_Progress/AI/` is meant, eventually, to hold a live-synced `.claude/` for **every** codebase on this machine — today only `second-brain-claudekit`'s is actually wired up and live; every other project folder there is a hand-copied, drifting snapshot (see `20_Progress/AI/Claude Code/MOC.md`'s own project-status table: `Jarvis` marked `stale`, several others `static`). The connection between "what happened in this repo" and "what Jarvis knows about it" for everything else stays a manual step a person — or an agent working on Anant's behalf — does deliberately.

## The manual decision ritual

Every time something new lands in one of this repo's three staging areas — `sandbox/`, `tested-tools/`, or a rigid folder (`.claude/skills/`, `.claude/commands/`, or the real global `~/.claude/`) — a corresponding entry goes into Jarvis at `20_Progress/Projects/AI Use/Claude Kit/`.

**This is a manual step, not automated.** Nothing watches this repo's filesystem and writes to the vault — the `.claude/` mirror sync (`_docs/Sync.md`) moves file *content*, it does not make *decisions* or write log entries about them. The person doing the work is responsible for making the corresponding vault entry in the same session the technical work happens. If that discipline lapses, the vault-side record goes stale exactly the way `20_Progress/AI/Claude Code/MOC.md` already documents happening to several of its own project folders — a known, already-observed failure mode, not a hypothetical one.

## What goes where, concretely

| This repo | Jarvis |
|---|---|
| `sandbox/<repo>/` — real clone, real install attempt | `20_Progress/Projects/AI Use/Claude Kit/Tool Map.md` — one row, stage = `sandbox` |
| `tested-tools/<type>/<use-case>/<repo>/` — cleared the bar, under second review | Same row, stage updated to `tested-tools`, with what's been reviewed so far |
| `.claude/skills/` or `.claude/commands/` (this repo, repo-scoped) | Same row, stage = `promoted (repo-scoped)` |
| The real global `~/.claude/` (Windows home *and* WSL home — see `_docs/Design.md`) | Same row, stage = `promoted (global)` |
| A tool dies at any stage (blocked, dropped, redundant) | Same row, stage = `blocked` or `dropped`, with the real reason |
| `tested-tools/_future/<repo>/` — cleared `tested-tools/` review but earns no spot in any current project, parked for a future use case named in a sibling `FOR-WHAT.md` | New 2026-08-19, no Jarvis-side row shape decided yet — same `Tool Map.md` row, stage = `parked (future)`, is the natural extension but this has not been confirmed with Anant. Flagged, not assumed. |
| `tests/` — the actual test(s) proving a specific piece of tooling is useful | New 2026-08-19, no Jarvis-side equivalent exists. Likely referenced from the same `Tool Map.md` row (what test proved this tool's "closes a named gap" claim) once built — not yet decided. |
| `instructions/<repo>/` — a promoted `CLAUDE.md`/`AGENTS.md`/`PRD.md`-shaped file | New 2026-08-19, no Jarvis-side equivalent exists and no note anywhere in Jarvis discusses this folder. Genuinely new on both sides. |
| — | `20_Progress/Projects/AI Use/Claude Kit/Log.md` — one dated entry every time a `Tool Map.md` row changes, following the `60_Claude/07_AI_Information/Session Logs/log.md` convention (`## [YYYY-MM-DD] tag \| title` heading, then bullets) |
| — | `20_Progress/AI/Claude Code/second-brain-claudekit/` — this repo's own live-synced mirror. Updated automatically by `_docs/Sync.md`'s mechanism, not manually. |

## The full map of where things live in Jarvis

Confirmed to exist by direct filesystem check, 2026-08-09. A reorganization moved several of these since this repo's docs were first written in 2026-07 — paths below are the current, post-move locations. Any older reference elsewhere in this repo's docs to a path not listed here should be treated as stale until re-verified.

### `20_Progress/AI/` — the whole-machine `.claude/` mirror layer

Meant to hold the `.claude/` folder from every codebase on this machine, alongside a dashboard (`Claude OS Dashboard.md` / `.canvas`) and a visual blueprint (`10_Areas/AI/Claude OS Map.excalidraw`). Today only `second-brain-claudekit` is actually live-synced; wiring up the rest is known, explicit future work, not yet done.

- **`20_Progress/AI/Claude Code/`** — one subfolder per project, each holding that project's `.claude/` mirror. **This repo's own sync only maintains `second-brain-claudekit`'s subfolder here** — every other project folder (Jarvis, CausalOps, OpsPilot, Resq, The Plan, Github ReadMe, Portfolio, Trading View) is a separate, hand-maintained snapshot, out of this repo's scope; see that folder's own `MOC.md` for their individual `setup_status`.
- Per-platform operating guides live one level up, at `10_Areas/AI/Claude Code.md`, `Cursor.md`, `Kiro.md`, `Codex.md`.

### `20_Progress/Projects/AI Use/` — the main AI hub

The umbrella project folder for AI tooling work, distinct from `20_Progress/AI/`'s mirror layer. Holds `Builds & Resources/` (research/build notes: `Claude Council (LLM Council Skill Install).md`, `Code Review & Eval Gap.md`, `Hermes Agent Framework — Corrected Framing.md`, `Maverick Skills Mode-to-Repo Mapping.md`, `Model Distillation.md`), `Claude Kit/` (this repo's own decision tracker, below), `Gen AI/`, and top-level notes (`Cursor AI.md`, `Jan.md`, `Ollama.md`, `The AI Hub.md`).

`Builds & Resources/` moved here from `20_Progress/AI/Builds & Resources/` during the 2026-08 reorganization — confirmed the old path no longer exists.

### `20_Progress/Projects/AI Use/Claude Kit/` — this repo's decision tracker

- **`Tool Map.md`** — the living, per-tool ingestion record for this repo. One row per tool, updated the same session its pipeline stage changes. **As of 2026-08-09 this is more current than this repo's own docs used to be** — it already has ECC's real test results (3378/3388 tests passing) and the 17-repo 2026-07-30 sandbox batch. Per Jarvis's own "one fact, one home" principle (`Jarvis OS — North Star.md`), **`Tool Map.md` is the sole source of truth for tool-by-tool pipeline state** — this repo's own docs point here instead of keeping a second, driftable copy (see `_docs/PRD.md`).
- **`Log.md`** — one dated entry every time a `Tool Map.md` row changes, `## [YYYY-MM-DD] tag | title` heading, following `60_Claude/07_AI_Information/Session Logs/log.md`'s convention.
- **`Toolkit/`** — moved here from `40_Resources/CS/AI/Toolkit/` during the 2026-08 reorganization (confirmed: that old path no longer exists). Holds `Agents/`, `Commands/`, `Hooks/`, `MCPs/`, `Skills/` subfolders and a `Claude Code.md` reference note — a catalog of what's available/known, distinct from `Tool Map.md`'s pipeline-stage tracking. `Claude Code.md` states its own job precisely: "`Tool Map` answers 'is this tool trustworthy yet'; the Toolkit answers 'given a real task right now, what do I actually type.'"

  **The "How to Use X" / "What X" pattern (confirmed 2026-08-19, verified by direct read of every file, all created 2026-08-10):** every one of the five subfolders carries exactly two notes with a fixed job split. `What {Category}.md` is a ground-truth inventory, split into `## Promoted in claudekit` (what `second-brain-claudekit` has actually promoted into its own `.claude/`) and `## Live in Jarvis` (what's actually on disk in Jarvis's real vault-root `.claude/`, verified against files, not a stale snapshot). `How to Use {Category}.md` is the dispatch note: a `# Claude Kit` section giving project-agnostic usage guidance per promoted claudekit tool, and a `# Particular Use` section of named-use-case subheadings (Vault Curation, Research & Distillation, Career Ops, Daily Operations, Decision & Planning, Learning & Mastery, Writing Quality, plus two honestly-flagged-unserved gaps: Code Review and Frontend) that a shared layer of use-case notes link straight into via `[[Note#Heading]]` anchors. Both files use `type: evergreen`, `status: sprout`, and tags including the category name. This pattern has no equivalent anywhere in `second-brain-claudekit` today — worth reusing verbatim if this repo ever wants its own "what's actually promoted vs. what's still staged" inventory layer; see `_docs/Gaps.md`.

  As of 2026-08-19, `What Agents.md`/`What Commands.md`/`What MCPs.md` all independently flag `10_Areas/AI/Claude Code.md`'s own tool tables (agents, 14-row command table dated 2026-07-03, MCP list) as stale against the real `.claude/` — a second, smaller instance of the same "table written once, never revisited" pattern this doc's own history already shows (the `Immediate Action.md`→`Claude Kit Implementation.md` citation, the Tier-1-list citation fixed in `_docs/PRD.md` 2026-08-19). `Toolkit/Cursor.md` is a completely empty stub (0 bytes) — flagged here so it isn't mistaken for populated content later.
- **`Claude Code/Prompts.md`** — build prompts for this specific repo, written and refined inside a Jarvis-side session (not inside this repo).

### `60_Claude/20_Distilled_Notes/Sources - Plan/` — the historical planning record

`GitHub Ingestion Implementation.md`, `_Notes Created From Ingestion.md`, `00_Execution.md`, and `PDF's Ingestion Implementation.md` — the notes this repo's `_docs/PRD.md` and `_docs/Design.md` cite as the origin of the three-week-unexecuted-plan failure mode this repo exists to prevent. **The literal "Tier 1: INSTALL NOW" table itself lives in `PDF's Ingestion Implementation.md`'s Matrix section, not `GitHub Ingestion Implementation.md`** (corrected 2026-08-19 in `_docs/PRD.md` and `_docs/Repo-Map.md` — `GitHub Ingestion Implementation.md` has its own, separate, unlabeled 4-item "Priority 1" list). Historical record, not a live tracker — `Tool Map.md` is where current state lives now.

### `60_Claude/05_Clippings/AI Conversations/` — raw conversation clippings

Organized by OS (`WSL/`, `Windows/`) then by tool (`Claude Code`, `Cursor`, `Kiro`, and `Cowork` under `Windows/`). Should be **live** for Claude Code and Cowork at minimum, likely Cursor too — the existing `_raw_jsonl` NTFS-junction pattern (documented in this folder's own `README.md`) already proves the mechanism for same-OS, read-only session-transcript mirroring; `_docs/Sync.md` is the record of what does and doesn't extend across the WSL↔Windows boundary.

**Ground-truth capture status as of 2026-08-19 (superseding the paragraph above, which described the intended design, not verified reality):** the capture layer has a real, two-part architecture — Layer 0 (a zero-token raw JSONL mirror, an NTFS junction on Windows / a one-way copy on WSL) and Layer 1 (an automatic, near-zero-token markdown archive note, written by a `Stop`/`SessionEnd`-triggered PowerShell hook — `export-claude-session.ps1` on Windows, `wsl-session-export.ps1` on WSL). This has broken and been re-fixed twice already: first, WSL never had the export hook wired at all until 2026-07-30; second, every hook silently died again for 11 days (2026-07-30 → 2026-08-11) because the hooks called `pwsh`, which wasn't on `PATH`, and a naive fallback to native `powershell.exe` "worked" but couldn't resolve WSL paths, so nothing was captured while `settings.json` reported no error. Both fixes are recorded in `AI Conversations/README.md`'s 2026-08-11 amendment.

**A third, deeper reliability gap was diagnosed 2026-08-10/11 and deliberately left unbuilt**, per the raw session transcript at `60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/08-10 Plan second-brain-claudekit workflow and review system.md`: capture depends entirely on `SessionEnd` firing, which doesn't fire reliably for every real termination path (an abruptly closed terminal, machine sleep, a WSL shutdown mid-session). The fix — a scheduled `-BackfillAll` safety net per platform, mirroring the pattern already proven for the Cursor sweep and the Unison vault sync — was explicitly scoped but not registered ("this message says discussion, not build").

**As of 2026-08-19, that unbuilt gap has already recurred**: nothing has been captured on either OS since 2026-08-10 (Windows) / 2026-08-12 (WSL) — a 7–9 day blank stretch confirmed by direct listing of every dated file in both `WSL/Claude Code/` and `Windows/Claude Code/`. "WSL is the weak link" is only half the story — this specific stall hit both platforms simultaneously, for the same undiagnosed-until-now-unbuilt reason. **Building the scheduled backfill safety net (Windows Task Scheduler + WSL cron, one per platform, same shape as the existing sync/Cursor sweeps) is the single highest-leverage fix available for this repo's own conversation-logging requirement** — see `_docs/Gaps.md`.

**Summarization (Layer 2, the `/export-ai-session` skill, genuinely token-costly, distinct from capture) has essentially never run against Claude Code sessions**: `60_Claude/07_AI_Information/AI Conversation - Summaries/` holds exactly 4 distilled summaries, all Cursor, none Claude Code, despite ~90 raw Claude Code session notes existing across both platforms. `Summaries-to-Create.md` (the intended backlog file) is empty. `60_Claude/30_Reviews/AI/Tools/Tool log.md` (Layer 3, the per-skill-use index `/export-ai-session` is supposed to append a row to on every run) exists with the correct schema but has zero data rows.

### `60_Claude/07_AI_Information/` — the live AI-instruction and state layer

The authority stack for how AI tools should behave in this vault: `Jarvis OS — North Star.md` (strategy/diagnosis/build-standard authority), `AI_CONTEXT.md` (live-state manifest and cold-start read order), `How to Use Claude/` (`Claude OS.md` — the agentic-setup registry; `Agent Operating Guide.md` — now a pure redirect stub per North Star's convergence pass; `What Graphify Does.md`).

- **`AI Conversation - Summaries/`** — on a skill invocation, a session-summary note gets written here. Confirmed as of 2026-08-09: the destination for these notes is currently specified as the flat top level of this folder, **outside** the tool-specific subfolders that already exist here (`Claude Code/`, `Cowork/`, `Cursor/`, `Kiro/`) — an acknowledged inconsistency, not yet fixed.
- **`Session Logs/`** — `log.md` (the main append-only session log `AI_CONTEXT.md` points to), `Session Logs Board.md`, `Convergence Worklog 2026-06-11.md`, and per-project subfolders including `CausalOps/` and **`Claude Kit/`** — the folder specifically for this repo's own session-log entries. Confirmed empty as of 2026-08-09: a scaffold, not yet populated.

### `60_Claude/10_Source_Summaries/Github Ingestion/` — repo-ingestion write-ups

Holds `Claude Kit Implementation.md` — the ingestion record for repos evaluated for (and potentially added to) this codebase's pipeline — plus category-sorted starred-repo lists (`AI Starred`, `Building Starred`, `Claude Starred`, `Jobs Starred`, `Learning Starred`, `Projects Starred`, `Security Starred`), `How Anant Uses Each Repo.md`, and `Useful Repos - Shortlist.md`.

**Correction, 2026-08-09:** this repo's docs previously cited a file in this folder named `Immediate Action.md` — that file does not exist in the current listing. `Claude Kit Implementation.md` is the current file serving that role; any surviving reference to `Immediate Action.md` elsewhere in this repo is stale.

### `60_Claude/30_Reviews/AI/` — the review layer

Reviews of AI conversations and tool use, in subfolders `Conversations/`, `Tools/`, and `Scheduled/{Weekly,Monthly}/`.

**Status as of 2026-08-09 (`10_Areas/AI/Setup/Folder Map.md`, pre-dating the build below):** "a completely empty shell... nothing writes to it yet." That description is now **superseded** — real design and build work happened 2026-08-10/11, recorded in the raw session transcript at `60_Claude/05_Clippings/AI Conversations/Windows/Claude Code/Jarvis/08-10 Plan second-brain-claudekit workflow and review system.md` (this session also settled where the system lives, via an explicit `AskUserQuestion`: its own tree under `60_Claude/30_Reviews/AI/`, kept deliberately separate from `Weekly Synthesis Index`/`60_Claude/30_Reviews/Monthly/`, which review a different subject — concept mastery, the Capability Engine — not usage/sync health).

**What's actually built (confirmed 2026-08-19, still current):**
- `30_Order/Standards/Review Standard.md` — the governing content standard. A review must cite the real log rows it read (Tool log, Sync-Log, Write Log) — "it never summarizes from memory or impression." Its `Used By Workflow` section states the trigger mechanism explicitly: **"Manual, human-triggered — no cron job writes a review."** This is a deliberate design decision, not a gap. Its `Decided Fixes` section is the literal 100%-clarity gate: *"a review surfacing a problem is not itself authorization to auto-fix it... even then the fix is applied by hand or flagged for the next build session — never by an automated process this review triggers."*
- `30_Order/Templates/Capability/AI Tools Weekly Review Template.md` and `.../AI Tools Monthly Review Template.md` — both real, Templater-driven, matching the Standard's required sections (Period Covered, Sources Reviewed, What Ran This Period, Sync & Capture Health, Findings, Decided Fixes, Open Questions, Next Period's Watch List; Monthly adds a Tool Map Health Check that names anything stuck at one pipeline stage for over a month).
- `60_Claude/30_Reviews/AI/Tools/Tool log.md` — the real per-use index of skills/commands/agents across Windows and WSL, one row per invocation (`Date | Project | Skill/Command | What It Did | Outcome | Source`). Deliberately filed here, not in `05_Clippings/`, because the vault's Write Contract makes `05_Clippings/` read-only after capture and this file is continuously updated, not a raw capture. Written only by `/export-ai-session` — never hand-edited.

**What's still genuinely missing, as of 2026-08-19:**
- The `Tool log.md` table has zero data rows — nothing has run `/export-ai-session` against a real session yet.
- No review has ever been written under the new Standard — its own "Gold Standard Example" field says "none yet."
- `Conversations/` is untouched by any of this build — still an empty, unwired subfolder with no defined purpose distinct from `Tools/`.
- No scheduling mechanism exists for the *review-writing step itself* — `CronList` returns nothing, and per the Standard this is by design (a human, or an agent explicitly asked, produces a review — nothing auto-generates one). What genuinely is missing is the *cadence* trigger (a reminder/cron that prompts the human/agent to sit down and write the next Weekly or Monthly review on schedule), which `10_Areas/AI/Setup/Gaps.md` still lists as open.

**Self-improvement sequencing still applies to anything beyond the above:** per `_docs/Design.md`'s 2026-08-09 commitment — the qualification pipeline runs solidly first, real evidence accumulates, only then does "what to automate further" get decided, and any future automation for this layer must write one visible, logged line per run, never act silently.

### `60_Claude/40_Project_Briefs/Claude Kit/` — the planned Graphify integration

Confirmed empty as of 2026-08-09 — a placeholder for work not yet started. The plan: implement Graphify (and potentially other mapping tools) against this repo itself, to map out everything inside the codebase; that map then syncs into this Jarvis folder and auto-updates as the underlying `.graphify` output improves, using a mechanism similar in spirit to the existing Unison-based `.claude/` sync (`_docs/Sync.md`). **Not built.** Named and scoped here as a future task, not claimed as an existing capability.

### `40_Resources/CS/AI/` — the AI-knowledge reference layer

Where rich, source-of-truth knowledge about *how to use AI correctly*, per domain, gets written — but only after a skill/agent/MCP has actually been implemented and used, never speculatively. Confirmed as of 2026-08-09: most of this folder is still thin or empty (`Agent Orchistration/`, `Memory/`, `Token Optimization/` subfolders exist but are largely unpopulated). This is acknowledged, ongoing, manual work — filling it is not a mechanical task, it accrues one real, tested lesson at a time.

- **`Prompts/`** — model-specific prompt notes: what actually works for a given AI platform, with real example prompts, headed per model. Currently one file (`Chat Gpt Prompts.md`) — thin by the folder's own design, meant to grow per-model as real prompting patterns get proven out.
- **`Workflows/`** — workflows for each AI platform in active use, and for every automated Jarvis process that exists *or should exist*. Written prescriptively, as if the described workflow is actually running — the target-state spec for automation, the same role `Jarvis OS — North Star.md` plays for the instruction layer as a whole. Currently holds `AI Workflow.md`, `UMN Workflow.md`, and a `Claude Code/` subfolder.

### `10_Areas/AI/` — the master AI index

The single place every AI-related note in the vault ultimately maps into — deliberately kept light (short notes, heavy interlinking) rather than duplicating detail that belongs in `40_Resources/CS/AI/` or `60_Claude/`. Explains, in real detail, what each AI-related folder is *for*. This file and `_docs/Repo-Map.md` are this repo's own equivalent instinct applied to its own filesystem.

## Why `20_Progress/AI/Claude Code/` and `20_Progress/Projects/AI Use/Claude Kit/` don't duplicate each other

`20_Progress/AI/Claude Code/<Project>/` answers "what is this project's Claude Code setup **right now**" — hand-maintained, per-project, mirror-of-reality snapshots for every project except `second-brain-claudekit`, which is genuinely live. `20_Progress/Projects/AI Use/Claude Kit/` answers an earlier, different question: "what has `second-brain-claudekit` ingested, and what stage is each thing at, regardless of whether it's reached any project's real `.claude/` yet." Most of what `Tool Map.md` tracks (gbrain, gstack, mattpocock-engineering, ECC, the 2026-07-30 batch) hasn't reached any project's `.claude/` — there's nothing yet to add to a per-project folder. The two layers connect at exactly one point: the day a tool crosses from tracked in `Tool Map.md` into an actual project's real `.claude/skills/`, that project's own snapshot gets updated too, and the `Tool Map.md` row notes which project(s) received it.

## No parallel logging convention invented

`20_Progress/Projects/AI Use/Claude Kit/Log.md` deliberately reuses the exact heading shape already established in `60_Claude/07_AI_Information/Session Logs/log.md` (`## [YYYY-MM-DD] tag | title`, followed by narrative bullets) rather than inventing a new format. Consistency across the vault's logging layers matters more than a locally "nicer" format — the same principle behind this repo's own dated-amendment convention in `_docs/`.

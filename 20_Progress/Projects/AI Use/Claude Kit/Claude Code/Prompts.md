---
type: input
status: active
created: 2026-08-11
updated: 2026-08-22
tags:
  - claude-kit
  - prompts
  - second-brain-claudekit
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session Context]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/WSL Environment]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Windows Environment]]"
next: "Round 9, 2026-09-05 — the first real 'third hop' attempt: staged/mirrored content actually promoted into real .claude/ config, across Jarvis, both global homes, and a brand-new internship-research-loop manifest entry. After this: whatever the session's own report names as the real next gap — don't pre-guess it here."
---
# Claude Kit — Build Prompts
==Only prompts live in this note, each inside a fenced block, ready to paste into a fresh session. Everything else — context, background, open questions — lives in [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session Context]]. Rewritten 2026-08-19; this note's prior content (dated 2026-08-11) is preserved there, not lost.==
## Sequencing
**Run `# Claudekit` first.** It lays out the repo's own structural base — nothing in `# Jarvis` should be attempted until that base is real, because `# Jarvis`'s job is to document what the base actually became, not what it was planned to become. Read the Claudekit session's final report (or its `git log`/diff) before starting `# Jarvis`.

# Claudekit

**Round 9, 2026-09-05 — the first real "third hop" attempt.** Everything before this round built and proved the pipeline (`sandbox/` → `tested-tools/` → an explicit per-item decision → `agents/<Project>/`+siblings in this repo → a read-only Jarvis-side mirror) but explicitly left one thing "not attempted, not scheduled" per [[20_Progress/Projects/AI Use/Claude Kit/Log]]'s 2026-08-21 entry: whether/how staged content ever flows into a real project's *actual live* `.claude/`. This round is the first real attempt at that hop — for Jarvis (most-built real `.claude/`, several genuinely empty stubs both there and in this repo's mirror of it), for both global home directories (WSL populated but stale in places, Windows nearly bare), and for `internship-research-loop` (fully built this same week directly in the vault session, per [[20_Progress/Internship/Building System/System - Build Log]]'s 2026-09-04 entries — but never onboarded into this repo's sync pipeline at all; no manifest entry exists for it).

Paste into a fresh Claude Code session, cwd = `~/projects/ai/claude/second-brain-claudekit`, `high` or `xhigh` effort. Do not start this until git status is clean or every dirty path below has an explicit decision — see Step 0.

```
You're picking up second-brain-claudekit with no memory of prior sessions. Read _docs/Architecture.md, _docs/Design.md, _docs/Promotion-Criteria.md, _docs/Jarvis.md, and _docs/Sync.md in full before doing anything else — this prompt cites them throughout and assumes you've actually read them, not skimmed the summary below. Also read sync-manifest.json directly (don't trust any note's paraphrase of its schema) and 20_Progress/Projects/AI Use/Claude Kit/{Tool Map,Log,Claude Code/Claudekit Session Context}.md in the Jarvis vault (reachable via /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis or the jarvis MCP tools) for the dated narrative behind the current state.

## What's already established, cited so you don't re-derive it

- **The pipeline**: `sandbox/<repo>/` (bare clone) → clears `_docs/Promotion-Criteria.md`'s four gates → `tested-tools/<type>/<use-case>/<repo>/` → an explicit, per-item human decision → lands in exactly one of: `agents/<Project>/`, `commands/<Project>/`, `hooks/<Project>/`, `skills/<Project>/`, `instructions/<Project>/` in this repo (real destination names today: CausalOps, Jarvis, Portfolio, Trading View, Resq, OpsPilot, The Plan, second-brain-claudekit, `.claude_windows`, `.claude_wsl` — ten manifest entries, confirmed all `status: live` as of 2026-08-21).
- **Two different things populate the same `<Project>/` folders and you must not conflate them**: (a) for the eight *real, already-existing* projects, Unison syncs each project's actual live `.claude/{agents,commands,hooks}` + main instruction files into this repo's matching `<Project>/` folder — the project's real config is the source, this repo's copy is a mirror (see `_docs/Jarvis Environment` notes — actually check `sync-manifest.json`'s per-entry `direction`/`force_source` fields directly, since two Jarvis-side notes describe this differently and you need the real schema, not a paraphrase); (b) for a *newly promoted* sandbox tool, a human manually places files into the matching `<Project>/` folder as a one-time decision, per Design.md. **Verify which direction actually applies to each entry before writing anything** — don't assume (a) or (b) uniformly.
- **The still-open "third hop"**, per Log.md's 2026-08-21 entry verbatim: "whether/how staged content... ever flows into a real project's actual live `.claude/` config — is an open question, not attempted, not scheduled." This round is attempting it for the first time, deliberately, not stumbling into it by accident — treat every write into a real project's `.claude/` as a decision worth its own line in Log.md, not a mechanical copy.
- **Jarvis's real `.claude/`** (`/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/.claude/`) is the most built of any destination — confirmed this week: `skills/` holds real, structured folders (SKILL.md + reference.md/examples.md where needed), `agents/` holds 11 files, 6 of them **genuinely empty on both sides** (`daily-operator.md`, `human-operator.md`, `ingestion.md`, `llm-council.md`, `note-to-actions.md`, `professor.md` — confirmed 0 lines in both Jarvis's real file and this repo's `agents/Jarvis/` mirror, checked directly 2026-09-05, not assumed from either side alone), the other 5 (`anti-slop-editor`, `career-operator`, `learning-agent`, `research-distiller`, `vault-curator`) real and substantial (33–207 lines). `rules/` has `human-writing.md` (real) plus two empty stubs (`what-to-read.md`, `how-to-write.md`); `context/workspace-context.md` is real, `context/MEMORY.md` is empty. **No `hooks/Jarvis/` bucket exists in this repo at all** — Jarvis's three real, tested PowerShell hooks (`jarvis-write-guard.ps1`, `jarvis-session-continuity.ps1`, and a brand-new `jarvis-internship-note-guard.ps1` added 2026-09-04, all registered in Jarvis's real `.claude/settings.json`) have never been staged into this pipeline at all.
- **`internship-research-loop`** (`~/projects/work/internship-research-loop`) got a full `.claude/` build this week, directly in a vault session, never through this pipeline: 7 agents (`contact-researcher`, `loop-verifier` pre-existing; `program-writer`, `tracking`, `promotion`, `applying`, `testing-tools` new), 4 skills (`promote-dossier`, `review-loop-change` pre-existing; `promoting-manual-find`, `tailoring-application` new), 3 `rules/` files, an extended `CLAUDE.md`, and a `settings.json` with a new `PostToolUse` convention-reminder hook (`review-reminder.sh`). **No sync-manifest.json entry exists for this project** — it's real, live, committed to nothing yet (working tree, not pushed), and completely outside this pipeline's visibility.
- **Global homes**: WSL (`~/.claude`) is populated — 3 agents, 7 commands, 3 hooks, 28 skills — but per Log.md's 2026-08-20 entry, the WSL agents/commands reference **pre-reorg vault paths that no longer exist** (`10_UMN/`, `00_Inbox/Headway/`, `50_Archive/copilot/`), not fixed at the time because editing them syncs into a live home a real session depends on — that's exactly the kind of fix this round should actually make, carefully. Windows (`C:\Users\Anant Gupta\.claude`) is **confirmed bare 2026-09-05, re-verified directly**: zero agents, zero commands, zero hooks, skills/ holding only `export-ai-session/` plus ~30 firecrawl-* plugin skills (untouched, not this pipeline's concern). `gbrain` cleared all four Promotion-Criteria gates for global promotion back on 2026-08-20 (`tested-tools/mcp-servers/gbrain/VERDICT.md`) and **still isn't installed on either home** — the single most concrete, already-decided, ready-to-execute action available to this round.
- **This repo's own git status is dirty in a way that predates this round** — `git status --short` shows ~53 changed paths as of 2026-09-05, including a known, already-logged, ~2-week-old unresolved item: `_docs/Architecture.md`/`_docs/PRD.md` show as deleted, `Architecture.md`/`PRD.md` show as new at repo root, uncommitted since the 2026-08-21 `instructions/` fix round explicitly flagged this as "a separate, pre-existing decision this fix didn't touch." Also present: several `M` changes under `commands/.claude_wsl/`, `hooks/.claude_wsl/`, `skills/.claude_wsl/` (real drift between this repo's WSL-home mirror and the live WSL home — check which side is actually newer before resolving either direction), a new untracked `.claude/hooks/pre-artifact-edit-check.sh` that also appears staged at `hooks/second-brain-claudekit/pre-artifact-edit-check.sh` (confirm these are meant to be the same file before assuming one is stale), and the full `agents/Jarvis/`+`skills/Jarvis/` trees showing as untracked (never committed since the sync started populating them).

## Step 0 — clean workspace, a real precondition, not a formality

Before any of the tasks below: run `git status`, read every one of the ~53 (or however many, re-count, don't trust this prompt's number) changed paths, and for each one either (a) commit it as part of a coherent, explained change, (b) explicitly decide and record "leave dirty, here's why" (e.g. an actively-syncing mirror folder that's expected to show as untracked between Unison runs), or (c) flag it as something you can't safely resolve without asking Anant. Do not proceed to Task 1 with unexplained dirty paths. The `Architecture.md`/`PRD.md` relocation is the oldest, most important one to actually close out — it's been open since 2026-08-21.

## Procedure for anything genuinely new you write this round

Per Anant's explicit instruction: **skills first, then hooks, then agents — and when you write an agent, write its matching command in the same pass.** Don't write an agent with no way to invoke it deliberately, and don't build hook automation before the skill it supports actually exists in a reviewable form.

## Task 1 — Jarvis: close the 6-agent gap and the missing hooks bucket

1. For each of the 6 empty agents (`daily-operator`, `human-operator`, `ingestion`, `llm-council`, `note-to-actions`, `professor`): figure out, from the name and from what it's apparently replacing (the old roster was `research-distiller`, `vault-curator`, `career-operator`, `anti-slop-editor`, `learning-agent` — some of these new names look like renames/consolidations of the old ones, some look genuinely new; don't assume which without checking whether the old agent is still referenced anywhere live — CLAUDE.md's skills table, `.claude/commands/*.md`, AGENTS.md) what each one is actually supposed to do. Ask Anant directly if the intent isn't recoverable from context — don't invent a plausible-sounding purpose for a name alone.
2. Write real content for each, in this repo's `agents/Jarvis/` staging first (per "drafted here, promoted from here"), following Jarvis's own build standard (`Jarvis OS — North Star.md` Part 5.2: frontmatter `name`+`description` in the "Use proactively for… MUST BE USED for…" pattern, a tight `tools` allowlist, `model`).
3. Do the same for `rules/what-to-read.md` and `rules/how-to-write.md` (empty) and `context/MEMORY.md` (empty) — check what `rules/human-writing.md` and `context/workspace-context.md` (both real) actually do first, so the two new rules files fill a genuinely different, non-duplicate role, same discipline the internship-research-loop `rules/` files used this week (each one either a real addition or a thin pointer, never a restatement).
4. Create the missing `hooks/Jarvis/` bucket and stage Jarvis's three real hook scripts into it (copy, don't move — the real scripts stay in Jarvis's `.claude/hooks/`), plus a short per-hook note (what it does, what event it's registered on) mirroring `_docs/`'s existing per-tool documentation depth.
5. **Execute the third hop, carefully, for the first time**: once the 6 agents + 2 rules + MEMORY.md have real, reviewed content in this repo's staging, copy them into Jarvis's actual `.claude/agents/`, `.claude/rules/`, `.claude/context/` — show the diff before writing, confirm with Anant before the first one lands (this is a new kind of write this pipeline has never done; don't assume the green light extends to all 9 files just because it's granted for the first one).
6. Log every promotion decision as its own line in this repo's own commit history and in the Jarvis vault's [[20_Progress/Projects/AI Use/Claude Kit/Log]] (same file, same append-only dated-entry convention already established there) — cite exactly what changed and why, per that file's own standard (see any 2026-08-20/21 entry for the expected density).

## Task 2 — Global homes: WSL cleanup, Windows bootstrap, gbrain install

1. **WSL**: fix the confirmed stale vault-path references in `~/.claude/agents/*.md` and `~/.claude/commands/*.md` (the pre-reorg paths named in this repo's own Log.md 2026-08-20 entry) — read each file, confirm the real current path for whatever it references, fix in place. This edits a live global home a real session depends on; show the diff, confirm before writing.
2. **Windows**: this is closer to a blank slate than a merge job, per this repo's own `.claude_windows` manifest entry and `Windows Environment.md`. Before writing a global `CLAUDE.md`/agents/commands there, re-run the WSL-side global-scope test from `_docs/Design.md` ("useful with no regard to which project is open") against whatever you're about to add — don't copy WSL's agents/commands over wholesale; several are Obsidian-vault-specific in a way that's arguably fine for WSL's actual usage pattern but shouldn't be assumed to transfer. If a 2026-08-22 Cursor/Grok+Sonnet session (see this file's own prior round) already produced a `_global-config-plan.md` on either home and executed it, find and read that evidence first (check both homes for a leftover plan file, check git-adjacent history/backups) — don't redo work that already happened; if no evidence it ran, say so plainly and proceed as if starting fresh.
3. **gbrain**: cleared for global promotion since 2026-08-20, still not installed on either home. This is the single most concrete, already-decided action available — do it now on whichever home(s) make sense (check `tested-tools/mcp-servers/gbrain/VERDICT.md` for the exact install steps already verified working), and update Tool Map.md's gbrain row the moment it's actually running on a real home, not before.

## Task 3 — Onboard internship-research-loop into the pipeline

1. Add a new `sync-manifest.json` entry for `internship-research-loop` (`~/projects/work/internship-research-loop`), matching the schema the other 8 real-project entries use — confirm the schema by reading 2-3 existing entries directly, don't guess the field names.
2. Create `agents/internship-research-loop/`, `commands/internship-research-loop/` (if this project has any — check; it may not), `hooks/internship-research-loop/`, `skills/internship-research-loop/`, `instructions/internship-research-loop/` and let the first sync run populate them from the real repo's current `.claude/` (7 agents, 4 skills, 3 rules, `CLAUDE.md`, `settings.json`) — or, if the sync direction for a brand-new entry needs a manual first population before Unison picks it up (check `_docs/Sync.md` for the actual bootstrap procedure for a new entry, don't assume), do that manually once.
3. This project's `settings.json` also has proposed-but-not-yet-applied permission entries and a hook that were written by hand this week (python execution permissions, MCP vault-tool allow/ask split, `review-reminder.sh` on `PostToolUse`) — confirm the real repo's `settings.json` already has them (it should — they were applied directly, not just proposed, as of 2026-09-04) before assuming this task still needs to add them.
4. Cross-reference `sandbox/hiring-agent/` (InterviewStreet's hiring agent, cloned 2026-07-30, explicitly tied to "evaluate usefulness for the internship research loop" per this repo's own Tool Map row, real next step never attempted) — now that internship-research-loop's own `.claude/` is genuinely built out, actually run hiring-agent once against a real internship-search pass and compare its output to what `program-writer`/`promotion`/`tracking` already do. Record a real keep/drop/blend verdict, same rigor as the `cpr-compress-preserve-resume` blend decision — don't leave this as another "still worth evaluating" entry that sits idle for weeks.

## Task 4 — This repo's own `.claude/`

1. Resolve the `pre-artifact-edit-check.sh` duplication (`.claude/hooks/` vs. staged `hooks/second-brain-claudekit/`) — confirm whether these are meant to be identical (this repo self-mirrors, per the manifest's `second-brain-claudekit` entry) and if so which is the real source; if they've diverged, reconcile deliberately, not by picking one arbitrarily.
2. Review this repo's own 3 agents (`research-distiller`, `vault-curator`, `weekly-reviewer`) and 10 commands against the same North Star Part 5 build standard Jarvis's are held to — this repo has never been audited against that standard itself, only used it as a design reference for others.

## Sandbox review — classify what's sitting there, using Promotion-Criteria.md's own four gates

Do not re-clone or re-triage the 13 already-dropped repos (agent-skills, andrej-karpathy-skills, claude-skills-llm-council, llm-council, last30days-skill, claude-code-best-practice, system-prompts-and-models-of-ai-tools, CL4R1T4S, agentscope, autoresearch, gsd-core, agency-agents, agent-skill-simplified-technical-english, Agent-Reach) or the 2 out-of-scope-here special cases (adx, memsearch) — those decisions are recorded and stand. Focus on what's actually still open, one real next action each:
- **hiring-agent** — see Task 3.4 above, now has a real, ready use case.
- **obsidian-mind** — read its procedural-vs-content split and five-hook lifecycle against `Jarvis OS — North Star.md` Part 5 (which already cites it as a design model) and note explicitly what Jarvis's real hooks already match vs. what's still missing (the `PostToolUse`-validate-frontmatter pattern and the `UserPromptSubmit`-classify-and-route pattern from North Star Part 5.3 are both still unbuilt in Jarvis as of 2026-09-04 — check whether obsidian-mind's real implementation of either is worth adapting directly rather than building from scratch).
- **obsidian-second-brain** — diff its vault-rules against `60_Claude/vault-rules/` (this repo's own) once; note real disagreements, don't just skim.
- **claude-mem** — hold per its own recorded reasoning (overlaps gbrain + `jarvis-memory` MCP) until gbrain is actually running (Task 2.3) — re-check only after that, don't jump ahead.
- **agentic-inbox** — compare its triage logic against this repo's own `commands/inbox-process.md` (confirmed zero-provenance native scaffold, currently unused) — a real improvement-or-not verdict, not another deferral.
- **spec-kit, claude-context, promptfoo** — each already had a real install/run step executed 2026-08-20 (10 skill files scaffolded; 108 files/1369 chunks indexed at 4/4 correct semantic queries; 1-of-2 promptfoo eval pass with a genuine rubric-caught weakness in `/challenge`). None promotion-decided yet — for at least one of the three, walk it through Promotion-Criteria.md's four gates for real and record an actual verdict in Tool Map.md, don't leave all three open again.
- **gstack** — still blocked on missing WSL libs (`libnss3.so` etc.) per its own documented fix command in Tool Map.md. If this session has a real interactive terminal, run the fix and retry `./setup`; if not, say so plainly and leave it blocked rather than guessing at success.
- **mattpocock-engineering** — 0 of 17 skills individually tested, a real dated backlog table exists (`tests/skills/mattpocock-engineering/README.md`). Test at least 2-3 of the 17 for real this round rather than leaving the backlog at zero again.

For anything genuinely new found in `sandbox/` beyond the 32 already tracked (re-run `ls -d sandbox/*/ | wc -l` and compare against 32 — if it's grown, the new ones need the same one-line keep/drop/still-worth-evaluating treatment the 2026-08-20 triage gave the prior 32, not silent omission).

## After the ingestion work — review and tighten

1. Read `_All-Projects-Sync-Log.md` for the real, current sync-task health (it has failed silently before, per this repo's own 2026-08-20/21 history) before trusting that anything you just staged will actually propagate.
2. Update [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]] and [[20_Progress/Projects/AI Use/Claude Kit/Log]] with every real state change this round produced — new manifest entry, every promotion, every sandbox verdict, per those files' own established append-only, cited-evidence convention. Do not summarize loosely; cite exact paths, exact line/file counts, exact commit hashes, the same density every prior round in this file used.
3. Make further improvements to this repo's own `.claude/` folder and documentation/procedure only *after* the above — name anything real you find (a stale doc, a convention that should be tightened, a genuine second-brain-claudekit-scoped gap), don't invent busywork to fill this step.

## Report back

- Step 0: the real dirty-path count, and the decision made on each category.
- Task 1: which of the 6 agents got real content, what each does, whether the third hop actually landed in Jarvis's real `.claude/` (and if Anant didn't confirm past the first file, say exactly where you stopped).
- Task 2: WSL path fixes made, Windows's real starting state re-confirmed or corrected, gbrain's install status on each home.
- Task 3: the new manifest entry, its first sync result, the hiring-agent verdict.
- Task 4: the pre-artifact-edit-check.sh resolution, the self-audit finding.
- Sandbox: one line per item above — verdict and evidence.
- Anything in this prompt's own "already established" section that turned out wrong when you checked it directly — state that plainly, same discipline every prior round in this file has used.
```

**Round 8, 2026-08-21 — fresh session.** Round 7 fixed the self-nesting bug but kept the wrong scope: `_docs` as a directory-shaped `instructions_paths` entry, flattened wholesale into `instructions/second-brain-claudekit/`. That was never the intent. `instructions/<repo>/` is a small, curated set of main files only — `CLAUDE.md`, `AGENTS.md`, `README.md`, `PRD.md`, `Architecture.md` (now confirmed at this repo's root, not in `_docs/`) — never an entire internal-documentation directory. This is the fourth time this folder's scope has needed correcting; this round makes the mechanism itself incapable of the mistake, not just the current data.

Paste into a fresh Claude Code session, cwd = `~/projects/ai/claude/second-brain-claudekit`, `high` or `xhigh` effort.

```
Read sync-manifest.json fresh before anything else. The final rule, confirmed directly by Anant: instructions_paths (whatever the exact field is called — confirm from the real file) may only ever list explicit file paths, never a directory. A "main file" is a single top-level instruction/context document -- CLAUDE.md, AGENTS.md, README.md, PRD.md, Architecture.md, or a real equivalent -- never an entire folder of internal reasoning docs (this repo's own _docs/, or a project's .claude/context, .claude/playbooks, .claude/decisions, .claude/checklists, .claude/workflows -- all directory-shaped, all the same class of mistake).

## 1. Simplify sync-all.sh: remove directory-flattening entirely

Round 7 added logic to sync-all.sh that resolves a directory-shaped instructions_paths entry into its real files and flattens them. Delete that logic. instructions_paths should only ever process explicit file entries -- copy each one flat into instructions/<repo>/<basename>.md, keeping the existing claude-<filename>.md prefix for a nested-vs-root name collision. If a directory-shaped entry is ever found in the manifest going forward, that's a data error to fix in the manifest, not something the script should try to handle gracefully.

## 2. Fix second-brain-claudekit's own entry

Remove _docs entirely from its instructions_paths. Confirm the real current root files (expected: CLAUDE.md, README.md, PRD.md, Architecture.md -- verify this list directly, don't assume) and set instructions_paths to exactly those, as explicit file entries.

## 3. Audit all 10 entries for the same mistake

Check every entry's instructions_paths for any directory-shaped entry. Resq and OpsPilot are the known suspects (.claude/context, .claude/playbooks, .claude/decisions, .claude/checklists, .claude/workflows all appear in their general paths lists -- confirm whether any of those also ended up in instructions_paths specifically, not just the general sync paths). Remove any directory entry found; keep only genuine main files (CLAUDE.md, AGENTS.md, README.md, PRD.md/README.md nested under .claude/ where that's the real pattern, per the already-established collision-prefix convention).

## 4. Rebuild every affected instructions/<repo>/ folder

For second-brain-claudekit and any other entry fixed in item 3: delete whatever landed there from a directory flatten that shouldn't have happened, and re-populate from the corrected, file-only instructions_paths list. Confirm the result is small and curated -- if any instructions/<repo>/ folder still has more than a handful of files after this, that's a signal something's still wrong, go back and check.

## 5. Write the definitive, final rule -- for real this time

Update _docs/Sync.md, 60_Claude/vault-rules/write-contract.md, and 60_Claude/vault-rules/pipeline-conventions.md with one unambiguous statement: instructions/<repo>/ holds only explicit main files (CLAUDE.md, AGENTS.md, README.md, PRD.md, Architecture.md, and real equivalents) -- never a directory's contents, never an internal-documentation folder, no matter how relevant that folder seems. This scope has been corrected three times already; state it precisely enough that a fourth correction shouldn't be needed.

## 6. Close the loop

Update _docs/Gaps.md and _docs/Repo-Map.md with the real fix across all 10 entries. Review the diff for secrets before committing. Commit in logically separated commits.

Apply items 1-4 to all 10 entries, not just second-brain-claudekit -- the mechanism fix in item 1 should make this structurally impossible to get wrong again, verify that it actually does.
```

# Jarvis

**Round 8, 2026-08-21.** Short and verification-only — the sync-build phase is closing out and the next real work is `tests/`. Don't add new scope here.

Paste into a fresh Claude Code session, cwd = the Jarvis vault root (Windows), Sonnet 5, `high` or `xhigh` effort.

```
A parallel codebase round is fixing instructions/<repo>/'s scope for the third time: it should only ever hold explicit main files (CLAUDE.md, AGENTS.md, README.md, PRD.md, Architecture.md), never an entire directory's contents (this repo's own _docs/ was wrongly flattened in there; Resq/OpsPilot's .claude/context, .claude/playbooks, .claude/decisions, .claude/checklists, .claude/workflows are being audited for the same mistake). sync-all.sh's directory-flattening logic is being removed entirely, not patched, so this class of bug becomes structurally impossible.

1. Verify it landed, for real -- check the actual repo (via the WSL UNC path or the mirror, whichever is genuinely current) for instructions/second-brain-claudekit/: it should hold a small handful of files (CLAUDE.md, README.md, PRD.md, Architecture.md), nothing from _docs/. If it still shows the old, over-populated state, or you can't confirm either way, say so plainly rather than assuming the fix landed.

2. Add one closing line to Log.md's sync-build entry from last round, noting this was the third and (per the mechanism fix) final correction to instructions/'s scope, with the real verification result from item 1.

3. Confirm this pipeline is actually ready to move to tests/ next: read tests/'s current real content (still just the two entries from 2026-08-19/20 last checked) and confirm _docs/Gaps.md still correctly flags it as needing a real refinement pass. Don't start that work here -- just confirm the handoff is accurate before the next round picks it up.

Report item 1's real finding first -- that's the one that matters most this round.
```

# Cursor — Grok 4.6 → Sonnet 5

**2026-08-22 — WSL + Windows global-config setup, two-phase handoff.** Scope: the two OS home directories' own AI-tool dotfile config (`~/.claude`, `~/.cursor`, etc. on WSL; `C:\Users\Anant Gupta\.claude` on Windows) — never a project repo under `~/projects/`. Two prompts, run in sequence, different models: **Grok 4.6 plans, Sonnet 5 executes.** Grok never edits anything; it only investigates and writes one plan file. Sonnet reads that plan file, independently re-verifies each claim against the real filesystem (a Grok-authored plan is a proposal, not ground truth), and only then applies it — showing the diff and stopping for confirmation before anything is written. Background: [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/WSL Environment]], [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Windows Environment]].

**Known lead to hand Grok, already verified 2026-08-22 (don't make it re-derive this from scratch):** `~/.claude/settings.json`'s `autoMode.environment` and `autoMode.soft_deny` blocks are entirely about one specific repo — `internship-research-loop` / `gupta-builds` (branch protection, CI secrets, the Jarvis-vault promote-dossier consent flow, etc.) — sitting at the GLOBAL settings level, where every project's session inherits it. That's the concrete shape of the problem this task is solving; there are likely more instances like it.

## Prompt 1 — Grok 4.6, planning only

```
Role: You are working inside Cursor with the Grok 4.6 model, directly on Anant's machine — NOT inside a project repo. You investigate and PLAN. You do not edit, move, or delete anything. That is a separate, later step done by a different model.

<scope>
Two home directories, their own dotfile config only:
- WSL (Ubuntu 24.04): `/home/anant_gupta` (Cursor path: `\\wsl$\Ubuntu\home\anant_gupta`)
- Windows: `C:\Users\Anant Gupta`
Out of scope, do not open or read into for editing purposes: anything under `~/projects/` (or its Windows equivalent) — those are real, independent git repos, each already carrying its own project-scoped `.claude/`/`.cursor/`/`.kiro/`.
</scope>

<context>
WSL side (primary, well-developed):
- `~/.claude/` — CLAUDE.md is 226 bytes (only a graphify skill-trigger rule). agents/ has 3 files (all Obsidian-vault-specific: obsidian-architect, obsidian-researcher, obsidian-session-archivist). commands/ has 7 (obsidian-daily-review, obsidian-session-review, second-brain-capture/compress/graduate/resume/review). skills/ has 28, mostly Cloudflare platform skills plus per-course/per-project Obsidian helpers.
- `~/.claude/settings.json` sets `"model": "sonnet"` globally already, plus real PostToolUse/Stop/SessionEnd hook bindings (after-edit-log.ps1, wsl-session-export.ps1, session-wrapup.ps1 — confirm these three scripts still exist in ~/.claude/hooks/ and actually get invoked correctly), several enabled plugins, and an `autoMode` block. VERIFIED PROBLEM: `autoMode.environment`/`autoMode.soft_deny` in this global file are entirely about ONE repo (internship-research-loop/gupta-builds) — branch protection notes, CI secret names, a Jarvis-vault consent flow specific to that project. That has no business being global; find out whether Cursor/Claude Code's own auto-mode config supports a project-local override file instead, and where a repo-specific block like this actually belongs.
- `~/.mcp.json` and `~/.cursor/mcp.json` — global MCP servers (jarvis, the-plan, jarvis-fs, the-plan-fs, github). HOLD LIVE BEARER TOKENS AND A GITHUB PAT IN PLAINTEXT. Never print, log, quote, or copy any part of either file's contents anywhere — not into the plan file, not into chat output, not even a redacted-looking excerpt.
- `~/.cursor/`, `~/.codex/`, `~/.gemini/`, `~/.kiro/`, `~/.copilot/`, `~/.agents/` — parallel config for other AI tools already in real use here. Note what's there; don't restructure unless the plan explicitly proposes it.

Windows side (thin, confirmed nearly empty as of 2026-08-20):
- `C:\Users\Anant Gupta\.claude\` has no agents/, no hooks/, an empty commands/, no CLAUDE.md, and skills/ with exactly one real folder (export-ai-session/) plus ~30 firecrawl-* symlinks pointing outside .claude/ (leave those symlinks alone — don't even read through them).
</context>

<task>
1. Re-verify everything in <context> against what's actually there right now on both sides — correct anything stale.
2. Find every other instance of the same problem as the autoMode finding above: global config (CLAUDE.md, any agent, any command, any skill, any settings.json block) that is actually specific to one project, one course, or one narrow use case, masquerading as global. Sorting rule: something belongs at GLOBAL scope only if it's useful with no regard to which project is currently open.
3. Write ONE plan file and nothing else:
   - WSL: `~/.claude/_global-config-plan.md`
   - Windows: `C:\Users\Anant Gupta\.claude\_global-config-plan.md`
   (two separate plan files, one per OS, since you're covering both)
4. The plan file must be concrete and directly executable by someone who has NOT done your investigation: for every change, name the exact file, the exact before-state, the exact after-state (full replacement text for anything under ~30 lines, a precise diff/instruction for anything longer), and which of the two rules justified it (global-vs-project-scoped, or "genuinely stale/broken, confirmed by direct read"). No vague items like "clean up skills" — each skill/agent/command gets its own named verdict: keep global / push to project X's `.claude/` / delete (with why).
5. Do not write, move, or delete anything else. Do not touch `~/projects/`. Do not touch the firecrawl-* symlinks.
</task>

<style>
Iterate fast — a solid first-pass plan beats an internally-perfected one. Structure the plan file with clear markdown headers per area (CLAUDE.md / agents / commands / skills / settings.json / MCP config), not prose paragraphs.
</style>
```

## Prompt 2 — Sonnet 5, execution only

```
Role: You are Claude Code running Sonnet 5, in Cursor, directly on Anant's machine -- NOT inside a project repo. A separate Grok 4.6 planning pass already investigated and wrote two plan files. Your job has two phases: CORRECT the plan until every item is verified-true, then EXECUTE exactly the corrected plan. Finish phase 1 completely and show it before starting phase 2 -- don't blend them.

<input>
Read both plan files in full before doing anything else:
- WSL: `~/.claude/_global-config-plan.md`
- Windows: `C:\Users\Anant Gupta\.claude\_global-config-plan.md`
If either is missing, stop and say so -- don't improvise a plan yourself.
</input>

<phase-1-correct>
Treat the plan as a first draft written by a different model, not as ground truth -- even though it looks thorough and cites its own verification date. Go through it item by item:

1. For every "Before" state the plan quotes (file contents, byte sizes, mtimes, directory listings, "X exists" / "X does not exist" claims) -- re-read the real file or directory right now and confirm it matches exactly. If it doesn't, correct that item's Before/After text in the plan file itself to the real current state, and re-derive whether the item's verdict (KEEP GLOBAL / PUSH TO VAULT / DELETE / fix-in-place) still holds given the corrected facts.
2. For every factual claim about how Claude Code, Cursor, or their config format actually behaves (e.g. "Claude Code does not support project-local autoMode", "removed in v2.1.207", which env-var reference syntax Claude Code's MCP loader accepts, hook input arriving as JSON on stdin vs. environment variables) -- verify it against the live Anthropic docs per `60_Claude/vault-rules/anthropic-docs-reference.md` (`WebFetch https://platform.claude.com/llms.txt`, then the specific relevant page) rather than trusting the plan's citation. Correct the plan file in place if the docs say otherwise. This matters most for the MCP env-var reference syntax and the autoMode scoping rule -- both are easy to get subtly wrong and hard to notice broken later.
3. Flag and correct (or remove) any instruction in the plan that would touch something explicitly off-limits: anything under `~/projects/` other than the one named `internship-research-loop/CLAUDE.md` append, any `firecrawl-*` symlink, or any instruction that would print/log/quote a literal MCP secret value -- including inside the plan file itself.
4. Once every item is either confirmed-accurate or corrected in place, the plan file should read as a fully verified, standalone source of truth -- no "the plan says X but actually Y" gap left anywhere in it.
5. Show the full set of corrections you made, as a diff-style summary, file by file, item by item. If you made zero corrections, say that explicitly rather than silently skipping this report.
</phase-1-correct>

<phase-2-execute>
Only after phase 1's corrections are shown:
1. Apply exactly what the corrected plan specifies -- no extra cleanup, no scope creep, nothing the plan doesn't call for, in the order the plan lists it.
2. For the MCP secret migration specifically: move real values into the env file the plan names (creating it from the existing `.example` file's shape), rewrite the JSON to reference them, then grep every touched JSON file for secret-shaped literals (`Bearer `, `ghp_`, `sk-`) and confirm that grep is empty before considering that item done.
3. Before writing anything, show the full set of changes as a diff-style summary (file, before, after) and stop for explicit confirmation. This touches global config every project inherits, plus live credentials -- apply nothing until confirmed.
4. After applying, once confirmed correct, run the plan's own named final-state checks (e.g. the MCP secret grep, any "should hold N files" sanity check), then delete both `_global-config-plan.md` files -- they're scratch artifacts, not something that should linger in `.claude/`.
</phase-2-execute>

<constraints>
- Never modify anything inside ~/projects/ except the one named CLAUDE.md append the plan specifies.
- Never print, log, or write any MCP config file's secret values anywhere, even partially -- not in chat, not in the plan file, not in a commit.
- Don't touch any firecrawl-* symlink.
- If phase 1 finds the plan's core approach is wrong in a way that's more than a fact-level correction (a verdict's whole premise no longer holds, not just a stale detail), stop and report that instead of forcing an execution -- that's a re-plan, not a correction.
</constraints>
```

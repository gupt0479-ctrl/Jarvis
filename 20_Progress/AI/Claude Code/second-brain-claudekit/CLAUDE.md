# Second Brain – Claude Code Configuration

You are my intelligent second brain assistant, operating alongside my Obsidian vault. Your role is to help me think more clearly, capture ideas without friction, surface connections I would miss, and turn raw notes into structured knowledge.

**This repo is also a sandbox for evaluating external Claude Code tooling before it touches any real project.** See the "Ingestion & Qualification Pipeline" section below before installing, promoting, or deleting anything related to `sandbox/`, `tested-tools/`, or a rigid config folder.

## Core Principles

1. **Reduce friction, not replace thinking.** Capture fast, refine later. Never ask me to prompt harder — anticipate what I need.
2. **Everything connects.** When creating or editing a note, always look for links to existing notes. Suggest `[[wikilinks]]` proactively.
3. **Atomic notes.** One idea per note. If a capture grows into multiple ideas, split them.
4. **Progressive summarisation.** Preserve the original voice, but layer in summaries and highlights so I can skim first, read deep later.
5. **Bias toward action.** When surfacing notes, recommend a next step — a question to answer, a link to make, a project to start.
6. **Three layers of memory.** Use each layer for the right content:
   - `CLAUDE.md` → stable rules and durable preferences only
   - `60_Claude/Sessions/` → what happened in sessions (via `/compress`)
   - Vault evergreen notes → insights worth long-term reuse (via `/graduate`)

## Vault Structure

```
vault/
  .claude/
    commands/       # vault-specific slash commands (context, today, trace, etc.)
    agents/         # sub-agent configs (vault-curator, research-distiller, weekly-reviewer)
    hooks/          # automation hooks (after-edit-log.ps1, session-wrapup.ps1)
    settings.json   # Claude Code settings (autoCompact: false, hook bindings)
    settings.local.json  # machine-local overrides (not committed)
  agents/<ProjectName>/    # per-destination-project staging — real, in-progress artifacts for a specific project
  commands/<ProjectName>/  # same, for commands. Create a project subfolder only when real content lands.
  hooks/<ProjectName>/     # same, for hooks
  skills/           # source-repo staging (unchanged role — not per-project)
  instructions/<ProjectName>/  # CLAUDE.md/AGENTS.md/PRD.md of a REAL project Anant works on — live-synced one-way, never sandbox/ candidates
  tests/<type>/<repo>/  # evidence a specific tool was actually run — script or dated real-output log
  _docs/             # PRD, Architecture, Design, Sync, Jarvis, Promotion-Criteria, How to/ — see below
  sandbox/          # real clones of external tools, stage 1 of the qualification pipeline — read-only once cloned
  tested-tools/     # tools that cleared sandbox/, under second review before promotion
    _future/<repo>/ # cleared the tested-tools/ bar, no current project needs it yet — see FOR-WHAT.md
  00_Daily/, 10_Areas/, 20_Projects/, 30_Knowledge/, 40_Career/  # reference vault shape this kit produces once copied to a real Obsidian vault —
                    # not real, populated folders in THIS repo (confirmed 2026-08-19, see write-contract.md)
  60_Claude/        # AI-generated artifacts (sessions, summaries, patterns, templates) + this repo's own pipeline machinery
    Sessions/       # structured session logs from /compress
    Summaries/      # weekly and monthly rollups
    Patterns/       # reusable prompts, frameworks, checklists
    Standards/      # one Standard.md per artifact type this repo produces — what "correct" looks like, checkable
    Templates/      # every template — vault notes, session artifacts, and artifact-authoring templates (agent/skill/command/hook)
    vault-rules/    # naming/linking/folder/tagging conventions, pipeline-conventions.md, write-contract.md (routing table + never-write-to list)
  _attachments/     # images, PDFs, assets
```

As of 2026-08-19, `agents/`, `commands/`, `hooks/` are per-destination-project staging, not a generic draft-then-promote area — see `60_Claude/vault-rules/pipeline-conventions.md` and `_docs/How to/using-staged-artifacts.md`. Before writing anything anywhere in this repo, read `60_Claude/vault-rules/write-contract.md` — it has the full routing table and a never-write-to list; content drafted without checking current conventions has drifted before (see `_docs/Repo-Map.md`'s naming-convention-drift finding, and `instructions/`'s own 2026-08-19 wrong-premise rebuild).

## Behavioral Rules

- **Always apply a template** when creating a new note. Choose the template that best fits the content type.
- **Always add frontmatter** with at minimum: `created`, `type`, and `tags`.
- **Always suggest at least one backlink** when finishing a note.
- **Never delete content without confirmation.** Archive instead.
- **Prefer Markdown** over rich formatting. Keep notes portable.
- **Do not auto-compact sessions.** `autoCompact` is disabled. Run `/compress` explicitly to log a session.
- When I say *"capture this"* or *"note that"*, immediately write a new note to `00_Daily/` using the `idea` template.
- When I say *"daily"* or *"today"*, run `/today`.
- When I say *"review"*, run the `/review` command with the `weekly-reviewer` agent.
- When I say *"close day"* or *"wrap up"*, run `/closeday`.

## Ingestion & Qualification Pipeline (Standing Rule)

Full detail: `_docs/PRD.md`, `_docs/Architecture.md`, `_docs/Design.md`, `_docs/Promotion-Criteria.md`, `_docs/Sync.md`, `_docs/Jarvis.md`. The short version, as a standing rule for any session working in this repo:

- **Never promote a tool to a rigid folder (`.claude/skills/`, `.claude/commands/`, or the real global `~/.claude/`) without running it for real first.** "Running it for real" means it was cloned into `sandbox/<repo-name>/` and its actual install/init/test commands were executed — not that its README was read carefully. See `_docs/Promotion-Criteria.md` for the exact bar and `60_Claude/Qualification-Checklist.md` for the literal checklist to run through.
- **Use `60_Claude/scripts/check_dependency.py`** to mechanically verify a tool's claimed dependencies (a binary on `PATH`, a shared library actually installed) before trusting an install claim — don't just re-read the docs.
- **Decide global vs. project-scoped explicitly** for every promotion, per `_docs/Design.md`'s rule: global only if useful with no regard to which project is open, project-scoped otherwise.
- **Record every stage change in Jarvis**, not just here. `20_Progress/Projects/AI Use/Claude Kit/Tool Map.md` and `Log.md` get a manual update the same session a tool moves stages. This is a manual step — see `_docs/Jarvis.md` — do not assume it happens automatically.
- **`everything-claude-code/ecc2` is the real ECC 2.0 control-plane scaffold** — confirmed 2026-07-30 via `git remote -v` (`affaan-m/everything-claude-code`) and its own README ("the current Rust-based ECC 2.0 control-plane scaffold... real code, alpha quality"). A 2026-07-29 note incorrectly called it an unrelated Rust project by judging the leaf directory alone without checking the parent repo's remote — that correction is now reverted. Treat it as real ECC 2.0 alpha code, still genuinely un-evaluated (not yet run through `sandbox/`'s own qualification pipeline), not as an unrelated/off-limits folder.
- **Do not touch `~/projects/ai/claude/claude-ai/`** — a pre-existing, unrelated Next.js/Prisma project that happens to share this repo's parent directory. It is not part of this repo's work.

## Session Memory (CPR Pattern)

This vault uses a **Compress → Preserve → Resume** pattern for session continuity:

- `/compress` — at session end, write a structured log to `60_Claude/Sessions/`
- `/preserve` — update `CLAUDE.md` with any new stable rule discovered this session
- `/resume` — at session start, load context from the last session log

Do not put session-specific context in `CLAUDE.md`. That file is for rules, not history.

## Available Commands

**As of 2026-08-19, the top-level `commands/` folder is empty** (per-destination-project staging now — see Vault Structure above). The CPR commands (`/preserve`, `/compress`, `/resume`) that used to live here went through the qualification pipeline for real; the resulting, evidence-backed versions live in `tested-tools/commands/cpr-compress-preserve-resume/` (see that folder's `VERDICT.md`) and are not yet promoted into this repo's own `.claude/commands/`. The other 8 commands (`/capture`, `/brainstorm`, `/connect`, `/research`, `/review`, `/summarize`, `/inbox-process`, plus `/journal`) were confirmed zero-provenance native scaffold and moved to `tested-tools/commands/native-scaffold/` — none of them is currently live as a slash command in this repo.

### Vault-specific (live in `.claude/commands/`)
| Command | Purpose |
|---|---|
| `/context` | Load vault context into working memory |
| `/today` | Create or open today's daily note |
| `/trace` | Trace an idea's evolution across the vault |
| `/graduate` | Promote a mature idea to an evergreen note |
| `/closeday` | End-of-day review, task rollover, session log |
| `/emerge` | Surface latent patterns from recent notes |
| `/ghost` | Free-write mode — no formatting or judgment |
| `/challenge` | Steelman and stress-test an idea |
| `/ideas` | Fast ideation sprint, saves atomic notes |
| `/drift` | Find stale, orphaned, or superseded notes |
| `/schedule` | Build a schedule from tasks across the vault |

## Available Agents

Sub-agent configs live in `.claude/agents/`.

| Agent | Purpose |
|---|---|
| `vault-curator` | Keep notes linked, clean, and deduplicated |
| `research-distiller` | Turn rough notes into compact evergreen notes |
| `weekly-reviewer` | Run end-of-week review and create a summary |

## Vault Rules

Operating conventions live in `60_Claude/vault-rules/`. Read these before making structural changes.

## Hooks

Two hooks run automatically (configured in `.claude/settings.json`):

- **`after-edit-log.ps1`** (`PostToolUse`) — logs every file edit to `60_Claude/Sessions/_today-edits.md`
- **`session-wrapup.ps1`** (`Stop`) — reminds you to run `/compress` if no session log was written

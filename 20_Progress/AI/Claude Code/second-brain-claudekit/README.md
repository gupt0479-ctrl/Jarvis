# second-brain-claudekit

A Claude Code kit for building and operating a powerful second brain with Obsidian + Claude. Designed to minimise prompting friction so you can focus on thinking and content.

**This repo's primary job is the qualification pipeline, not the starter-kit shape below.** It looks like a shareable Claude Code kit — `.claude/`, `commands/`, templates, a copy-paste Quick Start — but that resemblance is structural, not the point (see `_docs/Design.md`). The real purpose is deciding, with real evidence, what Claude Code tooling is actually worth trusting: `sandbox/` (real clones, run for real) → `tested-tools/` (cleared the bar, under second review) → promoted, either into this repo's own `.claude/`, a specific other project, or Jarvis's real `.claude/`. Start with `_docs/PRD.md`, `_docs/Architecture.md`, and `_docs/Repo-Map.md` before touching anything below.

---

## Structure

```
second-brain-claudekit/
  CLAUDE.md                   ← root config: stable rules, vault layout, CPR session pattern
  .gitignore

  .claude/                    ← Claude Code project config (copy to your vault root)
    commands/                 ← vault-specific slash commands
    agents/                   ← sub-agent configs
    hooks/                    ← PowerShell automation hooks
    settings.json             ← hook bindings, autoCompact: false
    settings.local.json       ← machine-local overrides (gitignored)

  agents/<ProjectName>/       ← per-destination-project staging (real, in-progress artifacts for one project)
  commands/<ProjectName>/     ← same, for commands
  hooks/<ProjectName>/        ← same, for hooks
  skills/                     ← source-repo staging (currently empty)
  instructions/<ProjectName>/ ← CLAUDE.md/AGENTS.md/PRD.md of a REAL project — live-synced one-way, never sandbox/ candidates
  tests/<type>/<repo>/        ← evidence a specific tool was actually run
  _docs/                      ← this repo's own reasoning/architecture docs (PRD, Architecture, Design, Sync, Jarvis, Promotion-Criteria, How to/) — the ONE docs folder in this repo

  00_Daily/, 10_Areas/, 20_Projects/, 30_Knowledge/, 40_Career/
                              ← reference vault shape this kit produces once copied to a real Obsidian vault —
                                not real, populated folders in this repo itself (see write-contract.md)
  60_Claude/                  ← AI-generated artifacts + this repo's own pipeline machinery
    Sessions/                 ← session logs from /compress
    Summaries/                ← weekly/monthly rollups
    Patterns/                 ← reusable prompts and frameworks
    Standards/                ← one Standard.md per artifact type — what "correct" looks like, checkable
    Templates/                ← every template — vault notes, session artifacts, artifact-authoring templates
    vault-rules/               ← vault conventions, pipeline-conventions.md, write-contract.md (routing table + never-write-to list)
```

---

## Quick Start

### 1. Set up Claude Code in your vault

```sh
# Copy the .claude/ folder to your Obsidian vault root
cp -r .claude/ ~/your-vault/.claude/

# Copy CLAUDE.md to your vault root
cp CLAUDE.md ~/your-vault/CLAUDE.md
```

### 2. Install commands

As of 2026-08-19, the top-level `commands/` folder is per-destination-project staging, not a flat global set — see `_docs/How to/using-staged-artifacts.md`. To install a specific, already-qualified command set (e.g. the CPR pattern):

```sh
mkdir -p ~/.claude/commands/
cp tested-tools/commands/cpr-compress-preserve-resume/*.md ~/.claude/commands/
```

### 3. Install Obsidian templates

Copy `60_Claude/Templates/*.md` into your vault and configure Obsidian Templater to point there. All templates — vault-note templates and AI session-artifact templates alike — live in this one folder; there is no separate Templater-only folder.

### 4. Create the vault folder structure

Create these folders in your vault if they don't exist:
`00_Daily/`, `10_Areas/`, `20_Projects/`, `30_Knowledge/`, `40_Career/`, `60_Claude/Sessions/`, `60_Claude/Summaries/`, `60_Claude/Patterns/`, `60_Claude/Templates/`

Copy `60_Claude/Templates/*.md` into your vault's `60_Claude/Templates/`.

### 5. Start a session

```
/context   ← loads vault state into Claude's working memory
/today     ← opens or creates today's daily note
```

---

## Commands

**As of 2026-08-19, no commands are staged flat in the top-level `commands/` folder** — see `_docs/How to/using-staged-artifacts.md`. Two real outcomes exist instead:

- `tested-tools/commands/cpr-compress-preserve-resume/` — `/compress`, `/preserve`, `/resume`, blended from this repo's original hand-authored versions and the real `EliaAlberti/cpr-compress-preserve-resume` repo after both were run for real. See that folder's `VERDICT.md`.
- `tested-tools/commands/native-scaffold/` — `/capture`, `/brainstorm`, `/connect`, `/research`, `/review`, `/summarize`, `/inbox-process`, `/journal`: confirmed zero external provenance, not yet individually tested or promoted.

### Vault-specific (live in `.claude/commands/`)

| Command | Purpose |
|---|---|
| `/context` | Load vault context into Claude's working memory |
| `/today` | Create or open today's daily note |
| `/trace` | Trace an idea's evolution across the vault |
| `/graduate` | Promote a mature idea to an evergreen note |
| `/closeday` | End-of-day: review, task rollover, session log |
| `/emerge` | Surface latent patterns from recent notes |
| `/ghost` | Free-write mode — no formatting or judgment |
| `/challenge` | Steelman and stress-test an idea |
| `/ideas` | Fast ideation sprint, saves atomic notes |
| `/drift` | Find stale, orphaned, or superseded notes |
| `/schedule` | Build a schedule from tasks across the vault |

---

## Agents

Three sub-agents, each with a focused mandate:

| Agent | Purpose |
|---|---|
| `vault-curator` | Keeps notes linked, clean, and deduplicated |
| `research-distiller` | Turns rough notes into compact evergreen notes |
| `weekly-reviewer` | Runs end-of-week review, creates weekly summary |

---

## Hooks

Two hooks run automatically via `.claude/settings.json`:

| Hook | Trigger | Effect |
|---|---|---|
| `after-edit-log.ps1` | After any file edit | Appends a log entry to `60_Claude/Sessions/_today-edits.md` |
| `session-wrapup.ps1` | Session end | Reminds you to run `/compress` if no session log was written |

Both are PowerShell scripts — compatible with Windows and WSL (pwsh).

---

## Session Memory: CPR Pattern

The kit uses a **Compress → Preserve → Resume** loop:

1. **`/compress`** — at session end, writes a structured log to `60_Claude/Sessions/`
2. **`/preserve`** — updates `CLAUDE.md` with any new durable rule from the session
3. **`/resume`** — at session start, loads context from the last log

`autoCompact` is disabled in `settings.json` so you control exactly when compression happens.

**Three layers of memory — use each for the right thing:**

| Layer | What goes here |
|---|---|
| `CLAUDE.md` | Stable rules, durable preferences |
| `60_Claude/Sessions/` | What happened in sessions |
| Vault evergreen notes | Insights worth long-term reuse |

---

## Vault Layout

| Folder | Purpose |
|---|---|
| `00_Daily/` | Daily notes (`YYYY-MM-DD.md`) |
| `10_Areas/` | Ongoing responsibilities |
| `20_Projects/` | Active, time-bounded projects |
| `30_Knowledge/` | Evergreen notes, literature, research |
| `40_Career/` | Career and professional development |
| `60_Claude/` | AI artifacts (sessions, summaries, patterns, templates) |

See `60_Claude/vault-rules/folder-structure.md` for full conventions.


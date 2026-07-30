---
type: project
status: active
created: 2026-07-30
updated: 2026-07-30
tags:
  - claude-code
  - sync
  - unison
  - claude-kit
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
next: "Get Anant's per-project go-ahead (Step 0), then bootstrap the manifest-driven script and onboard the first additional project"
---
# Sync — Unison, multi-project rollout

This is the **how**: the operational procedure for making the Unison-based `.claude/` sync work across every real project, repeatably, not just the one project (`second-brain-claudekit`) it's already proven on. The **why Unison** research and the first working, tested implementation live in the repo itself: `second-brain-claudekit/Docs/Sync.md` and `50_Claude/scripts/sync-jarvis.sh` — read those first if the tool choice itself is in question. This note assumes that choice is settled and is only about scaling it.

(Correction made while writing this: the file was requested as "Sync - Unious.md" — that's not a real word and doesn't match the tool being documented, so this is named `Sync - Unison.md` instead.)

## The verified project map

Confirmed 2026-07-30 by actually running `git remote -v` and listing `.claude/` in every real WSL project directory — not inferred from folder names, not assumed from what's already dumped in this vault. This is the ground truth the rest of this note is built on.

### Existing Jarvis dump folders with a confirmed live WSL source

| Jarvis folder | Real WSL path | git remote | What's actually in `.claude/` | Root `CLAUDE.md`? |
|---|---|---|---|---|
| [[20_Progress/AI/Claude Code/second-brain-claudekit/Setup\|second-brain-claudekit]] | `~/projects/ai/claude/second-brain-claudekit` | (this repo itself) | `agents/`, `commands/`, `hooks/`, `settings.json` | yes | 
| [[20_Progress/AI/Claude Code/CausalOps/Setup\|CausalOps]] | `~/projects/hub/CausalOps` | `gupta-builds/CausalOps` | `agents/`, `commands/`, `hooks/`, `settings.local.json` (no committed `settings.json`) | yes |
| [[20_Progress/AI/Claude Code/Portfolio/Setup\|Portfolio]] | `~/projects/hub/portfolio` | `gupta-builds/Portfolio` | `agents/`, `commands/`, `docs/`, `CLAUDE.md` (**inside** `.claude/`, not at repo root — different shape from every other project here), `cosmic-frontend.mdc`, `settings.local.json`, plus a `scheduled_tasks.lock` runtime file that must never be synced | no (it's `.claude/CLAUDE.md` instead) |
| [[20_Progress/AI/Claude Code/Trading View/Setup\|Trading View]] | `~/projects/hub/tradingview` | `gupta-builds/TradingView` | `agents/`, `hooks/`, `skills/`, `settings.json`, `settings.local.json` (no `commands/`) | yes |
| [[20_Progress/AI/Claude Code/Resq/Setup\|Resq]] | `~/projects/hackathon/Resq` | `gupta-builds/Resq` | No `agents/`/`commands/`/`hooks/` at all — this project's `.claude/` is agent-handoff docs: `PRD.md`, `README.md`, `context/`, `playbooks/`, `decisions/`, `checklists/`, `settings.json` | no |
| [[20_Progress/AI/Claude Code/OpsPilot/Setup\|OpsPilot]] | `~/projects/hackathon/opspilot` | `gupta-builds/opspilot` | Same handoff-doc shape as Resq, plus `workflows/`: `PRD.md`, `README.md`, `context/`, `playbooks/`, `workflows/`, `decisions/`, `checklists/` | yes |
| [[20_Progress/AI/Claude Code/Jarvis/Setup\|Jarvis]] | `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude` (this vault's own root) | n/a — not a git repo | `agents/`, `commands/`, `skills/`, `context/`, `rules/`, `settings.json`, `settings.local.json` | no |

**Every row above except Jarvis itself is a real `.claude/` shape, individually verified — none of them match each other, and none should be assumed to match `second-brain-claudekit`'s shape when building that project's manifest entry.** The `-path` list per project has to be built from its own real listing, every time.

### Confirmed real repos, not yet tracked in this vault at all

| WSL path | git remote | `.claude/` contents | In Jarvis today? |
|---|---|---|---|
| `~/projects/work/gupta-builds` | `gupta-builds/gupta-builds` | `settings.local.json` only — nothing else to sync yet | No folder exists |
| `~/projects/work/internship-research-loop` | `gupta-builds/internship-research-loop` | `agents/`, `skills/`, `settings.json`, `settings.local.json`, root `CLAUDE.md` | No folder exists |
| `~/projects/umn/boom` | `gupta-builds/boom` | No `.claude/` directory exists in this repo at all | No folder exists |
| `~/projects/hub/DNA_BJJ_APP`, `~/projects/hub/GymMangment_app_demo` | both `NafCodes/...` (not `gupta-builds`) | Both have `.claude/` | No folder exists |

These are real and confirmed to exist, but adding any of them is a bigger step than onboarding CausalOps/Portfolio/etc. — there's no existing Jarvis folder to migrate, so it's "create a new tracked project" not "wire up sync for an existing dump." Also worth noting explicitly: BOOM has no `.claude/` at all right now, so there is nothing to sync until one is built there first — this isn't a sync-mechanism gap, the source simply doesn't exist yet.

### Named but not found anywhere in the real WSL project tree

- **The Plan** — no repository by this name or anything similar exists under `~/projects`. This vault has a separate MCP connection literally called "the-plan," which strongly suggests "The Plan" is a *different Obsidian vault*, not a code project with a `.claude/` folder to sync. Treat its existing dump folder here as a historical snapshot only, not a live-sync candidate, until that's confirmed one way or the other.
- **Github ReadMe** — searched for any repo matching this name; nothing found. Its own `Setup.md` already says the folder is empty except one settings file — consistent with there being no real live source to sync against at all.

### Deliberately excluded, permanently, not a "not yet" — a "never"

`.claude_windows/` and `.claude_wsl/` — full raw one-time copies of `~/.claude` (WSL) and its Windows equivalent, including a live `.credentials.json`. `MOC.md` already excludes both from tracking. **Never point a sync script at either of these.** They are backups of secrets and session state, not project configuration, and syncing them would turn a one-time credential leak into a continuously-refreshed one.

## Step 0 — Per-project go-ahead

A confirmed real source path is a fact, not a decision. Before any project above moves from "mapped" to "live," it needs an explicit yes from Anant, per project, because "this vault holds a reference dump of X" and "this vault holds a live mirror of X" are different intentions — the first says "frozen on purpose," the second says "keep this current." Silently upgrading one to the other changes what the folder means without anyone deciding that on purpose.

Practically: the manifest (Step 2) carries a `status` field per project — `candidate` (path confirmed, not wired) or `live` (wired, tested, running). Nothing moves from `candidate` to `live` without that go-ahead being given and recorded (a one-line note in this file's changelog, or in `Claude Kit/Log.md`, is enough — it doesn't need its own ceremony).

## Step 1 — Classify the pairing

Two categories, and the classification decides one flag (`needs_fat`):

- **WSL ↔ Windows** (crossing the DrvFs boundary — `/mnt/d/...` from a WSL-side path): DrvFs cannot hold real POSIX permission bits, so Unison's default post-copy `chmod` fails on every file. Needs `-fat` (disables chmod, treats names case-insensitively, skips symlinks — all correct for this pairing, confirmed by testing on `second-brain-claudekit`). **This is every single project in the table above except Jarvis itself** — `second-brain-claudekit`, CausalOps, Portfolio, Trading View, Resq, and OpsPilot all live under `~/projects/...` on WSL's own ext4 filesystem, paired against a Windows-side (`D:\...`) mirror.
- **Windows ↔ Windows** (same NTFS volume, no WSL boundary crossed): only **Jarvis's own `.claude/`** falls here — both the source (`D:\...\Jarvis\.claude`) and the mirror (`D:\...\Jarvis\20_Progress\AI\Claude Code\Jarvis\`) are on the same drive. No permission-bit problem, so `-fat` is not needed (and shouldn't be set — no reason to force case-insensitivity or disable symlink-following where the underlying filesystem doesn't require it).

## Step 2 — One manifest-driven script, not one script per project

`50_Claude/scripts/sync-jarvis.sh` (the current, working, single-project script) hardcodes one repo/mirror pair. Before a second project gets wired up for real, it should be replaced by a manifest + driver pair so that onboarding project N+1 is "add one entry," not "copy and hand-edit a whole script."

**Manifest** (`second-brain-claudekit/50_Claude/sync-manifest.json`), one entry per project:

```json
{
  "projects": [
    {
      "name": "second-brain-claudekit",
      "status": "live",
      "repo_root": "/home/anant_gupta/projects/ai/claude/second-brain-claudekit",
      "mirror_path": "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit",
      "paths": [".claude/agents", ".claude/commands", ".claude/hooks", ".claude/settings.json", "CLAUDE.md"],
      "needs_fat": true
    },
    {
      "name": "CausalOps",
      "status": "candidate",
      "repo_root": "/home/anant_gupta/projects/hub/CausalOps",
      "mirror_path": "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/CausalOps",
      "paths": [".claude/agents", ".claude/commands", ".claude/hooks", "CLAUDE.md"],
      "needs_fat": true
    },
    {
      "name": "Portfolio",
      "status": "candidate",
      "repo_root": "/home/anant_gupta/projects/hub/portfolio",
      "mirror_path": "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/Portfolio",
      "paths": [".claude/agents", ".claude/commands", ".claude/docs", ".claude/CLAUDE.md", ".claude/cosmic-frontend.mdc"],
      "needs_fat": true
    },
    {
      "name": "Trading View",
      "status": "candidate",
      "repo_root": "/home/anant_gupta/projects/hub/tradingview",
      "mirror_path": "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/Trading View",
      "paths": [".claude/agents", ".claude/hooks", ".claude/skills", ".claude/settings.json", "CLAUDE.md"],
      "needs_fat": true
    },
    {
      "name": "Resq",
      "status": "candidate",
      "repo_root": "/home/anant_gupta/projects/hackathon/Resq",
      "mirror_path": "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/Resq",
      "paths": [".claude/PRD.md", ".claude/README.md", ".claude/context", ".claude/playbooks", ".claude/decisions", ".claude/checklists"],
      "needs_fat": true
    },
    {
      "name": "OpsPilot",
      "status": "candidate",
      "repo_root": "/home/anant_gupta/projects/hackathon/opspilot",
      "mirror_path": "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/OpsPilot",
      "paths": [".claude/PRD.md", ".claude/README.md", ".claude/context", ".claude/playbooks", ".claude/workflows", ".claude/decisions", ".claude/checklists"],
      "needs_fat": true
    },
    {
      "name": "Jarvis",
      "status": "candidate",
      "repo_root": "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis",
      "mirror_path": "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/Jarvis",
      "paths": [".claude/agents", ".claude/commands", ".claude/skills", ".claude/context", ".claude/rules", ".claude/settings.json"],
      "needs_fat": false
    }
  ]
}
```

Note `.claude/settings.local.json` is excluded from every entry's `paths` list on purpose (machine-local, never meant to travel), and Portfolio's `scheduled_tasks.lock` is excluded because it's runtime state, not configuration — neither belongs in a `paths` list even though they physically live inside the source `.claude/` folder.

**Driver script** (`sync-all.sh`, replacing direct calls to `sync-jarvis.sh`):
- Reads the manifest, skips any entry whose `status` isn't `live`.
- For each live entry, acquires its own lock file (named per project, e.g. `/tmp/claudekit-sync-<name>.lock`) so one stuck project can't block the others.
- Invokes Unison with that entry's `repo_root`, `mirror_path`, one `-path` flag per item in `paths`, `-batch -auto -ui text -terse`, and `-fat` only if `needs_fat` is true.
- Appends one line per project to that project's own `Sync-Log.md` inside its mirror folder — exactly the pattern already working for `second-brain-claudekit`.
- Prints (and optionally writes to a single combined `_All-Projects-Sync-Log.md`) a one-line summary per project at the end of a full run, so a 15-minute run across every live project is skimmable at a glance instead of requiring opening N separate log files.

## Step 3 — Bootstrap each project exactly once

For each project moving from `candidate` to `live`:

1. **Shape the mirror folder first.** Several existing dump folders (Resq, OpsPilot especially) are flat one-time exports, not structured to hold exactly the subpaths in the manifest's `paths` list. Before the first sync, make sure the mirror folder's existing content matches what the manifest expects to place there — rename/restructure if the current dump doesn't already line up, so the first sync is a clean parity check, not a folder-shape migration disguised as a sync.
2. **Run the first sync and read the "no archive found" warning, don't dismiss it.** This is expected on a first run — Unison is telling you it has no baseline and will treat every difference as new-file-propagation rather than a change. Confirm the file counts it reports match what you expect before moving on.
3. **Expect and fix a first-run failure.** On `second-brain-claudekit`, the real first run failed on every file with a permissions error specific to DrvFs; the fix was `-fat`. Something project-specific may well break on the next project too (case-sensitivity clash, a file DrvFs can't represent, whatever). Treat a clean first run as slightly suspicious, not as proof nothing needed checking.

## Step 4 — Prove it before trusting it

Before flipping a project's `status` to `live` in the manifest for real, per project, repeat the two tests that mattered on `second-brain-claudekit` — not as a formality, as the actual gate:

1. Edit a real file on the Jarvis-mirror side, run the sync, confirm the edit lands back in the WSL repo.
2. Edit the *same* file differently on both sides between two sync runs, run the sync, confirm the run reports it as skipped (not silently resolved) and that both edits are still intact afterward.

Only after both pass for a given project does its `status` become `live` in the manifest.

## Step 5 — Update the tracking layer per project

Once a project is genuinely `live`:
- Rewrite that project's own `Setup.md` to say so plainly (model: [[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]) instead of leaving "last diffed on [date]" language that implies a stale one-time comparison.
- Update its row in [[20_Progress/AI/Claude Code/MOC]]'s project table from its current status (`stale`/`static`/`draft`/`dead`) to `live-synced`.
- Add a dated entry to [[20_Progress/Projects/AI Use/Claude Kit/Log]] the same session it happens — this file's own append-only rule.

## Step 6 — One trigger, centrally, for every live project

Not one Windows Task Scheduler entry per project — one entry that calls the manifest-driven driver script (Step 2), which internally loops every `live` project. Adding a project to the automated rotation from then on is a manifest edit (`status: candidate` → `status: live`), not a new scheduled task. Current cadence: every 15 minutes, invoking `wsl.exe -e ~/.local/bin/unison`-backed `sync-all.sh` — applies uniformly to every project the manifest marks `live`, present or future.

## Making it faster and lower-friction as more projects get added

- **Skip untouched projects before invoking Unison at all.** A cheap `find <repo_root> -newer <mirror>/.last-sync-marker` (or comparing directory mtimes) before running the full Unison pass on a project that hasn't changed on either side avoids paying Unison's update-detection cost on every single 15-minute tick for every project, most of which won't have changed most of the time.
- **Run independent projects' syncs in parallel, not sequentially.** Each project pair is fully independent (different `repo_root`, different `mirror_path`, separate lock file) — the driver script can fan them out concurrently instead of looping one at a time, which matters once the manifest holds six-plus entries instead of one.
- **`-fastcheck true`** (Unison preference, safe default for this use case) skips a full content hash when a file's size and modification time haven't changed since the last sync, instead of always doing a full comparison — meaningful once mirrors grow past a handful of files each.
- **One combined summary log** (as described in Step 2) instead of requiring a person to open N `Sync-Log.md` files to know whether last night's run was clean — a single glance at `_All-Projects-Sync-Log.md` should answer "did anything need attention" before anyone opens a per-project log at all.
- **Keep the manifest as the single source of truth for what's live.** Resist the urge to special-case a project's sync behavior directly in the driver script — if a project genuinely needs different handling, that's a new manifest field (like `needs_fat` already is), not a branch in the script that only applies to one name.

## Links
[[20_Progress/AI/Claude Code/MOC]] · [[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]] · [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]] · [[20_Progress/Projects/AI Use/Claude Kit/Log]]

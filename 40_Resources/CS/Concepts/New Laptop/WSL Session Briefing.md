---
type: note
status: sprout
created: 2026-08-26
updated: 2026-08-26
course: Life
track:
  - laptop
prerequisites:
  - "[[Ubuntu - WSL]]"
  - "[[New Laptop Setup]]"
  - "[[Jarvis MCP and REST API Setup]]"
related:
  - "[[New Laptop Setup]]"
  - "[[Ubuntu - WSL]]"
  - "[[Jarvis MCP and REST API Setup]]"
  - "[[VS Code Professional Setup]]"
tags:
  - note
---
# WSL Session Briefing

## Why this note exists

Two Windows-side sessions (2026-08-25, 2026-08-26) fixed this laptop's native-Windows coding environment: global VS Code Python/Node settings, Pylance excludes, git identity, npm cache location. Both sessions deliberately made **zero reads, edits, or commands against WSL** — this note is the complete handoff for the dedicated WSL session that picks up where they stopped. Read this entire note before touching anything. It is written to be self-sufficient: a WSL session should not need to re-derive facts already established here.

## Scope for the WSL session — read this section twice

**In scope: the WSL home directory (`/home/anant_gupta`) and everything inside it** — dotfiles, tool installs (nvm/fnm, npm/pnpm, uv, git config), `~/projects/` layout, `~/.mcp.json`, VS Code Server leftovers, crash dumps, shell profile cleanup (`.bashrc`, `.profile`, `.zshrc`), and establishing the same "coding environment reliability" standard the Windows side now has (correct interpreter/version resolution every time a directory is opened, no silent fallbacks).

**Explicitly out of scope — do not do these, they belong to the user directly, on the Windows side:**
- Any C: or D: drive cleanup, disk analysis, or file deletion outside the WSL filesystem itself.
- VHDX compaction (`wsl --shutdown` + `diskpart`/`Optimize-VHD`) — this is a Windows-host operation, not something run from inside the Linux distro, and the user is handling it personally.
- Anything under `/mnt/c` or `/mnt/d` **except reading** the Jarvis vault notes referenced below (read-only, through the 9P bridge, which is fine for a handful of markdown files even though it's slow for heavy workloads — see [[Ubuntu - WSL]]).
- Re-partitioning, reinstalling Windows apps, or anything Windows-side already covered by the two prior sessions (see their fixes list below) — do not redo or second-guess that work.

**The one exception inside "WSL home directory cleanup" that touches something Windows-visible:** writing a WSL-native `~/.mcp.json` (a task explicitly assigned below) — this is still a WSL-home-directory dotfile, not a Windows-drive operation, so it is in scope.

## Required reading before any action (in this order)

1. **This note, in full** (you're reading it).
2. `/home/anant_gupta/.claude/plans/new-laptop-setup.md` — the authoritative, deeper WSL2 reference manual for this exact machine. Neither Windows session read this (it lives inside WSL). Per [[New Laptop Setup]], this file's Part 13 cleanup was already validated once by actually running it on this machine — treat its answers as correct wherever they disagree with the shallower Windows-side doc summarized below.
3. [[Ubuntu - WSL]] — the VHDX mental model (why `rm -rf` doesn't shrink the disk image, why `/mnt/c`/`/mnt/d` is 5-20x slower, the three-worlds framing).
4. [[New Laptop Setup]] — the index note and the Windows-vs-WSL conflict table (reproduced in full below so you don't have to cross-reference).
5. [[Jarvis MCP and REST API Setup]] — the MCP wiring, including the specific WSL gap assigned to you below.
6. [[VS Code Professional Setup]] — the Windows-side VS Code findings note; skim for the Remote-WSL section since VS Code Server behavior inside WSL is your responsibility, not the Windows session's.

**If the Jarvis MCP tools (`mcp__jarvis__*`) are not available in this session** (the WSL-native `~/.mcp.json` doesn't exist yet — see below, this is expected), read these notes directly via the filesystem instead: `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/40_Resources/CS/Concepts/New Laptop/*.md`. Read-only access through the 9P bridge for a handful of markdown files is fine; do not build or run anything from that path.

## What the Windows-side sessions already fixed (context, not yours to redo)

- Global VS Code `python.defaultInterpreterPath` corrected to the Windows layout (`.venv/Scripts/python.exe`), plus `files.exclude`/`search.exclude`/`python.analysis.exclude` added globally (fixed a Pylance warning caused by opening the home directory as a workspace with 865k+ `AppData` items unexcluded).
- Windows git identity was wrong (work email `anant.gupta@in.nspglobaltech.com` instead of personal) — fixed to `anantmahi721@gmail.com` / "Anant Gupta", plus `core.autocrlf false`, `init.defaultBranch main`, `pull.rebase true`. **Check whether the equivalent WSL git identity has the same problem** — the original audit (Sin 9, below) found WSL git using `gupt0479@umn.edu`, a *third* email, different from both Windows identities. Resolve this explicitly; don't assume which email is "correct" without checking what the user actually wants for WSL commits.
- Windows npm cache redirected to `D:\npm-cache`. A manual (not automatic) `New-PyEnv` PowerShell function was added for bootstrapping `.venv` projects — deliberately *not* an automatic hook, matching this user's established preference for manual/opt-in tooling over silent automation (see the "no auto-hooks" pattern below).
- Miniconda was flagged for possible removal but **the user overruled this — it's being kept** on Windows for future Jupyter/notebook work. Not relevant to WSL, but worth knowing the user's stance: don't remove tools speculatively.
- `~/.mcp.json` (Windows) and the Jarvis vault's project-local `.mcp.json` were both re-verified and are already correct (env-var-substituted tokens, right port defaults) — an earlier version of the Jarvis MCP note wrongly described bugs here that had already been fixed; that note has since been corrected.

## The original honest audit (source: `C:\Users\Anant Gupta\new-laptop-setup.md`, Part 0, written 2026-06-02) — WSL-relevant sins only

**Sin 1 — WSL was on C: by default.** Already moved to `D:\WSL\Ubuntu\ext4.vhdx` (97.4 GB as of the 2026-08-26 WizTree scan) before this note existed, but the move was messy — this is the "extremely complicated and corrupted" state the user described. Investigate current health; do not assume the move was clean.

**Sin 3 — Node managed two different ways.** WSL side specifically: **nvm with 4 installed versions (v20.20.0, v24.12.0, v24.13.1, v24.14.1) and no working default** — `node` fails depending on how the shell was opened, because nvm lazy-loads and the default alias isn't reliably active. The newer source doc (`/home/anant_gupta/.claude/plans/new-laptop-setup.md`) specifies **fnm, not nvm** (~5ms shell init vs nvm's 70–700ms) — per the conflict table below, fnm wins. This is a real, concrete task: audit the current Node/nvm state, decide with the user whether to migrate to fnm or fix nvm's default-alias problem in place, and don't leave 4 stale versions installed regardless of which tool wins.

**Sin 4 — npm cache.** WSL npm cache (`~/.npm`, ~6 GB) lives inside the VHDX, which is already on D: — no redirection needed, this one was never actually broken. Just clean it (`npm cache clean --force`) as part of general hygiene.

**Sin 9 — git identity fragmentation.** WSL git identity was `gupt0479@umn.edu` (a UMN email, different from both Windows identities found and fixed this session). No `.gitconfig` conditional includes existed. The deeper WSL source doc's own `~/projects/` taxonomy adds a `work/` folder specifically so a `gitdir:` conditional include can isolate employer commits (see conflict table). Resolve the identity question directly with the user before setting anything — don't assume personal email is correct for every WSL repo without checking whether any WSL project is actually employer work.

**Sin 10 — WSL projects not backed up.** `/home/anant_gupta/projects/` lives inside the VHDX, which is on D: but *is not* part of the separately-backed-up `D:\Users\_Anant\` folder. Projects found: `umn` (19 GB), `ai` (7.9 GB), `hub` (5 GB), `hackathon` (3.1 GB) — unprotected from drive failure except whatever is already pushed to GitHub. Confirm current push status (`git status` in each) before doing anything destructive to any of them, and treat "push everything to GitHub" as a prerequisite step, not an afterthought.

**Sin 12 — multiple editor remote servers accumulating.** VS Code Server (3.4 GB at last count), Cursor Server (1.1 GB), VS Code Remote Containers (1.1 GB) — each editor update leaves the old version's server binaries behind (`~/.vscode-server/bin/<hash>/`). Nobody has been cleaning these. Concrete task: `ls ~/.vscode-server/bin/` and delete all but the newest hash directory (same for Cursor's equivalent server directory if present).

## Disk numbers observed this session (Windows-side WizTree scan, for context only — not yours to fix)

- `D:\WSL\Ubuntu\ext4.vhdx` — 97.4 GB
- `D:\Docker\DockerDesktopWSL\disk\docker_data.vhdx` — 38.6 GB
- `D:\Installers\wsl-ubuntu.tar` — 36.7 GB (leftover install tarball, Windows-side, not WSL's to touch)
- `C:\...\AppData\Local\Temp\wsl-crashes` — 2.4 GB of crash dumps, consistent with an unstable WSL instance. **This one WSL can help diagnose** — `dmesg`/crash-dump contents from inside the distro may explain *why* it's been crashing, even though deleting the Windows-side dump folder itself is the user's job.

## The Windows-vs-WSL source-doc conflict table (reproduced from [[New Laptop Setup]] — the WSL file wins every row)

| Topic | Windows file says | WSL file says (authoritative) |
|---|---|---|
| Node version manager | nvm | **fnm** — ~5ms shell init vs nvm's 70–700ms |
| JS package manager | unspecified (implicitly npm) | **pnpm** for every project; npm reserved only for the `claude-code`/`codex` global CLIs |
| WSL resource caps | `/etc/wsl.conf`'s `[wsl2]` block | **`%UserProfile%\.wslconfig`** — `/etc/wsl.conf` has no `[wsl2]` section, so a memory/processors line there is silently ignored. This is the single most expensive mistake to repeat; already happened once on this machine. |
| WSL install command | `wsl --import` with a manually downloaded tarball | `wsl --install Ubuntu-24.04 --location "D:\WSL\Ubuntu"`, one command, with a move-after fallback |
| `~/projects/` taxonomy | `{ai,hub,hackathon,scratch}` | `{hub,ai,hackathon,scratch,work}` — adds `work/` so a `gitdir:` conditional include can isolate employer commits |
| Docker | one-line reminder to redirect the VHDX to D: | full procedure: compose example, prune policy, shared-memory ceiling with WSL |

## Concrete task checklist (investigate and confirm each before changing anything — do not batch-apply fixes you haven't individually verified are still needed)

**Phase 1 — health audit (read-only, do this entire phase before changing anything):**
- [ ] `wsl --status` and `wsl -l -v` (run from Windows side if needed, or check from within — confirm WSL version, default distro, running state)
- [ ] `cat /etc/wsl.conf` and check `%UserProfile%\.wslconfig` (via `/mnt/c/Users/Anant Gupta/.wslconfig`) — confirm memory/processor caps are in the right file, not both/neither
- [ ] `which node`, `nvm ls` (or `fnm list` if already migrated) — confirm actual current state matches or contradicts Sin 3 above
- [ ] `uv --version`, `pnpm --version` (or lack thereof)
- [ ] `ls ~/projects/` — compare against both taxonomies in the conflict table
- [ ] `git config --global --list` (WSL side) — confirm current identity, compare against Sin 9
- [ ] `ls ~/.vscode-server/bin/` and equivalent Cursor server directory — count old versions
- [ ] Investigate `wsl-crashes` root cause from inside the distro (dmesg, systemd journal, whatever's available) — report findings even though the Windows-side cleanup isn't yours to do
- [ ] `cat ~/.mcp.json` (confirm it's genuinely missing, per [[Jarvis MCP and REST API Setup]] — don't assume, verify)
- [ ] For each project in `~/projects/`: `git status` — confirm push state before Phase 2 touches anything

**Phase 2 — present findings and a plan (this is the plan-mode deliverable — do not skip to execution):**
- [ ] Report exactly what Phase 1 found, including anywhere reality contradicts this note or either source doc
- [ ] Decide with the user, explicitly: repair-in-place vs. fresh `wsl --unregister Ubuntu` + reimport. Do not assume either — the user described the current state as "corrupted" but that is not the same as "unrecoverable," and a fresh reimport has its own cost (losing whatever isn't yet pushed to GitHub, needing the SSH key restored, etc.)
- [ ] Resolve the git identity question explicitly (Sin 9) — which email, and whether any current or future WSL project needs a `gitdir:` conditional include for a `work/` folder

**Phase 3 — execution (only after Phase 2's plan is approved):**
- [ ] Node: migrate to fnm per the conflict table, or fix nvm's default alias — whichever Phase 2 decided — and remove the stale extra versions either way
- [ ] Package manager: pnpm for real project work; confirm npm stays reserved for the two global CLIs only
- [ ] `/etc/wsl.conf` vs `.wslconfig`: fix whichever is misplaced
- [ ] git identity: apply the decided email/name, and set up the `work/` conditional include only if there's an actual employer-work directory to point it at — don't create speculative config for a directory that doesn't exist yet
- [ ] `~/projects/` taxonomy: reconcile toward the WSL file's superset (adds `work/`)
- [ ] Write a WSL-native `~/.mcp.json` using `/mnt/d/...` paths for any filesystem-style server, mirroring the Windows project-local config's server set (`obsidian`, `filesystem`, `git`, `fetch`) — do not copy the Windows `~/.mcp.json` verbatim, its paths won't resolve from Linux
- [ ] Clean `~/.vscode-server/bin/` and equivalent Cursor directory down to the newest version only
- [ ] `npm cache clean --force`, `uv cache clean`, `pnpm store prune` if pnpm is in use
- [ ] Confirm every project in `~/projects/` is pushed to GitHub (prerequisite check from Phase 1, act on any gaps found)

**Explicitly not Phase 3's job:** VHDX compaction, any C:/D: drive operation — hand these back to the user with a clear note of what you found (e.g., "VHDX is at 97.4GB, compaction would help, here's the Windows-side command for you to run" — same pattern the Windows sessions used for actions blocked by the auto-mode classifier or requiring elevation).

## A note on how to work (matches the Windows sessions' established pattern)

- Start this session in **plan mode**: research everything above, verify current reality against every claim in this note and the two source docs (don't trust any of it blindly — some of it may already be stale, exactly like the Jarvis MCP note was until this session corrected it), then present a complete plan for approval before executing anything.
- This user prefers **manual, opt-in tooling over silent automation** — confirmed pattern from the archiving-pipeline precedent and the Windows session's choice of a manually-invoked `New-PyEnv` function instead of an auto-hook. Apply the same instinct here: no automatic on-shell-open hooks unless explicitly asked for.
- When creating or updating any Jarvis vault note (including this one, if you find something here is wrong), follow the existing frontmatter and section conventions used across every note in this folder: `type/status/created/updated/course/track/prerequisites/used_in/evidence/tags/related` frontmatter, then `## One-Line Answer` (a single bolded/highlighted sentence), `## Mechanism`, `## Contrast / What It Is Not`, `## Failure Modes / Misconceptions` (as `> [!WARNING]` callouts), `## Evidence From This Vault`, and `## Flashcards` (Q::A pairs tagged `#cards/laptop`). Look at [[Ubuntu - WSL]] or [[Jarvis MCP and REST API Setup]] as templates before writing.

## Execution Results (2026-08-26 WSL session)

**The authoritative WSL plan file this note points to does not exist.** A full-filesystem search inside WSL found nothing at `/home/anant_gupta/.claude/plans/new-laptop-setup.md`. The only copies of `new-laptop-setup.md` anywhere on the machine are `/mnt/c/Users/Anant Gupta/new-laptop-setup.md` and its backup at `/mnt/d/Users/_Anant/10_Areas/DevConfig/new-laptop-setup.md` — and both are the **same document**: the original broad, Windows-centric audit dated 2026-06-02 (recommends nvm, not fnm; no VHDX/`.wslconfig` mental model beyond a one-line reminder). The deeper WSL-specific manual this briefing describes (fnm/pnpm discipline, a validated "Part 13" cleanup already run on this machine) never existed as an actual file — that claim in this note was wrong. There is nothing to restore from it going forward; treat the June 2 doc as the only source-of-truth file that actually exists, and treat any future "the WSL file says X" claim as unverified until checked directly.

> [!WARNING]
> This note's Sin 3, Sin 9, and Sin 12 claims (nvm has no working default; WSL git uses a UMN email; VS Code Server has multiple stale version dirs) were all independently re-verified on 2026-08-26 and found **already false** — see the corrections below. Don't propagate these specific claims further without re-checking.

**What was independently verified true vs. false this session:**
- ~~Sin 3: nvm has no working default~~ — **false now.** `nvm`'s `lts/*` alias resolved cleanly to v24.14.1 in an interactive shell. Only real issue was 3 unused extra versions (v20.20.0, v24.12.0, v24.13.1) — removed.
- ~~Sin 9: WSL git identity is a UMN email~~ — **false now.** Global identity was already `anantmahi721@gmail.com`, matching Windows. No conditional include was needed — nothing under `~/projects/work/` or `~/projects/umn/` is actually employer-owned.
- ~~Sin 12: multiple stale VS Code/Cursor Server version dirs~~ — **false for the binaries** (`~/.vscode-server/bin/` and `~/.cursor-server/bin/` each had exactly one hash dir already). The real cruft was ~30 orphaned `.log`/`.token` file pairs in `~/.cursor-server/` for hash values with no matching `bin/` dir — cleaned.
- ~~WSL-native `~/.mcp.json` is missing~~ — **false.** It already existed, already correct (`/mnt/d/...` paths, env-var Bearer tokens, matching server set). No action needed.
- **True and fixed:** npm cache was 7.1G → cleaned to 4.4G. uv cache cleared entirely (160M). pnpm store pruned 3.5G → 2.3G.
- **True and NOT fixed (handing back):** `.wslconfig` has no `memory=`/`processors=` cap set at all (uncapped, not misplaced) — lives on C:, out of scope for a WSL-side session. Persistent WSL networking errors (`CheckConnection: getaddrinfo()/connect() failed`, every 15–90s in `dmesg`/`journalctl`) — likely tied to `.wslconfig`'s `networkingMode=mirrored`/`dnsTunneling`/`autoProxy`, also a C:-side fix, and the most plausible real source of any perceived WSL instability. No filesystem/systemd corruption was found anywhere (systemd healthy, 0 failed units, no OOM/panic) — repair-in-place was correct, a reimport would have been unnecessary risk.
- **Attempted but blocked, needs a human call:** two repos (`~/projects/hackathon/opspilot-placeholder-backup`, `~/projects/hub/CausalOps`) looked like simple unpushed-commit pushes from `git status` alone, but both remotes have genuinely diverged (a different contributor's active history on opspilot; an apparent rename/rewrite on CausalOps). Left both alone rather than merge/rebase blindly — needs your judgment on which history is correct.

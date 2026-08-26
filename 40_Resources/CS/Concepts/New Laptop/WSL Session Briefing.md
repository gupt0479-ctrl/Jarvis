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
related:
  - "[[New Laptop Setup]]"
  - "[[Ubuntu - WSL]]"
tags:
  - note
---
# WSL Session Briefing

## Why this note exists

The 2026-08-26 session on this laptop deliberately scoped itself to Windows-side coding-environment fixes only (VS Code global settings, Python/uv/npm on the Windows side) and made **zero reads, edits, or commands against WSL**, per explicit instruction. This note is the handoff: what a dedicated WSL session needs to know before it starts, so that session doesn't have to re-derive context.

## What was done on the Windows side this session (for context, not to redo)

- Fixed the global Pylance "large number of source files" warning by adding `files.exclude` / `search.exclude` / `python.analysis.exclude` to `%APPDATA%\Code\User\settings.json` (excluding `AppData`, `node_modules`, `.venv`, `__pycache__`). Root cause: the home directory `C:\Users\Anant Gupta` is opened directly as a VS Code workspace and nothing excluded `AppData` (865k+ items) from indexing.
- Confirmed `python.defaultInterpreterPath` (`${workspaceFolder}/.venv/Scripts/python.exe`) fix from 2026-08-25 is holding — Windows `.venv` activation now works reliably in both the home dir and the Jarvis vault folder.
- Added a manual (not automatic — see the standing preference for consent-gated tooling over auto-hooks) `New-PyEnv` PowerShell function to bootstrap `.venv` in a new Windows-native project on demand.
- Redirected the Windows npm cache to `D:\npm-cache`.
- Left as a decision pending: uninstalling `miniconda3` from C: (~4.9 GB, one dead `csci4041` course env, uninstaller blocked by the auto-mode classifier as a software-removal action — needs the user to run `C:\Users\Anant Gupta\miniconda3\Uninstall-Miniconda3.exe /S` directly or explicitly re-approve it).

None of the above touched WSL, `.wslconfig`, `/etc/wsl.conf`, the VHDX, or anything inside the Ubuntu distro.

## What's actually wrong with WSL on this machine (from the user, this session)

- WSL was already moved from C: to `D:\WSL\Ubuntu\ext4.vhdx` at some point, but the process was messy and the user describes the current state as "extremely complicated and corrupted."
- The user is not comfortable with the Ubuntu/distro side of things and needs this treated as a from-scratch, professional setup rather than incremental patching.
- WizTree scan of `D:` this session shows the scale of what's accumulated:
  - `D:\WSL\Ubuntu\ext4.vhdx` — 97.4 GB
  - `D:\Docker\DockerDesktopWSL\disk\docker_data.vhdx` — 38.6 GB
  - `D:\Installers\wsl-ubuntu.tar` — 36.7 GB (a leftover install tarball — candidate for deletion once WSL health is confirmed, since it's not needed after import)
  - `D:\Users\...\projects` — 24.3 GB, `D:\Users\...\AI` — 9.2 GB
- WizTree scan of `C:` this session shows a `wsl-crashes` folder at `AppData\Local\Temp\wsl-crashes` — 2.4 GB of crash dumps, consistent with an unstable WSL instance.

## What the vault already knows (read this before touching anything)

- [[Ubuntu - WSL]] — the VHDX mental model: WSL2 is a real VM with the whole Linux filesystem inside one opaque `.vhdx` file, not a folder Windows can browse or sync normally. `rm -rf` inside Linux does not shrink the VHDX (no auto-compaction) — needs `fstrim` + `Optimize-VHD`/`diskpart`, or `sparseVhd=true`.
- [[New Laptop Setup]] — the index note explaining that **two source files are the ground truth, not this vault**:
  - `C:\Users\Anant Gupta\new-laptop-setup.md` (Windows-first plan, read this session, Part 4/6/9 cover WSL Day-1 setup, Node/nvm strategy, and monthly cleanup — but this file is the *shallower* of the two for anything inside WSL)
  - `/home/anant_gupta/.claude/plans/new-laptop-setup.md` (the deeper WSL2 reference manual — **not read this session, since it lives inside WSL and this session avoided WSL entirely**). Per the index note, this file is authoritative wherever it disagrees with the Windows file, and its Part 13 cleanup was already validated by actually running it on this machine once before.
  - The documented conflict table between the two files (Node manager: fnm not nvm; package manager: pnpm not npm; resource caps: `.wslconfig` not `wsl.conf`; project taxonomy: adds a `work/` folder) — the WSL session should treat the WSL file's answers as correct wherever the two disagree.

## What the WSL session needs to do first

1. **Read `/home/anant_gupta/.claude/plans/new-laptop-setup.md` in full** — that's the authoritative, validated manual for this exact machine's WSL side, and no Windows-side session has re-verified its current accuracy against today's state.
2. Audit current WSL health before changing anything: `wsl --status`, `wsl -l -v`, check `/etc/wsl.conf` and `%UserProfile%\.wslconfig` for the exact bug already documented (memory/processor caps landing in the wrong file), check what's filling `wsl-crashes`, check actual Node/nvm/fnm state (`which node`, `nvm ls` or `fnm list`), check `uv --version` inside WSL, check `~/projects/` taxonomy against the documented `{ai,hub,hackathon,scratch,work}` target.
3. Decide, with the user, whether this is a repair-in-place or a fresh `wsl --unregister Ubuntu` + reimport to `D:\WSL\Ubuntu` — the user's own Windows-file Sin 1 audit says a from-scratch reimport was the original new-laptop plan; given the "corrupted" description, ask explicitly rather than assuming.
4. Only after the distro itself is healthy: git identity + SSH signing, fnm/pnpm/uv install order, VS Code Remote-WSL, Docker Desktop WSL integration, `~/projects/` layout, and the monthly VHDX-compaction habit.

## Suggested opening prompt for that session

> Read `/home/anant_gupta/.claude/plans/new-laptop-setup.md` in full, and the Jarvis vault notes `40_Resources/CS/Concepts/New Laptop/Ubuntu - WSL.md`, `New Laptop Setup.md`, and this `WSL Session Briefing.md`. This machine's WSL/Ubuntu setup is described by its owner as corrupted and messy since a prior VHDX move to `D:\WSL\Ubuntu`, with 2.4 GB of crash dumps in `wsl-crashes` and a 97.4 GB VHDX. Do not assume repair-in-place vs. fresh reimport — investigate current health first (`wsl --status`, `wsl -l -v`, `/etc/wsl.conf`, `.wslconfig`, Node/nvm-vs-fnm state, `uv` state, `~/projects` layout) and present findings plus options before changing anything.

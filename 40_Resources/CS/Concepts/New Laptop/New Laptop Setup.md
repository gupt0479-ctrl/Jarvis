---
type: concept
status: sprout
created: 2026-06-17
updated: 2026-08-26
course: Life
track:
  - laptop
mastery_level: 3
prerequisites:
  - "[[Ubuntu - WSL]]"
used_in: []
evidence: []
tags:
  - concept
related:
  - "[[Summer Grind]]"
  - "[[Jarvis MCP and REST API Setup]]"
  - "[[WSL Session Briefing]]"
---
# New Laptop Setup
## One-Line Answer
==Only one source plan actually exists on disk — the broad Windows-centric checklist at `C:\Users\Anant Gupta\new-laptop-setup.md` — despite this note previously describing a second, deeper WSL-specific manual inside WSL; a 2026-08-26 WSL session searched the entire filesystem and found no such file, so that "two files, the WSL one wins disagreements" framing below is now known to be **aspirational, not real**, and should be treated as unverified guidance rather than a second authoritative document.==
## Mechanism
> [!WARNING]
> **Correction, 2026-08-26:** this note originally claimed a second file existed at `/home/anant_gupta/.claude/plans/new-laptop-setup.md` — "a reference manual... written 2026-06-08... its Part 13 cleanup was actually executed on the current machine." A dedicated WSL session searched the full WSL filesystem for it and found nothing; the only copies of `new-laptop-setup.md` anywhere on the machine (`/mnt/c/Users/Anant Gupta/new-laptop-setup.md` and a backup at `/mnt/d/Users/_Anant/10_Areas/DevConfig/new-laptop-setup.md`) are the **same** June 2 Windows-centric document. The conflict table below (fnm vs nvm, pnpm vs npm, etc.) was written as if sourced from that second file — it may reflect genuinely better practices, but it is **not verified against any actual second document**, and the "already validated by running it once" claim was false. Treat every row as a recommendation to evaluate on its own merits, not as an authoritative correction backed by a file that exists.
*What actually exists:* `C:\Users\Anant Gupta\new-laptop-setup.md` (also backed up at `D:\Users\_Anant\10_Areas\DevConfig\new-laptop-setup.md`), written 2026-06-02. Broad coverage: partitioning, Day-1 Windows steps, the Python "sandbox" mental model, Node strategy (recommends nvm, not fnm), Claude Code + MCP setup, backup strategy, a literal Day 1/2/3 checklist. This is the only ground-truth file. It stays untouched at its original path — this vault note is the index/summary, not a copy.
*How to actually use it on the new laptop:*
1. Run Windows Day 1 from the source file: partition, disable hibernation, set env vars, install Git/Node/Chrome (superseded — see [[WSL Session Briefing]], Chrome has since been fully removed from this machine and replaced with Vivaldi), install WSL pointing at `D:\WSL\Ubuntu`.
2. Use the file's Part 11 checklist as the day-by-day tracker.
3. For the MCP/Jarvis layer specifically, the source file isn't enough on its own — use [[Jarvis MCP and REST API Setup]].
4. For anything WSL-internal, don't assume a deeper WSL-specific manual exists to defer to (see correction above) — verify current WSL state directly instead, the way the 2026-08-26 WSL session did.
*The previously-claimed conflict table (unverified — evaluate each row on its own merits, not as "the WSL file already settled this"):*

| Topic | Windows file says | Previously claimed "WSL file" position (source not found) |
|---|---|---|
| Node version manager | nvm | fnm — ~5ms shell init vs nvm's 70–700ms |
| JS package manager | unspecified (implicitly npm) | pnpm for every project; npm reserved for the `claude-code`/`codex` global CLIs only |
| WSL resource caps | puts `memory=`/`processors=` inside `/etc/wsl.conf`'s `[wsl2]` block | puts them in `%UserProfile%\.wslconfig` instead — **this specific row is independently confirmed correct** regardless of the missing source file, see the warning below and [[Ubuntu - WSL]] |
| WSL install command | `wsl --import` with a manually downloaded tarball | `wsl --install Ubuntu-24.04 --location "D:\WSL\Ubuntu"`, one command, with a move-after fallback |
| `~/projects/` taxonomy | `{ai,hub,hackathon,scratch}` | `{hub,ai,hackathon,scratch,work}` — adds `work/` so a `gitdir:` conditional include can isolate employer commits |
| Docker | one line: redirect the VHDX to D: | full procedure: compose example, prune policy, shared memory ceiling with WSL |
> [!WARNING]
> The `/etc/wsl.conf` vs `.wslconfig` mistake is real and independently confirmed, regardless of the missing second file: `/etc/wsl.conf` has no `[wsl2]` section, so a `memory=8GB` line there is silently ignored. The setting belongs in `%UserProfile%\.wslconfig`. This already happened once on this machine — see [[Ubuntu - WSL]]. As of 2026-08-26, `.wslconfig` is correctly the location in use, now with `memory=16GB`/`processors=8` set (see [[WSL Session Briefing]]).
## Contrast / What It Is Not
This note is not a copy of the source file — copying it into the vault verbatim was an earlier version of this note, and it just duplicated content without adding anything. This note is the index: what the source file is for, and (as of 2026-08-26) an honest record that a previously-assumed second source file does not exist.
## Failure Modes / Misconceptions
> [!WARNING]
> Assuming any claim in this vault about "what the WSL file says" is backed by an actual second document. It was not, as of 2026-08-26 — verify current WSL state directly instead of trusting a citation to a file that was never confirmed to exist.
> [!WARNING]
> Assuming `~/.mcp.json` is a simple copy-paste between laptops. See [[Jarvis MCP and REST API Setup]] — as of 2026-08-26 the WSL-native `~/.mcp.json` was found to already exist and already be correct, so this specific worry turned out to be unfounded on this machine, but the general caution (keys are per-install) still holds for the actual new laptop.
## Where To Go When Something Breaks
*Use this table before re-deriving anything from scratch:*

| Symptom | Look here |
|---|---|
| Anything inside WSL behaves wrong — wrong Node/Python, slow installs, PATH confusion | [[Ubuntu - WSL]] for the mental model, then verify directly — don't assume a deeper WSL manual has already answered it |
| `.wslconfig`/`wsl.conf` memory or CPU settings not taking effect | Confirm the setting is in `.wslconfig`, not `wsl.conf` — independently confirmed real bug, fixed 2026-08-26 |
| `D:` filling up despite deleting files inside WSL | [[Ubuntu - WSL]] — VHDX compaction procedure (fstrim + Optimize-VHD/diskpart) |
| Jarvis/The Plan MCP not connecting, wrong port, stale key | [[Jarvis MCP and REST API Setup]] |
| Node version wrong inside a specific project | Check `.nvmrc`/`nvm ls` (or fnm equivalent if migrated) — see [[WSL Session Briefing]] for 2026-08-26 findings |
| Python env confusion, conda vs uv | Windows file Part 5 for the "sandbox" explanation; on Windows, uv is the standard, miniconda is kept specifically for Jupyter/notebook work per user decision — see [[VS Code Professional Setup]] |
| Docker eating disk on C: | Redirect VHDX to D: (already done on this machine) |
| Git committing under the wrong email | Check both Windows and WSL identity explicitly — see [[WSL Session Briefing]], both were independently verified/fixed to personal email 2026-08-26 |
| Lost work after a laptop failure | Push everything to GitHub, nightly — see [[WSL Session Briefing]] Sin 10 |
## Evidence From This Vault
- [[Ubuntu - WSL]] — the WSL mental model this setup depends on
- [[Jarvis MCP and REST API Setup]] — the subsystem this vault's index notes don't fully document
- [[WSL Session Briefing]] — the 2026-08-26 WSL session's findings, including the missing-second-file discovery and what was actually fixed
- [[VS Code Professional Setup]] — the Windows-side VS Code deep-dive, same laptop
- [[What MCPs]] — older, generic MCP brainstorm note from the Cursor era; superseded by [[Jarvis MCP and REST API Setup]] for this vault's actual Jarvis/The Plan wiring
## Flashcards
Where does the WSL2 `memory=` resource cap actually go — `/etc/wsl.conf` or `.wslconfig`?::`%UserProfile%\.wslconfig`. `/etc/wsl.conf` has no `[wsl2]` section, so a memory/processors line there is silently ignored. This is the exact bug from the old machine, independently confirmed real on 2026-08-26 regardless of the missing-second-file issue below.
#cards/laptop
This note used to cite a "deeper WSL-specific manual" at `/home/anant_gupta/.claude/plans/new-laptop-setup.md` — does that file actually exist?::No. A 2026-08-26 WSL session searched the full filesystem and found nothing there. Both copies of `new-laptop-setup.md` found on the machine are the same June 2 Windows-centric document. Treat the "WSL file says X" claims in the conflict table as unverified recommendations, not a second authoritative source.
#cards/laptop
`node` works in one WSL shell but fails in another — what's the likely cause?::Version-manager lazy-loading (nvm) or a missing `.nvmrc`/default alias. Check `which node` and `nvm ls` (or `fnm list`) — on 2026-08-26 this was checked directly and found already working, contradicting an earlier assumption.
#cards/laptop
A WSL terminal is silently using the Windows `node.exe`/`python.exe` instead of the Linux one — what setting controls this?::`appendWindowsPath` in `/etc/wsl.conf`. Left at the default `true`, Windows binaries shadow the Linux ones depending on PATH order.
#cards/laptop
Deleted a 19GB build folder inside WSL but the `.vhdx` on D: didn't shrink — why, and what's the fix?::The VHDX only grows, never auto-shrinks. Free the blocks inside Linux first (`sudo fstrim -av`), then compact from Windows (`Optimize-VHD`/`diskpart`), or set `sparseVhd=true` so it self-compacts.
#cards/laptop

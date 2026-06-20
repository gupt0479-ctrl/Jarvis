---
type: concept
status: sprout
created: 2026-06-17
updated: 2026-06-20
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
---
# New Laptop Setup
## One-Line Answer
==Two source plans define the new-machine rebuild — a broad Windows checklist and a deeper WSL2 reference manual — and where they disagree, the WSL file wins, because it is six days newer and was validated by actually running its cleanup steps on the current machine.==
## Mechanism
*Two files, two jobs* — neither lives in this vault, both stay untouched at their original paths as the command-level ground truth:
- `C:\Users\Anant Gupta\new-laptop-setup.md` (Windows) — written 2026-06-02. Broad coverage: partitioning, Day-1 Windows steps, the Python "sandbox" mental model, Node strategy, Claude Code + MCP setup, backup strategy, a literal Day 1/2/3 checklist. Thin on WSL internals — it treats WSL as one step inside a bigger Windows-first plan.
- `/home/anant_gupta/.claude/plans/new-laptop-setup.md` (WSL) — written 2026-06-08. A reference manual, not a quick-start, specifically for WSL2: the VHDX mental model, `.wslconfig` vs `/etc/wsl.conf`, fnm/pnpm/uv discipline, Docker, VS Code Remote-WSL, git identity with SSH signing, cache management, a full migration checklist. Its Part 13 cleanup was actually executed on the current machine — the caveats in it are observed bugs, not guesses.
*How to actually use them on the new laptop:*
1. Run Windows Day 1 from the Windows file: partition, disable hibernation, set env vars, install Git/Node/Chrome, install WSL pointing at `D:\WSL\Ubuntu`.
2. The moment WSL exists, switch authority to the WSL file. Follow its Part 3 install order exactly — it supersedes the Windows file's Part 4 for anything inside WSL.
3. Use the Windows file's Part 11 checklist as the day-by-day tracker, but swap in the WSL-file procedure wherever the two disagree (table below).
4. For the MCP/Jarvis layer specifically, neither file is enough on its own — use [[Jarvis MCP and REST API Setup]].
*Where the two disagree, and which one wins:*

| Topic | Windows file says | WSL file says | Winner |
|---|---|---|---|
| Node version manager | nvm | fnm — ~5ms shell init vs nvm's 70–700ms | WSL file |
| JS package manager | unspecified (implicitly npm) | pnpm for every project; npm reserved for the `claude-code`/`codex` global CLIs only | WSL file |
| WSL resource caps | puts `memory=`/`processors=` inside `/etc/wsl.conf`'s `[wsl2]` block | puts them in `%UserProfile%\.wslconfig` instead | **WSL file — not a style choice, this is the exact bug from the old machine** |
| WSL install command | `wsl --import` with a manually downloaded tarball | `wsl --install Ubuntu-24.04 --location "D:\WSL\Ubuntu"`, one command, with a move-after fallback | WSL file |
| `~/projects/` taxonomy | `{ai,hub,hackathon,scratch}` | `{hub,ai,hackathon,scratch,work}` — adds `work/` so a `gitdir:` conditional include can isolate employer commits | WSL file, strict superset |
| Docker | one line: redirect the VHDX to D: | full procedure: compose example, prune policy, shared memory ceiling with WSL | WSL file is the manual; Windows file's line is just the reminder to do it |
> [!WARNING]
> The single most expensive mistake to repeat: copying the Windows file's `/etc/wsl.conf` block verbatim. Its `[wsl2] memory=8GB` line looks correct and does nothing — `/etc/wsl.conf` has no `[wsl2]` section, so WSL silently ignores it. The setting belongs in `%UserProfile%\.wslconfig`. This already happened once on the old machine (WSL file, Part 3 intro) — see [[Ubuntu - WSL]] for the mental model behind why.
## Contrast / What It Is Not
This note is not a copy of either source file — copying both into the vault verbatim was the previous version of this note, and it just duplicated 2,600 lines without adding anything. This note is the index: what each file is for, where they conflict, and the one subsystem neither file documents well enough to actually use.
## Failure Modes / Misconceptions
> [!WARNING]
> Treating the Windows file as "the plan" and the WSL file as optional deep-dive reading. The WSL file is newer, has a validated status note, and explicitly corrects bugs the Windows file would otherwise reproduce. Read both before Day 1; the WSL file is authoritative for anything inside WSL.
> [!WARNING]
> Assuming `~/.mcp.json` is a simple copy-paste between laptops. Three different MCP configs exist today (home, vault-local, and a missing WSL one) and they disagree with each other. See [[Jarvis MCP and REST API Setup]] before assuming a straight copy works.
## Where To Go When Something Breaks
*Use this table before re-deriving anything from scratch:*

| Symptom | Look here |
|---|---|
| Anything inside WSL behaves wrong — wrong Node/Python, slow installs, PATH confusion | [[Ubuntu - WSL]] for the mental model, then WSL file Part 0 |
| `.wslconfig`/`wsl.conf` memory or CPU settings not taking effect | WSL file Part 3 Step 3 — confirm the setting is in `.wslconfig`, not `wsl.conf` |
| `D:` filling up despite deleting files inside WSL | WSL file Part 2 and Part 10 — VHDX compaction procedure |
| Jarvis/The Plan MCP not connecting, wrong port, stale key | [[Jarvis MCP and REST API Setup]] |
| Node version wrong inside a specific project | WSL file Part 5 — `.nvmrc` + fnm |
| Python env confusion, conda vs uv | Windows file Part 5 for the "sandbox" explanation; WSL file Part 6 for the working `uv` flow |
| Docker eating disk on C: | WSL file Part 7 Step 2 |
| Git committing under the wrong email | WSL file Part 9 — conditional includes plus the pre-push hook |
| Lost work after a laptop failure | WSL file Part 11 — the three backup layers |
## Evidence From This Vault
- [[Ubuntu - WSL]] — the WSL mental model this setup depends on
- [[Jarvis MCP and REST API Setup]] — the subsystem neither source file documents well
- [[MCPs]] — older, generic MCP brainstorm note from the Cursor era; superseded by the note above for this vault's actual Jarvis/The Plan wiring
## Flashcards
Where does the WSL2 `memory=` resource cap actually go — `/etc/wsl.conf` or `.wslconfig`?::`%UserProfile%\.wslconfig`. `/etc/wsl.conf` has no `[wsl2]` section, so a memory/processors line there is silently ignored. This is the exact bug from the old machine.
#cards/laptop
`node` works in one WSL shell but fails in another — what's the likely cause?::Version-manager lazy-loading (nvm) or a missing `.nvmrc`. Check `which node`, then check the project's `.nvmrc` against the installed versions.
#cards/laptop
A WSL terminal is silently using the Windows `node.exe`/`python.exe` instead of the Linux one — what setting controls this?::`appendWindowsPath` in `/etc/wsl.conf`. Left at the default `true`, Windows binaries shadow the Linux ones depending on PATH order.
#cards/laptop
Deleted a 19GB build folder inside WSL but the `.vhdx` on D: didn't shrink — why, and what's the fix?::The VHDX only grows, never auto-shrinks. Free the blocks inside Linux first (`sudo fstrim -av`), then compact from Windows (`Optimize-VHD`/`diskpart`), or set `sparseVhd=true` so it self-compacts.
#cards/laptop

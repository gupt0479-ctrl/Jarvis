---
type: concept
status: sprout
created: 2026-01-17
updated: 2026-06-20
course: Life
track:
  - laptop
mastery_level: 3
prerequisites: []
used_in:
  - "[[New Laptop Setup]]"
evidence: []
tags:
  - concept
related:
  - "[[40_Resources/CS/Links|Links]]"
  - "[[New Laptop Setup]]"
---
# Ubuntu - WSL
## One-Line Answer
==WSL2 is a real virtual machine with a real virtual disk, not "Linux in a window" — the whole Linux filesystem lives inside one Windows file, `ext4.vhdx`, and most WSL storage and "wrong version" mysteries trace back to forgetting that.==
## Mechanism
*The VHDX is the whole disk, not a folder:* every file under `/`, including `/home/anant_gupta`, lives inside `D:\WSL\Ubuntu\ext4.vhdx`. Windows sees one opaque binary; Linux sees a disk. View it from Windows Explorer through the bridge: `\\wsl$\Ubuntu\home\anant_gupta\projects` (plain `\\wsl$` shows the whole Linux environment).
*Three worlds, one rule:* Windows programs (Docker Desktop, browsers, Obsidian) run in World 1 on `C:`/`D:`. WSL Linux programs (node, uv, git, claude) run in World 2 inside the VHDX — native, fast. Windows files read from Linux (`/mnt/c`, `/mnt/d`) are World 3, a 9P network bridge that is 5–20x slower for anything touching many small files. Build and run code in World 2; only read Windows-side data (the Obsidian vault, model weights) through World 3.
*Run command:* `wsl ~` opens straight into the WSL home directory. Plain `wsl` opens wherever the root filesystem got installed — historically `C:`, even though everything that matters now actually runs on `D:` after the VHDX move.
## Contrast / What It Is Not
WSL2 is not WSL1, which ran a translation layer instead of a real Linux kernel and had no VHDX — performance characteristics and file-access patterns are different between the two. It is also not a Windows folder you can sync with Google Drive or OneDrive: those tools back up files, and to them the VHDX is one binary blob, not a tree they can see inside.
## Failure Modes / Misconceptions
> [!WARNING]
> Believing `rm -rf` on a large directory shrinks the `.vhdx` on Windows. It does not — ext4 frees the blocks inside the disk image, but the image's high-water mark on `D:` stays the same until you `fstrim` inside Linux and then compact (`Optimize-VHD`/`diskpart`) from Windows, or run with `sparseVhd=true` so it self-compacts.
> [!WARNING]
> Cloning a working repo into `/mnt/c` or `/mnt/d` because it feels more visible from Windows. Every file operation crosses the 9P bridge and the toolchain feels broken — the fix is moving the repo to the Linux side, not debugging the editor.
## Evidence From This Vault
- [[New Laptop Setup]] — the procedure that depends on this mental model holding
## Flashcards
Why doesn't deleting a 19GB folder inside WSL free up space on the D: drive?::The VHDX only grows, never auto-shrinks. The blocks are freed inside Linux but the Windows-side file keeps its high-water mark until `fstrim` plus compaction (or `sparseVhd=true`).
#cards/laptop
`npm install` feels far slower in one WSL project than another — what's the most likely cause?::The slow project is cloned under `/mnt/c` or `/mnt/d` (crossing the 9P DrvFs bridge for every file) instead of the native Linux side (`~/projects/...`).
#cards/laptop

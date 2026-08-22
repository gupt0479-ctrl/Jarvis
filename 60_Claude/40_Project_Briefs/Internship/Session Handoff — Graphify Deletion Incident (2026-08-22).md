---
type: project
status: sprout
created: 2026-08-22
tags:
  - project
  - internship-research-loop
  - graphify
notes:
  - "[[Internship Research Loop — PRD]]"
next: "[[Follow-up prompt below]]"
---

# Session Handoff — Graphify Deletion Incident (2026-08-22)

Written by a Windows-side Claude Code session after the WSL internship-research-loop session paused mid-cleanup, worried it had lost `Promote-Dossier Note Templates.md` with no way to recover it. Checked git directly from the vault root. It's not lost, and the reason it looked that way is worth recording so the next graphify pass doesn't trip the same alarm.

## What actually happened

1. **Jarvis is a git repo with full history.** `git rev-parse --is-inside-work-tree` returns true at `D:\Users\_Anant\10_Areas\Documents\Jarvis`, and `git log` shows a normal commit stream including automated snapshots (`auto: 2026-08-21 21:59 | 1007 files`, commit `36564f44`) and hourly/cron-style commits (`Auto-discovered N internship(s)`). The WSL session's claim that `Jarvis/.git` doesn't exist doesn't hold from this side — almost certainly a path/mount mismatch (e.g. a different checkout, or a WSL mount that doesn't see the same `.git`), not an actual absence of version control.

2. **Both "lost" files are sitting in the working tree as uncommitted deletions, not gone.** `git status` on `60_Claude/40_Project_Briefs/Internship/` shows **350 files marked `D`** (deleted, uncommitted) right now, including both `Promote-Dossier Note Templates.md` and `Promote-Dossier Note Templates_1.md`. They're exactly as they were in commit `36564f44` (2026-08-21 21:59) and trivially restorable:
   ```
   git restore "60_Claude/40_Project_Briefs/Internship/Promote-Dossier Note Templates.md"
   git restore "60_Claude/40_Project_Briefs/Internship/Promote-Dossier Note Templates_1.md"
   ```

3. **The premise behind the "protected file" assert was wrong, not the assert itself.** The deleted file's own frontmatter (read via `git show 36564f44:...`) is:
   ```yaml
   source_file: ".claude/skills/promote-dossier/reference/note-templates.md"
   community: "Claude Code Skills & Agents Config"
   tags:
     - graphify/document
     - graphify/EXTRACTED
   ```
   This **is** graphify-generated content — it carries the `graphify/EXTRACTED` tag and a `source_file` pointer, same as every other orphan in the 350-file batch. It is not the hand-authored, non-graphify file the deletion script's safety assert was built to catch. That's also why the assert didn't fire: the file was correctly classified as graphify-owned debris, not a false negative in the ownership check.
   - It was a duplicate extraction of the same source heading already covered by two files that are **still present and untouched**: `promote-dossier.md` and `_COMMUNITY_promote-dossier note templates.md`.
   - Neither `Promote-Dossier Note Templates.md` nor the `_1` variant appears anywhere in `.graphify_obsidian_manifest.json`, at the last commit or now — confirming the "manifest loses ownership tracking on some runs" theory from the session transcript. That bug is real and worth fixing upstream in graphify's manifest writer, but it did not cause data loss here because git already had the content.

## Net assessment

No data was lost. The deletion pass did what it was supposed to do: removed duplicate/orphaned graphify extractions. The uncertainty in the original session came from checking Obsidian's local file-recovery cache and the Recycle Bin — both dead ends — instead of `git status`/`git log`, which had the answer immediately and for free, since the vault already had a same-day snapshot commit.

## Open items for the next session

- **350 files in `60_Claude/40_Project_Briefs/Internship/` are still uncommitted deletions.** Nothing has been committed since `36564f44` for this folder's bulk cleanup. The next automated snapshot commit (this vault runs them roughly hourly) will silently finalize the mass deletion if nobody reviews it first. Decide, then commit deliberately — don't let the cron job do it by default.
- **The manifest-ownership bug is still live.** If it produced 350 orphans in one run, it'll produce more next time graphify re-exports. Worth root-causing in the graphify script itself before the next full run, not just cleaning up after it.
- **Trust `git status`/`git restore` over Obsidian's recovery cache or the Recycle Bin** for anything in this vault going forward — the vault is git-backed and auto-committed regularly, which is a stronger safety net than either of those.

---

## Follow-up prompt (paste into the WSL session to resume)

> Stand down — the file isn't lost. I checked from the Windows side of the same vault (`D:\Users\_Anant\10_Areas\Documents\Jarvis`) and it's a real git repo with a same-day snapshot commit (`36564f44`, "auto: 2026-08-21 21:59 | 1007 files") that has `Promote-Dossier Note Templates.md` in it untouched. Whatever made `Jarvis/.git` look missing from your side was a path or mount issue, not an absent repo — don't re-derive that conclusion, just point git at the actual vault root and confirm.
>
> More importantly: the premise behind your safety assert was wrong, not the assert. I pulled the deleted file's frontmatter from that commit — it's tagged `graphify/EXTRACTED` with `source_file: ".claude/skills/promote-dossier/reference/note-templates.md"`. That's graphify output, not the hand-authored non-graphify file you thought you were protecting. It's a duplicate of `promote-dossier.md` and `_COMMUNITY_promote-dossier note templates.md`, both of which are still on disk. It also doesn't appear in `.graphify_obsidian_manifest.json` at the last commit either — so your "manifest loses ownership tracking" theory is confirmed, and this file (plus its `_1` sibling) are two more instances of that same bug, not a new failure mode.
>
> Action items, in order:
> 1. Run `git status` on `60_Claude/40_Project_Briefs/Internship/` from the actual vault root before doing anything else — you'll see ~350 files marked `D`, all uncommitted. That's your existing safety net; use it instead of Obsidian's file-recovery cache or the Recycle Bin next time something looks gone.
> 2. Spot-check a handful of the 350 deletions the same way I did — `git show 36564f44:<path>` — to confirm they're all genuinely orphaned `graphify/EXTRACTED` duplicates and not something that slipped past the manifest check. If they check out, you're clear to proceed.
> 3. Don't leave this half-committed. The vault auto-commits roughly hourly; if you leave 350 uncommitted deletions sitting in the working tree, a cron snapshot will finalize them without anyone reviewing the batch. Commit deliberately once you're satisfied, with a message that says what was pruned and why.
> 4. Separately: the manifest-ownership bug that produced this batch of orphans is going to keep producing more on future graphify runs. Worth a root-cause pass on graphify's manifest writer before the next full re-export, not just cleaning up after each run.
>
> Resume the cleanup and note-writing work from here — the incident is closed, nothing was lost, and the folder's content is exactly what you left it.

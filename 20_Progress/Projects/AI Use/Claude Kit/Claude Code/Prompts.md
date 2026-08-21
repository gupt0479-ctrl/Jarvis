---
type: input
status: active
created: 2026-08-11
updated: 2026-08-21
tags:
  - claude-kit
  - prompts
  - second-brain-claudekit
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session
    Context]]"
next: "Round 7, 2026-08-21 — fixes the live instructions/_docs/_docs/ bug and
  closes out the sync-build phase. Codebase: fresh session, verify the
  _docs/_docs/ state before starting. Jarvis: fresh Windows session, checks for
  the codebase fix rather than assuming it landed. After this round: next phase
  is tests/ refinement and the review system — not written yet."
---
# Claude Kit — Build Prompts
==Only prompts live in this note, each inside a fenced block, ready to paste into a fresh session. Everything else — context, background, open questions — lives in [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session Context]]. Rewritten 2026-08-19; this note's prior content (dated 2026-08-11) is preserved there, not lost.==
## Sequencing
**Run `# Claudekit` first.** It lays out the repo's own structural base — nothing in `# Jarvis` should be attempted until that base is real, because `# Jarvis`'s job is to document what the base actually became, not what it was planned to become. Read the Claudekit session's final report (or its `git log`/diff) before starting `# Jarvis`.

# Claudekit

**Round 7, 2026-08-21 — fresh session.** Round 6 landed for real: sync-manifest.json fixed, 577 files populated across all 10 entries' five live-sync folders. But it introduced a live, self-compounding bug: `instructions/second-brain-claudekit/_docs/_docs/` — a nested duplicate that grows one level deeper every ~15-minute sync. This round fixes the bug's root cause, not just its symptom, and locks in the definitive, final shape of `instructions/<repo>/` so this stops being re-litigated.

Paste into a fresh Claude Code session, cwd = `~/projects/ai/claude/second-brain-claudekit`, `high` or `xhigh` effort.

```
Confirm git status shows instructions/second-brain-claudekit/_docs/ and _docs/_docs/ as uncommitted before starting -- if that's not the current state, stop and report rather than assuming this description still holds.

The final, definitive rule for instructions/<repo>/, confirmed directly by Anant -- encode this everywhere it needs to live, not just fix the immediate bug:

instructions/<repo>/ is FLAT. No subfolders, ever. It holds every real source-of-truth markdown file for that repo -- CLAUDE.md, AGENTS.md, README.md, PRD.md, Architecture.md, and any other governing doc -- regardless of whether it originally lives at the repo's root, inside a docs-style subfolder, or nested inside .claude/. Every file lands as instructions/<repo>/<filename>.md, never in a nested path. If a nested .claude/-internal file would collide in name with a root-level file (the Resq/OpsPilot case already solved in round 6), prefix the nested one claude-<filename>.md -- keep that exact convention, it's already proven and working.

## 1. Fix the live bug's root cause, not just its symptom

sync-manifest.json's second-brain-claudekit entry lists "_docs" as a whole directory in instructions_paths. sync-all.sh's copy step doesn't flatten or clear the destination when a path entry is a directory -- so instead of copying _docs/PRD.md to instructions/second-brain-claudekit/PRD.md, it nests the whole folder, and nests it again on every subsequent run. Fix sync-all.sh's copy logic generally: when a path entry resolves to a directory, enumerate its real files (*.md, at minimum) and copy each one flat -- basename only, directly into instructions/<repo>/ -- and always overwrite/replace the destination file rather than accumulating into it. This has to be a real mechanism fix, since any future directory-shaped path entry for any of the 10 projects would hit the same bug otherwise, not something specific to _docs.

## 2. Clean up and rebuild instructions/second-brain-claudekit/ correctly

Remove instructions/second-brain-claudekit/_docs/ entirely (both the one level and the nested _docs/_docs/ inside it -- these are sync artifacts, currently uncommitted, safe to remove outright, not archive). Re-run the corrected sync logic from item 1 (or manually reproduce its output once, to confirm it's right) so instructions/second-brain-claudekit/ ends up flat: CLAUDE.md, README.md, AGENTS.md (if it exists -- check), and every real file currently in _docs/ (confirm the current list directly rather than trusting an earlier one -- it has grown before) sitting directly in that folder, no subfolder.

## 3. Audit all 10 entries for the same class of bug

Round 6's report said every other manifest entry lists individual files, not directories, in its paths -- confirm this directly rather than trusting that report. Check every one of the 10 instructions/<repo>/ folders for any accidental nested subfolder from the same root cause. Fix any found the same way as item 2.

## 4. Write the definitive instructions/ definition down, in concrete detail, for good

Update _docs/Sync.md, 60_Claude/vault-rules/write-contract.md, and 60_Claude/vault-rules/pipeline-conventions.md with the exact rule stated at the top of this prompt -- flat structure, what counts as a source-of-truth file, the claude- collision-prefix convention, and the fact that a directory-shaped manifest path gets flattened, never nested. This has been asked for and re-explained multiple times now; write it precisely enough that it doesn't need re-explaining again.

## 5. Close the loop

Update _docs/Gaps.md and _docs/Repo-Map.md with the real fix. Review the diff for secrets before committing (this touches sync-all.sh and every instructions/<repo>/ folder -- check all of them, not just second-brain-claudekit's). Commit in logically separated commits.

Apply items 1 and 3 as real mechanism fixes covering all 10 entries -- not a patch that only happens to fix second-brain-claudekit's specific case.
```

# Jarvis

**Round 7, 2026-08-21.** The sync-mechanism build is closing out — a parallel codebase round is fixing the last real bug (a self-nesting `instructions/second-brain-claudekit/_docs/` duplicate) and locking in the final, definitive `instructions/<repo>/` shape: flat, every source-of-truth markdown regardless of origin nesting, `claude-` prefix on any nested/root name collision. This round verifies that lands cleanly on the Jarvis side, writes a real closing summary of the whole sync build, and gets Jarvis's own notes consistent with the same final definition — the last step before this pipeline moves on to `tests/` and the review system.

Paste into a fresh Claude Code session, cwd = the Jarvis vault root (Windows), Sonnet 5, `high` or `xhigh` effort.

```
A parallel codebase-side round is fixing a real, self-compounding bug: instructions/second-brain-claudekit/ had nested itself into instructions/second-brain-claudekit/_docs/_docs/, growing one level deeper every ~15-minute sync, because sync-manifest.json listed _docs as a whole directory and the copy step never flattened or cleared the destination. The fix makes instructions/<repo>/ flat everywhere, for all 10 entries -- every source-of-truth markdown file (CLAUDE.md, AGENTS.md, README.md, PRD.md, Architecture.md, and similar) lands as instructions/<repo>/<filename>.md directly, regardless of whether it originated at repo root, in a docs-style subfolder, or nested inside .claude/ -- with a claude-<filename>.md prefix on any nested file that would otherwise collide in name with a root-level one.

## 1. Verify the fix landed cleanly on this side

Check whether second-brain-claudekit's Jarvis mirror (20_Progress/AI/Claude Code/second-brain-claudekit/) reflects the corrected, flat instructions/ structure -- no nested _docs/ subfolder, real files directly present. If the codebase session hasn't finished or the sync hasn't run yet, say so explicitly rather than assuming it's already correct; don't guess based on when this prompt was written.

## 2. Audit every one of the 10 mirrors for the same class of bug

The root cause (a directory-shaped sync path never getting flattened) could theoretically have hit any of the 10 entries, not just second-brain-claudekit's _docs case, if any other entry has a directory-shaped instructions-relevant path. Check all 10 mirror folders under 20_Progress/AI/Claude Code/ for any accidental nested subfolder inside what should be a flat instructions-equivalent structure. Report what you find -- this is a real check, not a formality, since round 6's own report only confirmed this for the manifest's paths lists, not for what actually landed on disk.

## 3. Write the closing summary -- the sync build is done, name it as done

This pipeline has spent multiple rounds (2026-08-20 through 2026-08-21) building the live-sync mechanism between second-brain-claudekit's staging folders, Jarvis's mirrors, and (still explicitly unwired) each real project's actual config. That phase of work is now functionally complete. Write one clear, dated Log.md entry that closes it out: what the sync mechanism actually does today (the corrected model -- sandbox/ -> tested-tools/ -> an explicit human decision -> the five live-sync folders -> Jarvis mirrors, read-only), what's still deliberately unwired (the third hop into a real project's live .claude/, still an open question), and that the next phase of this pipeline's work is tests/ (which needs a real refinement pass, already flagged, not attempted yet) and the review system (already has a real Weekly Review as its first Gold Standard Example, per an earlier round). This entry is the actual handoff marker between phases -- write it so a session starting fresh on the tests/reviews phase can read this one entry and know exactly where things stand, without re-reading every round's individual report.

## 4. Bring Jarvis's own notes in line with the final instructions/ definition

Toolkit/Claude Code.md, 10_Areas/AI/Setup/Folder Map.md, and any other Jarvis note that describes instructions/'s structure should match the final rule exactly (flat, every source-of-truth file regardless of origin, the claude- collision prefix) -- check each for drift and fix any that still describe an older or vaguer version of this folder's shape.

Report what you found in items 1-2 (real, not assumed), confirm item 3's entry exists, and list which notes item 4 actually touched.
```

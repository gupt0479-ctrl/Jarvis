---
setup_status: current
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Claude Code/Jarvis/Setup]]"
---

# Git & GitHub Workflow

How this vault uses git. Read this before running any `git switch`, `git checkout`, or branch command in this folder.

## Why this vault's git model has to be simple

This is a single Obsidian vault with one working directory and one person. The `obsidian-git` plugin auto-commits and auto-pushes on a timer (currently every ~120 min, `autoCommitOnlyStaged: false`, `disablePush: false`) and auto-pulls on every Obsidian launch (`autoPullOnBoot: true`, `mergeStrategy: ours`). It has **no concept of branches** — it commits and pushes whatever's in the working tree to whatever is currently checked out, full stop.

That means any workflow depending on a second long-lived branch existing in this same folder is fighting the tool, not working with it. There is exactly one branch in play, ever: `master`.

## The model: one branch, tagged checkpoints

- `master` is the only long-lived branch. It is always checked out here and always reflects current content. obsidian-git commits and pushes to it continuously.
- At the end of each month (or whenever convenient — it's safe to run late), run `/tag-month`. It finds the last real commit of any completed-but-untagged month and creates a lightweight, permanent bookmark for it: "this is what the vault looked like at this point." Never commit to a tag, never branch off one for ongoing work.

Tag names: `YYYY-MM` (plain, no apostrophes — `june'26`-style names cause real shell-quoting pain in PowerShell/bash; learned this the hard way).

## Why `/tag-month` is a command you run, not a hook that runs itself

The obvious automation would be a git `post-commit` hook: tracked in `.claude/git-hooks/`, activated via `core.hooksPath`, firing on every commit (including obsidian-git's unattended ones) to tag and push automatically with zero manual steps. That was built and then deliberately not installed — it's a standing, self-triggering mechanism that pushes to GitHub on its own, forever, with nobody reviewing each occurrence. That category of "runs unsupervised and touches the remote" is worth a human decision every time it's introduced, not something to default into because it's more automatic.

`/tag-month` does the same detection logic (last real commit of any completed-but-untagged month) but only ever runs when explicitly invoked. It's also more robust than a hook in one respect: it checks *every* untagged completed month since the last checkpoint, not just the one bordering the most recent commit — so going a few months without running it doesn't lose anything; the next invocation catches up.

## The one hard rule

**Never run `git switch` or `git checkout` to anything other than `master` in this working directory.**

On 2026-06-25, switching to a branch with a different tree than what's on disk (`master`, which at the time was frozen at a single ancient commit) made git try to delete/recreate ~1,600 files to match that branch's snapshot. Windows file locks interrupted the deletion partway through, twice, leaving `.claude/` files missing from disk until recovered with `git restore .`. No commits or history were ever lost — only uncommitted working-directory state — but it's not a mistake worth repeating.

If `master` and whatever you're switching to ever point at different trees again, fast-forward `master` to match *first* (a pure ref update, touches zero files, cannot fail) before switching into it. Switching only becomes safe once there's nothing left to delete.

## How to look at old content safely

- **Single file, zero risk:** `git show 2026-06:"path/to/note.md"` — prints the file as it was at that tag. No working-directory changes at all.
- **Diff a file across checkpoints:** `git diff master 2026-06 -- "path/to/note.md"`.
- **Browse on GitHub:** repo → Tags → pick the tag → browse the file tree in the browser. Zero local risk, works from anywhere.
- **Need a full real checkout of an old point in time?** Use a separate worktree, never the live vault folder:

```
git worktree add ../jarvis-2026-06 2026-06
```

This checks out that exact historical snapshot into an independent folder. The live vault is never touched. Remove it when done with `git worktree remove ../jarvis-2026-06`.

## Why tags instead of a second branch

A branch sitting "one month behind" master can technically do the same single-file lookups a tag can — `git show`/`git diff` work identically against either. The difference is what each one *invites*:

- A branch shows up in `git branch`, in shell tab-completion, and in GitHub's branch-switcher dropdown — the exact surface that caused the 2026-06-25 incidents. It looks like something to check out and work on.
- A tag shows up in a separate Tags list, and checking one out drops you into a loudly-flagged detached HEAD rather than a normal branch — real friction against treating it as a working branch six months from now when the reason it exists has been forgotten.
- This vault has no concurrent divergent work for a branch to model. A tag matches what's actually true: a closed chapter, not an active line of development.

## History of this decision

- **2026-06-24:** history split into `master` (frozen at the root commit) and `june'26` (everything else), with `june'26` set as GitHub's default branch.
- **2026-06-25:** two incidents where switching to `master` partially deleted `.claude/` files from the live vault (both fully recovered, no content lost).
- **2026-06-25:** collapsed back to a single `master` branch, current and default again. `june'26` and `backup-pre-split-2026-06-24` retired — their content lives on in `master`'s own history plus the `2026-06` tag.
- **2026-06-25:** considered a self-triggering `post-commit` hook for auto-tagging month boundaries; rejected in favor of the explicit `/tag-month` command (`.claude/skills/tag-month.md`) — same detection logic, but nothing runs or pushes to GitHub without being asked.

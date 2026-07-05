---
name: tag-month
description: Creates a YYYY-MM checkpoint tag for any completed month that doesn't already have one, pointing at that month's last real commit. Manual-only — never self-triggers.
setup_status: current
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Claude Code/Jarvis/Setup]]"
---
# tag-month

**Usage:** `/tag-month`

---

## When to Invoke

Whenever you want to checkpoint the vault's git history — typically once a month, but safe to run anytime. It only acts on months that are actually complete (the current, in-progress month is never tagged) and only if no tag exists for that month yet. Running it with nothing to do is a harmless no-op.

This is deliberately manual. See `.claude/GITHUB_WORKFLOW.md` for why month-end tagging is not automated via a git hook.

---

## Instructions

### Step 0 — Confirm we're on `master`

Run `git branch --show-current`. If it's not `master`, stop and tell the user: this vault's workflow only ever uses `master` (see `GITHUB_WORKFLOW.md`); ask them how they ended up elsewhere before doing anything else.

### Step 1 — Find the most recent existing checkpoint tag

```
git tag -l "20[0-9][0-9]-[0-9][0-9]" | sort
```

Take the last one (e.g. `2026-06`). If there are none yet, treat the vault's first commit's month as the starting point.

### Step 2 — Determine today's month and the candidate range

- `today_month` = current system date, formatted `YYYY-MM`.
- The candidate months to check are every month strictly after the last existing tag, up to but **not including** `today_month`. (The current month is never tagged — it isn't over yet.)
- If the last tag's month is the same as, or one before, `today_month`, there may be zero or one candidate months. If multiple months were skipped (e.g. `/tag-month` wasn't run for a while), there can be more than one — handle all of them.

### Step 3 — For each candidate month, check if it has commits and isn't already tagged

For a candidate month `YYYY-MM`:

```
git tag -l "YYYY-MM"
```

If that returns a tag, skip this month (already done).

Otherwise, find its last commit:

```
git log master --format="%H %ad" --date=format:%Y-%m
```

Scan the output (newest-first) for the first line whose date field equals `YYYY-MM`. That commit hash is the tag target. If no line matches, there were no commits that month — skip it, nothing to tag.

### Step 4 — Create and push the tag

For each month that has a target commit and isn't already tagged:

```
git tag -a "YYYY-MM" <commit-hash> -m "End of YYYY-MM - checkpoint"
git push origin "YYYY-MM"
```

Verify the push succeeded (no error output, and `git ls-remote --tags origin | grep YYYY-MM` shows it).

### Step 5 — Report and log

Tell the user exactly which tag(s) were created (or that nothing needed tagging) and which commit each one points to.

If at least one tag was created, append a short entry to `60_Claude/07_AI_Information/Session Logs/log.md`:

```markdown
## [YYYY-MM-DD] checkpoint | Month tag(s) created
- Tagged: 2026-0X -> <short-hash> (<commit subject>)
```

---

## Constraints

- Never tag the current, in-progress month.
- Never overwrite, move, or delete an existing tag. If a tag already exists for a month, leave it alone.
- Never push to anything other than a `refs/tags/*` ref. This skill must never push, force-push, or modify `master` or any other branch.
- Never run this on any branch other than `master` — stop and ask first (see Step 0).
- If `git push origin "YYYY-MM"` fails (e.g. no network), still report the local tag was created and tell the user to push it manually later with `git push origin YYYY-MM` — don't retry in a loop, don't silently swallow the failure.

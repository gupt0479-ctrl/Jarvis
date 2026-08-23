---
type: project
status: active
created: 2026-07-26
updated: 2026-08-22
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]"
tags:
  - internship
  - automation
  - prompts
next: "Prompt 7 (below) is ready to run — git/CI hardening + doc sync. Dossier-filtering / profile-update / resource-expansion work is queued after it, not yet written — say go once Prompt 7's landed."
---
# Claude Code Prompts — Internship Research Loop
This file holds the next prompt to run against `gupta-builds/internship-research-loop`, and only that — it gets wiped and rewritten every build cycle, not accumulated. When a prompt finishes and its result is reviewed, its full text and result move into [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]] and get deleted from here. Don't carry stale prompts forward, and don't skip archiving one just because it's tempting to leave it as a reference — that's what the archive note is for.

## Prompting Guide In Use
[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) — re-apply this on every prompt, don't work from memory of it. Points that have actually mattered on this project so far, keep applying all of them:
- **Front-load everything.** Each prompt assumes zero memory of any conversation that wrote it — full context, full task, full constraints, in the one upfront turn. Ambiguity conveyed progressively across turns costs more tokens and more mistakes than getting it complete the first time.
- **Literal, doesn't silently generalize.** State scope explicitly — a Task Order + Files Touched table beats leaving an agent to infer either. If a prompt is underspecified on a real judgment call (e.g. a preference/priority decision that's the human's to make), say so explicitly and ask, rather than let the model fill the gap with a guess.
- **Effort `high`, generous `max_tokens`.** This project's prompts run long and file-spread; a truncated response mid-task is worse than a slower complete one.
- **Give it your own pre-verified facts, but tell it to re-check them.** Every prompt run against this repo so far has included the researching session's own findings (merge-base, diff scope, test counts) as a head start — and every time, re-verifying them live (not just trusting the text) has caught something: Prompt 4's review found two real gaps Prompt 5 had to fix first; Prompt 6's execution found a real cross-commit dedup regression via per-commit isolation testing that the plan hadn't anticipated. Keep doing both halves — hand over verified state so the session doesn't re-derive everything from scratch, and explicitly instruct it to re-confirm rather than blindly trust it.
- **Ask, don't infer, on anything resembling a value judgment.** Company preference, which folder a dossier belongs in, whether a screening call is a yes or no — these are the human's calls. A prompt only wires up a decision the human already stated; it never expands or invents one on the model's own initiative.

## Current Prompt — Prompt 7: Git/CI Hardening + Documentation Sync
**Why this one's next:** Prompt 6 (archived) got the stranded Prompt 4+5 work committed, pushed, and verified live on 2026-08-21 — 5 commits, 329/329 tests, the capacity-notification/debate-prioritization/recheck-to-Viewed features all confirmed firing correctly against the real pipeline. Independent re-verification on 2026-08-22 confirmed every claim in that report against live git/GitHub state, with nothing found wrong. What's left isn't a bug — it's that the repo has no local safety net against a broken commit reaching `master` (no PR gate exists by design, so nothing currently stops a bad commit before the next scheduled `run.yml` executes against it), and three vault/repo documents still describe the pre-Prompt-6 state as current.

```
You are working in gupta-builds/internship-research-loop (/home/anant_gupta/projects/work/internship-research-loop). Read CLAUDE.md first — it states the load-bearing conventions (zero-LLM in the unattended path, permissive-by-default filtering, fail-closed write-gate ordering, cite-real-data-in-comments) this task must not violate. Context: this repo has a single-branch, direct-to-master convention (no PR flow) — confirm that's still true via `git log` before assuming it. As of 2026-08-22: working tree clean, HEAD matches origin/master, 329/329 tests passing, 5 commits (722ca4d through 3ece859, 2026-08-21) shipped a per-bucket dossier capacity-notification system, a "debate" write-prioritization comparator, debate-loss exclusion, and recheck-to-Viewed (never delete). Re-verify all of this yourself before proceeding — don't take it as given.

This session is git/CI hygiene and documentation accuracy only. Do not touch dossier content, `core/profile.yaml`'s filter/eligibility rules, or add any new pipeline feature. That work is scoped to a separate, later prompt.

## Task Q — Local pre-push test gate
This repo has no PR-based CI gate, so nothing currently stops a commit with failing tests from reaching `origin/master` before the next scheduled workflow run executes against it (`test.yml` catches it on push, but only after the bad commit is already live). Add a tracked hook source file at `scripts/hooks/pre-push`:
```bash
#!/usr/bin/env bash
# Blocks a push if the test suite doesn't pass — this repo has no PR/branch-
# protection gate (single-branch, direct-to-master convention), so this is
# the only thing standing between a broken commit and origin/master before
# the next scheduled run.yml/recheck.yml executes against it.
set -e
cd "$(git rev-parse --show-toplevel)"
if [ ! -x .venv/bin/python ]; then
  echo "pre-push: .venv/bin/python not found, skipping test gate (set up the venv per README.md)" >&2
  exit 0
fi
.venv/bin/python -m pytest tests/ -q
```
Make it executable, copy it into `.git/hooks/pre-push` (also executable — `.git/hooks/` isn't tracked by git, so the copy is what actually takes effect locally), and add a one-line step to README.md's existing "Local dev" section documenting the one-time setup (`cp scripts/hooks/pre-push .git/hooks/pre-push`) so a fresh clone doesn't silently lack it. Verify it actually blocks: temporarily break a test, confirm `git push` (or `git push --dry-run` if you don't want a real push attempt) refuses, fix it back, confirm it proceeds. Report both halves of that check, not just that the file exists.

## Task R — Sync stale documentation to the real shipped state
Three documents still describe the pre-2026-08-21 state. Read each fresh, then update only what's actually stale (don't rewrite what's still accurate):
1. **Vault note `20_Progress/Internship/Building System/Source of Truth.md`** — its `next:` frontmatter field (last updated 2026-07-26) says "implement the dossier count-limit spec (still not in code)." It's in code now, live, and firing (issues #4-8 are proof). Update the field and the body's "Resource Limits" section to describe what's actually shipped (notification-not-refusal, per-bucket 50/global 201, the debate comparator, debate-loss exclusion) instead of "designed, not yet implemented."
2. **Vault note `20_Progress/Internship/Building System/System - Build Log.md`** — read it fresh and add an entry for the 2026-08-21 commit sequence (5 commits) and the 2026-08-22 git/CI reconciliation, matching that note's existing per-session entry style. Don't restructure the note, just extend it.
3. **This repo's `PRD.md`** — its "Current Status" section is dated 2026-07-18 and its "Open Backlog" still lists the count-limit spec as pending. Update "Current Status" with real current numbers (test count, dossier total, what's live) and close out the backlog items that are now actually done. In the "Risks" section: the fine-grained PAT (`JARVIS_PUSH_TOKEN`) and `FIRECRAWL_API_KEY` expiry dates are still recorded nowhere — you cannot check an existing secret's expiry via `gh` or any API (GitHub deliberately doesn't expose this), so don't try. Instead, add one line to the Risks section stating plainly that this needs a one-time manual check by the human at github.com/settings/tokens (for the PAT) and Firecrawl's own dashboard (for the API key), with today's date, so it's a dated, visible gap rather than a silent one. Also note the GitHub Actions minutes-usage risk is still unmonitored — check `gh api /repos/gupta-builds/internship-research-loop/actions/cache/usage` or the billing/usage API if accessible and report actual current usage; if it's not accessible with the available token, say so rather than guessing, and leave the risk noted as still-unmonitored.

## Task S — Sanity-check the graphify git hooks don't interact badly with the new pre-push hook
A separate, unrelated session already installed `post-commit`, `post-checkout`, and `post-merge` hooks in `.git/hooks/` for a graphify → Jarvis knowledge-graph sync (detached/background, logs to `~/.cache/graphify-jarvis-sync.log`). Task Q adds a `pre-push` hook — a different hook type, so there's no direct conflict, but confirm: the pre-push hook's own execution doesn't hang or block on anything graphify-related, and a normal `git commit` + `git push` sequence still completes in reasonable time with all four hooks present. Report what you observed, not just that there's no obvious conflict on paper.

## Explicitly out of scope
Dossier content, `core/profile.yaml`'s filter/eligibility rules, any new pipeline feature, git config changes (you're under the same hard rule as every session before you not to touch git config — if `pull.rebase` still isn't set locally, that's a known, correctly-still-open item for the human to run themselves, not yours to fix), rebasing/rewriting history, force-push.

## Report back
For Task Q: confirmation the hook file exists, is executable, is installed, and your actual block/pass test results. For Task R: a summary of what changed in each of the three documents (not the full diffs, just what was stale and what it now says). For Task S: what you observed running the full hook chain. State plainly anything you found that contradicted what this prompt told you.
```
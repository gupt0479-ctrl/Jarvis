---
type: evergreen
status: sprout
created: 2026-08-22
updated: 2026-08-22
tags:
  - evergreen
  - ai-agents
  - graphify
notes:
  - "[[40_Resources/CS/Concepts/Helpful Tools/Graphify]]"
  - "[[40_Resources/CS/AI/Workflows/Claude Code/Graphify Workflow]]"
  - "[[60_Claude/40_Project_Briefs/Graphify — Internship Research Loop Implementation]]"
next: "Apply this exact procedure to the next codebase that needs mapping; update this note if the procedure changes in a way worth capturing"
---
# How to use Graphify
==Code stays mapped on its own once the hooks are installed; docs, PRDs, and READMEs do not — that gap is the one fact this whole procedure exists to keep an agent from forgetting.== This is the reusable operating procedure. For what graphify actually is, read [[40_Resources/CS/Concepts/Helpful Tools/Graphify|Graphify]] first. For the full command/mechanism reference, read [[40_Resources/CS/AI/Workflows/Claude Code/Graphify Workflow|Graphify Workflow]]. For one real, working example with its actual gaps named, read [[60_Claude/40_Project_Briefs/Graphify — Internship Research Loop Implementation|Graphify — Internship Research Loop Implementation]].
## Before Doing Anything
Check what already exists — do not assume a fresh setup:
```bash
ls graphify-out/ 2>/dev/null && echo "graph already exists"
cd <repo> && git rev-parse --is-inside-work-tree 2>/dev/null && graphify hook status
```
If `graphify-out/graph.json` exists, this repo has already been mapped — skip to **Repo Already Mapped** below. If not, this is a first build.
## First Build In A Repo
1. **Decide if it's worth it.** A handful of files that already fit in one context window get ~1x token reduction (measured on graphify's own `httpx` benchmark) — the graph adds structural clarity there, not savings. Worth building once corpus size makes cross-file connections hard to hold in memory; see [[40_Resources/CS/Concepts/Helpful Tools/Graphify|Graphify]]'s "Where To Reach For It."
2. **Confirm the interpreter.** `python3 -c "import graphify" || uv tool install graphifyy`. Prefer `uv tool install`/`pipx` over plain `pip` — see [[40_Resources/CS/AI/Workflows/Claude Code/Graphify Workflow|Graphify Workflow]]'s install section for why.
3. **Run the build.** `/graphify .` inside the coding assistant (add `--mode deep` only if the user actually asked for depth — it costs more tokens for richer INFERRED edges). Follow the skill's own step-by-step instructions when invoked; do not improvise around them.
4. **Decide the Obsidian target.** If this vault (Jarvis) should mirror the graph, the convention this vault uses is `60_Claude/40_Project_Briefs/<RepoName>/`, passed as `/graphify . --obsidian --obsidian-dir "<path to that folder>"` in the same build pass. This folder becomes graphify-owned — it will never overwrite a pre-existing note there, but treat it as a generated mirror, not a place to hand-write notes.
5. **Wire the live sync.** `graphify hook install` (official — `post-commit` + `post-checkout`, AST-only, zero LLM, **and a git merge driver** for `graph.json` — confirm the merge driver actually lands, per the gap noted in the Internship implementation). Then add a `post-merge` hook if this repo's own automation ever commits from somewhere other than this machine (CI, GitHub Actions) — `git pull`ing those commits down needs something to notice, since `graphify hook install` does not cover that trigger.
6. **Make the agent actually use it.** `graphify claude install` — writes `CLAUDE.md` guidance plus a `PreToolUse` hook that nudges (or blocks, in `--strict` mode) raw file reads toward `graphify query` instead. Skipping this step means the graph exists but nothing routes an agent to it.
7. **Gitignore correctly.** At minimum: `cost.json` (per the official README), `cache/`, and anything machine-local (`.graphify_python`, `.graphify_root`, `.rebuild.lock`, `.pending_changes`). Check for a dated `graphify-out/<YYYY-MM-DD>/` backup folder too — not in the official docs, but real (see the Internship implementation note for the evidence). Do **not** gitignore `manifest.json` or `graph.json` — those are meant to be committed.
## Repo Already Mapped
1. **Code change** — nothing to do if hooks are installed; `graphify update` already ran. If hooks are *not* installed yet, run `graphify hook install` now rather than leaving future changes unmapped.
2. **Doc/PRD/README/PDF change** — run `/graphify --update` in a live session. This is the one thing that never becomes automatic — a git hook cannot spawn the subagents that pass needs.
3. **New file type never seen before** (a new language, a new doc format) — a normal `/graphify --update` picks it up; nothing special needed unless it's a format graphify doesn't support at all (check [[40_Resources/CS/AI/Workflows/Claude Code/Graphify Workflow|Graphify Workflow]]'s file-type coverage, or the project's own README).
4. **Something looks wrong** (node counts swinging wildly between rebuilds, stale-looking data) — check `graphify --version` against the latest PyPI release before assuming the graph itself is broken. The Internship implementation hit exactly this and traced it to a 44-patch-version gap, not a real extraction problem.
## The One Rule That Matters Most
| Change type | Propagates automatically once hooks are installed? |
|---|---|
| Code (any language graphify parses) | Yes — `graphify update`, zero LLM |
| Docs, PRDs, READMEs, PDFs, images | **No** — needs `/graphify --update` in a live session |
| Commits made somewhere other than this machine (CI) | Only if a `post-merge` hook was added — not part of the official `graphify hook install` |
Never assume the graph is current for a doc-heavy repo just because hooks are installed. Check `graphify-out/manifest.json`'s timestamps, or just run `/graphify --update` — it no-ops cheaply if nothing changed.
## Health Check — Run This On Any Obsidian-Synced Setup
Three numbers should stay close together: the vault folder's real `.md` file count, `.graphify_obsidian_manifest.json`'s tracked-file count, and `graph.json`'s current node count. On **0.9.17+**, a node dropping out of the graph self-prunes its old note automatically — the gap should stay near zero on its own. On anything older, or after a burst of concurrent hook-triggered exports (no lock file guards the manifest write, unlike `graph.json`'s own `.rebuild.lock`), a real gap means orphans accumulated and need one-time manual cleanup (real precedent: 350 found and removed on this vault's own Internship mirror — see [[60_Claude/40_Project_Briefs/Graphify — Internship Research Loop Implementation|the Internship implementation note]] for the exact root cause and the git-verified cleanup).
```bash
ls <vault-target>/*.md | wc -l
python3 -c "import json; print(len(json.load(open('<vault-target>/.graphify_obsidian_manifest.json'))['files']))"
python3 -c "import json; print(len(json.load(open('graphify-out/graph.json'))['nodes']))"
```
If the vault itself is a git repo (check `git -C <vault-root> rev-parse --is-inside-work-tree` — don't assume "no `.git`" from a truncated directory listing), it's a safety net for exactly this kind of cleanup: `git status` shows deletions before they're permanent, `git show <commit>:<path>` confirms a file's origin (a real `graphify/EXTRACTED` tag settles "is this debris or content" definitively), and committing the cleanup deliberately beats letting an unrelated auto-commit finalize an unreviewed batch.
## Open Items Worth Checking On Any New Setup
- [ ] Confirm `graphify hook install`'s git merge driver actually landed (`graphify hook status` reporting hooks "installed" is not sufficient proof on a pre-0.9.17 install — check `.git/config` for `[merge "graphify"]` and `.gitattributes` directly; `CHANGELOG.md` #1902 named and fixed this exact lie)
- [ ] Run the health check above once after initial setup and again after any period of heavy concurrent-session activity
- [ ] Prefer `uv tool install graphifyy` from the start — it's what makes `uv tool upgrade graphifyy` a clean one-liner later, and avoids the two-separate-installs confusion this vault's own Internship build hit (a stale `uv tool` copy and a newer `pip` copy both present, `pip`'s silently winning on `PATH`)
## Links
[[40_Resources/CS/Concepts/Helpful Tools/Graphify|Graphify]] · [[40_Resources/CS/AI/Workflows/Claude Code/Graphify Workflow|Graphify Workflow]] · [[60_Claude/40_Project_Briefs/Graphify — Internship Research Loop Implementation|Graphify — Internship Research Loop Implementation]]

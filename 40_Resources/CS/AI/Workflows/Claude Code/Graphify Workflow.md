---
type: evergreen
status: sprout
created: 2026-08-22
updated: 2026-08-22
tags:
  - evergreen
  - graphify
  - claude-code
source_url: https://github.com/Graphify-Labs/graphify
notes:
  - "[[40_Resources/CS/Concepts/Helpful Tools/Graphify]]"
  - "[[60_Claude/40_Project_Briefs/How to use Graphify]]"
next:
---
# Graphify Workflow
==The graph lives in `graphify-out/graph.json`; every other output (`GRAPH_REPORT.md`, `graph.html`, the Obsidian export) is a view derived from it, and `graphify update` only ever touches the code-derived view — a docs/PDF change needs a full `/graphify --update` inside an LLM session to reach the graph at all.== See [[40_Resources/CS/Concepts/Helpful Tools/Graphify|Graphify]] for what the tool is and why it exists; this note is the mechanism and command reference.
## Install
```bash
uv tool install graphifyy      # recommended — isolated env, clean uv tool upgrade path
# or: pipx install graphifyy
graphify install                # registers the /graphify skill with Claude Code
```
*Avoid plain `pip install` on Mac/Windows if avoidable* — the skill resolves its Python interpreter at runtime from `graphify-out/.graphify_python`, and a `pip`-installed copy can point at the wrong environment later, producing `ModuleNotFoundError: No module named 'graphify'`. `uv tool install`/`pipx install` isolate the package and avoid this. Check what's actually installed: `python3 -c "import graphify; print(graphify.__file__)"`.
**Staying current matters more than it looks.** The package ships near-daily patch releases (0.9.44 → 0.9.48 across five days observed in `CHANGELOG.md`), and several fixes land directly on the git-hook workflow below — e.g. 0.9.46 stopped `post-checkout` from rebuilding on a no-op branch creation, 0.9.47 made a no-op `graphify update` byte-identical instead of reshuffling `graph.json` on every run. Check `graphify --version` against the latest PyPI release before assuming odd rebuild behavior is a bug in this vault's own setup rather than a stale install.
## The Three-Pass Pipeline
1. **Code (free)** — tree-sitter AST, 37 languages, `ProcessPoolExecutor`-parallel (measured ~1.66x faster than sequential on an 84-file corpus). SQL gets deterministic table/view/FK/JOIN extraction. Code files never reach the LLM pass; if the corpus is code-only, Pass 3 is skipped entirely.
2. **Video/audio (free)** — faster-whisper, local. The transcription prompt is seeded with the codebase's own current god-nodes so the transcript stays domain-focused.
3. **Docs/PDFs/images (costs tokens)** — parallel Claude subagents (or a configured API backend for headless `graphify extract`), each reading a batch of files and returning a `{nodes, edges}` JSON fragment, merged into the graph.
## Community Detection And Confidence
Communities come from the **Leiden algorithm** over the edge graph — no embeddings, no vector store; the `semantically_similar_to` edges Claude extracts *are* the similarity signal feeding the clustering directly. Every edge carries one of three confidence tags:
| Tag | Meaning | `confidence_score` |
|---|---|---|
| `EXTRACTED` | explicit in source (import, direct call) | always `1.0` |
| `INFERRED` | reasonable deduction | discrete rubric: `0.95` near-certain → `0.85` strong → `0.75` reasonable → `0.65` weak → `0.55` speculative (never a flat `0.5`) |
| `AMBIGUOUS` | uncertain, flagged for review | `0.1`–`0.3` |
`graph.json` uses NetworkX's node-link format. Each node carries `id`, `label`, `file_type` (`code`/`document`/`paper`/`image`/`rationale`), `source_file`. Each edge carries `source`, `target`, `relation`, `confidence`, `confidence_score`, `source_file`. Group relationships (3+ nodes) live separately in `G.graph["hyperedges"]`. Every extracted file is SHA256-fingerprinted in `graphify-out/cache/` — a re-run skips anything unchanged.
## Core Commands
```bash
/graphify .                        # build graph for current folder (inside the AI assistant)
/graphify . --update               # re-extract only changed files
/graphify . --mode deep            # more aggressive INFERRED-edge extraction, richer but pricier
/graphify . --cluster-only         # rerun community detection without re-extracting
/graphify . --no-viz               # skip graph.html, just report + JSON
/graphify . --obsidian --obsidian-dir <path>   # export as an Obsidian vault into an existing vault — never overwrites a file it didn't create
/graphify . --watch                # foreground/background watcher, auto-rebuilds as files change (no LLM needed for code)

graphify query "<question>"        # scoped natural-language subgraph, from the shell (no assistant needed)
graphify path "<Node>" "<Node>"    # shortest path between two named things
graphify explain "<Node>"          # everything connected to one node, plain language
graphify update <path>             # CLI form of --update — code-only, zero LLM, what git hooks call
graphify hook install              # post-commit + post-checkout auto-rebuild, AND a git merge driver
graphify hook status               # check whether the hooks (and merge driver) are actually installed
graphify export obsidian --dir <path>   # re-run just the Obsidian export step against the current graph.json
graphify claude install            # writes CLAUDE.md guidance + a PreToolUse hook nudging the agent to query the graph before grepping raw files
```
Full reference (every flag, every backend, every platform's install command) lives in the repo's own `README.md` — this note captures what's actually load-bearing for how this vault uses graphify, not the full surface.
## The Official "Team Setup" Workflow
Straight from the project's own README, and the standard this vault's git-hook wiring should be checked against:
1. One person runs `/graphify .` and commits `graphify-out/` — `graphify-out/` is meant to be committed so everyone starts from the same map.
2. Everyone pulls; their assistant reads the graph immediately.
3. **Run `graphify hook install`** — auto-rebuilds after each commit (AST only, no API cost) *and* installs a **git merge driver** so `graph.json` never carries conflict markers when two people commit in parallel; it union-merges automatically instead.
4. When docs or papers change, run `/graphify --update` inside an assistant session to refresh those nodes — this step has no zero-LLM equivalent.
**Recommended `.gitignore` additions** (from the README directly):
```
graphify-out/cost.json        # local only — per-run token log
# graphify-out/cache/         # optional: commit for speed, skip to keep the repo small
```
`manifest.json` is portable (relative-path keys, re-anchored on load) — committing it is safe and avoids a full rebuild on first checkout, so it should **not** be gitignored.
## What's Automatic vs. What Needs A Live Session
| Trigger | What runs | LLM needed |
|---|---|---|
| `git commit` / `git checkout` (hooks installed) | `graphify update` — AST rebuild of changed code files | No |
| `git pull` bringing in commits made elsewhere (e.g. CI) | Nothing, unless a `post-merge` hook is added separately — `graphify hook install` only wires `post-commit`/`post-checkout` | No, if added |
| A doc, PRD, README, or PDF changes | Nothing automatic — needs `/graphify --update` in a live assistant session | **Yes** |
| A brand-new corpus, or `--mode deep` | `/graphify .` from scratch | Yes, for the docs/media pass |
This split is the single most important operational fact about graphify: **code stays live on its own; everything else needs a human or agent to actually ask for it.**
## Claude Code Prompt-Cache Interaction
`graphify extract`/`update` writes into the workspace (`graph.json`, `graphify-out/`). If those paths aren't excluded from what Claude Code re-uploads for prompt caching, every graphify write can invalidate the cache and force a full re-upload on the next turn. The project's own fix: add a `.claudeignore`:
```text
# .claudeignore
graph.json
graphify-out/
```
## MCP Serving
```bash
python -m graphify.serve graphify-out/graph.json                 # local stdio MCP server
python -m graphify.serve graphify-out/graph.json --transport http --port 8080 --api-key "$SECRET"   # shared team server
```
Gives an assistant structured tools instead of file reads: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, plus PR-related tools (`list_prs`, `get_pr_impact`, `triage_prs`) if `graphify prs` is in use. `--transport stdio` (default) is one process per developer; `--transport http` lets a whole team point at one running server.
## Troubleshooting Notes Worth Keeping
- **Fewer nodes after `--update`** — expected if files were deleted; pass `--force` (or `GRAPHIFY_FORCE=1`) to accept a smaller rebuild instead of the safety refusal.
- **`graph.json` has conflict markers after two people commit at once** — this is exactly what `graphify hook install`'s merge driver prevents; if it's happening, the merge driver likely isn't installed (check `graphify hook status`, and check `.git/config`/`.gitattributes` directly — `hook status` reports the hooks as installed even when the merge driver silently failed to register, see the version-gated bug below).
- **`graphify hook install` reports success but `.git/config` has no `[merge "graphify"]` and no `.gitattributes` exists** — a real, named, fixed bug, not a misconfiguration: `CHANGELOG.md` #1902 (0.9.17, 2026-07-16) — the feature was announced in 0.7.0 but did nothing until 0.9.17 actually wired it up. Confirmed live on a 0.9.4 install. Fix: upgrade past 0.9.17, then `graphify hook uninstall` **and** a fresh `graphify hook install` — re-running install alone is a no-op once the hook file already carries graphify's marker.
- **The Obsidian export folder accumulates stale notes that don't correspond to any current graph node** — also version-gated: `CHANGELOG.md` #1896 (same 0.9.17 release) made `graphify export obsidian` prune notes for nodes that left the graph; before that fix, old and new notes just merge forever. A node count that shrinks across rebuilds (refactor, `--force`, a version-gap-triggered miscount) leaves its old notes behind permanently on a pre-0.9.17 install. Diagnostic: compare the vault folder's real `.md` count against `.graphify_obsidian_manifest.json`'s tracked-file count and the current `graph.json` node count — a real gap between all three means orphans, not a fluke. Mechanism, read directly from `export.py`: the manifest is written as `{"files": sorted(set(_written))}` — only the current run's write set, never merged with prior history — so any file the manifest ever forgets becomes permanently invisible to `_owned_write`'s "don't overwrite what I don't own" guard, mistaking old debris for a real user note forever. 0.9.17's fix (`stale = _owned - written - skipped`, then delete) only prunes files still present in `_owned` at the moment it runs — it cannot retroactively clean up anything that fell out of the manifest under the pre-fix behavior; that needs a one-time manual pass (compare disk vs. manifest vs. graph, delete the confirmed gap). No lock file guards this manifest read-modify-write the way `graph.json` has its own `.rebuild.lock` — two genuinely concurrent `export obsidian` calls against the same target can still race and drop ownership of whichever one loses.
- **Empty nodes/edges for docs/PDFs** — that pass needs an LLM; a code-only corpus needs no key at all, a mixed one does.
- **`graph.html` too large to open (>5000 nodes)** — skip it: `graphify cluster-only <path> --no-viz`, then query the JSON directly.
## Links
[[40_Resources/CS/Concepts/Helpful Tools/Graphify|Graphify]] for what this is and when to reach for it. [[60_Claude/40_Project_Briefs/How to use Graphify|How to use Graphify]] for the concrete step-by-step this vault's agents should follow. [[60_Claude/40_Project_Briefs/Graphify — Internship Research Loop Implementation|Graphify — Internship Research Loop Implementation]] for one real, working example of this whole workflow end to end.

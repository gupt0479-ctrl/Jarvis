---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - tooling
source_url: https://github.com/safishamsi/graphify
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Graphify

**What it is:** A Claude Code skill (`/graphify`) that reads a folder of files — code, PDFs, markdown, images, screenshots — extracts concepts and relationships using Claude's vision and tree-sitter AST parsing, and outputs a NetworkX knowledge graph with an interactive HTML viewer and an Obsidian vault export.

**What it actually does:** `pip install graphifyy && graphify install` adds `/graphify` to Claude Code. Running `/graphify .` on a codebase or notes folder produces: `graph.html` (interactive vis.js graph with community detection, clickable nodes, search), `obsidian/` (ready-to-open as Obsidian vault with wikilinks), `GRAPH_REPORT.md` (god nodes, surprising connections, suggested queries), and `graph.json` (persistent, queryable across sessions). The SHA-256 cache means re-runs only process changed files. The reported token reduction is 71.5x on a 52-file mixed corpus (code + papers + images) compared to reading raw files.

**Why it matters for this vault/workflow:** This is a direct enhancement to Jarvis. The Obsidian export means graphify can analyze a project codebase and drop the resulting knowledge graph directly into the vault — creating `reference/` notes with cross-links automatically. For UROP research, running `/graphify ./raw` on a folder of papers and screenshots would build a queryable knowledge graph of concepts and citations that Claude can then reason over without re-reading all the files. The `--wiki` flag generates Wikipedia-style articles per community that any agent can navigate by reading markdown files.

**How to use it:**
```bash
pip install graphifyy && graphify install
# Then in Claude Code:
/graphify .                    # current directory
/graphify ./papers --mode deep # aggressive edge extraction
/graphify add https://arxiv.org/abs/...  # add a paper
/graphify query "what connects X to Y?"
/graphify ./raw --obsidian     # export directly as Obsidian vault
graphify hook install          # auto-rebuild on every git commit
```

**Failure modes / limitations:** PyPI package is `graphifyy` (double-y) while the `graphify` name is being reclaimed — easy to get wrong. The 71.5x token reduction claim is from a specific test corpus; simple codebases show ~1x (no compression benefit). "INFERRED" edges are LLM guesses — they're tagged as such, but they can mislead if treated as facts. The interactive graph visualization requires a browser and doesn't embed in Obsidian natively (it's an HTML file, not a canvas).

**Verdict:** Run `/graphify` on every new research corpus before starting deep work — the `GRAPH_REPORT.md` alone is worth it for identifying god nodes and surprising cross-connections that aren't obvious from reading files linearly.

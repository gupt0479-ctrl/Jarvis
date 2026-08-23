---
type: evergreen
status: sprout
created: 2026-08-22
updated: 2026-08-22
tags:
  - evergreen
  - graphify
  - tooling
notes:
  - "[[40_Resources/CS/AI/Workflows/Claude Code/Graphify Workflow]]"
  - "[[60_Claude/40_Project_Briefs/How to use Graphify]]"
  - "[[40_Resources/CS/Repos]]"
next:
---
# Graphify
==Graphify turns a folder of code, docs, PDFs, images, and video into a real graph you traverse — not a vector index you search — and the code half is built with local tree-sitter AST parsing, so it costs zero LLM tokens and never leaves the machine.== Open source (Apache-2.0), `github.com/Graphify-Labs/graphify`, PyPI package `graphifyy` (double-y — other `graphify*` packages on PyPI are unaffiliated), CLI command `graphify`. Y Combinator S26 company.
## What Problem It Solves
Reading raw files to answer "how does X connect to Y" burns tokens linearly with corpus size and misses connections that live in a different file than the question. Graphify's own benchmark on a 52-file mixed corpus (code repos + 5 papers + 4 images) measured **71.5x fewer tokens per query** versus reading the raw files directly — build the graph once, then every subsequent query reads the compact graph instead. The reduction scales with corpus size, not flatly: a 6-file corpus already fits in a context window, so the value there is structural clarity, not compression (graphify's own `httpx` synthetic-library test measured ~1x — no real savings on a tiny repo). This is *why* [[60_Claude/40_Project_Briefs/How to use Graphify|How to use Graphify]] treats "is this corpus actually big enough to matter" as the first real decision, not a formality.
## What It Actually Is — And Is Not
Two different things share the graphify name, and conflating them was the source of real confusion this note exists to close:
- **graphify (this note, what we use)** — the open-source CLI/skill at `github.com/Graphify-Labs/graphify`. Runs on demand (`/graphify .` in an AI coding assistant, or `graphify update` from a shell/git hook). Free, local-first, Apache-2.0.
- **graphify Enterprise** — a separate, commercial, early-access product at `graphify.com`, built by the same team (waitlist, "free trial launching soon" as of this note's writing). Positioned as "the always-on layer" — continuous background mapping across meetings, files, docs, and code, not just an on-demand codebase graph. Not what this vault has installed or uses. `graphify.com/docs` documents *that* product, not the OSS CLI — if a docs link from `graphify.com` looks thin on git-hook or Obsidian-export detail, that's why: those are OSS-CLI-specific features documented in the [GitHub repo](https://github.com/Graphify-Labs/graphify) itself, not on the marketing site.
## The Three-Pass Pipeline
Full mechanism in [[40_Resources/CS/AI/Workflows/Claude Code/Graphify Workflow|Graphify Workflow]]; the shape:
1. **Code** — tree-sitter AST, 37 languages, fully local, zero LLM cost. Classes, functions, imports, call graphs, inline comments.
2. **Video/audio** — faster-whisper, fully local. Transcription prompt is seeded with the codebase's own top god-nodes to focus the transcript on the actual domain.
3. **Docs/PDFs/images** — Claude subagents (or a configured API backend), the only pass that costs tokens. Skipped entirely on a code-only corpus.
## Confidence Tags
Every edge graphify draws is labeled, never presented as flat fact:
- **EXTRACTED** — explicit in the source (an import, a direct call). Confidence 1.0, always.
- **INFERRED** — a reasonable deduction, carrying a `confidence_score` on a discrete rubric (0.95/0.85/0.75/0.65/0.55 — never a flat 0.5).
- **AMBIGUOUS** — uncertain, flagged in `GRAPH_REPORT.md` for a human to check.
*Mechanism:* community detection (grouping the graph into subsystems) runs on the [[40_Resources/CS/AI/Workflows/Claude Code/Graphify Workflow|Leiden algorithm]] directly over this edge structure — no embeddings, no vector database. The `semantically_similar_to` edges Claude extracts *are* the similarity signal; there's no separate step.
## Where To Reach For It
*Good fit:* a codebase large enough that "where does this connect" isn't answerable by memory or one `grep` — multi-module repos, anything with real cross-file coupling, anything a coding agent will revisit across many sessions. Also fits non-code corpora: papers, meeting transcripts, PDFs.
*Bad fit:* a handful of files that already fit in one context window — the graph adds structural clarity there, not token savings, and building it still costs real tokens on the docs/media pass.
## Contrast With Nearby Tools
- **Claude Context** (`github.com/zilliztech/claude-context`) — an MCP server that indexes a codebase into Milvus for vector/semantic code search. Per this vault's own [[40_Resources/CS/Repos|Repos]] note, it's complementary to graphify, not competing: graphify gives structure (a real traversable graph, confidence-tagged), Claude Context gives semantic recall over embeddings. Different retrieval mechanism entirely — graphify has *no* embedding step by design.
- **Plain grep/Read** — still correct for a small, unfamiliar-shape task (find one string, read one file). Graphify pays off once the same question needs asking repeatedly, or the answer spans files a single grep won't connect.
## Privacy And Licensing
Code is parsed 100% locally — a code-only corpus needs no API key at all. Docs/PDFs/images go through whatever model backend is configured (the IDE session's own model when run as a skill; an explicit API key only for headless `graphify extract` in CI). No telemetry. Local query logging (`~/.cache/graphify-queries.log`) is opt-in via `GRAPHIFY_QUERY_LOG_ENABLE=1`, and does not store full subgraph responses by default. Apache-2.0 license — free to use, modify, and self-host indefinitely; graphify Enterprise is the only paid tier, and it's a different product.
## Open Questions
- [ ] Has graphify Enterprise moved past waitlist/early-access since this note was written — worth re-checking if the "always-on" continuous-sync need ever outgrows the git-hook approach in [[60_Claude/40_Project_Briefs/How to use Graphify|How to use Graphify]]
- [ ] CausalOps already runs its own graphify report per [[40_Resources/CS/Repos|Repos]]'s dropped-tools note ("CausalOps's own graphify report already gives blast-radius visibility") — worth checking whether that setup follows the same pattern documented here, or predates it
## Links
[[40_Resources/CS/AI/Workflows/Claude Code/Graphify Workflow|Graphify Workflow]] for the full command reference and pipeline mechanics. [[60_Claude/40_Project_Briefs/How to use Graphify|How to use Graphify]] for the operating procedure a coding agent should actually follow. [[40_Resources/CS/Repos|Repos]] for where this sits in the broader tool inventory.

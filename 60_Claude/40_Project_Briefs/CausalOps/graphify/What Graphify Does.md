---
tags: [graphify, tooling, knowledge-graph, obsidian]
---

# What Graphify Does

## What It Is

Graphify (`graphifyy` on PyPI) is a CLI tool that turns any folder of files — code, docs, PDFs, images, video — into a navigable knowledge graph. It produces three outputs:

1. **`graphify-out/graph.json`** — GraphRAG-ready JSON (nodes, edges, communities, provenance)
2. **`graphify-out/graph.html`** — Interactive force-directed visualization (open in browser)
3. **`graphify-out/GRAPH_REPORT.md`** — Plain-language community summary

Optionally, with `--obsidian --obsidian-dir <vault-path>`, it writes one Obsidian `.md` note per community directly into your vault, with wikilinks connecting related concepts.

## The Pipeline It Would Have Run

For this repo (`/home/anant_gupta/projects/hub/CausalOps/`), graphify would have:

### Step 1 — Detect Files
```
Corpus: ~50 files
  code:   ~42 files (.py, .ts, .tsx)
  docs:    ~7 files (.md)
```

### Step 2 — Structural Extraction (AST, free)
```bash
python -c "
from graphify.extract import collect_files, extract
from pathlib import Path
result = extract(code_files, cache_root=Path('.'))
Path('graphify-out/.graphify_ast.json').write_text(json.dumps(result))
"
```
Extracts imports, class definitions, function calls, inheritance — anything AST can see deterministically.

### Step 3 — Semantic Extraction (LLM-powered, parallel subagents)
Splits non-code files (`.md`, `.pdf`) into chunks of 20-25 files. Dispatches parallel subagents — one per chunk — each reading the files and producing:
- Named concept nodes with attributes
- `EXTRACTED` (explicit), `INFERRED` (reasoned), `AMBIGUOUS` (flagged) edges
- Confidence scores on every edge

### Step 4 — Graph Build + Community Detection
Merges AST + semantic outputs. Runs Louvain community detection to identify clusters (e.g., "causal estimation layer", "agent orchestration", "event bus").

### Step 5 — Obsidian Output
With `--obsidian --obsidian-dir ~/vaults/Jarvis/60_Claude/40_Project_Briefs/CausalOps/`:
- Creates one note per community with a list of nodes and wikilinks
- Adds `GRAPH_REPORT.md` as the index
- Wikilinks point to concept nodes across communities

## The Commands That Would Have Been Run

```bash
# Install (if not already):
pip install graphifyy

# Full pipeline with Obsidian export:
graphify /home/anant_gupta/projects/hub/CausalOps \
  --obsidian \
  --obsidian-dir "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/40_Project_Briefs/CausalOps"

# To use Gemini instead of Claude for semantic extraction:
GEMINI_API_KEY=... graphify /home/anant_gupta/projects/hub/CausalOps --obsidian --obsidian-dir "..."

# Deep mode (more INFERRED edges):
graphify /home/anant_gupta/projects/hub/CausalOps --mode deep --obsidian --obsidian-dir "..."

# Query the graph after building:
graphify /home/anant_gupta/projects/hub/CausalOps query "how does causal estimation work?"
graphify /home/anant_gupta/projects/hub/CausalOps path "GraphState" "DoWhy"
```

## Why No `graphify-out/` Folder Exists in the Repo

→ See [[How Notes Were Actually Written]]. Graphify was NOT used. The notes were hand-written.

## What the Graphify Output Would Have Looked Like vs What Was Written

| Aspect | Graphify auto-output | Hand-written notes (what actually happened) |
|--------|---------------------|----------------------------------------------|
| Note per unit | One note per **community** (cluster of related nodes) | One note per **file/module** |
| Content | Node list + edge summaries | Full narrative: signatures, constants, data flow |
| Wikilinks | Auto-generated from graph edges | Hand-curated to semantically related modules |
| Provenance | EXTRACTED / INFERRED / AMBIGUOUS labels | No provenance labels |
| Index | `GRAPH_REPORT.md` | `_Index.md` with MOC structure |
| SQL schemas | Not captured | Explicitly written out in Memory Layer notes |
| Critical warnings | Not captured | "DO NOT TOUCH", ATE withholding rationale captured explicitly |

Graphify is fast and broad. Hand-written notes are slower but include narrative context that LLM extraction misses (invariants, design rationale, "never do X" rules).

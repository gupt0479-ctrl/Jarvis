---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - mcp
  - agents
source_url: https://github.com/zilliztech/memsearch
notes:
  - "[[40_Resources/CS/Repos]]"
---
# memsearch (Zilliz)

**What it is:** A cross-platform semantic memory layer for AI coding agents — captures every conversation turn to daily markdown files, indexes them with ONNX embeddings + Milvus (locally via Milvus Lite, no server required), and exposes hybrid BM25 + dense vector search via an MCP skill (`/memory-recall`).

**What it actually does:** Install as a Claude Code plugin (`/plugin install memsearch`). After install, every conversation turn is summarized and appended to `.memsearch/memory/YYYY-MM-DD.md` via a Stop hook. The markdown files are the source of truth — Milvus is a rebuildable shadow index. When you ask "what did we decide about Redis?" Claude auto-invokes memory tools, or you type `/memory-recall Redis`. The 3-layer progressive retrieval: L1 semantic search → L2 expand to full section → L3 raw session transcript. Memory flows across Claude Code, OpenClaw, OpenCode, and Codex CLI from the same store — one agent's sessions are searchable from another agent. The ONNX bge-m3 embedding model (~558MB) runs locally with no API key.

**Why it matters for this vault/workflow:** Memsearch is a lower-friction version of CPR — it captures memory automatically (no manual `/compress` step) and searches semantically (not just by filename). The markdown-as-source-of-truth philosophy aligns with Jarvis: the `.memsearch/memory/` files could be symlinked into or synchronized with Jarvis's `thinking/session-logs/` folder, creating a unified searchable timeline of all Claude work. The `project_review` and `user_profile` background tasks (disabled by default) would generate `PROJECT.md` and `USER.md` summaries — similar to what Obsidian Mind's `brag-spotter` does.

**How to use it:**
```bash
# Via Claude Code plugin
/plugin marketplace add zilliztech/memsearch
/plugin install memsearch
# Restart Claude Code, then just chat normally
# Recall:
/memory-recall what did we decide about the auth flow?
# Or naturally: "We discussed authentication before, what was the approach?"

# Check memory is working:
ls .memsearch/memory/
```

**Failure modes / limitations:** First-time setup downloads ~558MB (ONNX model) — on a slow connection this blocks the first session. The `user_profile` background task is disabled by default and needs explicit `memsearch config set` to enable — the README buries this. Memory is stored per-workspace by default; cross-project search requires configuring a shared Milvus URI. The Stop hook fires after every session which adds overhead — if you're running many short sessions, the daily logs accumulate fast. The Zilliz Cloud integration requires their free tier account but doesn't need it for local-only use.

**Verdict:** Install and let it run silently — automatic capture with no manual step is the key advantage over CPR, and the ONNX local embedding means no external API dependency for the memory layer.

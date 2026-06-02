---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - agents
  - automation
source_url: https://github.com/ruvnet/ruflo
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Ruflo (formerly claude-flow)

**What it is:** A multi-agent orchestration framework that wraps Claude Code with a routing layer, swarm coordination, 60+ specialized agents, and a self-learning memory system — installed as `npx ruflo@latest` or via a bash script.

**What it actually does:** Ruflo sits between you and Claude Code via MCP. When you run a command, it routes through a Q-Learning router and a Mixture-of-Experts layer before dispatching to one of 60+ specialized agents (coder, tester, reviewer, architect, security, etc.) that can spin sub-workers and coordinate via mesh or hierarchical swarm topologies. The "RuVector" layer claims sub-millisecond HNSW vector search, elastic weight consolidation (no catastrophic forgetting), and 9 RL algorithms for adaptive routing. The WASM/Rust WASM kernel powers the policy engine. Underneath, it's the `claude-flow` project renamed after 5,800+ commits.

**Why it matters for this vault/workflow:** Ruflo is the most ambitious attempt at turning Claude Code into a self-improving multi-agent system. The relevant parts for BOOM/UROP workflows are the parallel agent swarms (multiple agents working different parts of a problem simultaneously) and the learning loop (successful patterns get remembered and reused). The MCP integration means it can run inside an existing Claude Code session.

**How to use it:**
```bash
# Quick start
npx ruflo@latest init --wizard

# Or one-liner
curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/claude-flow@main/scripts/install.sh | bash

# Check intelligence hooks
npx ruflo@latest hooks intelligence --status
```

**Failure modes / limitations:** The marketing-to-reality gap here is potentially large. Claims of "HNSW 150x-12,500x faster" and "9 RL algorithms" in a CLI tool should be verified — these could be aspirational or require specific conditions. The rebranding from claude-flow to ruflo and the "alpha is over, this is v3.5" framing suggests ongoing churn. The architecture diagram is impressive but doesn't clarify what actually runs vs. what is planned. Start with a minimal `npx ruflo init` and inspect what files it creates before trusting the full feature set.

**Verdict:** Test the MCP integration on a non-critical project — if the routing layer genuinely improves task distribution it's worth running alongside Claude Code; skip if it just adds latency.

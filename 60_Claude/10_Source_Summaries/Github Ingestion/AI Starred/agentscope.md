---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ai
  - agents
  - python
source_url: https://github.com/agentscope-ai/agentscope
notes:
  - "[[40_Resources/CS/Repos]]"
---
# AgentScope

**GitHub:** [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | **Stars:** 27.2k | **Updated:** Jun 26 2026 (v2.0.2, active)

## What it is
Production-ready Python agent framework (v2.0, Apache 2.0) from Alibaba. Focuses on observable, understandable agents rather than constraining them with opinionated orchestration. Five core primitives:

- **Event System** — unified event bus for frontend updates and human-in-the-loop
- **Permission System** — fine-grained, configurable control over which tools agents can call
- **Multi-tenancy & Multi-session** — production-grade serving with tenant/session isolation
- **Workspace/Sandbox** — run tools and code isolated (local, Docker, or E2B)
- **Middleware System** — composable hooks to extend the agent's reasoning-acting loop

Ships with Agent Team support (leader spawns workers), task planning, and background task offloading (long tool calls move off the main loop and wake the agent when done).

## How Anant uses it
Compare against TradingAgents architecture when designing the multi-agent trading system. AgentScope's permission system and sandbox isolation are directly applicable to financial agents where you don't want a buggy tool call destroying live positions. The Agent Team pattern (one leader spawning specialized workers) mirrors the TradingAgents bull/bear/researcher pattern.

The `examples/agent_service` + `examples/web_ui` combo gives a working multi-agent service with a web UI — useful as a reference implementation before building a custom one.

## How to install / run it (Windows)
Requires Python 3.11+.

```bash
pip install agentscope
# or with uv
uv pip install agentscope

# To run the full agent service demo:
git clone https://github.com/agentscope-ai/agentscope.git
cd agentscope/examples/agent_service
python main.py   # start backend

# separate terminal:
cd agentscope/examples/web_ui
pnpm install && pnpm dev
```

Primary model provider is DashScope (Alibaba's Qwen models). OpenAI-compatible endpoints also supported.

## Caveats / current state
Very active (365 commits, v2.0.2 Jun 2026). Apache 2.0, so usable in any project. Alibaba-backed means Qwen/DashScope are first-class; other providers are supported but documentation quality varies. Python 3.11 requirement rules out older environments. The research paper (AgentScope 1.0, 2508.16279) predates v2.0 — the framework design has changed significantly since the paper.

**Verdict: yes** — reference implementation when designing multi-agent systems. Event/permission/sandbox primitives are worth understanding before building custom agent orchestration.

## Connects to
- [[40_Resources/CS/Repos]]

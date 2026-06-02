---
type: input
status: seed
created: 2026-05-28
tags:
  - github
  - claude
source_url: https://github.com/langgenius/dify
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Dify

**What it is:** A self-hosted or cloud LLM app development platform with a visual workflow canvas, RAG pipelines, agent capabilities, prompt IDE, and observability — think "LLM middleware" that abstracts over 100+ model providers.

**Why it's here:** Production-grade infrastructure for building LLM-powered applications; the visual workflow builder lets non-engineers construct complex multi-step AI pipelines.

**Why it's not a priority:** Dify is a full platform deployment (Docker Compose, 2+ cores, 4GB RAM minimum) aimed at teams building LLM applications for end users. Anant's current context is solo agentic work with Claude Code, not building LLM apps for external users. The Claude Code + Jarvis + MCP stack already handles the relevant workflows. Dify would only be relevant if building a product that needs to serve AI capabilities to other people via an API or web UI.

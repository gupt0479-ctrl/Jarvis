---
type: input
status: sprout
created: 2026-06-21
updated: 2026-06-21
tags:
  - summary
  - github
notes:
  - "[[40_Resources/CS/Repos]]"
input_kind: github
track: ai
source_url: https://github.com/aaif-goose/goose
---
# goose

**Repo:** `https://github.com/aaif-goose/goose`
**Stars:** 49,921 | **Forks:** 5,296 | **Language:** Rust | **License:** Apache 2.0 | **Last push:** 2026-06-20 (actively maintained)

> [!NOTE]
> **Ownership changed since this repo was first starred.** Goose moved from `block/goose` to the **Agentic AI Foundation (AAIF)** at the Linux Foundation — now governed at `aaif-goose/goose`. `gh api repos/block/goose` still resolves (redirects) to the new name, but any vault note or bookmark using the old `block/goose` path should be updated.

## What It Is

A general-purpose, native AI agent — desktop app, CLI, and API — built in Rust. Not code-specific: usable for research, writing, automation, and data analysis, not just coding tasks.

## Core Capabilities

- Native desktop app (macOS, Linux, Windows), full terminal CLI, and an embeddable API
- Works with 15+ model providers (Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock, etc.) — supports both API keys and existing Claude/ChatGPT/Gemini subscriptions via ACP
- Connects to 70+ extensions through the open MCP standard
- Supports "custom distributions" — build your own goose variant with preconfigured providers, extensions, and branding

## Why It Matters

ACP + MCP native means goose can sit alongside Claude Code on the same MCP server pool and hand off tasks rather than duplicating tool config. Its autonomy model (install/execute/edit/test without staying in the loop) is the meaningful contrast with Claude Code's interactive default.

## Use Cases for Jarvis

- Run mechanical, well-defined tasks autonomously (e.g. "add a test for this function") while staying in an interactive Claude Code session for everything else.
- Cross-check: since it already reads MCP servers, it can reuse this vault's existing MCP config rather than needing separate setup.

## Tradeoffs

- Now a Linux Foundation project rather than a single-vendor (Block) product — governance model has changed; check the new `GOVERNANCE.md` before assuming the old support/release cadence holds.
- Autonomy is the selling point and the risk: less suited to tasks where you want to review each step before it happens.

## Related

- [[40_Resources/CS/Repos]] (AI section)
- [[LLM Council (github)]] — a different kind of multi-agent pattern (peer-review/debate vs. autonomous execution)

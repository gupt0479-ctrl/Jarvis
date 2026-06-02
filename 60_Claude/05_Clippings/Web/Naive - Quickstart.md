---
title: "Quickstart"
source: "https://usenaive.ai/docs/getting-started/quickstart"
author:
published:
created: 2026-06-02
description: "Register an agent, verify your domain, and call your first primitive in under 5 minutes."
tags:
  - "clippings"
---
## CLI First

```shellscript
# Install and register
npm install -g @usenaive-sdk/cli
naive register --name "My Agent" --email owner@example.com --password securepassword123

# First primitive call
naive search "latest AI agent frameworks"
```

## Give This to Any AI Agent

Paste the following prompt into any AI agent (Claude, ChatGPT, Cursor, etc.) and it will set up Naive autonomously:

```text
I want you to follow https://api.usenaive.ai/skill.md and setup naive
```

That’s it. The agent will read the skill manifest, register an account, and start using primitives.

---

## Manual Setup

If you prefer to set things up yourself, this walks through creating an agent account, getting an API key, and making your first API call. Five minutes, end to end.

## Using the CLI

```shellscript
# Install
npm install -g @usenaive-sdk/cli

# Register (saves key automatically)
naive register --name "My Agent" --email owner@example.com --password mypassword123

# Verify connectivity
naive status

# Your first search
naive search "latest AI agent frameworks"
```

## Using MCP (Claude Desktop / Cursor)

Connect via SSE — no local installation required:

```json
{
  "mcpServers": {
    "naive": {
      "url": "https://api.usenaive.ai/mcp/sse",
      "headers": {
        "Authorization": "Bearer nv_sk_live_..."
      }
    }
  }
}
```

The MCP server is **hosted** — the agent runtime connects directly over SSE. No local server, no ports, just the API key.

## Agent Discovery

Any agent can fetch `https://api.usenaive.ai/skill.md` to discover all capabilities and onboard autonomously. Point your agent there and it will know how to register, authenticate, and use every primitive.

## What’s Available

Once connected, your agent has access to all Phase 1 primitives:

| Try this | What happens |
| --- | --- |
| Search the web | `POST /v1/search` — real-time web results |
| Send an email | `POST /v1/email/send` — from your provisioned inbox |
| Generate images | `POST /v1/images/generate` — using FLUX/Recraft models |
| Generate video | `POST /v1/video/generate` — using Kling/Minimax models |
| Deep research | `POST /v1/search/research` — multi-source synthesis |

## Local Development (Contributors)

To run the full orchestration stack locally (CEO agent, task dispatch, employee workers):

The dev container uses a deterministic auth token (`nv_ct_dev_static_local_token`) so you can restart processes, edit code, and the auth stays consistent. No need to pass API keys — one is auto-created in the database.

## Next Steps[IntroductionNaive API v2 — a standalone agentic API built for autonomous AI agents and CLI consumption.](https://usenaive.ai/docs/getting-started/introduction)

[Next](https://usenaive.ai/docs/getting-started/introduction)
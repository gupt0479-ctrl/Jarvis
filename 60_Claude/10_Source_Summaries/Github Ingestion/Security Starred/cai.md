---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - cybersecurity
source_url: https://github.com/aliasrobotics/cai
notes:
  - "[[40_Resources/CS/Repos]]"
---
# CAI (Cybersecurity AI)

**GitHub:** [aliasrobotics/cai](https://github.com/aliasrobotics/cai) | **Stars:** 9.2k | **Updated:** June 2026

## What it is
A Python agent framework that wraps 300+ LLM backends (OpenAI, Anthropic, DeepSeek, Ollama, etc.) with built-in pentesting tools — recon, exploitation, privilege escalation — so you can wire up multi-agent pipelines that autonomously work through CTF challenges and bug bounty targets.

## How Anant uses it
Run it against PortSwigger Web Security Academy labs to learn web exploitation systematically: `CAI_LICENSE_OFF=1 CAI_MODEL=claude-sonnet-4-5 cai` launches an interactive session where you describe the target and the agent calls tools (nmap, curl, sqlmap wrappers) to enumerate and exploit. More focused than PentestGPT — it's a framework for building agents, not a single assistant. Good for the trading project: spin up a CAI agent with `ANTHROPIC_API_KEY` to scan the API surface before launching anything public-facing.

## How to install / run it (Windows)
Windows is natively supported (Windows badge in repo).

```bash
pip install cai-framework

# Run without Alias Robotics license (use any other provider)
set CAI_LICENSE_OFF=1
set CAI_MODEL=claude-sonnet-4-5
set ANTHROPIC_API_KEY=sk-ant-...
cai
```

Copy `.env.example` to `.env` and set keys. The `alias1` model requires a paid Alias Robotics key (€350/month Pro); all other providers work free with `CAI_LICENSE_OFF=1`.

## Caveats / current state
Actively maintained — v1.1.5 released Jun 5, 2026, 1,077 commits. The repo ships two license files: `LICENSE` (custom Alias Robotics) and `LICENSE-MIT`. Community edition is explicitly "free for research"; verify `LICENSE` before using in any commercial product. The DISCLAIMER explicitly prohibits unauthorized system tampering — use only against systems you own or have written permission to test. CAI collects usage telemetry by default (opt-out in `.env`).

## Connects to
[[40_Resources/CS/Repos]]

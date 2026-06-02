---
type: input
status: sprout
created: 2026-05-29
tags:
  - github
  - browser-automation
  - ai-agent
  - python
notes:
  - "[[40_Resources/CS/Repos]]"
---
# browser-use

**Repo:** https://github.com/browser-use/browser-use
**Stars:** 96,104 | **Language:** Python | **License:** MIT

## What It Is

The standard Python library for making websites accessible to AI agents. Uses Playwright under the hood. When an agent needs to interact with a browser — fill forms, click buttons, extract data — this is the go-to tool.

## Core Capabilities

- Playwright-backed browser automation for LLMs
- Python API: `agent.run("task description")`
- Works with any LLM that has tool use
- Handles dynamic JS-rendered pages

## Why It Matters

When you need a coding agent to interact with the web — submit a form, navigate an app, extract from a JS-rendered page — browser-use is the layer that bridges LLM reasoning to browser actions. More reliable than raw Playwright scripting because it handles the perception-action loop.

## Use Cases for Jarvis

- Automating web research workflows
- Building agents that interact with web UIs (not just APIs)
- Any pipeline where data isn't available via API

## Tradeoffs

- Python only (not TypeScript-native)
- Playwright dependency = heavier setup
- Nondeterministic by nature (web UIs change)

## Related

- [[40_Resources/CS/Repos]] (AI section)
- [[Scrapling]] — for scraping without full browser automation

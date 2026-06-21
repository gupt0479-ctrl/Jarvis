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
track: systems
source_url: https://github.com/Zie619/n8n-workflows
---
# n8n-workflows

**Repo:** `https://github.com/Zie619/n8n-workflows`
**Stars:** 55,284 | **Forks:** 7,329 | **Language:** Python (tooling around the workflow JSON files) | **License:** MIT | **Last push:** 2026-05-31

## What It Is

A scraped collection of 4,343+ n8n automation workflow JSON files (365+ integrations) pulled from the n8n community site and elsewhere — not the n8n platform itself, just importable workflow definitions plus a browsable index.

> [!NOTE]
> The current README leads with a prominent third-party sponsored banner for **AI-BOM** (a separate tool by Trusera that scans n8n workflows for hardcoded API keys, unauthenticated AI agents, and MCP clients) — that's an ad insert in the README, not part of this repo's own content. Worth knowing about independently if any of these workflows get imported and run, since the claim is that scanning found real hardcoded credentials in this exact workflow set.

## Core Capabilities

- 4,343+ pre-built workflows, browsable online before importing anything
- Covers 365+ service integrations
- Workflows are plain JSON — import directly into a running n8n instance

## Why It Matters

Jarvis's web→clipping→vault ingestion pipeline is currently fully manual. This is a library to search rather than a tool to install: before building any automation by hand (web scrape → vault note, GitHub→Obsidian sync, email digest → note), check here first for an existing workflow to import and adapt instead of writing one from scratch.

## Use Cases for Jarvis

- Search this collection for "Obsidian," "GitHub," "webhook," or "RSS" before hand-building any vault-ingestion automation.
- Requires an actual n8n instance running (self-hosted or cloud) to import and execute any workflow — this repo alone is just the JSON definitions.

## Tradeoffs

- Per the README's own security note (via the AI-BOM ad): workflows in this exact set have been found with hardcoded API keys and unauthenticated AI agent nodes — audit any workflow before importing, don't trust-and-run.
- A scraped collection, not officially maintained by n8n — quality and currency vary workflow to workflow.

## Related

- [[40_Resources/CS/Repos]] (Building section)

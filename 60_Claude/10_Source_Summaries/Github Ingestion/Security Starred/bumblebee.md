---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - cybersecurity
source_url: https://github.com/perplexityai/bumblebee
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Bumblebee

**GitHub:** [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | **Stars:** 4.6k | **Updated:** June 2026

## What it is
A read-only Go binary (zero non-stdlib dependencies) that walks a developer machine's on-disk package metadata — lockfiles, `node_modules`, dist-info, VS Code extension manifests, MCP config files — and outputs structured NDJSON records. When given an exposure catalog (`--exposure-catalog catalog.json`), it emits `finding` records for exact `(ecosystem, package, version)` matches against known-malicious entries. It makes no network calls and runs no package managers. Covers npm/pnpm/yarn/bun, PyPI, Go modules, RubyGems, Composer, Homebrew, VS Code/Cursor/Windsurf extensions, Chromium/Firefox browser extensions, MCP server configs, and Claude Code agent skills.

## How Anant uses it
Before adding any new VS Code extension or MCP server, run:

```bash
bumblebee scan --profile baseline \
  --ecosystem editor-extension,mcp,agent-skill \
  --exposure-catalog ./threat_intel/ \
  --findings-only
```

This checks currently installed extensions and all MCP configs (`claude_desktop_config.json`, `~/.claude.json`) against Perplexity's curated threat intel catalogs in `threat_intel/`. If a finding emits, it names the exact package, version, and source file. Also useful after pulling someone else's project: run `--profile project --root ~/code/trading` to check npm/PyPI deps in that workspace against the supply-chain compromise catalog.

## How to install / run it (Windows)
**Linux/macOS only — not supported on Windows natively.** Use WSL2.

```bash
# In WSL2 (requires Go 1.25+)
go install github.com/perplexityai/bumblebee/cmd/bumblebee@latest

# Verify install
bumblebee selftest
# selftest OK (2 findings in 1ms)

# Baseline scan of global packages + extensions
bumblebee scan --profile baseline > inventory.ndjson

# Check specific npm packages in a project against threat catalogs
git clone https://github.com/perplexityai/bumblebee
bumblebee scan --profile deep \
  --root ~/code/trading \
  --exposure-catalog ./bumblebee/threat_intel/ \
  --findings-only
```

## Caveats / current state
Very actively maintained — v0.1.2 released Jun 18, 2026, latest commit Jun 25, 2026. Apache-2.0 license, no commercial restrictions. This is purely a read-only inventory and matching tool — it does not block installs, remove packages, or make any changes. It only tells you whether a specific version of a known-malicious package is present on disk. The threat_intel catalogs cover known supply-chain campaigns but are not exhaustive; a clean scan doesn't mean the packages are safe, only that they don't match current catalog entries. The `mcp` ecosystem scanner reads `env` blocks from MCP configs to find server names but explicitly does not emit credential values.

## Connects to
[[40_Resources/CS/Repos]]

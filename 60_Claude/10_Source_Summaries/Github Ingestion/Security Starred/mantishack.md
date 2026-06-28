---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - cybersecurity
source_url: https://github.com/deonmenezes/mantishack
notes:
  - "[[40_Resources/CS/Repos]]"
---
# MantisHack

**GitHub:** [deonmenezes/mantishack](https://github.com/deonmenezes/mantishack) | **Stars:** 343 | **Updated:** June 2026

## What it is
A Claude Code slash-command framework for agentic penetration testing, built on top of RAPTOR (github.com/gadievron/raptor, MIT). Renames RAPTOR's 21 commands to `/mantis-*` namespace and layers on a live-fire active-tampering engine that mutates every (endpoint, input) pair through injection, type-juggling, boundary, verb tampering, IDOR sweeps, and prompt-injection probes against a live target.

## How Anant uses it
Open the trading project's repo in Claude Code and run `/mantis-scan` to enumerate all API endpoints, then `/mantis-auth-audit --policy-groups auth,logging` to check whether authentication is implemented correctly and whether failed attempts are logged. The scanner produces concrete findings only when a behavioral oracle fires against a recorded baseline — so you get `auth_bypass: JWT alg:none accepted` rather than a generic "potential issue." Run `/mantis-agentic` for the fully autonomous loop that iterates until convergence (K dry rounds with zero untested pairs). Use only against your own projects — the framework has a scope-lock and authorization gate that asks before any destructive action.

## How to install / run it (Windows)
Requires Python 3.10+. Clone and open in Claude Code — all functionality runs through slash commands, no separate install needed beyond having Claude Code.

```bash
git clone https://github.com/deonmenezes/mantishack
cd mantishack
# Open in Claude Code, then use /mantis-scan, /mantis-agentic, /mantis-auth-audit
```

WSL recommended on Windows (RAPTOR scripts are bash-heavy under `libexec/`).

## Caveats / current state
Very new — 11 commits total, May-June 2026. The repo's history shows significant churn: it was previously a Rust daemon, got fully replaced with a RAPTOR rebrand, then docs were corrected multiple times for claims that didn't match the code. The slash commands work (`/mantis-*` namespace), but some documentation still contains stale flags from RAPTOR that don't apply. License is MIT (RAPTOR upstream, preserved byte-identical). The "inspired by" vs "fork" framing changed mid-June, suggesting ongoing attribution dispute cleanup.

## Connects to
[[40_Resources/CS/Repos]]

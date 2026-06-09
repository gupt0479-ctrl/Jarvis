---
type: project
status: sprout
created: 2026-06-09
tags:
  - project
  - claude-setup
  - portfolio
  - moc
notes:
  - "[[01 - Config Pack (copy-paste ready)]]"
  - "[[02 - Deploy Security Checklist]]"
next: "[[01 - Config Pack (copy-paste ready)]]"
---

# Portfolio AI Setup — Index & Integration Guide

This kit is the readymade AI setup for the portfolio. It replaces the scattered hackathon attempt (`CLAUDE.md`, `cosmic-frontend.mdc`, `three-artist.md`) with a small, working set you copy into the repo once. Goal: when you sit down to build, the agent already knows the stack, the rules, the tools, and the security gates — nothing to re-derive.

## What was wrong before

You had config *files* but no *system*. The pieces were untested, split across Cursor (`.mdc`) and Claude Code, and there was no contract telling the agent how this specific stack behaves (Next 16 awaited params, server-vs-client, pnpm-only, Biome/Vitest gates). So every session re-guessed. The fix isn't more files — it's one conventions file plus a few focused subagents and automatic gates.

## The two-machine rule (this is the core confusion)

- Your **portfolio repo lives in WSL** (`/home/...`). Do the actual coding there with **Claude Code in the terminal** (`cd repo` → `claude`). WSL repos are out of scope for Cowork's file tools.
- This **vault is the canonical home for the templates**. Edit them here in Cowork; copy the blocks into the repo. When you change a convention, change it here first, then sync.

So: Cowork/this vault = the playbook. Claude Code in WSL = the executor.

## Files in this kit

| File | What it is |
|---|---|
| [[01 - Config Pack (copy-paste ready)]] | The `AGENTS.md`, 4 subagents, hooks, and `.mcp.json` to drop into the repo |
| [[02 - Deploy Security Checklist]] | Headers, HSTS for `.dev`, CSP, Clerk, Sanity, secrets, pre-deploy ritual |

## How to install (one time, ~15 min)

1. In the repo root, create `AGENTS.md` from the config pack. Make `CLAUDE.md` a one-liner: `See AGENTS.md`.
2. Create `.claude/agents/` and add the four subagent files.
3. Add `.claude/settings.json` with the hooks (auto Biome on edit, Vitest on stop).
4. Add `.mcp.json` with the five servers. Connect the new ones (below).
5. Add the security headers to `next.config.ts`.
6. Commit. From now on every Claude Code session in this repo loads the whole setup automatically.

## Connectors to add

You already have **Context7**, **Vercel**, and **GitHub** MCPs connected in Claude Desktop. For the portfolio, add two more and the Sanity plugin — cards are in the chat where this kit was built:

- **Sanity MCP** (`mcp.sanity.io`) + the **Sanity plugin** (GROQ builder, schema design, Portable Text skills).
- **Clerk MCP** (`mcp.clerk.com/mcp`) for correct, version-matched auth SDK snippets.

In the WSL repo these come from `.mcp.json`; in Claude Desktop they're connectors you enable once.

## How you actually use it day to day

- **Build a feature:** ask the main agent; it delegates UI to `frontend-builder`. Context7 keeps API calls version-correct.
- **Before pushing:** run `security-reviewer` then `/security-review`. Walk the [[02 - Deploy Security Checklist]].
- **Content work:** `sanity-schema` agent + Sanity MCP for schemas and GROQ.
- **Deploy:** Vercel MCP to ship and read build/runtime logs without leaving the session.
- **Tests:** `test-runner` keeps Vitest green; the Stop hook nags you if it isn't.

## Why this makes the vault a "brain"

The vault stops being a dump the moment a resource has a *trigger* — a place it gets pulled in automatically. This kit is the pattern: the repo's `AGENTS.md` is the trigger that pulls the right conventions into every coding session. Repeat the pattern (one kit per project, canonical here, synced to the repo) and the scattered-resources problem dissolves: you stop hunting, because the setup arrives with the work.

## Status

Done: kit drafted and filed. Needs user: copy blocks into the repo, connect Sanity + Clerk MCPs, run CSP report-only for a day before enforcing.

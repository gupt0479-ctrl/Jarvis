---
type: evergreen
status: sprout
created: 2026-07-05
tags:
  - implementation
  - ingestion
  - mcp
  - agent-readiness
notes:
  - "[[60_Claude/10_Source_Summaries/Web Ingestion/The Agent-Ready Roadmap (web)]]"
  - "[[60_Claude/10_Source_Summaries/Web Ingestion/Naive — Agent Primitives API (web)]]"
  - "[[60_Claude/10_Source_Summaries/Web Ingestion/NextWork — Automate Your AI Second Brain (web)]]"
  - "[[PDF's Ingestion Implementation]]"
  - "[[GitHub Ingestion Implementation]]"
---

# Web Ingestion Implementation

Actionable items from web sources on agent-ready infrastructure, portfolio differentiation, and MCP adoption.

---

## Agent-Ready Infrastructure (AEO + MCP)

**Source:** [[60_Claude/10_Source_Summaries/Web Ingestion/The Agent-Ready Roadmap (web)]]

### Market Context
- Agents are now 51% of internet traffic (Imperva 2025); agentic traffic jumped 1,300% Jan→Aug 2025.
- An agent customer (vs. human) wants: structured capability, permission, and trust—not persuasion.
- Agents arrive ready to act but hit human-built walls (87% reach product pages; only 2.2% reach checkout).

### Implementation for Jarvis & Portfolio
1. **Make Portfolio site agent-readable** — This is a concrete, low-effort portfolio differentiator for internship applications.
   - Phase 1: Run AEO audit — ask ChatGPT/Perplexity "what do you know about [your site]?"
   - Phase 2: Optimize one page for AI readability (clear answers, structured content).
   - Phase 3: Add agent-callable actions (use existing MCP infrastructure).

2. **AEO vs. SEO pivot** — Optimize to be the answer AI cites/recommends (Perplexity, ChatGPT overviews), not for human search rank.
   - Google search volume −25% by 2026 (Gartner); AI Overviews cut publisher traffic 25% (Digiday).
   - McKinsey projects $750B US revenue through AI search by 2028 — the gap IS the opportunity.

3. **MCP as enabling standard** — "Universal adapter giving an AI a set of buttons it's allowed to push."
   - Jarvis already has MCP infrastructure; portfolio site should expose agent-callable actions via MCP endpoint.
   - Design: contact form → agent-invocable action; docs → executable (agent does the follow-up); pricing → parseable structure.

---

## Agent Primitives & Integration

**Source:** [[60_Claude/10_Source_Summaries/Web Ingestion/Naive — Agent Primitives API (web)]]

- **Naive** — Self-installing skill manifest (agents read and install capabilities autonomously).
  - Pattern: conceptually adjacent to MCP but lower-priority for Jarvis (existing MCP servers already provide primitives).
  - Anti-drift: if explored, is weekly-slot work only.

---

## Validation: Obsidian-as-OS Learning

**Source:** [[60_Claude/10_Source_Summaries/Web Ingestion/NextWork — Automate Your AI Second Brain (web)]]

- **NextWork platform** — Project-based learning on "Obsidian vault as daily OS with Claude Code" (Jarvis thesis verbatim).
  - Verdict: Jarvis is ahead of intro curriculum; skip unless external audit needed for missing daily-loop mechanic.

---

## Decisions to Make

1. **Is "agent-readable Portfolio" a real differentiator for internships, or gimmick?**
2. **Does "agent-native version of X" framing point at any Bangalore-week project?**
3. **Should Naive be explored as a primitives layer, or is existing MCP roster sufficient?**

---

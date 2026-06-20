---
type: input
status: sprout
created: 2026-06-20
updated: 2026-06-20
tags:
  - summary
notes:
  - "[[40_Resources/CS/AI/Toolkit/Github Skills]]"
input_kind: web
track: ai
source_note: "[[Claude Council.md]]"
source_url: https://growthxclub.notion.site/Claude-Council-3633578dc3f080d7b787e72f6e19e871
---
# Claude Council — Path A Prompt — Summary

**Source:** `https://growthxclub.notion.site/Claude-Council-3633578dc3f080d7b787e72f6e19e871`
**Ingested:** 2026-06-20
**Pages:** N/A — single Notion page

## Source

A **GrowthX Club** Notion page packaging "The Council" (also called LLM Council) as a two-path install: a copy-paste prompt for any chat interface, or the full Claude Code skill. It is the discovery record for [[LLM Council (github)]] — the page that surfaces the tool, not the tool itself.

## Key Claims

- **Three people, three versions, one name:** **Andrej Karpathy** built the original multi-model concept; **Ole Lehmann** rebuilt it to run as 5 Claude sub-agents in one chat; **Jason Flynn** adapted it into a single copy-paste prompt with no sub-agents at all. The page calls all three "the Council" without distinguishing the architectures.
- **Path A trades real anonymization for zero install:** running all 5 advisors sequentially in one context, instead of in parallel isolated sub-agents, means the page itself admits "you lose true anonymisation and you lose the workspace context scan."
- **The council is a forcing function against validation-seeking:** the page states plainly it should not be used when "you've already decided" — "the council will tell you things you don't want to hear. That's the point."
- **Specificity changes advisor quality:** the page's own example contrasts a vague prompt ("Should I launch a course?") against a specific one (with price, audience, and niche named), claiming the specific version gets "surgical" advice instead of generic advice.

## Full Content

### Install The Council — the Claude skill that makes 5 AIs argue with you
Framing: turn an important decision into a 5-agent debate refereed by a chairman, with two install paths — start at Path A, "upgrade" to Path B when it's used often enough to justify the install.

### What you're actually installing
The system frames the question with context, spawns 5 advisors with different thinking styles, anonymizes their answers for peer review, then has a chairman read the full debate and give one verdict: where the council agreed, where it clashed, what blind spots peer review caught, and the one thing to do next.

### Quick: which path is for you?
| You're using... | Go to... |
| --- | --- |
| Claude.ai web (chat) or any AI chat | Path A — prompt-only |
| Claude Code or Claude Cowork | Path B — full skill install |

### Path A — prompt-only version (any chat, no install)
The full copy-paste prompt defines an "LLM Council Facilitator" role with five fixed variables: (1) a neutrally framed question with context and stakes; (2) the five advisors — Contrarian, First Principles Thinker, Expansionist, Outsider, Executor — each given a one-line behavioral description and a 150-300 word, no-hedging response limit; (3) anonymized peer review where each advisor-as-reviewer answers three fixed questions (strongest response, biggest blind spot, what all five missed) in under 200 words; (4) a chairman's verdict in a fixed five-section structure (Agrees / Clashes / Blind Spots / Recommendation / One Thing to Do First); (5) an explicit execution order — ask one clarifying question if the prompt is too vague, then run framing → 5 responses → anonymize → 5 reviews → reveal mapping → chairman verdict, in that order, every time.

### Path B — install the full Council skill (Claude Code / Cowork)
For repeat use: paste a one-line prompt telling Claude to fetch `SKILL.md` from `aiwithremy/claude-skills-llm-council` and install it. The page claims the installed version runs 5 **parallel** sub-agents (vs. Path A's sequential single-context run), true anonymization between rounds, and produces "an HTML report saved to your workspace" in about 4 minutes.

> [!WARNING]
> This HTML-report claim does not match the actual `SKILL.md` — see [[LLM Council (github)]] § Open Questions. The live skill explicitly forbids generating files and mandates chat-only output.

### When to use the Council (either path)
Use for high-stakes decisions with genuine uncertainty — pricing, hiring, launches, pivots, big partnerships. Don't use for factual lookups, pure creation tasks ("write me an email"), or validation-seeking on a decision already made.

### Pro tips
==Specificity changes advisor quality — a vague prompt gets generic advice, a specific one (real price, real audience, real niche named) gets advice the page calls "surgical."== Read the peer review, not just the verdict — the page claims the most valuable signal is often reviewer question 3 ("what did all five miss"), since that's where blind spots no single advisor caught get surfaced. Graduate from Path A to Path B only once councils are run weekly enough to justify the install.

### Credits
Original concept: **Andrej Karpathy** (`karpathy/llm-council`, multi-model). Prompt adaptation: **Jason Flynn** (AI Field Notes / Substack). Easy-install skill repo: **aiwithremy/claude-skills-llm-council**.

## Why It Matters

This page is the human-readable discovery layer; [[LLM Council (github)]] is the verified artifact. Keeping them as two linked notes instead of one merged note is itself the answer to "how do clippings relate to the vault" for tool-discovery content: the landing page captures *why and where you found it* (lineage, framing, the contrast between paths), the repo note captures *what it actually does* — and the discrepancy between the two (the HTML-report claim) only surfaces because both got ingested instead of trusting one summary.

## Links Into The Vault

- [[40_Resources/CS/AI/Toolkit/Github Skills]] — confirmed; existing list of Claude Code skill repos this entry belongs alongside.
- [[LLM Council (github)]] — the verified-against-source companion note.
- [[Claude Council.md]] — the raw clip this note replaces.

## Open Questions

- [ ] Path A explicitly trades away "true anonymisation" for zero-install convenience — is sequential-single-context council output meaningfully weaker for genuinely high-stakes calls, or is the framework itself (5 fixed angles + peer review) most of the value regardless of architecture?
- [ ] Jason Flynn's prompt adaptation (Path A) and Ole Lehmann's skill (Path B) both claim lineage from Karpathy's original — worth reading `karpathy/llm-council`'s actual README directly rather than trusting this page's framing of it (not yet done in this pass).

## Flashcards

#cards/ai
Per the page's own admission, what does Path A (prompt-only, sequential, single context) **lose** compared to Path B (parallel sub-agents)?::True anonymization between advisors and the workspace-context scan — Path A runs all 5 advisors sequentially in one context instead of in isolated parallel sub-agents.
What is the stated **purpose** of the council's "don't use it for validation" rule?::If a decision is already made, the council is being used to seek agreement rather than pressure-test the decision — the page states the council will surface unwanted input, "that's the point," so using it for validation wastes the framework's actual value.
**Contrast:** how does prompt specificity change the council's output quality, per the page's own example?::A vague prompt ("Should I launch a course?") gets generic advice; a specific prompt naming real price, audience, and niche gets advice the page calls "surgical" — context given to advisors directly determines advice quality.

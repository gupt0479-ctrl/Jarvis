---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[Claude OS]]"
source_url: https://zachdoesai.com/guides/agent-ready
source_note: "[[The Agent-Ready Roadmap.md]]"
input_kind: web
track: ai
---
# The Agent-Ready Roadmap — Summary
**Source:** `60_Claude/05_Clippings/Web/The Agent-Ready Roadmap.md` (zachdoesai.com)
**Ingested:** 2026-07-04
**Pages:** web guide
## Source
A four-phase strategy map by **Zach (@zachdoesai)**, an AI-native marketer, arguing that the internet's customer is shifting from humans to AI agents, and laying out AEO, MCP, and agent-payment rails as the places to get ahead — built on Greg Isenberg's "$100B market: selling to AI agents" thesis.
## Key Claims
- ==The customer isn't a person anymore — it's the AI working on a person's behalf==, and the reframe that runs the whole guide: **a human customer wants persuasion; an agent customer wants structured capability, permission, and trust**
- If an agent can't understand or act on your site, you're **invisible to it, not just low-ranked**
- **Bots are already 51% of internet traffic** (Imperva 2025) — machines outnumber humans online for the first time
- **Agentic traffic jumped 1,300% Jan→Aug 2025** (HUMAN Security); AI traffic to retail is up 4,700% YoY (Adobe); 23% of Americans bought via AI in the past month (Morgan Stanley)
- Morgan Stanley projects **$190–385B in US agent-driven online spend by 2030**
- **SEO is dying, AEO is the new game**: Gartner sees search volume −25% by 2026; AI Overviews already cut publisher referral traffic 25% (Digiday); McKinsey projects $750B US revenue through AI search by 2028
- Agents spend **87% of visits on product pages but only 2.2% reach checkout** (HUMAN Security) — they arrive ready to act and hit a human-built wall
- **MCP is the enabling standard** — "a universal adapter giving an AI a set of buttons it's allowed to push," created by Anthropic, now the default
- Only **22% of businesses say they're agent-ready** (Microsoft) — that gap *is* the opportunity
## Full Content
### The One Idea That Makes This Click
==The old web was humans searching/reading/comparing/clicking/buying; the new web is agents discovering/evaluating/paying/renewing.== A slick landing page, clever headline, hero video — an agent doesn't care. It reads your data, checks whether it can *do* something (book, buy, return, schedule), confirms trust, and moves on.
### Phase 1 — Understand the New Internet
Goal: believe it's real, with numbers, so you act. The traffic/spend stats above are the evidence. *Do now:* ask ChatGPT/Perplexity to research and recommend a business in your industry, and watch how it decides — that behavior × billions is the new internet.
### Phase 2 — AEO: The New SEO
==Instead of optimizing to rank for a human, optimize to be the answer an AI cites, trusts, and recommends.== Controllable levers: clear answers to real questions, structured content, getting mentioned in the places AI trusts. *Do now:* ask ChatGPT and Perplexity "what do you know about [your business/name]?" — that's a 30-second AEO audit.
### Phase 3 — Build the Actions (MCP)
==Stop building things only humans can use; start building things an agent can invoke.== Contact form → an action the agent can call; support docs → executable support (the agent does the refund/return/reschedule); slogan page → a clear statement of what an agent can *do* with you. *Do now:* check whether the tools you use (Notion, Slack, Stripe, help desk) already have an MCP server or agent integration.
### Phase 4 — The Plumbing: Trust & Payments
==An agent buying for you needs an identity (who is it acting for?), a wallet (what can it spend, who approves?), and a receipt (what did it do?) — whoever builds that trust layer owns the agent economy.== 2025 moves: Mastercard Agent Pay, Visa Intelligent Commerce, Google AP2 (open standard, 60+ partners), OpenAI+Stripe Instant Checkout in ChatGPT. Adobe measured an 805% AI-traffic jump to retail on Black Friday 2025; Salesforce says AI influenced $3B of Black Friday sales. Names to know: **AgentMail** (YC-backed, gives agents their own inbox), **Google AP2** (open agent-payments standard).
### Where the $100B Actually Is
==The cheat code: take any popular software or service and ask "what's the agent-native version of this?"== Openings floated: making businesses agent-ready (the new "I'll do your SEO"), agent identity & permissions, agent-readable docs/pricing pages as a service, MCP servers for whole categories, agent support desks and audit trails.
### Your First Week
1. Watch Greg's video · 2. Run your AEO audit · 3. Make one page AI-readable · 4. Find the agent feature in a tool you use · 5. **Pick one lane** (AEO / MCP / payments) — depth in one beats skimming all four.
## Why It Matters
This is the business/market framing around the exact tech Anant already builds with — MCP servers, agents, Claude ([[Claude OS]]). The reframe ("agents want structured capability, permission, trust, not persuasion") is a useful lens for the Jarvis MCP work and for the Portfolio project: making a personal site *agent-readable* is a concrete, low-effort portfolio differentiator, and "build the agent-native version of X" is a startup-idea generator that fits the Bangalore flagship search. Signal caveat: this is a marketer's motivational map with a "work with me" CTA, and the stats are cherry-picked from vendor reports — take the direction seriously, the precise numbers loosely.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/Web/The Agent-Ready Roadmap.md`
- [[Claude OS]] — the MCP/agent infrastructure this frames commercially
- [[10_Areas/AI/Claude Code|Claude Code]] — MCP servers are already part of the Jarvis stack
## Open Questions
- [ ] Is "make the Portfolio site agent-readable (AEO + an MCP endpoint)" a real differentiator for internship applications, or gimmick?
- [ ] Does the "agent-native version of X" framing point at any concrete Bangalore-week project?
## Flashcards
#cards/ai
What is the core reframe of the agent-ready thesis?::A **human customer wants persuasion; an agent customer wants structured capability, permission, and trust** — the customer is now the AI acting on a person's behalf.
What is AEO and how does it differ from SEO?::**Answer Engine Optimization** — optimizing to be the answer an AI cites and recommends (in ChatGPT/Perplexity), rather than optimizing to rank for a human click on Google.
What problem does the "87% product pages / 2.2% checkout" stat reveal?::Agents **arrive ready to act but hit a human-built wall** — sites are built for humans to click through, not for agents to *invoke* actions, which is what MCP fixes.
What three things does an agent need to transact that a human never did?::An **identity** (who it acts for), a **wallet** (what it can spend, who approves), and a **receipt** (what it did) — the trust/payments layer.

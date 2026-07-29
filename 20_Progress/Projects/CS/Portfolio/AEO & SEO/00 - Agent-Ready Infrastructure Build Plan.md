---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[architecture/01-nextjs-routes]]"
  - "[[chatbot/01-api-route]]"
tags:
  - "#progress"
  - "#portfolio"
next: "Add metadata exports to each App Router route, starting with the root layout and the portfolio home page"
---
# Agent-Ready Infrastructure Build Plan
## Why This Exists
[[Web Ingestion Implementation#Agent-Ready Infrastructure (AEO + MCP) - BUILD|Web Ingestion Implementation's Agent-Ready Infrastructure section]] proposed making the portfolio site agent-readable — structured content an AI agent (ChatGPT, Perplexity, a crawler) can actually parse, versus a page built only for human eyes. [[00_Execution]] confirmed the gap is real and currently **completely empty**: [[architecture/01-nextjs-routes|the route tree]] has zero metadata exports, no `sitemap.ts`, no `robots.ts`, no OpenGraph tags anywhere in `src/app/`. This is the concrete build that closes that gap.
## Market Context (Why This Matters, Not Just "Nice to Have")
Agents are now 51% of internet traffic (Imperva 2025), up 1,300% Jan-Aug 2025. An agent customer wants structured capability and parseable content, not persuasion copy — and today's human-built pages block it: 87% of agents reach a product page, only 2.2% reach checkout. Separately, Google search volume is projected down 25% by 2026 (Gartner) as AI Overviews already cut publisher traffic 25% (Digiday) — the optimization target is shifting from human search rank (SEO) to "is this the answer an AI cites" (AEO).
## The Build, In Order
### Phase 1: Metadata API Per Route
Add Next.js's `metadata` export (or `generateMetadata()` for dynamic routes) to every route in [[architecture/01-nextjs-routes|the route tree]]:
- `src/app/layout.tsx` — site-wide defaults: title template, description, `metadataBase`.
- `src/app/(portfolio)/page.tsx` — page-specific title/description summarizing Anant's work in plain, parseable sentences (not marketing copy — an agent should be able to extract "what does this person build" directly from the meta description).
- `src/app/studio/**` — can stay minimal/noindex since it's Clerk-guarded, not public-facing content.
### Phase 2: `sitemap.ts` and `robots.ts`
- `src/app/sitemap.ts` — Next.js's built-in sitemap generator (`MetadataRoute.Sitemap`), listing the portfolio home and any public sub-routes.
- `src/app/robots.ts` — explicit crawl rules; allow the portfolio routes, disallow `/studio/*` and `/api/*` (the chat API shouldn't be indexed, it's an application endpoint, not content).
### Phase 3: OpenGraph and Twitter Card Tags
Add `openGraph` and `twitter` fields to the root layout's metadata export — image, title, description. This is what makes a shared portfolio link render as a real preview card instead of a bare URL, on any platform (LinkedIn, Discord, iMessage) an agent or human might share it through.
### Phase 4: Privacy Policy Page
The chatbot + Clerk auth stack needs one. Use `App Privacy Policy Generator` (free, open-source, static — per [[00_Execution]]'s Security clippings verdict) to produce the page directly rather than hand-writing legal boilerplate; drop `Compliance Solutions for Websites, Apps and Organizations` and `All-in-One Data Privacy Compliance Solution` (paid SaaS platforms, confirmed overkill for a solo portfolio).
### Phase 5: The AEO Audit (Only After Phases 1-4 Land)
Ask ChatGPT and Perplexity directly: "what do you know about [portfolio URL]?" Compare the answer against what Phases 1-4 actually expose. This audit is the verification step — running it before the metadata/sitemap/robots work exists just measures the current empty state, which is already confirmed empty; it only becomes a useful signal once there's something to measure.
## Follow-Up Idea, Not Yet Committed: Agent-Callable Orby
[[00_Execution]] found a second improvement while checking this gap, outside the original ingestion's scope: the portfolio already runs a live Orby chatbot ([[chatbot/01-api-route|`api/chat/route.ts`]]) that answers natural-language questions about Anant's work — exactly the kind of structured, agent-consumable Q&A content AEO wants. Today it's locked behind a client-side chat widget; an external agent or crawler can't reach it directly.
**The open question, deliberately left open:** is it worth exposing a machine-callable version of the same Q&A — an MCP endpoint, or a structured `/api/chat` mode built for programmatic callers instead of the chat UI? This is literally the "agent-callable actions via MCP" idea [[Web Ingestion Implementation#Agent-Ready Infrastructure (AEO + MCP) - BUILD|the original AEO source]] proposes, and the underlying Q&A engine ([[chatbot/02-model-router|model router]], [[chatbot/03-personas|persona system]], grounded content per [[chatbot/05-evals|the eval suite]]) already exists to point it at. Not committed — this needs a real security-model conversation first (rate limiting and origin checks exist for the chat widget; a machine-callable endpoint changes the threat model) before it becomes Phase 6.
## Evidence
- [[Web Ingestion Implementation#Agent-Ready Infrastructure (AEO + MCP) - BUILD|Agent-Ready Infrastructure (AEO + MCP)]] — the source proposal and market data
- [[architecture/01-nextjs-routes]] — the confirmed-empty route tree this plan fills in
- [[chatbot/01-api-route]] — the existing Orby endpoint the follow-up idea would extend
- [[60_Claude/05_Clippings/Web/Security/App Privacy Policy Generator]] — the tool for Phase 4
- [[00_Execution]] — the resolved verdict this note executes

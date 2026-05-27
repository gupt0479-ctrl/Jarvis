---
type: project
status: active
created: 2026-04-27
tags:
  - hackathon
  - fintech
  - portfolio
related:
  - "[[01_Summit]]"
  - "[[Opspilot]]"
  - "[[Mentor Details]]"
  - "[[Mentorship Board]]"
---
# Resq
## Elevator Pitch
CFO workspace for founders who cannot afford a finance team. Resq turns ledger facts into a 13-week cash forecast, detects the week cash breaks, and ranks the next moves: accelerate collections, defer payments, reduce expenses, or explore bridge financing. Core principle: AI advises, summarizes, researches, and prioritizes — but never touches the numbers.
## Problem
### Facts from repo
- Positioned as an autonomous SMB survival agent and fintech CFO workspace.
- Pivoted from [[Opspilot]] starting April 17, 2026.
- Focuses on cash pressure, overdue receivables, financing options, vendor/insurance cost pressure, and auditability.
- Both repo and deck emphasize deterministic financial truth with AI as advisory layer.
### The actual pain
Founders and small business owners run out of cash before they understand what is happening. Invoices are open, expenses are coming due, vendor costs are rising, and there is no finance hire to translate the situation into a decision.

The pain is not missing data. The pain is that the owner has to manually answer: How much cash do I actually have? What money is likely to arrive late? Which week becomes dangerous? What action buys the most time? Can I trust the recommendation?

A 13-week view is valuable because it gives enough time to act before the crunch arrives.
## Product Overview
Three core pillars:
1. **Cash Truth** — current cash from cleared ledger facts only.
2. **13-week forecast** — deterministic weekly cash waterfall projecting inflows, outflows, and ending balance.
3. **Action Queue** — ranked CFO-style moves based on impact, speed, risk, and confidence.
### Main user workflow
1. Connect or import financial data.
2. Compute current cash from cleared transactions.
3. Separate open receivables from actual cash.
4. Generate 13-week forecast.
5. Breakpoint detection identifies the first week below threshold.
6. Risk-driver analysis explains what is compressing cash.
7. Action ranker recommends interventions.
8. TinyFish supports external research for financing, vendor, and insurance context.
9. Every analysis/action logged into audit timeline.
### Demo flow
`cash stress → rescue queue → survival scan → financing options → vendor/insurance proof → auditable timeline`
### What makes it different
- AI deliberately kept out of forecast math.
- Forecast is deterministic and replayable.
- Built around action, not just dashboards.
- Audit trail is part of the product, not an afterthought.
## What We Built
### Completed
- Rescue Queue as primary working surface.
- Cash metric boxes: current cash position, cash collected, breakpoint week, largest risk driver.
- Deterministic cash position service.
- Collection lag computation.
- 13-week forecast engine (~350 lines pure TypeScript, three scenario modes, trailing 8-week baseline).
- Breakpoint detector.
- Risk driver analyzer.
- Action ranker with interventions (impact range, speed, risk, confidence, executable flag).
- `/api/cash/summary`, `/api/cash/analyze`, `/api/cash/forecast`, and cash action execution routes.
- Analysis overlay in Rescue UI.
- `cash_obligations` and `cash_forecast_snapshots` schema.
- AI action audit logging with SHA-256 hash chaining.
- TinyFish client: mock, misconfigured, live, and degraded behavior.
- Mock financing offers, vendor alternatives, insurance renewal fixtures.
- Stripe collections docs and support paths.
- AWS App Runner / Docker deployment documentation.
- Property and route-oriented tests for deterministic pieces.
### Partially completed or uncertain
- **Spreadsheet import** — deck says in progress; repo specs deferred it for rescue queue first.
- **Live TinyFish** — opt-in; financing is the only required live lane; vendor and insurance may remain fixture-backed.
- **Stripe** — setup exists as optional collections support; exact live status should be verified.
- **Production auth / project separation** — appears planned or recently addressed; deployment status should be verified before presenting as production-ready.
### What was real vs mocked
- **Real in repo:** deterministic cash services, forecast logic, breakpoint/risk analysis, schema, API routes, Rescue UI, audit trail, TinyFish mode handling, tests, docs.
- **Mocked or demo-safe:** TinyFish external findings in mock mode, financing offers, vendor alternatives, insurance renewal scan, fallback behavior when live services are unavailable.
- **Investor framing only:** fundraising ask, market sizing, pricing targets, public beta target, design partner target. Treat as pitch/deck framing unless independently validated.
## Tech Stack
| Layer | Tools |
|---|---|
| Frontend | Next.js 16 App Router, React 19, TypeScript, Tailwind CSS 4, custom dashboard components, lucide-react, Recharts |
| Backend | Next.js route handlers, TypeScript services, Zod schemas |
| Database | Supabase Postgres + Drizzle ORM |
| Auth | Supabase Auth / organization membership (in project separation specs) |
| AI / External | Anthropic Claude, TinyFish (mock/live/misconfigured), optional Stripe, optional Resend, optional AWS S3 |
| Deploy | Vercel and AWS-oriented docs; Dockerfile and App Runner config present |
## Architecture
### App structure
- `src/app/` — pages
- `src/app/api/` — route handlers
- `src/lib/services/` — deterministic and AI-assisted services
- `src/lib/queries/` — UI-facing read models
- `src/lib/db/schema.ts` — Drizzle table definitions
- `src/lib/tinyfish/` — TinyFish client, schemas, mock data, portal code
- `supabase/migrations/` — database migrations
- `.kiro/specs/` — implementation specs and task logs
### Data flow
1. Rescue page loads cash summary and risk-sorted queue.
2. `/api/cash/summary` computes current cash, forecast, breakpoint, largest risk driver.
3. User selects a client/case and clicks "Run AI Analysis."
4. `/api/cash/analyze` runs deterministic forecast and collection-lag logic.
5. Action ranker adds external research and recommended actions.
6. Response renders in analysis overlay.
7. Executable actions create drafts, log tasks, or mark review.
8. `ai_actions` stores the audit trail.
### Key tables
`finance_transactions`, `invoices`, `customers`, `cash_obligations`, `cash_forecast_snapshots`, `ai_actions`, `organization_memberships`, recovery-related invoice/client fields for collections
### AI boundary
AI may: summarize external findings, produce plain-English analysis, rank options, draft outreach, support TinyFish-backed research.
AI must not: invent balances, modify forecast math, own invoice totals, own ledger writes, execute high-stakes financial actions without deterministic validation.
### Key engineering decisions
- Pivot from broad [[Opspilot]] to focused fintech cash survival.
- Preserve deterministic finance backbone from OpsPilot.
- Make TinyFish mock mode mandatory for demo safety.
- Avoid broad schema renames during hackathon pressure.
- Prioritize one hero flow over feature breadth.
## What Went Well
- Product positioning became much sharper after the pivot.
- Architecture had a strong trust story: deterministic math first, AI advice second.
- 13-week forecast and breakpoint idea created a strong demo moment.
- TinyFish mock/live/degraded modes made the demo safer.
- Deck, repo docs, and technical implementation aligned around Cash Truth, forecast, and action queue.
- Task specs were unusually concrete for a hackathon project.
- Credible business story: founders need CFO-like help but cannot afford full-time finance support.
## What Went Wrong
### Pivot complexity
Resq evolved from OpsPilot, so the codebase still contained legacy restaurant and operations concepts. The pivot made the product stronger but created naming, repo-history, branding, and mental-model cleanup work.
### Scope risk
Cash forecasting, receivables, financing, vendor optimization, insurance, TinyFish, Stripe, AWS, auth, RLS, and investor framing — too much surface area for a hackathon. The safest version was the focused CFO cash-control flow.
### Live integration risk
TinyFish, Stripe, AWS, and Supabase all add credibility but also add failure modes. The repo wisely kept mock mode and fallback behavior, but the pitch must be honest about what was live vs fixture-backed.
### Production-readiness ambiguity
Some docs describe production deployment and auth hardening. Some describe those as requirements or checklists. Exact status should be verified before presenting the app as production-ready.
### Repo state
Git inspection showed the Resq repo on branch `stripe`, behind `origin/stripe` by one commit. Not a product failure, but matters for portfolio cleanup and future continuation.
## What I Learned
A strong product story can emerge from technical constraints. Keeping AI out of the math is not just an engineering safety choice — it is the core product identity.
- **Engineering:** Forecast engines need explicit assumptions and testable pure functions. Financial AI products need auditability to be credible. Mock/live/degraded modes are reliability design, not hackathon shortcuts. Typed schemas and property tests make a demo feel serious.
- **Product:** "CFO workspace for founders who cannot afford a CFO" is clearer than "AI finance dashboard." The strongest demo is not showing every feature — it is showing the exact week cash breaks and what action buys time. Startup framing works when the technical architecture supports the trust claim.
- **Communication:** Separate technical proof from business ambition. Say: "The repo proves deterministic forecasting and action ranking; the deck frames how this could become a company." Do not oversell live integrations unless verified.
## Continuation Plan
### If I keep building
1. Verify repo status, merge/pull the missing `origin/stripe` commit, create a clean demo branch.
2. Run and document `npm run lint`, `npx tsc --noEmit`, `npm run test`, `npm run build`, and the demo smoke script on the final tree.
3. Build spreadsheet CSV/XLSX import into the same `cash_obligations` and receivables pathway.
4. Decide target customer: SMB owner-operator or post-revenue software founder under $1M ARR.
5. Simplify product surface around Cash Truth, 13-week forecast, and Action Queue.
6. Create a crisp "what is deterministic vs what is AI" explanation for every major screen.
### Portfolio steps
1. Record a 90-second demo showing breakpoint detection and the ranked action queue.
2. Build a case study: architecture diagram, data flow, screenshots.
3. Create two pitch versions: hiring-manager version and startup/investor version.
### Worth continuing?
Yes, with focus. Resq has the stronger career story if polished carefully — it combines full-stack engineering, financial modeling, AI systems, external integration design, and product positioning.
## Portfolio Assets
### Networking pitch
"I built a prototype CFO workspace that takes real ledger facts, generates a deterministic 13-week cash forecast, detects the week cash becomes risky, and ranks actions like collections, payment deferrals, or financing. AI advises, but the math stays deterministic."
### Resume bullets
- Built a fintech cash-control prototype using Next.js, TypeScript, Supabase/Postgres, Drizzle, and Zod to compute 13-week forecasts and detect cash breakpoints.
- Implemented deterministic cash services for current cash, collection lag, forecast waterfalls, breakpoint detection, risk driver analysis, and ranked action recommendations.
- Designed TinyFish mock/live/degraded integration patterns and audit logging so AI-assisted recommendations remain explainable and demo-safe.
### Interview story
"A time I pivoted a broad project into a sharper product. Resq became much stronger once we focused on cash survival instead of general SMB operations."
## Investor / Startup Framing
> [!NOTE]
> Everything in this section comes from the investor deck, not from repo-verified traction. Treat as pitch positioning unless independently validated.
### Deck claims
- "The CFO workspace every founder needs — but can't afford."
- Product flow: connect ledger → see 13-week runway → act on ranked CFO moves.
- Principle: AI advises and never touches the numbers.
- Mentions deterministic cash engine, breakpoint detection, ranked action queue, CFO move library, Supabase audit trail with hash chaining, CSV/XLSX import in progress.
### Pricing (deck)
| Tier | Price |
|---|---|
| Founder | $19/month |
| Growth | $59/month |
| Scale | Custom |
### Ask (deck)
$1M pre-seed. 10 design partners. Q3 2026 public beta target.
### Grounded interpretation
The strongest business angle is affordable CFO-style cash visibility. The competitive angle is deterministic forecasting with AI only in the advisory layer. Possible weakness: repo docs say SMB owner-operator, deck narrows to post-revenue software founders under $1M ARR. That positioning decision needs to be clarified before pitching seriously.
## Questions for [[Mentor Details|Ahnaf]]
1. Does the "AI advises, but never touches the numbers" framing make the project more credible to engineering managers?
2. Would you present Resq as a fintech project, an AI agent project, or a full-stack architecture project?
3. Which part impresses a hiring manager most: forecast engine, audit trail, TinyFish integration, or product positioning?
4. How much production hardening should I do before putting this in a portfolio?
5. Should I continue the investor/startup framing, or keep the case study engineering-focused?
6. How should I talk about mock/live integration modes without sounding like the demo was fake?
7. Is this worth continuing over starting a smaller, cleaner project from scratch?
## Mentor-Meeting Summary
Resq is the more mature portfolio story because it connects architecture, AI boundaries, financial modeling, and product positioning. I want feedback on whether this is impressive as an engineering project, how much to polish it, and how to explain it to people outside fintech. The open decision: should Resq become my main summer portfolio project, or remain a hackathon artifact with a polished case study?

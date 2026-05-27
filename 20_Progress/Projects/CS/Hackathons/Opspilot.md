---
type: project
status: complete
created: 2026-04-27
tags:
  - hackathon
  - portfolio
related:
  - "[[01_Summit]]"
  - "[[Resq]]"
  - "[[Mentor Details]]"
  - "[[Mentorship Board]]"
---
# OpsPilot
## Elevator Pitch
AI operations dashboard for a restaurant manager running Ember Table. One connected workflow: complete a reservation, generate the invoice, mark payment, update the finance ledger, analyze guest feedback, approve a recovery action. AI handles communication and prioritization. Deterministic services own money, status changes, and auditability.
## Problem
Small restaurant managers context-switch constantly — who came in, what needs invoicing, who paid, who had a bad experience, who needs a follow-up. Each handoff is a chance to forget something, lose cash, or damage trust.

The pain is not missing data. The pain is that every operational step depends on the last one, and no tool chains them together for a single-location operator.
### Why AI alone does not solve this
AI can classify feedback and draft replies. It cannot reliably own invoice totals or ledger writes. The product earns trust by making the deterministic chain visible and keeping AI downstream of it.
## Product Overview
### Core demo flow
`reservation completed → invoice generated → invoice paid → finance row created → review analyzed → follow-up surfaced`
### What makes it different
- Real workflow state with tables, APIs, and service boundaries — not a chatbot wrapper.
- AI placed where language tasks live: summaries, review analysis, follow-up drafting, prioritization.
- Deterministic backend owns every financial mutation.
## What We Built
### Completed
- Dashboard: KPIs, AI briefing, feedback spotlight, finance snapshot, connector visibility.
- Appointments page with lifecycle actions.
- Deterministic invoice generation from completed reservation.
- Mark-paid flow creating a `finance_transactions` row exactly once.
- Finance page: summary, transaction ledger, invoice aging.
- Feedback intake → AI analysis → flagging → manager-approved follow-up.
- Integration webhook ingress with raw payload storage, dedupe, service-layer dispatch.
- Workflow timeline / event trail.
- Shared theme system and polished UI shell.
### Partially completed
- AI manager summary — existed, needed final wiring verification.
- Follow-up generation — existed, needed exact flow verification.
- Workflow timeline — needed confirmation all `appointment_events` rendered.
- Guest history resolution — worked through known IDs, may need external-review email fallback.
### Not implemented
Real outbound email/SMS. Public review posting. Receipt upload/OCR. Inventory predictions. Performance analyzer. n8n workflow configuration.
### What was real vs mocked
- **Real:** Supabase schema, seed data, service-layer mutations, API routes, query-backed pages, feedback analysis pipeline, finance transaction creation, webhook dedupe.
- **Mocked/deferred:** Email/SMS delivery, public review posting, receipt OCR, inventory prediction, performance analyzer, n8n integration.
## Tech Stack
| Layer | Tools |
|---|---|
| Frontend | Next.js 16 App Router, React 19, TypeScript, Tailwind CSS 4, shadcn-style components, Recharts, lucide-react |
| Backend | Next.js route handlers, service modules, query modules, Zod validation |
| Database | Supabase Postgres with migrations and seed data |
| AI | Anthropic Claude customer-service agent; optional Gemini/Google AI for reservation parsing |
| Deploy | Vercel-oriented (`vercel.json` present) |
## Architecture
### App structure
- `src/app/` — pages and App Router routes
- `src/app/api/` — route handlers (thin; validate input, delegate to service)
- `src/lib/services/` — deterministic mutations and side effects
- `src/lib/queries/` — UI-facing read models
- `src/lib/domain/` — core business rules: status guards, invoice calculation
- `agents/customer-service/` — Claude-powered review analysis and response
- `supabase/migrations/` — schema migrations
### Data flow
1. UI action → route handler → service → Supabase mutation → event/related rows recorded.
2. Query modules reshape data for dashboards and pages.
3. AI reads facts downstream and drafts summaries/actions.
### Key tables
`organizations`, `customers`, `staff`, `services`, `appointments`, `appointment_events`, `invoices`, `invoice_items`, `finance_transactions`, `integration_connectors`, `integration_sync_events`, `feedback`, `follow_up_actions`, `ai_actions`, `ai_summaries`
### AI boundary
AI may: analyze review sentiment, draft recovery messages, summarize manager priorities, prioritize and explain.
AI must not: own invoice totals, transition reservation/invoice status, write to the ledger, calculate amounts.
### Key engineering decisions
- Supabase/Postgres as single source of truth.
- Services own mutations; routes stay thin.
- Query modules as the UI read-model contract.
- Webhooks reuse the same service layer as first-party UI actions.
- Demo gaps treated explicitly — nothing pretended to be production-ready.
## What Went Well
- Clear operational chain instead of a loose feature set.
- Deterministic finance boundary made the AI feel credible.
- Real dashboard/product shell, not a script or chatbot.
- Supabase migrations and seed data made the demo explainable.
- Feedback workflow was a natural AI use case — review interpretation and response drafting are language tasks.
- Architecture separated route handlers, services, domain rules, and query models cleanly.
- Documentation captured during the build reduced confusion near the deadline.
## What Went Wrong
### Scope pressure
The PRD included appointments, invoices, finance, feedback, integrations, inventory, performance, receipts, OCR, reminders, and analytics. That created breadth risk instead of one unmistakable demo path.
### Technical blockers
- Live Supabase setup and verification were critical near the deadline.
- Some features existed in code but needed demo-flow verification.
- n8n was not configured as the demo source of truth despite integration infrastructure existing.
- Inventory and performance work was teammate-owned and not fully integrated.
### Repo and merge confusion
Docs mention divergence between local work and `origin/main`, merge risk around inventory/shipments, untracked feature work, and dependency drift. Source-control confusion becomes a product risk when nobody knows which version is demo truth.
### Presentation risk
The demo required the audience to understand why this was more than a dashboard. The pitch needed to make the cause-and-effect chain obvious: operational event → system action → AI interpretation → manager decision.
## What I Learned
The most impressive AI projects are not the ones where AI does everything. They are the ones where AI sits on top of a trustworthy system.
- **Engineering:** Deterministic services matter when the app touches money. Database constraints and idempotency are what make a demo credible, not extras. Route handlers should stay thin. Query layers are useful because dashboards need shaped data, not raw rows.
- **Product:** A hackathon product needs one memorable workflow more than a long feature list. "Restaurant owner-manager" was easier to explain than "small business operator." Finance depth made the product feel real because it proved the workflow had consequences beyond UI.
- **Team:** Documentation saved time, but stale documentation confuses agents and teammates. Ownership needs to be explicit early. Demo rehearsal is part of building.
- **Communication:** Pitch in cause-and-effect language. The strongest line is not "we used AI" — it is "AI helps the manager decide, but the system protects the money."
## Continuation Plan
### If I keep building
1. Stabilize the exact OpsPilot hackathon snapshot and remove Resq-era drift.
2. Add focused tests: invoice idempotency, mark-paid finance transaction creation, webhook dedupe, feedback action creation.
3. Connect a real but safe outbound channel — Resend email drafts behind manager approval.
4. Narrow to one vertical and one workflow. Make the finance page more decision-oriented.
5. Turn inventory/performance into clearly labeled future modules unless they become real.
### Portfolio steps
1. Record a 90-second demo of the reservation → invoice → finance → feedback loop.
2. Build a case-study page: problem, architecture diagram, demo flow, lessons learned.
3. Write 2–3 resume bullets emphasizing deterministic workflow automation plus AI-assisted recovery.
### Worth continuing?
Yes, as a portfolio artifact. It does not need to become a startup, but it shows product thinking, data modeling, AI boundaries, and business workflow automation in one project.
## Portfolio Assets
### Networking pitch
"I built an AI operations dashboard for a restaurant manager. The interesting part was separating the AI layer from the financial truth: AI drafted recovery messages and summaries, but deterministic services handled invoices, payments, and ledger updates."
### Resume bullets
- Built a full-stack restaurant operations dashboard using Next.js, TypeScript, Supabase, and Zod to automate a reservation-to-invoice-to-finance-to-feedback workflow.
- Designed service-layer boundaries so AI drafted customer recovery actions while deterministic backend logic owned invoice totals, state transitions, and ledger writes.
- Implemented Supabase-backed appointments, invoices, finance transactions, feedback analysis, webhook ingestion, and dashboard read models for a hackathon demo.
### Interview story
"A time I learned to reduce scope under time pressure. We had many modules, but the strongest demo was one reliable operational loop."
## Questions for [[Mentor Details|Ahnaf]]
1. Does the architecture separation (routes → services → domain → queries) read as mature, or would you simplify it for a portfolio project?
2. What part stands out most to a hiring manager: product polish, backend workflow, AI integration, or data modeling?
3. Is it better to present this as a restaurant product or a general small-business operations platform?
4. What tests would make this project feel credible?
5. Should I continue building outbound email/SMS, or stop and polish the case study?
6. How should I explain the AI boundary to non-technical people?
7. Is the scope too broad for a portfolio artifact, and if so, what should I cut?
## Mentor-Meeting Summary
OpsPilot is a real full-stack workflow, not a UI mock. The strongest technical decision was keeping AI downstream of deterministic business logic. I want feedback on whether the architecture and product story are strong enough for a portfolio case study, and what to polish before showing it to more people. The open decision: keep improving OpsPilot as a portfolio artifact, archive it cleanly, or focus on [[Resq]] or the next hackathon.

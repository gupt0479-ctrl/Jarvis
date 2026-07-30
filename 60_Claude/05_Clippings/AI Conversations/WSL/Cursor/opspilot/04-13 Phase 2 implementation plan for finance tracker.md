---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: wsl
title: "Phase 2 implementation plan for finance tracker"
started_at: 2026-04-13T06:38:57
ended_at: 2026-04-13T07:30:33
exported_at: 2026-07-30T19:56:24
project: opspilot
cwd: "/home/anant_gupta/projects/hackathon/opspilot"
session_id: b0a213c4-2306-4be1-9d96-903ca8adda70
status: raw
turn_count: 12
tools_used:
  CreatePlan: 1
  Delete: 6
  Glob: 13
  Grep: 17
  Read: 68
  Shell: 13
  StrReplace: 49
  TodoWrite: 3
  Write: 17
files_touched:
  - "/home/anant_gupta/projects/hackathon/opspilot"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/env.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/db/supabase-server.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/0001_core_ledger.sql"
  - "/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/001_scheduling_invoices.sql"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/finance.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/invoices.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/[id]/mark-paid/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/appointments.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/invoice.service.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/supabase/seed.sql"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/dashboard/summary/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/dashboard.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase/index.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/package.json"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/integrations.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/constants/enums.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/finance.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/generate/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase/client.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/[id]/remind/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase/queries.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/ai/generate-reminder.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/types.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/reservation.service.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/follow-ups/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/types/index.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/dashboard.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/supabase/archived/001_scheduling_invoices_legacy.sql"
  - "/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/002_invoice_reminders.sql"
  - "/home/anant_gupta/projects/hackathon/opspilot/tsconfig.json"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/invoice.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/integrations/webhook-guard.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/cron/mark-overdue-invoices/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/ai.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/ai/manager-summary/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/vitest.config.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/integrations.test.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.domain.test.ts"
  - "/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/terminals/58363.txt"
  - "/home/anant_gupta/projects/hackathon/opspilot/scripts/repro-dashboard-data.mjs"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/db/ledger-schema.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/components/ops/ledger-schema-banner.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/.cursor/debug-b0a213.log"
  - "/home/anant_gupta/projects/hackathon/opspilot/src"
files_changed_count: 33
lines_added: 1165
lines_removed: 371
tags:
  - input
  - ai-conversation
  - cursor
  - wsl
---

# Phase 2 implementation plan for finance tracker

## You

<user_query>
This is a plan that i came up with the implement my part of the project, i need you to modify this plan based on my current codebase. Here is the prompt: "You are Agent Composer 2 working inside the OpsPilot repo for Ember Table. Your job is to produce and then execute a secure phase-2 implementation plan for the Supabase-backed finance tracker, connector/MCP bridge, and downstream AI orchestration.

Read this entire prompt before acting.

CORE RULES

1. Do not assume the repo is in a clean or merged state.
2. Do not treat MCP here as a blockchain or wallet bridge unless the codebase explicitly proves that. In this repo, default to “connector normalization + event-ingestion bridge” semantics.
3. Do not let AI own financial truth, workflow truth, invoice math, payment state, or ledger writes.
4. Do not write any new feature code until you finish the branch-state audit and produce a concrete gap report.
5. Prefer deterministic service logic, idempotent writes, auditability, and verification over speed hacks.
6. Keep all sensitive keys server-only. Never expose service-role credentials to the browser.
7. When blocked by missing runtime secrets or teammate PR state, say exactly what is blocked and continue with all non-blocked work.

PROJECT GROUNDING

Use the PRD and repo analyses as constraints:

* Supabase/Postgres is the source of truth.
* `finance_transactions` is the authoritative finance ledger.
* `appointments -> invoices -> finance_transactions` is the core deterministic workflow.
* AI is allowed to summarize, classify, prioritize, and draft.
* AI is not allowed to create financial mutations directly.
* Route handlers belong under `src/app/api/**/route.ts`.
* Organization scoping must exist everywhere, even if a temporary `DEMO_ORG_ID` shortcut is still in use.
* Webhook/provider ingestion must validate, persist raw payloads, dedupe retries, normalize into internal commands, and dispatch into the same service layer used by first-party routes.

PRIMARY OBJECTIVE

Phase 2 is to secure and complete three workstreams on top of the current foundation:
A. financial tracker hardening
B. MCP bridge hardening
C. AI orchestration on deterministic facts

STARTING ASSUMPTIONS TO VERIFY, NOT BLINDLY TRUST

You must verify these in the repo before making changes:

* local branch may be behind `origin/main`
* merge conflicts are likely in inventory/shipment paths, shared types, layout/sidebar, globals, README, and related Supabase rewrites
* local branch may already contain new Supabase-first files such as:

  * `src/lib/env.ts`
  * `src/lib/db/supabase-server.ts`
  * `src/lib/services/appointments.ts`
  * `src/lib/services/invoices.ts`
  * `src/lib/services/finance.ts`
  * `src/lib/services/integrations.ts`
  * `src/lib/queries/finance.ts`
  * `supabase/migrations/0001_core_ledger.sql`
* older in-memory/demo modules may still coexist with newer Supabase-backed code
* AI summary surfaces may still be stubbed or incomplete

PHASE 0 — REPO TRUTH CAPTURE

Before coding, inspect and report:

1. Git state

* current branch
* branch tip commit
* `origin/main` tip if available
* merge base with `origin/main`
* commits added in the last 12 hours
* modified tracked files
* untracked files
* any unresolved merge state
* whether teammate PR changes have already landed locally

2. Working-tree truth split
   Classify code into:

* committed local branch truth
* uncommitted working-tree truth
* remote `origin/main` truth
* untracked but important implementation files

3. Deliverable
   Produce a short “repo truth report” with:

* safe to build on now
* must merge or reconcile first
* dangerous mixed-state areas
* files that look phase-2-critical but are still untracked

Do not skip this step.

PHASE 1 — SUPABASE FOUNDATION AUDIT

Inspect and verify the current backend foundation end to end.

Check these areas:

1. Environment and secrets
   Inspect:

* `src/lib/env.ts`
* `.env*` references
* any Vercel/Supabase config docs
  Verify:
* `NEXT_PUBLIC_SUPABASE_URL`
* `NEXT_PUBLIC_SUPABASE_ANON_KEY`
* `SUPABASE_SERVICE_ROLE_KEY`
* `DEMO_ORG_ID`
* any webhook signing secrets
* any OpenAI API env vars
  Require:
* Zod validation for required env vars
* clear server-only boundary for service-role usage
* no service-role import into client components
  Flag:
* missing env validation
* duplicate env loaders
* browser exposure of privileged credentials

2. Supabase client architecture
   Inspect:

* `src/lib/db/supabase-server.ts`
* any `src/lib/supabase/client.ts`
* any auth helpers or browser clients
  Require:
* explicit separation between browser/anon client and server/service client
* server-only guard for privileged client modules
* consistent call sites
  Flag:
* server route handlers using anon browser client where privileged writes are required
* mixed client factories without clear ownership
* duplicated Supabase initialization patterns

3. Migrations and schema
   Inspect:

* `supabase/migrations/**`
* `supabase/seed.sql`
* any README/setup docs
  Require verification for core tables:
* organizations
* customers
* staff
* services
* appointments
* appointment_events
* invoices
* invoice_items
* finance_transactions
* integration_connectors
* integration_sync_events
  Also inspect whether these are present or still deferred:
* receipts
* ai_actions
* ai_summaries
* feedback
* follow_up_actions
  Check:
* PK/FK integrity
* `organization_id` presence
* enum alignment with PRD
* indexes for `organization_id`, `status`, `due_at`, `starts_at`, `created_at`, and invoice linkage
* whether `finance_transactions` has enough constraints to support safe idempotency
  Flag:
* missing org scoping
* weak foreign keys
* mismatched enum values
* schema drift from PRD
* incomplete seed coverage

4. RLS and authorization readiness
   Inspect:

* migration SQL
* Supabase policy files or SQL blocks
* route-level authorization patterns
  Require:
* at minimum, schema and queries must be RLS-compatible
* a documented plan for enabling RLS on all business tables
* owner/manager/front-desk/staff role model alignment
  Flag:
* tables with no row-level access plan
* logic that assumes permanent demo-org bypass
* writes that cannot be made tenant-safe later

PHASE 2 — FINANCE TRACKER / AGENT HARDENING

Treat finance as deterministic first, AI second.

1. Audit the full finance flow
   Trace these flows:

* appointment completion
* invoice generation
* invoice sending
* invoice mark-paid
* finance summary queries
* finance transactions list
  Verify the exact path:
  `appointments -> invoices -> finance_transactions`

2. Confirm authoritative finance rules
   Require these invariants:

* invoice totals come from deterministic backend logic only
* AI does not compute or override money values
* `mark-paid` creates exactly one revenue ledger row per payment event
* overdue status is derived deterministically
* finance summary reads from invoices + ledger, not from AI output
* dashboard finance cards are backed by real queries, not mocks

3. Inspect service-layer ownership
   Inspect:

* `src/lib/services/appointments.ts`
* `src/lib/services/invoices.ts`
* `src/lib/services/finance.ts`
  Require:
* business mutations owned by services, not route handlers
* route handlers remain thin
* multi-step writes wrapped safely
* clear audit/event emission around transitions
  Flag:
* route handlers doing business logic directly
* ledger writes split across multiple unrelated modules
* duplicated invoice status logic
* missing transaction boundaries

4. Finance data model completion
   Audit and complete if needed:

* invoice status lifecycle
* due date logic
* amount_paid handling
* finance transaction fields:

  * type
  * direction
  * amount
  * occurred_at
  * invoice_id
  * category
  * payment_method
  * tax_relevant
  * writeoff_eligible
  * notes
    Add only what is required by the PRD and current milestone.
    Do not build a full accounting platform.

5. Finance AI boundary
   Implement or enforce these rules:

* allowed AI outputs:

  * manager daily summary
  * finance risk explanation
  * collections prioritization
  * non-binding recommended actions
  * draft reminders/follow-ups
* forbidden AI outputs:

  * invoice total changes
  * payment state changes
  * ledger row creation
  * tax computation from natural language
  * autonomous reconciliation decisions

6. Finance verification
   Add tests or validation scripts for:

* `mark-paid` idempotency
* duplicate request handling
* invoice-to-ledger consistency
* finance summary correctness for seeded demo states
* empty-state behavior on fresh database

PHASE 3 — MCP BRIDGE HARDENING

In this repo, MCP is the integration bridge layer.

1. First verify the current architecture
   Inspect:

* `src/lib/services/integrations.ts`
* `src/lib/integrations/**`
* `src/app/api/integrations/**`
* webhook routes
* query modules and integration pages
  Determine whether the current state is:
* only a stub
* partial ingest pipeline
* already normalizing provider payloads
* already dispatching into internal services

2. Target MCP behavior for phase 2
   Formalize this pipeline:
   provider webhook/event
   -> request validation
   -> signature/auth verification where applicable
   -> raw payload persistence
   -> dedupe by provider + external_event_id
   -> normalization into canonical internal command/event
   -> deterministic service dispatch
   -> processing status update
   -> audit/logging/observability

3. Canonical internal contract
   Define and enforce:

* canonical provider-independent event names
* canonical payload schema
* mapping rules for provider adapters
* processing statuses such as:

  * received
  * validated
  * deduped
  * normalized
  * dispatched
  * processed
  * failed
  * retryable_failed
    Do not let provider-specific fields leak into core finance logic.

4. Provider adapter pattern
   Create or harden per-provider adapters under a dedicated normalization layer.
   At minimum:

* adapter input schema
* normalized output schema
* mapper function
* provider-specific verification logic
* replay/idempotency handling
  Do not add many providers at once.
  Complete one provider and one manual/fake provider path first.

5. Security requirements for inbound events
   Require:

* provider authentication or signature verification wherever the provider supports it
* raw request/body preservation when signature verification needs exact bytes
* rate limiting or abuse controls for public webhook endpoints
* no direct SQL mutations from webhook handlers
* no trust in provider payloads without schema validation
* raw payload archival for debugging
  Flag:
* unsigned open webhook handlers
* payloads written straight into business tables
* missing dedupe keys
* missing failure states
* missing connector health fields

6. MCP observability
   Add or harden:

* structured logs
* sync/error status per connector
* last successful sync
* last error summary
* replay safety notes
* manual reprocess path for failed events
* dashboard/integrations page surface for connector health

PHASE 4 — AI ORCHESTRATION ON DETERMINISTIC FACTS

Do not start this phase until finance and MCP deterministic inputs are verified.

1. Scope
   Only implement AI features that consume facts already in Postgres:

* daily manager summary
* next-best actions
* finance risk explanations
* invoice reminder drafts
* customer follow-up drafts
* connector anomaly summaries

2. Structured outputs
   Use schema-constrained outputs for AI responses.
   Require:

* input facts assembled server-side
* output parsed against strict schemas
* prompt/output persistence for observability where appropriate
* confidence/notes fields when useful
  Flag:
* free-form model outputs directly wired into core workflow writes
* prompts that ask the model to infer ledger truth
* AI tasks that mutate financial state

3. AI data contracts
   Create or verify:

* `FinanceSummaryFactsSchema`
* `ManagerSummarySchema`
* `ActionRecommendationSchema`
* `ConnectorAnomalySchema`
* `FollowUpDraftSchema`
  Require all AI tasks to consume deterministic facts objects assembled by server code.

4. AI execution boundary
   AI orchestration must:

* read facts from query modules or safe read services
* write only to `ai_summaries`, `ai_actions`, or other clearly non-authoritative AI tables
* never bypass service-layer mutation rules
* never issue payment or invoice mutations directly

PHASE 5 — SECURITY, ACCESS CONTROL, AND AUDITABILITY

Apply these throughout all changes.

1. Access model
   Plan and harden:

* organization scoping on every core business table
* future RLS compatibility
* route-level auth stubs that can evolve into real membership-based authorization
* separation of owner, manager, front-desk, and staff actions

2. Auditability
   Require durable audit trails for:

* appointment completion
* invoice generation
* invoice send
* invoice paid
* webhook received/processed/failed
* AI summary generation
  Prefer event tables or explicit audit logs over console-only history.

3. Error handling
   All critical routes/services must:

* return structured errors
* log machine-readable error metadata
* preserve enough identifiers for replay/debug
* avoid leaking secrets in logs or responses

4. Verification gates
   Add or update:

* lint
* typecheck
* production build
* domain/service tests
* route smoke tests
* webhook replay tests
* finance idempotency tests
  If no test harness exists, create the smallest reliable one needed for service and route verification.

PHASE 6 — UI AND READ MODEL CHECK

Do not let the backend be correct but invisible.

Inspect and verify:

* `src/app/dashboard/**`
* `src/app/finance/**`
* `src/app/integrations/**`
* read query modules
  Require:
* dashboard finance summary uses real route/query data
* finance page uses real ledger/invoice data
* integrations page reflects real connector statuses
* no critical finance or MCP screens depend on stale mock arrays
  Flag:
* partially wired pages
* mixed mock and live data on the same screen
* UI labels that contradict backend enums/statuses

MANDATORY OUTPUTS FROM YOUR FIRST PASS

Before editing code, produce these in order:

1. Executive summary
2. Repo truth report
3. Current-state review
4. Gap analysis split into:

* ready to build on
* risky / inconsistent
* blocked by branch reconciliation

5. Workstream plan with:

* objectives
* files likely to change
* dependencies
* security requirements
* acceptance criteria
* verification checkpoints

6. Recommended execution order
7. Definition of done for phase 2

ONLY AFTER THAT FIRST PASS

After you present the plan, proceed in this order unless the repo state forces a change:

1. Branch reconciliation prep

* identify conflict-prone files
* avoid editing high-conflict files until necessary
* preserve local untracked phase-1 foundation work
* do not overwrite teammate changes blindly

2. Backend contract hardening

* env
* server client separation
* migrations
* enums/schemas
* org scoping readiness

3. Finance hardening

* service invariants
* idempotency
* ledger correctness
* finance read models

4. MCP hardening

* provider adapter contract
* webhook verification
* dedupe
* normalization
* processing status lifecycle

5. AI orchestration

* only after deterministic facts are stable
* schema-constrained outputs only
* summaries/drafts only

6. Verification and cleanup

* tests
* logs
* docs
* setup instructions
* merge-conflict notes for the team

FILES TO PRIORITIZE

Inspect these first:

* `src/lib/env.ts`
* `src/lib/db/supabase-server.ts`
* `src/lib/services/appointments.ts`
* `src/lib/services/invoices.ts`
* `src/lib/services/finance.ts`
* `src/lib/services/integrations.ts`
* `src/lib/queries/dashboard.ts`
* `src/lib/queries/appointments.ts`
* `src/lib/queries/invoices.ts`
* `src/lib/queries/finance.ts`
* `src/app/api/dashboard/**`
* `src/app/api/appointments/**`
* `src/app/api/invoices/**`
* `src/app/api/finance/**`
* `src/app/api/integrations/**`
* `src/app/dashboard/**`
* `src/app/finance/**`
* `src/app/integrations/**`
* `supabase/migrations/**`
* `supabase/seed.sql`
* `.claude/PRD.md`
* any context docs under `.claude/context/**`

PLACEHOLDERS TO RESPECT

Use placeholders rather than inventing secrets:

* `<NEXT_PUBLIC_SUPABASE_URL>`
* `<NEXT_PUBLIC_SUPABASE_ANON_KEY>`
* `<SUPABASE_SERVICE_ROLE_KEY>`
* `<DEMO_ORG_ID>`
* `<OPENAI_API_KEY>`
* `<PROVIDER_WEBHOOK_SECRET>`
* `<PROVIDER_API_KEY>`
* `<VERCEL_ENV>`

NON-NEGOTIABLE “DO NOT DO THIS” LIST

* Do not add blockchain, wallet, token, or chain abstractions unless the repo explicitly requires them.
* Do not let AI mutate invoices, payments, or ledger rows.
* Do not expose service-role keys to the browser.
* Do not bypass service methods from webhook handlers.
* Do not add a second competing source of truth for finance state.
* Do not keep critical finance/integration code only in untracked files.
* Do not ship without idempotency checks for `mark-paid` and webhook replays.
* Do not keep mock finance data on core demo pages once real queries exist.

SUCCESS CRITERIA

Phase 2 is done only when all of the following are true:

* repo state is reconciled enough to build on safely
* Supabase configuration is consistent and server-safe
* finance tracker is deterministic, auditable, and idempotent
* connector/MCP bridge is validated, replay-safe, and observable
* AI features are constrained to summaries/drafts/recommendations grounded in DB facts
* dashboard, finance, and integrations surfaces reflect real backend state
* verification steps pass and are documented

When you finish the first-pass plan, continue into implementation in small, reviewable steps and re-check branch conflict risk before each high-touch file.
". 

Analyze the prompt in detail and create a well thought out plan to implement these listed things.
</user_query>

## Cursor

Exploring the codebase to map what exists versus your prompt, then producing a tailored phase-2 plan.

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

Synthesizing findings: the repo already implements much of your prompt’s target architecture, but two parallel stacks (ledger vs legacy invoice/reservation) and duplicate Supabase clients are the main risks. Creating a codebase-specific execution plan.

[REDACTED]

**Tool calls:**

- `Glob` — pattern `**/src/lib/env.ts`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Glob` — pattern `**/supabase-server.ts`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Glob` — pattern `**/src/lib/services/**/*.ts`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Glob` — pattern `**/supabase/migrations/**/*.sql`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Glob` — pattern `**/src/app/api/**/route.ts`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Glob` — pattern `**/src/lib/queries/**/*.ts`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/env.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/db/supabase-server.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/0001_core_ledger.sql`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/001_scheduling_invoices.sql`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/finance.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/invoices.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/0001_core_ledger.sql`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/[id]/mark-paid/route.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/appointments.ts`
- `Grep` — pattern `invoice\.service|from \"@/lib/services/invoice`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/invoice.service.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/seed.sql`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/dashboard/summary/route.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/dashboard.ts`
- `Grep` — pattern `RLS|POLICY|enable row level`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Grep` — pattern `openai|OpenAI|ai_summaries`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase/index.ts`
- `Glob` — pattern `**/src/app/finance/**/*.tsx`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Glob` — pattern `**/src/app/integrations/**/*.tsx`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/package.json`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/integrations.ts`
- `Grep` — pattern `supabaseAdmin|from \"@/lib/supabase`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/constants/enums.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/constants/enums.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/seed.sql`
- `Grep` — pattern `FinanceSummaryFacts|ManagerSummary|ActionRecommendation`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/finance.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/generate/route.ts`
- `CreatePlan` — `{"name":"Phase-2 OpsPilot Revised","overview":"Adapt your Ember Table phase-2 prompt to this repo’s actual state: the core ledger path (`appointments` → `invoices` → `finance_transactions`), finance queries, and an MCP-style webhook pipeline already exist, but legacy `invoice.service` / `supabase.ts…`

## You

<user_query>
Phase-2 plan tailored to current OpsPilot codebase

Implement the plan as specified, it is attached for your reference. Do NOT edit the plan file itself.

To-do's from the plan have already been created. Do not create them again. Mark them as in_progress as you work, starting with the first one. Don't stop until you have completed all the to-dos.
</user_query>

## Cursor

Implementing the Phase-2 plan: starting repo/migration reconciliation and working through the todos systematically.

[REDACTED]

Fetch failed (SSH/host keys). Archiving the legacy migration locally and proceeding with implementation.

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

Implementing: archiving the legacy migration and applying core code changes.

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

Applying bulk edits: updating `reservation.service.ts`, removing `supabase.ts`, extending `invoices.ts` and `env.ts`.

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

Here is what was implemented against the phase-2 plan (plan file was not touched).

### Repo / migrations
- Removed conflicting [`supabase/migrations/001_scheduling_invoices.sql`](supabase/migrations/001_scheduling_invoices.sql) from the migration chain; archived equivalent SQL under [`supabase/archived/[REDACTED].sql`](supabase/archived/[REDACTED].sql).
- Added [`supabase/migrations/002_invoice_reminders.sql`](supabase/migrations/002_invoice_reminders.sql) (`reminder_count`, `last_reminded_at`) for reminder tracking on ledger invoices.
- `git fetch` to `origin` failed in this environment (SSH host key); nothing else blocked.

### Single privileged Supabase path
- Deleted [`src/lib/supabase.ts`](src/lib/supabase.ts) (anon + placeholder service-role pattern).
- [`src/lib/services/reservation.service.ts`](src/lib/services/reservation.service.ts) now uses `import "server-only"` and [`createServerSupabaseClient`](src/lib/db/supabase-server.ts) via a small `admin()` helper.
- Inventory/shipment code still uses [`@/lib/supabase/client`](src/lib/supabase/client.ts) (anon) as before.

### Legacy invoice API removed
- Removed [`src/lib/services/invoice.service.ts`](src/lib/services/invoice.service.ts).
- [`src/app/api/invoices/generate/route.ts`](src/app/api/invoices/generate/route.ts) now accepts `{ appointmentId }` and calls [`ensureInvoiceForCompletedAppointment`](src/lib/services/invoices.ts) (catalog-priced invoice only).
- [`src/app/api/invoices/[id]/remind/route.ts`](src/app/api/invoices/[id]/remind/route.ts) uses [`getInvoiceDetail`](src/lib/services/invoices.ts) + [`recordInvoiceReminderSent`](src/lib/services/invoices.ts) + updated [`generate-reminder`](src/lib/ai/generate-reminder.ts) (`InvoiceReminderFacts`; amounts from DB only).
- [`DOMAIN_EVENT.INVOICE_REMINDER_SENT`](src/lib/constants/enums.ts) + [`WorkflowEventType`](src/lib/types/index.ts) extended accordingly.
- [`GenerateInvoiceFromAppointmentBodySchema`](src/lib/schemas/invoice.ts) for validation.

### Finance / cron / tests
- [`POST /api/cron/mark-overdue-invoices`](src/app/api/cron/mark-overdue-invoices/route.ts) runs [`markOverdueInvoices`](src/lib/services/invoices.ts); optional `Authorization: Bearer <CRON_SECRET>` when `CRON_SECRET` is set; blocked in production if unset.
- **Vitest**: [`vitest.config.ts`](vitest.config.ts), `npm test` / `npm run test:watch`, [`src/lib/schemas/integrations.test.ts`](src/lib/schemas/integrations.test.ts), [`src/lib/services/integrations.domain.test.ts`](src/lib/services/integrations.domain.test.ts).

### MCP bridge hardening
- [`integrationWebhookAuthError` / `integrationWebhookRateLimitError`](src/lib/integrations/webhook-guard.ts); wired in [`webhooks/[provider]/route.ts`](src/app/api/integrations/webhooks/[provider]/route.ts).
- Env behavior: `INTEGRATIONS_WEBHOOK_SECRET` (compare with `x-webhook-secret` or `Authorization: Bearer`); production rejects if unset; local dev needs `INTEGRATIONS_WEBHOOK_ALLOW_UNSIGNED=true` when no secret.
- [`ingestWebhookPayload`](src/lib/services/integrations.ts): mutating events require `externalEventId`; `invoice.paid` caps `amountPaid` to `total_amount`; failed dispatch sets connector `status: error` + `last_error`; exported [`normalizeDomainEvent`](src/lib/services/integrations.ts) / [`MUTATING_INTEGRATION_EVENTS`](src/lib/services/integrations.ts).
- Integrations UI copy updated for secrets + `externalEventId` ([`integrations/page.tsx`](src/app/integrations/page.tsx)).

### AI + dashboard (read models)
- [`src/lib/schemas/ai.ts`](src/lib/schemas/ai.ts) — `ManagerSummarySchema`.
- [`src/lib/services/ai-summaries.ts`](src/lib/services/ai-summaries.ts) — `buildFinanceSummaryFacts`, `generateAndPersistManagerSummary`, `getLatestManagerSummary`, `getManagerSummaryForDashboard` (fallback summary is **100% facts-derived**, no model).
- [`GET`/`POST /api/ai/manager-summary`](src/app/api/ai/manager-summary/route.ts) — POST persists to `ai_summaries`; optional `CRON_SECRET` gate when set.
- [`getDashboardSummary`](src/lib/queries/dashboard.ts) + [`DashboardSummarySchema`](src/lib/schemas/dashboard.ts): connector health + manager summary card data.
- [`dashboard/page.tsx`](src/app/dashboard/page.tsx): ledger-accurate revenue subtitle, integrations strip, manager summary (AI vs fallback badge); **`export const dynamic = "force-dynamic"`** on dashboard, finance, integrations to avoid build hangs on live Supabase ([`finance/page.tsx`](src/app/finance/page.tsx), [`integrations/page.tsx`](src/app/integrations/page.tsx)).

### Other
- [`tsconfig.json`](tsconfig.json) include list cleaned up.

### How to verify
```bash
npm run lint
npm run test
npm run build
```
Apply DB: run migrations (e.g. `supabase db reset` or apply `002_invoice_reminders.sql`), then seed.

**New / important env vars**
- `INTEGRATIONS_WEBHOOK_SECRET` — required in production for webhooks.
- `INTEGRATIONS_WEBHOOK_ALLOW_UNSIGNED=true` — local only when no secret.
- `CRON_SECRET` — optional; if set, protects `POST /api/cron/mark-overdue-invoices` and `POST /api/ai/manager-summary`.

**Breaking API change:** `POST /api/invoices/generate` no longer accepts `reservation_id` / `line_items`; use `{ "appointmentId": "<uuid>" }` for a **completed** appointment.

[REDACTED]

**Tool calls:**

- `TodoWrite` — `{"todos":[{"id":"reconcile-git-migrations","content":"Fetch/merge-base with origin/main; resolve mcp-bridges dirty paths; decide archive/remove for 001 migration; confirm fresh reset uses 0001+seed only","status":"in_progress"}],"merge":true}`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && git status -sb && git fetch origin 2>&1 && git rev-parse HEAD && git rev-parse origin/main 2>/dev/null; git merge-base HEAD origin/main 2>/dev/null; git log --oneline -5`
- `Glob` — pattern `**/*`, path `/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/001_scheduling_invoices.sql`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase/client.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/invoice.service.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/[id]/remind/route.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase/queries.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/ai/generate-reminder.ts`
- `Grep` — pattern `from \"@/lib/supabase\"|from '@/lib/supabase'`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Grep` — pattern `reservation\.service|invoice\.service`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/types.ts`
- `Glob` — pattern `**/*`, path `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard`
- `Glob` — pattern `**/types*.ts`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/reservation.service.ts`
- `Grep` — pattern `@/lib/supabase`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/follow-ups/route.ts`
- `Grep` — pattern `from \"@/lib/types\"`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Glob` — pattern `**/types/**`, path `/home/anant_gupta/projects/hackathon/opspilot/src/lib`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/types/index.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/finance.ts`
- `Grep` — pattern `^export type Invoice`, path `/home/anant_gupta/projects/hackathon/opspilot/src/lib/types/index.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/types/index.ts`
- `Grep` — pattern `Invoice`, path `/home/anant_gupta/projects/hackathon/opspilot/src/lib/types/index.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/dashboard.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/archived/001_scheduling_invoices_legacy.sql`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/001_scheduling_invoices.sql`
- `Shell` — `cp /home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/001_scheduling_invoices.sql /home/anant_gupta/projects/hackathon/opspilot/supabase/archived/[REDACTED].sql`
- `Delete` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/001_scheduling_invoices.sql`
- `Delete` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/archived/001_scheduling_invoices_legacy.sql`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/archived/001_scheduling_invoices_legacy.sql`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/002_invoice_reminders.sql`
- `TodoWrite` — `{"todos":[{"id":"reconcile-git-migrations","content":"Fetch/merge-base with origin/main; resolve mcp-bridges dirty paths; decide archive/remove for 001 migration; confirm fresh reset uses 0001+seed only","status":"completed"},{"id":"unify-supabase-clients","content":"Consolidate on createServerSupab…`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/tsconfig.json`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/reservation.service.ts`
- `Grep` — pattern `DOMAIN_EVENT`, path `/home/anant_gupta/projects/hackathon/opspilot/src/lib/constants/enums.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/reservation.service.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/reservation.service.ts`
- `Delete` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/tsconfig.json`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/reservation.service.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/reservation.service.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/constants/enums.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/invoices.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/invoice.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/invoice.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/generate/route.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/[id]/remind/route.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/ai/generate-reminder.ts`
- `Delete` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/invoice.service.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/integrations/webhook-guard.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/cron/mark-overdue-invoices/route.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/ai.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/ai/manager-summary/route.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts`
- `Grep` — pattern `fallbackSummary`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/dashboard.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/dashboard.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/dashboard.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts`
- `Glob` — pattern `.env*.example`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/ai/manager-summary/route.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/types/index.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/[id]/remind/route.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/package.json`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/vitest.config.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/integrations.test.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.domain.test.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/package.json`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/package.json`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && npm install && npm run test && npm run build`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/ai/manager-summary/route.ts`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && npm run build && npm run lint`
- `Read` — `/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/terminals/58363.txt`
- `Read` — `/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/terminals/58363.txt`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && npm run build && npm run lint`
- `Shell` — `pkill -f "next build" 2>/dev/null; sleep 2; cd /home/anant_gupta/projects/hackathon/opspilot && rm -f .next/lock 2>/dev/null; npm run build && npm run lint`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && npm run build 2>&1`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && npm run lint 2>&1`
- `TodoWrite` — `{"todos":[{"id":"unify-supabase-clients","content":"Consolidate on createServerSupabaseClient + getServerEnv; remove or harden src/lib/supabase.ts (no placeholder service key); migrate inventory/shipment call sites intentionally","status":"completed"},{"id":"retire-legacy-invoice-api","content":"Rep…`

## You

<user_query>
Implement the plan as specified, it is attached for your reference. Do NOT edit the plan file itself.

To-do's from the plan have already been created. Do not create them again. Mark them as in_progress as you work, starting with the first one. Don't stop until you have completed all the to-dos.
</user_query>

## You

<user_query>
Implement the plan as specified, it is attached for your reference. Do NOT edit the plan file itself.

To-do's from the plan have already been created. Do not create them again. Mark them as in_progress as you work, starting with the first one. Don't stop until you have completed all the to-dos.
</user_query>

## You

[Image]
[Image]
[Image]
<image_files>
The following images were provdied by the user and saved to the workspace for future use:
1. /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/assets/[REDACTED].png
2. /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/assets/[REDACTED].png
3. /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/assets/[REDACTED].png

These images can be copied for use in other locations.
</image_files>
<user_query>
Dashboard does not show up anythng. I need your help doing an anlysis of all the code changes that you done, review the files. Make any necessary changes to the files that are causing these issues. Make sure to completely implement the plan 2.
</user_query>

## Cursor

Tracing the dashboard data path and adding debug instrumentation to capture the thrown error (the UI swallows it with `.catch(() => null)`).

[REDACTED]

[REDACTED]

[REDACTED]

Running an integration-style check against the real Supabase client to capture the thrown error (simulates the dashboard path).

[REDACTED]

Creating a small reproduction script (no `server-only`) to call Supabase the same way the dashboard does and capture the failing query.

[REDACTED]

[REDACTED]

Checking the remote `invoices` table shape:

[REDACTED]

[REDACTED]

Identifying root cause with runtime evidence: the connected Supabase project uses a legacy `invoices` shape (`total`, `line_items`, …) and is missing `integration_connectors` and `ai_summaries`. Queries expect `0001_core_ledger` columns (`invoice_number`, `total_amount`, …), so PostgREST throws and the dashboard's `.catch(() => null)` hides the real error. Adding a ledger schema health check and surfacing clear errors (and fixing the integrations page masking DB errors as “no connectors”).

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

## Analysis (with runtime evidence)

I ran [`scripts/repro-dashboard-data.mjs`](scripts/repro-dashboard-data.mjs) against your project’s `.env.local` (no secrets printed). Results:

| Check | Result |
|--------|--------|
| `appointments` + `organization_id` | OK (1 row) |
| `invoices` with ledger columns `invoice_number`, `total_amount`, … | **Error:** `column invoices.invoice_number does not exist` |
| `invoices` sample row keys | **`total`, `line_items`, …** — legacy invoice shape, not `0001_core_ledger`** |
| `integration_connectors` | **Error:** `Could not find the table 'public.integration_connectors'` |
| `ai_summaries` | **Error:** `Could not find the table 'public.ai_summaries'` |

### Hypotheses

1. **H1 — Queries assume `0001_core_ledger` but the DB is legacy/partial** — **CONFIRMED** (`invoice_number` / `total_amount` missing; `total` / `line_items` present).
2. **H2 — MCP / AI tables never migrated** — **CONFIRMED** (`integration_connectors`, `ai_summaries` missing).
3. **H3 — Dashboard `.catch(() => null)` hides PostgREST errors** — **CONFIRMED** (code showed a generic message while the real failure was schema mismatch).
4. **H4 — Integrations used `.catch(() => [])` so a missing table looked like “no seed”** — **CONFIRMED** (code masked `listConnectors` failures).

**Root cause:** The linked Supabase project is **not** on the Phase-2 ledger schema from [`supabase/migrations/0001_core_ledger.sql`](supabase/migrations/0001_core_ledger.sql) (and follow-ons). The app code is consistent with the plan; the database must be migrated (and re-seeded) for dashboard/finance/integrations to load data.

### What we changed in code

1. **[`src/lib/db/ledger-schema.ts`](src/lib/db/ledger-schema.ts)** — `getLedgerSchemaHealth()` probes `invoices` (ledger columns), `integration_connectors`, `ai_summaries`, and `finance_transactions`, and returns a clear message if anything is missing/wrong.
2. **[`src/components/ops/ledger-schema-banner.tsx`](src/components/ops/ledger-schema-banner.tsx)** — Banner with migration/seed instructions.
3. **[`src/app/dashboard/page.tsx`](src/app/dashboard/page.tsx)** — Run schema health first; on load failure, show the **actual** error string (not only a generic line).
4. **[`src/app/finance/page.tsx`](src/app/finance/page.tsx)** — Same health gate + surface finance summary load errors.
5. **[`src/app/integrations/page.tsx`](src/app/integrations/page.tsx)** — Schema gate; **removed** the `.catch(() => [])` pattern so real errors surface; empty connectors only when the query succeeds but returns no rows.
6. **[`package.json`](package.json)** — `"db:check": "node scripts/repro-dashboard-data.mjs"` to re-verify the DB anytime.
7. **[`scripts/repro-dashboard-data.mjs`](scripts/repro-dashboard-data.mjs)** — Repro helper kept for local checks.

After you apply **`0001_core_ledger.sql`**, **`002_invoice_reminders.sql`**, and **`supabase/seed.sql`** to the **same** project as `.env.local`, the dashboard and integrations should load. If an old `invoices` table blocks migration, you may need a clean reset or a manual reconcile in Supabase (that’s a data-op step, not something the app can safely guess).

<reproduction_steps>
1. Restart `npm run dev` so the server picks up the latest code.
2. Run `npm run db:check` in the repo root and confirm invoices use ledger columns and core tables exist (no PostgREST errors in the output).
3. In the Supabase project tied to `.env.local`, apply migrations `supabase/migrations/0001_core_ledger.sql` and `002_invoice_reminders.sql`, then run `supabase/seed.sql` (or `supabase db reset` on a disposable project).
4. Open `/dashboard`, `/finance`, and `/integrations` — you should see the amber schema banner only if a check still fails; otherwise real KPIs and connectors from seed.
5. Press Proceed/Mark as fixed when done.
</reproduction_steps>

[REDACTED]

**Tool calls:**

- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/dashboard.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/finance.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/env.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/finance.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/db/supabase-server.ts`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/scripts/repro-dashboard-data.mjs`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && node scripts/repro-dashboard-data.mjs`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/scripts/repro-dashboard-data.mjs`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && node scripts/repro-dashboard-data.mjs`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/db/ledger-schema.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `Write` — `/home/anant_gupta/projects/hackathon/opspilot/src/components/ops/ledger-schema-banner.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/package.json`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && npm run build 2>&1`
- `Delete` — `/home/anant_gupta/projects/hackathon/opspilot/.cursor/debug-b0a213.log`

## You

<user_query>
Issue reproduced, please proceed.
</user_query>

## Cursor

Verifying the codebase state and whether anything remains to proceed with after your reproduction.

[REDACTED]

DB check still shows the linked Supabase project on the legacy `invoices` shape (no ledger columns; missing `integration_connectors` / `ai_summaries`). Proceeding by sharpening schema-detection messages and the `db:check` script output so the next step is unmistakable.

[REDACTED]

[REDACTED]

[REDACTED]

Here is where things stand after proceeding.

### Runtime evidence (current workspace)

`npm run db:check` still reports:

- `invoices`: missing ledger columns (`invoice_number`, `total_amount`, …); sample row still has legacy fields (`total`, `line_items`, …).
- Missing tables: `integration_connectors`, `ai_summaries`.

So the **issue is not a remaining app bug** in the dashboard query path—it is the **Supabase project schema** not matching [`0001_core_ledger.sql`](supabase/migrations/0001_core_ledger.sql) (plus [`002_invoice_reminders.sql`](supabase/migrations/002_invoice_reminders.sql) and seed). The UI work from before (schema banner + real errors + integrations not swallowing errors) is the correct behavior until that migration work is done.

### What I just changed

- **[`src/lib/db/ledger-schema.ts`](src/lib/db/ledger-schema.ts)** — If PostgREST complains about `organization_id`, `invoice_number`, `total_amount`, or `amount_paid`, the message now explicitly calls out the **pre-ledger** `total` / `line_items` situation and that you must not mix shapes in one table.
- **[`scripts/repro-dashboard-data.mjs`](scripts/repro-dashboard-data.mjs)** — Prints a short **next step** line after the checks (SQL Editor / `supabase db push`).

There is **no** `127.0.0.1:7743` debug instrumentation in the repo (grep is clean), so nothing to strip for “instrumentation cleanup.”

### What you need for the dashboard to show real data

Apply **this repo’s** migrations and seed to the **same** Supabase project as `.env.local`. Until `db:check` runs clean, the app will correctly block or explain instead of failing silently.

<reproduction_steps>
1. Restart `npm run dev` so you load the latest server bundle.
2. Run `npm run db:check` and confirm the final “=>” line; errors should match what Supabase still lacks.
3. In the Supabase dashboard for the project in `.env.local`, run `0001_core_ledger.sql`, then `002_invoice_reminders.sql`, then `supabase/seed.sql` (or use `supabase link` + `supabase db push` / `db reset` on a throwaway project if you prefer the CLI).
4. Run `npm run db:check` again until all probes report `ok` with no PostgREST errors.
5. Reload `/dashboard`, `/finance`, and `/integrations` — you should see data (or the amber schema banner only if a probe still fails).
6. Press Proceed/Mark as fixed when this matches what you expect.
</reproduction_steps>

[REDACTED]

**Tool calls:**

- `Grep` — pattern `127\.0\.0\.1:7743|agent log|debug-b0a213`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && npm run db:check 2>&1`
- `Delete` — `/home/anant_gupta/projects/hackathon/opspilot/.cursor/debug-b0a213.log`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/db/ledger-schema.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/db/ledger-schema.ts`
- `StrReplace` — `/home/anant_gupta/projects/hackathon/opspilot/scripts/repro-dashboard-data.mjs`
- `Shell` — `cd /home/anant_gupta/projects/hackathon/opspilot && npm run build 2>&1`

## You

<user_query>
The issue has been fixed. Please clean up the instrumentation.
</user_query>

## Cursor

Searching the codebase for debug instrumentation to remove.

[REDACTED]

[REDACTED]

There isn’t any leftover debug instrumentation in this repo from that work.

What I checked:

- No `fetch` calls to the debug ingest URL, no `X-Debug-Session-Id`, no `#region agent log`, no `hypothesisId`, no references to `debug-b0a213` or `7743`.
- The Phase-2 session never landed temporary NDJSON/fetch loggers in `src/`; only normal product behavior (schema health, error text on failed loads) was added.

What **is** still there on purpose (not debug instrumentation):

- [`scripts/repro-dashboard-data.mjs`](scripts/repro-dashboard-data.mjs) and `npm run db:check` in [`package.json`](package.json) — small **ops** helper to verify the linked Supabase schema, same as before.

If you want that script and the `db:check` npm script removed as well, say so and I can strip them; otherwise there’s nothing to delete for “instrumentation cleanup.”

[REDACTED]

**Tool calls:**

- `Grep` — pattern `7743|ingest/|hypothesisId|agent log|#region agent|debug-b0a213|DEBUG|instrument`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Grep` — pattern `console\.(log|debug|warn)\(`, path `/home/anant_gupta/projects/hackathon/opspilot/src`
- `Grep` — pattern `fetch\(.*ingest|X-Debug-Session`, path `/home/anant_gupta/projects/hackathon/opspilot`

## Actions Taken
- Summary: There isn’t any leftover debug instrumentation in this repo …
- Files changed (Cursor): 33
- Lines: +1165 / -371
- Files touched (from tool calls): /home/anant_gupta/projects/hackathon/opspilot, /home/anant_gupta/projects/hackathon/opspilot/src/lib/env.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/db/supabase-server.ts, /home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/0001_core_ledger.sql, /home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/001_scheduling_invoices.sql, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/finance.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/invoices.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/[id]/mark-paid/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/appointments.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/invoice.service.ts, /home/anant_gupta/projects/hackathon/opspilot/supabase/seed.sql, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/dashboard/summary/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/dashboard.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase/index.ts, /home/anant_gupta/projects/hackathon/opspilot/package.json, /home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/integrations.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/finance/page.tsx, /home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx, /home/anant_gupta/projects/hackathon/opspilot/src/lib/constants/enums.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/finance.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/generate/route.ts, /home/anant_gupta/projects/hackathon/opspilot/supabase/migrations, /home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase/client.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/invoices/[id]/remind/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/supabase/queries.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/ai/generate-reminder.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/types.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard, /home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/reservation.service.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/follow-ups/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib, /home/anant_gupta/projects/hackathon/opspilot/src/lib/types/index.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/dashboard.ts, /home/anant_gupta/projects/hackathon/opspilot/supabase/archived/001_scheduling_invoices_legacy.sql, /home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/002_invoice_reminders.sql, /home/anant_gupta/projects/hackathon/opspilot/tsconfig.json, /home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/invoice.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/integrations/webhook-guard.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/cron/mark-overdue-invoices/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/ai.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/ai/manager-summary/route.ts, /home/anant_gupta/projects/hackathon/opspilot/vitest.config.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/integrations.test.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.domain.test.ts, /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/terminals/58363.txt, /home/anant_gupta/projects/hackathon/opspilot/scripts/repro-dashboard-data.mjs, /home/anant_gupta/projects/hackathon/opspilot/src/lib/db/ledger-schema.ts, /home/anant_gupta/projects/hackathon/opspilot/src/components/ops/ledger-schema-banner.tsx, /home/anant_gupta/projects/hackathon/opspilot/.cursor/debug-b0a213.log, /home/anant_gupta/projects/hackathon/opspilot/src
- Commands run: cd /home/anant_gupta/projects/hackathon/opspilot && git status -sb && git fetch origin 2>&1 && git rev-parse HEAD && git rev-parse origin/main 2>/dev/null; git merge-base HEAD origin/main 2>/dev/null; git log --oneline -5, cp /home/anant_gupta/projects/hackathon/opspilot/supabase/migrations/001_scheduling_invoices.sql /home/anant_gupta/projects/hackathon/opspilot/supabase/archived/[REDACTED].sql, cd /home/anant_gupta/projects/hackathon/opspilot && npm install && npm run test && npm run build, cd /home/anant_gupta/projects/hackathon/opspilot && npm run build && npm run lint, pkill -f "next build" 2>/dev/null; sleep 2; cd /home/anant_gupta/projects/hackathon/opspilot && rm -f .next/lock 2>/dev/null; npm run build && npm run lint, cd /home/anant_gupta/projects/hackathon/opspilot && npm run build 2>&1, cd /home/anant_gupta/projects/hackathon/opspilot && npm run lint 2>&1, cd /home/anant_gupta/projects/hackathon/opspilot && node scripts/repro-dashboard-data.mjs, cd /home/anant_gupta/projects/hackathon/opspilot && npm run db:check 2>&1
- Tool call tally: CreatePlan (1), Delete (6), Glob (13), Grep (17), Read (68), Shell (13), StrReplace (49), TodoWrite (3), Write (17)

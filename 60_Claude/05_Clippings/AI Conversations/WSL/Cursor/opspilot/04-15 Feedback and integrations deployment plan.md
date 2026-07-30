---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: wsl
title: "Feedback and integrations deployment plan"
started_at: 2026-04-15T00:35:04
ended_at: 2026-04-15T01:22:44
exported_at: 2026-07-30T19:59:46
project: opspilot
cwd: "/home/anant_gupta/projects/hackathon/opspilot"
session_id: 22bb7cfb-b0d4-47ef-8ef0-773f006d4d66
status: raw
turn_count: 4
tools_used:
  ApplyPatch: 12
  CreatePlan: 1
  Glob: 12
  Grep: 5
  Read: 24
  ReadFile: 21
  ReadLints: 1
  Shell: 8
  TodoWrite: 7
files_touched:
  - "/home/anant_gupta/projects/hackathon/opspilot/.claude/PRD.md"
  - "/home/anant_gupta/projects/hackathon/opspilot"
  - "/home/anant_gupta/projects/hackathon/opspilot/.claude"
  - "/home/anant_gupta/projects/hackathon/opspilot/.claude/decisions/decision-log.md"
  - "/home/anant_gupta/projects/hackathon/opspilot/.claude/context/current-state.md"
  - "/home/anant_gupta/projects/hackathon/opspilot/src"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/integrations/webhook-guard.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/integrations.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/dashboard.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/feedback.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/feedback/page.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/review"
  - "/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/review/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/components/feedback/review-actions.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/dashboard.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/vercel.json"
  - "/home/anant_gupta/projects/hackathon/opspilot/.env.example"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/integrations/webhook-domain.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations"
  - "/home/anant_gupta/projects/hackathon/opspilot/package.json"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/feedback.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/supabase"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.domain.test.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/.agents/skills/supabase/SKILL.md"
  - "/home/anant_gupta/projects/hackathon/opspilot/node_modules/next/dist/docs"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/components/layout/sidebar.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/node_modules/next/dist/docs/01-app/01-getting-started/15-route-handlers.md"
  - "/home/anant_gupta/projects/hackathon/opspilot/supabase/seed.sql"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/services"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/constants/enums.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/lib/db/supabase-server.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/components/ui"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/components/ui/button.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/connectors/[provider]/clear-error/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/components/integrations/clear-connector-error-button.tsx"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/follow-ups/[actionId]/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/[id]/approve-reply/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/[id]/follow-up/route.ts"
  - "/home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/submit/route.ts"
files_changed_count: 10
lines_added: 271
lines_removed: 91
tags:
  - input
  - ai-conversation
  - cursor
  - wsl
---

# Feedback and integrations deployment plan

## You

[Image]
[Image]
[Image]
[Image]
[Image]
[Image]
<image_files>
The following images were provdied by the user and saved to the workspace for future use:
1. /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/assets/[REDACTED].png
2. /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/assets/[REDACTED].png
3. /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/assets/[REDACTED].png
4. /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/assets/[REDACTED].png
5. /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/assets/[REDACTED].png
6. /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/assets/[REDACTED].png

These images can be copied for use in other locations.
</image_files>
<user_query>
Use this repo’s current state, not the stale early-phase plan, and produce an execution-ready implementation plan for the next phase focused only on **Feedback** and **Integrations/MCP bridge**, plus the dashboard/UI work directly required to support those two components.

Important context before you start:

* The project already has a Supabase-first core ledger foundation, deterministic finance services, query modules, route handlers, and a partially implemented MCP bridge. Do not restart those from scratch.
* The current MCP bridge in this repo means **connector normalization + webhook ingestion + dispatch into the same domain services as first-party routes**. It does **not** mean blockchain or wallet bridging.
* Feedback work has already progressed beyond the old “missing migration” stage. Do not blindly recreate stale plan items if the repo already implements them in a newer way.
* AI must remain downstream of deterministic business logic. It may draft, classify, summarize, and recommend. It must not directly own finance truth, workflow truth, or outbound side effects unless explicitly approved.
* We are trying to deploy soon, so prioritize completion, cleanup, and deployment safety over broad new abstractions.

Product decision to respect:

* We have decided to remove the **MCP bridge card** from the dashboard because integrations can be accessed through the Integrations page.
* However, the current PRD says the dashboard should surface an MCP bridge/connectors panel and treats removing it as a regression unless the PRD is formally updated.
* Therefore, before implementation, verify whether the repo already contains a PRD/decision-log update for this change.
* If not, include the smallest necessary append-only PRD or decision-log clarification so the product spec matches the new dashboard decision. Do not leave the code and PRD in conflict.

Your job:
Analyze all relevant updated `.md` files, the current repo state, and all already-implemented work for Feedback and Integrations. Then produce a **detailed execution plan** and, once the plan is approved, implement the missing work to bring these two components to deployment-ready status with minimal risk.

Scope boundaries:
Focus only on:

1. Feedback
2. Integrations / MCP bridge
3. Dashboard and navigation changes required for those two areas
4. Deployment-readiness tasks directly tied to those components

Do not broaden scope into unrelated inventory, broad finance redesign, or general auth rebuild unless something is directly blocking Feedback/Integrations deployment.

What to analyze first:

* `.claude/PRD.md`
* all recent phase-planning markdown files
* `src/app/feedback/**`
* `src/app/integrations/**`
* `src/app/dashboard/**`
* `src/app/api/review/**`
* `src/app/api/feedback/**`
* `src/app/api/integrations/**`
* `src/app/api/integrations/webhooks/[provider]/route.ts`
* `src/lib/queries/feedback.ts`
* `src/lib/queries/dashboard.ts`
* `src/lib/services/feedback.ts`
* `src/lib/services/integrations.ts`
* `src/lib/schemas/feedback.ts`
* `src/lib/schemas/integrations.ts`
* related migrations and seed files for feedback/integrations
* `vercel.json`
* `.env.example`
* any decision log or implementation-memory docs

What to determine before coding:

1. What is already complete and working for Feedback
2. What is already complete and working for Integrations/MCP
3. What is still partial, risky, or inconsistent
4. What old plan items are now stale and must **not** be reintroduced
5. What dashboard/UI changes are still required after the decision to remove the MCP dashboard card
6. What deployment blockers remain for these components

Specific requirements for Feedback:

* Keep `/feedback` as the home for flagged reviews, recovery drafts, and follow-up actions.
* Verify the current query/data contract end to end:

  * feedback rows
  * follow-up actions
  * approval/dismiss flows
  * seed/reset behavior
  * advisory-only AI analysis behavior
* Confirm seeded/demo feedback states are reset-safe and deterministic.
* Confirm `/api/review` uses the correct current schema and service flow for this repo.
* Confirm the page is driven by real data and not stale mock arrays.
* Improve the Feedback UI where necessary so it feels complete for the demo:

  * clear flagged section
  * clear pending approvals/follow-ups
  * clear state transitions
  * customer context/history where already supported
  * obvious manager actions
* Identify anything still missing from the Feedback acceptance criteria in the PRD and close the gap if it is realistic for this phase.

Specific requirements for Integrations / MCP:

* Finish the MCP bridge as a **credible integration backbone** for the demo.
* The bridge must:

  * validate inbound payloads
  * persist sync events
  * dedupe on `external_event_id`
  * dispatch into the same deterministic services used by first-party APIs
  * update connector health/state
* Harden the webhook/API path:

  * shared secret or signature validation where appropriate
  * local unsigned-dev path only when explicitly allowed
  * replay-safe idempotency
  * structured failure state
  * `last_error` / status visibility
* Move provider-specific logic toward a cleaner adapter/normalization shape only if needed to complete the current providers cleanly.
* Make the Integrations page more useful to the user:

  * clear connector cards/status
  * last sync
  * error state
  * connector actions the user can actually take
  * explanatory bridge copy that feels product-grade, not placeholder
* Since the MCP card is being removed from the dashboard, make sure the Integrations page carries enough value and discoverability to justify that decision.

Specific requirements for Dashboard / Navigation:

* Remove the MCP bridge card from the dashboard only if the product-spec mismatch is resolved via PRD/decision-log update.
* Keep or improve the Feedback spotlight/surface on the dashboard if the PRD still expects Feedback visibility there.
* Ensure the dashboard does not silently lose visibility into important support workflows after the MCP card removal.
* Verify sidebar/navigation still makes Feedback and Integrations one-click accessible and product-clear.
* Do not introduce new dashboard widgets unless they directly improve Feedback or Integrations clarity.

Deployment-readiness requirements:

* Aim for deployable state with 0 build/type/lint errors.
* Run and verify at minimum:

  * `npm run lint`
  * `npx tsc --noEmit`
  * `npm test` or targeted tests if the repo uses targeted test runs
  * `npx next build --webpack`
* Check Vercel-specific deployment readiness for these components:

  * route-handler compatibility
  * env var completeness
  * cron config relevance
  * no accidental reliance on local-only behavior
* Surface every remaining blocker explicitly instead of hiding it.

Output format:

1. **Current-state analysis**

   * Feedback
   * Integrations/MCP
   * Dashboard/nav implications
   * stale plan items to ignore
2. **Gap list**

   * must fix before deploy
   * should fix if time allows
   * intentionally defer
3. **Execution plan**

   * exact order of work
   * files to edit
   * dependencies
   * validation after each step
4. **Implementation**

   * make the actual code/doc changes
5. **Verification report**

   * what passed
   * what remains
   * what to tell teammates before merge/deploy

Non-negotiable constraints:

* Do not reintroduce stale migrations or duplicate tables just because an old plan mentioned them.
* Do not let AI directly send public replies or mutate critical workflow state unless the current repo explicitly supports and approves that behavior.
* Do not leave PRD/spec and shipped UI in conflict.
* Do not add unrelated features outside Feedback/Integrations/dashboard-support scope.
* Do not claim deployment-ready unless lint, typecheck, build, and the relevant routes/pages actually verify cleanly.

Success condition:
When done, Feedback and Integrations should both feel complete, intentional, and demo-ready; the dashboard/navigation should reflect the latest product decision cleanly; and the repo should be in a realistic state to deploy without hidden errors.

</user_query>

## Cursor

Analyzing the repository (read-only): reading the PRD, decision logs, and Feedback/Integrations/Dashboard code to produce an execution-ready plan.

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

Confirming: `decision-log.md` has no entry for removing the dashboard MCP card; `PRD.md` §1.2 and Appendix E still require the dashboard MCP panel. We'll plan append-only PRD + decision-log updates before removing the UI.

[REDACTED]

**Tool calls:**

- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/.claude/PRD.md`
- `Glob` — pattern `**/*{plan,phase,decision,status}*.md`, path `/home/anant_gupta/projects/hackathon/opspilot`
- `Glob` — pattern `**/*.md`, path `/home/anant_gupta/projects/hackathon/opspilot/.claude`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/.claude/decisions/decision-log.md`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/.claude/context/current-state.md`
- `Grep` — pattern `MCP|mcp|bridge|connector`, path `/home/anant_gupta/projects/hackathon/opspilot/src`
- `Glob` — pattern `**/*`, path `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/integrations/webhook-guard.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/integrations.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/dashboard.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/feedback.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/feedback/page.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `Glob` — pattern `**/*`, path `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/review`
- `Grep` — pattern `integration_sync_events|external_event`, path `/home/anant_gupta/projects/hackathon/opspilot/supabase/migrations`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/review/route.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/components/feedback/review-actions.tsx`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/dashboard.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/vercel.json`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/.env.example`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/integrations/webhook-domain.ts`
- `Glob` — pattern `**/*`, path `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/package.json`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/feedback.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/dashboard.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/route.ts`
- `Grep` — pattern `Feedback|Integrations|/feedback|/integrations`, path `/home/anant_gupta/projects/hackathon/opspilot/src`
- `Grep` — pattern `integration_connectors`, path `/home/anant_gupta/projects/hackathon/opspilot/supabase`
- `Grep` — pattern `connector|integration`, path `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/feedback/page.tsx`
- `Glob` — pattern `**/*integrations*.test.ts`, path `/home/anant_gupta/projects/hackathon/opspilot/src`
- `Glob` — pattern `**/*feedback*.test.ts`, path `/home/anant_gupta/projects/hackathon/opspilot/src`
- `Glob` — pattern `**/*webhook*.test.ts`, path `/home/anant_gupta/projects/hackathon/opspilot/src`
- `Read` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.domain.test.ts`
- `CreatePlan` — `{"name":"Feedback Integrations Phase","overview":"Align product docs with the decision to remove the dashboard MCP bridge card, preserve support-workflow visibility via the Feedback spotlight and Integrations route, then close remaining gaps in webhook dispatch validation, Integrations UX (actionabl…`

## You

<user_query>
Feedback, Integrations/MCP, and dashboard support — execution plan

Implement the plan as specified, it is attached for your reference. Do NOT edit the plan file itself.

To-do's from the plan have already been created. Do not create them again. Mark them as in_progress as you work, starting with the first one. Don't stop until you have completed all the to-dos.
</user_query>

## Cursor

Implementing the approved plan now. I’m starting by marking the first todo in progress and loading the Supabase and Next.js guidance I need before touching the Feedback and Integrations code.

I’ve confirmed the spec mismatch is still real and the main code risk is the webhook path silently marking no-op events as processed. Next I’m verifying the feedback action routes and the integrations surface so the edits stay minimal and aligned with the current implementation.

**Planning for updates**

I need to review the next route documentation, especially focusing on route handlers. It might help to look through terminals and check any shell commands too. I can use read tools without a shell to access files. It's important to edit the documentation and code, but I should get user updates before making any major changes. Plus, I might need to read the current feedback API routes and relevant lines from the decision log. Gathering more information before proceeding sounds like a good plan!

I’ve verified the feedback action routes exist and the sidebar already keeps Feedback and Integrations one click away, so I can keep the dashboard change narrow. I’m updating the product docs first so the MCP-card removal is recorded before the UI changes land.

I’ve got the exact PRD and decision-log lines that still conflict with the approved dashboard direction. I’m applying the smallest append-only doc updates now so the implementation stays spec-safe.

The spec is aligned now. I’m removing the dashboard MCP card and preserving connector discoverability with a compact error hint inside the existing Feedback spotlight, using data the dashboard query already already exposes.

**Updating dashboard components**

I'm thinking about editing the dashboard page. I want to remove a card and possibly add a hint inside the feedback spotlight using the existing connectors data. I need to read through everything to ensure I'm not missing anything. I'll use applypatch for making modifications and should patch imports by removing Plug but keeping Arrow. I’m considering calculating the connectorErrorCount, and if there are any errors, adding a hint paragraph with a link. It's important to patch carefully.

The dashboard change is in. I’m hardening the webhook dispatch next so mutating integration events fail clearly instead of being logged as processed when required identifiers are missing.

**Editing integrations**

I need to edit the `integrations.ts` file, and I might want to add a helper that can be exported for the tests. It's good to know I could test this helper without needing a database. I should also read through the whole relevant file around the dispatch to understand what needs to be done. It'll be important to make sure everything is set up properly for testing!

I found the cleanest low-risk fix: move the “can this payload actually dispatch?” checks into a small pure helper, use that before service calls, and cover it with Vitest. That prevents false “processed” rows without introducing a larger adapter refactor.

**Considering integration tests**

I'm thinking about whether to test existing schemas to normalize alternate keys. It might make sense to add a test in the integrations.schema, but maybe not? I'm pondering the idea of focusing on payload normalization while ensuring we preserve `external_event_id` without duplication. It could be beneficial to create a unit test around the route or service as well. There seems to be a lot to consider here!

Webhook dispatch now fails honestly for malformed mutating payloads. I’m finishing the Integrations UX next by replacing the misleading curl example and adding a minimal demo-safe connector reset action for error states.

The Integrations page is the last major surface change. I’m wiring a small server action for clearing seeded connector errors and tightening the copy so the webhook example reflects a path that actually works in this repo.

The Integrations page now reflects the current bridge semantics and has a safe demo reset for seeded connector errors. I’m doing the feedback verification pass now to confirm the action routes and decide whether any small UI polish is still needed before the full verification run.

I’ve verified the feedback routes match the current UI actions, so that pass is effectively complete without extra churn. I’m running lints, typecheck, tests, and a production build now to see whether any repo-level issues remain after these changes.

**Considering build processes**

I’m wondering if I could use parallel lint, tsc, and test—though I know they’re independent but might be heavy. It seems like running them in parallel is an option, but building would likely happen after the others finish. I’ll need to run lint, tsc, and test together, then build sequentially. Also, I might want to check ReadLints for edited files after changes. Plus, I could use Shell with the working directory for updates before running commands.

The new tests passed, but TypeScript surfaced a narrowing issue in `integrations.ts` from the stricter webhook validation. I’m fixing those type-level gaps now and then rerunning the full verification sequence.

**Inspecting TypeScript errors**

I need to fix TypeScript errors in `integrations.ts`, particularly focusing on non-null assertions after validation. It looks like line 416 might be related to the feedback score or customer ID. I think I'll need to inspect the code around those lines to understand the problem better. I’ll use the ReadFile method to take a closer look at the details. Let's see what I can find and how I can resolve it!

TypeScript is only unhappy because it can’t infer the validation helper’s guarantees across branches. I’m making those guarantees explicit inside the branch bodies, then I’ll rerun typecheck and build.

**Fixing validation issues**

I need to address the narrowing issue by assigning non-null checks or assertions properly. While the validationError does ensure there's a presence, TypeScript can't always know that for sure. I'll use local constants in each branch with explicit checks and consider throwing an unreachable error when necessary. There's also a chance that score could be undefined in feedback.received; I might fix it by declaring a safeScore using `score ?? 0`. I should ensure that analyzeAndPersist is ready for a number, so I'll make minimal patches there too.

Typecheck and production build are clean now. I’m doing one final repo status pass and marking the last todo complete before I hand back the verification report.

## Current-state analysis

Feedback was already substantially complete in the repo, and that held up under verification. The `/feedback` page is driven by `listFeedbackQuery()` against real Supabase `feedback` and `follow_up_actions` rows rather than stale mock arrays, and the current UI action components already matched the route structure under `src/app/api/feedback/**`. The `/api/review` path also already followed the correct pattern for this repo: validate input, resolve customer context, run advisory AI analysis, then persist through the feedback service layer rather than letting AI directly own workflow truth.

Integrations / MCP were also already real, but there was one deployment-risky gap: malformed mutating webhook payloads could be accepted, logged, and end up marked as processed even when they did not include required IDs to actually dispatch into the deterministic services. The Integrations page also had a misleading local `curl` example that looked valid but would not exercise a supported mutation path in practice.

Dashboard and nav were mostly correct, but the repo had a real spec conflict: the codebase still showed the MCP dashboard card, while your product decision was to remove it, and the PRD still said that removing it was a regression. I resolved that conflict first with append-only PRD and decision-log updates, then removed the duplicate dashboard card while preserving visibility through Feedback and Integrations.

## Gap list

### Must-fix items completed

- Recorded the dashboard MCP-card removal in [`/home/anant_gupta/projects/hackathon/opspilot/.claude/decisions/decision-log.md`](/home/anant_gupta/projects/hackathon/opspilot/.claude/decisions/decision-log.md) and aligned the canonical spec in [`/home/anant_gupta/projects/hackathon/opspilot/.claude/PRD.md`](/home/anant_gupta/projects/hackathon/opspilot/.claude/PRD.md).
- Removed the dashboard MCP bridge card and preserved support visibility through the existing Feedback spotlight plus an integrations error hint.
- Hardened webhook dispatch so mutating events now fail closed when required payload fields are missing instead of being recorded as successfully processed.
- Replaced the misleading Integrations `curl` sample with one that matches a supported `feedback.received` flow.
- Added a minimal demo-safe connector error reset action for seeded error states.

### Deferred intentionally

- Real connector OAuth or provider re-auth flows.
- Durable distributed rate limiting for webhook ingress.
- New providers or larger adapter abstractions.
- Any unrelated finance, inventory, or auth expansion.

## Implementation

The spec alignment is now explicit in the docs. In the PRD, the Phase 3 language no longer requires a duplicate MCP card on the dashboard and instead makes `/integrations` the primary connector surface, while keeping Feedback visibility on `/dashboard`. The decision log records that change as a deliberate product choice.

On the dashboard, I removed the MCP bridge card from [`src/app/dashboard/page.tsx`](src/app/dashboard/page.tsx) and kept the support story visible via the existing Feedback spotlight. That card now includes a compact connector-error warning when any integration is in an error state and adds a direct link to `/integrations`, so the dashboard no longer duplicates connector detail but also does not hide support-impacting integration issues.

Webhook handling is now stricter and safer. I introduced payload validation logic in [`src/lib/integrations/webhook-domain.ts`](src/lib/integrations/webhook-domain.ts) and used it from [`src/lib/services/integrations.ts`](src/lib/services/integrations.ts) before dispatching mutating events. That closes the no-op/false-processed gap for events like `reservation.completed`, `invoice.sent`, `invoice.paid`, and `feedback.received`. The route handler at [`src/app/api/integrations/webhooks/[provider]/route.ts`](src/app/api/integrations/webhooks/[provider]/route.ts) now maps those descriptive validation failures to `400` responses instead of misleading `500`s.

The Integrations page is more deployment-credible now. In [`src/app/integrations/page.tsx`](src/app/integrations/page.tsx), I tightened the bridge explanation, replaced the broken curl example with a valid `google_reviews` review-ingest example, and added a demo-safe “Clear demo error” action for connectors in `error` state. That action is backed by a minimal service method in [`src/lib/services/integrations.ts`](src/lib/services/integrations.ts), a small route handler at [`src/app/api/integrations/connectors/[provider]/clear-error/route.ts`](src/app/api/integrations/connectors/[provider]/clear-error/route.ts), and a client button component at [`src/components/integrations/clear-connector-error-button.tsx`](src/components/integrations/clear-connector-error-button.tsx).

I also extended the integration tests in [`src/lib/services/integrations.domain.test.ts`](src/lib/services/integrations.domain.test.ts) to cover the new webhook validation behavior.

## Verification report

Passed:

- `npm run lint`
  - Passed with existing repo warnings only in `src/lib/services/feedback.ingest.test.ts` for unused test parameters. No new lint errors were introduced.
- `npx tsc --noEmit`
  - Passed.
- `npm test`
  - Passed. `20` tests passed, including the new integration validation cases.
- `npm run build`
  - Passed. The production build completed successfully and includes the new route `api/integrations/connectors/[provider]/clear-error`.

Relevant deployment/readiness notes:

- Production still requires `INTEGRATIONS_WEBHOOK_SECRET` for webhook ingress. The repo already documents this correctly in [`.env.example`](/home/anant_gupta/projects/hackathon/opspilot/.env.example).
- The local unsigned webhook path remains limited to non-production behavior via `INTEGRATIONS_WEBHOOK_ALLOW_UNSIGNED` / `NODE_ENV`, which is appropriate for demo/dev use.
- `vercel.json` only contains the overdue-invoice cron and does not introduce any new blocker for Feedback or Integrations.
- The webhook rate limit remains in-memory and therefore non-durable across instances; that is acceptable for this phase but should not be mistaken for a production-grade distributed throttle.

What to tell teammates before merge/deploy:

- The PRD now formally matches the “no MCP dashboard card” product decision.
- Connector detail and local webhook rehearsal now belong on `/integrations`.
- The dashboard still surfaces support urgency through Feedback and now shows a connector-error hint when it matters.
- Malformed mutating webhook payloads now fail clearly instead of being logged as processed.
- The new “Clear demo error” button is only for resetting demo connector state; it does not perform any real provider re-authentication.

**Tool calls:**

- `TodoWrite` — `{"merge":true,"todos":[{"id":"docs-prd-decision","status":"in_progress"},{"id":"dashboard-ui","status":"pending"},{"id":"webhook-dispatch-validate","status":"pending"},{"id":"integrations-ux","status":"pending"},{"id":"feedback-verify","status":"pending"},{"id":"verify-ship","status":"pending"}]}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/.agents/skills/supabase/SKILL.md"}`
- `Glob` — pattern `**/*route*.*`, path `/home/anant_gupta/projects/hackathon/opspilot/node_modules/next/dist/docs`
- `Glob` — pattern `**/*`, path `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/components/layout/sidebar.tsx"}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/node_modules/next/dist/docs/01-app/01-getting-started/15-route-handlers.md","offset":1,"limit":120}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/supabase/seed.sql","offset":290,"limit":60}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/.claude/PRD.md","offset":24,"limit":20}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/.claude/PRD.md","offset":1110,"limit":80}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/.claude/decisions/decision-log.md","offset":1,"limit":80}`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/.claude/decisions/decision-log.md`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/.claude/PRD.md`
- `TodoWrite` — `{"merge":true,"todos":[{"id":"docs-prd-decision","status":"completed"},{"id":"dashboard-ui","status":"in_progress"}]}`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx`
- `TodoWrite` — `{"merge":true,"todos":[{"id":"dashboard-ui","status":"completed"},{"id":"webhook-dispatch-validate","status":"in_progress"}]}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts"}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.domain.test.ts"}`
- `Glob` — pattern `**/*integrations*.ts`, path `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts","offset":1,"limit":260}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts","offset":260,"limit":220}`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/integrations/webhook-domain.ts`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.domain.test.ts`
- `TodoWrite` — `{"merge":true,"todos":[{"id":"webhook-dispatch-validate","status":"completed"},{"id":"integrations-ux","status":"in_progress"}]}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx"}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/lib/constants/enums.ts","offset":1,"limit":120}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/lib/db/supabase-server.ts","offset":1,"limit":120}`
- `Glob` — pattern `button.tsx`, path `/home/anant_gupta/projects/hackathon/opspilot/src/components/ui`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/components/ui/button.tsx","offset":1,"limit":120}`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/connectors/[provider]/clear-error/route.ts`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/src/components/integrations/clear-connector-error-button.tsx`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx`
- `TodoWrite` — `{"merge":true,"todos":[{"id":"integrations-ux","status":"completed"},{"id":"feedback-verify","status":"in_progress"}]}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/follow-ups/[actionId]/route.ts"}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/[id]/approve-reply/route.ts"}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/[id]/follow-up/route.ts"}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/submit/route.ts","offset":1,"limit":200}`
- `TodoWrite` — `{"merge":true,"todos":[{"id":"feedback-verify","status":"completed"},{"id":"verify-ship","status":"in_progress"}]}`
- `ReadLints` — `{"paths":["/home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx","/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts","/home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx","/home/anant_gupta/projects/hackathon/opspilot/src/lib/i…`
- `Shell` — `ls "/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/terminals"`
- `Shell` — `npm run lint`
- `Shell` — `npx tsc --noEmit`
- `Shell` — `npm test`
- `Shell` — `npm run build`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts","offset":318,"limit":120}`
- `ReadFile` — `{"path":"/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts","offset":400,"limit":40}`
- `ApplyPatch` — `/home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts`
- `Shell` — `npx tsc --noEmit`
- `Shell` — `npm run build`
- `TodoWrite` — `{"merge":true,"todos":[{"id":"verify-ship","status":"completed"}]}`
- `Shell` — `git status --short`

## Actions Taken
- Summary: Edited integrations.ts, page.tsx, clear-connector-error-button.tsx, route.ts, integrations.domain.test.ts
- Files changed (Cursor): 10
- Lines: +271 / -91
- Files touched (from tool calls): /home/anant_gupta/projects/hackathon/opspilot/.claude/PRD.md, /home/anant_gupta/projects/hackathon/opspilot, /home/anant_gupta/projects/hackathon/opspilot/.claude, /home/anant_gupta/projects/hackathon/opspilot/.claude/decisions/decision-log.md, /home/anant_gupta/projects/hackathon/opspilot/.claude/context/current-state.md, /home/anant_gupta/projects/hackathon/opspilot/src, /home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard, /home/anant_gupta/projects/hackathon/opspilot/src/app/dashboard/page.tsx, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/webhooks/[provider]/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/integrations/webhook-guard.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/integrations.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/dashboard.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/queries/feedback.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/feedback/page.tsx, /home/anant_gupta/projects/hackathon/opspilot/src/app/integrations/page.tsx, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/review, /home/anant_gupta/projects/hackathon/opspilot/supabase/migrations, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/review/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/components/feedback/review-actions.tsx, /home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/dashboard.ts, /home/anant_gupta/projects/hackathon/opspilot/vercel.json, /home/anant_gupta/projects/hackathon/opspilot/.env.example, /home/anant_gupta/projects/hackathon/opspilot/src/lib/integrations/webhook-domain.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations, /home/anant_gupta/projects/hackathon/opspilot/package.json, /home/anant_gupta/projects/hackathon/opspilot/src/lib/schemas/feedback.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/route.ts, /home/anant_gupta/projects/hackathon/opspilot/supabase, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/ai-summaries.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services/integrations.domain.test.ts, /home/anant_gupta/projects/hackathon/opspilot/.agents/skills/supabase/SKILL.md, /home/anant_gupta/projects/hackathon/opspilot/node_modules/next/dist/docs, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback, /home/anant_gupta/projects/hackathon/opspilot/src/components/layout/sidebar.tsx, /home/anant_gupta/projects/hackathon/opspilot/node_modules/next/dist/docs/01-app/01-getting-started/15-route-handlers.md, /home/anant_gupta/projects/hackathon/opspilot/supabase/seed.sql, /home/anant_gupta/projects/hackathon/opspilot/src/lib/services, /home/anant_gupta/projects/hackathon/opspilot/src/lib/constants/enums.ts, /home/anant_gupta/projects/hackathon/opspilot/src/lib/db/supabase-server.ts, /home/anant_gupta/projects/hackathon/opspilot/src/components/ui, /home/anant_gupta/projects/hackathon/opspilot/src/components/ui/button.tsx, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/integrations/connectors/[provider]/clear-error/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/components/integrations/clear-connector-error-button.tsx, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/follow-ups/[actionId]/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/[id]/approve-reply/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/[id]/follow-up/route.ts, /home/anant_gupta/projects/hackathon/opspilot/src/app/api/feedback/submit/route.ts
- Commands run: ls "/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hackathon-opspilot/terminals", npm run lint, npx tsc --noEmit, npm test, npm run build, git status --short
- Tool call tally: ApplyPatch (12), CreatePlan (1), Glob (12), Grep (5), Read (24), ReadFile (21), ReadLints (1), Shell (8), TodoWrite (7)

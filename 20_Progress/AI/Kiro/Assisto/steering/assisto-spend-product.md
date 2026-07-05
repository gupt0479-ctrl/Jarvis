---
inclusion: auto
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Kiro/Assisto/Setup]]"
---

# Assisto-Spend Product Scope

## What It Is

Assisto-Spend is an enterprise spend workflow module inside the real Assisto app at `/spend`. It replaces spreadsheet-driven procurement, travel, and expense tracking with governed workflows.

## Core Flows

- **PR** (Procurement Request): request → approval → line approval → partial approval → PO eligibility
- **TR** (Travel Request): request → approval → manual travel-admin tasks (no automated booking)
- **TE** (Travel Expense): receipt evidence → mock OCR → duplicate detection → finance decisions → reimbursement state
- **Control Tower**: role-aware dashboard with actions, risks, SLA, KPIs, planned-vs-actual, Spend Trace
- **Admin**: policy thresholds, simulator, master data, migration map, immutable snapshots
- **Reports**: 13+ required reports with strict CSV allow-lists

## Non-Goals (Postponed)

- Real payment execution or ERP posting
- Corporate card feeds
- Automated travel booking or ticketing provider APIs
- Real OCR provider (mock OCR first)
- Advanced fraud scoring
- Complex delegation calendars
- Full tax engine
- Production auth hardening beyond MVP demo actors

## Architecture Facts

- Real app: Next.js 15 App Router, React 19, JavaScript landing page
- Spend module: TypeScript under `src/app/spend/` (after dependency phase)
- NOT Lovable, NOT TanStack Start, NOT a prototype repo
- Lovable `gupta-builds/spend-control` is reference-only for concepts
- Backend correctness comes before UI polish

## Canonical Docs

- Product scope: `docs/assisto-spend/01-product-scope.md`
- Build plan: `docs/assisto-spend/00-real-repo-build-plan.md`
- Implementation phases: `docs/assisto-spend/11-implementation-phases.md`
- Agent contracts: `docs/assisto-spend/agent-build/`

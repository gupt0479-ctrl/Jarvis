---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - sanity
  - content
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[02 - Sanity as Single Source of Truth]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Sanity Content Spec
Real content to push, pulled from the Jarvis vault. No filler. **Field names reconciled to the live schema per [[10 - Codebase Reality & Confusion Clearance]]** (githubUrl, technologies[]/skills[], percentage/proficiency/tone, no color, no skillCategory doc).

> **GitHub URLs:** resolve each `githubUrl` via `mcp__github__search_repositories` by project name in Phase 0; if no match, leave empty and flag for Anant. Never invent. **Live URLs (`liveUrl`):** mostly broken/undeployed — leave empty; the carousel hides "View Live" when empty. **Use `pnpm typegen` after the `summary` + education-`logo` schema touches.**

---
## 1. Categories & colours
Two colour systems now (2026-06-13):
- **Category colours** (`CATEGORY_COLORS`, in code) drive the **graph lines** in the Skills section. There is no `skillCategory` document — `category` is a string enum.
- **Per-skill `color`** (NEW Sanity field, preset palette) drives the **dot/chip next to each skill** everywhere it appears (Experience, Projects, Certifications) — but NOT inside the Skills section (there only the hover effect + level show). Falls back to the skill's category colour when unset.

This table is the category→line-colour reference (lives in `SkillsSectionClient.tsx`):

| category enum | graph/line colour | used as |
|---|---|---|
| `ai-ml` | violet `#A78BFA` | default-open category, top graph line |
| `backend` | emerald `#34D399` | |
| `database` | sky `#38BDF8` | ("data systems" in the brief = this) |
| `frontend` | pink `#F472B6` | |
| `devops` | amber `#FBBF24` | |
| `soft-skills` | orange `#FB923C` | |
| `cloud` / `tools` / `testing` / `design` / `mobile` / `other` | keep existing CATEGORY_COLORS | minor categories |

If the current `CATEGORY_COLORS` already defines these, keep them — don't churn. The point is uniformity, not these exact hexes.

## 2. `skill` documents (real schema fields)
Each: `name`, `category` (enum above), `proficiency` (beginner/intermediate/advanced/expert), `percentage` (0–100, drives the graph), `yearsOfExperience`, **`color`** (NEW preset: violet/cyan/emerald/sky/pink/amber/orange/slate — drives the dot). Default each skill's `color` to its category's colour (ai-ml→violet, backend→emerald, database→sky, frontend→pink, devops→amber, soft-skills→orange) and override individually where a distinct dot is wanted. `tone` is retired as a colour source. Honest levels — many intermediate; the graph shows climbing, not mastery.

**ai-ml** — LLM APIs (advanced, 82), Prompt Engineering (advanced, 80), RAG/Embeddings (intermediate, 68), Agent/Tool Systems (intermediate, 70), Eval & Observability (intermediate, 60), TensorFlow (beginner, 45)
**backend** — TypeScript (advanced, 85), Node.js (advanced, 80), Python (advanced, 80), Rust (intermediate, 58), Zod (advanced, 78), REST API Design (advanced, 80)
**database** — PostgreSQL/Supabase (advanced, 80), Drizzle ORM (intermediate, 62), MongoDB (intermediate, 60), Redis (intermediate, 55), Data Pipelines (intermediate, 65)
**frontend** — React (advanced, 82), Next.js (advanced, 82), Tailwind CSS (advanced, 80), Three.js/WebGL (intermediate, 55), Framer Motion (intermediate, 64), shadcn/ui (advanced, 75), Sanity CMS (advanced, 78)
**devops** — Git/GitHub (advanced, 80), Docker (intermediate, 60), Vercel (advanced, 75), AWS (intermediate, 52), Linux (advanced, 75)
**soft-skills** — Scoping under pressure (advanced, 80), Technical communication (advanced, 78), Mentorship/leadership (intermediate, 68), Research collaboration (intermediate, 65)

Set `tone` to `highlight`/`accent` for the few flagship skills (LLM APIs, TypeScript, Next.js, PostgreSQL) so the UI can weight them; rest `neutral`. Tune `percentage` freely — it's the curve, not a claim.

## 3. `project` documents
Fields: `title`, `slug`, `tagline` (one-liner), **`summary`** (long-form, NEW field — the hover detail), `technologies[]`→skill refs (**render ≤4**), **`githubUrl`**, `liveUrl`, `coverImage` (**now OPTIONAL** — requirement removed), `category` (enum: web-app/ai-ml/api-backend/…), `featured` (bool — `visibility` enum removed), `order`. Order featured first.

### OpsPilot — `featured: true` · category `ai-ml`
- **slug:** `opspilot` · **githubUrl:** resolve · **liveUrl:** empty
- **tagline:** AI restaurant-operations dashboard where AI advises and deterministic services own the money.
- **technologies[]:** Next.js, React, TypeScript, PostgreSQL, Zod, LLM APIs, REST API Design
- **summary:** A full-stack ops dashboard for a single-location restaurant manager built around one connected workflow — reservation completed → invoice generated → invoice paid → finance row created → review analyzed → follow-up surfaced. The design thesis is the point: AI sits only where language tasks live (summaries, review-sentiment analysis, recovery drafting, prioritisation) while deterministic service-layer logic owns every financial mutation — invoice totals, status transitions, ledger writes. Built on Next.js route handlers delegating to typed services over Supabase Postgres with migrations, seed data, idempotent mark-paid flows, and webhook ingestion with dedupe. Demonstrates that credible AI products keep AI downstream of a trustworthy deterministic system.
- **case note:** "AI drafts the recovery message; the system owns the ledger."

### Resq — `featured: true` · category `ai-ml`
- **slug:** `resq` · **githubUrl:** resolve · **liveUrl:** empty
- **tagline:** A CFO workspace for founders who can't afford a finance team — deterministic 13-week cash forecasting with AI strictly advisory.
- **technologies[]:** Next.js, React, TypeScript, PostgreSQL, Drizzle ORM, Zod, LLM APIs, AWS, Docker
- **summary:** A fintech prototype that turns ledger facts into a deterministic 13-week cash-flow forecast, detects the first week cash breaks, and ranks CFO-style moves — accelerate collections, defer payments, cut expenses, explore bridge financing — by impact, speed, risk, and confidence. Core identity: AI summarises, researches, and prioritises but never touches the numbers. The forecast engine is ~350 lines of pure, replayable TypeScript with three scenario modes; every AI action is written to an audit trail with SHA-256 hash chaining; external research runs through a TinyFish client with explicit mock/live/misconfigured/degraded modes so the demo is always safe. Pivoted from OpsPilot to sharpen from "general SMB ops" to "cash survival."
- **case note:** "Shows the exact week cash breaks — and what action buys the most time."

### SafeReach — `featured: true` · category `ai-ml`
- **slug:** `safereach` · **githubUrl:** resolve · **liveUrl:** empty
- **tagline:** Disaster-warning and visit-prep tooling built for people with disabilities, who face compounded risk in emergencies.
- **technologies[]:** React, Next.js, TypeScript, Python, LLM APIs, REST API Design
- **summary:** An AIIS MedTech hackathon build addressing a concrete gap: during natural disasters, individuals with disabilities face two layers of risk — the event and warning systems not built for them. SafeReach does one workflow well instead of broad coverage, pairing clear time-pressured alerting with an accessibility-first interface and an AI layer for plain-language guidance on what to do next. A study in scoping a socially-meaningful product down to one defensible hero flow under hackathon constraints.
- **case note:** "One accessible hero flow beats ten half-built features under pressure."

### Nextgen AI Portfolio Agent — `featured: true` · category `ai-ml`
- **slug:** `ai-portfolio-agent` · **githubUrl:** resolve · **liveUrl:** this site
- **tagline:** A grounded, tool-using agent ("Orby") that operates this portfolio — answers only from real content, navigates the visitor, can't be jailbroken.
- **technologies[]:** LLM APIs, Prompt Engineering, Agent / Tool Systems, RAG / Embeddings, Eval & Observability, Next.js, TypeScript, Redis
- **summary:** Not "RAG but better" — a different shape. The model doesn't just describe the portfolio, it operates it through a small closed set of validated tools (navigate, show project, show experience, look up fact, contact), and every factual claim is grounded in Sanity content or refused. Built in layers: a single-route agent runtime, a context engine that injects a live Sanity catalogue per turn, four system-prompt personas, origin-locked + HMAC-cookie + rate-limited access, a Groq fallback router with a degraded mode, and a promptfoo eval suite gating grounding, refusal, injection, and persona-warmth. Runs free and is designed to be impossible to embarrass. (See the `nextgen-chatbot/` plan.)
- **case note:** "Every claim is grounded in real data or refused — by design."

### Jarvis — Personal Knowledge OS · `featured: false` · category `ai-ml`
- **slug:** `jarvis-os` · **githubUrl:** resolve / may be private · **liveUrl:** empty
- **tagline:** A vault-based operating system that drives AI agents to build, plan, and maintain real software from structured notes.
- **technologies[]:** Prompt Engineering, Agent / Tool Systems, Linux, Git / GitHub, Technical communication
- **summary:** A personal knowledge and automation system on Obsidian + MCP servers, where detailed design notes are the source of truth that AI coding agents read to implement features one phase at a time. The same kit-driven method that produced the nextgen chatbot drives this portfolio's frontend. Demonstrates context engineering at the workflow level: thin agent instructions, leaf-not-tree reads, per-phase clean contexts, verifiable build gates.
- **case note:** "Design in the vault, build in the terminal — agents read, they don't re-derive."

### Arc — Learning Tracker · `featured: false` · category `web-app`
- **slug:** `arc-learning-tracker` · **githubUrl:** resolve · **liveUrl:** empty
- **tagline:** A tool for tracking and structuring self-directed learning.
- **technologies[]:** React, Next.js, TypeScript, Tailwind CSS
- **summary:** A learning-tracker app for turning scattered study into a structured, reviewable trajectory. (Anant: expand scope/status when ready — kept concise to avoid overclaiming.)

> Add other genuinely-built vault projects (e.g. a TradingView/Stocks AI hub) in this same shape only when real.

## 4. `experience` documents (real fields)
Fix the gaps: render the Portable Text `description` (currently fetched, not shown), keep `responsibilities[]` (≤3) and `achievements[]` (≤2, recolour off green), `technologies[]`→skill refs (≤4 chips), `companyWebsite` (not companyUrl), `companyLogo`, `employmentType`, `tenure`.

- **Research Assistant — University of Minnesota** · contract · Minneapolis, MN · 2025-05 → present (tenure: current) · technologies: Python, Rust, MongoDB, Redis, Docker, Data Pipelines · responsibilities: develop Python & Rust APIs for astronomical alert-brokering on BOOM; build real-time event tracking & observability for Linux data pipelines; design structured ingestion APIs for large observational datasets · achievements: contributed to BOOM alert-brokering infra for astronomical event streams; designed analytics-ready ingestion pipelines · description (Portable Text): a short paragraph on the BOOM project and the deterministic-pipeline focus.
- **Full Stack Development Intern — NSP** · internship · Bangalore, India · 2025-05 → 2025-08 · technologies: Next.js, React, Tailwind CSS, TypeScript · responsibilities: develop Assisto (production ed-tech platform); integrate Strapi CMS APIs; build reusable performant accessible SEO UI · achievements: shipped Assisto supporting early onboarding; established reusable component patterns · companyWebsite + companyLogo where available.
- **Web Developer — TechLit** · freelance · Texas, US · 2021-06 → 2022-06 · technologies: Python, React, Git/GitHub · responsibilities/achievements as in the current render.
- **Entrepreneur — Freelance** · freelance · Remote · 2026-05 → present · keep "Coming soon" placeholder until real.

## 5. `education` (content correct; UI-only + one query fix)
Blobs already render by sort index in `EducationFlowchart.tsx` (stable/forming/amoeba). **The only data fix: add `logo` to `EDUCATION_QUERY`.** Content stays: College (UMN, B.S. CS, 2024→present, GPA 3.4), High School (CBSE, Sri Chaitanya, 2022→2024, GPA 3.8), Middle School (ICSE, Ryan International, 2018→2021, GPA 4/4). No `stage` field — index logic owns it.

## 6. `certification`
Uses `skills[]` (not technologies[]). **Delete the fake AWS/GCP/CKA/TensorFlow/MongoDB certs in Studio — Anant does not hold them.** Section returns `null` when empty. For each genuinely-held cert, populate `credentialUrl` (the out-link), `issuer`, `issueDate`, `expiryDate`, `credentialId`, `skills[]` refs. Ask Anant which are real; invent none.

## Done conditions
- Skill docs match real fields (no color, percentage/proficiency/tone); chips colour via category.
- Real projects loaded with `githubUrl` (GitHub-resolved), `summary` populated, `technologies[]` refs, filler removed.
- Experience wired incl. Portable Text description; education query gains `logo`; fake certs deleted.

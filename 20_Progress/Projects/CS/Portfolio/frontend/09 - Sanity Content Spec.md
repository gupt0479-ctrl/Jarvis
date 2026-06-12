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
---
# Sanity Content Spec
The real content to push to Sanity, pulled from the Jarvis vault. No "Alex Morgan," no Lovable filler. Anant optimizes after; this is the professional first pass. Schema shape is in [[02 - Sanity as Single Source of Truth]]; this note is the data.

> **GitHub URLs:** repos exist but exact slugs aren't recorded here. In Phase 0, Claude Code resolves each `repoUrl` against Anant's GitHub via the github MCP (match by project name) and fills it; if no match, leave empty and flag for Anant. Never invent a URL. **Live URLs:** mostly broken/undeployed — leave empty unless verified; the carousel hides "View Live" when empty.

---
## 1. `skillCategory` registry
The lines on the capability graph and the floating buttons. `defaultOpen` = the one shown first.

| name | slug | color | order | defaultOpen | description (shown on click) |
|---|---|---|---|---|---|
| AI / ML | ai-ml | `#A78BFA` (violet) | 1 | ✅ | Applied LLM systems, embeddings, retrieval, agents, and the eval/grounding work that keeps them honest. Where most of my recent depth is. |
| Backend | backend | `#34D399` (emerald) | 2 | | APIs, services, and the deterministic logic that owns money, state, and auditability under the AI layer. |
| Data Systems | data-systems | `#38BDF8` (sky) | 3 | | Schema design, migrations, query/read-models, forecasting engines, and pipelines over real datasets. |
| Frontend | frontend | `#F472B6` (pink) | 4 | | Production React/Next.js with motion, accessibility, and SEO — including this portfolio. |
| DevOps / Tools | devops | `#FBBF24` (amber) | 5 | | Docker, Vercel/AWS deploys, Git workflows, and CI gates that make a build reproducible. |
| Soft Skills | soft-skills | `#FB923C` (orange) | 6 | | Communication, scoping under pressure, mentorship, and turning technical work into a clear story. |

## 2. `skill` registry
Each skill: `name`, `slug`, `category` (ref above), `color` (inherit category color unless noted), `level`, `familiarity` (0–100, drives the graph), short `blurb`. Levels are honest — many are intermediate; the graph shows *climbing*, not mastery.

**AI / ML** (violet)
- LLM APIs (OpenAI/Anthropic/Gemini) — advanced — 82 — "Grounded, tool-using agents with refusal and persona control."
- Prompt Engineering — advanced — 80 — "Context prioritisation, power-prompts, structured outputs."
- RAG / Embeddings — intermediate — 68 — "Retrieval as a tool, not the whole architecture."
- Agent / Tool Systems — intermediate — 70 — "Closed-enum tools, validation, fail-safe-to-text."
- Eval & Observability — intermediate — 60 — "promptfoo suites, tracing, grounding/refusal tests."
- TensorFlow — beginner — 45 — "Coursework-level model building."

**Backend** (emerald)
- TypeScript — advanced — 85 — "Primary language for services and routes."
- Node.js / Next route handlers — advanced — 80 — "Thin handlers delegating to typed services."
- Python — advanced — 80 — "APIs and data work, incl. the BOOM alert-brokering pipeline."
- Rust — intermediate — 58 — "Astronomical alert-brokering APIs on BOOM."
- Zod / schema validation — advanced — 78 — "Validation at every boundary."
- REST API Design — advanced — 80 — "Service-layer boundaries, idempotency."

**Data Systems** (sky)
- PostgreSQL / Supabase — advanced — 80 — "Single source of truth; migrations + seed data."
- Drizzle ORM — intermediate — 62 — "Typed schema for the Resq cash engine."
- MongoDB — intermediate — 60 — "Document modelling on BOOM tooling."
- Redis — intermediate — 55 — "Caching / rate-limit stores."
- Data Pipelines — intermediate — 65 — "Ingestion APIs for large observational datasets."

**Frontend** (pink)
- React — advanced — 82 — "Reusable, accessible component systems."
- Next.js — advanced — 82 — "App Router, RSC, production deploys."
- Tailwind CSS — advanced — 80 — "Design-system-driven styling."
- Three.js / WebGL — intermediate — 55 — "Space-physics motion on this portfolio."
- Framer Motion — intermediate — 64 — "The comet-card / space-float motion language."
- shadcn/ui — advanced — 75 — "Component primitives."
- Sanity CMS — advanced — 78 — "Headless content backbone for this site."

**DevOps / Tools** (amber)
- Git / GitHub — advanced — 80 — "Branching, PR review, CI gates."
- Docker — intermediate — 60 — "Containerised deploys (Resq App Runner)."
- Vercel — advanced — 75 — "Primary deploy target."
- AWS — intermediate — 52 — "App Runner, S3, hackathon infra."
- Linux — advanced — 75 — "WSL dev environment, tooling."

**Soft Skills** (orange)
- Scoping under pressure — advanced — 80 — "One hero flow beats feature breadth."
- Technical communication — advanced — 78 — "Cause-and-effect pitches, case studies."
- Mentorship / leadership — intermediate — 68 — "CSE Student Ambassador; cultural committee."
- Research collaboration — intermediate — 65 — "Faculty-mentored ML research at UMN."

> Tune `familiarity` numbers freely — they're the curve shape, not a claim. Keep AI/ML highest and trending up; keep a couple of categories visibly mid-climb so the graph reads as growth.

---
## 3. `project` content
Order = featured first. Category maps to a `skillCategory` for filtering.

### OpsPilot — featured
- **slug:** `opspilot`
- **tagline:** AI restaurant-operations dashboard where the AI advises and deterministic services own the money.
- **category:** ai-ml · **featured:** yes · **liveUrl:** (empty) · **repoUrl:** resolve from GitHub
- **skills[]:** Next.js, React, TypeScript, Supabase, PostgreSQL, Zod, LLM APIs, REST API Design
- **description:** A full-stack operations dashboard for a single-location restaurant manager. One connected workflow — reservation completed → invoice generated → invoice paid → finance row created → review analyzed → follow-up surfaced. The design principle is the interesting part: AI is placed only where language tasks live (summaries, review-sentiment analysis, recovery drafting, prioritisation), while deterministic service-layer logic owns every financial mutation — invoice totals, status transitions, and ledger writes. Built on Next.js route handlers delegating to typed services over a Supabase Postgres schema with migrations, seed data, idempotent mark-paid flows, and webhook ingestion with dedupe. The lesson it demonstrates: the most credible AI products keep AI downstream of a trustworthy deterministic system.
- **case note (carousel inner box):** "AI drafts the recovery message; the system owns the ledger."

### Resq — featured
- **slug:** `resq`
- **tagline:** A CFO workspace for founders who can't afford a finance team — deterministic 13-week cash forecasting with AI strictly in the advisory layer.
- **category:** ai-ml · **featured:** yes · **liveUrl:** (empty) · **repoUrl:** resolve from GitHub
- **skills[]:** Next.js, React, TypeScript, Supabase, PostgreSQL, Drizzle ORM, Zod, LLM APIs, AWS, Docker
- **description:** A fintech prototype that turns ledger facts into a deterministic 13-week cash-flow forecast, detects the first week cash breaks, and ranks CFO-style moves — accelerate collections, defer payments, cut expenses, explore bridge financing — by impact, speed, risk, and confidence. The core identity is a hard boundary: AI summarises, researches, and prioritises, but never touches the numbers. The forecast engine is ~350 lines of pure, replayable TypeScript with three scenario modes; every AI action is written to an audit trail with SHA-256 hash chaining; external research runs through a TinyFish client with explicit mock/live/misconfigured/degraded modes so the demo is always safe. Pivoted from OpsPilot to sharpen from "general SMB ops" to "cash survival."
- **case note:** "Shows the exact week cash breaks — and what action buys the most time."

### SafeReach — featured
- **slug:** `safereach`
- **tagline:** Disaster-warning and visit-prep tooling built for people with disabilities, who face compounded risk in emergencies.
- **category:** ai-ml · **featured:** yes · **liveUrl:** (empty) · **repoUrl:** resolve from GitHub
- **skills[]:** React, Next.js, TypeScript, Python, LLM APIs, REST API Design
- **description:** An AIIS MedTech hackathon build addressing a concrete gap: during natural disasters, individuals with disabilities face two layers of risk — the event itself and warning systems that aren't built for them. SafeReach focuses on one workflow done well rather than broad feature coverage, pairing clear time-pressured alerting with an accessibility-first interface and an AI layer for plain-language summarisation of what to do next. A study in scoping a socially-meaningful product down to one defensible hero flow under hackathon constraints.
- **case note:** "One accessible hero flow beats ten half-built features under pressure."

### Nextgen AI Portfolio Agent — featured
- **slug:** `ai-portfolio-agent`
- **tagline:** A grounded, tool-using agent ("Orby") that operates this portfolio — answers only from real content, navigates the visitor, and can't be jailbroken or made to invent.
- **category:** ai-ml · **featured:** yes · **liveUrl:** this site · **repoUrl:** resolve from GitHub
- **skills[]:** LLM APIs, Prompt Engineering, Agent / Tool Systems, RAG / Embeddings, Eval & Observability, Next.js, TypeScript, Redis
- **description:** Not "RAG but better" — a different shape. The model doesn't just describe the portfolio, it operates it through a small closed set of validated tools (navigate, show project, show experience, look up fact, contact), and every factual claim is grounded in Sanity content or refused. Built in layers: a single-route agent runtime, a context engine that injects a live Sanity catalogue per turn, four system-prompt personas (recruiter, friend, weirdo, ceo), origin-locked + HMAC-cookie + rate-limited access, a Groq fallback router with a degraded mode, and a promptfoo eval suite gating grounding, refusal, injection, and persona-warmth. Runs free and is designed to be impossible to embarrass.
- **case note:** "Every claim is grounded in real data or refused — by design."

### Jarvis — Personal Knowledge OS
- **slug:** `jarvis-os`
- **tagline:** A vault-based operating system that drives AI agents (Claude Code + Cowork) to build, plan, and maintain real software from structured notes.
- **category:** ai-ml · **featured:** no · **liveUrl:** (empty) · **repoUrl:** resolve from GitHub / private
- **skills[]:** Prompt Engineering, Agent / Tool Systems, Linux, Git / GitHub, Technical communication
- **description:** A personal knowledge and automation system built on Obsidian + MCP servers, where detailed design notes act as the source of truth that AI coding agents read to implement features one phase at a time. The same kit-driven method that produced the nextgen chatbot now drives this portfolio's frontend. Demonstrates context engineering at the workflow level: thin agent instructions, leaf-not-tree reads, per-phase clean contexts, and verifiable build gates.
- **case note:** "Design in the vault, build in the terminal — agents read, they don't re-derive."

### Arc — Learning Tracker
- **slug:** `arc-learning-tracker`
- **tagline:** A tool for tracking and structuring self-directed learning.
- **category:** frontend · **featured:** no · **liveUrl:** (empty) · **repoUrl:** resolve from GitHub
- **skills[]:** React, Next.js, TypeScript, Tailwind CSS
- **description:** A learning-tracker application for turning scattered study into a structured, reviewable trajectory. (Anant: expand scope/status when ready — kept concise here to avoid overclaiming.)

> If other vault projects (e.g. TradingView/Stocks Trading AI Hub) become real and worth showing, add them as additional `project` docs in this same shape. Don't surface anything that isn't genuinely built.

---
## 4. `experience` content (verify against current Sanity / résumé)
These mirror what already renders; the fix is wiring `employmentType`, `description`, `achievements`, `companyLogo`, `companyUrl`, and Sanity skill refs.

- **Research Assistant — University of Minnesota** · contract · Minneapolis, MN · 2025-05 → present · skills: Python, Rust, MongoDB, Redis, Docker, Data Pipelines · description: "Develop Python and Rust APIs for astronomical alert-brokering on the BOOM project; build real-time event tracking and observability tooling for Linux data pipelines; design structured ingestion APIs for large observational datasets." · achievements: contributed to BOOM alert-brokering infrastructure for astronomical event streams; designed analytics-ready ingestion pipelines.
- **Full Stack Development Intern — NSP** · internship · Bangalore, India · 2025-05 → 2025-08 · skills: Next.js, React, Tailwind CSS, TypeScript · description: "Developed Assisto, a production ed-tech web platform; integrated Strapi CMS APIs for backend-driven pages; built reusable, performant, accessible, SEO-focused UI components." · achievements: shipped Assisto to production supporting early user onboarding; established reusable component patterns that accelerated page development.
- **Web Developer — TechLit** · freelance · Texas, US · 2021-06 → 2022-06 · skills: Python, React, Git / GitHub · description: "Built the initial TechLit learning portal with HTML, CSS, and Python backend integrations; coordinated feature planning with a remote U.S.–India team; deployed and maintained the platform supporting cross-cultural education." · achievements: launched TechLit cross-cultural learning platform; delivered core portal features enabling remote team coordination.
- **Entrepreneur — Freelance** · freelance · Remote · 2026-05 → present · "Coming soon" placeholder is fine; keep as-is until real.

## 5. `education` (UI-only per [[06 - Education Flowchart]]; content already correct)
- College — B.S. Computer Science, University of Minnesota–Twin Cities, 2024 → present, GPA 3.4 — stage: `college` (perfect circle)
- High School — CBSE, Sri Chaitanya College, 2022 → 2024, GPA 3.8 — stage: `high` (partly formed)
- Middle School — ICSE, Ryan International School, 2018 → 2021, GPA 4/4 — stage: `middle` (amoeba)

## 6. `certification`
Keep only genuinely-held credentials. Current cards (AWS SA-Pro, GCP PCA, GitHub Actions, CKA, TensorFlow Dev, MongoDB Dev) appear to be dummy — **do not present unearned certs.** Ask Anant which are real; for each real one, populate `credentialUrl` (the out-link) and Sanity skill refs. Schema stays ready either way.

## Done conditions
- `skillCategory` + `skill` registries created with the colours above; every section's chips reference them.
- Real projects loaded (OpsPilot, Resq, SafeReach, AI Portfolio Agent, Jarvis, Arc); filler removed; repoUrls resolved via GitHub MCP; empty liveUrls hidden.
- Experience fields wired; education stages tagged; certifications de-faked pending Anant's confirmation.

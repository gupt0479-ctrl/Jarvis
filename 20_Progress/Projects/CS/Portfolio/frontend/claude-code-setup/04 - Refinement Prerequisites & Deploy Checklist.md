---
type: concept
status: active
created: 2026-06-13
updated: 2026-06-13
tags:
  - portfolio
  - claude-setup
  - frontend
  - deploy
notes:
  - "[[00 - Frontend Build Kit — Index]]"
  - "[[03 - Per-Phase Build Prompts]]"
---
# Refinement Prerequisites & Deploy Checklist
> Read once before R0. Everything needed to run the final pass ([[03 - Per-Phase Build Prompts]]) cleanly and ship today. If a prerequisite is missing, fix it inside the relevant phase — don't block the whole run.

## Packages to confirm present (check `package.json` before R-phases that need them)
Most are already installed (the build runs). Confirm, and only `pnpm add` if genuinely missing:
- **`@portabletext/react`** — needed in R2 to render the experience Portable Text `description`. If absent: `pnpm add @portabletext/react`.
- **`@react-spring/web`** and **`@react-three/drei`** (`Float`, `MeshDistortMaterial`) — already used by Projects (R3) and Education (R5). Confirm only.
- **`recharts`** + the shadcn `ChartContainer/ChartTooltipContent` wrappers — already used by Skills (R4). Confirm only.
- **`@react-three/postprocessing`** — ONLY if you choose to do the optional ObsidianBackground polish ([[11 - ObsidianBackground Enhancement]]). Not part of the ship-today path.

## Sanity / data prerequisites (R1)
- Run `pnpm typegen` after EVERY schema edit (`skill.color`, `project.summary`, `project.coverImage` optional, remove `project.visibility`, `EDUCATION_QUERY` logo), then `pnpm typecheck`. Never hand-edit `src/sanity/types/index.ts`.
- `skill.color` is a **preset enum mapped to hex in one place** — keep that map next to `CATEGORY_COLORS` so dots and graph lines stay coherent.
- No `.env` changes are required for this pass (Sanity, GitHub, chatbot are already configured and working).

## Per-phase verification (every session ends with)
1. `pnpm typecheck` clean.
2. Visual check against the phase's ACCEPTANCE line in [[03 - Per-Phase Build Prompts]].
3. No new console errors on the affected section.
4. `prefers-reduced-motion` still behaves (no runaway animation).

## Guardrails (unchanged)
pnpm only. No `tailwind.config.ts`. No git commits / no deploys by the agent (Anant owns both). Don't touch `OrbyCanvas.tsx`, `src/app/api/`, `src/lib/chat-*`. Don't rename `technologies[]`. Invent no URLs.

## Final pre-deploy checklist (after R8, before Anant deploys)
- [ ] `pnpm typecheck` clean.
- [ ] `pnpm build` clean (runs typegen + typecheck + next build).
- [ ] `pnpm lint` (Biome) clean.
- [ ] Each section's ACCEPTANCE met (R0–R7) — quick scroll-through at 1280px and at 375px mobile.
- [ ] No console errors; no CSP violations if CSP was enabled (else CSP deferred to post-deploy — the other security headers already ship).
- [ ] Orby speech cloud doesn't clip; header pill static; uniform section spacing; no blank boxes.
- [ ] Real content only (no fake certs/projects); GitHub links resolve; broken live links hidden.

## Deploy (Anant runs this — not the agent)
The repo deploys to Vercel. After the checklist is green, Anant runs the deploy (Vercel dashboard or `vercel --prod`, per the existing setup). The agent stops at "green-light reported."

> **CSP timing:** if shipping today is tight, deploy WITHOUT the new CSP (the existing HSTS/X-CTO/X-Frame/Referrer/Permissions headers already protect the site) and add CSP in report-only → enforce immediately after. Don't let CSP block the launch.

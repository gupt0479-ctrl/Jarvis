---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Kiro/Portfolio/Setup]]"
---
# Portfolio v1 — Project Context

## Stack

| Layer | Tech |
|-------|------|
| Framework | Next.js 16 App Router |
| Styling | Tailwind v4 (CSS-first — NO `tailwind.config.ts`) |
| Components | shadcn/Radix |
| Animation | Framer Motion / Motion |
| 3D | React Three Fiber + @react-three/drei |
| CMS | Sanity (all content — profile, projects, experience, skills, education, certs) |
| Auth | Clerk (studio-only) |
| Bot protection | Cloudflare Turnstile |
| Linter | Biome (NOT ESLint) |
| Package manager | pnpm |
| Deploy | Vercel (site) + Cloudflare Workers |

## Commands

```bash
pnpm dev          # dev server
pnpm lint         # biome check
pnpm format       # biome format --write
pnpm typecheck    # tsc --noEmit
pnpm build        # production build
```

## Visual Identity

Space command center: dark translucent surfaces, violet/cyan accents, everything floats.

### Color Tokens

| Token | Value |
|-------|-------|
| Background | `rgba(9, 10, 18, 1)` |
| Card surface (low) | `rgba(9, 10, 18, 0.72)` |
| Card surface (high) | `rgba(14, 16, 28, 0.82)` |
| Card border | `rgba(167, 139, 250, 0.22)` |
| Card border hover | `rgba(167, 139, 250, 0.45)` |
| Accent violet | `#7C3AED` / `#A78BFA` |
| Accent cyan | `#06B6D4` / `#67E8F9` |
| Accent green (signal) | `#10B981` |

### `.cosmic-card` Contract

- Dark translucent bg (`opacity: 0.78`), never solid, never transparent
- `border: 1px solid rgba(167, 139, 250, 0.22)`
- `backdrop-filter: blur(12px)` + `-webkit-backdrop-filter`
- Float at rest: `translateY(-2px)`, subtle shadow
- Lift on hover: `translateY(-6px)`, brighter border, stronger glow

### `.float-btn` Contract

- Default: `translateY(-1px)`, faint border glow, shadow
- Hover: `translateY(-3px)`, brighter border
- Active: `translateY(0)`, compressed shadow
- Applies to: all CTAs, carousel arrows, social icons, Lab launcher

### Section Kickers

Monospace label above each section heading (`font-size: 0.75rem`, cyan-muted):

| Section | Kicker |
|---------|--------|
| Hero | `// hi, I'm` |
| About | `// scan report` |
| Experience | `// trajectory` |
| Projects | `// build log` |
| Skills | `// capability matrix` |
| Education | `// origins` |
| Certifications | `// credentials` |
| Blog / Contact | `// uplink` |

## File Map

| Area | Path |
|------|------|
| Design system CSS | `src/app/globals.css` |
| Space background | `src/components/three/ObsidianBackground.tsx` |
| 3D project carousel | `src/components/three/ProjectsSlider.tsx` |
| 3D hover card | `src/components/ui/comet-card.tsx` |
| Sections | `src/components/sections/` |
| Portfolio Lab | `src/components/lab/PortfolioLab.tsx` |
| Orby companion | `src/components/orby/` |
| Chat system | `src/lib/chat-tools.ts`, `src/lib/model-router.ts`, `src/lib/personas.ts` |
| Chat API | `src/app/api/chat/route.ts` |
| Sanity queries | `src/lib/sanity.queries.ts` |
| Class merge util | `src/lib/utils.ts` → `cn()` |

## Forbidden

- Creating `tailwind.config.ts` — Tailwind v4 is CSS-first
- Using ESLint — Biome only
- Hardcoding content — all content from Sanity
- Solid white or `opacity: 1` cards
- Fully transparent cards (must have backdrop-filter)
- Raw `THREE.Scene`/`THREE.Renderer` outside R3F
- `new THREE.*` inside `useFrame` — mutate refs only
- Using `npm` or `yarn` — pnpm only
- Creating `src/pages/` — App Router only

## R3F Rules

- Dynamic import with `ssr: false` always
- `useMemo` for geometries and position arrays
- Canvas: `dpr={[1, 2]}`, `performance={{ min: 0.5 }}`
- `prefers-reduced-motion` → disable animations
- Mobile (<768px) → halve particle counts
- ObsidianBackground: `position: fixed`, `z-index: 0`, `pointer-events: none`

## Framer Motion

- Section entry: `initial={{ opacity: 0, y: 24 }}`, `whileInView`, `viewport={{ once: true }}`
- Stagger: `staggerChildren: 0.08`
- Buttons: `whileHover={{ y: -2 }}`, `whileTap={{ y: 1 }}`

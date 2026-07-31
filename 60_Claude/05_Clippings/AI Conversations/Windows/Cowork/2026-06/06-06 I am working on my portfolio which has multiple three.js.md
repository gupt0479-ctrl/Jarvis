---
type: input
input_kind: ai-conversation
source_app: cowork
source_os: windows
title: "I am working on my portfolio which has multiple three.js"
started_at: 2026-06-06T03:18:10
ended_at: 2026-06-06T03:22:59
exported_at: 2026-07-31T21:03:36
duration_minutes: 4.8
project: 2026-06
session_id: a4609a00-003c-46f6-b7fe-5cb872bf100b
status: raw
turn_count: 2
tools_used:
  mcp__cowork__present_files: 1
  mcp__jarvis__search_simple: 2
  mcp__jarvis__vault_read: 1
  mcp__workspace__bash: 1
  TaskCreate: 2
  TaskUpdate: 4
  ToolSearch: 3
  Write: 3
tokens:
  input: 38
  output: 21636
  cache_creation: 99745
  cache_read: 1216852
  total: 1338271
cost_usd: 1.28818
model:
  - "claude-sonnet-4-6"
files_touched:
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\40_Project_Briefs\\portfolio-frontend-kit\\CLAUDE.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\40_Project_Briefs\\portfolio-frontend-kit\\cosmic-frontend.mdc"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\40_Project_Briefs\\portfolio-frontend-kit\\three-artist.md"
tags:
  - input
  - ai-conversation
  - cowork
  - windows
---

# I am working on my portfolio which has multiple three.js

## You

I am working on my portfolio which has multiple three.js components and cards that appear to be floating. Multiple things that need to work out but my ai agent's just can't seem to give me the result I desire. I want to add a crazy front end developer kit to claude or maybe cursor. Search the resources in my vault for this. I want to focus on front end development for producing three dimensional background and multiple cards that appear to be in space

## Claude

Your vault has everything I need. You have a Next.js 16 App Router + Three.js/R3F + Tailwind v4 + shadcn + Framer Motion stack, with a full cosmic UI refactor spec already documented. The problem is clear: agents don't know your component contracts, design tokens, or R3F patterns, so they guess wrong every time.

The fix is a three-file kit — a `CLAUDE.md` for Claude Code, a `.mdc` for Cursor rules, and a specialized `three-artist` agent. Let me build them.

Three files built from your vault's own spec. Here's where each one goes:

**`CLAUDE.md`** → drop at `ai-portfolio/CLAUDE.md` (repo root). Claude Code reads this automatically on every session. It encodes your full stack, the component contracts for `cosmic-card` and `float-btn`, all the R3F rules, forbidden actions, and the real Sanity content so the agent never hardcodes "Alex Morgan" again.

**`cosmic-frontend.mdc`** → goes at `ai-portfolio/.cursor/rules/cosmic-frontend.mdc`. Cursor picks this up via glob — it activates when you're in `three/`, `comet-card.tsx`, or `globals.css`. Has copy-paste recipes for float physics, particle sphere, elastic tether, the card CSS, and organic education blobs.

**`three-artist.md`** → goes at `ai-portfolio/.claude/agents/three-artist.md`. Invoke it in Claude Code with `@three-artist` when you need a focused 3D session. It has its own verification checklist so it doesn't hand you back untested Three.js.

The root cause of your agent failures is that they were working from zero context every time — guessing at your color tokens, card opacity rules, and whether to use raw Three.js or R3F. These files fix that permanently. The `CLAUDE.md` alone will eliminate most of the drift.

### Tool Calls

- `ToolSearch` -- `{"query":"select:TaskCreate","max_results":1}`
- `TaskCreate` -- `{"subject":"Search vault for frontend/Three.js resources","description":"Search Jarvis vault for any existing notes on Three.js, frontend dev, portfolio, Cursor, or Claude Code setups","activeForm":"Searching vault"}`
- `ToolSearch` -- `{"query":"select:TaskUpdate","max_results":1}`
- `TaskUpdate` -- `{"taskId":"1","status":"in_progress"}`
- `mcp__jarvis__search_simple` -- `{"query":"three.js frontend portfolio"}`
- `mcp__jarvis__search_simple` -- `{"query":"cursor claude code frontend development"}`
- `mcp__jarvis__vault_read` -- `{"path":"20_Progress/Projects/CS/Portfolio/Portfolio.md"}`
- `TaskUpdate` -- `{"taskId":"1","status":"completed"}`
- `TaskCreate` -- `{"subject":"Build portfolio frontend developer kit","description":"Create 3 files: CLAUDE.md for portfolio repo, Claude Code three-artist agent, and Cursor rules mdc file — all tailored to the cosmic Three.js stack","activeForm":"Building the kit"}`
- `TaskUpdate` -- `{"taskId":"2","status":"in_progress"}`
- `mcp__workspace__bash` -- `{"command":"mkdir -p /sessions/jolly-sharp-clarke/mnt/Jarvis/60_Claude/40_Project_Briefs/portfolio-frontend-kit"}`
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\40_Project_Briefs\portfolio-frontend-kit\CLAUDE.md`
```
# Portfolio Repo — Claude Operating Instructions

> Drop this file at the root of your portfolio repo (`ai-portfolio/CLAUDE.md`).
> It primes Claude Code with exact stack knowledge, component contracts, and visual identity before touching any file.

---

## Stack (exact — do not assume defaults)

| Layer | Tech |
|-------|------|
| Framework | Next.js 16 App Router |
| Styling | Tailwind v4 (CSS-first — **no `tailwind.config.ts`**) |
| Components | shadcn/Radix |
| Animation | Framer Motion / Motion |
| 3D | Three.js + **React Three Fiber (R3F)** + `@react-three/drei` |
| CMS | Sanity (profile, projects, experience, skills, education, certs) |
| Auth | Clerk |
| Linter | Biome (**not ESLint**) |
| Package manager | pnpm |

---

## Key Files

| Path | Role |
|------|------|
| `src/components/three/ObsidianBackground.tsx` | Main R3F canvas — particle sphere + starfield |
| `src/components/ui/comet-card.tsx` | Base 3D-hover floating card primitive |
| `src/components/three/ProjectsSlider.tsx` | 3D project carousel |
| `src/components/sections/*` | All page sections |
| `src/app/globals.css` | Design system: `.cosmic-card`, `.float-btn`, `.section-kicker`, `.orbit-chip` |
| `src/lib/sanity.queries.ts` | All Sanity data fetching |

---

## Visual Identity — Never Deviate

The site is a **floating portfolio command center inside space**.  
Think: cosmic terminal, orbital cards, dark translucent surfaces, violet/cyan signal accents.

### Color tokens

| Token | Value |
|-------|-------|
| Background | `rgba(9, 10, 18, 1)` |
| Card surface (low) | `rgba(9, 10, 18, 0.72)` |
| Card surface (high) | `rgba(14, 16, 28, 0.82)` |
| Card border | `rgba(167, 139, 250, 0.22)` |
| Accent violet | `#7C3AED` / `#A78BFA` |
| Accent cyan | `#06B6D4` / `#67E8F9` |
| Accent green (signal only) | `#10B981` |

### `.cosmic-card` contract

Every card MUST:
- Dark translucent background — not fully transparent, not solid, not white
- `border: 1px solid rgba(167, 139, 250, 0.22)`
- `backdrop-filter: blur(12px)`
- Readable over the Three.js background at all times
- Float visually at rest: `translateY(-2px)`, subtle shadow, faint border glow
- Lift on hover: `translateY(-6px)`, brighter border, stronger glow

```css
.cosmic-card {
  background: rgba(9, 10, 18, 0.78);
  border: 1px solid rgba(167, 139, 250, 0.22);
  box-shadow:
    0 0 0 1px rgba(167, 139, 250, 0.08) inset,
    0 8px 32px rgba(0, 0, 0, 0.6),
    0 0 24px rgba(124, 58, 237, 0.06);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  transform: translateY(-2px);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.cosmic-card:hover {
  transform: translateY(-6px);
  border-color: rgba(167, 139, 250, 0.45);
  box-shadow:
    0 0 0 1px rgba(167, 139, 250, 0.15) inset,
    0 16px 48px rgba(0, 0, 0, 0.7),
    0 0 40px rgba(124, 58, 237, 0.12);
}
```

### `.float-btn` contract

Every button MUST look floating even at rest:
- Default: `box-shadow` on, `translateY(-1px)`, faint border glow
- Hover: lift more, brighten border, cursor sheen
- Active: `translateY(1px)`, compressed shadow
- Apply to: hero CTAs, project buttons, carousel arrows, contact buttons, AI Lab launcher, footer back-to-top, social icons

---

## Three.js / R3F Rules

1. **Always use React Three Fiber** — no raw imperative Three.js outside the R3F component tree. If you find legacy imperative code, migrate it.

2. **Use `@react-three/drei`** for helpers: `Stars`, `Float`, `MeshDistortMaterial`, `Environment`, `OrbitControls` (dev only), etc.

3. **Float physics for objects in space:**
```tsx
import { Float } from '@react-three/drei'

// Cards/objects gently drifting in space
<Float speed={1.2} rotationIntensity={0.3} floatIntensity={0.5} floatingRange={[-0.05, 0.05]}>
  <mesh>
    {/* your geometry */}
  </mesh>
</Float>

// Organic blobs (education section)
<Float speed={0.8} rotationIntensity={0.15}>
  <mesh>
    <sphereGeometry args={[1, 64, 64]} />
    <MeshDistortMaterial
      color="#1E1B4B"
      distort={0.35}
      speed={1.5}
      transparent
      opacity={0.6}
    />
  </mesh>
</Float>
```

4. **Particle sphere pattern:**
```tsx
import { useRef, useMemo } from 'react'
import { useFrame } from '@react-three/fiber'
import * as THREE from 'three'

function ParticleSphere({ count = 2000, radius = 2.5 }) {
  const ref = useRef<THREE.Points>(null)

  const positions = useMemo(() => {
    const pos = new Float32Array(count * 3)
    for (let i = 0; i < count; i++) {
      const theta = Math.random() * Math.PI * 2
      const phi = Math.acos(2 * Math.random() - 1)
      const r = radius + (Math.random() - 0.5) * 0.3
      pos[i * 3]     = r * Math.sin(phi) * Math.cos(theta)
      pos[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta)
      pos[i * 3 + 2] = r * Math.cos(phi)
    }
    return pos
  }, [count, radius])

  useFrame((_, delta) => {
    if (ref.current) ref.current.rotation.y += delta * 0.05
  })

  return (
    <points ref={ref}>
      <bufferGeometry>
        <bufferAttribute attach="attributes-position" args={[positions, 3]} />
      </bufferGeometry>
      <pointsMaterial size={0.015} color="#A78BFA" sizeAttenuation transparent opacity={0.7} />
    </points>
  )
}
```

5. **Performance rules (mandatory):**
   - `prefers-reduced-motion` → stop `useFrame` rotations, disable float animations
   - Mobile (viewport < 768px) → halve particle counts, disable post-processing
   - Never create `new THREE.*` objects inside `useFrame` — mutate refs only
   - `useMemo` for all geometries and positions
   - Canvas: `dpr={[1, 2]}` and `performance={{ min: 0.5 }}`
   - Dispose geometries/materials in cleanup

6. **ObsidianBackground contract:**
   - Canvas is `position: fixed`, `z-index: 0`, `pointer-events: none`
   - All page content renders at `z-index: 1+`
   - Reduce particle intensity (opacity/count) behind text-heavy sections via scroll position

---

## CometCard Rules

File: `src/components/ui/comet-card.tsx`

Props:
- `className`
- `variant`: `"default"` | `"dark"` | `"large"`

Behavior by variant:
- `dark`: more opaque background (`opacity: 0.88`), reduced 3D tilt (`max 8deg`)
- `large`: max tilt `8deg` — large slabs must not warp like warped glass
- All variants: respect `prefers-reduced-motion` — disable tilt if user prefers it

---

## Framer Motion Patterns

```tsx
// Section entry (all sections)
<motion.div
  initial={{ opacity: 0, y: 24 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-80px" }}
  transition={{ duration: 0.5, ease: "easeOut" }}
/>

// Staggered children
<motion.div variants={{ visible: { transition: { staggerChildren: 0.08 } } }}>

// Float buttons
<motion.button whileHover={{ y: -2 }} whileTap={{ y: 1 }}>

// Project card elastic spring (use @react-spring/web for physics)
import { useSpring, animated } from '@react-spring/web'
const [springs, api] = useSpring(() => ({
  x: 0,
  config: { tension: 180, friction: 24 } // rubber-band tether feel
}))
```

---

## Content Rules

**ALL content comes from Sanity** via `src/lib/sanity.queries.ts`. Never hardcode.

Real data for reference only:
- Name: Anant Gupta
- Role: AI & Data Systems Engineer / Full-Stack Developer
- University: University of Minnesota–Twin Cities, B.S. CS 2024–2028
- Location: Minneapolis, MN
- Experience: BOOM research assistant, NSEdu web dev intern, CSE Student Ambassador, Techlit co-founder
- Tech: Rust, Python, React, Next.js, TypeScript, Tailwind, LLM APIs, MongoDB, Kafka, Docker

---

## Forbidden Actions

- Creating `tailwind.config.ts` — Tailwind v4 is CSS-first
- Creating `src/pages/` — this is App Router
- Using ESLint config — Biome only
- Hardcoding content — use Sanity queries
- Making cards solid white or `opacity: 1` visible
- Making cards fully transparent (`opacity: 0` or just a border)
- Writing raw `THREE.Scene` / `THREE.Renderer` outside R3F
- Creating new THREE objects inside `useFrame`
- Committing git — user manages all commits
- Using `npm` or `yarn` — pnpm only

---

## Commands

```bash
pnpm dev          # dev server
pnpm lint         # biome check
pnpm format       # biome format --write
pnpm typecheck    # tsc --noEmit
pnpm build        # production build
```

---

## Section Kickers

Every section gets a commented code-style label above its heading:

| Section | Kicker |
|---------|--------|
| Hero | `// hi, I'm` |
| About | `// scan report` |
| Experience | `// trajectory` |
| Projects | `// build log` |
| Skills | `// capability matrix` |
| Education | `// origins` |
| Certifications | `// credentials` |
| Blog | `// uplink` |
| Contact | `// uplink` |

Style: cyan/violet-muted, monospace, `font-size: 0.75rem`.

```
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\40_Project_Briefs\portfolio-frontend-kit\cosmic-frontend.mdc`
```
---
description: Three.js R3F cosmic portfolio — floating cards, space backgrounds, 3D effects
globs: ["src/components/three/**", "src/components/ui/comet-card.tsx", "src/app/globals.css", "src/components/sections/**"]
alwaysApply: false
---

# Cosmic Portfolio — Three.js / R3F Cursor Rules

## Core Identity
This is a **floating portfolio command center inside space**.
Dark translucent cards. Violet/cyan accents. Everything floats.
Never: white backgrounds, flat buttons, solid opaque cards, or raw imperative Three.js.

---

## Stack
- React Three Fiber (R3F) — never raw `THREE.WebGLRenderer` outside R3F
- `@react-three/drei` — Float, Stars, MeshDistortMaterial, etc.
- Framer Motion — section entries, button interactions
- `@react-spring/web` — elastic/physics animations (project slider tether)
- Tailwind v4 (CSS-first, no `tailwind.config.ts`)
- Next.js 16 App Router

---

## Float Pattern — Objects in Space

Use R3F `Float` from `@react-three/drei` for any 3D object that should drift:

```tsx
import { Float, MeshDistortMaterial } from '@react-three/drei'

// Standard card float
<Float speed={1.2} rotationIntensity={0.3} floatIntensity={0.5} floatingRange={[-0.05, 0.05]}>
  <mesh>
    <planeGeometry args={[2, 1.2]} />
    <meshStandardMaterial
      color="#0A0B14"
      transparent
      opacity={0.82}
      roughness={0.1}
      metalness={0.3}
    />
  </mesh>
</Float>

// Organic blob — education flowchart nodes
<Float speed={0.8} rotationIntensity={0.15} floatIntensity={0.4}>
  <mesh>
    <sphereGeometry args={[1, 64, 64]} />
    <MeshDistortMaterial
      color="#1E1B4B"
      distort={0.35}
      speed={1.5}
      transparent
      opacity={0.55}
    />
  </mesh>
</Float>
```

---

## CSS Floating Cards (DOM level)

```css
/* globals.css — add or update these */

.cosmic-card {
  background: rgba(9, 10, 18, 0.78);
  border: 1px solid rgba(167, 139, 250, 0.22);
  box-shadow:
    0 0 0 1px rgba(167, 139, 250, 0.08) inset,
    0 8px 32px rgba(0, 0, 0, 0.6),
    0 0 24px rgba(124, 58, 237, 0.06);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: 16px;
  transform: translateY(-2px);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.cosmic-card:hover {
  transform: translateY(-6px);
  border-color: rgba(167, 139, 250, 0.45);
  box-shadow:
    0 0 0 1px rgba(167, 139, 250, 0.15) inset,
    0 16px 48px rgba(0, 0, 0, 0.7),
    0 0 40px rgba(124, 58, 237, 0.12);
}

.float-btn {
  transform: translateY(-1px);
  box-shadow:
    0 4px 12px rgba(0, 0, 0, 0.4),
    0 0 0 1px rgba(167, 139, 250, 0.2);
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.float-btn:hover {
  transform: translateY(-3px);
  box-shadow:
    0 8px 24px rgba(0, 0, 0, 0.5),
    0 0 0 1px rgba(167, 139, 250, 0.45),
    0 0 16px rgba(124, 58, 237, 0.15);
}

.float-btn:active {
  transform: translateY(0);
  box-shadow:
    0 2px 6px rgba(0, 0, 0, 0.3),
    0 0 0 1px rgba(167, 139, 250, 0.15);
}

.section-kicker {
  font-family: ui-monospace, monospace;
  font-size: 0.75rem;
  color: rgba(103, 232, 249, 0.65);
  letter-spacing: 0.05em;
  margin-bottom: 0.5rem;
}
```

---

## Particle Sphere

```tsx
import { useRef, useMemo } from 'react'
import { useFrame } from '@react-three/fiber'
import * as THREE from 'three'

function ParticleSphere({ count = 2000, radius = 2.5 }: { count?: number; radius?: number }) {
  const ref = useRef<THREE.Points>(null)

  const positions = useMemo(() => {
    const pos = new Float32Array(count * 3)
    for (let i = 0; i < count; i++) {
      const theta = Math.random() * Math.PI * 2
      const phi = Math.acos(2 * Math.random() - 1)
      const r = radius + (Math.random() - 0.5) * 0.3
      pos[i * 3]     = r * Math.sin(phi) * Math.cos(theta)
      pos[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta)
      pos[i * 3 + 2] = r * Math.cos(phi)
    }
    return pos
  }, [count, radius])

  useFrame((_, delta) => {
    if (ref.current) ref.current.rotation.y += delta * 0.05
  })

  return (
    <points ref={ref}>
      <bufferGeometry>
        <bufferAttribute attach="attributes-position" args={[positions, 3]} />
      </bufferGeometry>
      <pointsMaterial
        size={0.015}
        color="#A78BFA"
        sizeAttenuation
        transparent
        opacity={0.7}
      />
    </points>
  )
}
```

---

## Project Slider — Elastic Tether Effect

```tsx
import { useSpring, animated } from '@react-spring/web'

// When user clicks left/right, card springs into center with rubber-band feel
const [springs, api] = useSpring(() => ({
  x: 0,
  config: {
    tension: 180,  // spring stiffness — higher = snappier
    friction: 24,  // damping — lower = more bounce
    mass: 1,
  }
}))

// Trigger: api.start({ x: targetX })
// Wrap the card container with <animated.div style={springs}>
```

---

## Performance Rules

Always check these before finishing a Three.js component:

```tsx
// 1. Detect reduced motion
const prefersReduced = typeof window !== 'undefined'
  && window.matchMedia('(prefers-reduced-motion: reduce)').matches

// 2. Detect mobile
const isMobile = typeof window !== 'undefined' && window.innerWidth < 768

// 3. Conditional counts
const particleCount = isMobile ? 800 : prefersReduced ? 0 : 2000

// 4. Never create objects in useFrame
useFrame((_, delta) => {
  if (ref.current && !prefersReduced) {
    ref.current.rotation.y += delta * 0.05  // mutate, don't create
  }
})

// 5. Canvas settings
<Canvas dpr={[1, 2]} performance={{ min: 0.5 }}>
```

---

## CometCard Variants

```tsx
// comet-card.tsx — variant logic
type CometCardProps = {
  variant?: 'default' | 'dark' | 'large'
  children: React.ReactNode
  className?: string
}

// variant="dark" → opacity 0.88, maxTilt 8deg
// variant="large" → maxTilt 8deg (slabs don't warp)
// variant="default" → maxTilt 15deg, opacity 0.78

// Always respect reduced motion:
const prefersReduced = useReducedMotion() // from framer-motion
```

---

## Education — Organic Flowchart

Three stages, each as a morphing blob in R3F or an SVG blob with CSS animation:

```tsx
// Distortion levels encode growth:
// Middle school: distort={0.6} — most deformed
// High school:   distort={0.4} — partially formed
// College:       distort={0.15} — nearly perfect sphere, glowing

// Connection between nodes: dotted SVG line with animated dashoffset
// Light travels from bottom (middle school) to top (college)
```

---

## Framer Motion — Standard Patterns

```tsx
// Section entry — use on every section wrapper
<motion.section
  initial={{ opacity: 0, y: 24 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-80px" }}
  transition={{ duration: 0.5, ease: "easeOut" }}
>

// Stagger container
const container = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.08 } }
}

// Float button
<motion.button
  className="float-btn"
  whileHover={{ y: -2 }}
  whileTap={{ y: 1 }}
  transition={{ type: "spring", stiffness: 400, damping: 20 }}
>
```

---

## Background Canvas Contract

`ObsidianBackground.tsx` rules:
- Canvas: `position: fixed`, `inset: 0`, `z-index: 0`, `pointer-events: none`
- All content: `position: relative`, `z-index: 1+`
- Reduce particle opacity (not count) near scroll positions of text-heavy sections
- No post-processing on mobile

---

## Color Quick Reference

| Name | Value |
|------|-------|
| Space black | `#090A12` |
| Card low | `rgba(9,10,18,0.72)` |
| Card high | `rgba(14,16,28,0.82)` |
| Border | `rgba(167,139,250,0.22)` |
| Violet | `#A78BFA` |
| Cyan | `#67E8F9` |
| Green signal | `#10B981` |

```
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\40_Project_Briefs\portfolio-frontend-kit\three-artist.md`
```
# three-artist — Claude Code Agent

> File goes at: `ai-portfolio/.claude/agents/three-artist.md`
> Invoked when: user asks for Three.js/R3F work, floating card effects, space background changes, or 3D animations.

---

## Agent Identity

You are the Three.js / R3F specialist for Anant's cosmic portfolio. Your job is to produce production-quality 3D and animation code that matches the site's floating-command-center-in-space aesthetic. You do not guess at design intent — you use the rules below.

Read `CLAUDE.md` at the repo root before every session. It has the component contracts and design tokens you need.

---

## Scope

Handle:
- `src/components/three/` — all R3F components
- `src/components/ui/comet-card.tsx` — 3D hover card
- `src/app/globals.css` — `.cosmic-card`, `.float-btn`, `.section-kicker`, `.orbit-chip`
- CSS float/glow animations across any section component

Do not touch:
- Sanity queries or schemas
- Clerk auth
- API routes
- `pnpm-lock.yaml`

---

## Rules (hard constraints)

### R3F only
Never write `new THREE.WebGLRenderer()`, `new THREE.Scene()`, or manual render loops. Every Three.js scene lives inside an R3F `<Canvas>`. If you find legacy imperative Three.js, migrate it.

### Float physics — standard recipe
```tsx
import { Float } from '@react-three/drei'

<Float
  speed={1.2}
  rotationIntensity={0.3}
  floatIntensity={0.5}
  floatingRange={[-0.05, 0.05]}
>
  {/* mesh goes here */}
</Float>
```

Adjust `speed` and `floatIntensity` by context:
- Hero sphere: `speed={0.6}`, `floatIntensity={0.3}` — slow and majestic
- Project cards: `speed={1.2}`, `floatIntensity={0.5}` — active drift
- Education blobs: `speed={0.8}`, `floatIntensity={0.4}` — organic

### Card surfaces
- Background: `rgba(9, 10, 18, 0.78)` to `rgba(14, 16, 28, 0.82)`
- Never fully transparent, never fully opaque, never white
- `backdrop-filter: blur(12px)` always
- Border: `1px solid rgba(167, 139, 250, 0.22)`, brightens on hover to `0.45`

### Performance (non-negotiable)
```tsx
// Check this at component top
const prefersReduced = typeof window !== 'undefined'
  && window.matchMedia('(prefers-reduced-motion: reduce)').matches
const isMobile = typeof window !== 'undefined' && window.innerWidth < 768

// In useFrame — mutate only, never create
useFrame((_, delta) => {
  if (ref.current && !prefersReduced) {
    ref.current.rotation.y += delta * 0.05
  }
})

// Particle counts
const count = isMobile ? 800 : prefersReduced ? 0 : 2000

// Canvas
<Canvas dpr={[1, 2]} performance={{ min: 0.5 }}>
```

### CometCard tilt limits
- Default variant: max 15deg
- Dark variant: max 8deg, opacity 0.88
- Large variant: max 8deg — large slabs must not distort into warped glass

---

## Recipes

### Glowing timeline rail (Experience section)
```css
.timeline-rail {
  width: 2px;
  background: linear-gradient(
    to bottom,
    transparent,
    rgba(167, 139, 250, 0.6) 10%,
    rgba(103, 232, 249, 0.4) 50%,
    rgba(167, 139, 250, 0.6) 90%,
    transparent
  );
  box-shadow: 0 0 8px rgba(167, 139, 250, 0.3);
}
.timeline-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #A78BFA;
  box-shadow: 0 0 12px rgba(167, 139, 250, 0.6), 0 0 4px rgba(167, 139, 250, 0.9);
}
```

### Elastic project slider tether
```tsx
import { useSpring, animated } from '@react-spring/web'

const [springs, api] = useSpring(() => ({
  x: 0,
  config: { tension: 180, friction: 24, mass: 1 }
}))

// Fire on arrow click: api.start({ x: direction * cardWidth * -1 })
// Wrap carousel track: <animated.div style={{ x: springs.x }}>
```

### Multi-line skills graph (recharts)
```tsx
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts'

// Lines per category — hover highlights one, dims others via opacity state
const lines = [
  { key: 'aiml',    color: '#A78BFA', label: 'AI/ML' },
  { key: 'data',    color: '#67E8F9', label: 'Data Systems' },
  { key: 'backend', color: '#10B981', label: 'Backend' },
  { key: 'frontend',color: '#F59E0B', label: 'Frontend' },
  { key: 'devops',  color: '#EF4444', label: 'DevOps/Tools' },
]

// Category button interactions:
// AI/ML → pulse/glow on hover
// Backend → terminal cursor blink
// Frontend → shimmer sweep
// DevOps → deployment dots trail
// Data → animated tick bars
```

### Organic education blob (SVG CSS — no R3F needed)
```css
.edu-blob {
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  animation: morph 6s ease-in-out infinite;
  background: rgba(30, 27, 75, 0.7);
  border: 1px solid rgba(167, 139, 250, 0.3);
  box-shadow: 0 0 30px rgba(124, 58, 237, 0.15);
}
@keyframes morph {
  0%, 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
  25%       { border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%; }
  50%       { border-radius: 50% 60% 30% 60% / 30% 40% 70% 60%; }
  75%       { border-radius: 40% 60% 50% 30% / 60% 30% 60% 40%; }
}
/* Middle school: more distorted → faster animation speed (4s) */
/* College: more stable → slower (10s) and more circular border-radius */
```

---

## Output Format

When writing R3F components:
1. TypeScript always
2. Export named component + types
3. Include `useMemo` for geometries
4. Include reduced-motion check
5. Include mobile count/quality check
6. Comment the "why" on non-obvious values (e.g., `// 0.05 — slow drift keeps it readable`)

When writing CSS:
1. Add to `globals.css` under appropriate section comment
2. No inline styles for design system values
3. All transitions: `ease` or `easeOut`, 150–300ms
4. Always include `-webkit-backdrop-filter` alongside `backdrop-filter`

---

## Verification Checklist

Before declaring any Three.js task done:
- [ ] `pnpm typecheck` passes
- [ ] Canvas has `pointer-events: none`
- [ ] Content is readable over the background
- [ ] `prefers-reduced-motion` handled
- [ ] No new THREE objects created inside `useFrame`
- [ ] Mobile renders at reduced quality
- [ ] Card surfaces are translucent (not solid, not transparent)
- [ ] Buttons look floating at rest

```
- `TaskUpdate` -- `{"taskId":"2","status":"completed"}`
- `ToolSearch` -- `{"query":"select:mcp__cowork__present_files","max_results":1}`
- `mcp__cowork__present_files` -- `{"files":[{"file_path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\40_Project_Briefs\\portfolio-frontend-kit\\CLAUDE.md"},{"file_path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\40_Project_Briefs\\portfolio-frontend-kit\\cosmic-frontend.mdc"},{"file_path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\60_Claude\\40_Project_Briefs\\portfolio-frontend-kit\\three-artist.md"}]}`

## Actions Taken

**Files created:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\40_Project_Briefs\portfolio-frontend-kit\CLAUDE.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\40_Project_Briefs\portfolio-frontend-kit\cosmic-frontend.mdc`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\40_Project_Briefs\portfolio-frontend-kit\three-artist.md`

**Files modified:**
_None_

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
_None_



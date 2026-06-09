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

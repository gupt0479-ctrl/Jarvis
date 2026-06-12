---
tags: [portfolio, design-system, tailwind, css, components]
---

# Design System

> [[../INDEX|← Back to Index]]

## Tailwind CSS v4 — CSS-First

**No `tailwind.config.ts`** — Tailwind v4 is configured entirely in `src/app/globals.css` via `@theme`. Never create a tailwind config file.

## Color Tokens

| Token | Value | Usage |
|-------|-------|-------|
| Background | `rgba(9, 10, 18, 1)` | Page background |
| Card surface low | `rgba(9, 10, 18, 0.72)` | Subtle cards |
| Card surface high | `rgba(14, 16, 28, 0.82)` | Prominent cards |
| Card border | `rgba(167, 139, 250, 0.22)` | All card borders |
| Accent violet | `#7C3AED` / `#A78BFA` | Primary accent |
| Accent cyan | `#06B6D4` / `#67E8F9` | Secondary accent |
| Accent green | `#10B981` | Signal/status only |

## CSS Utility Classes (globals.css)

| Class | Purpose |
|-------|---------|
| `.cosmic-card` | Standard floating card — dark translucent + blur |
| `.cosmic-card--dark` | More opaque variant |
| `.cosmic-card--subtle` | Less prominent variant |
| `.float-btn` | Floating button with lift on hover |
| `.section-kicker` | Cyan/violet monospace label above section titles |
| `.orbit-chip` | Small tag/badge chip |
| `.section-backdrop` | Scroll-based backdrop for sections |

## cn() — God Node (96 edges)

```typescript
// src/lib/utils.ts L4
import { clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'
export function cn(...inputs: ClassValue[]) { return twMerge(clsx(inputs)) }
```

**96 edges** — most connected node in the entire graph. Used in every component. Always use `cn()` for class merging, never string concatenation.

Community 6 owns `cn()` alongside the sidebar primitives.

## CometCard — `src/components/ui/comet-card.tsx`

**17 edges** — cross-community card primitive.

```typescript
<CometCard variant="default" | "dark" | "subtle" className="...">
  {children}
</CometCard>
```

Props:
- `variant`: `"default"` | `"dark"` | `"subtle"` (maps to cosmic-card classes)
- `className`: merged via `cn()`

Behavior:
- 3D tilt effect on mouse hover (mouse tracking)
- `dark` variant: more opaque, max 8° tilt
- `large` variant: max 8° tilt (large slabs mustn't warp)
- Respects `prefers-reduced-motion` — disables tilt
- Glow on hover via CSS box-shadow transition

Community 13 owns CometCard alongside CertificationsSection (both use the dark card heavily).

## .cosmic-card Contract

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
```

**Never**: solid white, `opacity: 1` visible, or fully transparent.

## .float-btn Contract

Every button must float even at rest:
- Default: `box-shadow` on, `translateY(-1px)`, faint border glow
- Hover: lift more, brighten border
- Active: `translateY(1px)`, compressed shadow

## Section Kickers

Each section has a commented code-style label:

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

Style: cyan/violet-muted, monospace, `font-size: 0.75rem`, class `.section-kicker`.

## Fonts

- `ubuntu` — body text (loaded in root layout)
- `lora` — serif accent (loaded in root layout)
- Both via `next/font/google`

## shadcn / Radix Primitives

Community 24 — Dropdown menus
Community 47 — Card, CardHeader, CardTitle, CardContent, CardFooter, CardDescription, CardAction
Community 28 — Chart (Recharts-based): ChartContainer, ChartTooltipContent, ChartLegendContent

Always use shadcn/Radix primitives and lucide icons before writing new UI from scratch.

## See Also
- [[../components/05-ui-primitives|UI Primitives Detail]]
- [[../components/04-three-js|Three.js / R3F]]

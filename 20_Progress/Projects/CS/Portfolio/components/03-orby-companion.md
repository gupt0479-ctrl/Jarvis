---
tags: [portfolio, components, orby, 3D, animation]
---

# Orby Companion Components

> [[../INDEX|← Back to Index]] · [[00-overview|Component Map]]

## Overview

Orby is the 3D AI companion that floats on the portfolio page. It has a 3D model, speech cloud, scroll-aware state, and typed text animation. Spans Communities 30, 32, 36, 37.

## Component Tree

```
Orby.tsx  (Community 32 — entry)
  ├── OrbyCanvas.tsx     (Community 37 — R3F canvas)
  │     └── OrbyModel.tsx  (3D model + animations)
  │           └── OrbyArrow.tsx  (directional arrow)
  ├── OrbySpeechCloud.tsx  (Community 30 — speech bubble)
  └── useOrbyState.ts     (Community 36 — state machine)
```

Also accessed from Lab panel:
```
PanelOrby.tsx   (Community 37)
  └── OrbyCanvas.tsx
```

## Orby.tsx — Community 32

```typescript
// Key exports
function Orby(): JSX.Element
function OrbyArrow(props: OrbyArrowProps): JSX.Element
function getPose(): OrbySpeechCloudProps  // determines current pose/expression
```

`Orby()` is the top-level page companion (floating bottom-right).
`PanelOrby()` is the in-Lab panel version with different sizing.

## OrbyCanvas.tsx — Community 37

```typescript
interface OrbyCanvasProps { ... }
interface SceneProps { ... }
function OrbyCanvas(props: OrbyCanvasProps): JSX.Element
```

R3F `<Canvas>` wrapper. Manages camera, lighting, and scene setup for the Orby model.

## OrbyModel.tsx

- Uses `useFrame` for scroll-driven animations
- Calls `cn()` (surprising connection — uses class utility in a 3D component)
- Reads `useScrollProgress()` for pose decisions

## OrbySpeechCloud — Community 30

```typescript
interface OrbySpeechCloudProps { ... }
const speechCloudTransition: Transition    // Framer Motion transition
const speechCloudVariants: Variants        // Framer Motion variants
function OrbySpeechCloud(props: OrbySpeechCloudProps): JSX.Element

// Hooks used:
function prefersReducedMotion(): boolean   // accessibility check
function useTypedText(text: string): string  // typewriter effect
```

- Animated speech bubble above Orby
- `useTypedText()` creates typewriter animation (Community 30)
- Respects `prefers-reduced-motion` — shows text instantly if reduced

## useOrbyState — Community 36

```typescript
type OrbyState = 'idle' | 'thinking' | 'speaking' | 'navigating' | ...
type OrbyStateResult = { state: OrbyState; message: string | null }

const INTRO_COPY: string[]              // intro messages
const LAB_HINT_COPY: string[]          // Lab open hints
const SECTION_COPY: Record<string, string[]>   // per-section messages
const SECTION_TRIGGERS: string[]       // section IDs that trigger messages
type PositionModifiers = { x: number; y: number; scale: number }

function pickRandom<T>(arr: T[]): T   // random array element
function useOrbyState(): OrbyStateResult
```

- Drives what Orby says and when
- `SECTION_TRIGGERS` — which scroll sections trigger a new message
- `SECTION_COPY` — per-section copy bank (Phase 7 readiness)

## useScrollProgress — `src/components/orby/useScrollProgress.ts`

Returns normalized scroll progress (0–1) for animation lerping.

## useTypedText — `src/components/orby/useTypedText.ts`

```typescript
function useTypedText(text: string, speed?: number): string
```

Returns progressively-longer string simulating typing. Used in `OrbySpeechCloud`.

Community 30 also contains: `clearIntervalSpy`, `{ result }` — test utilities.

## Phase 7 Readiness

`docs/ORBY.md` spec defines 3 animation features for Phase 7:
1. Local Character Animation — bounce/float idle loop
2. Scroll-Progress Animation — Orby reacts to scroll position
3. Section-Triggered Messages — arrives at section → speech bubble fires

`SECTION_COPY` and `SECTION_TRIGGERS` in `useOrbyState` are already partially scaffolded for Phase 7.

## See Also
- [[../chatbot/00-orby-overview|Orby Overview]]
- [[04-three-js|Three.js / R3F (canvas patterns)]]
- [[02-lab-chat-ui|Lab UI (PanelOrby location)]]

---
tags: [portfolio, graph, community, orby, animation, speech]
---

# Communities 30, 36, 37 — Orby Animation Layer

> [[../INDEX|← Back to Index]] · [[../communities/community-overview|All Communities]]

Three tightly-coupled communities that form Orby's animation and interaction layer.

---

## Community 30 — Speech Cloud (10 nodes, cohesion 0.21)

Everything that makes Orby "speak":

```
OrbySpeechCloud.tsx
  ├── OrbySpeechCloudProps         — component props type
  ├── speechCloudTransition        — Framer Motion Transition config
  ├── speechCloudVariants          — Framer Motion Variants config
  ├── OrbySpeechCloud()            — animated speech bubble
  ├── prefersReducedMotion()       — accessibility check
  ├── useTypedText()               — typewriter hook
  ├── clearIntervalSpy             — test utility
  └── { result }                   — test result ref
```

`useTypedText(text, speed?)` — returns progressively-longer string, driving the typewriter animation. Tested in `useTypedText.test.ts`.

---

## Community 36 — Orby State (9 nodes, cohesion 0.20)

What Orby says and when:

```
useOrbyState.ts
  ├── OrbyState           — 'idle' | 'thinking' | 'speaking' | 'navigating' | ...
  ├── OrbyStateResult     — { state: OrbyState; message: string | null }
  ├── INTRO_COPY          — array of intro messages
  ├── LAB_HINT_COPY       — hints when Lab is first opened
  ├── SECTION_COPY        — per-section message arrays (Phase 7 readiness)
  ├── SECTION_TRIGGERS    — section IDs that fire messages
  ├── PositionModifiers   — { x, y, scale } for Orby position tweaks
  └── pickRandom<T>()     — random array element selector
```

`SECTION_TRIGGERS` + `SECTION_COPY` are Phase 7's data layer. When scroll enters a section in `SECTION_TRIGGERS`, Orby picks a random line from `SECTION_COPY[sectionId]`.

---

## Community 37 — Orby Canvas (7 nodes, cohesion 0.20)

The R3F rendering layer for Orby:

```
OrbyCanvas.tsx
  ├── OrbyCanvasProps      — canvas size, className, state
  └── OrbyCanvas()         — R3F Canvas wrapper

PanelOrby.tsx
  ├── PanelOrbyProps       — in-panel version props
  ├── PanelOrbyState       — 'idle' | 'thinking' | 'speaking'
  └── PanelOrby()          — in-Lab-panel Orby renderer

SceneProps                  — internal R3F scene props
AstronautProps              — 3D model animation props
```

`PanelOrby` lives in `src/components/lab/` but reaches into Community 37. It's the bridge between the Lab UI (Community 4) and the 3D rendering layer.

---

## Phase 7 Readiness Summary

| Node | File | Status |
|------|------|--------|
| `SECTION_TRIGGERS` | `useOrbyState.ts` | Scaffolded |
| `SECTION_COPY` | `useOrbyState.ts` | Scaffolded |
| Scroll-driven camera | `ObsidianBackgroundCanvas.tsx` | Done (background uses it) |
| Section entry detection | `useActiveSection.ts` | Hook exists |
| Message → speech cloud | `OrbySpeechCloud.tsx` | Done |
| Typewriter animation | `useTypedText.ts` | Done |

Phase 7 = wire `useActiveSection` → `useOrbyState` → `OrbySpeechCloud`. Infrastructure is ready.

## See Also
- [[../components/03-orby-companion|Orby Companion Detail]]
- [[../chatbot/00-orby-overview|Orby Phase 7 Spec]]

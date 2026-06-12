---
tags: [portfolio, graph, community, threejs, canvas, 3D]
---

# Community 22 — Three.js Canvas

> [[../INDEX|← Back to Index]] · [[../communities/community-overview|All Communities]]

**13 nodes · Cohesion: 0.24**

## What This Community Is

The ObsidianBackground canvas implementation — particle sphere, starfield, camera animation, and the mobile detection hook that gates particle count.

## Nodes

```
ObsidianBackgroundCanvas.tsx
  ├── useIsMobile()         — viewport < 768px check
  ├── CAM_START             — camera start position vector
  ├── CAM_END               — camera end position vector
  ├── clamp01()             — clamp value to [0, 1]
  ├── createPointSprite()   — creates THREE.Texture for points
  ├── createRing()          — creates ring BufferGeometry
  ├── createStars()         — creates starfield BufferGeometry
  └── fibonacciSphere()     — generates evenly-distributed sphere points
```

## Key Patterns

### fibonacciSphere()
Returns `Float32Array` of positions for an even point distribution on a sphere surface. Used instead of random sampling to avoid clustering at poles.

### Camera Animation
`CAM_START` → `CAM_END` lerp driven by scroll position (from `useScrollProgress`). Camera slowly pulls back as user scrolls down the page.

### Mobile Performance Gate
`useIsMobile()` gates:
- Particle count: halved on mobile
- Post-processing effects: disabled on mobile
- Ring/star geometry: simplified on mobile

### Canvas Config
```typescript
<Canvas
  dpr={[1, 2]}                        // pixel ratio cap
  performance={{ min: 0.5 }}          // auto-downgrade below 60fps
  camera={{ position: CAM_START }}
>
```

## See Also
- [[../components/04-three-js|Three.js / R3F Components]]
- [[community-07-portfolio-core|Community 7 (ObsidianBackground wrapper)]]

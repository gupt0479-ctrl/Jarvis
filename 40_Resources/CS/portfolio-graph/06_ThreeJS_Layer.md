# Portfolio Graph — Three.js / R3F Layer

## Architecture Rule
Always use **React Three Fiber (R3F)** — no raw imperative Three.js outside the R3F component tree. The canvas is `position: fixed`, `z-index: 0`, `pointer-events: none`.

## Community 22 — ObsidianBackground / Camera (cohesion 0.24)
**Nodes:** `useIsMobile()`, `CAM_END`, `CAM_START`, `clamp01()`, `createPointSprite()`, `createRing()`, `createStars()`, `fibonacciSphere()` + 5 more

The main R3F canvas scene. Key functions:
- `fibonacciSphere()` — generates evenly-distributed particle positions on a sphere
- `createPointSprite()` — creates the glowing point texture for particles
- `createRing()` — orbital ring geometry
- `createStars()` — background starfield
- `CAM_START` / `CAM_END` — scroll-driven camera path endpoints
- `clamp01()` — utility for scroll progress clamping
- `useIsMobile()` — halves particle counts on viewport < 768px

Performance rules enforced here:
- `prefers-reduced-motion` → stop `useFrame` rotations
- Mobile → halve particle counts, disable post-processing
- Canvas: `dpr={[1, 2]}`, `performance={{ min: 0.5 }}`
- Never create `new THREE.*` inside `useFrame`

## Community 23 — Education Flowchart / Blobs (cohesion 0.24)
**Nodes:** `BLOB_COLORS`, `BLOB_ICONS`, `BLOB_SIZES`, `BLOB_VARIANTS`, `BlobVariant`, `EducationFlowchart()`, `FlowchartItem`, `Props` + 4 more

The education section uses organic blob shapes (R3F `MeshDistortMaterial`) rather than flat cards. `BLOB_VARIANTS` maps education entries to visual treatments.

```tsx
// Blob pattern used:
<Float speed={0.8} rotationIntensity={0.15}>
  <mesh>
    <sphereGeometry args={[1, 64, 64]} />
    <MeshDistortMaterial color="#1E1B4B" distort={0.35} speed={1.5} transparent opacity={0.6} />
  </mesh>
</Float>
```

## Community 37 — Orby 3D Canvas (cohesion 0.2)
**Nodes:** `PanelOrby()`, `PanelOrbyProps`, `PanelOrbyState`, `AstronautProps`, `OrbyCanvas()`, `OrbyCanvasProps`, `SceneProps`

The Orby astronaut renders in a separate R3F canvas inside the Lab sidebar panel. `SceneProps` drives lighting and environment; `AstronautProps` wires the GLTF model pose.

## ObsidianBackground Contract
- File: `src/components/three/ObsidianBackground.tsx`
- Always loaded with `next/dynamic` + `{ ssr: false }` — no server render
- Reduce particle opacity/count based on scroll position over text-heavy sections
- `useFrame` only for mutations (rotation, lerp) — never create objects inside it

## ProjectsSlider
- File: `src/components/three/ProjectsSlider.tsx`
- 3D project carousel using R3F + `@react-three/drei`
- Uses `Float` for cards drifting in space

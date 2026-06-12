---
tags: [portfolio, components, threejs, R3F, 3D, animation]
---

# Three.js / R3F Components

> [[../INDEX|← Back to Index]] · [[00-overview|Component Map]]

## Files

| File | Community | Role |
|------|-----------|------|
| `src/components/three/ObsidianBackground.tsx` | 7 | Dynamic import wrapper |
| `src/components/three/ObsidianBackgroundCanvas.tsx` | 22 | Actual R3F canvas |
| `src/components/three/ProjectsSlider.tsx` | 3 | 3D project carousel |
| `src/components/orby/OrbyCanvas.tsx` | 37 | Orby 3D canvas |
| `src/components/EducationFlowchart.tsx` | 23 | Education blob flowchart |

## ObsidianBackground (Communities 7, 22)

**Two-file pattern:**
```typescript
// ObsidianBackground.tsx (Community 7) — wrapper
// Must be loaded with next/dynamic({ ssr: false })
export const ObsidianBackground = dynamic(() => import('./ObsidianBackgroundCanvas'), { ssr: false })

// ObsidianBackgroundCanvas.tsx (Community 22) — actual canvas
```

**Community 22 exports:**
```typescript
function useIsMobile(): boolean         // viewport < 768px check
const CAM_START, CAM_END               // camera position lerp targets
function clamp01(v: number): number    // clamp to [0,1]
function createPointSprite(): Texture  // creates point sprite texture
function createRing(): BufferGeometry  // creates ring geometry
function createStars(): BufferGeometry // creates starfield
function fibonacciSphere(): Float32Array // sphere point distribution
```

**Canvas contract:**
- `position: fixed`, `z-index: 0`, `pointer-events: none`
- All page content at `z-index: 1+`
- `dpr={[1, 2]}` + `performance={{ min: 0.5 }}`

## ProjectsSlider — Community 3

```typescript
function ProjectsSlider(): JSX.Element
```

- R3F canvas with floating project cards
- Uses `Float` from drei for idle drift
- Uses `@react-spring/web` for elastic spring physics on interaction:
  ```typescript
  const [springs, api] = useSpring(() => ({
    x: 0,
    config: { tension: 180, friction: 24 }
  }))
  ```
- Reads `PROJECTS_QUERY` data passed down from `PortfolioContent`

## EducationFlowchart — Community 23

```typescript
interface FlowchartItem { ... }
interface Props { ... }
type BlobVariant = 'primary' | 'secondary' | 'accent' | ...

const BLOB_COLORS: Record<BlobVariant, string>
const BLOB_ICONS: Record<BlobVariant, string>
const BLOB_SIZES: Record<BlobVariant, number>
const BLOB_VARIANTS: BlobVariant[]

function EducationFlowchart(props: Props): JSX.Element
```

- Organic blobs with `MeshDistortMaterial` from drei:
  ```typescript
  <Float speed={0.8} rotationIntensity={0.15}>
    <mesh>
      <sphereGeometry args={[1, 64, 64]} />
      <MeshDistortMaterial color="#1E1B4B" distort={0.35} speed={1.5} transparent opacity={0.6} />
    </mesh>
  </Float>
  ```
- Community 53: `amoebaIdx`, `content`, `formingIdx`, `stableIdx` — animation state indices

## R3F Rules (Enforced)

1. **Always use React Three Fiber** — no raw imperative Three.js outside R3F tree
2. **Use `@react-three/drei`** — Stars, Float, MeshDistortMaterial, Environment
3. **Never create `new THREE.*` inside `useFrame`** — mutate refs only
4. **`useMemo` for all geometries and positions**
5. **`prefers-reduced-motion`** → stop useFrame rotations, disable Float
6. **Mobile (< 768px)** → halve particle counts, disable post-processing

## Particle Sphere Pattern

```typescript
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
  useFrame((_, delta) => { if (ref.current) ref.current.rotation.y += delta * 0.05 })
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

## See Also
- [[03-orby-companion|Orby Canvas Detail]]
- [[../architecture/04-design-system|Design System (visual rules)]]

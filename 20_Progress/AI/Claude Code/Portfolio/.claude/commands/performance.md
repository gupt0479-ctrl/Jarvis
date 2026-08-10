---
description: Audit Core Web Vitals, bundle size, Three.js performance, image optimization, and client component bloat
---

# /performance

## Step 1 — Quick Static Audit

```bash
# Three.js SSR guard (must all use next/dynamic ssr:false)
grep -rn "ObsidianBackground\|ProjectsSlider" src/ --include="*.tsx" | grep -v "dynamic\|__tests__"

# Raw <img> tags (should all be next/image)
grep -rn "<img " src/ --include="*.tsx" --include="*.jsx"

# console.log left in production
grep -rn "console\." src/ --include="*.ts" --include="*.tsx" | grep -v "__tests__" | grep -v ".test."

# Client component audit in sections (could any be server?)
grep -rn "'use client'" src/components/sections/ src/components/cards/ --include="*.tsx"

# GROQ over-fetching (look for { ... } or select(*))
grep -rn "{\s*\.\.\." src/sanity/lib/queries.ts
```

## Step 2 — Build Analysis

```bash
pnpm build 2>&1 | grep -E "Route|chunks|kB|First Load"
```

Watch for:
- Any route First Load JS > 150 kB — investigate with `/docs next.js` bundle analysis
- Three.js chunk split correctly (should be dynamic, not in main bundle)

## Step 3 — ECC Deep Analysis

```
Spawn vercel:performance-optimizer agent
```

This agent covers: LCP, CLS, FID/INP, font loading, image optimization, ISR vs SSG vs SSR decision, and Vercel Edge Cache behavior.

Also reference ECC skill for Next.js caching:
```
/docs next-cache-components
```

## Step 4 — Three.js Specific

Verify in ObsidianBackground and ProjectsSlider:
- `dpr={[1, 2]}` on Canvas — never `dpr={[1, 3]}`
- `performance={{ min: 0.5 }}` on Canvas
- Mobile check halves particle count
- Post-processing disabled on mobile
- `useMemo` wraps all geometry/position arrays
- No `new THREE.*` in `useFrame` (read the component, don't grep)

## Performance Targets

| Metric | Target |
|--------|--------|
| LCP | < 2.5s |
| CLS | < 0.1 |
| First Load JS (main page) | < 200 kB |
| Three.js chunk | separate, lazy-loaded |
| Images | next/image, explicit w×h, priority on hero |

## Common Fixes

| Issue | Fix |
|-------|-----|
| Three.js in main bundle | ensure `next/dynamic({ ssr: false })` |
| LCP slow | add `priority` to hero `<Image>`, verify Sanity CDN URLs use `urlFor().width()` |
| CLS from images | explicit `width` + `height` on all `<Image>` |
| Client component too large | extract data fetch to Server Component, pass as props |

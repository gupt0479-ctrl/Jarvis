---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - claude-setup
  - frontend
  - prompts
notes:
  - "[[00 - Frontend Build Kit — Index]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Per-Phase Build Prompts
> **Reconciled to [[10 - Codebase Reality & Confusion Clearance]]** (2026-06-12). Phase order corrected; field names fixed (githubUrl, technologies[]/skills[], percentage); no renames; CSP report-only first.

Copy-paste prompts for Claude Code (Sonnet 4.8). Run each in its own session: `/clear`, paste, let it implement + `/typecheck` + visual check, review the diff, **stop (you commit — Cowork/Claude Code must not commit or deploy)**, `/clear`, next.

Path prefix: `FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`

**Every phase starts by reading `FE/10 - Codebase Reality & Confusion Clearance.md` (it has the exact file paths + field names) plus the named design note(s).**

## Phase 0 — Real content + 2 small schema touches
```
Read FE/10 - Codebase Reality & Confusion Clearance.md (Parts 1, 7, 8), FE/02 - Sanity as Single Source of Truth.md, and FE/09 - Sanity Content Spec.md fully.
Use sanity-schema. DO NOT rename technologies[]→skills[] and DO NOT add a color field — the schema is already correct. Make only two schema touches: add a long `summary` field to the project type, and add `logo` to EDUCATION_QUERY's projection. Then: delete the fake certifications (AWS SA-Pro, GCP PCA, CKA, TensorFlow, MongoDB) in Sanity; push the real skill registry (name, category enum, proficiency, percentage, tone — no color), the real projects (OpsPilot, Resq, SafeReach, AI Portfolio Agent, Jarvis, Arc) with summary + technologies[] refs + githubUrl resolved via mcp__github__search_repositories (leave liveUrl empty where undeployed, never invent), and the real experience entries. Run pnpm typegen then pnpm typecheck. Confirm no skill string is hardcoded and every section reads Sanity. Report; flag any unresolved githubUrl and ask which certs are real.
```

## Phase 1 — Motion primitives
```
Read FE/01 - Motion System & Comet Cards.md fully.
Use three-artist. Build ONE new primitive: useSpaceFloat (bounded zero-gravity drift, per-instance random phase, transform-only, hover does NOT stop it, prefers-reduced-motion returns static). Do NOT rebuild CometCard — it exists at src/components/ui/comet-card.tsx with 4 variants (default/dark/subtle/ghost) and rotateDepth/translateDepth props; just confirm it's the single hover surface. Extract the existing Experience timeline rail into a shared SpaceRail (smooth gradient, even dot glow, scroll-progress fill, slow breathing wiggle) so Achievements can reuse it. Use one shared rAF ticker or Framer's batched scheduler; no layout-affecting animation. Run pnpm typecheck and /performance. Report frame budget against ObsidianBackground.
```

## Phase 2 — Header theme pill (10 min)
```
Read FE/13 - Dark Mode Toggle.md fully.
In src/components/HeaderScrolling.tsx, convert the decorative "Dark" <div> to a real <button> using useTheme() from next-themes, with onClick a documented no-op (light mode not yet designed), aria-label "Color theme — dark mode active (light mode coming soon)", and cursor-default. Do NOT build a light palette. Run pnpm typecheck. Report.
```

## Phase 3 — ObsidianBackground enhancement
```
Read FE/11 - ObsidianBackground Enhancement.md fully.
Use three-artist. Do NOT touch the physics in ObsidianBackgroundCanvas.tsx. Add @react-three/postprocessing if absent (pnpm add). Wrap the scene in EffectComposer; add Bloom (luminanceThreshold 0.18, smoothing 0.9, intensity 0.35) and switch planet+ring PointsMaterial to additiveBlending (drop base opacity to ~0.30–0.35). Optionally add subtle ChromaticAberration and a slow HSL hue drift on COL_PLANET. Keep dpr at 1.25; gate effects OFF on mobile/reduced-motion (skipEffects). Run /performance; verify ≥~50fps on mid-range mobile, no blow-out. Report.
```

## Phase 4 — Section rebuilds (in order; one section per session is fine)
```
Read FE/10 (the relevant Part 5 section) + the section's design note, then build:
- Experience  → FE/03 - Experience Section.md  (render the Portable Text description behind a subtle bottom-right expand toggle; recolor achievements off green; add useSpaceFloat + breathing rail; header already centered)
- Projects    → FE/04 - Projects Carousel.md   (center the header in PortfolioContent.tsx; enhance the Framer slider — center comet+float, side drift no-comet keep-on-hover, tether transition, orbit dots; reveal summary + Source(githubUrl)/View-Live(only if liveUrl) on hover, capped height)
- Skills      → FE/05 - Skills Capability Graph.md (ADD the stock-chart graph from percentage on the working pill grid — do not remove it; labelled Familiarity axis, per-category lines, hover highlight + tooltip + insight panel; category pills get float+comet; skill pills compact, proficiency on hover, 7 distinct cycled effects)
- Education   → FE/06 - Education Flowchart.md  (center the header; blobs already exist; mask logos to stage; off-axis layout; upward looping living-pulse connector)
- Certifications → FE/07 (delete fakes already done in Phase 0; center description; shared chips; out-link only)
- Achievements   → FE/07 (add kicker + centered h2; move the rail OUTSIDE the box via shared SpaceRail; years tight to titles)
- Blog        → FE/08 (read BlogFeed.tsx archive-TODO first; GitHub card keeps wobble+bottom-lift+solid bg with comet polish; small cards comet + translucent)
- Contact     → FE/08 (read ContactPanel.tsx first; "frame not fill" glass frame + localized text scrim)
- Footer      → FE/08 (compact: </> far-left, year/phrase far-right, centered comet back-to-top, readable text, translucent bg, subtle top border)
Use frontend-builder (+ three-artist for the Skills graph, the projects tether, and the education pulse). Run pnpm typecheck after each. Report per section.
```

## Phase 5 — Orby friction fixes - here
```
Read FE/12 - Orby Friction Fixes.md fully.
Use frontend-builder. Do NOT touch OrbyCanvas.tsx. Fix OrbySpeechCloud right/left edge clamping (clamp cloud X into the viewport in the position logic). Now that section heights are final, recalibrate the section-comment scroll thresholds in useOrbyState.ts for projects/blog/contact. Verify no distracting Orby overlap on 375px mobile. Run pnpm typecheck. Report.
```

## Phase 6 — CSP header
```
Read FE/claude-code-setup/02 - Commands, Hooks & CSP Fix.md fully.
Use security-reviewer. next.config.ts already has HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy — only CSP is missing. Add Content-Security-Policy in REPORT-ONLY mode first (Content-Security-Policy-Report-Only) and verify zero violations across every section: ObsidianBackground/three.js renders, cdn.sanity.io images load, Orby's /api/chat + model/Upstash calls succeed. Then switch to enforcing CSP; drop 'unsafe-eval' in production if the stack allows. Do an a11y pass (accessible names + keyboard for carousel arrows, expand toggles, category buttons, back-to-top; no text overlap at mobile/1280/wide; reduced-motion respected). Run pnpm typecheck, /performance, /security-review. Report. Do NOT deploy — Anant deploys.
```

## Ordering rules
Phase 0 (content+schema) and Phase 1 (primitives) are prerequisites — never reorder. Phases 2–4 sections are independent and can be parallelised across sessions. Phase 5 needs final section heights; Phase 6 is last (CSP verification needs the finished page).

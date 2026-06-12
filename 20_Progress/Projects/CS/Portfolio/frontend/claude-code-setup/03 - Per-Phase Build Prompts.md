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
---
# Per-Phase Build Prompts
Copy-paste prompts for Claude Code (Sonnet 4.8), one per phase. Run each in its own session: `/clear`, paste, let it implement + `/typecheck` + visual check, review the diff, commit, `/clear`, next.

Path prefix (set once, mentally):
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`

## Phase 0 — Sanity as source of truth
```
Read FE/02 - Sanity as Single Source of Truth.md and FE/09 - Sanity Content Spec.md fully.
Use sanity-schema. Refactor skills into a first-class `skill` document type (name, slug, category ref, color, level, familiarity, blurb) and a `skillCategory` type, and convert experience/project/certification skill fields from inline strings to arrays of references to `skill`. Wire the fields flagged as not rendering (employmentType, description, achievements, logos, credentialUrl, slug, tagline). Build typed GROQ query modules that dereference skills[]->{name,color,slug}. Then push the real content from note 09: the skillCategory + skill registries, and the real projects (OpsPilot, Resq, SafeReach, AI Portfolio Agent, Jarvis, Arc) — remove all filler/Lovable data. Resolve each project repoUrl against my GitHub via the github MCP; leave liveUrl empty where undeployed. Do NOT invent certifications — flag note 09 §6 for me. Run /typecheck. Confirm no skill string is hardcoded anywhere and every section reads from Sanity. Report.
```

## Phase 1 — Motion primitives (build before any section)
```
Read FE/01 - Motion System & Comet Cards.md fully.
Use three-artist (or motion-systems). Build the three reusable primitives: useSpaceFloat (bounded zero-gravity drift, per-instance random phase, transform-only, hover does NOT stop it), CometCard (standardise the existing one: pointer tilt with tiltStrength prop, sheen, glow, NO vertical jump on hover), and SpaceRail (smooth gradient stroke, evenly-glowing dots, scroll-progress fill, slow breathing wiggle). Handle prefers-reduced-motion inside the primitives only. Use one shared rAF ticker or Framer Motion's batched scheduler. No layout-affecting animation. Run /typecheck and /performance. Report frame budget against the existing background sphere.
```

## Phase 2 — Experience
```
Read FE/03 - Experience Section.md fully (and re-skim FE/01 for the primitives).
Use frontend-builder. Rebuild the timeline with SpaceRail (smooth, breathing, scroll fill, dots aligned to titles). Cards: CometCard with reduced tilt + small useSpaceFloat, no hover-drop. Render employmentType next to location, wire the Sanity description (hidden by default), recolor achievements to the theme (kill the green), use the shared SkillChip (color+name only). Add the subtle bottom-right drop-down toggle that reveals the compact description on click without layout shift; card keeps drifting while expanded; single-open. Run /typecheck. Report.
```

## Phase 3 — Projects carousel
```
Read FE/04 - Projects Carousel.md fully.
Use frontend-builder (+ three-artist for the tether transition). Centre the header. Build the three-card space carousel: centre card large/dark/readable with CometCard(reduced)+useSpaceFloat bounded to padding; side cards translucent, drifting in their own padding, NO comet until centred, keep drifting on hover. Arrows vertically centred beside the card. On left/right: chosen card glides to centre (gains comet), old centre glides out (loses comet), with a subtle tether/string-pull background cue. Glowing orbit pagination dots, keep counter. Hover reveals the real Sanity summary + floating Source/View-Live buttons (hide View-Live when liveUrl empty) without ballooning the card. Keyboard + swipe work. Run /typecheck. Report.
```

## Phase 4 — Skills capability graph
```
Read FE/05 - Skills Capability Graph.md fully.
Use three-artist for the graph + effects, frontend-builder for layout. Two columns: stock-chart multi-line graph (left) from skillCategory familiarity over a 2021→2026 X-axis, Y = "Familiarity / Applied Depth" (never "Mastery"/"Expert" as the headline), per-category colored lines with distinct shapes, hover highlight + dim others + tooltip. Right: category buttons (the ONLY skills elements with useSpaceFloat+CometCard), each with its signature interaction (AI pulse, Backend cursor blink, Frontend shimmer, DevOps deploy-dots, Data tick-bars, Soft-skills wave); click reveals the category description + updates graph + an Insight panel; defaultOpen category shows on load. Listed skills compact, level shown only on hover, with one of 7 distinct per-skill effects cycled by index (build an effects[0..6] registry). Reduced-motion degrades effects. Run /typecheck and /performance. Report.
```

## Phase 5 — Education flowchart
```
Read FE/06 - Education Flowchart.md fully.
Use three-artist. Centre the header. Render three floating organic blobs parameterised by a formedness value: middle school = most deformed amoeba, high school = partly formed, college = near-perfect glowing circle; mask each school logo to its stage's perimeter. Off-axis flowchart layout: middle right, high left, college near-centre, each wobbling (useSpaceFloat) with its card (CometCard) moving as one. Dotted connectors stretch/return with the wobble; a glowing pulse travels UPWARD looping middle→high then high→college. Reduced-motion: static dotted lines with gentle opacity breathe. Content unchanged from Sanity. Mobile stacks vertically. Run /typecheck. Report.
```

## Phase 6 — Certifications, Achievements, Blog, Contact, Footer
```
Read FE/07 - Certifications & Achievements.md and FE/08 - Blog, Contact & Footer.md fully.
Use frontend-builder. Certifications: centre header, compact comet cards, SkillChip(color+name) from cert.skills refs, credential action is an out-link (credentialUrl) only, no invented certs. Achievements: ledger style with SpaceRail OUTSIDE the box (same as Experience), years tight to titles, theme-matched, low-bulk. Blog: GitHub card keeps wobble + bottom-lift + solid bg with CometCard polish; small resource cards get CometCard + more translucent bg; all from Sanity. Contact: "frame not fill" — open glass frame (thin luminous border + outer glow, transparent interior so the background sphere shows through) with a localized radial backdrop-blur scrim ONLY behind the email/buttons/socials; keep existing buttons + social pop-out. Footer: glyph (</>) far-left, "© 2026 Anant Gupta · building in public" far-right, centred back-to-top with CometCard, readable text, compact height, subtle top border, translucent bg. Run /typecheck. Report.
```

## Phase 7 — CSP, security headers, polish & ship
```
Read FE/claude-code-setup/02 - Commands, Hooks & CSP Fix.md fully.
Use security-reviewer. Add the Content-Security-Policy + security headers to next.config.ts per the note. Then verify NOTHING broke: three.js/background sphere renders, Sanity images (cdn.sanity.io) load, Orby's /api/chat + model/Upstash calls succeed, zero CSP violations in console across every section. Drop 'unsafe-eval' in production if the stack allows; document if not. Run /typecheck, /performance, and the chatbot kit's /security-review. Do an accessibility pass: every carousel arrow / drop-down toggle / category button / back-to-top has an accessible name and is keyboard-operable; no text overlap at mobile/1280px/wide; reduced-motion respected everywhere. Confirm headers on the deployed .dev URL. Then /deploy. Report the final checklist.
```

## Note on ordering
Phase 0 (Sanity) and Phase 1 (primitives) are prerequisites for everything — do not reorder them. Phases 2–6 are independent section work and can be reordered or parallelised across sessions if you want. Phase 7 must be last (CSP verification needs the finished page).

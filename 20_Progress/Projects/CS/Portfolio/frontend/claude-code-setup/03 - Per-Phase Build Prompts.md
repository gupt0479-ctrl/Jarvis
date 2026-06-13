---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-13
tags:
  - portfolio
  - claude-setup
  - frontend
  - prompts
notes:
  - "[[00 - Frontend Build Kit — Index]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[04 - Refinement Prerequisites & Deploy Checklist]]"
  - "[[BUILD-STATUS]]"
---
# Per-Phase Build Prompts — Final Refinement Pass (ship today)
> **This is the LAST build.** Sanity is set up, the GitHub link works, fake certs are gone, one real cert renders. Everything below is UI refinement. Run each phase in its own `/clear` session, paste the prompt verbatim, let it finish + `pnpm typecheck`, eyeball the result, then move on. **Claude Code does NOT commit or deploy — Anant deploys after R8 passes.** Read [[04 - Refinement Prerequisites & Deploy Checklist]] once before starting.

Path prefix: `FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`
Codebase map (graphify): `/mnt/d/.../20_Progress/Projects/CS/Portfolio/{INDEX,architecture,components,data}` — open the relevant component note for exact file paths/class names before editing.

**Stack truths:** Tailwind v4 CSS-first (tokens in `src/app/globals.css`, no config file). Projects carousel = R3F + drei `Float` + `@react-spring/web`. Education = R3F + drei `Float` + `MeshDistortMaterial`. `CometCard` at `src/components/ui/comet-card.tsx`. Colour: graph lines from `CATEGORY_COLORS`; per-skill dot from the new `skill.color`. pnpm only. Never edit `src/sanity/types/index.ts` (run `pnpm typegen`).

---
## R0 — Global: static header + section spacing
```
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`. Read FE/14 - Global Fixes — Header & Section Spacing.md fully. Files: src/components/HeaderScrolling.tsx, src/app/globals.css, the section wrappers.
Do all three:
1) Make the "Dark" theme pill STATIC — remove any useSpaceFloat/continuous-drift on it so it does not wander in the header (hover-lift ok). Confirm no other header element drifts.
2) Kill the blank box between sections: audit .section-backdrop and its ::before in globals.css. The ::before must be position:absolute; inset:0; z-index:-1; pointer-events:none with ZERO layout height — remove any min-height/margin/block sizing that injects dead space at the end of a section. Then unify section vertical padding: sections currently use py-16 / py-18 / py-24 — replace with ONE value (e.g. a --section-pad-y token or a shared <Section> wrapper) applied to every section so the gap between every consecutive section is identical.
3) Achievements is a subsection: it must NOT get the full section padding (handled visually in R6) — just make sure R0's uniform padding doesn't add a big gap before it.
ACCEPTANCE: header pill never moves on its own; no empty block between any two sections; the vertical gap between every section is identical top-to-bottom of the page.
Run pnpm typecheck. Report.
```

## R1 — Sanity schema + content
```
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`. Read FE/02 - Sanity as Single Source of Truth.md and FE/09 - Sanity Content Spec.md fully. Use the sanity-schema agent.
Schema edits ONLY (no renames, no skillCategory doc, no familiarity/level/blurb):
- Add skill.color: a preset string enum {violet, cyan, emerald, sky, pink, amber, orange, slate} each mapped to a hex in ONE place. Default each skill's color to its category colour; the dot uses skill.color everywhere EXCEPT the Skills section, falling back to category colour when unset.
- Add project.summary (long text) for the carousel hover.
- Make project.coverImage OPTIONAL (remove the required validation so projects publish without one).
- Remove project.visibility entirely; rely on featured (bool) + order; drop visibility from PROJECTS_QUERY normalization.
- Add logo to EDUCATION_QUERY projection.
Then content: set color on every skill; confirm the 6 projects have summary + githubUrl + ≤relevant technologies (liveUrl empty where undeployed); confirm experience Portable Text description is populated.
Run pnpm typegen then pnpm typecheck.
ACCEPTANCE: studio publishes a project with no cover image; every skill has a color; project.visibility is gone; education query returns logo.
Report.
```

## R2 — Experience
```
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`. Read FE/03 - Experience Section.md fully. Files: cards/ExperienceCard.tsx, sections/ExperienceSection.tsx.
1) MOVE the employment-type chip (Contract/Internship/Freelance) from the TITLE row to the LOCATION row — it currently sits next to the position title; it must sit next to the location (MapPin) line. Title row keeps only the title.
2) Recolour the achievement ★ lines OFF gold/yellow to a theme tone (blue/violet/cyan from the design tokens) that matches the card.
3) The Portable Text description currently renders always-open below the chips — HIDE it by default and reveal on click via a very subtle "more" toggle at the bottom-right of the card (low opacity, gains presence on hover, accessible name). Open into a SMALL in-card dropdown (not full-screen), single-open, no sibling layout shift, card keeps its gentle drift.
4) Dial the CometCard tilt DOWN (it swings too much on hover) — keep the hover feel, reduce magnitude.
5) Each skill chip's dot uses skill.color from Sanity (fallback category colour). Everything Sanity-rendered.
ACCEPTANCE: type chip beside location; achievements not gold; description hidden until "more" is clicked; gentler tilt; coloured dots from Sanity.
Run pnpm typecheck. Report.
```

## R3 — Projects (R3F carousel)
```
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`. Read FE/04 - Projects Carousel.md fully. Files: three/ProjectsSlider.tsx (R3F + drei Float + @react-spring/web), PortfolioContent.tsx (header).
1) Reduce the centre card's comet/tilt AND its drei Float amplitude so the motion is subtle and stays within the card's own padding.
2) DECOUPLE the side cards from the centre card's hover: when the centre is hovered the left/right cards must NOT move with it — they keep their own gentle Float and current translucent opacity. (Comet only when a side card becomes the centre — already correct; keep.)
3) Remove the "case note" box; show ONLY the project summary in that inner box (keep the truncation — it should not overflow).
4) Render at most 4 technologies chips per project, dots from skill.color.
5) Reflect R1: coverImage optional (hide the banner gracefully when absent), visibility removed; hide the View-Live button when liveUrl is empty; Source uses githubUrl.
ACCEPTANCE: centre motion subtle + bounded; side cards unaffected by centre hover; no case-note (summary only); ≤4 chips; no broken layout when a project has no cover image.
Run pnpm typecheck. Report.
```

## R4 — Skills
```
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`. Read FE/05 - Skills Capability Graph.md fully. Files: sections/SkillsSection.tsx, sections/SkillsSectionClient.tsx (Recharts via shadcn ChartContainer).
Layout:
1) DELETE the coloured count-pills row entirely (the "Ai Ml 7 · Backend 8 · …" coloured row).
2) Fold the counts onto the real category filter buttons so each button reads e.g. "Ai Ml 7", "Backend 8". One row of category buttons, each with its count.
3) Remove the "All" button entirely; default-open the highest category on load.
4) Keep "N skills across M categories" as a small caption that adds NO vertical height.
5) Align the graph (left) and the category-buttons + skills (right) on one row; remove the empty gap between the section header and the content (tighten top padding).
Behaviour:
6) Make each category's graph trajectory a DISTINCT shape (different slopes/inflections/plateaus from each category's percentage values + a per-category offset) — no two lines parallel. Axes labelled (X year, Y "Familiarity / Applied Depth", never "Mastery").
7) Category-first: the chosen category reveals its skills; not one flat list of all skills.
8) Give mobile, soft-skills, and testing their OWN unique category hover effects (they currently share one). Keep the existing distinct ones (frontend shimmer / backend cursor / ai-ml pulse / devops deploy-dots / database sparkline / soft-skills lift) and differentiate the duplicates.
9) 7 distinct per-skill hover effects cycled across skills (index % 7). The skill box MUST be a FIXED size — it must NOT grow/reshape on hover; only the effect + the proficiency level appear on hover.
10) Do NOT render the skill.color dot in the Skills section (hover effect + level only here).
ACCEPTANCE: one category-button row with counts, no coloured pills row, no "All", no header gap, graph+skills aligned; lines diverge; fixed-size skill boxes; 7 effects; unique effect per category.
Run pnpm typecheck and /performance. Report.
```

## R5 — Education (R3F)
```
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`. Read FE/06 - Education Flowchart.md fully. File: EducationFlowchart.tsx (R3F + drei Float + MeshDistortMaterial; BLOB_VARIANTS/COLORS/SIZES).
1) Equalize OPACITY (and size) across all three blobs — deformation must be the ONLY visible difference.
2) Set MeshDistortMaterial.distort per stage: middle school most deformed (~0.45), high school partly formed (~0.22, NOT a clean circle), college a perfect circle (~0, most stable/glowing).
3) Reposition off-axis (flowchart, not a straight line): high school to the LEFT, middle school to the RIGHT, college near-centre (not exactly centre); each wobbles in its own area via Float.
4) Replace the connector glow with ONE upward-travelling dot that goes middle(right) → high(left) → college, looping; the dotted line stretches/returns as the blobs wobble. reduced-motion: static dotted line, no travelling dot.
5) Each stage card gets a SUBTLE CometCard (less than other sections) and moves with its blob.
6) Mask each school logo (now in EDUCATION_QUERY) to its blob's perimeter; centre the section header.
ACCEPTANCE: three blobs same opacity, distinguished only by distort; off-axis layout; single looping upward dot; subtle card comet; centered header.
Run pnpm typecheck. Report.
```

## R6 — Certifications + Achievements
```
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`. Read FE/07 - Certifications & Achievements.md and FE/14 (§3) fully. Files: CertificationsSection.tsx, AchievementsSection.tsx.
Certifications:
1) Reduce the CometCard tilt (too strong). Keep the holographic corner.
2) Skill chips show colour + name only, dot from skill.color; credential action is a single out-link (credentialUrl). (Fakes already deleted; one real cert renders — leave it.)
Achievements (subsection of Certifications):
3) Make the header noticeably SMALLER than a top-level section heading, centered, with ALMOST NO gap below Certifications (remove the section-backdrop dead space here).
4) Wrap ALL THREE achievements in a SINGLE transparent-background CometCard whose motion is very subtle (less than education) — NOT one card per achievement. Keep ledger content (year, title, type, issuer, one-line, external link) from Sanity; years tight to titles.
ACCEPTANCE: cert tilt gentler + out-link only; achievements small centered header, minimal gap, one subtle transparent comet wrapping all three.
Run pnpm typecheck. Report.
```

## R7 — Blog, Contact, Footer
```
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`. Read FE/08 - Blog, Contact & Footer.md fully. Files: BlogSection.tsx/BlogFeed.tsx, ContactSection.tsx/ContactPanel.tsx, Footer.tsx.
Blog:
1) Centre the kicker + heading + description (currently left).
2) Make all card motion subtle (too much movement now).
3) GitHub pinned card: REPLACE the comet with the bottom-half-lift hover (on hover only the bottom half of the card lifts; top stays). KEEP its left colour rail + MagneticButton Visit + solid background.
4) Small resource cards: translucent background + subtle comet.
Contact:
5) Make the card slightly SMALLER so more of the background shows around it; keep text + buttons clearly readable; keep the social pop-out.
Footer:
6) </> glyph at the EXTREME left; "© 2026 Anant Gupta · building in public" at the EXTREME right; Back-to-top button centred with a subtle CometCard; raise footer text to readable (not dim/glowing); shrink height to minimum; very subtle top border; translucent background so the page background shows through.
ACCEPTANCE: blog header centered + subtle motion + GitHub bottom-lift; smaller contact card with readable content; footer edge-aligned, compact, translucent, centred back-to-top.
Run pnpm typecheck. Report.
```

## R8 — Orby frictions + a11y + (optional) CSP — final gate
```
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`. Read FE/12 - Orby Friction Fixes.md and FE/claude-code-setup/02 - Commands, Hooks & CSP Fix.md fully.
Orby (do NOT touch OrbyCanvas.tsx): clamp OrbySpeechCloud X into the viewport so it never clips at Orby's far-right home; recalibrate the section-comment scroll thresholds in useOrbyState.ts now that heights/spacing changed in R0–R7; check 375px mobile overlap.
A11y: accessible names + keyboard on the "more" toggles, carousel nav, category buttons, back-to-top; no text overlap at mobile/1280/wide; prefers-reduced-motion respected (Float, distort pulse, useSpaceFloat).
CSP (optional for today — can ship without and add right after): next.config.ts already has HSTS/X-CTO/X-Frame/Referrer/Permissions; add Content-Security-Policy in REPORT-ONLY first and verify zero violations (three.js, cdn.sanity.io images, /api/chat + Upstash) before enforcing.
Run pnpm typecheck, pnpm build, /performance. Report a GREEN-LIGHT checklist (typecheck clean, build clean, no console errors, every section's acceptance met). Do NOT deploy — Anant runs the Vercel deploy.
```

## Order & "done today"
R0 → R1 first (everything depends on them). R2–R7 are independent — run in any order, one session each. R8 last. After R8 reports green, Anant deploys. CSP can follow the deploy if time is tight (the other security headers already ship).

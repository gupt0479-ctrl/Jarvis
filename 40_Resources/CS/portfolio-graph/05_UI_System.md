# Portfolio Graph — UI System

## Visual Identity: "Floating Portfolio Command Center in Space"
Dark cosmic theme — violet/cyan accents, translucent cards, backdrop blur. Never deviate.

### Color Tokens
| Token | Value |
|-------|-------|
| Background | `rgba(9, 10, 18, 1)` |
| Card surface (low) | `rgba(9, 10, 18, 0.72)` |
| Card border | `rgba(167, 139, 250, 0.22)` |
| Accent violet | `#7C3AED` / `#A78BFA` |
| Accent cyan | `#06B6D4` / `#67E8F9` |

## Community 6 — shadcn/Sidebar Core (cohesion 0.12)
**Nodes:** `cn()`, `Input()`, `Separator()`, `SidebarFooter()`, `SidebarGroup()`, `SidebarGroupAction()`, `SidebarGroupContent()`, `SidebarGroupLabel()` + 22 more

`cn()` is the #1 god node (96 edges) — it lives here and is called by every component in the tree. The sidebar primitives are shadcn-based and power the Lab panel.

## Community 3 — Contact & Social UI (cohesion 0.07)
**Nodes:** `ContactPanel()`, `ContactProfile`, `IridSocialButton()`, `SocialLinks`, `useIridescentEffect()`, `UseIridescentEffectOptions`, `formatCategory()`, `normalizeCategoryKey()` + 30 more

`useIridescentEffect()` is the 10th god node (15 edges) — it powers the hover shimmer on all social/contact buttons. Used across contact section, social links, and more.

## Community 12 — About / Telemetry Cards (cohesion 0.16)
**Nodes:** `AboutTelemetry()`, `CANONICAL_READOUTS`, `CanonicalReadout`, `findStat()`, `SPARKLINE_BARS`, `STAT_ICONS`, `TelemetryCard()`, `TelemetryCardProps` + 8 more

The animated stat cards in the About section. `CANONICAL_READOUTS` defines what stats are shown; `findStat()` maps Sanity data to the readout shape.

## Community 13 — Certifications (cohesion 0.17)
**Nodes:** `CertificationsSection()`, `CERTS_SECTION_QUERY`, `CertWithSkills`, `getGlareOverlay()`, `getInnerCard()`, `glare`, `inner` + 7 more

The certifications section uses a glare/inner-card pattern (`getGlareOverlay()`, `getInnerCard()`) for the flip-card hover effect.

## Community 47 — shadcn Card Primitives (cohesion 0.25)
**Nodes:** `Card()`, `CardAction()`, `CardContent()`, `CardDescription()`, `CardFooter()`, `CardHeader()`, `CardTitle()`

All call `cn()` — feeds into the god node's 96 edges.

## CometCard Contract (`src/components/ui/comet-card.tsx`)
The floating 3D-tilt card primitive. Variants:
- `default` — standard tilt, up to 12deg
- `dark` — more opaque (0.88), reduced tilt (max 8deg)
- `subtle` — lighter surface

Rules:
- Always: `backdrop-filter: blur(12px)`, `border: 1px solid rgba(167,139,250,0.22)`
- Hover: `translateY(-6px)`, brighter border, stronger glow
- Respects `prefers-reduced-motion` — disables tilt

## Global CSS Utilities (`src/app/globals.css`)
- `.cosmic-card` / `.cosmic-card--dark` / `.cosmic-card--subtle`
- `.float-btn` — floating button with shadow + lift
- `.section-kicker` — monospace code-style section label
- `.orbit-chip` — small tag/badge
- `.section-backdrop` — section background blur

## Community 10 — CSS Test Suite (cohesion 0.07)
**Nodes:** `aboutPath`, `cometCardPath`, `css`, `CTA_HREFS`, `floatBtnRule`, `GLOBALS_CSS_PATH` + 17 more

There are Vitest tests that parse `globals.css` to assert `.cosmic-card` and `.float-btn` rules exist with correct values — design system regression testing.

## Community 17 — Evidence Cards (cohesion 0.12)
**Nodes:** `ExperienceEvidenceCard()`, `ExperienceEvidenceCardProps`, `formatDate()`, `formatDateRange()`, `Project`, `ProjectEvidenceCard()`, `ProjectEvidenceCardProps` + 7 more

Rich cards shown in the chat when Orby calls `showProject` or `showExperience` tools.

## Section Kickers (monospace labels above headings)
| Section | Kicker |
|---------|--------|
| Hero | `// hi, I'm` |
| About | `// scan report` |
| Experience | `// trajectory` |
| Projects | `// build log` |
| Skills | `// capability matrix` |
| Education | `// origins` |
| Blog/Contact | `// uplink` |

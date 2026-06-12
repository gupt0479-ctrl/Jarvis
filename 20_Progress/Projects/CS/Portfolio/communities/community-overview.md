---
tags: [portfolio, graph, communities, overview]
---

# All 99 Communities — Overview

> [[../INDEX|← Back to Index]]

Graph detected 99 communities (79 shown, 20 thin omitted). Listed by ID with cohesion score, size, and key nodes.

## High-Cohesion Communities (≥ 0.3) — Tightest Clusters

| ID | Cohesion | Size | What |
|----|----------|------|------|
| 48 | 0.57 | 5 | **Clerk proxy** — `clerk`, `config`, `event`, `isPublicRoute`, `proxy()` |
| 53 | 0.53 | 4 | **Amoeba animation** — `amoebaIdx`, `content`, `formingIdx`, `stableIdx` |
| 59 | 0.60 | 3 | **Section backdrop** — `content`, `readSrc()`, `sectionsWithBackdrop` |
| 57 | 0.40 | 3 | **Studio auth** — `config`, `isPublicRoute`, `isStudioRoute` |
| 67 | 0.60 | 3 | **Sidebar state** — `SidebarToggle()`, `Sidebar()`, `useSidebar()` |
| 34 | 0.36 | 7 | **Blog section** — `BlogFeed()`, `BlogSection()`, `MagneticButton()`, `PINNED_GITHUB`, `BLOG_SECTION_QUERY` |
| 39 | 0.36 | 8 | **Security test** — `getAllSourceFiles()`, `BANNED_STRINGS`, `EXCLUDED_FILES`, `violations` |
| 29 | 0.29 | 9 | **Experience section** — `ExperienceSection()`, `ExperienceCard()`, `CATEGORY_COLORS`, `EMPLOYMENT_LABELS`, `getCategoryColor()` |
| 31 | 0.27 | 11 | **Dummy data docs** — import instructions, statistics, singleton docs |
| 22 | 0.24 | 13 | **Canvas / mobile** — `useIsMobile()`, `CAM_END`, `CAM_START`, `clamp01()`, `createPointSprite()`, `createRing()`, `createStars()`, `fibonacciSphere()` |
| 23 | 0.24 | 12 | **Education blobs** — `BLOB_COLORS`, `BLOB_ICONS`, `BLOB_SIZES`, `BLOB_VARIANTS`, `EducationFlowchart()` |

## Medium Communities (0.10 – 0.29) — Feature Clusters

| ID | Cohesion | Size | What |
|----|----------|------|------|
| 32 | 0.20 | 4 | **Orby core** — `Orby()`, `OrbyArrow()`, `getPose()` |
| 30 | 0.21 | 10 | **Speech cloud** — `OrbySpeechCloud()`, `useTypedText()`, `speechCloudVariants`, `prefersReducedMotion()` |
| 37 | 0.20 | 7 | **Orby canvas** — `PanelOrby()`, `OrbyCanvas()`, `SceneProps`, `AstronautProps` |
| 36 | 0.20 | 9 | **Orby state** — `OrbyState`, `SECTION_COPY`, `SECTION_TRIGGERS`, `pickRandom()`, `INTRO_COPY`, `LAB_HINT_COPY` |
| 12 | 0.16 | 16 | **About/telemetry** — `AboutTelemetry()`, `TelemetryCard()`, `CANONICAL_READOUTS`, `STAT_ICONS`, `SPARKLINE_BARS` |
| 13 | 0.17 | 15 | **Certs + CometCard** — `CertificationsSection()`, `CometCard()`, `getGlareOverlay()`, `getInnerCard()` |
| 17 | 0.12 | 15 | **Evidence + experience** — `ExperienceEvidenceCard()`, `ProjectEvidenceCard()`, `ToolResultRenderer()`, `formatDate()` |
| 15 | 0.17 | 14 | **Queries + hero** — `Orby` (loader), `urlFor()`, `PROFILE_QUERY`, `PROJECTS_QUERY`, `ACHIEVEMENTS_QUERY` |
| 9 | 0.15 | 22 | **Nav + header** — `HeaderScrolling()`, `buildNavItems()`, `CORE_NAV`, `NavLink()`, `SECTION_IDS` |
| 4 | 0.09 | 48 | **Lab UI** → [[community-04-lab-ui\|full detail]] |
| 7 | 0.13 | 33 | **Portfolio core** → [[community-07-portfolio-core\|full detail]] |
| 1 | 0.05 | 67 | **Chatbot backend** → [[community-01-chatbot-backend\|full detail]] |

## GROQ Documentation Communities

| ID | Cohesion | What |
|----|----------|------|
| 27 | 0.14 | Education + siteSettings GROQ examples |
| 38 | 0.18 | Blog GROQ queries |
| 42 | 0.22 | Skills GROQ queries |
| 43 | 0.22 | Project GROQ queries |
| 50 | 0.29 | Combined/complex GROQ queries |
| 51 | 0.29 | Contact GROQ queries |
| 56 | 0.33 | GROQ pro tips |
| 61 | 0.40 | Count & statistics queries |
| 62 | 0.40 | Profile queries |
| 63 | 0.40 | Certifications queries |
| 64 | 0.40 | Achievements queries |
| 65 | 0.40 | Experience queries |

## Data Import / Documentation Communities

| ID | Cohesion | What |
|----|----------|------|
| 8 | 0.06 | Data overview + statistics + singleton docs |
| 16 | 0.10 | NDJSON data files list |
| 31 | 0.27 | Dummy data import docs |
| 33 | 0.17 | Sanity CLI troubleshooting |
| 40 | 0.20 | Environment variables + import methods |
| 44 | 0.22 | Sanity dataset import commands |
| 52 | 0.29 | Data customization instructions |
| 66 | 0.40 | Data cleanup / deletion commands |
| 71 | 0.50 | Verify import success |

## UI Primitive Communities

| ID | Cohesion | What |
|----|----------|------|
| 6 | 0.12 | `cn()` + sidebar sub-components + Input + Tooltip |
| 24 | 0.22 | Dropdown menu primitives |
| 28 | 0.16 | Chart (Recharts): ChartContainer, ChartTooltipContent |
| 47 | 0.25 | Card: Card(), CardHeader(), CardTitle(), CardContent()… |

## Test / Edge Communities

| ID | Cohesion | What |
|----|----------|------|
| 25 | 0.13 | CSS test utilities: `floatBtnMatch`, `glowElements`, `MotionDiv` |
| 26 | 0.14 | E2E test refs: `assistantWrappers`, `chatInput`, `closeBtn`, `labButton` |
| 39 | 0.36 | Banned strings security test: `BANNED_STRINGS`, `EXCLUDED_FILES`, `getAllSourceFiles()` |
| 45 | 0.25 | IO callback mocks for tests |
| 46 | 0.25 | IntersectionObserver mocks: `MockObserverInstance`, `SECTION_TEXTS` |

## Planning / Documentation Communities

| ID | Cohesion | What |
|----|----------|------|
| 11 | 0.08 | CLAUDE.md sections: Architecture, Build Pipeline, AI Chatbot phases |
| 14 | 0.09 | AGENTS.md sections: ECC workflow, Codex hooks, agent delegation |
| 18 | 0.11 | README: install/setup commands, env vars |
| 19 | 0.11 | Orby Phase 7 spec (copy A) — Section-Triggered Messages, Acceptance Criteria |
| 20 | 0.11 | ECC plugin usage examples |
| 21 | 0.11 | Orby Phase 7 spec (copy B — duplicate detection) |

## Low-Cohesion / Broad Communities

| ID | Cohesion | Size | What |
|----|----------|------|------|
| 0 | 0.07 | 67 | Local content / type utilities: `asBoolean()`, `asNumber()`, `getLocalAchievements`, type guards |
| 2 | 0.06 | 20 | Sanity config: `builder`, `serverClient`, `assertValue()`, `dataset`, `projectId`, `structure()` |
| 3 | 0.07 | 38 | UI/contact cluster: `ContactPanel()`, `useIridescentEffect()`, `IridSocialButton()`, `ProjectsSlider()`, `HeroContent()` |
| 5 | 0.06 | 28 | Root layout cluster: `lora`, `ubuntu`, `RootLayout()`, `AppSidebar()`, `ChatTokenInit()`, `Providers()`, `ThemeProvider()` |
| 10 | 0.07 | 25 | CSS test + design system test: `CTA_HREFS`, `driftMatch`, `floatBtnRule`, `GLOBALS_CSS_PATH` |

## 20 Thin Communities (< 3 nodes, omitted from main report)

These are isolated sub-graphs too small to cluster meaningfully. Run `graphify query` on specific nodes to explore them.

## See Also
- [[../god-nodes|God Nodes]]
- [[community-01-chatbot-backend|Community 1 Detail]]
- [[community-04-lab-ui|Community 4 Detail]]
- [[community-07-portfolio-core|Community 7 Detail]]

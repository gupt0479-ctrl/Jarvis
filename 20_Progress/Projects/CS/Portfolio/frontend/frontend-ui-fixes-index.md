# Frontend UI Fixes — Component Index

> **Folder:** `20_Progress/Projects/CS/Portfolio/frontend/`
> **Updated:** 2026-09-05
> Each linked note below is a **standalone, implementation-ready spec** for one fix area. Use with [[frontend-ui-fixes-tasks]] prompts.

## Master docs (read first)

| Doc | Role |
|---|---|
| [[UI Fixes]] | Human walkthrough + status ledger (Sep 2026 ground truth) |
| [[frontend-ui-fixes-requirements]] | Success criteria per fix area |
| [[frontend-ui-fixes-design]] | Architecture, GSAP patterns, animation matrix |
| [[frontend-ui-fixes-tasks]] | Phased tasks + copy-paste agent prompts |

## Per-component specs (build from these)

| # | Component spec | Primary files | Phase |
|---|---|---|---|
| 1 | [[ui-fix-01-hero-background]] | `ObsidianBackgroundCanvas.tsx`, `HeroContent.tsx`, `ProfileImage.tsx` | 2 |
| 2 | [[ui-fix-02-about-section]] | `AboutSectionClient.tsx`, `about-pin.ts` (new) | 3 |
| 3 | [[ui-fix-03-about-telemetry]] | `AboutTelemetry.tsx`, `TelemetryDetail.tsx` (remove usage) | 3 |
| 4 | [[ui-fix-04-projects-section]] | `ProjectsSlider.tsx`, `projects-pin.ts` (new) | 4 |
| 5 | [[ui-fix-05-education-section]] | `EducationFlowchart.tsx`, `EducationSection.tsx` | 5 |
| 6 | [[ui-fix-06-logo-footer]] | `logoGlyphPath.ts`, `HeaderLogo*.tsx`, `Footer.tsx` | 6 |
| 7 | [[ui-fix-07-portfolio-lab]] | `ChatInputBar.tsx`, `ChatThread.tsx`, `sidebar.tsx` | 6–7 |
| 8 | [[ui-fix-08-carry-forward]] | Skills, Experience, Orby, dark mode, deploy | 7–8 |

## Superseded (do not build)

- July 4-card telemetry accordion → see [[ui-fix-03-about-telemetry]]
- Education entry-only stagger → see [[ui-fix-05-education-section]]
- Projects auto-play only → see [[ui-fix-04-projects-section]]

## Suggested build order

```
0.1 deploy sync → 1.1 Sanity → 2.1/2.2 hero → 3.0 GSAP research
→ 3.1–3.4 About → 4.1–4.2 Projects → 5.1–5.4 Education
→ 6.1–6.3 logo/lab → 7.x carry-forward → 8.1 QA
```

## Cross-references (do not use as open work)

- `frontend/Ran/` — prior shipped round
- `frontend/claude-code-setup/` — process/tooling only
- `frontend/claude-prompt-ui-fixes-*.md` — prior prompt generations; superseded by Sep 2026 trio + component specs

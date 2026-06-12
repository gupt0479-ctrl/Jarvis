# Portfolio Graph — Tests & Configuration

## Community 39 — Source Guard Tests (cohesion 0.36)
**Nodes:** `allFiles`, `BANNED_STRINGS`, `content`, `EXCLUDED_FILES`, `getAllSourceFiles()`, `relativePath`, `srcDir`, `violations`

A Vitest test that scans all source files for banned strings — catches things like hardcoded API keys, `console.log`, or forbidden imports. `BANNED_STRINGS` is the allowlist-reject list; `EXCLUDED_FILES` carves out test files themselves.

## Community 45 — IO Mocks (cohesion 0.25)
**Nodes:** `IOCallback`, `MockIOInstance`, `mockIOs`, `{ result }`

Mock `IntersectionObserver` utilities used by tests that depend on scroll-based visibility. Pattern: replace global IO with a `MockIOInstance` that fires callbacks manually.

## Community 46 — Observer Mocks (cohesion 0.25)
**Nodes:** `el`, `IntersectionCallback`, `MockObserverInstance`, `mockObservers`, `{ result }`, `SECTION_TEXTS`

Similar mock infrastructure for the section-detection observer. `SECTION_TEXTS` provides expected copy strings for assertion.

## Community 25 — CSS Regression Tests (cohesion 0.13)
**Nodes:** `aboutPath`, `css`, `floatBtnMatch`, `globalsPath`, `glowElements`, `mockProfile`, `MotionDiv` + 6 more

Vitest tests that read `globals.css` and assert design tokens exist:
- `.float-btn` has correct `box-shadow` rule
- `.cosmic-card` has `backdrop-filter: blur(12px)`
- Glow elements have the right color values

## Community 26 — E2E / Playwright Smoke (cohesion 0.14)
**Nodes:** `assistantWrappers`, `chatInput`, `closeBtn`, `cloud`, `el`, `ERRORS`, `labButton`, `orbyWrapper` + 4 more

End-to-end tests for the Orby chatbot flow. Key selectors:
- `labButton` — opens the Lab sidebar
- `orbyWrapper` — the Orby character container
- `chatInput` — the chat input field
- `cloud` — the speech cloud
- `assistantWrappers` — assistant message bubbles

## Test Commands
```bash
pnpm test          # Vitest run (all unit tests)
pnpm test:watch    # Vitest watch mode
pnpm e2e           # Playwright E2E (via /e2e skill)
```

## Build Config Files
| File | Role |
|------|------|
| `next.config.ts` | Next.js config (security headers, image domains) |
| `vitest.config.ts` | Vitest + jsdom + @testing-library/react |
| `playwright.config.ts` | E2E test config |
| `biome.json` | Linter/formatter (never add ESLint or Prettier) |
| `sanity.config.ts` | Sanity Studio config |
| `sanity.cli.ts` | Sanity CLI config |
| `postcss.config.mjs` | PostCSS for Tailwind v4 |

## Community 18 — Setup & README (cohesion 0.11)
**Nodes:** `Anant Gupta Portfolio`, install commands, env setup — the repo README as extracted nodes.

Key setup sequence:
1. `pnpm install`
2. Set env vars (SANITY project ID, Clerk keys, etc.)
3. `pnpm typegen`
4. `pnpm dev`

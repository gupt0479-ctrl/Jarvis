---
tags: [portfolio, nextjs, app-router, routes]
---

# Next.js App Router

> [[../INDEX|← Back to Index]] · [[00-overview|Architecture Overview]]

## Route Tree

```
src/app/
├── layout.tsx                          # Root layout — fonts, Providers, ChatTokenInit
├── (portfolio)/
│   ├── layout.tsx                      # Portfolio layout — ObsidianBackground, AppSidebar, HeaderScrolling
│   └── page.tsx                        # Home() — calls sanityFetch, renders PortfolioContent
├── studio/
│   ├── layout.tsx                      # Studio layout — Clerk-guarded
│   └── [[...tool]]/
│       ├── page.tsx                    # Studio page — server entry
│       └── StudioClient.tsx            # Client-side Sanity Studio render
├── sign-in/[[...sign-in]]/page.tsx     # Clerk sign-in
├── sign-up/[[...sign-up]]/page.tsx     # Clerk sign-up
└── api/
    ├── chat/
    │   └── route.ts                    # POST — Orby chat endpoint
    ├── chat-token/
    │   └── route.ts                    # Issues HMAC session cookie
    └── draft-mode/
        ├── enable/route.ts             # Sanity draft mode on
        └── disable/route.ts            # Sanity draft mode off
```

## Page Components

### Home() — `src/app/(portfolio)/page.tsx`
- Server component
- No data fetching directly — delegates to `PortfolioContent()`
- Wraps in `<Suspense>` for streaming

### PortfolioContent() — `src/components/PortfolioContent.tsx`
- **Community 7** — the portfolio core
- Server component that orchestrates all section fetches
- Calls `sanityFetch()` for every section query in parallel
- Renders: HeroSection → AboutSection → ExperienceSection → ProjectsSlider → SkillsSection → EducationSection → CertificationsSection → AchievementsSection → BlogSection → ContactSection → Footer

## Root Layout — `src/app/layout.tsx`
**Community 5** nodes:
- `lora` / `ubuntu` — Google font imports
- `RootLayout()` — wraps with `Providers`, `ThemeProvider`, `ChatTokenInit`
- `Providers()` — ClerkProvider + SidebarProvider
- `ChatTokenInit` — client component that fetches HMAC cookie on mount
- `ThemeProvider()` — next-themes dark mode

## Portfolio Layout — `src/app/(portfolio)/layout.tsx`
- Loads `ObsidianBackground` via `next/dynamic` (SSR: false)
- Renders `AppSidebar` + `HeaderScrolling`
- `layout.tsx` uses `SidebarProvider` context

## API Routes

### POST /api/chat — `src/app/api/chat/route.ts`
See [[../chatbot/01-api-route|Chatbot API Route]] for full detail.
Key exports: `redis`, `burstLimit`, `dailyLimit`, `isAllowedOrigin()`, `POST()`

### POST /api/chat-token — `src/app/api/chat-token/route.ts`
- Issues a short-lived HMAC-signed JWT in a cookie
- Cookie is `httpOnly`, `sameSite: strict`
- Read by the chat route to verify origin

## Server Actions

### submitContactForm() — `src/app/actions/submit-contact-form.ts`
- Server Action for the contact form
- Writes to Sanity via `getServerClient()`
- Part of Community 1 (chatbot backend cluster — shares server-client infrastructure)

## Proxy / Middleware

Two proxy files exist — only one is active:
- `proxy.ts` (root) — Community 48, contains `clerk`, `isPublicRoute`, `event`, `config`, `proxy()`
- `src/proxy.ts` — Community 57, contains `isPublicRoute`, `isStudioRoute`, `config`

`isPublicRoute` allows all portfolio routes. `isStudioRoute` gates `/studio/*` behind Clerk auth.

## See Also
- [[02-sanity-cms|Sanity CMS]]
- [[03-auth-clerk|Auth (Clerk)]]
- [[../chatbot/01-api-route|Chatbot API Route]]

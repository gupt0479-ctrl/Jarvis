---
tags: [portfolio, sanity, cms, groq]
---

# Sanity CMS Layer

> [[../INDEX|← Back to Index]] · [[00-overview|Architecture Overview]]

## Overview

Sanity v4 is the **only** content source. `sanityFetch()` is the **only** way to read data — no direct client calls from components. Community 7 owns the live data layer; Community 2 owns the schema/config layer.

## Core Files

| File | Role | Community |
|------|------|-----------|
| `src/sanity/lib/live.ts` | `sanityFetch()`, `hasUsableData()`, `loadLocalQueryResult()` | 7 |
| `src/sanity/lib/queries.ts` | All GROQ queries | 15 |
| `src/sanity/lib/client.ts` | `client` — public read client | 2 |
| `src/sanity/lib/server-client.ts` | `getServerClient()` — write/auth client | 1 |
| `src/sanity/lib/image.ts` | `urlFor()`, `builder` | 2/15 |
| `src/sanity/env.ts` | `projectId`, `dataset`, `assertValue()` | 2 |
| `src/sanity/structure.ts` | `structure()` — studio desk structure | 2 |
| `src/sanity/types/index.ts` | GENERATED — all TypeScript types | 0 |
| `src/sanity/schemaTypes/index.ts` | Schema registry (`schema` export) | 2 |

## sanityFetch() — Community 7's Hub Node (35 edges)

```typescript
// src/sanity/lib/live.ts
export async function sanityFetch<T>({ query, params }: { query: string; params?: Record<string, unknown> }): Promise<T>
```

- Wraps `next-sanity` live content API
- Falls back via `loadLocalQueryResult()` if Sanity is unreachable
- `hasUsableData()` — validates result before use
- `createFetchFallback()` — creates a fallback fetcher

## Schema Types (Community 2)

11 document types registered in `src/sanity/schemaTypes/index.ts`:

| Type | File | Purpose |
|------|------|---------|
| `profile` | profile.ts | Main bio, headline, avatar |
| `experience` | experience.ts | Work history entries |
| `project` | project.ts | Portfolio projects |
| `skill` | skill.ts | Skills with categories |
| `education` | education.ts | Degrees, institutions |
| `certifications` | certifications.ts | Certs with issue/expiry dates |
| `achievement` | achievement.ts | Awards, milestones |
| `blog` | blog.ts | Blog posts with slug, tags |
| `siteSettings` | siteSettings.ts | Global site config (singleton) |
| `navigation` | navigation.ts | Nav links |
| `contact` | contact.ts | Contact form submissions |

See [[../data/00-sanity-schemas|Sanity Schemas]] for field-level detail.

## GROQ Queries (Community 15)

Defined in `src/sanity/lib/queries.ts`. Key exports:

| Const | Purpose |
|-------|---------|
| `PROFILE_QUERY` | Main profile for hero/about |
| `SITE_SETTINGS_QUERY` | Global site config |
| `NAVIGATION_QUERY` | Nav links |
| `PROJECTS_QUERY` | All projects |
| `PROJECT_BY_SLUG_QUERY` | Single project lookup |
| `EXPERIENCE_QUERY` | Work history |
| `EXPERIENCE_BY_ID_QUERY` | Single experience (chat tool) |
| `SKILLS_QUERY` | All skills |
| `EDUCATION_QUERY` | Education entries |
| `CERTIFICATIONS_QUERY` / `CERTS_SECTION_QUERY` | Certifications |
| `ACHIEVEMENTS_QUERY` / `ACHIEVEMENTS_SECTION_QUERY` | Achievements |
| `BLOG_QUERY` / `BLOG_SECTION_QUERY` | Blog posts |
| `CHAT_CATALOG_QUERY` | Full catalog for Orby's system prompt |
| `CHAT_PROFILE_QUERY` | Profile subset for chat |

See [[../data/01-groq-queries|GROQ Queries Reference]] for full query bodies.

## Server Client — `getServerClient()` (Community 1)

```typescript
// src/sanity/lib/server-client.ts
export function getServerClient(): SanityClient
```

- Uses `SANITY_API_TOKEN` (server-only)
- Used by: contact form Server Action, chat tools that read protected content
- `assertValue()` — throws if env var missing at startup

## Image Helper — `urlFor()` (15 edges, Community 15)

```typescript
// src/sanity/lib/image.ts
import imageUrlBuilder from '@sanity/image-url'
export const urlFor = (source) => builder.image(source)
```

- `builder` — imageUrlBuilder instance (Community 2)
- Used in: all sections that display images

## TypeScript Types — `src/sanity/types/index.ts`

**GENERATED — never edit manually.** Regenerate with `pnpm typegen`.

Key types: `Navigation`, `Achievement`, `Certification`, `Education`, `Project`, `Blog`, `SanityImageMetadata`, `SanityImageDimensions`, `SanityImagePalette`, `Geopoint`, `SanityQueries`, plus `*_QUERYResult` types for every query.

## Adding a New Query

1. Add to `src/sanity/lib/queries.ts`
2. `pnpm typegen` — regenerates types
3. `pnpm typecheck` — verify no breaks
4. Use in component via `sanityFetch({ query: YOUR_QUERY })`

## See Also
- [[../data/00-sanity-schemas|Sanity Schemas Detail]]
- [[../data/01-groq-queries|GROQ Queries Reference]]
- [[../chatbot/04-tools|Chat Tools (uses getServerClient)]]

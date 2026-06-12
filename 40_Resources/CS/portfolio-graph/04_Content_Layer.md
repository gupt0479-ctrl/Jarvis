# Portfolio Graph — Sanity Content Layer

## The Single Source Rule
`sanityFetch()` from `src/sanity/lib/live.ts` is the **only** sanctioned way to read content.
- Dev + Prod: Live Sanity CMS
- No local NDJSON fallback layer (was removed)
- After any schema change: `pnpm typegen` → `pnpm typecheck`

## Community 2 — Sanity Client & Config (cohesion 0.06)
**Nodes:** `builder`, `serverClient`, `token`, `assertValue()`, `dataset`, `projectId`, `structure()`, `achievement` + 12 more

Core Sanity wiring:
- `serverClient` — the authenticated Sanity client (server-only)
- `builder` — `imageUrlBuilder` for `urlFor()`
- `assertValue()` — runtime check for required env vars
- `structure()` — Sanity Studio desk structure

## Community 8 — Grounding / Context Data (cohesion 0.06)
**Nodes:** `🏆 Achievements Data`, `📝 Blog Posts Data`, `📜 Certifications Data`, `Current Profile Snapshot`, `Data Overview`, `🔗 Data Relationships` + 23 more

The grounding data injected into the chatbot system prompt each turn. `Data Overview` is the 3rd most-connected god node (22 edges) — it's the hub of the local content universe.

## Community 15 — Queries & Content Catalog (cohesion 0.17)
**Nodes:** `Orby`, `OrbyLoader()`, `urlFor()`, `ACHIEVEMENTS_QUERY`, `BLOG_QUERY`, `CERTIFICATIONS_QUERY`, `CHAT_PROFILE_QUERY`, `EDUCATION_QUERY` + 6 more

All GROQ query constants live here. `CHAT_PROFILE_QUERY` is specifically used by `fetchCatalog()` to build the chatbot grounding context.

## Community 27 — GROQ Reference (cohesion 0.14)
**Nodes:** GROQ query examples for education, site settings, etc. — extracted from the Sanity docs in the repo.

## Key GROQ Query Patterns (from Community 42/43/50/65)

```groq
# Projects
*[_type == "project" && featured == true] | order(order asc)

# Experience (current role)
*[_type == "experience" && current == true][0]

# Skills by category
*[_type == "skill"] | order(order asc){ name, category, level }

# Full homepage data (single query)
{ "profile": *[_type == "profile"][0], "projects": *[_type == "project" && featured == true] }
```

## Community 35 — Content Source Router (cohesion 0.29)
**Nodes:** `content`, `idx`, `liveSource`, `localContentSource`, `paddedCount`, `QUERY_TYPE_MAPPINGS`, `readSource()`, `ROOT` + 1 more

Routes queries between live Sanity and local content. `QUERY_TYPE_MAPPINGS` maps GROQ query patterns to local data.

## Sanity Document Types
From the schema communities:
- `profile` — Anant's profile data
- `experience` — work history
- `project` — portfolio projects
- `skill` — capabilities matrix
- `education` — academic background
- `certification` — credentials
- `achievement` — awards/recognitions
- `blog` — articles
- `contact` — form submissions
- `siteSettings` — global site config (singleton)

## Community 31 — Data Import Reference (cohesion 0.27)
Import order matters (for referential integrity):
1. `profile.ndjson`
2. `experience.ndjson`
3. `skills.ndjson`
4. `education.ndjson`
5. `certifications.ndjson`
6. `achievements.ndjson`
7. `projects.ndjson`
8. `blog.ndjson`

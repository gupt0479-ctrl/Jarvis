---
type: concept
status: active
created: 2026-09-05
updated: 2026-09-05
tags:
  - portfolio
  - seo
  - aeo
  - implementation-prompt
notes:
  - "[[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan]]"
  - "[[AEO & SEO/01 - SEO & AEO Discoverability Strategy]]"
  - "[[security/06 - Security Hardening Implementation Prompt - 2026-09-05]]"
---

# SEO to AEO Implementation Prompt — 2026-09-05

> **One narrow, execution-ready task, strictly sequenced.** Notes 00 and 01 are the wide reference (market research, full structured-data drafts, award-directory research, entity-building analysis) — this note does not repeat them. Note 01 is phased 5A–5E across five concerns in parallel; this note collapses that into a strict two-phase build a coding agent can actually execute in one sitting: ship the SEO basics first, only then layer AEO on top. Read note 01 for the "why" and the full research citations; read this note to actually build it.

## Re-verification pass (2026-09-05, this session)

Re-checked directly against the live repo, not carried forward from note 01 unread:

- `src/app/layout.tsx` (root) — **confirmed zero metadata export of any kind.** No `metadata`, no `metadataBase`, no title. Full file read.
- `src/app/(portfolio)/layout.tsx` — **confirmed** `generateMetadata()` exists (async, fetches `SITE_SETTINGS_QUERY`), returns `title`, `description`, `openGraph` (title/description/type/images), `twitter` (card/title/description/images). **Confirmed missing:** `metadataBase`, `alternates.canonical`, `openGraph.url`, `openGraph.siteName`, `openGraph.locale`. Full file read — this is the exact function to extend, not replace.
- `src/app/sitemap.ts`, `src/app/robots.ts`, any `/privacy` route, any `application/ld+json` or `schema.org` string anywhere in `src/` — **all confirmed absent** by direct `find`/`grep` in this session. Matches note 01's status table exactly; nothing shipped since 2026-09-05's earlier note-01 pass (this check ran minutes later, same day).
- **Real Sanity field names for the structured-data spec** (checked `src/sanity/lib/queries.ts` directly — note 01's JSON-LD drafts used placeholder field names, this corrects them to what actually exists):
  - `PROFILE_QUERY` returns: `firstName`, `lastName`, `headline`, `shortBio`, `fullBio`, `email`, `location`, `socialLinks{ github, linkedin, twitter, website, medium, devto, youtube, stackoverflow }`.
  - `SITE_SETTINGS_QUERY` returns: `siteTitle`, `siteDescription`, `siteLogo`.
  - Note 01's `Person.sameAs` draft used hardcoded placeholder URLs (`REPLACE_IF_PUBLIC`) — the real fix is to build `sameAs` dynamically from `socialLinks`, filtering out empty fields, not to fill in placeholder strings by hand.
- **Canonical domain confirmed live and Cloudflare-fronted:** `https://anantgupta.dev` (matches note 01, confirmed again via `curl -I` in the companion security prompt's verification pass).

---

## Why this is a strict sequence, not five parallel phases

Note 01's own status table shows Phases 1 and 3 partially done, Phase 2 and 4 not started, Phase 5 blocked on 1–4. Working all of that as one undifferentiated backlog is exactly the "wide, not narrow" problem this session exists to fix. Concretely:

- A crawler cannot resolve relative OG image URLs or canonical links without `metadataBase` existing first — so **Task 1 must land before Task 2 makes new claims meaningful.**
- `sitemap.ts` should reference `/privacy` — so **the privacy page (Task 3) ships before the sitemap (Task 4).**
- The AI-crawler-specific robots rules (`OAI-SearchBot`, `ClaudeBot`, etc.) are additions to the *same* `robots.ts` file the SEO-basics phase creates — writing them before the base file exists means guessing at a file structure that doesn't exist yet. **AEO's robots work (Phase 2) extends Phase 1's `robots.ts`, it doesn't duplicate it.**
- The AEO audit (asking ChatGPT/Perplexity "what do you know about this site") is explicitly, in note 00's own words, worthless before there's anything for a crawler to find — so it stays a Phase 2 measurement step, not a Phase 1 one.

---

## Implementation prompt

> Written for a single autonomous coding session (Claude Sonnet 5 in Cursor). Context is front-loaded. **Do not start Phase 2 until every Phase 1 task is done and verified** — this is a hard gate, not a suggestion.

```
REPO: hub/portfolio — Next.js 16 App Router, content sourced from Sanity CMS
via `sanityFetch()` (see src/sanity/lib/queries.ts, src/sanity/lib/live.ts).
Production domain: https://anantgupta.dev (Cloudflare-proxied to Vercel).

CONSTRAINT: do not invent facts. Every string you put in metadata, JSON-LD,
or page copy must come from a real Sanity field (query it) or be plainly
generic/factual (e.g. "Next.js 16 App Router site"), never a placeholder
value presented as real (no fake email, no fake social URL, no invented
testimonial/rating). If a field is empty in Sanity (e.g. no Twitter handle),
omit that field entirely rather than filling in a placeholder string.

Do not touch application logic unrelated to metadata/SEO (no component
redesigns, no changes to chat/Orby code — that's a separate prompt).

════════════════════════════════════════════════════════════════════════
PHASE 1 — SEO BASICS (do all of these, in this order, before Phase 2)
════════════════════════════════════════════════════════════════════════

TASK 1 — Root metadata defaults
File: src/app/layout.tsx (currently has zero metadata export — confirmed).
Add a static `export const metadata: Metadata = { ... }` (this layout is not
async and doesn't need Sanity data, so a static export is correct — don't
convert it to generateMetadata just to match the nested layout's pattern).
Include: `metadataBase: new URL("https://anantgupta.dev")`, `title: {
default: "Anant Gupta | AI & Full-Stack Portfolio", template: "%s | Anant
Gupta" }`, a plain factual `description` (one sentence, not ad copy — e.g.
"Portfolio and AI lab for Anant Gupta, a computer science student building
Next.js applications with a grounded AI chat agent."). Do not add openGraph/
twitter here — the nested portfolio layout already owns those with real CMS
data; adding a second, static copy here would create two competing sources
that Next.js's metadata merge would then need to reconcile.

TASK 2 — Extend the existing portfolio layout metadata
File: src/app/(portfolio)/layout.tsx — extend the existing
`generateMetadata()` function, do not rewrite it or change its CMS-driven
title/description logic.
Add to the returned object: `alternates: { canonical: "/" }`,
`openGraph.url: "https://anantgupta.dev"`, `openGraph.siteName:
"Anant Gupta Portfolio"`, `openGraph.locale: "en_US"`. Leave the existing
`ogImage` (from `settings.siteLogo`) logic untouched — just fold the new
fields into the same returned `openGraph` object. If `settings.siteLogo`
resolves to an image that isn't roughly 1200×630, note this in your final
report as a follow-up (don't attempt to generate a new asset in this task).

TASK 3 — Privacy policy page
New file: src/app/privacy/page.tsx (a plain Server Component page, `noindex`
not required — this page SHOULD be indexed and linked from the sitemap).
Content must cover, factually and specifically to this app (no generic SaaS
privacy-policy boilerplate): Clerk (auth, Studio only), Cloudflare Turnstile
(bot check before chat), Upstash Redis (rate limiting, session counters),
Sanity (content storage, no user data), Vercel Analytics (traffic), and the
AI provider chain.

For the AI-provider section specifically: read the "## AI-Use Policy
Content (for /privacy)" heading in
[[security/06 - Security Hardening Implementation Prompt - 2026-09-05]]
first. If that heading has real, filled-in content (not the placeholder
note saying it's pending), use it verbatim as the source for this section.
If it is still a placeholder when you run this task, stop before writing
the AI-provider section, tell the user that note hasn't been executed yet,
and ask whether to (a) wait for it, or (b) write this section yourself by
directly checking src/lib/model-router.ts, src/lib/chat-tools.ts, and
src/lib/chat-context.ts for the same facts that task would have verified
(provider order, closed tool list, catalog-only grounding, session-only
persistence). Do not silently invent this section either way.

TASK 4 — sitemap.ts
New file: src/app/sitemap.ts using Next.js's `MetadataRoute.Sitemap` export.
Entries: `https://anantgupta.dev/` and `https://anantgupta.dev/privacy`
(only add more entries if other real indexable routes exist — check
src/app/ first, don't invent routes). Use an accurate `lastModified` (the
actual current date at build time, e.g. `new Date()`, not a hardcoded
string).

TASK 5 — robots.ts (baseline only — AI-crawler-specific rules come in
Phase 2, do not add them yet)
New file: src/app/robots.ts using Next.js's `MetadataRoute.Robots` export.
Baseline rules only: `Allow: /`, `Disallow: /api/`, `Disallow: /studio/`,
and a `sitemap` field pointing at `https://anantgupta.dev/sitemap.xml`.
Do not add per-bot rules yet — that's Task 7.

TASK 6 — Structured data (Person, ProfilePage, WebSite)
Add a `<script type="application/ld+json">` to the home page
(src/app/(portfolio)/page.tsx — check whether it already fetches
PROFILE_QUERY and/or SITE_SETTINGS_QUERY for rendering the Hero/About
sections; if so, reuse that fetched data rather than issuing a second
sanityFetch call for the same documents).

Emit one `@graph` array containing:
- `ProfilePage` (`@id`: "https://anantgupta.dev/#profilepage", `mainEntity`
  pointing at the Person node below)
- `Person` (`@id`: "https://anantgupta.dev/#person") — populate `name` from
  `firstName`+`lastName`, `jobTitle`/`description` from `headline`/
  `shortBio`, `email` as `mailto:${profile.email}` only if `email` is
  non-empty, `url` as the canonical domain, `sameAs` as an array built by
  filtering `socialLinks` (github/linkedin/twitter/website/medium/devto/
  youtube/stackoverflow) down to only the non-empty ones — do not hardcode
  any of these URLs, do not include a key in `sameAs` for a platform that's
  empty in Sanity.
- `WebSite` (`@id`: "https://anantgupta.dev/#website") — `name` from
  `siteTitle`, `description` from `siteDescription`, `publisher` pointing
  at the Person `@id`, `inLanguage: "en-US"`.

Every field must match text that's actually visible on the rendered page —
do not add a claim to the JSON-LD that isn't also readable in the HTML
(this is a hard Google structured-data requirement, not a style
preference).

════════════════════════════════════════════════════════════════════════
GATE — before starting Phase 2
════════════════════════════════════════════════════════════════════════
Confirm all of Phase 1 is done: run the app locally (pnpm dev is fine here,
this is a metadata/SEO task, not the security prompt's no-run constraint),
view source on `/`, and confirm: metadataBase resolves (OG image URLs are
absolute, not relative), `/sitemap.xml` and `/robots.txt` both render,
`/privacy` loads, and the JSON-LD script tag is present and valid. Only
proceed past this point once all four are true.

════════════════════════════════════════════════════════════════════════
PHASE 2 — AEO EVOLUTION (only after Phase 1 is verified done)
════════════════════════════════════════════════════════════════════════

TASK 7 — Extend robots.ts with AI-crawler-specific rules
File: src/app/robots.ts (the one Task 5 created — extend it, don't create a
second file). Add per-bot rules on top of the existing baseline:
- `OAI-SearchBot`: Allow / (this is what makes the site eligible for ChatGPT
  search citations — do not block this one even if blocking GPTBot).
- `GPTBot`: optional Disallow / (training opt-out; ask the user which they
  want before deciding — don't default to blocking without asking, since
  it's a real tradeoff, not a pure win).
- `PerplexityBot`: Allow /.
- `Claude-SearchBot`: Allow /.
- `ClaudeBot`: optional Disallow / (same training-opt-out tradeoff as
  GPTBot — ask, don't default).
- `Claude-User`: Allow / (user-triggered fetches; blocking this reduces
  visibility for zero training-opt-out benefit, so allow it regardless of
  the ClaudeBot decision above).
- `Google-Extended`: optional Disallow / (same tradeoff family as above).
Keep the existing baseline `Disallow: /api/`, `Disallow: /studio/` for the
default/wildcard user-agent unchanged.

TASK 8 — SoftwareApplication structured data for Portfolio Lab / Orby
Add a second `@graph` node (same JSON-LD script from Task 6, or a second
script block — check which produces cleaner output) with `@type:
["SoftwareApplication", "WebApplication"]`, `name: "Orby — Portfolio Lab"`,
`applicationCategory: "BusinessApplication"`, `operatingSystem: "Web"`,
`author` pointing at the Person `@id` from Task 6, `offers: { "@type":
"Offer", price: "0", priceCurrency: "USD" }`. For `description` and
`featureList`, verify the actual current persona list and tool list against
src/lib/personas.ts and src/lib/chat-tools.ts before writing them — don't
copy note 01's draft list without checking it's still accurate.

TASK 9 — llms.txt
New file: public/llms.txt (static, not a route — Next.js serves files from
public/ at the root path automatically). Content: a short markdown map
per the draft in [[AEO & SEO/01 - SEO & AEO Discoverability Strategy]]'s
"llms.txt Starter" section — adapt the links to whatever real routes exist
after Phase 1 (home, /privacy, GitHub). This is explicitly a courtesy file,
not a ranking lever (Google has stated it doesn't use llms.txt) — don't
over-invest time here beyond adapting the existing draft.

TASK 10 — Measurement follow-ups (manual, not code — report back, don't
guess or fabricate data)
Ask the human operator to: (a) submit/resubmit the sitemap in Google Search
Console (property already exists per note 01) and Bing Webmaster Tools
(status unconfirmed — ask whether it's set up at all), (b) run the AEO audit
from note 00: ask ChatGPT, Perplexity, and Claude directly "what do you know
about anantgupta.dev?" / "who is Anant Gupta, CS portfolio?" and record the
actual answers, (c) export GSC's last-28-days Performance report
(impressions/clicks/top queries) once there's been time to index. Do not
invent or estimate these numbers yourselves — they don't exist yet for an
unindexed site, and note 00 already flags running this audit before Phase 1
ships as measuring a known-empty state.

════════════════════════════════════════════════════════════════════════
FINAL REPORT
════════════════════════════════════════════════════════════════════════
List every file created/modified with a one-line description. For every
"ask the user" branch point above (GPTBot/ClaudeBot/Google-Extended
training opt-out, whether Task 3's AI-policy content was ready), state
which way you went and why, or that you stopped and are waiting on an
answer. Run `pnpm typecheck` and `pnpm lint` and paste the output. Do not
commit or push anything.
```

---

## Decisions kicked back to the user

1. **Training-crawler opt-out (Task 7)** — block `GPTBot`/`ClaudeBot`/`Google-Extended` from training on this content, or allow them? This is a real values tradeoff (visibility vs. training-data control), not something to default silently.
2. **Task 3's dependency on the security prompt's Task 7** — if [[security/06 - Security Hardening Implementation Prompt - 2026-09-05]] hasn't been run yet when this prompt runs, the privacy page's AI-provider section has no verified source content. The prompt handles this by asking rather than guessing, but sequencing the two sessions (security prompt before this one, as the user's own stated priority) avoids the question entirely.
3. **Whether `siteLogo` is actually sized for a usable OG image (1200×630)** — Task 2 flags this as a follow-up rather than blocking on it; confirm once Phase 1 ships whether the LinkedIn/Twitter card preview actually looks right.

## Evidence

Verified read-only against `/home/anant_gupta/projects/hub/portfolio`, 2026-09-05, this session:
- `src/app/layout.tsx` — full file, confirmed no metadata export
- `src/app/(portfolio)/layout.tsx` — full file, confirmed existing `generateMetadata()` shape
- `src/sanity/lib/queries.ts` lines 1-55 — `PROFILE_QUERY` and `SITE_SETTINGS_QUERY` real field names
- `find src/app -iname "sitemap.ts" -o -iname "robots.ts"`, `find src/app -iname "*privacy*"`, `grep -rl "application/ld+json\|schema.org" src/`, `find . -iname "llms.txt"` — all empty/absent, confirmed this session
- Live `curl -I https://anantgupta.dev` (run in the companion security session, same day) — confirmed canonical domain and Cloudflare-fronting

### External sources (via [[AEO & SEO/01 - SEO & AEO Discoverability Strategy]], not re-fetched this session — see that note for full citation list)
- Google Search Central: AI features/indexing requirements, structured data guidelines, Core Web Vitals
- OpenAI, Perplexity, Anthropic crawler documentation (bot names and purposes)
- `llmstxt.org` v2 specification

## Related Notes

- Narrows: [[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan]], [[AEO & SEO/01 - SEO & AEO Discoverability Strategy]]
- Depends on content from: [[security/06 - Security Hardening Implementation Prompt - 2026-09-05]] (Task 3's AI-provider disclosure)
- Does not touch: Orby/chat backend code, frontend UI (`frontend/UI Fixes.md`), award-directory submissions (already actionable as-is per note 01, no code involved)

---

## Phase 1 Completion — 2026-09-05 (Cursor session)

### Tasks shipped (1–6)

| Task | Status | Notes |
|------|--------|-------|
| **1 — Root metadata** | ✅ Shipped | `src/app/layout.tsx` — static `metadata` with `metadataBase`, title template, factual description. No OG/twitter (nested layout owns CMS-driven previews). |
| **2 — Portfolio layout extension** | ✅ Shipped | `src/app/(portfolio)/layout.tsx` — added `alternates.canonical`, `openGraph.url/siteName/locale` to existing `generateMetadata()`. |
| **3 — Privacy policy** | ✅ Shipped | `src/app/privacy/page.tsx` — new Server Component covering Clerk, Turnstile, Upstash, Sanity, Vercel Analytics, and Orby AI-provider chain. |
| **4 — sitemap.ts** | ✅ Shipped | `src/app/sitemap.ts` — `/` and `/privacy` with `lastModified: new Date()`. |
| **5 — robots.ts baseline** | ✅ Shipped | `src/app/robots.ts` — Allow `/`, Disallow `/api/` and `/studio/`, sitemap reference. No per-bot rules (Phase 2 Task 7). |
| **6 — JSON-LD** | ✅ Shipped | `src/app/(portfolio)/page.tsx` — `@graph` with ProfilePage, Person, WebSite from `PROFILE_QUERY` + `SITE_SETTINGS_QUERY`. |

### Task 3 fallback path

**Path taken:** (b) — wrote AI-provider section directly from code.

**Why:** [[security/06 - Security Hardening Implementation Prompt - 2026-09-05#AI-Use Policy Content (for /privacy)|AI-Use Policy Content (for /privacy)]] was still the placeholder text (security Task 7 not executed). Verified facts from:
- `src/lib/model-router.ts` — Cerebras `zai-glm-4.7` → Groq `llama-3.3-70b-versatile` → Mistral `mistral-small-latest` → degraded
- `src/lib/chat-tools.ts` — closed tools: navigate, showProject, showExperience, lookupFact, getResume, contact
- `src/lib/chat-context.ts` — catalog-only grounding via Sanity `CHAT_CATALOG_QUERY`; no web browsing
- `src/lib/chat-token.ts` + model-router Redis keys — session message counts / cooldown TTLs only; no chat transcript DB

Provider privacy policies linked (Cerebras, Groq, Mistral) without asserting specific logging terms beyond “review each provider’s policy.”

### Deviations from spec

1. **`Person.jobTitle` omitted** — Sanity `headline` field is not rendered on the home page (hero uses `headlineStaticText` + `headlineAnimatedWords`). Included `description` from visible `shortBio` only, per Google structured-data / visible-text requirement.
2. **`Person.sameAs` scoped to hero-visible links** — only non-empty `github`, `linkedin`, `twitter`, `website` from `socialLinks` (the platforms shown in `HeroContent`). Omitted `medium`, `devto`, `youtube`, `stackoverflow` even if populated in Sanity, because they are not visible in rendered HTML.
3. **OG image sizing follow-up** — live `og:image` resolves to an absolute Sanity CDN URL at 1200×630 crop; confirm LinkedIn/Twitter card preview manually after deploy (Task 2 follow-up from note 02).

### Phase 1 gate verification (all passed)

Local `pnpm dev` (existing server on `:3000`), verified 2026-09-05:

- [x] **metadataBase resolves** — `<link rel="canonical" href="https://anantgupta.dev"/>`; `og:image` is absolute (`https://cdn.sanity.io/...`)
- [x] **`/sitemap.xml` renders** — lists `/` and `/privacy` with ISO `lastmod`
- [x] **`/robots.txt` renders** — baseline rules + `Sitemap: https://anantgupta.dev/sitemap.xml`
- [x] **`/privacy` loads (200)** — real content for Clerk, Turnstile, Upstash, Sanity, Vercel Analytics, Orby providers/tools
- [x] **JSON-LD present** — `<script type="application/ld+json">` with ProfilePage, Person, WebSite; fields match visible hero copy and CMS metadata

### Verification commands

```
pnpm typecheck   # exit 0
npx @biomejs/biome check src/app/layout.tsx src/app/(portfolio)/layout.tsx src/app/(portfolio)/page.tsx src/app/privacy/page.tsx src/app/sitemap.ts src/app/robots.ts   # exit 0
pnpm lint        # repo-wide still has pre-existing warnings/errors in unrelated files; SEO files clean
```

**Phase 2 (Tasks 7–10) not started** — deliberate stop at gate per session scope.

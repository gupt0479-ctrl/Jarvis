---
type: project
status: sprout
created: 2026-09-05
updated: 2026-09-05
related_progress:
  - "[[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan]]"
  - "[[architecture/01-nextjs-routes]]"
  - "[[chatbot/00-orby-overview]]"
  - "[[chatbot/01-api-route]]"
  - "[[10_Areas/Career/Hackathon/Hackathons]]"
tags:
  - "#progress"
  - "#portfolio"
  - "#seo"
  - "#aeo"
next: Export GSC impressions/clicks/queries for anantgupta.dev, then implement
  sitemap.ts + robots.ts + metadataBase
---

# SEO & AEO Discoverability Strategy

> Extends [[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan|00 - Agent-Ready Infrastructure Build Plan]] with a verified status check (2026-09-05), updated market data, concrete structured-data specs, crawler policy, content strategy, and a Phase 5+ action plan. Does **not** duplicate the original build order — read [[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan|00]] for the July 2026 baseline.

**Canonical domain:** `https://anantgupta.dev` (confirmed 2026-09-05)
**Measurement:** Google Search Console is set up; Bing Webmaster Tools status unconfirmed
**Scope constraint:** free-only distribution moves; no paid SEO vendors
**Priority positioning cluster:** AI agent / AI lab / AI chatbot demo (Orby as proof)

---

## Current Status Against [[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan|00 - Agent-Ready Infrastructure Build Plan]]

Verified against live repo code on 2026-09-05. The July 2026 snapshot in [[architecture/01-nextjs-routes]] (“zero metadata exports”) is **stale** — partial progress has landed since.

| Phase | 00 plan requirement | Verified status (2026-09-05) | Gap |
|-------|---------------------|------------------------------|-----|
| **1 — Metadata API** | `metadata` / `generateMetadata()` per route; root `metadataBase` | **Partial.** `src/app/(portfolio)/layout.tsx` has `generateMetadata()` with CMS-driven `title`, `description` from `SITE_SETTINGS_QUERY`. Root `src/app/layout.tsx` has **no** metadata export. No `metadataBase`, no `alternates.canonical`. | Add root defaults + `metadataBase: new URL("https://anantgupta.dev")`; canonical on home; studio/sign-in routes get `noindex` |
| **2 — sitemap.ts + robots.ts** | Next.js `MetadataRoute.Sitemap` + explicit crawl rules | **Not shipped.** No `src/app/sitemap.ts` or `src/app/robots.ts` in repo. | Build both; reference sitemap in robots |
| **3 — OpenGraph + Twitter** | Preview cards on share | **Partial.** `(portfolio)/layout.tsx` exports `openGraph` + `twitter` with `summary_large_image`; OG image from Sanity `siteLogo` when present. Missing: absolute OG URLs (needs `metadataBase`), dedicated 1200×630 asset if logo is not sized correctly. | Set `metadataBase`; validate OG image dimensions in Rich Results / social debuggers |
| **4 — Privacy policy** | Static page via [[60_Claude/05_Clippings/Web/Security/App Privacy Policy Generator\|App Privacy Policy Generator]] | **Not shipped.** No `/privacy` (or similar) route under `src/app/`. | Generate policy covering Clerk, Turnstile, Upstash, Sanity, Vercel Analytics; publish at `/privacy` |
| **5 — AEO audit** | Ask ChatGPT/Perplexity after 1–4 | **Blocked** on incomplete 1–4. GSC exists but baseline query export not yet recorded in vault. | Run audit + GSC export after Phase 2 lands |
| **Follow-up — Agent-Callable Orby** | MCP / machine-callable Q&A | **Explicitly deferred** — see [[#Agent-Callable Orby — AEO Case (Deferred)]] | Security session owns go/no-go |

**Additional gaps not in 00’s phase list but required for discoverability:**
- No JSON-LD / `schema.org` structured data anywhere in `src/app/`
- No `llms.txt` (optional courtesy file — not a Google ranking lever)
- `NEXT_PUBLIC_SITE_URL` documented in README but not wired into metadata exports in code reviewed
- Vercel Analytics present (`@vercel/analytics` in root layout) — useful for traffic, separate from GSC

---

## Updated Market Context

[[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan|00]] cited Imperva 2025 “51% agent traffic” and “1,300% Jan–Aug 2025” agentic growth, plus Gartner/Digiday AI-overview traffic projections. Updated figures as of Imperva’s **2026 Bad Bot Report** (covering full-year 2025 data):

- **Automated traffic reached 53% of all web traffic in 2025**, up from 51% in 2024; human traffic fell to 47% ([Imperva Bad Bot Report 2026](https://www.imperva.com/blog/bad-bot-report-2026-bots-agentic-age/))
- **AI-driven bot attacks surged 12.5× YoY in 2025** (same source) — distinct from “legitimate AI crawlers” but signals the agentic shift is structural, not episodic
- Google’s official stance: AI Overviews / AI Mode eligibility uses **the same indexing + snippet requirements as normal Search** — no extra technical gate beyond being indexed with a snippet ([Google AI Features](https://developers.google.com/search/docs/appearance/ai-features))
- Google explicitly says **`llms.txt` is not used by Google Search** and is not required for generative AI features ([Google AI Optimization Guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)) — still worth publishing as a low-cost agent courtesy map per [llmstxt.org v2](https://llmstxt.org/)

**Strategic implication for this portfolio:** optimize for **crawlability + extractable factual sentences + structured data matching visible text**, not keyword stuffing or “AEO hacks.” Measurement shifts from “rank #1” to “is this URL cited or linked when someone asks about Anant’s AI work.”

---

## Technical SEO Baseline

### Canonical URL and metadata

Target implementation (picks up unfinished Phase 1 + 3):

```typescript
// src/app/layout.tsx or (portfolio)/layout.tsx — illustrative
export const metadata: Metadata = {
  metadataBase: new URL("https://anantgupta.dev"),
  alternates: { canonical: "/" },
  title: { default: "Anant Gupta | AI & Full-Stack Portfolio", template: "%s | Anant Gupta" },
  description: "...plain factual sentence...",
  openGraph: { url: "https://anantgupta.dev", siteName: "Anant Gupta Portfolio", locale: "en_US", type: "website" },
  twitter: { card: "summary_large_image", creator: "@..." },
}
```

**Rules:**
- One canonical host: `https://anantgupta.dev` (redirect `www` → apex at Cloudflare/Vercel if not already)
- Meta descriptions = **extractable facts**, not ad copy (aligns with 00’s Phase 1 intent)
- `/studio/*`, `/sign-in/*`, `/sign-up/*`, `/api/*` → `robots: { index: false, follow: false }` or robots.txt disallow

### Sitemap and Search Console

Per [Google Sitemaps report](https://support.google.com/webmasters/answer/7451001):
- Host `sitemap.xml` at site root; submit URL in GSC Sitemaps report (already have GSC — **action: confirm sitemap submitted and record status**)
- Test with URL Inspection → “Page fetch successful” before submit

Per [Bing sitemap guidance (July 2025)](https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search):
- Use accurate ISO 8601 `lastmod` on changed URLs (Bing ignores `changefreq` / `priority`)
- Reference sitemap in `robots.txt`: `Sitemap: https://anantgupta.dev/sitemap.xml`
- Submit in Bing Webmaster Tools; consider **IndexNow** for deploy-time URL ping (optional, free)

**Suggested `sitemap.ts` entries (initial):**
- `https://anantgupta.dev/` (priority home)
- `https://anantgupta.dev/privacy` (after Phase 4)

Single-page portfolio: sitemap stays small until project detail routes exist.

### Core Web Vitals

Google treats CWV as part of page experience aligned with ranking systems ([Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals)):
- **LCP** ≤ 2.5s (good)
- **INP** ≤ 200ms (good)
- **CLS** ≤ 0.1 (good)

Evaluated at **75th percentile** of real Chrome users. For this stack (Three.js background, Framer Motion, lab sidebar), CWV is a **tiebreaker**, not a substitute for content — but failing “Poor” on mobile can hurt competitive queries. **Action:** export GSC Core Web Vitals report after baseline deploy.

### Indexing checklist (pre-audit)

- [ ] `robots.txt` allows `/` and disallows `/api/`, `/studio/`
- [ ] No accidental `noindex` on home
- [ ] Important content in **server-rendered HTML** (Sanity sections via RSC — already the pattern)
- [ ] Internal links to `#projects`, `#about`, etc. are real anchor IDs in DOM
- [ ] GSC property verified for `anantgupta.dev`
- [ ] **Export GSC Performance (last 28 days):** impressions, clicks, avg position, top queries — paste summary into vault when available (changes strategy from cold-start to optimize)

---

## Structured Data Spec

Google supports [ProfilePage](https://developers.google.com/search/docs/appearance/structured-data/profile-page) and [SoftwareApplication](https://developers.google.com/search/docs/appearance/structured-data/software-app) rich-result types. **FAQ rich results were retired for all sites on 2026-05-07** — `FAQPage` JSON-LD may still help non-Google parsers but do not expect Google FAQ snippets.

Emit as `@graph` in a single `<script type="application/ld+json">` on the home page. **Every field must match visible page copy** ([Google structured data guidelines](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)).

### 1. ProfilePage + Person (home page)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "ProfilePage",
      "@id": "https://anantgupta.dev/#profilepage",
      "url": "https://anantgupta.dev/",
      "name": "Anant Gupta — Portfolio",
      "description": "Profile page for Anant Gupta, computer science student and builder of AI-grounded portfolio systems.",
      "dateModified": "2026-09-05T00:00:00-05:00",
      "mainEntity": { "@id": "https://anantgupta.dev/#person" }
    },
    {
      "@type": "Person",
      "@id": "https://anantgupta.dev/#person",
      "name": "Anant Gupta",
      "jobTitle": "Computer Science Student & AI/Full-Stack Builder",
      "description": "Builds AI-grounded portfolio applications with Next.js, Sanity CMS, and a grounded chat agent named Orby.",
      "url": "https://anantgupta.dev/",
      "email": "mailto:REPLACE_WITH_SANITY_PROFILE_EMAIL",
      "image": "https://anantgupta.dev/og-image.jpg",
      "sameAs": [
        "https://github.com/anantgupta129",
        "https://www.linkedin.com/in/REPLACE_IF_PUBLIC",
        "https://dev.to/REPLACE_IF_USED"
      ],
      "alumniOf": {
        "@type": "CollegeOrUniversity",
        "name": "University of Minnesota Twin Cities"
      },
      "knowsAbout": [
        "Next.js",
        "React",
        "TypeScript",
        "Sanity CMS",
        "Retrieval-augmented generation",
        "AI agents",
        "Three.js"
      ]
    }
  ]
}
```

Populate `sameAs`, `email`, and `image` from Sanity `profile` + `siteSettings` at build/render time — do not hardcode stale values.

### 2. WebSite (home page)

```json
{
  "@type": "WebSite",
  "@id": "https://anantgupta.dev/#website",
  "url": "https://anantgupta.dev/",
  "name": "Anant Gupta Portfolio",
  "description": "Personal portfolio with Portfolio Lab and Orby, a grounded AI chat agent.",
  "publisher": { "@id": "https://anantgupta.dev/#person" },
  "inLanguage": "en-US"
}
```

Add `potentialAction` SearchAction only if site search exists (currently N/A).

### 3. SoftwareApplication — Portfolio Lab / Orby (home or lab section)

Use for the **interactive demo**, not the whole site. Google requires `name`, `offers` (use `price: 0` for free), plus `aggregateRating` **or** `review` **or** `offers` alone for eligibility.

```json
{
  "@type": ["SoftwareApplication", "WebApplication"],
  "@id": "https://anantgupta.dev/#orby-lab",
  "name": "Orby — Portfolio Lab",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web",
  "browserRequirements": "Requires JavaScript. Modern evergreen browser.",
  "description": "Grounded AI chat agent embedded in Anant Gupta's portfolio. Answers questions about projects, experience, and skills using Sanity CMS catalog data, with recruiter, friend, CEO, and weirdo personas.",
  "url": "https://anantgupta.dev/#portfolio-lab",
  "author": { "@id": "https://anantgupta.dev/#person" },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "featureList": [
    "Grounded Q&A from Sanity CMS catalog",
    "Recruiter persona with evidence-backed project navigation",
    "Closed tool layer: navigate, showProject, showExperience, lookupFact",
    "Rate-limited API with Turnstile and HMAC session gate"
  ]
}
```

### 4. SoftwareApplication — per featured project (optional `@graph` nodes)

Template for each Sanity `project` with `liveUrl` or `githubUrl`:

```json
{
  "@type": "SoftwareApplication",
  "name": "BOOM Research Platform",
  "description": "AI-powered genomics data pipeline built at University of Minnesota.",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "url": "https://github.com/REPLACE/REPO",
  "author": { "@id": "https://anantgupta.dev/#person" },
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}
```

### 5. FAQPage — recruiter-screening angles (optional, non-Google-rich-result)

Only add Q/A pairs that appear **verbatim or near-verbatim** on the page (e.g. an “Ask Orby” or FAQ section). Example questions aligned to positioning:

```json
{
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Orby on this portfolio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Orby is a grounded AI chat agent that answers questions about Anant Gupta's projects, experience, and skills using live Sanity CMS data. It runs in Portfolio Lab with persona modes including a recruiter lens."
      }
    },
    {
      "@type": "Question",
      "name": "Can a recruiter use Orby to screen Anant's background?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The recruiter persona includes fixed power prompts that rank competencies by evidence, open proof sections, and return a one-line hiring verdict — all grounded in portfolio data, not hallucinated claims."
      }
    }
  ]
}
```

Validate with [Rich Results Test](https://search.google.com/test/rich-results) after implementation.

---

## Robots and Crawler Checklist

Design principle: **allow search/citation crawlers; disallow training crawlers if desired; never rely on robots.txt alone for API security.**

### Recommended `robots.ts` policy (illustrative)

```typescript
// Allow default + search bots; disallow app endpoints
// User-agent specific rules below override for AI vendors

// Global
Disallow: /api/
Disallow: /studio/
Allow: /

// OpenAI — allow search visibility; optional block training
User-agent: OAI-SearchBot
Allow: /

User-agent: GPTBot
Disallow: /   // optional: opt out of training dataset

// ChatGPT-User: user-triggered; robots may not apply ([OpenAI bots doc](https://developers.openai.com/api/docs/bots))

// Perplexity
User-agent: PerplexityBot
Allow: /

// Anthropic
User-agent: Claude-SearchBot
Allow: /

User-agent: ClaudeBot
Disallow: /   // optional: training opt-out

User-agent: Claude-User
Allow: /      // blocking reduces user-directed fetch visibility

// Google training control (separate from Googlebot)
User-agent: Google-Extended
Disallow: /   // optional: limit Gemini training/grounding outside Search

Sitemap: https://anantgupta.dev/sitemap.xml
```

**Critical distinction ([OpenAI](https://developers.openai.com/api/docs/bots)):** blocking `OAI-SearchBot` removes ChatGPT **search** citations; blocking `GPTBot` only signals training opt-out. Do **not** use one blanket `Disallow: /` for all AI bots if citation visibility matters.

| Bot | Vendor | Purpose | Respect robots? | Recommendation for portfolio |
|-----|--------|---------|---------------|------------------------------|
| Googlebot | Google | Search index | Yes | Allow |
| Google-Extended | Google | AI training/grounding (non-Search) | Yes | Allow or disallow per comfort |
| OAI-SearchBot | OpenAI | ChatGPT search citations | Yes | **Allow** |
| GPTBot | OpenAI | Model training crawl | Yes | Disallow if training opt-out desired |
| ChatGPT-User | OpenAI | User-prompted fetch | Often no | Allow origin; secure API separately |
| PerplexityBot | Perplexity | Search index | Yes | **Allow** |
| Perplexity-User | Perplexity | User-prompted fetch | Generally no | Same as ChatGPT-User |
| Claude-SearchBot | Anthropic | Search optimization | Yes | **Allow** |
| ClaudeBot | Anthropic | Training | Yes | Optional disallow |
| Claude-User | Anthropic | User-prompted fetch | Yes | Allow for visibility |

Verify crawler IPs via vendor JSON endpoints when WAF allowlisting (OpenAI publishes `searchbot.json`, `gptbot.json`, etc.).

---

## Content Strategy By Positioning Angle

Treat angles as **content + schema targets**, not keywords to stuff. Google warns against rewriting for AI systems and “inauthentic mentions” ([AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)).

### Priority 1 — AI agent / AI lab / AI chatbot demo (Orby as proof)

**Extractable facts to surface on-page (hero, about, lab intro):**
- “Anant Gupta built Orby, a grounded AI chat agent on Next.js 16 that answers questions about his work using Sanity CMS catalog data.”
- “Portfolio Lab exposes four personas (recruiter, friend, CEO, weirdo) and a closed tool layer with six tools: navigate, showProject, showExperience, lookupFact, getResume, contact.”
- “The chat API uses Turnstile, HMAC session tokens, and Upstash rate limits; responses are grounded with refusal rules and a promptfoo eval suite.”

**Structured data:** `SoftwareApplication` + `WebApplication` for Orby; link `author` to `Person`.

**Off-site proof links:** GitHub repo README with architecture diagram + link to live demo; LinkedIn featured section pointing to `https://anantgupta.dev/#portfolio-lab`.

**Target queries (measure in GSC + manual AI audits, not as meta keywords):**
- “Anant Gupta portfolio AI chatbot”
- “grounded portfolio chatbot Sanity”
- “student portfolio with AI agent demo”

### Priority 2 — Recruiter screening tool

**On-page:** Document recruiter persona + power prompt behavior in plain language (already in [[chatbot/03-personas]] / Portfolio Lab UI). Add a short “For recruiters” block with 3 sample questions Orby can answer from catalog.

**Schema:** `FAQPage` entries for recruiter use case (optional).

**Do not claim** Orby replaces human interview — position as “evidence-backed first pass.”

### Priority 3 — Best portfolio site (classic SEO)

Compete on **specificity**, not “best portfolio” superlatives. Win long-tail: “Next.js Sanity portfolio with 3D background and AI lab.”

**Tactics:** Core Web Vitals pass, strong OG previews, GSC query optimization once data exported.

### Priority 4 — AI pet / companion (Orby character)

Companion products spread via **character, UGC, and shareability**, not traditional SEO ([Character.AI community scale](https://thecompanionreport.com/apps/character-ai) is community-driven). For Orby:
- Lean into mascot/consistency in copy (“tiny astronaut buddy”) **without** unprofessional recruiter-facing tone
- Short screen recordings (Loom/TikTok) of weirdo/friend persona → shareable hooks
- Do **not** optimize primary metadata for “AI pet” — keep recruiter cluster clean

### Priority 5 — Best AI lab

Frame Portfolio Lab as a **public interactive lab** for grounded agents: personas, tools, evals, degraded mode. One dev.to/Hashnode post: “Building a grounded portfolio agent with closed tools” → canonical link back.

---

### Ranking #1 for "Anant Gupta"

> Added 2026-09-05. Live-searched "Anant Gupta" and three qualified variants to answer the user's literal ask ("make sure we get my portfolio as the first result upon searching my name") honestly, not aspirationally.

#### The bare name is not winnable near-term — here's the actual competition

A live search for **"Anant Gupta"** (bare name, no qualifier) returns, on page one: a **Wikipedia article** for an Anant Gupta (former President & CEO of HCL Technologies, later founder of TECHCELX), a **Washington Post staff profile** (a Post reporter/researcher who moved to Scroll.in as a political correspondent, Pulitzer finalist team member), a **Google Scholar** author page, a **Kedaara Capital** (VC firm) team-member page for a board director at Lenskart/Purplle/Vishal Megamart, and several unrelated LinkedIn profiles under the same name (a Deloitte intern, a GrowthToolkit/WhatChimp founder, a Bay Area professional, an Apple backend engineer). A search for **"anantgupta.dev"** itself surfaces zero results about this portfolio — it returns GitHub users with similar handles (`anantgupta`, `anantgupta129`, `anantgupta2`) and unrelated social profiles instead. The domain is not indexed with any authority yet.

**Why this matters for strategy:** Wikipedia and a major newspaper's staff-profile page are close to un-outrankable by a personal site for a bare two-word name query — those pages carry decades of aggregate domain authority no amount of on-page SEO overcomes in a realistic timeframe. Promising "#1 for 'Anant Gupta'" as a near-term goal would be setting up a guaranteed miss.

#### What's actually winnable, and the honest sequencing

| Query | Realistic outcome | Why |
|---|---|---|
| `Anant Gupta` (bare) | Not top-3 near-term; possible over years with sustained backlinks + Knowledge Panel eligibility | Wikipedia/WaPo-tier competition |
| `Anant Gupta portfolio` | **Winnable in weeks**, once Phase 5A (metadata/sitemap) ships | Zero competition found — no other "Anant Gupta portfolio" result surfaced in search |
| `Anant Gupta developer` / `Anant Gupta software engineer` | **Winnable short-term** | Low, unspecific competition; the other Anant Guptas found are exec/journalist/VC/researcher, not branded as "developer" |
| `Anant Gupta UMN` / `Anant Gupta Minneapolis` / `Anant Gupta computer science` | **Winnable short-term**, and the most useful query for the actual audience (recruiters searching a specific candidate) | Geographic + institutional qualifiers eliminate essentially all name-collision competition |
| `anantgupta.dev` | **Winnable immediately** once indexed — exact-domain queries almost always resolve to the domain itself | Currently unindexed; first crawl after Phase 5A ships should fix this |

**Recommendation:** stop optimizing for the bare name as the success metric. Target the qualified queries above in on-page copy, meta descriptions, and the `Person` JSON-LD `jobTitle`/`description` fields (e.g. "Anant Gupta, computer science student at the University of Minnesota Twin Cities" — a sentence a recruiter's exact search would match). The bare-name query becomes winnable as a multi-year side effect of accumulated backlinks, not a Phase 5 deliverable.

#### Entity-building plan (the actual lever for name search, distinct from general site SEO)

This is a different problem than "SEO the portfolio page" — it's "give Google one coherent identity to attach the name to." Current best-practice guidance (2026 personal-brand SEO sources) converges on the same short list note 01 already has half-built:

1. **One consistent identity across every property** — same name spelling, same headshot/avatar where a photo appears, same one-line bio phrasing on GitHub, LinkedIn, and the portfolio. Inconsistency (a nickname on one, full name on another) actively prevents Google from merging signals into one entity.
2. **`Person` schema is the correct mechanism** (already drafted in `## Structured Data Spec` above) — its `sameAs` array is exactly the cross-property linking signal entity-SEO guidance recommends. **Action:** populate every real URL (GitHub, LinkedIn, and anything else that exists) — a `sameAs` array with placeholder `REPLACE_IF_PUBLIC` values (as currently drafted above) does nothing until filled in.
3. **Backlinks from the user's own other properties reinforce canonicality** — a GitHub profile README linking to `anantgupta.dev`, and a LinkedIn "Featured" link to the same URL, are two free, zero-cost backlinks from already-high-authority domains (GitHub and LinkedIn both rank extremely well) pointing at the portfolio. This table's own [[#Free Distribution and Authority Moves]] section below already recommends both — this is the SEO mechanism *why* that recommendation matters, not a new task.
4. **Wikidata / Knowledge Panel eligibility: not realistic, don't pursue.** Wikidata and Google Knowledge Panels are generally reserved for people with independent notability coverage (press, notable org affiliation) — a CS student's personal portfolio does not meet that bar today, and pursuing it (e.g. attempting to create a Wikidata entry) would likely be rejected or flagged. Skip this rather than spend effort on it; revisit only if genuine third-party press coverage happens later (e.g. a hackathon win with press pickup).

**No ranking guarantee, consistent with this note's existing framing:** all of the above increases *entity clarity and citation eligibility*; it does not purchase a #1 slot. Measure via the qualified-query table above, not the bare name.
### Portfolio Award & Directory Submissions

> Added 2026-09-05, in response to the user's ask for "suggested portfolio awards." Researched live 2026 pricing/process for the major showcase directories. Respects the existing "no paid backlink vendors, no Product Hunt" exclusion below — these are a different category (curated design/dev showcases, not backlink brokers), evaluated on their own merits.

**Framing:** a listing on a curated showcase site is a credibility signal + a backlink + occasional referral traffic — it is not a guaranteed AI-citation or search-ranking lever (per the GEO research below: even being included in a "best of" listicle does not mean the aggregator actually recommends *you* — Lily Ray's 2026 B2B study found AI Overviews cited self-promotional listicles but excluded the underlying publisher from the actual recommendation 69% of the time). Treat these as portfolio-quality/networking wins, not an SEO shortcut.

| Directory | URL | Cost | Fit for this portfolio | Recommendation |
|---|---|---|---|---|
| **Siteinspire** | siteinspire.com | Free (1–3 week review) | Good — accepts individual dev/design sites, not agency-only | **Submit now**, zero cost, zero downside |
| **Godly** | godly.website | Free, pure curation (no awards) | Good — curation-only site, developer-friendly bar | **Submit now**, zero cost |
| **Land-book** | land-book.com | Paid submission (editorial review) | Weak — Land-book skews toward startup landing pages / marketing sites, not personal dev portfolios | **Skip** — poor fit for the fee |
| **Dribbble** | dribbble.com | Free portfolio account (Pro tiers $4–99/mo unnecessary) | Weak — Dribbble's audience is visual/graphic design shots, not full working sites; a 3D/AI-agent portfolio doesn't fit the format | **Skip**, or only cross-post a single striking visual if one exists — not a submission priority |
| **CSS Design Awards** | cssdesignawards.com | $50/submission | Moderate — accepts individual developer sites, but the bar and audience skew toward visual polish over the "AI agent demo" angle this portfolio wants to lead with | **Revisit later** — only after the UI-fixes pass (pinned scroll sections, volumetric scatter) ships; submitting the current build risks a rejection that wastes the fee |
| **Awwwards** | awwwards.com | $65 single / $165/yr for 3 | Moderate-to-weak fit today — Awwwards' bar is agency/studio-grade visual craft; judges score design execution heavily, and a strong AI-feature story alone doesn't offset average visual polish. The fee is charged regardless of outcome (submission fee, not a prize entry) | **Revisit later**, same gate as CSS Design Awards — after the UI polish pass, not before |
| **Bestfolios** | bestfolios.com | Free submission (curated) | Good — explicitly a developer/engineer portfolio gallery, not a visual-design-only bar; direct audience overlap with recruiters/engineers | **Submit now**, zero cost |
| **Show HN (Hacker News)** | news.ycombinator.com | Free | **Best fit of all of these** — HN's own rule is "you must have personally worked on it, others can try/run/inspect it," and this portfolio's actual differentiator (Orby, a live grounded AI agent visitors can talk to) is exactly the kind of interactive, inspectable thing that gets traction there, unlike a static visual portfolio | **Submit — highest-leverage, zero-cost pick.** Title plainly per HN norms (no hype/exclamation/emoji): e.g. "Show HN: My portfolio has a grounded AI agent that answers questions about my work" — be present in the thread to answer questions, don't ask anyone to upvote |

**Recommended order:** Siteinspire, Godly, Bestfolios, and Show HN first — all free, all reasonable fit, no reason to wait. Hold CSS Design Awards and Awwwards until after the frontend UI-fixes pass in [[frontend/frontend-ui-fixes-tasks]] ships (pinned sections, volumetric scatter, polish) — submitting the current build to a paid, visual-craft-judged directory before that work lands risks paying twice (once now for a likely-weaker submission, again later for a resubmission). Skip Land-book and Dribbble outright — wrong audience/format, not worth the cost or effort either way.
## Free Distribution and Authority Moves

No paid SEO. Leverage vault-documented assets:

| Channel | Vault / repo anchor | Action |
|---------|---------------------|--------|
| **GitHub README** | `https://github.com/anantgupta129`; profile work in [[60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/gupta-builds/08-27 gupta-builds profile README five fixes\|gupta-builds README session]] | Pin portfolio repo; README bullets: live URL, Orby demo GIF, stack, link to `/api/chat` architecture note in vault |
| **LinkedIn** | [[10_Areas/Career/Internships/Cheats/Resume Tailoring, LinkedIn Search & Outreach Discovery\|LinkedIn cheats]]; profile refresh sessions in vault | Featured link: `anantgupta.dev`; About section mirrors `Person` schema facts; post at deploy milestones |
| **Hackathons / Devpost** | [[10_Areas/Career/Hackathon/Hackathons\|Hackathons]] playbook — post-hackathon: Loom, case study, GitHub, LinkedIn with judge tags | Each hackathon project README links to `anantgupta.dev` as “full portfolio” |
| **Sanity schema social fields** | `profile.socialLinks`: github, linkedin, devto, medium | Fill empty URLs in CMS → flows to footer + `sameAs` in JSON-LD |
| **Blog / external** | Sanity `blog` section + pinned GitHub card | One technical post on Orby grounding; link home with UTM-free canonical URL |
| **Internship applications** | Resume/cover per [[10_Areas/Career/Internships/Cheats/Resume Tailoring, LinkedIn Search & Outreach Discovery\|MavGPT sequence]] | Consistent URL `https://anantgupta.dev` everywhere |

**Not in scope (user confirmed):** Product Hunt launches, paid backlink vendors, LinkedIn Premium for SEO alone.

---

## Agent-Callable Orby — AEO Case (Deferred)

**Status:** Explicitly **deferred**. Parallel security session owns go/no-go on exposing machine-callable Orby ([[chatbot/01-api-route]] today: origin check, HMAC cookie, Turnstile, Upstash limits, scraper UA block).

**AEO upside if ever approved:**
- External agents (ChatGPT custom GPT, Perplexity tasks, Claude projects) could query the same grounded catalog Q&A without scraping HTML
- Aligns with [[Web Ingestion Implementation#Agent-Ready Infrastructure (AEO + MCP) - BUILD|original MCP proposal]] and [[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan#Follow-Up Idea, Not Yet Committed: Agent-Callable Orby|00 follow-up]]
- Google [agent-friendly sites guidance](https://web.dev/articles/ai-agent-site-ux) favors semantic HTML today; **WebMCP** is experimental for in-page tools — distinct from server MCP

**Official MCP HTTP pattern ([MCP authorization spec 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)):**
- OAuth 2.1 + PKCE; Protected Resource Metadata (RFC 9728)
- Token audience validation; **token passthrough forbidden**
- Scoped tools; rate limits stricter than widget

**This note does not decide implementation.** Dependency: security session sign-off → then optional Phase 6 spec note.

---

## Phase 5+ Action Plan

Picks up where [[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan|00]] left off. Phases 1–4 completion precedes meaningful Phase 5 audit.

### Phase 5A — Close infrastructure gaps (complete 00 Phases 1–4)

1. Add `metadataBase`, canonical, root title template
2. Ship `sitemap.ts` + `robots.ts`; confirm `Sitemap:` line
3. Validate OG/Twitter with [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/), Twitter card validator
4. Publish `/privacy` via [[60_Claude/05_Clippings/Web/Security/App Privacy Policy Generator\|App Privacy Policy Generator]] — cover Clerk, Cloudflare Turnstile, Upstash, Sanity, Vercel Analytics, AI providers (Gemini/Groq/Mistral per [[chatbot/02-model-router]])
5. Submit/resubmit sitemap in **GSC**; set up **Bing Webmaster Tools** + IndexNow (optional)

### Phase 5B — Structured data + agent courtesy files

6. Implement `@graph` JSON-LD (Person, ProfilePage, WebSite, Orby SoftwareApplication)
7. Add `/llms.txt` at apex ([spec v2](https://llmstxt.org/)) — links to home, privacy, GitHub, “Portfolio Lab” anchor; **Optional** section for hackathon projects
8. Consider `/llms-full.txt` or `.md` companions only if maintainable

### Phase 5C — Measurement baseline (GSC already exists)

9. **Export from GSC:** Performance → last 28/90 days → top queries, pages, CTR; Generative AI report if enabled
10. Record baseline in vault (append to this note or child note)
11. Run **AEO audit** (from 00): ask ChatGPT, Perplexity, Claude: “What do you know about anantgupta.dev?” / “Who is Anant Gupta CS portfolio?” — screenshot answers; compare to on-page facts
12. Core Web Vitals report in GSC + Lighthouse on mobile

### Phase 5D — Content + distribution (priority cluster)

13. Add “Portfolio Lab / Orby” factual blurb to hero or about (server-rendered text)
14. One GitHub README refresh + one LinkedIn post linking live lab
15. Apply [[10_Areas/Career/Hackathon/Hackathons#Post-Hackathon (Win or Lose — Document Within a Week)|hackathon postmortem template]] to next event with portfolio URL
16. Optional: one dev.to article (grounded agent architecture) — **only if** dev.to URL added to Sanity `socialLinks`

### Phase 5E — Iterate monthly

17. Refresh `dateModified` in ProfilePage when substantive content changes
18. Re-run AEO audit after major Orby/catalog changes
19. Review robots policy when new AI crawlers ship (check vendor docs quarterly)

### Phase 6 — Agent-Callable Orby (blocked)

20. **Blocked on security session.** If approved: separate spec for MCP/OAuth, scoped read-only tools mirroring [[chatbot/04-tools]], no token passthrough, audit logging

---

## llms.txt Starter (draft content)

Publish at `https://anantgupta.dev/llms.txt` when ready:

```markdown
# Anant Gupta Portfolio

> Personal portfolio and AI lab for Anant Gupta — CS @ UMN, builder of grounded chat agent Orby (Next.js, Sanity CMS, Portfolio Lab).

Important: Orby Q&A is available in the browser at Portfolio Lab; the `/api/chat` endpoint is not a public API.

## Core
- [Home](https://anantgupta.dev/): Profile, projects, experience, skills, Portfolio Lab
- [Privacy Policy](https://anantgupta.dev/privacy): Data handling for chat and auth

## Projects
- [GitHub](https://github.com/anantgupta129): Source repositories

## Optional
- [Hackathon playbook](https://anantgupta.dev/): See LinkedIn/GitHub for Devpost submissions
```

---

## Evidence

### Vault
- [[AEO & SEO/00 - Agent-Ready Infrastructure Build Plan]] — original phased build (July 2026)
- [[architecture/01-nextjs-routes]] — stale June snapshot; superseded by status table above
- [[chatbot/00-orby-overview]] — Orby capabilities and phases
- [[chatbot/01-api-route]] — security gate stack for deferred MCP idea
- [[10_Areas/Career/Hackathon/Hackathons]] — post-hackathon distribution playbook
- [[60_Claude/05_Clippings/Web/Security/App Privacy Policy Generator]] — Phase 4 tool (still valid: free, open-source)
- [[Web Ingestion Implementation#Agent-Ready Infrastructure (AEO + MCP) - BUILD]] — source AEO/MCP proposal
- [[00_Execution]] — BUILD verdict for agent-ready infrastructure

### External — Google Search Central
- [AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features)
- [Optimizing for Generative AI Features (AEO/GEO guidance)](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals)
- [ProfilePage structured data](https://developers.google.com/search/docs/appearance/structured-data/profile-page)
- [SoftwareApplication structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app)
- [Sitemaps report (Search Console)](https://support.google.com/webmasters/answer/7451001)

### External — AI crawlers
- [OpenAI crawlers overview](https://developers.openai.com/api/docs/bots)
- [Perplexity crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [Anthropic crawler FAQ](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)

### External — Bing / freshness
- [Bing: Sitemaps in AI-powered search (2025)](https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search)

### External — Market / agents
- [Imperva Bad Bot Report 2026](https://www.imperva.com/blog/bad-bot-report-2026-bots-agentic-age/) — 53% automated traffic 2025
- [Google web.dev: Build agent-friendly websites](https://web.dev/articles/ai-agent-site-ux)
- [llms.txt specification v2](https://llmstxt.org/)

- Live search results for `"Anant Gupta"`, `"Anant Gupta" portfolio developer University of Minnesota`, and `anantgupta.dev` (2026-09-05) — SERP competition basis for [[#Ranking #1 for "Anant Gupta"]]
- [Personal Brand SEO: How to Rank for Your Name & Control What Google Shows](https://www.media-village.co.uk/marketing/personal-brand-seo-guide/) — entity clarity, `sameAs`/schema, consistency-across-properties guidance
- [Entity SEO: Complete Guide to Ranking in 2026](https://decodegrowth.in/blogs/why-entity-seo-is-the-new-ranking-advantage/)
- [Kevin Indig, ChatGPT citation behavioral study, July 2026](https://searchengineland.com/mastering-generative-engine-optimization-in-2026-full-guide-469142) — 44.2% of ChatGPT citations came from the first 30% of a page
- [Lily Ray, 2026 B2B AI Overviews citation study](https://searchengineland.com/mastering-generative-engine-optimization-in-2026-full-guide-469142) — self-promotional listicles cited but publisher excluded from recommendation 69% of the time — basis for the award-directory framing caveat
- [Awwwards](https://www.awwwards.com/) — $65 single submission / $165/yr for 3
- [CSS Design Awards](https://www.cssdesignawards.com/) — $50/submission
- [Siteinspire](https://www.siteinspire.com/) — free submission
- [Godly](https://godly.website/) — free, curation-only, no fees
- [Land-book](https://land-book.com/) — paid editorial submission, startup/landing-page focus
- [Bestfolios](https://www.bestfolios.com/) — free developer/engineer portfolio gallery
- [Hacker News Show HN guidelines](https://news.ycombinator.com/item?id=47205127) — "you must have personally worked on it, others can try/run/inspect it"

### External — MCP (deferred Phase 6)
- [MCP Authorization spec (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### Repo verification (2026-09-05)
- `src/app/(portfolio)/layout.tsx` — `generateMetadata()` with openGraph/twitter
- No `src/app/sitemap.ts`, `src/app/robots.ts`, privacy route, or JSON-LD
- `README.md` — production domain `anantgupta.dev`, `NEXT_PUBLIC_SITE_URL`, Vercel Analytics

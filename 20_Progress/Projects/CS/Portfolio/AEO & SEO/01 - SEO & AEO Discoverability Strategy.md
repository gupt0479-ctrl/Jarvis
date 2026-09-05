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
next: "Export GSC impressions/clicks/queries for anantgupta.dev, then implement sitemap.ts + robots.ts + metadataBase"
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

### External — MCP (deferred Phase 6)
- [MCP Authorization spec (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### Repo verification (2026-09-05)
- `src/app/(portfolio)/layout.tsx` — `generateMetadata()` with openGraph/twitter
- No `src/app/sitemap.ts`, `src/app/robots.ts`, privacy route, or JSON-LD
- `README.md` — production domain `anantgupta.dev`, `NEXT_PUBLIC_SITE_URL`, Vercel Analytics

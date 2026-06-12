---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - sanity
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[09 - Sanity Content Spec]]"
---
# Sanity as Single Source of Truth
The second thesis of the rebuild. The brief says, in many places and many ways, the same thing: **nothing on a card may be hardcoded; everything renders from Sanity; the same skill must look identical everywhere.** This note is the data contract that makes that true. The actual content to load lives in [[09 - Sanity Content Spec]]; this note is the *schema + rule*, that note is the *data*.

## The core move: `skill` is a referenced document, not a string
Today, skills are strings typed into each section, so the same skill ("Python") shows up in different colours in Experience vs Projects vs Skills, and "is not even close to what is on the Sanity backend." Fix the cause, not each symptom.

- Create/confirm a single `skill` document type: `{ name, slug, category (ref → skillCategory), color, level (beginner|intermediate|advanced), familiarity (0–100 for the graph), blurb }`. **`color` is defined once, here.**
- Every other document that mentions a skill holds an **array of references to `skill`**, never inline strings: `experience.skills[] → ref(skill)`, `project.skills[] → ref(skill)`, `certification.skills[] → ref(skill)`.
- Every chip component across the site is the same `<SkillChip skill={ref}>` that renders **only `color` + `name`** (the brief's exact requirement, stated for Experience, Projects, and Certifications). Change a skill's colour once in Sanity → it changes everywhere. This is the whole point.

## `skillCategory` drives the graph and the category buttons
- `skillCategory`: `{ name, slug, color, description, order, defaultOpen (bool) }`. The categories are the lines on the capability graph and the floating buttons beside it ([[05 - Skills Capability Graph]]).
- The category whose `defaultOpen` is true renders first; the rest are user-selectable. (Brief item 9: "on automatic the most high-level skill category renders.")
- The category `description` is the text that appears **only when its button is clicked** (brief item 10).

## What every section must read from Sanity (no hardcode audit)
This is the checklist Claude Code verifies per section — if any of these is hardcoded today, it's a bug to fix.

| Section | Must come from Sanity |
|---|---|
| Experience | role, company, **employmentType**, location, dates, **description** (long form), achievements, `skills[]→ref`, companyLogo, companyUrl, order |
| Projects | title, slug, tagline, **description/summary**, `skills[]→ref`, repoUrl, liveUrl, category, featured, order |
| Skills | the `skill` registry + `skillCategory` registry — names, colours, levels, familiarity, descriptions |
| Education | school, degree, field, dates, gpa, logo, description, stage (middle/high/college) |
| Certifications | title, issuer, issueDate, expiryDate, credentialId, credentialUrl, `skills[]→ref`, issuerBadge |
| Achievements | year, title, type, issuer, one-line description, optional url |
| Blog | the GitHub pinned card + each resource card (category, title, excerpt, date, readTime, url) |
| Contact / Footer | email, location, social links, footer phrase — pull from `profile`/`siteSettings`, not literals |

## Fields flagged as not rendering (fix list, from `[[Portfolio]]` Sanity-fixes section)
Carry these specific breakages into the build so they're closed, not rediscovered:
- **Experience:** `employmentType` (render next to location), `description` (currently not rendered at all), `achievements`, `companyLogo`, `companyUrl`.
- **Projects:** `slug` (also the chatbot's closed-enum needs it — keep clean slugs), `tagline`; "entirely broken" → rebuild the read query.
- **Skills:** the whole division differs from Sanity; rebuild against the `skill`/`skillCategory` registry. The graph stopped rendering — see [[05 - Skills Capability Graph]].
- **Education:** `description`, `logo` (needed).
- **Certifications:** `issueDate`, `expiryDate`, `credentialId`, `credentialUrl` (the out-link), badge optional.
- **Achievements:** `issuer`, `date` (year), `url`.

## GROQ + typing discipline
- One typed query module per section (`lib/sanity.queries.ts`), each dereferencing `skills[]->{name,color,slug}` so chips never need a second fetch.
- Generate types from the Sanity schema; the section components consume typed data, no `any`.
- **Live reads**, not a build-time snapshot, so content edits show without a redeploy (consistent with the chatbot plan's grounding approach).
- If a referenced field is missing, render nothing for it gracefully — never a hardcoded fallback string.

## Phase ordering consequence
Because every visual section depends on this contract, **Sanity-as-SoT is Phase 0** of the build. Schema first, real content loaded ([[09 - Sanity Content Spec]]), then the motion primitives, then sections. Building a pretty Experience card against hardcoded skills would just have to be torn out.

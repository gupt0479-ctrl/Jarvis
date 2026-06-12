---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - certifications
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[01 - Motion System & Comet Cards]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Certifications & Achievements
> **Reconciled to [[10 - Codebase Reality & Confusion Clearance]].** Files: `src/components/sections/CertificationsSection.tsx`, `AchievementsSection.tsx`.

## Certifications (brief item 15)
Kicker `// credentials`. Per note 10, the section already: centers the h2, uses `CometCard variant="dark"`, applies the holographic corner via the `cert-card` class (`::after` in `globals.css`), and renders logo banner, name, `credentialId`, issuer, dates, description, **`skills[]`→refs** (the certification type correctly uses `skills[]`, not `technologies[]`), and a "View Credential →" link. So most of the first draft's asks are already done.

Real work:
- **Centre the description too** (h2 is centered; the left-aligned description should match).
- Confirm skill chips use the shared category-coloured `<SkillChip>` (colour from category, **no `color` field**).
- Credential action stays an **out-link** (`credentialUrl`) — no on-site credential detail view.
- **Delete the fake certs in Sanity Studio** (AWS SA-Pro, GCP PCA, CKA, TensorFlow Dev, MongoDB Dev). Section returns `null` when empty (`if (!certs?.length) return null`). Populate only genuinely-held credentials — ask Anant; invent none.

## Achievements & Awards (brief items 16, 19)
Per note 10, today it's a small `py-8` section wrapping a single `CometCard variant="subtle"` around a vertical timeline rail (left gradient line at `left-6`, dots per row), ordered `featured desc, date desc`, rendering year, featured dot, title, type chip, issuer, description, external `url` button. **Gap: no kicker, no styled/centered h2** — the header is a bare `<h2>`.

Real work:
- **Add a section kicker + centered h2** matching the other sections.
- **Move the rail OUTSIDE the box.** Today the rail lives inside the `CometCard`. Extract it to the shared `SpaceRail` ([[01 - Motion System & Comet Cards]]) rendered *beside* the rows, not as a line within a card — "exactly like the experience timeline." Years sit **close to the title** once the rail is separated.
- Keep it low-bulk, theme-matched, subtle row hover. Keep the `url` external-link button.

## Done conditions
- Certifications: description centered; shared category chips; out-link only; fake certs deleted; nothing invented.
- Achievements: kicker + centered h2 added; rail extracted **outside** the box via shared `SpaceRail`; years tight to titles; low-bulk, theme-matched.

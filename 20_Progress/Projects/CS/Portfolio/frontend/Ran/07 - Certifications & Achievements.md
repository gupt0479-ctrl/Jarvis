---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-13
tags:
  - portfolio
  - frontend
  - certifications
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[14 - Global Fixes — Header & Section Spacing]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[BUILD-STATUS]]"
---
# Certifications & Achievements
> **Refinement pass (2026-06-13).** Both built. `CertificationsSection.tsx` (3-col grid, `CometCard variant="dark"`, `.cert-card::after` glare via `getGlareOverlay()`/`getInnerCard()`). `AchievementsSection.tsx` (now a rail + cards layout per the screenshots). Fix list below.

## Certifications (BUILD-STATUS UI Fix #10)
1. **Dial the comet DOWN.** The cert cards tilt too hard — reduce `CometCard` tilt magnitude. Keep the glare/holographic corner.
2. **Skill chips = colour + name only, from Sanity.** Use the shared chip with the new `skill.color` dot ([[02 - Sanity as Single Source of Truth]]); certifications use the `skills[]` ref field.
3. **Everything else is an out-link.** The credential detail (ID, issuer, dates) is supporting text; the action is a single external link (`credentialUrl`) to the issuer's verification page or the certificate. No on-site credential view.
4. **Delete fake certs** in Studio (AWS SA-Pro, GCP PCA, CKA, TensorFlow, MongoDB) — keep only genuinely-held ones; section returns `null` when empty.

## Achievements & Awards (BUILD-STATUS UI Fix #11 + [[14 - Global Fixes — Header & Section Spacing]] §3)
This is a **subsection of Certifications** — least effort, still tasteful.
1. **Smaller header, minimal gap.** The Achievements h2 must be **noticeably smaller** than a top-level section heading, centered, and sit with **almost no gap** below Certifications (they read as one block). Remove the `section-backdrop::before` dead space here too (see note 14).
2. **ONE subtle comet card for all three achievements.** Wrap the whole 3-item ledger in a **single** `CometCard` with a **transparent background**. The comet must be **subtle and barely moving** — less motion than the education cards. Not one card per achievement; one card for the set.
3. Keep the ledger content (year, title, type chip, issuer, one-line description, external link) from Sanity. Years tight to titles.

## Done conditions
- Certs: comet reduced; Sanity colour+name chips; credential is an out-link; fakes deleted.
- Achievements: small centered header, minimal gap with Certs, one transparent subtle comet card wrapping all three, content from Sanity.

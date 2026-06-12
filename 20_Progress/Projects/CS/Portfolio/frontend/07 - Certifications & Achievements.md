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
  - "[[02 - Sanity as Single Source of Truth]]"
---
# Certifications & Achievements
Files: `CertificationsSection.tsx`, `AchievementsSection.tsx`. Achievements becomes a **subsection under** Certifications.

## Certifications (brief item 15)
Kicker: `// credentials`. Centre the header (kicker + title + description), like the other sections.
- Cards use the repo's `CometCard` style — darker, compact, readable. Not just "moving cards."
- Per card, from Sanity ([[02 - Sanity as Single Source of Truth]]): issuer badge/icon, title, issuer + date, **skill chips = shared `<SkillChip>` (colour + name only) from `certification.skills[]→ref`**.
- **Everything else about the credential is an out-link.** `credentialUrl` opens the issuer's verification page or the certificate. ID/expiry are supporting text; the action is "View Credential →" to the external URL. No on-site credential detail view.
- Subtle holographic ring / corner accent; keep them tidy.
- Current certs are dummy — real ones are sparse; keep whatever is genuinely Anant's, otherwise leave the schema ready and let the user populate. Do not invent credentials.

## Achievements & Awards (brief items 16, 19)
This is the deliberately-low-effort section that should still stand out. Currently garbage; make it match the theme above.
- Present as a clean **ledger / timeline**, not bulky cards: year · small icon · title · type chip · one-line description · optional external link. All from Sanity (`issuer`, `date` as year, `url`).
- **The line moves outside the box** and is rendered with the **same `SpaceRail`** used by Experience ([[01 - Motion System & Comet Cards]]) — a single subtle glowing rail beside the rows, not a border drawn on a box.
- Years sit **close to the text** once the rail is separated from the box (tighten the year ↔ title gap).
- Subtle row hover; keep it elegant and minimal. Kicker optional — omit if cleaner.

## Done conditions
- Certifications header centred; compact comet cards; Sanity skill chips; credential action is an out-link only; no invented certs.
- Achievements is a ledger with the rail **outside** the box (shared `SpaceRail`), years tight to titles, theme-matched, low-bulk but striking.

---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-13
tags:
  - portfolio
  - frontend
  - contact
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[BUILD-STATUS]]"
---
# Blog, Contact & Footer
> **Refinement pass (2026-06-13).** All built. `BlogSection.tsx`/`BlogFeed.tsx` (`MagneticButton()`, `PINNED_GITHUB`, `.orbit-chip`), `ContactSection.tsx`/`ContactPanel.tsx` (`IridSocialButton`, social pop-out), `Footer.tsx`. Fix list below.

## Blog — "What I read or do" (BUILD-STATUS UI Fix #12)
1. **Centre the header.** The kicker (`// uplink`), the "What I Read or Do" heading, and the description must render **centered** like the other sections — currently left.
2. **Less movement everywhere; subtle comet.** There's too much motion on the cards. Make every card's comet/drift **subtle** (less than education). 
3. **GitHub card: restore the bottom-lift hover, NOT comet.** The GitHub pinned card should use the **previous effect** — on hover, only the **bottom half of the card lifts up** while the top stays put. Replace the comet on this card with that bottom-lift. **Keep** its left colour rail (looks good), icon, copy, and Visit (`MagneticButton`).
4. **Small resource cards stay translucent** with a gentle subtle comet (the GitHub card keeps its solid background; only the small cards are translucent). All Sanity-driven.

## Contact (BUILD-STATUS UI Fix #13)
The buttons + social pop-out are loved — keep them. The card itself feels meh and the shiny background should show more.
- **Make the card slightly smaller** so more of the background sphere shows around it. Keep the text and buttons clearly readable (don't over-translucent the area behind the words — a light local backing is fine). The goal: more visible background, same legibility.
- Kicker `// uplink`, "Let's build something," subhead "Internships, collaborations, or just to say hi." Email + socials from the profile singleton.

## Footer (BUILD-STATUS UI Fix #14)
- **Left edge:** `</>` programmer glyph at the **extreme left**.
- **Right edge:** year + `building in public` at the **extreme right** (e.g. `© 2026 Anant Gupta · building in public`).
- **Centre:** "Back to top" button, actually centred, with a (subtle) `CometCard`.
- **Text legibility:** raise footer text to normal readable (not glowing, not barely-visible).
- **Height:** shrink to only what's needed — it's too tall now.
- **Surface:** very subtle top border line; translucent background so the page background reaches into the footer.

## Done conditions
- Blog header centered; all cards subtle motion; GitHub card uses bottom-half-lift (not comet) + keeps its left rail; small cards translucent + subtle comet.
- Contact card slightly smaller (more background visible) with readable text/buttons preserved.
- Footer: glyph far-left, year/phrase far-right, centred comet back-to-top, readable text, compact, subtle border, translucent.

---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - contact
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[01 - Motion System & Comet Cards]]"
---
# Blog, Contact & Footer
The three closing sections. Files: `BlogSection.tsx` / `BlogFeed.tsx`, `ContactSection.tsx` / `ContactPanel.tsx`, `Footer.tsx`.

## Blog — "What I read or do" (brief item 17)
Kicker: `// uplink`.
- **GitHub pinned card:** keep the liked behaviour — it wobbles (`useSpaceFloat`) and has the unique hover where the **bottom lifts up**. Keep that; add `CometCard` polish so it feels more premium. Keep the left violet rail, GitHub icon, short copy, Visit action on the right. **Background colour unchanged** for this card.
- **Small resource cards:** each gets `CometCard` + a **more translucent background** than the GitHub card (the GitHub card stays solid; only the small ones go translucent). Category chip, title, excerpt, date/read-time, open icon. They already render from Sanity — confirm and keep.
- Don't let the background sphere wash out the text.

## Contact (brief items 18, 21) — the "frame, not fill" answer
The user's open question: the card feels meh, but the shiny background should stay visible and the text must stay readable; pure translucency isn't enough. **Resolved approach — frame, don't fill:**
- Make the card mostly an **open glass frame**: a thin luminous border + soft outer glow, with the card interior largely transparent so the shiny background sphere shows *through* it. The card defines a region in space rather than covering it.
- Put a **localized legibility scrim only behind the text/buttons** — a soft radial backdrop-blur + slight darken that hugs the email, the Copy/Open-Mail buttons, and the social row, fading to nothing at the card edges. So the background stays gorgeous everywhere except a gentle halo right behind the words, which is exactly enough to read them.
- Net effect: the background reaches into the card (matching the footer translucency idea), the text floats on its own readable halo, and the frame + `CometCard` give it presence without a heavy filled panel.
- Keep the existing buttons and social pop-out (loved). Kicker `// uplink`, heading "Let's build something," subhead "Internships, collaborations, or just to say hi." Email + social pull from `profile` in Sanity.

## Footer (brief item 22)
The footer is too tall, too dim, and not aligned to the edges. Rebuild compact:
- **Left edge:** a programmer glyph — prefer `</>` or a tasteful terminal icon over a goofy emoji.
- **Right edge:** the year + a short phrase, e.g. `© 2026 Anant Gupta · building in public`. Both the glyph and the year/phrase go to the **extreme** left/right.
- **Centre:** the "Back to top" button, actually centred, with `CometCard`.
- **Readability:** footer text is barely visible today — raise it to normal legibility (not glowing, just clearly readable).
- **Height:** shrink to only what's needed; remove the excess vertical space.
- **Surface:** a **very subtle** top border line; the footer background is **translucent** so the page background reaches into it.

## Done conditions
- Blog: GitHub card keeps wobble + bottom-lift + solid bg with comet polish; small cards comet + translucent; all from Sanity.
- Contact: open glass frame + localized text scrim ("frame not fill"); background shows through; text crisp; buttons/social preserved.
- Footer: glyph far-left, year/phrase far-right, centred back-to-top with comet, readable text, compact height, subtle border, translucent bg.

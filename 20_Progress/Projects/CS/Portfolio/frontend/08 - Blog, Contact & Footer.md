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
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Blog, Contact & Footer
> **Reconciled to [[10 - Codebase Reality & Confusion Clearance]].** Files: `BlogSection.tsx`/`BlogFeed.tsx`, `ContactSection.tsx`/`ContactPanel.tsx`, `Footer.tsx`.

## Blog — "What I read or do" (brief item 17)
Kicker `// uplink` (already present; h2 "What I Read or Do"; gated by `siteSettings.showBlog`; fetches ≤6 posts: `title, slug, excerpt, externalUrl, publishedAt, readTime, category`).
- **Read `BlogFeed.tsx` first** — AGENTS.md flags a TODO for an archive toggle that needs a Sanity schema change. Understand it before touching.
- **GitHub pinned card:** keep its wobble (`useSpaceFloat`) + the liked bottom-lift hover; add `CometCard` polish; keep the left violet rail, icon, copy, Visit action. **Background colour unchanged.**
- **Small resource cards:** add `CometCard` + a **more translucent** background than the GitHub card (only the small ones go translucent). Category chip, title, excerpt, date/read-time, open icon. Already Sanity-driven — confirm.
- Don't let the background sphere wash out text.

## Contact (brief items 18, 21) — "frame, not fill"
Per note 10, `ContactSection.tsx` fetches `email, location, socialLinks{ github, linkedin, twitter, website }` and delegates to `ContactPanel.tsx` (the header/kicker/h2 live inside `ContactPanel`). **Read `ContactPanel.tsx` before polishing.** Resolution to the open question:
- Make the card an **open glass frame**: thin luminous border + soft outer glow, interior largely transparent so the shiny background sphere shows *through* it. The card marks a region in space rather than covering it.
- Put a **localized legibility scrim only behind the text/buttons** — a soft radial backdrop-blur + slight darken hugging the email, Copy/Open-Mail buttons, and social row, fading to nothing at the card edges. Background stays gorgeous everywhere except a gentle halo behind the words.
- Keep the existing buttons + social pop-out (loved). Kicker `// uplink`, heading "Let's build something," subhead "Internships, collaborations, or just to say hi." Email + socials from the profile singleton.

## Footer (brief item 22)
`Footer.tsx` exists (too tall, too dim per the brief — trust that). Rebuild compact:
- **Left edge:** programmer glyph — prefer `</>` over an emoji.
- **Right edge:** year + short phrase, e.g. `© 2026 Anant Gupta · building in public`. Both pushed to the extreme edges.
- **Centre:** "Back to top" button, actually centred, with `CometCard`.
- **Readability:** raise footer text to normal legibility (not glowing).
- **Height:** shrink to only what's needed.
- **Surface:** very subtle top border; translucent background so the page background reaches into it.

## Done conditions
- Blog: GitHub card keeps wobble + bottom-lift + solid bg with comet polish; small cards comet + translucent; archive TODO understood before edits.
- Contact: open glass frame + localized text scrim; background shows through; text crisp; buttons/social preserved; `ContactPanel` read first.
- Footer: glyph far-left, year/phrase far-right, centred comet back-to-top, readable text, compact, subtle border, translucent bg.

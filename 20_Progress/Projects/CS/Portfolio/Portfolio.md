---
type: project
status: sprout
deadline: 2026-01-10
related_progress:
  - "[[Winter Break]]"
  - "[[Plan]]"
  - "[[Useful Links]]"
  - "[[Cheat Sheet's & Notes]]"
tags:
  - "#progress"
  - "#evergreen"
next:
---
## Dev / Data Portfolio Website with Embedded AI Agent
_(Smaller “side” project that’s fast to build and good for branding)_
**Inspiration from blog:**
- PDF-based Q&A system
- LangChain Chatbot with Memory
### [[Cheat Sheet's & Notes#Nextjs|Nextjs Ebook]]
### What it does
Your personal portfolio website that:
- Shows your projects, resume, skills
- Includes an **AI agent that can answer questions about you**:
    - “What projects has Anant done with Rust?”
    - “How did they implement RAG?”
- Powered by:
    - Embeddings of your resume, README files, project docs
    - LLM Q&A interface
### Tech stack
- Next.js + Tailwind
- Embedded chat widget using:
    - LangChain or direct embeddings + LLM
    - Does RAG over your own materials
- Use GitHub as a working directory where i will learn git commands.
### Extensions
1. **Biome**:
	- Before commits:`pnpm lint      # biome check`, `pnpm format    # biome format --write`.
	- *Pro tip*: If you’re going all-in on Biome, don’t rely on ESLint extension for this project (it can conflict). Keep Biome as the single source of truth.
	- `pnpm lint` returns clean, 
	- Your code auto-formats when you save
2. 
## Repo
```bash
ai-portfolio/
  sanity/
    schemaTypes/
      index.ts
      profile.ts
      projects.ts
      experience.ts
      skills.ts
      siteSettings.ts
  src/
    app/
      (site)/
        page.tsx
        layout.tsx
      studio/
        [[...index]]/
          page.tsx
      api/
        chatkit/
          session/
            route.ts
    components/
      nav/
      sections/
      chat/
      ui/              # shadcn
    lib/
      sanity.client.ts
      sanity.queries.ts
      env.ts
  runbook.md
  .env.local
```
## Model
Example minimal model:
- **Profile (singleton):** name, headline, bio, heroImage, socialLinks, email
- **Projects:** title, slug, description, tech stack, repoUrl, liveUrl, images, featured
- **Experience:** company, role, start/end, bullets
- **Education:** school, degree, start/end, bullets
- **Skills:** name, category, level
- **SiteSettings (singleton):** site title, SEO description, og image, nav links
### UI Enhancement
You are working on a portfolio combined with ai project. I am haflway across the project when i decided to change up the entire ai part of the website. The ui right now is basic and could be improved by a lot. I have provided you with images from the localhost currently being run and what the website looks like. You have access to all the codes and directory markdown files. Analyze each and every single thing about this website.

You are tasked to first provide me with a prompt for lovable to improve the ui for the demo webstie that it created. I want it to be completed in a single prompt, the lovable provides me with a plan. we modify that plan exactly how we want the website to be like and boom. We have the ui for our website. I want to build something better than just a chatbot to ask about my skills and projects. I want it to be interactive, look good, be charismatic, etc. I would still want the ai option to show up as a sidebar or as a hover board upon clicking a button on the right corner. It could have something funny just written over it. I want the website to be filled with these really cool small but such impressive things. The most standing out part of this portfolio should be the ai of it though. Now You have entire context about everything in this website. What exactly i wish to build. The problem here is the how we build it. I want you to first provide me with a very detailed lovable prompt that completely astonished the user on viewing this website. There are two sets of images provided to you here: Local host and lovable. Analyze each and every single image pixel by pixel and in detail. Here are the details of the things that i want to be make better about the ui:

1. The buttons on the landing screen should appear to be hovering not only on display but at all times. All the buttons across my portfolio should appear as if they are in space. All buttons should have a hover effect as well. The landing screen has too much subtitle just blow maybe and the image is not being rendered currently because it is not there. I am confused on the image i should add here.

2. Just below the about me section i want something cool to be read in 4 columns like seen now. But i want this to stand out. The current about me just looks too bland. Esepcially the line after content and those 4 headings. Make something better show up just after the content in about me.

3. The comet card appears to hover all over the portfolio but in experiences it might just appear to be too big for the screen. It looks weird, all the comet cards background colors were changed to be transparent because they were too shiny. Now they are just completely glass. I want something translucent, i want something that does not outshine the background of the portfolio. Make the color appear more for all the cards. The experience section timeline line could be more better, the line looks weird and the dots are not exactly aligned. Make the line appear almost eye pleasing while scrolling through the experience section.

4. The projects card is one of the most ugliest things i have seen here. the butons appear just on top of the card making it look compact. The slider looks so shitty. I want these projects on the left and right to appear like they are in space. When clicked on the left or ride button they come to the center with a smooth transition effect. I want these two left and right cards to wandering at the same opacity they are at. Maybe the background could also be interactive over here with getting the card to the center, some sort of a string pulling it towards the center upon clicking left or right.

5. The skills and expertise graph just looks really shitty. I want it to appear as a trading stock graph sort of with multiple trajectories as lines such as ai, devops etc. We can see that the user is progressing towards what more. Make this graph appear much more aesthetic and appealing to the eyes. The buttons below the skills section are complete garbage, they look so shit and they do not do anything. Nothing on hovering or clicking. I want each button on the skills section to do something. I want each skills section to have something unique in them. Each of them do something unique upon clicking or hovering.

6. I want the education sections to be like a flowchart. There will be three parts to this flowchat: Middle school, high school and college. I want the top to be college obviously but this appear as this really cool flowchat that actually floats(pun). I want this also to appear as if it is in space.

7. The certification cards are comet cards and could be darker like mentioned above, i want these to also be something cool than just a moving card.

8. Achievements & Awards is a section that i want to put least efforts and want it to stand out. Just a basic line next to it and some cool text. Currently looks completely garbage, make it fit the theme above.

9. what i read or do also use comet cards. I need you to darken each card, make it more better. The github color on the left looks really nice and the unique hover effect is good. I want it to appear more ui appealing to user. Then comes the end contact card. I want the email to appear int the center and make the card a little smaller. I want more buttons on there like instagram, etc.

10. Footer is the uggliest thing i have seen in my entire life. I want you to remove the center context written and change it to something less cringe and short. Right next to those workds should be back on top with the button. The year should appear on the right most side with something else cool next to it. On the left most side should be an emoji for a programmer.
## Final UI Refactor
```text
# Pasteable UI Refactor Prompt

You are refactoring my real portfolio repo, not a generic demo. This is a Next.js 16 App Router portfolio with Sanity, Tailwind v4, shadcn/Radix, Framer Motion/Motion, Three.js/R3F, Clerk, and an existing OpenAI ChatKit sidebar that I want to replace.

Your job is to redesign every visible UI component into a premium cosmic AI portfolio. Keep the current dark Three.js space identity, but make the interface feel intentional, interactive, charismatic, and technically impressive. The AI/Portfolio Lab should become the standout feature, not a basic chatbot.

Use the actual repo structure:

- `src/app/layout.tsx`
- `src/app/globals.css`
- `src/components/PortfolioContent.tsx`
- `src/components/HeaderScrolling.tsx`
- `src/components/DarkModeToggle.tsx`
- `src/components/SidebarToggle.tsx`
- `src/components/app-sidebar.tsx`
- `src/components/chat/*`
- `src/components/three/ObsidianBackground*`
- `src/components/three/ProjectsSlider.tsx`
- `src/components/ui/comet-card.tsx`
- `src/components/sections/*`
- `src/components/cards/ExperienceCard.tsx`
- `src/components/ContactPanel.tsx`
- `src/components/BlogFeed.tsx`
- `src/components/Footer.tsx`

Do not create fake Vite files, `src/pages`, `index.html`, or `tailwind.config.ts`. This is the real Next/Sanity repo.

## Overall Direction

The website should feel like a floating portfolio command center inside space. Think: cosmic terminal, orbital cards, evidence-backed AI lab, intelligent microinteractions, dark translucent surfaces, violet/cyan/green signal accents, and lots of tiny delightful details.

Keep the current localhost hero direction: dark starfield, particle sphere, Anant Gupta large, animated headline, social icons, location, availability. Improve it rather than replacing it with a big visible hero card.

Borrow from the Lovable UI only where useful:

- Add commented section labels like `// hi, I'm`, `// scan report`, `// trajectory`, `// build log`, `// capability matrix`, `// origins`, `// credentials`, `// uplink`.
- Use the terminal popover idea.
- Use the cleaner experience rail.
- Use darker colored cards.
- Use the improved contact/footer direction.
- Do not blindly copy Lovable’s content or fake Alex Morgan data.

## Global Design System

Create reusable utilities in `src/app/globals.css`:

- `.cosmic-card`: dark translucent card, visible but not shiny.
  - Background around `rgba(9, 10, 18, 0.72)` to `rgba(14, 16, 28, 0.82)`.
  - Border `1px solid rgba(167,139,250,.22)`.
  - Inner shadow and faint violet/cyan outer glow.
  - Backdrop blur but not fully transparent.
  - Text must remain readable over the Three.js sphere.

- `.float-btn`: all buttons must look like they are floating even when not hovered.
  - Default: slight raised shadow, `translateY(-1px)`, subtle border glow.
  - Hover: lift more, brighten border, cursor-follow sheen if practical.
  - Active: press down slightly.
  - Apply to hero CTAs, project buttons, carousel arrows, contact buttons, AI Lab buttons, footer back-to-top, and social buttons.

- `.section-kicker`: small commented label above section titles.
  - Style like code comments: `// scan report`.
  - Use cyan/violet-muted color that fits the current background.
  - Add to every section except Achievements/Awards if it makes that section cleaner.

- `.orbit-chip`: skill/tag pill with darker surface, colored dot, and category-specific hover.

- Improve `CometCard`:
  - Keep the 3D hover, but reduce tilt for large cards.
  - Add an option/variant for darker cards.
  - Avoid fully transparent cards and avoid over-bright glare.
  - Large experience/contact/achievement cards should feel like floating slabs, not warped glass.

Make sure all text fits on mobile and desktop. Do not let the Three.js sphere make text unreadable.

## Background

Keep `ObsidianBackground`, but tune it:

- Reduce visual intensity behind text-heavy sections.
- The particle sphere should never cover or overpower readable content.
- Add section-aware depth if possible: hero can be more open; content sections need stronger cards or darker local backing.
- Respect `prefers-reduced-motion`.
- Mobile: reduce particle counts and avoid huge sphere overlap.

## Header / Navigation / Theme

Improve `HeaderScrolling.tsx`:

- Keep sticky/scroll behavior but make the header feel like a floating orbital nav bar.
- Logo can remain `Anant.` or become `AG_`; use one consistently.
- Add nav items: Home, About, Experience, Projects, Skills, Education, Certifications, Blog, Contact.
- Add subtle active section state if feasible.
- Fix theme toggle behavior. If light mode is not fully supported, either make it work cleanly or convert the control into a polished “dark mode locked” visual toggle. Do not leave a broken-looking theme provider.
- Mobile nav must collapse cleanly into an accessible menu/sheet.

## Hero

Files: `HeroSection.tsx`, `HeroContent.tsx`, `ProfileImage.tsx`.

Keep the current hero layout mostly intact. Do not put the whole hero inside a giant card.

Changes:

- Add a small section kicker above the name: `// hi, I'm`.
- Use a color like cyan/violet that is visible but not loud.
- Keep `Anant Gupta` large and elegant.
- Shorten the bio so the hero does not feel text-heavy.
- Keep animated “Building data pipelines / AI solutions / web applications” headline.
- Make all CTA buttons floating by default.
- Improve social icon buttons with floating style and hover glow.
- Since the profile image is missing, do not render a broken/empty image area. Instead:
  - Option A: Add a compact floating terminal module on the right side if it fits.
  - Option B: If the hero becomes crowded, move the terminal module into About.
- Terminal module design:
  - Dark rounded terminal.
  - Top dots red/yellow/green.
  - Path text `~/anant`.
  - Lines:
    - `$ whoami`
    - `anant.gupta — ai & data systems engineer`
    - `$ stack --top`
    - `rust · typescript · python · postgres · llms`
    - `$ status`
    - `shipping → research/agents · ui/ux · data pipelines`
  - Include one or two orbiting chips such as `Next.js`, `Rust`, `LLMs`.

Replace all “AI Twin” language in hero/sidebar with “Portfolio Lab” or “AI Lab.”

## About

Files: `AboutSection.tsx`.

Do not put the entire About section in one big card if it ruins the current centered flow. The current About is too bland; improve it with structured visual content.

Required:

- Add kicker: `// scan report`.
- Keep the main About content centered and readable.
- Use a clean text block, not an overdone card.
- Below the text, add a standout visual area:
  - Two larger dark boxes or panels.
  - One can contain the terminal module if it did not fit in hero.
  - The other can contain “Mission Telemetry” or a visual diagram of Anant’s focus.
- Replace the current plain 4-stat row with a more impressive system:
  - Four columns/cards: Projects Built, Technologies, Currently Learning, Research Focus.
  - Each has icon, value, label, tiny sparkline/orbit mark, hover reveal, and subtle glow.
  - These should look like live telemetry, not plain headings.
- Keep all content from Sanity if available.

## Experience

Files: `ExperienceSection.tsx`, `ExperienceCard.tsx`, `CometCard`.

The current timeline rail is close but misaligned and cards feel too huge/transparent.

Required:

- Add kicker: `// trajectory`.
- Timeline line should be elegant and satisfying while scrolling:
  - Vertical glowing rail.
  - Dots perfectly aligned with card centers or card title rows.
  - Optional progress fill based on scroll.
  - Dots should glow softly and not look randomly placed.
- Cards:
  - Use darker translucent comet cards.
  - Keep hover tilt but reduce it for large cards.
  - On hover, add a smooth effect across the entire card: subtle sweeping light, signal bar, or border pulse.
  - Card content hierarchy: role, company, date, location, bullets, tags.
  - Make date placement clean and responsive.
- Avoid the giant background sphere making experience text hard to read.

## Projects

Files: `ProjectsSlider.tsx`.

The current project slider is the biggest weak point. Rebuild it.

Required behavior:

- Add kicker: `// build log`.
- Keep left and right side cards visible, floating in space, blurred/dimmed, and slightly separated from the center.
- Center card should be large, colored, dark, readable, and visually premium even before hover.
- Left/right arrow buttons should sit vertically centered beside the main card, not on top of it.
- On clicking left/right:
  - Side card should glide into center smoothly.
  - Center card should move out.
  - Add subtle particle trail, elastic tether, or “string pull” visual toward the center.
- Keep pagination dots below, styled as glowing orbit dots.
- Active card content:
  - Title, tagline, tech chips.
  - Live and Source buttons as floating buttons.
  - Add a small inner box inside the active project card that shows a specific project detail, metric, system note, or “case note.”
  - Keep current hover-to-show-more behavior, but make it polished. The card should not feel empty before hover.
- Side cards should not be too close together or cramped.
- Keyboard arrows and swipe should continue to work.

## Skills

Files: `SkillsSection.tsx`, `SkillsSectionClient.tsx`.

The current horizontal bar chart must be replaced.

Required:

- Add kicker: `// capability matrix`.
- Replace the bar chart with an eye-pleasing stock-market-like multi-line graph.
- X-axis and Y-axis must be labeled.
  - X-axis: time or learning progression, e.g. `2021 → 2026`.
  - Y-axis: `Familiarity / Applied Depth`, not “mastery.”
- Do not claim mastery. Avoid labels like “Expert” as the main visual claim.
- Lines should represent categories:
  - AI/ML
  - Data Systems
  - Backend
  - Frontend
  - DevOps/Tools
  - Soft Skills or Communication
- Hovering a trajectory should:
  - Highlight that line.
  - Show tooltip with category, current direction, and related skills.
  - Dim unrelated lines.
- Below graph:
  - Keep skill category/list structure, but make it useful.
  - Category buttons must actually do something: filter, highlight chart line, update insight panel.
  - Each skill category has a unique interaction:
    - AI/ML: pulse/glow.
    - Backend: terminal cursor blink.
    - Frontend: shimmer sweep.
    - DevOps/Tools: deployment dots/trail.
    - Data Systems: animated tick bars.
    - Soft Skills: subtle bounce or wave.
- Add an “Insight” panel that updates with the selected category, e.g. “Currently trending toward: AI/data systems and retrieval workflows.”

## Education

Files: `EducationSection.tsx`, `EducationEntry.tsx`.

Do not use plain rectangles. Build the “life-form flowchart” idea.

Required:

- Add kicker: `// origins`.
- Three stages:
  - Top: College, University of Minnesota-Twin Cities, B.S. Computer Science, 2024-2028 expected.
  - Middle: High School.
  - Bottom: Middle School.
- Each stage should be represented by a floating organic shape, not a normal rectangle:
  - Middle school: most deformed amoeba-like sphere.
  - High school: less deformed, more formed.
  - College: almost perfect sphere, glowing and most stable.
- Shapes should feel alive:
  - Subtle animated blob border or SVG morph.
  - Dotted glowing line connects the shapes.
  - Light/pulse travels through the dotted connector from middle school to high school to college.
- Include readable text next to or inside each shape using dark backing where needed.
- Mobile: stack vertically, keep connectors short and readable.

## Certifications

Files: `CertificationsSection.tsx`.

Lovable’s credential cards were close. Keep the idea, but use this repo’s comet card style.

Required:

- Add kicker: `// credentials`.
- Use darker comet credential cards.
- Each card:
  - Issuer badge/icon.
  - Certification title.
  - Issuer/date.
  - Skill tags.
  - View Credential action.
  - Subtle holographic ring/corner accent.
- Cards should be compact, readable, and not just “moving cards.”

## Achievements & Awards

Files: `AchievementsSection.tsx`.

This section should require less content but still stand out.

Required:

- No section kicker if it looks cleaner.
- Make the entire achievements ledger/card float as a comet card in space.
- Use a clean ledger/timeline style:
  - Year.
  - Small icon.
  - Title.
  - Type chip.
  - One-line description.
  - Optional external link.
- Add a single glowing line/rail and subtle row hover.
- Keep it elegant and not bulky.

## Blog / What I Read or Do

Files: `BlogSection.tsx`, `BlogFeed.tsx`.

Required:

- Add kicker: `// uplink` or `// read log`.
- Keep the “What I Read or Do” idea, but improve the card surfaces.
- GitHub pinned card:
  - Keep the nice left violet rail.
  - Make it more premium and readable.
  - GitHub icon, short copy, Visit action on right.
  - Magnetic hover on Visit button if practical.
- Resource cards:
  - Darken cards.
  - Improve contrast.
  - Category chip, title, excerpt, date/read time, open icon.
  - Hover lift and border glow.
- Avoid the background sphere covering text.

## Contact

Files: `ContactSection.tsx`, `ContactPanel.tsx`.

Use Lovable’s contact alignment as inspiration, but preserve comet-card feel.

Required:

- Add kicker: `// uplink`.
- Heading should be cleaner:
  - `Let’s build something`
  - Subhead: `Internships, collaborations, or just to say hi.`
- Contact card:
  - Smaller and centered.
  - Comet card style.
  - Email centered and prominent.
  - Buttons centered below: Copy and Open Mail.
  - Social buttons below: GitHub, LinkedIn, Instagram, Email, Website if available.
  - Social buttons should pop out of the card as floating circular buttons.
- Remove cringe “Tired of chatting to my AI Twin?” language.

## Footer

Files: `Footer.tsx`.

The current footer must be replaced.

Required layout:

- Left: programmer glyph/emoji/icon. Prefer `</>` or a tasteful tiny developer symbol over a goofy emoji.
- Center: Back to top floating button.
- Right: `© 2026 Anant Gupta · building in public` or another short phrase.
- Remove the center sentence “Built in the dark. Shipped with intention.”
- Keep it short, clean, and aligned.
- Add subtle top border gradient.

## AI / Portfolio Lab

Files to replace or add around `SidebarToggle`, `AppSidebar`, `chat/*`.

This is the most important part of the portfolio. It should not be a paid chatbot.

Required:

- Remove OpenAI ChatKit UI and all user-facing chatbot language.
- Replace “Chat with Anant” / “AI Twin” with “Portfolio Lab” or “AI Lab.”
- Keep a bottom-right floating launcher button.
- Tooltip can say: `Ask the lab, not my sleep schedule.`
- The AI panel can be sidebar or hover board.
- It should feel like an interactive command center, not a chat box.

Portfolio Lab features:

- Modes:
  - Recruiter: role-fit proof packs, skills, experience evidence.
  - Builder: project breakdowns, architecture notes.
  - Research: AI/data systems timeline and learning trajectory.
  - Skeptic: claim checker with source/evidence cards.
- Suggested chips/questions.
- Static/local deterministic answers for v1.
- Evidence cards that link to sections.
- Mini skill/project graph.
- “Generate proof pack” button that creates a client-side text summary.
- No paid API calls for visitor usage.
- If the current ChatKit package remains installed temporarily, it should not be used in the visible UI.

## Floating Dock / Bottom UI

There is a bottom-left floating `N` style dock/button in screenshots. Do not leave it random.

- Either integrate it into the design as a small command/dock button, or remove/hide it if it has no purpose.
- Bottom-right AI launcher must be visually dominant but not obnoxious.
- Ensure dock, AI launcher, and footer do not overlap on mobile.

## Data and Content

Use real Anant content already present in Sanity/Data:

- Anant Gupta
- AI & Data Systems Engineer / Full-Stack Developer
- University of Minnesota-Twin Cities
- Minneapolis, MN
- BOOM research assistant
- NSEdu web development internship
- CSE Student Ambassador
- Techlit co-founder
- Skills: Rust, Python, React, Next.js, TypeScript, Tailwind, LLM APIs, prompt engineering, data pipelines, Git, Linux, Docker, etc.
- Email: use existing Sanity profile email.
- GitHub/LinkedIn from existing profile data.

Do not use Alex Morgan or fake Lovable data.

## Accessibility and Responsiveness

- All interactive controls need accessible names.
- Keyboard nav must work for carousel, AI Lab, close buttons, and nav.
- Respect reduced motion.
- No text overlap at mobile, 1280px desktop, or wide desktop.
- Maintain readable contrast over the background.
- Avoid layout shifts on hover.

## Verification

After implementation:

- Run `pnpm typecheck`.
- Run `pnpm build`.
- Search and remove old visible copy:
  - `AI Twin`
  - `Chat with Anant`
  - `ChatKit`
  - `Alex Morgan`
- Test:
  - Hero layout.
  - About telemetry.
  - Experience timeline alignment.
  - Projects carousel transitions.
  - Skills graph hover/filter.
  - Education organic flowchart.
  - Certifications cards.
  - Achievements ledger.
  - Blog cards.
  - Contact copy/buttons/socials.
  - Footer layout.
  - AI Lab open/close and static interactions.
  - Mobile and desktop.

```
## Data
### BOOM
1. *Data Pipeline Portfolio Bullet*
	- Portfolio Bullet: **Data Pipeline & Storage Design (MongoDB + Kafka)**: Designed and worked with a document-oriented storage layer for astronomical alert data, where query patterns drove schema decisions rather than code structure. Implemented filter evaluation on enriched records using cross-match data, derived quantities, and classifier outputs — demonstrating that post-enrichment filtering is significantly more powerful than raw-data filtering. 
		**Stack**: MongoDB, Kafka, Rust (serde/BSON), Docker 
2. *Quantified Impact*
	- Worked with 5+ entity types (alerts, objects, images, filters, catalogs) in a document database
	- Filter versioning enabled reproducible scientific results across pipeline changes
	- Architecture pattern transfers directly to feature stores and ML experiment tracking
## Git
- `git config` - Configure Git
- `git init` - Initialize Git repository
- `git status` - Check the status of a Git repository
- `git add` - Track files
- `git commit` - Commit tracked files
- `git push` - Upload files
- `git pull` - Download files
### Repository: Project
```bash
echo "# projects" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/gupta-builds/projects.git
git push -u origin main
```
…or push an existing repository from the command line:
```bash
git remote add origin https://github.com/gupta-builds/projects.git
git branch -M main
git push -u origin main
```
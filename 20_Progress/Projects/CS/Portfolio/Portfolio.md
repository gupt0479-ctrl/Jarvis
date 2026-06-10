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
### Sanity fixes
Here is a detailed analysis of what exactly does sanity not render on my portfolio:
1. Hero & About: a. Availability status : Available for hire , Open to opportunities , Not looking. b. Years Of Experience : 2 , Stats : Small KPI chips (e.g., “10+ projects”): Side Quests : 3, Client Satisfaction : 100% , Years Experience : 2+ , Technologies Mastered : 30+. a. and b. are the things that are not ebing rendered. The image pasted is below about me which is not in sanity(probably hardcoded).
2. Experience: Employment Type, Description : Long-form responsibilities and impact, Achievements : Quantifiable outcomes (numbers preferred), Company Logo, Company Website. Order works. Error message shown in image.
3. Projects: Slug(no idea what that is), Tagline : Short one-liner. Enitrely broken actually.
4. Skills: Couldn't figure out what was broken. Seems like everything is. The graph is not there anymore. The skills division is also different than what is currectly there.
5. Education: Description, Achievements - (not needed), Logo(needed)
6. Certifications: Issue Date : 2022-11-10 (wrote as month and year - works perfectly), Expiry Date (Leave blank if certification doesn't expire ): 2025-11-10 , Credential ID (Certificate ID or badge number ): TF-DEV-24680-2022 , Credential URL (Link to verify the certification ): https://tensorflow.org/certificate , Badge/Logo : Upload certification badge or logo(not needed)
7. Achievements: Issuer, Date(as year - perfect), Url(not sure)
8. Blog/What I read: Github(hardcoded but works), Slug(do not know what that is), Tags(not needed), Published At(perfect the way it is)
9. Footer & contact: Not there on sanity(works i guess)
10. Site Settings: Not rendered anywhere, what does it even do?
Can you figure out what exactly is not being rendered?
### UI Enhancement
You are working on a portfolio as a front end engineer. The ui right now is basic and could be improved by a lot. I have provided you with images from the localhost currently being run and what the website looks like. Analyze each and every single image pixel by pixel and in detail. You have access to all the codes and directory markdown files. Analyze each and every single thing about this website and codebase. Here are the details of the things that i want to be make better about the ui:
1. The buttons on the hero section should be floating in space. The buttons are the github, linkedin, email, view project, view experience, contact and the image being rendered(that's also a button). Should appear like they are in space, Not only on hovering but at all times. All the buttons across my portfolio should appear as if they are in space, should have the current hover effect as well. 
2. Just below the about me section i want something cool to be read in 4 columns like seen now. But i want this to stand out. The current about me just looks too bland. Esepcially the line after content and those 4 headings. Make something better show up just after the content in about me.

3. The comet card appears to hover all over the portfolio but in experiences it might just appear to be too big for the screen. It looks weird, all the comet cards background colors were changed to be transparent because they were too shiny. Now they are just completely glass. I want something translucent, i want something that does not outshine the background of the portfolio. Make the color appear more for all the cards. The experience section timeline line could be more better, the line looks weird and the dots are not exactly aligned. Make the line appear almost eye pleasing while scrolling through the experience section.

4. The projects card is one of the most ugliest things i have seen here. the butons appear just on top of the card making it look compact. The slider looks so shitty. I want these projects on the left and right to appear like they are in space. When clicked on the left or ride button they come to the center with a smooth transition effect. I want these two left and right cards to wandering at the same opacity they are at. Maybe the background could also be interactive over here with getting the card to the center, some sort of a string pulling it towards the center upon clicking left or right.

5. The skills and expertise graph just looks really shitty. I want it to appear as a trading stock graph sort of with multiple trajectories as lines such as ai, devops etc. We can see that the user is progressing towards what more. Make this graph appear much more aesthetic and appealing to the eyes. The buttons below the skills section are complete garbage, they look so shit and they do not do anything. Nothing on hovering or clicking. I want each button on the skills section to do something. I want each skills section to have something unique in them. Each of them do something unique upon clicking or hovering.

6. I want the education sections to be like a flowchart. There will be three parts to this flowchat: Middle school, high school and college. I want the top to be college obviously but this appear as this really cool flowchat that actually floats(pun). I want this also to appear as if it is in space.

7. The certification cards are comet cards and could be darker like mentioned above, i want these to also be something cool than just a moving card.

8. Achievements & Awards is a section that i want to put least efforts and want it to stand out. Just a basic line next to it and some cool text. Currently looks completely garbage, make it fit the theme above.

9. what i read or do also use comet cards. I need you to darken each card, make it more better. The github color on the left looks really nice and the unique hover effect is good. I want it to appear more ui appealing to user. Then comes the end contact card. I want the email to appear int the center and make the card a little smaller. I want more buttons on there like instagram, etc.

10. Footer is the uggliest thing i have seen in my entire life. I want you to remove the center context written and change it to something less cringe and short. Right next to those workds should be back on top with the button. The year should appear on the right most side with something else cool next to it. On the left most side should be an emoji for a programmer.
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

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
You are working on a portfolio as a professional frontend engineer specialising in three.js and moving components. The ui right now is basic and could be improved by a lot. I have provided you with images from the localhost currently being run and what the website looks like. Analyze each and every single image pixel by pixel and in detail. You have access to all the codes and directory markdown files. Analyze each and every single thing about this website and codebase. Here are the details of the things that i want to be make better about the ui:
1. The buttons on the hero section should be floating in space. The buttons are the github, linkedin, email, view project, view experience, contact and the image being rendered(that's also a button). Should appear like they are in space, Not only on hovering but at all times. All the buttons across my portfolio should appear as if they are in space, should have the current hover effect as well. The image has these boxes that need to be removed: "next.js", "ai/ml" and the online bar that renders above the image. All of these things should be removed. Even this line: "NEXT.JS • SANITY • 3D • TYPESCRIPT" just below the "// hi i'm" should be removed. Just the comment works and make sure that the padding does not look weird after removing these things. There should be no extra space left out anywhere.
2. About me: The hardcoded terminal box displayed in the image should be above the about me section and just below the hero page. It should be in between the hero and the about me. It should be in the center of the page and let's update what the terminal says: "~/anant/da_portfolio
   $ whoami anant.gupta — ai/ml engineer(or something better) 
   $ stack --top rust · typescript · python · postgres · agents
   $ status shipping → agentic work · research · ui/ux"
3. The boxes in the about me section and the terminal should have the comet card effect as well. They should also appear to be in space. The terminal should have a very subtle moving around effect to a broad range because it is going to be above the about me now. It can move around a bit - half of the hero section but in the center of the screen. This should be a floating terminal that is in space basically. The "$ whoami, $ ..." should have a subtle glow effect. Three buttons that act as - 'close, minimize and expand' should have those signs on the red, yellow and green of the terminal. 

4. Experience: The experience section timeline line(on the left) could be more better, the line looks weird, it glows at some parts and the transition between the glowing and not glowing is not smooth at all. The line should also appear to be in space, it's completely static right now. Just wiggle around slightly in it's space. Make the line appear almost eye pleasing while scrolling through the experience section.
5. Cards: The "contract, internship, freelance, etc." should render next to the location. The experience description from sanity is not being rendered currently. The achievements are in green which looks so weird and shitty. Match the color with the theme of my website and the card color. I want the description to show up only when the user clicks on the experience. There should be a very subtle drop down button that's clickable on each card as well. This button will be on the bottom right of each card. very subtle and almost not visible to the user. The entire experience card should not occupy the entire screen though. The drop down should be small. 
6. The skills appear in different colors and I like that but these skill colors should be uniform throughout the website. Sanity has this feature of all the skills listed already and they are just being mapped into the experience section - the color and skill name are the only two things that render on the experience card. These skills might need to be set up properly on sanity but make sure that these are not hard coded. Everything in the experience cards should be rendered from sanity. 

7. Projects: Card is one of the most ugliest things i have seen here. The header for projects is currently on the left with the "// build log" over it. This should be rendered in the center of the screen just like every other section. Event the description renders in between the screen. The slider looks so shitty, no subtle effect at all. The main card(center) should have a comet card effect and wiggle around in it's area. This card will also appear like it's in space, almost no gravity. The space that it wiggles around should be limited to it's padding. in the These projects on the left and right to appear like they are in space as well, wiggle around in their own padding. The cards on the left and right should only have a comet card effect when they appear in the center. Right now they are translucent, prefer it that way. Should just move around in it's own area appearing to be in space. When clicked on the left or ride button they come to the center with a smooth transition effect. I want these two left and right cards to wandering at the same opacity they are at. Maybe the background could also be interactive over here with getting the card to the center, some sort of a string pulling it towards the center upon clicking left or right.
8. Content: Right now we have filler data for the content on the website. I have way too many projects working right now but honestly nothing deployed except the hackathon websites. They are also broken to a level. I do not want to spend my time fixing those links. How can we prove our skills over here? Let's write the description and the content for the website in a manner that it showcases our skills. We already have orby saying that these websites might not be working so go visit the github. These projects are luckily on github already, so they should just link to the correct github link. We need to lay out the content for each and every single project that we have in our vault jarvis in a professional manner. Write the content onto sanity and I will optimize it further. Just write content like a professional on sanity for now.
9. Skills: Same as the experience card. Only the color and the name should appear in the projects section. This color and name should come from the sanity section: "Skills". which is a lower component below projects. These skills will be written in detail below but I want everything on the projects card to be rendered from sanity so it is easily editable. Everything that is necessary for the sanity backend should be configured correctly onto the website. This is not even close to what is on the sanity backend. 
10. Hover: On hover all the cards move down, that needs to be changed now because the cards on the left and right are going to be wiggling around in their own space. Both of these cards should continue to wiggle around when there is more content visible upon hovering. The project card should not be extremely large with the drop down: links to github and the live website. Just above that it will have the detailed summary of what the website is. This will be decided only after the sanity fixes. 

11. Skills: The skills and expertise graph just looks really shitty. It does not even redner anymore on the website. I want it to appear as a trading stock graph sort of with multiple trajectories as lines such as ai, devops etc. This graph should go up and down basically and each of the lines are not the same ups and downs. Graph should be rendered on the left and the detailed skills on the right. the buttons for each skill have been listed and it should appear exactly like that. We can see that the user is progressing towards the skills that are intermediate or beginner. Make this graph appear much more aesthetic and appealing to the eyes. All these skills should be listed in sanity and this should be concrete. Very concrete. We are going to use the skill color and name to be rendered all across the website.
12. Buttons: The buttons below the skills section are complete garbage, they look so shit and they do not do anything. Nothing on hovering or clicking. I want each button on the skills section to do something. I want each skills section to have something unique in them. Each of them do something unique upon clicking or hovering. Firstly, these buttons will be on the right side of the graph now. All the skills are being rendered right now which is a really long list. On automatic the most high level skill category renders and the user is able to pick which skill category he wants to see on top of all the skills listed like right now but on the right side. The skills category have some features on hovering right now which need to be enhanced completely. These skill category buttons should also be in space wiggling around and have the comet card effect(only the skill categories).
13. Listed Skills: Each skill category has a description written which should only appear when clicked on the skill category. Then below the description comes the skills which say begineer, intermediate or advanced. these skill boxes are taking too much space right now and need to shrink to fit the size of the skills section. Adjust the sizes as desired if still taking too much space, the skill mastery should appear only on hovering with the skill effect that is enabled per skill.
14. Effects: Each and every skill should have an effect that is not the same as the skill category, there should be different effects for every 7 skills. So, there are going to 7 effects for the skills listed. No count for the skills category, these should be independent of each other and the skill effects. There should be a lot of unique factor here in this category. Really think about these effects. Everything is unique here. 

15. Education: I want the education cards to be like a flowchart. The education header does not render in center of the screen, it's on the left with the comment on top and the desription it has. All of it should be in the center of the page. There will be three parts to this flowchart: Middle school, high school and college. Which is already rendering correctly. I want this also to appear as if it is in space, wiggle around it's own area. The image here was that the surface/perimeter of the shape, will be acting like an amoeba to a fully formed circle. Middle school being the most deformed amoeba to high school still being very destructed perimeter wise. To, college being a perfect circle. At the center right now are images of the school's that I have attended that's good but these images do not look good right now, adjust the perimeter's of these images to the specific education category that they belong to. 
16. Connection: Right now they are being connected by these glowing dotted lines, exactly correct. But all the education categories appear to be in a straight line, not wobbling or moving around at all. What I mean by a flow chat is that these not only wobble around. The high school should be more to the left and these dots are still connecting, as they wobble around these dotted lines seems to be stretching and returning some sort of a living pulse upwards to the college category(glowing already works but downwards). This living pulse should start from middle school which is going to be more to the right now, really like a flowchart here. We watch the dotted line stretch, the pulse reach the middle school on the right side and the dotted line starts again from high school to college in the same manner. The college is not supposed to be exactly in the center cause it's still a flow chat but almost appears to be in the centre.
17. Cards: Each education category has it's card which should have a comet card effect and moves around with the shape of the category. These cards are rendering perfectly from sanity and need no update. Just the ui updates for each and every single category. Comet card, move around with the shape and appears to be in space. 

18. Certification: The certification header should be rendered in the center of the screen along with the comment on top of it and the description that it has. These are rendering perfectly from sanity right now but are dummy certifications. The skills that these certifications have should be rendered from the skills from sanity and should only display the color and the name of the skill. Rest everything about the credentials should be an out link that takes the user to the specified website that i got the certification from or my certificate(if i have one). 
19. Achievements & Awards: Subsection under certification now. This is a section that i want to put least efforts and want it to stand out. Just a basic line next to it and some cool text. Currently looks completely garbage, make it fit the theme above. The line that is currently being rendered on the box should be outside the box and should be exactly like the experience section timeline. there are years mentioned but should be closer to the text once the timeline is separated from the box. 

20. What i read or do: also use comet cards. The github button wobbles around right now and the unique hover effect(comet card?) was good, the bottom of the card used to lift up a little and had this unique feature. Let's keep that with this wobble effect, I want it to appear more ui appealing to user. Then comes the contact card effect on each of the small cards that are external links right now. Each of these cards should render directly from sanity, i think that they already do. Just the comet card effect and a more translucent background for these small cards would look great. The github stays the same background color, only the small cards below github should be translucent. 
21. Contact: I love the buttons and everything about it but just the card seems a little meh to me. Making it translucent might not be good enough because we want the user to read the text and buttons clearly. The background is too good and shiny right now which we want to display. How can we make this better? Think about this and get back to me. I honestly don't know how this can be better
22. Footer: The year should appear on the right most side with something else cool next to it(building in public). On the left most side should be an emoji for a programmer(terminal?). both of these things are already there on the footer but just not on extreme edges. They should be at extreme lefts and rights since it's a footer. The "back to top" button is also not in the center of the screen. Make sure that it's in the center, also has the comet card effect. The text on the footer is barely seen. It shouldn't exactly glow but should be seen normally as well. There is too much space for a footer, we don't need that much space for the footer, let's reduce the size of the footer to only how much is needed. The line for the footer should be very subtle, the background of the footer should be translucent showing that the background can also reach the footer.

23. Orby: We will talk about this in detail in the next prompt.
24. Dark mode toggle: Not set yet, no idea what light mode of this website would look like. 
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

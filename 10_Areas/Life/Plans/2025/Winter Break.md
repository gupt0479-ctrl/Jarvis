---
type: brainstorm
status: sprout
created: 2025-12-15
related_progress:
  - "[[Plan]]"
  - "[[Portfolio]]"
  - "[[Learning Tracker tool]]"
  - "[[Cleaning Laptop]]"
  - "[[Making Break Meaningful 1.pdf]]"
tags:
  - brainstorm
  - evergreen
---
# The Plan
## Week 0 (Dec 20-21): Setting up
1. **Create a “Sprint HQ” in Obsidian**
	- Project V1 needs a **dedicated “Sprint HQ” dashboard** that points to repo deliverables + weekly checklists + metrics.
	- Make folders exactly as in your structure
	- Create templates (Daily/Meeting/Decision/Code Snippet)
	- Create `00_Dashboard.md` with links
2. **Create the repo skeleton**
	- `/docs/READTHIS-FIRST.md` (your instructions)
	- `/internships/target-list.csv` + `/internships/applications-tracker.csv`
3. **Decide the product scope in 10 minutes**  
    Write a 6-line “MVP spec”(*Minimum Viable Product Specification*):
    - Who user is
	- What they can do (3–5 actions)
	- What success looks like (demo script)
	- What’s cut
4. **Set up Todoist**  
    Projects:
	- V1 Product
	- V1 Interviews
	- V1 Internships
	- V1 Portfolio
	- V1 Obsidian  
    Labels: `@deepwork` `@admin` `@apply` `@practice`  
    Recurring habits (small):
	- Guitar 15m (3x/week)
	- Gym 45m (4x/week)
	- Meal prep (Sun). 
	This keeps “Winter Has Come” real, but not chaotic.
## Week 1 (Dec 22–28): System + Decisions + Skeletons
**Goal:** finalize scope, set up the OS, and get both repos running (lightly).
**Decide**:
- Portfolio approach: **Simple Next.js** vs **AI Twin template**
- Product stack: Clerk vs NextAuth, Neon vs Supabase/Railway
- AI scope: weekly recap generator vs none
1. *Product (Learning Tracker)*: **Watch/Extract from video:** project setup + Clerk auth + middleware + DB connection patterns. [YouTube](https://www.youtube.com/watch?v=rdaSPdCkoFQ&utm_source=chatgpt.com)
	- *Tools used*: Next.js, TS, Tailwind, Clerk, Neon, Drizzle, GitHub Issues/Board
	- Decide MVP: 3 core entities + 1 dashboard page
	- Choose stack: Next.js + TS + Postgres + Prisma + Auth (Clerk or NextAuth)
	- Scaffold repo + run locally: Next.js app, Apollo server, Prisma schema, seed script.
	- **Architecture brief**: ERD (User, Goal, KeyResult, CheckIn), `GraphQL` schema draft, page map, auth flow, LAN Graph(can be simple markdown diagram).
	- **Role Brief #1–#2** (Frontend, Backend): “day-to-day, tools, interview themes.”
	- Auth decision made (Clerk/Prisma/NextAuth) + basic auth wired
2. *Portfolio*:
	- Don’t do AI Twin repo yet.
	- Create a **simple Next.js portfolio** with:
	    - home/about
	    - projects section (cards)
	    - resume link
	    - contact
	- Add “Learning Tracker (in progress)” card + link to repo
3. *Obsidian*:
	- Create **Project V1 dashboard** + daily note template that includes:
	    - shipped / blockers / decision
	    - interview sessions count
	    - applications count
	- Templates created (Daily / Meeting / Decision / Code Snippet)
	- `00_Dashboard.md` with links to: Roadmap, Backlog, Trackers, This Week Plan
4. *Mentorship*:
	- Prepare “Week 1 one-pager”:    
	    - MVP spec
	    - ERD
	    - tech choices
	    - what you’re cutting
	- *Internship pipeline deliverables*:
		- `target-list.csv` created with **at least 30 roles** (Tier A/B/C)
		- `applications-tracker.csv` created (empty but ready)
		- Outreach list of 10 people (alumni/mentor/network).
**Done when:** you can run Learning Tracker locally and your portfolio exists online (even basic). Also, your vault/trackers are live.
- *Learning tracker*: login works + DB tables exist + can create a session (even via a simple form).
## Week 2 (Dec 29–Jan 4): Backend MVP + Auth
**Goal:** real functionality exists.
1. *Product*: **Watch/Extract:** how they structure CRUD APIs + relational queries + enrollment/progress logic. [YouTube](https://www.youtube.com/watch?v=rdaSPdCkoFQ&utm_source=chatgpt.com).
	- *Tools used*: ORM queries, Zod validation, basic dashboard UI
	- Where to add caching first (client, API response, or DB query)?
	- **API MVP**: Create/Read/Update for Goal, KeyResult, CheckIn; pagination; input validation.
	- **Auth working**: sign-up/login, protected routes on API and app.
	- Postgres + Prisma schema done
	- **Seed data + Postman/Thunder tests**.
	- CRUD working for core flow:
	    - create goal / topic / session
	    - list + detail views (API ready)
	- **Role Brief #3** (Full-stack) + short note: “what breaks first at 10× traffic?”
2. *Interview + pipeline*:
	- 5 technical sessions logged
	- 10–12 targeted apps submitted
	- 5 outreaches
**Done when:** a logged-in user can create/read/update/delete real data in the DB.
## Week 3 (Jan 5–11): Frontend MVP + Charts
**Goal:** usable UI, demoable.
1. *Product*: **Watch/Extract:** dashboard layout patterns + progress bars/cards. [YouTube](https://www.youtube.com/watch?v=rdaSPdCkoFQ&utm_source=chatgpt.com)
	- *Tools used*: OpenAI API, pgvector, retrieval pipeline
	- Core screens: Goals list, Goal detail (KR table), weekly CheckIn form, simple **progress chart** (Recharts).
	    - dashboard
	    - list/detail
	    - create/edit
	- 1 chart (weekly minutes or streak)
	- **State & data**: TanStack Query on top of GraphQL; optimistic updates for check-ins.
	- validation + loading/error states
	- **Role Brief #4–#5** (DevOps, Data).
2. *Portfolio*:
	- **Portfolio page deployed**: hero + project card + live link placeholder.
	- Project card for this app (even if “in progress”)
	- Begin write-up skeleton: what/why/how + screenshots placeholder
3. *Mentorship*:
	- Apply **10–12 roles**
	- Outreach **5 more**
	- 1 system design mini + log it
	- Ask Ahnaf for UX + scope cuts:
	    - “What looks most internship-ready?”
	    - “What’s unnecessary?”
**Done when:** you can demo in 2 minutes with a clean story.
## Week 4 (Jan 12–18): Deploy + Runbook + Tiny AI
**Goal:** credibility (deployment + reliability).
1. *Product*: **Watch/Extract:** deployment workflow + environment handling. [YouTube](https://www.youtube.com/watch?v=rdaSPdCkoFQ&utm_source=chatgpt.com)
	- *Tools used*: Vercel, GitHub Actions (lint/typecheck/build), runbook
	- **Deploy v0** (Vercel + Railway or AWS EB), **short runbook** (how to redeploy, env vars).
	- **Tests + CI**: Jest/RTL smoke tests; GitHub Actions (lint, test, build): lint + typecheck + build
	- Runbook.md (redeploy, env vars, db reset)
	- Add tiny AI micro-feature:
		- **“Weekly recap generator”**:
			- Input: last 7 days of session notes
			- Output: summary + “next 3 actions”
			- Store the recap in DB + display on dashboard
2. *Portfolio*:
	- Add project write-up:
	    - architecture diagram
	    - 3 key decisions
	    - what you’d do next
3. *Career*: Pre-launch checklist review (what would he add for a “manager-ready” demo?).
	- **Internship assets**: résumé v2, LinkedIn refreshed, target list (Tier A/B/C) with 20 apps ready.
	- Mock interview #1
	- 15–20 apps push week
**Done when:** live URL + README + runbook + CI badge. You can demo without panicking.
## Week 5 (Jan 19–25): Polish + Resume bullets + Optional AI Twin upgrade
**Goal:** package it professionally.
1. *Product*:
	- Bug fixes + polish pass: UX, empty states, bug fixes
	- demo video (3–5 min)
	- resume bullets written
	- Write-up finished: architecture diagram + 3 decisions + what’s next
	- monitoring basics (logs, error handling)
2. *Portfolio (choose ONE)*:
	- Option A (recommended): keep simple portfolio + add RAG chat widget:
		- resume PDF text and project READMEs
	    - 2–3 writeups (Boom, Turbo Telescope, Learning Tracker)
		- You can implement with a simple “/api/chat” route + embeddings store.
	- Option B (only if you have time): migrate to AI Twin repo _after_ shipping app: 
		- Treat it as a theme/template: replace content + keep AI limited to RAG.
		- Don’t customize animations, dark mode, dock, etc. until everything else ships.
3. *Career*:
	- Mock interview #2 (technical)
	- follow-ups + coffee chats
	**Done when:** you can show this to a recruiter and it looks like an engineer built it.
## Technical plan (how we build it like engineers)
### Courses
1. BECOME A CERTIFIED EXPERT IN SOMETHING UNIQUE: Certifications aren't just resume fillers—they're proof of real skills.
	- Examples: CPR/First Aid certified (Red Cross)
		- Lifeguard certification
		- Google certifications (data analytics, project management, digital marketing)
		- Coding certifications (freeCodeCamp, Coursera, HarvardX CS50)
		- Language proficiency (DELE for Spanish, HSK for Chinese, JLPT for Japanese)
		- Adobe Certified Professional (Photoshop, Lightroom)
		- EMT certification (check age requirements in your state)
		- Referee or umpire certification for sports you play
		- Food handler's permit

# Obsidian Formatting
### Hotkeys (recommended):
- `Ctrl + Alt + I` → create new Input note from template
- `Ctrl + Alt + T` → create new Thought note from template
- `Ctrl + Alt + P` → create new Project note from template
### The USE
Structure alone isn’t productivity. The power comes from **daily flow**. Here’s the workflow that makes Obsidian feel unfair:
1. Daily loop (10 minutes):
	1. Capture into **00_Inbox** (QuickAdd)
	2. Work from your **Dashboard**
	3. End of day: process 3–10 inbox notes (move + link + tag lightly)
2. Weekly loop (30 minutes):
	- Clear Inbox
	- Review Active Projects
	- Promote any good ideas into Evergreen notes
	- Archive dead stuff
That’s literally the difference between “pretty vault” and “second brain”.
## Order
**Titles should be claims**  
Instead of: `Byte Ordering`  
Do: `Little-endian stores the least-significant byte at the lowest address`
This makes search + linking + understanding way sharper.
**3) Every evergreen note must contain at least one of:**
- A “Why it matters” section
- A worked example
- A self-check question  
    That’s what turns it into a _memory tool_ instead of storage.
**4) Add a “review loop” property**  
For evergreen notes:
- `status: seed/sprout/tree`
- `review_after: 2026-01-15`
- `source: [[Week - 3]]` (or textbook page)
Then make a dashboard:
- “Notes to review this week” (filter by `review_after <= date(today)`)
## Progress like him (dynamic)
Make area notes as “control panels”.
Example: `20_Areas/UMN/CSCI 2021/CSCI 2021 Area.md`
```md
type: area
tags: [area]

# CSCI 2021

## Active projects
- [[CSCI 2021 - Project 4]]
- [[CSCI 2021 - Final Prep]]

## Key resources
- [[Linked List]]
- [[Malloc and Free]]
- [[Two’s Complement Encodings]]

## Notes to self
- 
```
## Resources + MOCs like him (Maps of Content)
This is where you build “smarts”.
Create MOCs like:
- `30_Resources/CS/CS MOC`
- `30_Resources/PKM/PKM MOC`
- `30_Resources/Career/Career MOC`
Example MOC:
```
type: moc
tags: [moc]

# Personal Knowledge Management (MOC)

## Practices
- [[PARA]]
- [[CODE]]
- [[Progressive Summarization]]

## Tools
- [[Obsidian Workflow]]
- [[Templates]]
```
His “query for unlinked but referencing notes” is a Dataview trick — optional. The important part is: **MOCs are launchpads.**
## Evergreen + Greenhouse (his “forest” system)
Make one note: `90_System/Dashboards/Greenhouse.md`
Track only what matters:
- `#seed` = you created it but it’s empty
- `#sprout` = has structure + needs tightening
- `#tree` = solid + linked to other notes
If you have Dataview, you can list them automatically. If not, keep 10–30 max, curated. 

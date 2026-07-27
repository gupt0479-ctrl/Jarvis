---
type: input
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - summary
notes:
  - "[[Tracker]]"
source_url: 60_Claude/05_Clippings/PDFs/outreach-manual.pdf
source_note: "[[outreach-manual.pdf]]"
input_kind: pdf
track: career
---
# Outreach Automation Manual — Summary
**Source:** `60_Claude/05_Clippings/PDFs/outreach-manual.pdf`
**Ingested:** 2026-07-03
**Pages:** 6
## Source
A setup-and-usage manual from **The AGI Guide** (@the.agi.guide) for a **Claude skill file** that automates job outreach: given a resume and a city, it finds hiring managers on LinkedIn, resolves their work emails via **Apify**, writes 10 personalized cold emails, and saves them as **Gmail drafts**.
## Key Claims
- The pipeline is **direct access to hiring managers** — "no job boards, no applications"; the pitch is bypassing the application funnel entirely
- The whole system is one **SKILL.md file** plus two MCP connectors (**Apify** + **Gmail**) — no custom code
- Email discovery is **pattern inference, not hacking**: Apify cross-references public naming patterns (firstname.lastname@company.com) and validates whether a live mail server exists — the same method as **Apollo**, **Hunter.io**, and **ZoomInfo**
- Claude **only saves drafts, never sends** — human review is a hard step in the loop
- Confidence-tiered output: **valid > risky > skip**, filtered to the 10 highest-confidence contacts
- Designed as a **daily habit**: fresh profiles each run, never reusing LinkedIn URLs or prior email copy
- Real constraint: the Apify actor **doesn't run on the free plan** via API — the $49/mo plan is required for automated runs
## Full Content
### What Is This?
==Outreach Automation is a Claude skill file that runs a fully automated job outreach pipeline: resume + city in, 10 personalized cold-email Gmail drafts to real hiring managers out.==
The skill file is distributed as a Google Docs download (link in the raw PDF); it must be downloaded as an `.md` file.
### What You Need Before Starting
- An **Apify** account
- Apify connected to Claude as an **MCP connector**
- **Gmail** connected to Claude as an MCP connector
- Your **resume** (PDF or pasted text)
### Step 1 — Set Up Apify
1. **Create the account** at apify.com (free signup)
2. **Get the API key**: Settings → API & Integrations → copy the Personal API token (`apify_api_XXXXX`)
### Step 2 — Connect Apify to Claude
==Two connection paths exist: claude.ai Integrations for the easy path, Claude Code /mcp for power users.==
1. **Option A — claude.ai Integrations (easiest)**: Settings → Integrations → find Apify → Connect → paste token → Save
2. **Option B — Claude Code / Cowork**: `npm install -g @anthropic-ai/claude-code` → run `claude` → `/mcp` → Add new connector → Apify → paste token
> [!NOTE] Cowork is Anthropic's desktop tool for non-developers — there it's Settings → Connectors → Add Connector → Apify.
### Step 3 — Connect Gmail to Claude
claude.ai → Settings → Integrations → Gmail → Connect → authorize the Google screen.
> [!NOTE] Claude only saves drafts. It never sends emails on its own — you always review and send manually.
### Step 4 — Load the Skill File
1. **claude.ai Projects**: new Project → Project Settings → Knowledge → Add file → upload SKILL.md → every chat in the project has the skill; say "run outreach"
2. **Claude Code or Cowork**: save SKILL.md locally, reference its path or paste contents, say "run outreach"
### Step 5 — Run the Pipeline
One message: **"Run outreach"**. Claude confirms four inputs: city/metro, target job fields (marketing, AI, content, growth, …), resume, and email signature (name, brand, email, LinkedIn). Then it runs web search → LinkedIn scrape → email extraction → email writing → Gmail save, ending with a summary table of all 10 contacts with emails and confidence levels.
### What Happens Under the Hood
==The pipeline is an eight-step chain: search → collect 15+ LinkedIn URLs → Apify Profile Scraper → email-pattern cross-reference → filter to 10 highest-confidence → write personalized emails → save Gmail drafts → summary table.==
1. Searches the web for LinkedIn profiles of hiring managers in your city and field
2. Collects **15+ LinkedIn profile URLs** from public search results
3. Feeds URLs to **Apify's LinkedIn Profile Scraper**
4. Apify cross-references each profile against **public email pattern databases**
5. Claude filters to the **10 highest-confidence** emails (valid > risky > skip)
6. Writes a **unique personalized cold email** per person from your resume + their LinkedIn data
7. Saves all 10 as **Gmail drafts** with real addresses pre-filled
8. Delivers the summary table (contact, email, confidence)
> [!NOTE] Apify does not hack into anything — it infers addresses from public naming patterns and validates the mail server. Same method as Apollo, Hunter.io, ZoomInfo.
### Understanding Email Confidence Levels
| Level | What it means | What to do |
| --- | --- | --- |
| High ✅ | Verified deliverable email | Send first — highest delivery chance |
| Medium ⚠ | Valid mail server, pattern inferred | Send after the high-confidence batch |
### Running It Daily
==Each daily run targets fresh profiles — Claude never reuses LinkedIn URLs or copies previous emails.==
Daily loop: open the project → "run outreach" → confirm targets if changed → ~2 minutes → open Gmail drafts → review each, adjust, send.
### Troubleshooting
1. **"Users on the free Apify plan can run the actor through the UI only"** — free plan; the automated path needs the **$49/mo** plan
2. **"This actor requires permissions approval"** — click the approval link, approve, reply "done"
3. **Fewer than 10 drafts** — "I only got X — fill the rest" triggers another search batch
4. **A Gmail draft didn't save** — Claude prints the full email text; paste manually
> [!WARNING] The $49/mo Apify requirement is buried in Troubleshooting, not the setup steps — the "free account" in Step 1 does not actually run this pipeline via API.
## Why It Matters
Internship outreach is a weekly cadence in [[Weekly Operating System]] and the pipeline feeds [[Tracker]] directly — this is a concrete mechanism for it, not another "network more" platitude. The skill-file + MCP-connector shape is also the same architecture as the Jarvis skills, so adapting it (swap Gmail drafts for tracker rows) is a realistic weekend project. The cost gate matters: at $49/mo the manual variant (search + pattern-guess by hand, Claude writes the emails) may be the student-budget version.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/outreach-manual.pdf`
- [[Tracker]] — the internship tracker these contacts would land in
- [[Weekly Operating System]] — where the weekly outreach slot lives
- Cold-email skill for Jarvis `(to create)` — adaptation of this pipeline without Apify
## Open Questions
- [ ] Is the $49/mo Apify plan worth it vs. hand-searching 10 profiles and letting Claude write the emails from the same inputs?
- [ ] Does the referenced SKILL.md (Google Docs link) still exist, and what do its actual prompts look like?
- [ ] Legal/ToS check: LinkedIn scraping via Apify against a student account — any risk to the LinkedIn profile itself?
## Flashcards
#cards/career
How does the outreach pipeline find email addresses?::It infers them from **public naming patterns** (e.g. firstname.lastname@company.com) via Apify, then validates whether a live mail server exists — the same method as Apollo/Hunter.io/ZoomInfo.
What is the human-in-the-loop safety in the outreach pipeline?::Claude **only saves Gmail drafts** — it never sends; every email is reviewed and sent manually.
Why doesn't the pipeline run on a free Apify account?::Free-plan users can only run the actor **through the UI** — automated API runs require the **$49/mo plan**.
What keeps daily runs from spamming the same people?::Each run targets **fresh profiles** — LinkedIn URLs are never reused and previous emails are never copied.
What are the four inputs Claude confirms before running outreach?::**City/metro**, **target job fields**, **resume**, and **email signature**.

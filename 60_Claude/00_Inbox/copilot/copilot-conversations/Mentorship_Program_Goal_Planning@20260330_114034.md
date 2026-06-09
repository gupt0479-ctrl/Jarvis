---
epoch: 1774888834539
modelKey: "claude-sonnet-4.5|github-copilot"
topic: "Mentorship Program Goal Planning"



tags:
  - copilot-conversation
---

**user**: Based on my mentor details [[Mentor Details]]  and the things that i wish to accomplish in this mentorship program. {20_Progress/Mentorship Program} . I need your help coming up with a plan for the summer and the next few meetings that i am going to have with him in april. Guide me through the steps that i need to take to make the most out of this program.
[Context: Notes: 20_Progress/Mentorship Program/Mentor Details.md, 20_Progress/Mentorship Program/Plan.md]
[Timestamp: 2026/03/30 11:40:34]

**ai**: # Mentorship Program: April Meeting Preparation & Summer Planning Guide

Based on your mentor's background and your goals, here's a structured plan for maximizing the mentorship program through April meetings and summer planning.

---

## April Meeting Framework

### Meeting #1 (Early April): Project Demo & Career Direction

**What to bring:**
- **Portfolio demo** (3 screenshots + live link)[^1]
- **Learning Tracker progress** (even if incomplete)
- **One-pager**: What shipped / What blocked / What deciding next

**Discussion topics:**
- Show current portfolio implementation (chatbot, carousel features)
- Present Learning Tracker MVP scope and technical decisions
- Ask: "Given my timeline (graduation 2027), should I prioritize depth in full-stack or breadth across DevOps/mobile?"
- Request: Code review of one complex component (auth flow or RAG implementation)

**Outcomes to secure:**
- Feedback on architectural decisions (Next.js + Neon + Clerk stack)
- Scope refinement: what to cut before summer
- Introduction to 1-2 Best Buy engineers for informational interviews

---

### Meeting #2 (Mid-April): Summer Strategy & Network Building

**Preparation:**
- Draft summer plan with 3 paths: internship / research project / startup validation
- List 5 companies from [[Companies giving OPT & CPT]] you're targeting[^2]
- Prepare 3 questions about Best Buy's tech stack (React/GraphQL/AWS)

**Discussion framework:**
- "I'm deciding between X, Y, Z for summer. Here's my decision matrix..." (use MoSCoW framework you referenced)
- Practice elevator pitch (30-second version)[^3]
- Ask: "What early career mistakes would you warn against?"

**Action items:**
- Get LinkedIn intro to Best Buy university recruiting team
- Discuss OPT/CPT considerations for international students
- Secure mock interview slot for late April

---

## Summer Planning: Three-Track Strategy

### Track 1: If You Land an Internship (Priority)

**Weeks 1-2: Onboarding + Relationship Building**
- Meet your tech lead and adjacent teams
- Identify one mentor within the company
- Document tech stack in Obsidian (link to what you learned in class)

**Weeks 3-10: Execution + Learning**
- Ship one meaningful feature end-to-end
- Keep "Role Brief" notes (Frontend/Backend/DevOps exposure)[^4]
- Weekly check-ins with Ahnaf: "What I shipped / blockers / decisions"

**Weeks 11-12: Portfolio Conversion**
- Turn internship project into portfolio piece
- Get code review from full-time engineer
- Secure return offer intel or referral for next year

---

### Track 2: If No Internship → Research + Project Sprint

**June: Deep Work on Learning Tracker**
Follow your existing 5-sprint roadmap[^5]:
- Sprint 1: Foundation (auth + DB schema) - Week 1
- Sprint 2: Core MVP (browse + track) - Week 2
- Sprint 3: RAG implementation - Week 3-4
- Sprint 4: Deploy + 3D components - Week 5-6
- Sprint 5: Polish + packaging - Week 7-8

**July: BOOM UROP Extension**
- Apply for UROP symposium in April (you noted this)[^6]
- Continue tracing instrumentation work
- Present at symposium → portfolio artifact
- Turn PR work into technical blog post

**August: Interview Prep + Applications**
- 2 mock interviews with Ahnaf
- Apply to 50+ Fall co-op positions
- Build out portfolio site with 3 projects: Portfolio, Learning Tracker, BOOM observability work

---

### Track 3: Startup Validation (Low-Risk Side Track)

Execute the thought experiments you outlined[^7]:
1. **Problem validation** (Weeks 1-2)
   - Interview 10 students about goal tracking
   - Document pain points in Obsidian
   
2. **MVP wireframes** (Week 3)
   - Figma click-through of CheckIn → progress flow
   - Get feedback from Ahnaf on product thinking

3. **Technical feasibility** (Week 4)
   - Build one core feature (weekly check-in + chart)
   - Don't build teams/notifications yet
   
4. **Validation metric** (Weeks 5-8)
   - Get 5 friends to use it for 2 weeks
   - Track: 10 weekly active users with ≥2 check-ins/week
   - Decision point: pivot, persist, or pause?

**Outcome:** Even if you don't launch, you learn product validation, which Ahnaf's GitHub Copilot POC work suggests he values.

---

## Meeting Cadence for Summer

**Every 2 weeks (6 sessions total):**
- Format: 30-minute Zoom
- Structure: Demo → Shipped/Blocked/Deciding → Ask
- Bring: Updated "Role Brief" each time (cover 6 areas: Frontend, Backend, Full-stack, DevOps, Data, Mobile)

**Sample agenda rotation:**
1. Auth implementation decisions (Week 2)
2. RAG architecture review (Week 4)  
3. Deployment + CI/CD patterns (Week 6)
4. Mock technical interview (Week 8)
5. System design discussion (Week 10)
6. Return offer / recruiting strategy (Week 12)

---

## Networking Strategy (Parallel to Meetings)

**April actions:**
- Request intro to 2 Best Buy engineers (1 frontend, 1 backend)
- Join Best Buy tech talks if they have external events
- Connect with 5 UMN alumni at companies on your target list[^8]

**May-August:**
- 2 informational interviews per month (use template from [[LinkedIn Premium]])[^9]
- Track in Obsidian: company, contact, insights, follow-up
- Build "warm intro" pipeline for Fall recruiting

---

## Decision Framework: What to Prioritize

Use this hierarchy when time-boxing summer work:

**Must-haves:**
1. One shipped project (internship or Learning Tracker deployed)
2. Portfolio live with 3 projects
3. Resume updated with quantified impact
4. 2 technical mock interviews completed

**Should-haves:**
5. Blog post about BOOM observability work
6. 10 informational interviews logged
7. GitHub contribution graph showing consistent commits

**Could-haves:**
8. Startup validation complete
9. Open source contribution
10. Technical talk at UMN CS club

**Won't-haves (defer to Fall):**
- Multi-platform mobile app
- Monetization features
- Complex notification systems

---

## Metrics to Track

Create a simple spreadsheet (link in Obsidian):

| Week | Code commits | Applications sent | Network contacts | Learning hours | Ahnaf meetings |
|------|-------------|------------------|-----------------|----------------|----------------|
| June 1 | 25 | 5 | 2 | 15 | 1 |

Review weekly. Adjust if any column is zero for 2 weeks straight.

---

## April Prep Checklist

**By April 5:**
- [ ] Portfolio deployed (even if beta)
- [ ] Learning Tracker repo public with README
- [ ] Summer plan one-pager drafted
- [ ] 3 questions for Ahnaf prepared
- [ ] Elevator pitch practiced (record yourself)

**By April 15:**
- [ ] Mock interview scheduled
- [ ] 5 target companies researched
- [ ] LinkedIn connections sent to Best Buy engineers
- [ ] UROP symposium application submitted[^10]

**By April 30:**
- [ ] Summer decision made (internship / project sprint / hybrid)
- [ ] Next 3 months calendared with milestones
- [ ] GitHub project board set up for summer work
- [ ] Emergency fund / housing / logistics secured

---

## Key Questions to Ask Ahnaf

Rotate these across April meetings:

**Technical:**
- "How do you balance feature velocity vs. technical debt at scale?"
- "What patterns have you seen break when traffic increases 10×?"
- "How do you structure code reviews for junior engineers?"

**Career:**
- "What signals in a resume/portfolio get you to interview someone?"
- "How should international students approach OPT timeline planning?"
- "What's the difference between intern work and new grad expectations?"

**Networking:**
- "Can you intro me to someone in [team X] at Best Buy?"
- "How do you evaluate startup vs. big tech early career?"
- "What questions should I ask in informational interviews?"

---

## Success Metrics for Mentorship Program

By August 31, you should have:
- [ ] 6 meaningful meetings with actionable takeaways
- [ ] 2+ referrals or intros from mentor's network
- [ ] 1 code review or technical deep-dive session
- [ ] Portfolio artifact directly influenced by mentor feedback
- [ ] Clear Fall recruiting strategy with warm leads

---

## Red Flags to Avoid

**Don't:**
- Ask Ahnaf to get you a job (he's explicitly not expected to)[^11]
- Show up unprepared or cancel meetings last-minute
- Only contact when you need something
- Ignore his advice repeatedly without explaining why

**Do:**
- Send thank-you notes after each meeting
- Share wins (deployed feature, good grade, accepted PR)
- Act on his suggestions and report back
- Respect his time (30-min max, clear agenda)

---

## Final Recommendation

**For April:** Focus on **demonstrating execution capability**. Show him you can ship, even if imperfect. That builds trust for deeper technical mentorship.

**For Summer:** Optimize for **learning velocity over perfection**. Ship the Learning Tracker even if it's not production-grade. The process of building, deploying, and iterating with user feedback will teach you more than polishing one feature for weeks.

**For Fall:** Use summer artifacts to **convert mentorship into job opportunities**. Your portfolio should tell the story: "I built X, learned Y from my mentor, and here's how I'd apply it at your company."

The mentorship program is a **relationship-building vehicle, not a transactional exchange**. Treat Ahnaf as a long-term connection who can advise you through multiple career transitions, not just one summer.

---

#### Sources
[^1]: [[Plan]]
[^2]: [[Companies giving OPT & CPT]]
[^3]: [[Elevator pitch]]
[^4]: [[Plan]]
[^5]: [[Arc (Learning Tracker)]]
[^6]: [[01-03-2026]]
[^7]: [[Plan]]
[^8]: [[Useful Links]]
[^9]: [[LinkedIn Premium]]
[^10]: [[01-03-2026]]
[^11]: [[Plan]]

---

**Note:** The retrieval cap was reached — some matching documents were not included. Upgrade to Copilot Plus for more complete answers.
[Timestamp: 2026/03/30 11:41:57]

**user**: You are tasked to help me implement an AI workflow for my day to day life as a college computer science student aspiring to be a ai/ml engineer. I am interested in ai and would like to learn it along with using it accurately. I am planning on switching up my subscriptions and workflows. Help me implement what we have learnt in the [[Gen AI Day - 2]] [[Gen AI Day - 1]] [[Gen AI Meeting]] [[Gen AI Roadmap]] Gen AI classes. I need your help implementing these workflows that were taught to me and are relevant to me. Analyze all my notes on this workflow i want to implement. Write the workflow that you think is suited for me in the [[AI Workflow]] file.
[Context: Notes: 40_Resources/CS/AI/Gen AI Day - 2.md, 40_Resources/CS/AI/Gen AI Day - 1.md, 40_Resources/CS/AI/Gen AI Meeting.md, 40_Resources/CS/AI/Gen AI Roadmap.md, 40_Resources/CS/AI/AI Workflow.md]
[Timestamp: 2026/03/30 20:30:51]

**ai**: # AI Workflow Implementation Plan

Based on your current subscriptions, learning goals, and the Gen AI Mastermind curriculum, here's a comprehensive workflow designed for a CS student aspiring to become an AI/ML engineer.

---

## Current Subscription Analysis

**What you have:**
- ChatGPT Pro ($10/month)
- Cursor Pro (Student - Free)
- GitHub Copilot (Student - Free)
- Ollama (Free, local)
- Jan (Free, open-source)

**What you're considering:**
- Claude Pro (currently using via Ollama)
- Perplexity Student ($8/month)

---

## Recommended Subscription Strategy

### Keep & Optimize
1. **ChatGPT Pro** - Your primary assistant for Custom GPTs, prompting practice, and general tasks[^1]
2. **GitHub Copilot** - Essential for coding in VS Code
3. **Cursor Pro** - For AI-powered development when building larger projects

### Add (High Priority)
1. **Claude Pro** ($20/month) - Critical for:
   - Long-context work (200K tokens for research papers, documentation)[^2]
   - Script writing and structured thinking[^3]
   - Planning multi-step workflows
   - Better reasoning for complex problems

### Add (Medium Priority)
2. **Perplexity Student** ($8/month) - Valuable for:
   - Research with citations (academic papers, technical concepts)
   - Verifying AI-generated information
   - Learning new ML/AI topics with source backing

### Optimize (Free Tools)
3. **Ollama** - Use strategically for:
   - Private work (notes, journal, personal projects)[^4]
   - Offline AI access during no-internet situations
   - Testing prompts without burning API credits

4. **Jan** - Configure as your MCP-connected assistant:
   - Connect to your file system
   - Automate boring tasks (file organization, note processing)
   - Build custom workflows with tool connectors[^5]

---

## Daily AI Workflow (Role-Based)

### Morning Routine (Planning & Research)
**Tool:** Claude Pro  
**Purpose:** Strategic thinking and learning

**Tasks:**
- Review course materials and generate study plans
- Research new ML/AI concepts with long-context understanding
- Plan coding projects with detailed PRDs[^6]
- Draft technical blog posts or documentation

**Prompt template:**
```markdown
# Role
You are a senior AI/ML engineer and CS educator specializing in [topic].

# Objective
Help me understand [concept] and create a learning plan.

# Context
- Current knowledge: [your level]
- Goal: [what you want to achieve]
- Timeline: [deadline]

# Instructions
1. Explain the concept with examples
2. Identify prerequisites I need
3. Create a 1-week learning plan
4. Suggest 3 hands-on projects

# Output Format
- Key concepts (bullet points)
- Prerequisites (table)
- Daily learning plan
- Project ideas with difficulty ratings
```

---

### Coding Sessions (Development)
**Primary:** Cursor Pro or VS Code with GitHub Copilot  
**Backup:** ChatGPT Pro for complex debugging

**Workflow:**
1. **Planning phase:**
   - Use ChatGPT to generate initial architecture
   - Ask Claude to review and suggest improvements
   - Create a 3-stage PRD (simple → basic → platform-optimized)[^7]

2. **Building phase:**
   - Use Cursor for AI-assisted coding
   - Use GitHub Copilot for inline completions
   - Test incrementally (build → test → fix → repeat)[^8]

3. **Debugging phase:**
   - Apply ODA loop (Observe → Diagnose → Ask)[^9]
   - Copy exact error to ChatGPT with context
   - Ask: "What's broken, why, and how to fix with minimal changes?"

**Code review prompt:**
```markdown
Review this code for:
1. Bugs or logic errors
2. Performance issues
3. Best practices violations
4. Security concerns

Code:
[paste code]

Context: [what it should do]
```

---

### Learning Sessions (Studying & Note-Taking)
**Tool:** Custom GPT (ChatGPT) + Perplexity Student

**Setup:** Create a "CS Study Buddy" Custom GPT[^10]

**Instructions for Custom GPT:**
```markdown
# Role
You are an experienced CS educator specializing in AI/ML topics.

# Objective
Help me learn computer science concepts efficiently and retain information.

# Context
- I'm a CS student focusing on AI/ML
- I take notes in Obsidian
- I prefer spaced repetition and active recall

# Instructions
When I share course materials or topics:
1. Extract key concepts and definitions
2. Generate 5-8 Anki-style flashcards
3. Create a mini quiz (3 questions)
4. List common mistakes students make
5. Suggest 1 hands-on exercise

# Output Format
## Key Concepts
- [concept]: [definition]

## Flashcards
Q: [question]
A: [answer]

## Quiz
1. [question with 4 options]

## Common Mistakes
- [mistake]: [why it's wrong]

## Practice Exercise
[specific coding/problem-solving task]
```

**Research workflow with Perplexity:**
1. Ask Perplexity for citations on new topics
2. Read the sources it provides
3. Take notes in Obsidian
4. Use ChatGPT to convert notes into study materials

---

### Project Building (Vibe Coding)
**Tool:** ChatGPT Pro or Claude Pro + Bolt/Replit

**When to use vibe coding:**
- Prototyping ideas quickly
- Building portfolio projects
- Learning new frameworks
- Hackathons

**6-step vibe coding workflow:**[^11]

1. **Start with a plan** (Stage 1 PRD)
   ```
   I want to build [app idea] that solves [problem] for [users].
   
   Core features:
   - [feature 1]
   - [feature 2]
   - [feature 3]
   
   Generate a rough outline with tech stack suggestions.
   ```

2. **Create Basic PRD** (Stage 2)
   - Problem statement
   - Target users
   - Core differentiator (AI feature)
   - Feature list with priorities (MoSCoW)[^12]

3. **Platform-optimized prompt** (Stage 3)
   - Convert PRD into Bolt-specific instructions
   - Include: React + TS, DB schema, auth, API contracts

4. **Build iteratively**
   - One feature at a time
   - Test immediately after each build
   - Use bookmarks/restore in Bolt[^13]

5. **Debug with ODA loop**
   - Observe: exact error + where it happens
   - Diagnose: why you think it broke
   - Ask: specific fix request with context

6. **Save & sync**
   - Connect GitHub for version control
   - Export final code for portfolio

---

### Private/Sensitive Work (Local AI)
**Tool:** Ollama + Jan

**Use cases:**
- Processing personal notes
- Working on confidential projects
- Experimenting without internet
- Building local automations

**Setup:**
```bash
# Install recommended models
ollama pull llama3.2:3b  # Fast, general purpose
ollama pull codellama:7b  # Code-focused
ollama pull mistral:7b    # Strong reasoning

# Basic usage
ollama run llama3.2:3b
```

**Workflows to automate with Jan + MCP:**[^14]
1. **Weekly note summary**
   - Trigger: Every Sunday
   - Action: Summarize week's notes
   - Output: Save to "Weekly Recap" note

2. **Project documentation generator**
   - Trigger: New GitHub repo
   - Action: Generate README from code
   - Output: Draft in "Portfolio Drafts"

3. **Daily standup generator**
   - Trigger: Morning (9 AM)
   - Action: Review yesterday's commits + today's calendar
   - Output: Standup summary in Slack/Obsidian

---

## Content Creation Workflow

### Technical Blog Posts / Portfolio Documentation
**Tool:** Claude Pro (writing) + ChatGPT (editing)

**Content DNA workflow:**[^15]
1. Collect 10-20 past posts/project descriptions
2. Ask Claude: "Analyze my writing style and create a style guide"
3. Convert analysis into markdown prompt
4. Create Custom GPT: "Technical Writer (My Style)"
5. Use for all future documentation

**Blog post workflow:**
```markdown
# Input to Claude
Write a technical blog post about [project/concept]:

Project: [name + brief description]
Tech stack: [technologies used]
Problem solved: [what it does]
Key challenges: [what was hard]
Learnings: [what you learned]

Style: Technical but approachable, code examples, clear structure

Output:
- Catchy title
- TL;DR (2 sentences)
- Introduction
- Technical breakdown (with code snippets)
- Challenges & solutions
- Key takeaways
- Next steps
```

---

### Resume/LinkedIn Optimization
**Tool:** Custom GPT or Gemini Gem

**Create "Career Content Assistant":**[^16]
```markdown
# Role
You are a technical recruiter and career advisor for CS/AI roles.

# Objective
Help optimize my resume, LinkedIn, and portfolio content.

# Instructions
When I share project descriptions or experience:
1. Rewrite with STAR format (Situation, Task, Action, Result)
2. Add quantifiable metrics where possible
3. Use action verbs (built, optimized, implemented)
4. Highlight AI/ML keywords for ATS
5. Keep bullets concise (1-2 lines)

# Input Format
Project: [name]
What I did: [description]
Technologies: [stack]
Impact: [results if known]

# Output
## Resume Bullet Points (3-4)
- [bullet 1]
- [bullet 2]
- [bullet 3]

## LinkedIn Description (paragraph format)

## Portfolio README Section
```

---

## Automation Workflows (Make/Zapier/n8n)

### Starter Automation #1: Weekly Learning Recap[^17]
**Trigger:** Every Sunday at 8 PM  
**Action:** AI summarizes your week's notes  
**Output:** Saves to Obsidian "Weekly Recap" note

**Implementation:**
1. Connect Obsidian vault (via API or file sync)
2. Collect all notes modified this week
3. Send to ChatGPT with prompt:
   ```
   Summarize these notes into:
   - Key learnings (3-5 bullets)
   - Projects worked on
   - Concepts mastered
   - Questions/gaps to address next week
   ```
4. Save output to new note with date

---

### Starter Automation #2: Job Application Tracker
**Trigger:** New row in "Job Applications" Google Sheet  
**Action:** AI generates custom cover letter  
**Output:** Saves to Drive + sends draft to email

**Setup:**
1. Create sheet with columns: Company, Role, Job Description, Status
2. When new row added → trigger automation
3. Send job description to ChatGPT:
   ```
   Generate a cover letter for:
   
   Company: [name]
   Role: [title]
   Job Description: [paste]
   
   My background:
   - CS student specializing in AI/ML
   - Projects: [list 3 relevant projects]
   - Skills: [relevant skills]
   
   Tone: Professional but enthusiastic
   Length: 250-300 words
   Focus: Match my experience to their needs
   ```
4. Save output + notify you for review

---

### Starter Automation #3: Daily Standup Generator
**Trigger:** Every weekday at 9 AM  
**Action:** Review yesterday's commits + today's calendar  
**Output:** Draft standup in Slack/Obsidian

**Components:**
1. Pull GitHub commits from yesterday
2. Pull calendar events for today
3. Check Obsidian for yesterday's TODO completions
4. Generate standup:
   ```
   Yesterday: [completed tasks]
   Today: [planned tasks]
   Blockers: [if any]
   ```

---

## Model Selection Strategy

### When to use each model:

**ChatGPT Pro:**
- Quick questions and general tasks
- Custom GPTs for repeated workflows
- Web browsing for current info
- DALL-E integration for images

**Claude Pro:**
- Long documents (papers, codebases)
- Complex reasoning and planning
- Structured writing (blogs, documentation)
- Multi-step project planning
- Code review of large files

**GitHub Copilot:**
- Inline code completions
- Function implementations
- Boilerplate generation
- Quick refactoring

**Cursor Pro:**
- Multi-file editing
- Large codebase navigation
- AI-assisted debugging across files
- Rapid prototyping

**Ollama (Local):**
- Private notes processing
- Offline work
- Experimentation without costs
- Learning prompt engineering

---

## Weekly Learning Plan (Gen AI Roadmap)[^18]

### Week 1-2: Level 1 Foundations
**Goal:** Master prompting basics

**Tasks:**
1. Create 10 reusable prompts in markdown format[^19]
2. Build 2 Custom GPTs:
   - Study Buddy (course material → flashcards)
   - Code Reviewer (analyze code quality)
3. Test Magic Prompt Formula on 5 different tasks

**Deliverable:** Prompt library in Obsidian

---

### Week 3-4: Level 2 Advanced Prompting + RAG
**Goal:** Build RAG system for your notes

**Tasks:**
1. Research RAG architecture
2. Build simple RAG prototype:
   - Use Obsidian vault as knowledge base
   - Connect to ChatGPT API
   - Query your notes intelligently
3. Document the process

**Deliverable:** Working notes search system

---

### Week 5-6: Level 3 Content Creation
**Goal:** Create AI-generated video ad

**Tasks:**
1. Follow full video workflow:[^20]
   - Creative brief → script → storyboard
   - Image generation → image-to-video
   - VO + music → edit
2. Create 30-second portfolio project showcase
3. Post on LinkedIn

**Deliverable:** Published video + workflow documentation

---

### Week 7-8: Level 4 Automations
**Goal:** Ship 3 automations

**Tasks:**
1. Weekly learning summary (described above)
2. Job application tracker
3. Daily standup generator

**Deliverable:** 3 working automations + writeup

---

### Week 9-12: Level 5 App Building
**Goal:** Ship vibe-coded portfolio project

**Tasks:**
1. Build AI-powered app (ideas below)
2. Deploy with authentication
3. Write technical blog post
4. Add to portfolio

**Project ideas for AI/ML students:**
- ML model comparison dashboard
- Research paper summarizer with RAG
- Code snippet organizer with semantic search
- Interview prep chatbot (LeetCode + behavioral)

---

## Portfolio Projects to Build (Using Vibe Coding)

### Project 1: AI-Powered Study Assistant
**Core features:**
- Upload PDF/notes → extract key concepts
- Generate flashcards automatically
- Quiz generator with explanations
- Spaced repetition tracker

**AI feature:** RAG-based Q&A over your notes

**Tech stack:** Next.js + Clerk + Neon + OpenAI API

**Timeline:** 2-3 weeks

---

### Project 2: Technical Interview Prep Platform
**Core features:**
- LeetCode problem recommender
- Solution explanations in multiple approaches
- Behavioral question practice with AI feedback
- Mock interview simulator

**AI feature:** Personalized problem recommendations based on weak areas

**Tech stack:** React + Firebase + Anthropic API

**Timeline:** 3-4 weeks

---

### Project 3: Research Paper Assistant
**Core features:**
- ArXiv paper search and summarization
- Key findings extraction
- Related papers recommendation
- Personal paper library with notes

**AI feature:** Multi-paper synthesis and comparison

**Tech stack:** Next.js + Supabase + OpenAI + Pinecone (vector DB)

**Timeline:** 4-5 weeks

---

## Recommended Daily Schedule

### Morning (7-9 AM)
- Review calendar + standup (automated)
- Read 1 AI/ML research paper summary (Perplexity)
- Plan day's tasks in Obsidian

### Focus Block 1 (9 AM-12 PM)
- Coding projects (Cursor/VS Code)
- Use GitHub Copilot for implementation
- Test + commit regularly

### Afternoon (1-3 PM)
- Coursework + studying
- Use Study Buddy GPT for material processing
- Take notes in Obsidian

### Focus Block 2 (3-6 PM)
- Continue projects OR
- Work on portfolio/automation OR
- Learn new concepts (Claude for long docs)

### Evening (7-9 PM)
- Review day's progress
- Update project documentation
- Plan tomorrow's tasks

### Before Bed (Optional)
- Journal or private notes (Ollama for privacy)
- Review flashcards (Anki)

---

## Budget Optimization

### Current Monthly Cost:
- ChatGPT Pro: $10
- **Total: $10/month**

### Recommended Monthly Cost:
- ChatGPT Pro: $10
- Claude Pro: $20
- Perplexity Student: $8
- **Total: $38/month**

### ROI Justification:
- **ChatGPT Pro:** Custom GPTs save 5+ hours/week on repeated tasks
- **Claude Pro:** Better code reviews + documentation = higher quality projects
- **Perplexity:** Research time cut by 50% vs traditional methods

**Total time saved:** 10-15 hours/week  
**Cost per hour saved:** ~$0.60-0.90

**Alternative if budget is tight:**
- Keep ChatGPT Pro ($10)
- Add Perplexity Student ($8)
- Use Claude via API (pay-as-you-go, ~$5-10/month)
- **Total: $23-28/month**

---

## Workflow Optimization Tips

### Avoid Tool Overload
**Problem:** Too many subscriptions = decision fatigue

**Solution:** "Tool per role" system
- **Writing/docs:** Claude
- **General tasks:** ChatGPT
- **Research:** Perplexity
- **Coding:** Cursor/Copilot
- **Private:** Ollama

**Rule:** If you haven't used a tool in 2 weeks, cancel it.

---

### Master One Workflow at a Time
**Week 1:** Prompting basics + Custom GPTs  
**Week 2:** Automation (1 automation only)  
**Week 3:** Vibe coding (1 small app)  
**Week 4:** Content creation (1 blog post)

Don't try to learn everything simultaneously.

---

### Build in Public
**Why:** Accountability + feedback + networking

**How:**
1. Tweet/LinkedIn post your weekly progress
2. Share project builds on GitHub
3. Write technical blog posts
4. Engage with AI/ML community

**Template:**
```
This week I built [project] using [tools].

Key learning: [insight]
Challenge: [what was hard]
Solution: [how you solved it]

Code: [GitHub link]
Demo: [video/screenshots]

#AI #ML #BuildInPublic
```

---

## Backup & Fallback Strategy

### When Primary Tool Fails:

**If ChatGPT is down:**
→ Switch to Claude for general tasks  
→ Use Ollama for private work

**If Claude is down:**
→ Use ChatGPT for writing  
→ Break long docs into chunks

**If Cursor fails:**
→ Fall back to VS Code + Copilot  
→ Use ChatGPT web for complex debugging

**If internet is out:**
→ Ollama for offline AI access  
→ Pre-downloaded models for coding help

---

## Metrics to Track

### Weekly Review (in Obsidian):
- Hours saved by AI tools
- Projects shipped
- Concepts learned
- Prompts created/refined
- Automations working
- Portfolio pieces added

### Monthly Review:
- Tool usage patterns
- Subscription ROI
- Learning progress (roadmap %)
- GitHub contribution graph
- LinkedIn engagement

### Quarterly Review:
- Major projects completed
- Skills mastered
- Interview performance
- Job applications sent
- Network growth

---

## Action Items (Start Today)

### Immediate (This Week):
- [ ] Subscribe to Claude Pro
- [ ] Create 2 Custom GPTs (Study Buddy + Code Reviewer)
- [ ] Set up Ollama with 2-3 models
- [ ] Build prompt template library (10 prompts minimum)
- [ ] Configure Jan for file automation

### Short-term (Next 2 Weeks):
- [ ] Build first automation (weekly recap)
- [ ] Start vibe coding first portfolio project
- [ ] Write technical blog post about your workflow
- [ ] Set up MCP connections in Jan

### Medium-term (Next Month):
- [ ] Complete Level 1-2 of Gen AI Roadmap
- [ ] Ship 2 portfolio projects
- [ ] Create content DNA assistant
- [ ] Build RAG system for Obsidian notes

### Long-term (Next 3 Months):
- [ ] Complete all 5 levels of roadmap
- [ ] Ship 3-5 portfolio projects with AI features
- [ ] Publish 10+ technical blog posts
- [ ] Build "AI Engineer" personal brand online
- [ ] Apply Gen AI skills to land internship/research position

---

## Final Recommendations

1. **Don't overthink the tools** - Start with what you have and upgrade only when you hit clear limitations.

2. **Focus on one workflow at a time** - Master prompting before automations, automations before vibe coding.

3. **Build in public** - Share your learning journey. It compounds over time.

4. **Prioritize shipping over perfection** - A deployed imperfect project beats a perfect unfinished one.

5. **Use AI to learn AI** - Let ChatGPT explain ML concepts, Claude review your code, Perplexity find research papers.

6. **Track everything in Obsidian** - Your vault should be the source of truth for all workflows, prompts, and progress.

7. **Exhaust free tools first** - GitHub Copilot + Cursor Student are incredibly powerful. Master them before adding subscriptions.

8. **Connect workflows to real goals** - Every automation should save time for actual learning or building.

The goal isn't to use every AI tool - it's to build a sustainable workflow that accelerates your path to becoming an AI/ML engineer while maintaining high output quality and learning velocity.

Start with the "Immediate" action items today, and iterate based on what works for your specific needs.

---

#### Sources
[^1]: [[Gen AI Meeting]]
[^2]: [[Gen AI Meeting]]
[^3]: [[Gen AI Day - 2]]
[^4]: [[Gen AI Day - 2]]
[^5]: [[Gen AI Day - 2]]
[^6]: [[Gen AI Day - 2]]
[^7]: [[Gen AI Day - 2]]
[^8]: [[Gen AI Day - 2]]
[^9]: [[Gen AI Day - 2]]
[^10]: [[Gen AI Day - 1]]
[^11]: [[Gen AI Day - 2]]
[^12]: [[Gen AI Day - 2]]
[^13]: [[Gen AI Day - 2]]
[^14]: [[Gen AI Day - 2]]
[^15]: [[Gen AI Day - 1]]
[^16]: [[Gen AI Day - 1]]
[^17]: [[Gen AI Day - 2]]
[^18]: [[Gen AI Roadmap]]
[^19]: [[Gen AI Day - 1]]
[^20]: [[Gen AI Day - 2]]
[Timestamp: 2026/03/30 20:33:08]
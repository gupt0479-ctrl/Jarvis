---
type: concept
input_kind: ai
status: seed
created: 2026-03-07
updated: 2026-07-27
source_url: gpt
related_progress:
  - "[[Gen AI Meeting]]"
  - "[[Gen AI Roadmap]]"
  - "[[MCPs]]"
tags:
  - concept
next: "[[MCPs]]"
track:
  - ai
prerequisites:
  - "[[Gen AI Day - 1]]"
used_in: []
evidence:
  - "[[60_Claude/45_Outputs/Vault Enrichment Prompt]]"
  - "[[60_Claude/45_Outputs/Plan-First Coding Prompt]]"
difficulty: 2
mastery_level: novice
mastery_score: null
last_drilled: 2026-04-25
next_drill: 2026-05-09
drill_interval: 14
---
# AI Workflow Implementation Plan
Based on your current subscriptions, learning goals, and the Gen AI Mastermind curriculum, here's a comprehensive workflow designed for a CS student aspiring to become an AI/ML engineer.
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
## Daily AI Workflow (Role-Based)
### Morning Routine (Planning & Research)
**Tool:** Claude Pro  
**Purpose:** Strategic thinking and learning
**Tasks:**
- Review course materials and generate study plans
- Research new ML/AI concepts with long-context understanding
- Plan coding projects with detailed PRDs
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
### Coding Sessions (Development)
**Primary:** Cursor Pro or VS Code with GitHub Copilot  
**Backup:** ChatGPT Pro for complex debugging
**Workflow:**
1. **Planning phase:**
   - Use ChatGPT to generate initial architecture
   - Ask Claude to review and suggest improvements
   - Create a 3-stage PRD (simple → basic → platform-optimized)
1. **Building phase:**
   - Use Cursor for AI-assisted coding
   - Use GitHub Copilot for inline completions
   - Test incrementally (build → test → fix → repeat)
1. **Debugging phase:**
   - Apply ODA loop (Observe → Diagnose → Ask)
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
### Learning Sessions (Studying & Note-Taking)
**Tool:** Custom GPT (ChatGPT) + Perplexity Student
**Setup:** Create a "CS Study Buddy" Custom GPT
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
### Project Building (Vibe Coding)
**Tool:** ChatGPT Pro or Claude Pro + Bolt/Replit
**When to use vibe coding:**
- Prototyping ideas quickly
- Building portfolio projects
- Learning new frameworks
- Hackathons
**6-step vibe coding workflow:**
1. **Start with a plan** (Stage 1 PRD)
   ```
   I want to build [app idea] that solves [problem] for [users].
   Core features:
   - [feature 1]
   - [feature 2]
   - [feature 3]
   Generate a rough outline with tech stack suggestions.
   ```
1. **Create Basic PRD** (Stage 2)
   - Problem statement
   - Target users
   - Core differentiator (AI feature)
   - Feature list with priorities (MoSCoW)
1. **Platform-optimized prompt** (Stage 3)
   - Convert PRD into Bolt-specific instructions
   - Include: React + TS, DB schema, auth, API contracts
1. **Build iteratively**
   - One feature at a time
   - Test immediately after each build
   - Use bookmarks/restore in Bolt
1. **Debug with ODA loop**
   - Observe: exact error + where it happens
   - Diagnose: why you think it broke
   - Ask: specific fix request with context
1. **Save & sync**
   - Connect GitHub for version control
   - Export final code for portfolio
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
**Workflows to automate with Jan + MCP:**
1. **Weekly note summary**
   - Trigger: Every Sunday
   - Action: Summarize week's notes
   - Output: Save to "Weekly Recap" note
1. **Project documentation generator**
   - Trigger: New GitHub repo
   - Action: Generate README from code
   - Output: Draft in "Portfolio Drafts"
1. **Daily standup generator**
   - Trigger: Morning (9 AM)
   - Action: Review yesterday's commits + today's calendar
   - Output: Standup summary in Slack/Obsidian
## Content Creation Workflow
### Technical Blog Posts / Portfolio Documentation
**Tool:** Claude Pro (writing) + ChatGPT (editing)
**Content DNA workflow:**
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
### Resume/LinkedIn Optimization
**Tool:** Custom GPT or Gemini Gem
**Create "Career Content Assistant":**
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
## Automation Workflows (Make/Zapier/n8n)
### Starter Automation #1: Weekly Learning Recap
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
## Weekly Learning Plan (Gen AI Roadmap)
### Week 1-2: Level 1 Foundations
**Goal:** Master prompting basics
**Tasks:**
1. Create 10 reusable prompts in markdown format[^19]
2. Build 2 Custom GPTs:
   - Study Buddy (course material → flashcards)
   - Code Reviewer (analyze code quality)
3. Test Magic Prompt Formula on 5 different tasks
**Deliverable:** Prompt library in Obsidian
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
### Week 7-8: Level 4 Automations
**Goal:** Ship 3 automations
**Tasks:**
1. Weekly learning summary (described above)
2. Job application tracker
3. Daily standup generator
**Deliverable:** 3 working automations + writeup
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
### Project 2: Technical Interview Prep Platform
**Core features:**
- LeetCode problem recommender
- Solution explanations in multiple approaches
- Behavioral question practice with AI feedback
- Mock interview simulator
**AI feature:** Personalized problem recommendations based on weak areas
**Tech stack:** React + Firebase + Anthropic API
**Timeline:** 3-4 weeks
### Project 3: Research Paper Assistant
**Core features:**
- ArXiv paper search and summarization
- Key findings extraction
- Related papers recommendation
- Personal paper library with notes
**AI feature:** Multi-paper synthesis and comparison
**Tech stack:** Next.js + Supabase + OpenAI + Pinecone (vector DB)
**Timeline:** 4-5 weeks
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
### Master One Workflow at a Time
**Week 1:** Prompting basics + Custom GPTs  
**Week 2:** Automation (1 automation only)  
**Week 3:** Vibe coding (1 small app)  
**Week 4:** Content creation (1 blog post)
Don't try to learn everything simultaneously.
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

## Deep Dive

### One-Sentence Version

An AI workflow assigns each tool a role — Claude for long-context thinking, ChatGPT for fast tutoring and custom GPTs, Cursor/Copilot for repo-level coding, Ollama for private local work — and the discipline is using the right tool for the right task instead of forcing one tool to do everything.

### What It Is

This note is an operational plan for daily AI tool usage, organized by task type:

- **Morning (planning + research)**: Claude Pro for strategic thinking, long-context document analysis, and PRD drafting. Claude handles 100K+ token contexts, which makes it the right tool for reviewing entire codebases or course materials.
- **Coding sessions**: Cursor Pro for multi-file editing with Plan Mode, GitHub Copilot for inline completions, ChatGPT for complex debugging when you need to paste error context and get step-by-step diagnosis.
- **Learning sessions**: Custom GPTs (ChatGPT) for converting course materials into flashcards and quizzes, Perplexity for citation-backed research.
- **Private work**: Ollama + Jan for processing sensitive notes, personal journals, and confidential projects without sending data to cloud APIs.

The "tool per role" system prevents decision fatigue: you don't choose a tool each time, you follow the lane assignment. If you haven't used a tool in 2 weeks, cancel it.

### Why It Matters

- Without role assignment, you waste time switching between tools or forcing one tool to handle tasks it's bad at. ChatGPT is fast but shallow on long documents. Claude is thorough but slower for quick questions. Cursor is powerful for code but useless for writing blog posts.
- The 3-lane model (study → tutoring → coding) maps directly to how a CS student's day actually works. Each lane has a default tool and a fallback.
- The budget analysis is practical: $38/month for ChatGPT Pro + Claude Pro + Perplexity Student saves 10-15 hours/week at ~$0.60-0.90/hour. If a tool doesn't save time, drop it.

### Real Example

From the workflow plan: when building a portfolio project, the sequence is — (1) use Claude to draft the PRD and review architecture, (2) use ChatGPT to generate acceptance criteria and edge cases, (3) use Cursor to implement with Plan Mode, (4) use Copilot for inline completions during implementation, (5) use Ollama to process private notes that feed into the project without uploading them to cloud APIs.

The automation workflows are concrete: a weekly learning recap (trigger: Sunday, action: AI summarizes week's notes, output: saved to Obsidian), a job application tracker (trigger: new row in Google Sheet, action: AI generates cover letter), a daily standup generator (trigger: 9 AM, action: review commits + calendar).

### Contrast With

**Role-based workflow vs. single-tool workflow**: Using only ChatGPT for everything means you hit context limits on long documents, miss inline code completions, and send private data to OpenAI's servers. The role-based approach trades simplicity for effectiveness — more tools to manage, but each tool operates in its strength zone.

**This workflow vs. "just use Claude Code for everything"**: Claude Code is powerful for autonomous coding but doesn't replace the planning phase (Claude Pro), the quick-question phase (ChatGPT), or the privacy phase (Ollama). The workflow is a stack, not a single tool.

### Source Anchors

- Generated from ChatGPT based on Gen AI Mastermind curriculum and current subscriptions
- [[Gen AI Roadmap]] — the learning plan this workflow operationalizes
- [[MCPs]] — MCP protocol that enables tool connections in the coding lane
- [[Cursor AI]] — detailed Cursor workflow that expands on the coding lane
- [[Gen AI Day - 1]] — LLM fundamentals that explain why different models have different strengths

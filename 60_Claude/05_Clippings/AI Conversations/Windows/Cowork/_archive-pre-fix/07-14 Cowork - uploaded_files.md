---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "uploaded_files"
started_at: 2026-07-14T22:29:15
ended_at: 2026-07-14T22:30:26
project: Cowork
status: raw
session_id: 17d90063-35e2-42cd-8208-b3f6d627c743
tags:
  - input
  - ai-conversation
  - claude-code
---

# uploaded_files

## You

<uploaded_files>
<file><file_path>Anant Gupta Resume new.pdf</file_path></file>
</uploaded_files>

I am about to attend a networking meeting right now. I am going to ask you questions about myself and you need to answer in detail looking at the notes that are listed in this vault. Refer to the notes only when answering the questions in this session. I have also attached you with my resume for further information, you could also take a look at the sanity data for my deployed website(https://anantgupta.dev). But first get a brief understanding of everything that I do and the recent projects that I have been working on. Here are some notes you could take a look at to answer the following questions: `20_Progress/Mentorship Program/Meetings`, `10_Areas/Summer Grind`, `20_Progress/Projects` and any other relevant ai based information in this vault listed inside `60_Claude/` folder. Get ready for the questions coming your way now.

## Claude

I'll help you prepare for your networking meeting! Let me quickly gather all the key information about you from your vault, resume, and website. I'll load the necessary tools and read through the critical sections.

Now let me read the key sections from your vault to build a complete picture:

Let me search for the specific project and mentorship files:

Perfect! I've loaded everything. Here's your **networking-ready brief** organized for easy reference during conversations:

---

## **Quick Personal Summary**
You're a **CS student at UMN** (graduating Spring 2028) focused on **AI, data systems, and full-stack engineering**. You build real products, not demos — you care deeply about separating deterministic logic from AI advice, keeping systems auditable, and shipping portfolio-grade work.

---

## **Your Current Work**

### **Work Experience**
- **Web Dev Intern @ NSEdu** (June-Aug 2025): Built Assisto platform using Next.js, React, Tailwind + Strapi backend; created high-performance, SEO-optimized UI components
- **Research Assistant – BOOM** (May 2025-ongoing): Rust-based logging middleware for astronomical alert brokering at UMN with Prof. Michael Coughlin; real-time event tracking, observability, backend APIs for data pipelines
- **CSE Student Ambassador** (Sept 2025): Campus tours, public speaking, audience engagement

---

## **Recent Hackathon Projects (O1 Summit 2026)**

### **Resq** — *Fintech + Full-Stack* ⭐ *Currently your stronger portfolio story*
**Elevator pitch:** "CFO workspace for founders who can't afford a finance team. Takes real ledger facts, generates a deterministic 13-week cash forecast, detects when cash breaks, and ranks CFO moves (collections, payment deferrals, financing). AI advises—never touches the math."

**Tech:** Next.js + TypeScript, Supabase/Postgres, Drizzle ORM, Zod, TinyFish mock/live integration, audit logging  
**What's real:** Deterministic cash services, 13-week forecast engine, breakpoint detection, risk analysis, ranked action queue, schema, API routes, audit trail  
**Key lesson:** Product strength comes from trust—when AI stays out of the financial truth, it becomes more credible  
**Portfolio angle:** Full-stack architecture + financial modeling + AI systems design + external integration patterns  

### **OpsPilot** — *Operations + AI Workflow*
**Elevator pitch:** "AI operations dashboard for a restaurant manager. One connected workflow: complete reservation → generate invoice → mark paid → update finance ledger → analyze feedback → approve recovery. Deterministic backend owns money; AI handles communication and prioritization."

**Tech:** Next.js 16, React 19, TypeScript, Tailwind, Supabase, Recharts  
**What's real:** Full service layer (routes → services → domain rules → queries), Supabase schema with migrations, feedback analysis pipeline, finance transaction creation, webhook dedupe  
**Key lesson:** AI becomes useful only after the deterministic workflow is solid  
**Portfolio angle:** Product workflow design + service architecture + clear AI boundaries  

---

## **Other Active Projects**

- **Arc (Learning Tracker):** Full-stack learning platform with Clerk auth, Neon Postgres, Drizzle ORM, pgvector for retrieval-based tutoring (RAG)
- **Stocks/TradingView:** Data pipeline + indicators for evaluation, not prediction
- **Jarvis (Second Brain):** Personal PKM system—Obsidian vault with computer vision, automated insights, vault OS design
- **Certifications:** Git/GitHub, Generative AI Intermediate; planning NVIDIA AI/ML courses

---

## **Technical Strengths** *(Organized by what matters to networks)*

| What You Do | Tech Stack | Why It Matters |
|---|---|---|
| **Full-stack products** | Next.js, React, TypeScript, Tailwind, Supabase, Postgres | You ship real apps, not tutorials |
| **AI systems** | Claude APIs, RAG, embeddings, pgvector, LLM integration | You understand AI boundaries—not just prompt-chasing |
| **Data & backend** | Postgres, Drizzle ORM, service layers, Rust (BOOM project) | You can model complex workflows |
| **Infrastructure** | Vercel, Docker, AWS (learning), Linux, Git | You can deploy and observe systems |
| **Communication** | Public speaking (ambassador), technical writing, pitch clarity | You can explain work to engineers AND managers |

---

## **What Makes You Stand Out in Conversation**

1. **You think about AI boundaries:** Not "How do I use AI for everything?" but "Where does AI add value safely?" (Resq, OpsPilot both show this)
2. **You ship deterministic truth first:** Forecasts, ledger mutations, financial decisions are calculated—AI is advisory
3. **You document honestly:** You say what's real vs mocked, what broke, why you cut scope
4. **You build workflows, not dashboards:** Your projects solve actual operational problems (cash survival, restaurant management, learning progress)
5. **You're learning while building:** BOOM project shows you can work with research teams; hackathons show you can scope and ship under pressure

---

## **Summer 2026 Plan (If No Internship)**

**Your framework:** One active flagship project, one supporting project, one maintenance lane. Weekly execution, weekly evidence (screenshot/demo/README update).

**Flagship options you're deciding between:**
- **Arc (Learning Tracker)** → prove full-stack + GenAI product engineering
- **Resq** → continue as portfolio masterpiece (fintech + AI systems)
- **TradingView** → data pipeline + evaluation systems

**Also doing:** TA work (CSCI 4041/2041), internship pipeline tracking, freelancing (offer design), reading (Atomic Habits, Stoicism), system design study

---

## **Your Biggest Strengths to Lead With**

When someone asks "What do you do?" lead with:

1. **The BOOM project:** "I'm building Rust middleware for astronomical alert brokering—real-time event tracking and observability in data pipelines." *(Shows: research + systems + real work)*

2. **Your hackathon strategy:** "I built two projects at O1 Summit. The one I'm proud of is Resq—a CFO workspace that generates 13-week cash forecasts. The key insight was keeping the math deterministic and using AI only for advisory." *(Shows: product thinking + architecture + humility)*

3. **Your conviction about AI:** "I'm interested in AI application engineering—not building the models, but building systems where AI sits safely on top of trustworthy logic." *(Shows: discernment + experience)*

---

## **Conversation Starters for Networking**

**If they ask about internships:**  
"I did a web dev internship at NSEdu in Bangalore this summer—built the Assisto platform. Learned a lot about API design and accessible components. Right now I'm exploring what makes a strong student portfolio project."

**If they ask about AI projects:**  
"I've built a couple—OpsPilot (restaurant operations) and Resq (CFO cash forecasting). What I learned is that AI projects are more interesting when you separate what's deterministic from what's AI-driven. That's where you get credibility."

**If they ask what you're working on:**  
"I'm at the point where I'm deciding between deepening one flagship project (like Resq or Arc) vs building several smaller ones. I'm interested in real feedback on that—what looks better to hiring managers or investors you know?"

**If they mention their role/company:**  
Ask: "What does full-stack engineering look like on your team?" or "How do you think about data modeling when you're building for reliability?" *(connects to your strength areas)*

---

## **What You DON'T Want to Say**

- "I'm building an AI [anything]" — too vague. Say what the system *does* first.
- Oversell mocked features as real
- Make it sound like you're job-hunting desperately — position it as "exploring options"
- Forget to mention the non-AI part of your architecture

---

## **Ready for Questions?**

You've got:
✅ Real work to point to (BOOM, internship, hackathons)  
✅ Clear technical story (AI boundaries, deterministic systems, full-stack shipping)  
✅ Honest portfolio narrative (what broke, why you pivoted, what you learned)  
✅ Summer direction (but flexible enough to ask for advice)  

**I'm loaded and ready to answer detailed questions about any of your projects, research, or technical decisions during the meeting.**

What's your first question going to be at the networking event?

*Tools used: ToolSearch, mcp__jarvis__vault_read, Read, mcp__jarvis__vault_list*



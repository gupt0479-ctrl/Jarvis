---
name: obsidian-project-arc
description: Arc Backend project helper
---

You are a specialized assistant for Anant's Arc Backend project.

**Project Overview**:
- **Name**: Arc - Learning Tracker Tool + Backend
- **Type**: Full-stack application
- **Status**: Concept/Planning phase
- **Goal**: Build a learning tracker with AI integration

**Project Description**:
A learning tracker that helps users track their study sessions, create weekly recaps, and eventually integrates AI for content ingestion and Q&A.

**Tech Stack**:
- **Next.js (App Router) + TypeScript**
- **Tailwind CSS + shadcn/ui**
- **Auth**: Clerk
- **DB**: Postgres (Neon preferred)
- **ORM**: Drizzle
- **Charts**: Recharts
- **Deploy**: Vercel
- **AI (later)**: Vercel AI SDK + OpenAI
- **Vector store (later)**: pgvector in Neon Postgres

**MVP Entities (Sprint 1)**:
- **Course**: `{ id, userId, name, goal?, startDate?, createdAt, updatedAt }`
- **Topic**: `{ id, courseId, name, difficulty?, tags?, createdAt, updatedAt }`
- **StudySession**: `{ id, topicId, date, minutes, note?, createdAt }`
- **WeeklyRecap**: `{ id, userId, weekStart, recapText, nextStepsText, createdAt, updatedAt }`

**Optional (Sprint 2)**:
- **DailyStats**: `{ id, userId, date, minutes, sessionCount, xp }`

**Core Features**:
### MVP (Sprint 1)
- Auth (Clerk) + protected routes
- Courses: list/create
- Topics: list/create per course
- Sessions: log time + view history per topic
- Weekly recap: create/view for a week
- Dashboard shell: stats + weekly minutes chart

### Next (Sprint 2)
- Streak + XP (computed from sessions or persisted via DailyStats)
- Browse content tree: Language → Module → Lesson
- Mark lesson complete

### AI Phase (Sprint 3)
- Ingestion script: chunk lesson content → embed → store in pgvector
- Chat: embed question → similarity search → grounded answer → stream
- Persist chats per user

**API Surface**:
### Sprint 1 (Server Actions)
- Courses: create/list
- Topics: create/list
- Sessions: create/list
- Weekly recap: create/view

### API Routes (Later)
- Clerk webhooks
- Streaming AI chat endpoint
- Ingestion endpoints

**When to Use This Skill**:
1. User asks about Arc project
2. User needs help with backend architecture
3. User wants to review MVP scope
4. User needs help with database schema design

**Common Queries**:
- "What's in my Arc project?"
- "Help me design the database schema"
- "Review the MVP scope"
- "What tech stack should I use?"
- "How do I set up authentication?"

**Output Format**:
```markdown
## Arc Project

### Overview
- **Status**: Concept/Planning
- **Type**: Learning Tracker + Backend

### Tech Stack
- Next.js + TypeScript
- Clerk (Auth)
- Neon Postgres + Drizzle

### MVP Schema
| Entity | Fields |
|--------|--------|
| Course | id, userId, name, goal, startDate |
| Topic | id, courseId, name, difficulty |
| Session | id, topicId, date, minutes, note |
| WeeklyRecap | id, userId, weekStart, recapText |

### Next Steps
- [Action items]
```

---
type: concept
course:
status: sprout
mastery (1/10): 0
created:
topics: []
related:
  - "[[40_Resources/CS/Links|Links]]"
---
# Arc Backend
## MOC
- [[Arc (Learning Tracker)]]
- [[HW__ - ...]]
## Definition
- 
## Resources
- 
## Tech stack (keep it simple, ship fast)
- **Next.js (App Router) + TypeScript**
- **Tailwind CSS + shadcn/ui**
- **Auth:** Clerk
- **DB:** Postgres (Neon preferred)
- **ORM:** Drizzle
- **Charts:** Recharts
- **Deploy:** Vercel
- **AI (later):** Vercel AI SDK + OpenAI
- **Vector store (later):** pgvector in Neon Postgres
## Minimum Viable Product
### Product goals
- Ship a working tracker fast with minimal services.
- Secure auth + protected routes.
- Typed DB + clean migrations.
- Server components + server actions by default.
### MVP entities (minimal, scalable)
Auth identity: **User (from Clerk)**  
We do **not** store a full user row in DB in Sprint 1 unless needed later for preferences.
#### Data model (Sprint 1)
- **Course**
  - `{ id, userId, name, goal?, startDate?, createdAt, updatedAt }`
- **Topic**
  - `{ id, courseId, name, difficulty?, tags?, createdAt, updatedAt }`
- **StudySession**
  - `{ id, topicId, date, minutes, note?, createdAt }`
- **WeeklyRecap**
  - `{ id, userId, weekStart, recapText, nextStepsText, createdAt, updatedAt }`
> `userId` is the stable Clerk user id (e.g., `user_...`). Email is not used as an identifier.
#### Optional (Sprint 2, recommended if you want streak/XP fast queries)
- **DailyStats**
  - `{ id, userId, date, minutes, sessionCount, xp }` (unique `(userId, date)`)
## Core features
### MVP (Sprint 1)
- Auth (Clerk) + protected routes
- Courses: list/create
- Topics: list/create per course
- Sessions: log time + view history per topic
- Weekly recap: create/view for a week
- Dashboard shell: stats + weekly minutes chart (Recharts)
### Next (Sprint 2)
- Streak + XP (computed from sessions or persisted via DailyStats)
- Browse content tree:
  - Language → Module → Lesson
- Mark lesson complete
### AI phase (Sprint 3)
- Ingestion script: chunk lesson content → embed → store in pgvector (Neon)
- Chat: embed question → similarity search → grounded answer → stream
- Persist chats per user; optional scoping by course/topic/language/lesson
## API / actions surface
### Sprint 1 (preferred)
Use **server actions** for CRUD (minimal client networking).
- Courses: create/list (update/delete optional)
- Topics: create/list
- Sessions: create/list
- Weekly recap: create/view
### When API routes are used
- Clerk webhooks (optional)
- Streaming AI chat endpoint (later)
- Any ingestion endpoints (usually script-based instead)
### Why pgvector (not Pinecone) for MVP
One database keeps ops simple: the same Neon Postgres stores relational rows + vectors. Add a dedicated vector DB only if scale demands it later.
## Repo structure

## Common mistakes
- 
## Mini-test (answer without looking)
- [ ] Flashcards
- [ ] 
## Flashcards (best 3–8)


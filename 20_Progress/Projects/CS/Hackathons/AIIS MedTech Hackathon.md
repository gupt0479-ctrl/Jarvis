---
type: project
status: active
created: 2026-04-27
tags:
  - hackathon
  - medtech
  - planning
related:
  - "[[01_Summit]]"
  - "[[Opspilot]]"
  - "[[Resq]]"
  - "[[Mentor Details]]"
  - "[[Mentorship Board]]"
---
# AIIS MedTech Hackathon
## Problem Statement
### What’s happening
During natural disasters, individuals with disabilities face two layers of risk: 
- Immediate danger from the disaster itself 
- Loss of access to critical, life-sustaining infrastructure 
Power outages disrupt medical devices (ventilators, oxygen, refrigeration) 
Communication systems are often inaccessible or delayed
Emergency response lacks visibility into specialized needs 
- Life-threatening gaps in care and support
- Delayed or misprioritized aid
- Loss of independence and increased vulnerability
### The Opportunity
Build an AI-powered solution that:
- Helps individuals stay safe and independent
- Enables responders to prioritize specialized aid in real time 
Prototype an app, dashboard, or alert system.
Use synthetic or public data to simulate disaster scenarios.
Demonstrate clear impact through intelligent decision-making
### Judging Criteria
**Real Impact**
- Does this meaningfully help someone in a high-stakes situation? 
**Strong Execution**
- Is there a clear, working approach behind the idea? 
**Inclusive by Design**
- Can the people who need this actually use it?
**Original Thinking**
- Is this a thoughtful, non-obvious solution? 
**Practical Potential**
- Could this exist beyond today?
*Bottom line*: Build something that matters, works, and can be used when it counts.
### Problem
> [!PROBLEM] The strongest problem is: **During disasters, disabled people do not just need “help.” They need the right help, at the right place, before one dependency fails.** 
> - That dependency might be oxygen, a ventilator battery, elevator access, wheelchair transport, insulin refrigeration, ASL/text communication, a caregiver, or a safe shelter that is actually accessible.

==Build==: So the one thing I would build around is: **“Need visibility before failure.”**. Responders need a live, location-aware **needs graph**, not just a list of 911 calls. AI turns disability-specific disaster needs into a live triage map so responders know who needs power, transport, medicine, communication support, or accessible shelter first.

==Data==: The National Weather Service provides free API access to alerts, forecasts, and observations, so you can use real weather-alert structure even if your incident is simulated. HHS emPOWER gives de-identified state/county/ZIP-level counts for Medicare beneficiaries using electricity-dependent durable medical equipment and essential health services, which is exactly the kind of public data your project can reference. HHS also says emPOWER covers over 4.6 million independently living at-risk Medicare beneficiaries who rely on electricity-dependent equipment/devices or essential health services.
## Agents
1. *Agent 1*: Alert Intake Agent: Reads weather/disaster alert and identifies impacted ZIPs.
2. *Agent 2*: Need Extraction Agent: Turns free text into structured needs:
```json
{
  "medical_power": true,
  "device": "oxygen concentrator",
  "battery_hours": 2,
  "mobility": "wheelchair",
  "communication": "text_only",
  "evacuation_barrier": "elevator_out"
}
```
3. *Agent 3*: Triage Agent: Ranks cases using rules + AI explanation.
4. *Agent 4*: Resource Matching Agent: Matches person to accessible shelter, power hub, transport, caregiver, or medical supply.
5. *Agent 5*: Communication Agent: Writes the message in the person’s preferred format.
# Judging criteria map

|Criteria|How NeedBeacon wins|
|---|---|
|Real Impact|Finds people before oxygen, batteries, meds, transport, or caregiver support fails.|
|Strong Execution|Working dashboard, map, risk queue, check-in flow, AI extraction, and resource matching.|
|Inclusive by Design|SMS-first, large buttons, screen-reader friendly, text-only mode, caregiver mode.|
|Original Thinking|Focuses on “dependency failure countdown,” not generic disaster alerts.|
|Practical Potential|Uses existing public datasets, emergency registries, shelter lists, and responder workflows.|
# The exact pitch angle
> Use this framing: **“Disasters are usually mapped by hazard: fire zones, flood zones, outage zones. But disabled people are harmed when hazards intersect with dependencies. NeedBeacon maps the dependency layer.”**

Then show:
- Person A has 8 hours of battery → medium priority
- Person B has 1 hour oxygen + no caregiver → critical
- Person C is safe but needs accessible shelter tomorrow → lower priority
- Person D is deaf and only received voice evacuation notice → communication alert needed
This shows “intelligent decision-making” clearly.
## MVP Scope
### Must-have
- Patient profile with synthetic demo data.
- Daily symptom check-in form.
- Medication adherence log.
- Appointment questions list.
- Timeline of recent entries.
- AI-generated visit brief: symptom trends, adherence notes, patient questions, "ask your clinician" discussion prompts.
- Clear disclaimer: not medical advice, not emergency support.
### Should-have
- Export/share view for the appointment summary.
- Severity trend chart.
- Tagging for triggers or lifestyle factors.
- Caregiver note field.
- Simple audit trail showing what entries were used in the summary.
### Nice-to-have
- Voice-to-note capture.
- Calendar reminders.
- PDF generation.
- Clinician dashboard.
- Sponsor API integration if relevant.
### Cut explicitly
Diagnosis prediction. Medication change recommendations. Emergency triage. Real EHR integration. Real PHI storage. Complex multi-provider workflow. Overly broad disease coverage.
## Tech Stack
| Layer | Tools |
|---|---|
| Frontend | Next.js, React, TypeScript, Tailwind, shadcn-style components |
| Backend | Next.js route handlers |
| Database | Supabase Postgres |
| AI | LLM structured summary generation from user logs; JSON/schema-constrained output if possible |
| Deploy | Vercel |
| Auth | Supabase Auth or demo-only login; no real patient data |
## Risks
### Privacy and regulatory
- Do not collect or use real health data during the demo.
- Do not claim HIPAA compliance unless actually implemented.
- Make it clear this is a prototype using synthetic data.
### Fake-medical-advice risk
Avoid diagnosis, treatment recommendations, medication changes. Phrase outputs as "summary" and "questions to discuss with a clinician."
### Data quality
Patient-entered logs may be incomplete or biased. AI summaries can overstate patterns if data is sparse. The UI should show source entries used in the summary.
### Demo risk
AI generation may be slow or inconsistent. Use deterministic fallback summaries from the same structured data. Seed a strong demo patient with a realistic week of entries.
### Scope risk
Medtech ideas easily become too ambitious. The MVP stays focused on one workflow: appointment preparation.
## Execution Plan
### Pre-hackathon
- Choose the medtech track early.
- Validate 2–3 ideas with sponsors or mentors before building.
- Read sponsor API docs and pick one flagship integration at most.
- Prepare synthetic patient data.
- Draft the judging rubric map before coding.
- Decide team roles: product/pitch, frontend, backend/data, AI/integration.
### First 6 hours
- Scaffold Next.js app and core routes.
- Create Supabase schema: patient, logs, medications, appointments, summaries.
- Build main form and timeline.
- Deploy a basic version quickly.
### Middle build
- Implement AI visit-brief generator.
- Add charts and source-linked summary.
- Add privacy disclaimer and safe language.
- Build one polished demo patient flow.
### Final polish
- First screen is the actual usable app, not a landing page.
- Add empty/loading/error states.
- Rehearse the demo path.
- Create a backup recording.
### Demo strategy
1. Patient has scattered symptoms and questions.
2. Patient logs a few entries.
3. App turns logs into a visit brief.
4. Brief shows source-linked, non-diagnostic summaries.
5. Patient walks into the appointment more prepared.
## Questions for [[Mentor Details|Ahnaf]]
1. Is a care companion / visit-prep summarizer a strong enough hackathon idea, or does it need a more technical hook?
2. How can I make the architecture look mature without overbuilding?
3. Would engineering managers care more about the AI summary quality, the data model, or the privacy boundaries?
4. What is the best way to explain "not medical advice" without making the product sound weak?
5. Should I build patient-facing, clinician-facing, or caregiver-facing first?
6. What would make this feel like a real product demo instead of a class project?
7. What system design patterns should I use: audit trail, role-based access, queue, event log, or document generation?
8. How can I make this more career-useful than just another hackathon submission?
## Decision Log
### Current thinking
Build a focused care companion that turns daily patient logs into a clinician-ready visit brief. Keep the AI role limited to summarization, organization, and communication.
### Open questions
- Which disorder or condition should the demo focus on?
- Will sponsors provide a useful integration?
- Should the demo be patient-facing or clinician-facing?
- How much privacy/auth infrastructure is worth building during the hackathon?
### Next decision after talking to [[Mentor Details|Ahnaf]]
Decide the target user and exact demo workflow before writing code.

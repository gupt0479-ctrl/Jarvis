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
# 
## MOC
- [[W__ L__ - ...]]
- [[HW__ - ...]]
## Definition
- 
## Resources
- [Handbook](https://o1summit.notion.site/handbook)
- [Build Track Details](https://www.notion.so/o1summit/Tracks-In-Depth-3408b9dcbd4a817fb304eb736afbcb9d)
- 
#### For building
- [Vercel Agent skills](https://github.com/vercel-labs/agent-skills/tree/main/skills)
- [TinyFish](https://www.tinyfish.ai/)
- AWS Credits Information
- 
### How to use them
1. 
## Vibe Coding
### Before Hackathon
- Set up agent skills across all coding platforms.
- Figure out how to use AWS correctly throughout this project. 
-

## Slide 3 — THE SOLUTION
1. *Cash Truth: Cash Truth — Cleared ledger facts only. No AI-invented balances. Deterministic from day one.*
Talking points
- “We start from one rule: if a transaction has not cleared the ledger, it does not count. That keeps the foundation simple and trustworthy.”
- “Our finance_transactions table in Supabase is the single source of truth for cash movement. Every row has a clear direction — in or out — and a category such as revenue, expense, refund, or fee.”
- “We also protect the ledger at the database level. A unique index on (invoice_id, type, direction) blocks duplicate revenue entries before they can ever affect the balance.”
- “Current cash is calculated by summing all cleared transactions up to the selected date. It is a pure function: same inputs, same result, every single time.”
- “That means there is no guessing in the historical layer. No model is estimating balances for us. No assistant is filling in gaps. The ledger decides the answer.”
- “This is important because trust in the forecast starts with trust in the starting point. If the current position is wrong, every future week is wrong too.”
- “So our first promise is simple: the past and present are grounded in recorded facts, not generated output.”
1. *13-Week Forecast: 13-Week Forecast — Rule-based weekly waterfall. Explicit assumptions. Replayable and fully auditable.*
Talking points
- “Once we have the starting balance, we project forward using a 13-week waterfall. Each week runs Monday through Sunday so the view matches how operators usually think about payroll, vendor payments, and weekly planning.”
- “Every week contains four core pieces: opening balance, inflows, outflows, and closing balance.”
- “Inflows come from cash_receivables, and each receivable is weighted by a confidence score so expected collections are not treated as guaranteed.”
- “Outflows come from cash_obligations, plus trailing 8-week category averages for recurring costs that tend to show up again.”
- “The weekly formula is straightforward: closing = opening + inflows - outflows - refund_exposure.”
- “We also run three scenarios so the user is not looking at only one path. Base uses a 1.0x multiplier, stress uses 0.82x, and upside uses 1.12x.”
- “That multiplier only affects inflows. We leave outflows deterministic, because rent, payroll, and fixed commitments do not shrink just because the forecast is optimistic.”
- “From there, breakpoint detection scans the weeks and finds the first one where the closing balance drops below the threshold.”
- “That gives the operator a very specific answer: not just ‘you may have a problem soon,’ but ‘this is the exact week where pressure becomes critical.’”
- “Every run is also hashed with SHA-256, then compared to the previous run. If the result changes — for example, if the breakpoint moves earlier — we capture that change in the audit trail automatically.”
- “So the forecast is not a black box. It is explicit, repeatable, and easy to inspect.”
1. *Action Queue:  Action Queue — Ranked CFO moves: accelerate collections, defer payments, explore bridge financing.*
Talking points
- “Once the forecast identifies pressure, we translate it into actions. This is where the product becomes operational rather than just analytical.”
- “The action queue is generated deterministically from forecast output. It is not a free-form AI suggestion list.”
- “We currently rank four action types: accelerate collections on slipping receivables, defer obligations that can safely move by two weeks, reduce discretionary spend when the breakpoint is close, and surface bridge financing when the shortfall is large enough.”
- “Each action is presented with a structured decision frame: expected impact range, speed to effect in days, risk level, and confidence score.”
- “That structure matters because operators do not just need ideas — they need to know what is fast, what is safe, and what is likely to help the most.”
- “Bridge financing is intentionally advisory only. It is marked executable: false, because we never want the system taking external financing steps automatically.”
- “That separation is one of our core design rules: AI can investigate and advise, but it does not change balances, it does not rewrite forecast math, and it does not execute high-stakes financial actions.”
- “In our architecture, AI lives in the research layer — things like TinyFish search, external signal gathering, and summarization.”
- “The calculation layer is pure TypeScript. That line between math and advice is what keeps the product both useful and credible.”
## Slide 7 — TRACTION & MILESTONES
Built in 24 hours. Ready to scale.
COMPLETE: Deterministic cash engine
Deterministic cash engine — COMPLETE
Talking points
- “The foundation is already in place. Our core ledger is backed by 10 Supabase migrations and enforced directly at the database level.”
- “We have finance_transactions with idempotency protections, cash_obligations with 8 categories and 6 recurrence patterns, cash_receivables with confidence scoring and collection lag tracking, and refund_exposure with its own status workflow.”
- “All amounts use NUMERIC(12,2), and the schema uses CHECK constraints to keep invalid states out of the system.”
- “That means correctness is not just a frontend claim. It is enforced where the data actually lives.”
## COMPLETE: 13-week forecast with breakpoint detection
Talking points
- “The forecast engine itself is already working as a self-contained deterministic module.”
- “It is roughly 350 lines of pure TypeScript with three scenario modes, a trailing 8-week baseline, 13 weekly buckets, and itemized inflow and outflow detail.”
- “It also includes automatic breakpoint detection, dynamic threshold calculation, SHA-256 payload hashing for deviation tracking, and full audit logging into ai_actions.”
- “We also export core functions like detectPure() and computeDeviation() for property testing, which gives us confidence that the forecast behaves consistently as inputs change.”
## COMPLETE: Ranked action queue + CFO move library
Talking points
- “On top of the forecast, we already have a structured action system.”
- “Each action includes impact range, speed to effect, risk level, confidence score, executable flag, and guidance text.”
- “We also extended the collections side with trajectory analysis, LTV-weighted escalation, legal and timing guardrails, high-stakes checks, portal reconnaissance, and external signal enrichment through TinyFish.”
- “So the output is not just ‘here are some ideas.’ It is a ranked, constrained set of next steps.”
## COMPLETE: Supabase audit trail with hash chaining
Talking points
- “Every important system step is auditable.”
- “All agent actions go through recordAiAction(), which is idempotent and can safely handle replayed triggers.”
- “Forecast runs store both payloadHash and prevPayloadHash, which gives us chain verification across runs.”
- “cash_forecast_snapshots stores full JSONB forecast payloads, so we can compare one run to the next and explain exactly what changed.”
- “And the ?view=audit endpoint exposes the full timeline with timestamps, so the user can inspect the history rather than just trust the latest screen.”
## IN PROGRESS: CSV & XLSX spreadsheet import
CSV & XLSX spreadsheet import — IN PROGRESS
Talking points
- “The next step is spreadsheet import, because that is how many finance teams actually work today.”
- “Right now the demo uses seeded configuration in cash-forecast-config.ts so we can guarantee a stable and repeatable flow.”
- “The import path will map CSV and XLSX files into the same cash_obligations and cash_receivables tables the engine already uses.”
- “That means we are not building a separate demo-only path. We are extending the real system entrypoint.”
- “The schema is already prepared for this. What remains is the parser, validation layer, and upload experience.”
## The Ask
We’re raising $1M pre-seed, targeting 10 early design partners, Q3 ’26 public beta.
Talking points
- “What we are showing is not just a concept deck. It is a working system with clear rules, strong data constraints, and a path to production.”
- “The stack is already set up for serious use: Supabase with RLS, Next.js on App Runner, Drizzle ORM with typed schemas, and three TinyFish modes — mock, misconfigured, and live — so the system remains stable in both demo and real environments.”
- “Most importantly, the architecture reflects how finance software actually earns trust: deterministic calculations first, explicit assumptions second, advisory intelligence on top.”
- “That is the reason this can grow from a hackathon build into something real for finance teams.”
## Common mistakes
- 
## Mini-test (answer without looking)
- [ ] Flashcards
- [ ] 
## Flashcards (best 3–8)


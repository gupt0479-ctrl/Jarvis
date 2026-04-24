# context

**Description:** Summarize current state from relevant vault areas — projects, inbox, progress notes, and recent activity.

**Usage:** `/context` or "What's my current context?"

---

## Instructions

When this skill is invoked:

### 1. Scan Key Areas

Read the following to build a picture of current state:

**Active Projects (`20_Progress/`):**
- List all `.md` files
- Extract `status:`, `deadline:`, `next:` from frontmatter
- Note any stalled projects (no `next` action)

**Inbox (`00_Inbox/`):**
- Check `00_Inbox/Inbox Board.md` for Dataview results
- Identify unprocessed thoughts and brainstorms

**Current Studies (`10_UMN/`):**
- List active course boards
- Note any upcoming exams or assignments mentioned

**Recent Claude Activity (`60_Claude/`):**
- Read last 5 entries from `60_Claude/10_Session_Logs/log.md`
- Check what's been worked on recently

**Recent Clippings (`60_Claude/05_Clippings/`):**
- List files modified in last 7 days
- Check if any need ingestion

### 2. Build the Summary

Create a response structured as:

```markdown
## Current State Summary

### Active Projects (20_Progress/)

| Project | Status | Next Action |
|---------|--------|-------------|
| [Name] | [status] | [next or "⚠️ No next action"] |

### Inbox Items Needing Attention (00_Inbox/)

- [X unprocessed thoughts]
- [Y unprocessed brainstorms]

### Current Courses (10_UMN/)

- [Course 1] — [any upcoming deadlines]
- [Course 2] — [any upcoming deadlines]

### Recent Claude Activity

- [Recent session 1]
- [Recent session 2]

### Clippings Pending Ingestion

- [File 1] — [date]
- [File 2] — [date]

---

## Suggested Next Actions

1. [Highest priority based on deadlines/status]
2. [Second priority]
3. [Third priority]

## Questions to Consider

- [Question about stalled projects]
- [Question about priorities]
```

### 3. Offer Follow-Up Commands

Suggest relevant next steps:

- "Run `/today` to build a realistic plan"
- "Run `/ingest-clipping` to process pending sources"
- "Run `/weekly-review` to reflect on recent progress"

---

## Safety Constraints

- **Read-only operation** — This skill only reads, never writes
- **Respect privacy** — Don't surface sensitive info unless user asks
- **Be honest about gaps** — If info is missing, say so; don't fabricate

---

## Example Output

```markdown
## Current State Summary

### Active Projects

| Project | Status | Next Action |
|---------|--------|-------------|
| [[Freelancing]] | seed | ⚠️ No next action |
| [[Mentorship Program]] | sprout | [[Mentor Details]] |
| [[UROP]] | sprout | [[BOOM Board]] |
| [[Projects]] | tree | [[Cleaning Laptop]] |

### Inbox Items

- 3 unprocessed thoughts in `00_Inbox/`
- 1 unprocessed brainstorm

### Current Courses

- [[CSCI 2041]] — No deadlines noted
- [[MGMT 3001]] — No deadlines noted
- [[MUS 1013]] — Week 1 covered

### Recent Claude Activity

- [2026-04-08] Vault system initialization

### Clippings Pending

- `Kairo — Know What's Coming.md` — 2026-03-28
- `AI Training Jobs...md` — 2026-03-27

---

## Suggested Next Actions

1. Process pending clippings (2 items)
2. Define next action for Freelancing project
3. Review inbox items

## Questions

- What's the priority between UROP, mentorship, and freelancing?
- Should we ingest those clippings now?
```

---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: wsl
title: "Skills and subagents for portfolio"
started_at: 2026-03-08T07:48:46
ended_at: 2026-03-08T08:30:56
exported_at: 2026-07-30T19:56:24
project: portfolio
cwd: "/home/anant_gupta/projects/portfolio"
session_id: 8622f294-59a2-4139-a79b-e05e95af91ae
status: raw
turn_count: 4
tools_used:
files_changed_count: 6
lines_added: 182
lines_removed: 0
tags:
  - input
  - ai-conversation
  - cursor
  - wsl
---

# Skills and subagents for portfolio

## You

<manually_attached_skills>
The user has manually attached the following skills to their message.
These skills contain specific instructions or workflows that the user wants you to follow for this request.
You should read and follow the instructions in these skills carefully.

Skill Name: create-skill
Path: \home\anant_gupta\.cursor\skills-cursor\create-skill\SKILL.md
SKILL.md content:
# Creating Skills in Cursor

This skill guides you through creating effective Agent Skills for Cursor. Skills are markdown files that teach the agent how to perform specific tasks: reviewing PRs using team standards, generating commit messages in a preferred format, querying database schemas, or any specialized workflow.

## Before You Begin: Gather Requirements

Before creating a skill, gather essential information from the user about:

1. **Purpose and scope**: What specific task or workflow should this skill help with?
2. **Target location**: Should this be a personal skill (~/.cursor/skills/) or project skill (.cursor/skills/)?
3. **Trigger scenarios**: When should the agent automatically apply this skill?
4. **Key domain knowledge**: What specialized information does the agent need that it wouldn't already know?
5. **Output format preferences**: Are there specific templates, formats, or styles required?
6. **Existing patterns**: Are there existing examples or conventions to follow?

### Inferring from Context

If you have previous conversation context, infer the skill from what was discussed. You can create skills based on workflows, patterns, or domain knowledge that emerged in the conversation.

### Gathering Additional Information

If you need clarification, use the AskQuestion tool when available:

```
Example AskQuestion usage:
- "Where should this skill be stored?" with options like ["Personal (~/.cursor/skills/)", "Project (.cursor/skills/)"]
- "Should this skill include executable scripts?" with options like ["Yes", "No"]
```

If the AskQuestion tool is not available, ask these questions conversationally.

---

## Skill File Structure

### Directory Layout

Skills are stored as directories containing a `SKILL.md` file:

```
skill-name/
├── SKILL.md              # Required - main instructions
├── reference.md          # Optional - detailed documentation
├── examples.md           # Optional - usage examples
└── scripts/              # Optional - utility scripts
    ├── validate.py
    └── helper.sh
```

### Storage Locations

| Type | Path | Scope |
|------|------|-------|
| Personal | ~/.cursor/skills/skill-name/ | Available across all your projects |
| Project | .cursor/skills/skill-name/ | Shared with anyone using the repository |

**IMPORTANT**: Never create skills in `~/.cursor/skills-cursor/`. This directory is reserved for Cursor's internal built-in skills and is managed automatically by the system.

### SKILL.md Structure

Every skill requires a `SKILL.md` file with YAML frontmatter and markdown body:

```markdown
---
name: your-skill-name
description: Brief description of what this skill does and when to use it
---

# Your Skill Name

## Instructions
Clear, step-by-step guidance for the agent.

## Examples
Concrete examples of using this skill.
```

### Required Metadata Fields

| Field | Requirements | Purpose |
|-------|--------------|---------|
| `name` | Max 64 chars, lowercase letters/numbers/hyphens only | Unique identifier for the skill |
| `description` | Max 1024 chars, non-empty | Helps agent decide when to apply the skill |

---

## Writing Effective Descriptions

The description is **critical** for skill discovery. The agent uses it to decide when to apply your skill.

### Description Best Practices

1. **Write in third person** (the description is injected into the system prompt):
   - ✅ Good: "Processes Excel files and generates reports"
   - ❌ Avoid: "I can help you process Excel files"
   - ❌ Avoid: "You can use this to process Excel files"

2. **Be specific and include trigger terms**:
   - ✅ Good: "Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."
   - ❌ Vague: "Helps with documents"

3. **Include both WHAT and WHEN**:
   - WHAT: What the skill does (specific capabilities)
   - WHEN: When the agent should use it (trigger scenarios)

### Description Examples

```yaml
# PDF Processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.

# Excel Analysis
description: Analyze Excel spreadsheets, create pivot tables, generate charts. Use when analyzing Excel files, spreadsheets, tabular data, or .xlsx files.

# Git Commit Helper
description: Generate descriptive commit messages by analyzing git diffs. Use when the user asks for help writing commit messages or reviewing staged changes.

# Code Review
description: Review code for quality, security, and best practices following team standards. Use when reviewing pull requests, code changes, or when the user asks for a code review.
```

---

## Core Authoring Principles

### 1. Concise is Key

The context window is shared with conversation history, other skills, and requests. Every token competes for space.

**Default assumption**: The agent is already very smart. Only add context it doesn't already have.

Challenge each piece of information:
- "Does the agent really need this explanation?"
- "Can I assume the agent knows this?"
- "Does this paragraph justify its token cost?"

**Good (concise)**:
```markdown
## Extract PDF text

Use pdfplumber for text extraction:

\`\`\`python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
\`\`\`
```

**Bad (verbose)**:
```markdown
## Extract PDF text

PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available for PDF processing, but we
recommend pdfplumber because it's easy to use and handles most cases well...
```

### 2. Keep SKILL.md Under 500 Lines

For optimal performance, the main SKILL.md file should be concise. Use progressive disclosure for detailed content.

### 3. Progressive Disclosure

Put essential information in SKILL.md; detailed reference material in separate files that the agent reads only when needed.

```markdown
# PDF Processing

## Quick start
[Essential instructions here]

## Additional resources
- For complete API details, see [reference.md](reference.md)
- For usage examples, see [examples.md](examples.md)
```

**Keep references one level deep** - link directly from SKILL.md to reference files. Deeply nested references may result in partial reads.

### 4. Set Appropriate Degrees of Freedom

Match specificity to the task's fragility:

| Freedom Level | When to Use | Example |
|---------------|-------------|---------|
| **High** (text instructions) | Multiple valid approaches, context-dependent | Code review guidelines |
| **Medium** (pseudocode/templates) | Preferred pattern with acceptable variation | Report generation |
| **Low** (specific scripts) | Fragile operations, consistency critical | Database migrations |

---

## Common Patterns

### Template Pattern

Provide output format templates:

```markdown
## Report structure

Use this template:

\`\`\`markdown
# [Analysis Title]

## Executive summary
[One-paragraph overview of key findings]

## Key findings
- Finding 1 with supporting data
- Finding 2 with supporting data

## Recommendations
1. Specific actionable recommendation
2. Specific actionable recommendation
\`\`\`
```

### Examples Pattern

For skills where output quality depends on seeing examples:

```markdown
## Commit message format

**Example 1:**
Input: Added user authentication with JWT tokens
Output:
\`\`\`
feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware
\`\`\`

**Example 2:**
Input: Fixed bug where dates displayed incorrectly
Output:
\`\`\`
fix(reports): correct date formatting in timezone conversion

Use UTC timestamps consistently across report generation
\`\`\`
```

### Workflow Pattern

Break complex operations into clear steps with checklists:

```markdown
## Form filling workflow

Copy this checklist and track progress:

\`\`\`
Task Progress:
- [ ] Step 1: Analyze the form
- [ ] Step 2: Create field mapping
- [ ] Step 3: Validate mapping
- [ ] Step 4: Fill the form
- [ ] Step 5: Verify output
\`\`\`

**Step 1: Analyze the form**
Run: \`python scripts/analyze_form.py input.pdf\`
...
```

### Conditional Workflow Pattern

Guide through decision points:

```markdown
## Document modification workflow

1. Determine the modification type:

   **Creating new content?** → Follow "Creation workflow" below
   **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow:
   - Use docx-js library
   - Build document from scratch
   ...
```

### Feedback Loop Pattern

For quality-critical tasks, implement validation loops:

```markdown
## Document editing process

1. Make your edits
2. **Validate immediately**: \`python scripts/validate.py output/\`
3. If validation fails:
   - Review the error message
   - Fix the issues
   - Run validation again
4. **Only proceed when validation passes**
```

---

## Utility Scripts

Pre-made scripts offer advantages over generated code:
- More reliable than generated code
- Save tokens (no code in context)
- Save time (no code generation)
- Ensure consistency across uses

```markdown
## Utility scripts

**analyze_form.py**: Extract all form fields from PDF
\`\`\`bash
python scripts/analyze_form.py input.pdf > fields.json
\`\`\`

**validate.py**: Check for errors
\`\`\`bash
python scripts/validate.py fields.json
# Returns: "OK" or lists conflicts
\`\`\`
```

Make clear whether the agent should **execute** the script (most common) or **read** it as reference.

---

## Anti-Patterns to Avoid

### 1. Windows-Style Paths
- ✅ Use: `scripts/helper.py`
- ❌ Avoid: `scripts\helper.py`

### 2. Too Many Options
```markdown
# Bad - confusing
"You can use pypdf, or pdfplumber, or PyMuPDF, or..."

# Good - provide a default with escape hatch
"Use pdfplumber for text extraction.
For scanned PDFs requiring OCR, use pdf2image with pytesseract instead."
```

### 3. Time-Sensitive Information
```markdown
# Bad - will become outdated
"If you're doing this before August 2025, use the old API."

# Good - use an "old patterns" section
## Current method
Use the v2 API endpoint.

## Old patterns (deprecated)
<details>
<summary>Legacy v1 API</summary>
...
</details>
```

### 4. Inconsistent Terminology
Choose one term and use it throughout:
- ✅ Always "API endpoint" (not mixing "URL", "route", "path")
- ✅ Always "field" (not mixing "box", "element", "control")

### 5. Vague Skill Names
- ✅ Good: `processing-pdfs`, `analyzing-spreadsheets`
- ❌ Avoid: `helper`, `utils`, `tools`

---

## Skill Creation Workflow

When helping a user create a skill, follow this process:

### Phase 1: Discovery

Gather information about:
1. The skill's purpose and primary use case
2. Storage location (personal vs project)
3. Trigger scenarios
4. Any specific requirements or constraints
5. Existing examples or patterns to follow

If you have access to the AskQuestion tool, use it for efficient structured gathering. Otherwise, ask conversationally.

### Phase 2: Design

1. Draft the skill name (lowercase, hyphens, max 64 chars)
2. Write a specific, third-person description
3. Outline the main sections needed
4. Identify if supporting files or scripts are needed

### Phase 3: Implementation

1. Create the directory structure
2. Write the SKILL.md file with frontmatter
3. Create any supporting reference files
4. Create any utility scripts if needed

### Phase 4: Verification

1. Verify the SKILL.md is under 500 lines
2. Check that the description is specific and includes trigger terms
3. Ensure consistent terminology throughout
4. Verify all file references are one level deep
5. Test that the skill can be discovered and applied

---

## Complete Example

Here's a complete example of a well-structured skill:

**Directory structure:**
```
code-review/
├── SKILL.md
├── STANDARDS.md
└── examples.md
```

**SKILL.md:**
```markdown
---
name: code-review
description: Review code for quality, security, and maintainability following team standards. Use when reviewing pull requests, examining code changes, or when the user asks for a code review.
---

# Code Review

## Quick Start

When reviewing code:

1. Check for correctness and potential bugs
2. Verify security best practices
3. Assess code readability and maintainability
4. Ensure tests are adequate

## Review Checklist

- [ ] Logic is correct and handles edge cases
- [ ] No security vulnerabilities (SQL injection, XSS, etc.)
- [ ] Code follows project style conventions
- [ ] Functions are appropriately sized and focused
- [ ] Error handling is comprehensive
- [ ] Tests cover the changes

## Providing Feedback

Format feedback as:
- 🔴 **Critical**: Must fix before merge
- 🟡 **Suggestion**: Consider improving
- 🟢 **Nice to have**: Optional enhancement

## Additional Resources

- For detailed coding standards, see [STANDARDS.md](STANDARDS.md)
- For example reviews, see [examples.md](examples.md)
```

---

## Summary Checklist

Before finalizing a skill, verify:

### Core Quality
- [ ] Description is specific and includes key terms
- [ ] Description includes both WHAT and WHEN
- [ ] Written in third person
- [ ] SKILL.md body is under 500 lines
- [ ] Consistent terminology throughout
- [ ] Examples are concrete, not abstract

### Structure
- [ ] File references are one level deep
- [ ] Progressive disclosure used appropriately
- [ ] Workflows have clear steps
- [ ] No time-sensitive information

### If Including Scripts
- [ ] Scripts solve problems rather than punt
- [ ] Required packages are documented
- [ ] Error handling is explicit and helpful
- [ ] No Windows-style paths

---

Skill Name: create-subagent
Path: \home\anant_gupta\.cursor\skills-cursor\create-subagent\SKILL.md
SKILL.md content:
# Creating Custom Subagents

This skill guides you through creating custom subagents for Cursor. Subagents are specialized AI assistants that run in isolated contexts with custom system prompts.

## When to Use Subagents

Subagents help you:
- **Preserve context** by isolating exploration from your main conversation
- **Specialize behavior** with focused system prompts for specific domains
- **Reuse configurations** across projects with user-level subagents

### Inferring from Context

If you have previous conversation context, infer the subagent's purpose and behavior from what was discussed. Create the subagent based on specialized tasks or workflows that emerged in the conversation.

## Subagent Locations

| Location | Scope | Priority |
|----------|-------|----------|
| `.cursor/agents/` | Current project | Higher |
| `~/.cursor/agents/` | All your projects | Lower |

When multiple subagents share the same name, the higher-priority location wins.

**Project subagents** (`.cursor/agents/`): Ideal for codebase-specific agents. Check into version control to share with your team.

**User subagents** (`~/.cursor/agents/`): Personal agents available across all your projects.

## Subagent File Format

Create a `.md` file with YAML frontmatter and a markdown body (the system prompt):

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```

### Required Fields

| Field | Description |
|-------|-------------|
| `name` | Unique identifier (lowercase letters and hyphens only) |
| `description` | When to delegate to this subagent (be specific!) |

## Writing Effective Descriptions

The description is **critical** - the AI uses it to decide when to delegate.

```yaml
# ❌ Too vague
description: Helps with code

# ✅ Specific and actionable
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
```

Include "use proactively" to encourage automatic delegation.

## Example Subagents

### Code Reviewer

```markdown
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is clear and readable
- Functions and variables are well-named
- No duplicated code
- Proper error handling
- No exposed secrets or API keys
- Input validation implemented
- Good test coverage
- Performance considerations addressed

Provide feedback organized by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific examples of how to fix issues.
```

### Debugger

```markdown
---
name: debugger
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works

Debugging process:
- Analyze error messages and logs
- Check recent code changes
- Form and test hypotheses
- Add strategic debug logging
- Inspect variable states

For each issue, provide:
- Root cause explanation
- Evidence supporting the diagnosis
- Specific code fix
- Testing approach
- Prevention recommendations

Focus on fixing the underlying issue, not the symptoms.
```

### Data Scientist

```markdown
---
name: data-scientist
description: Data analysis expert for SQL queries, BigQuery operations, and data insights. Use proactively for data analysis tasks and queries.
---

You are a data scientist specializing in SQL and BigQuery analysis.

When invoked:
1. Understand the data analysis requirement
2. Write efficient SQL queries
3. Use BigQuery command line tools (bq) when appropriate
4. Analyze and summarize results
5. Present findings clearly

Key practices:
- Write optimized SQL queries with proper filters
- Use appropriate aggregations and joins
- Include comments explaining complex logic
- Format results for readability
- Provide data-driven recommendations

For each analysis:
- Explain the query approach
- Document any assumptions
- Highlight key findings
- Suggest next steps based on data

Always ensure queries are efficient and cost-effective.
```

## Subagent Creation Workflow

### Step 1: Decide the Scope

- **Project-level** (`.cursor/agents/`): For codebase-specific agents shared with team
- **User-level** (`~/.cursor/agents/`): For personal agents across all projects

### Step 2: Create the File

```bash
# For project-level
mkdir -p .cursor/agents
touch .cursor/agents/my-agent.md

# For user-level
mkdir -p ~/.cursor/agents
touch ~/.cursor/agents/my-agent.md
```

### Step 3: Define Configuration

Write the frontmatter with the required fields (`name` and `description`).

### Step 4: Write the System Prompt

The body becomes the system prompt. Be specific about:
- What the agent should do when invoked
- The workflow or process to follow
- Output format and structure
- Any constraints or guidelines

### Step 5: Test the Agent

Ask the AI to use your new agent:

```
Use the my-agent subagent to [task description]
```

## Best Practices

1. **Design focused subagents**: Each should excel at one specific task
2. **Write detailed descriptions**: Include trigger terms so the AI knows when to delegate
3. **Check into version control**: Share project subagents with your team
4. **Use proactive language**: Include "use proactively" in descriptions

## Troubleshooting

### Subagent Not Found
- Ensure file is in `.cursor/agents/` or `~/.cursor/agents/`
- Check file has `.md` extension
- Verify YAML frontmatter syntax is valid
</manually_attached_skills>
<user_query>
/create-skill /create-subagent I need your help creating skills and subagents for this portfolio based on everything that you can grasp about the current codebase. I need you to create these agents in such a way that i completely finish this portfolio looking amazing. 
</user_query>

## Cursor

Exploring the portfolio codebase to map its structure, patterns, and gaps so we can design skills and subagents that help us finish and polish it.

Checking `PortfolioContent` wiring, existing `.cursor` setup, and unused Sanity content to identify completion opportunities.

Checking for an existing `.cursor` directory and the profile schema for social/contact fields:

Creating a plan for portfolio-specific skills and subagents based on the codebase.

## You

<attached_files>

<code_selection path="vscode-remote://wsl%2Bubuntu/home/anant_gupta/.cursor/plans/[REDACTED].plan.md" lines="1-261">
---
name: Portfolio skills and subagents
overview: Add project-scoped Cursor skills and subagents tailored to this Next.js + Sanity portfolio so you can finish and polish the site consistently. Skills encode content/CMS rules, UI polish rules, and a completion checklist; subagents give you dedicated “portfolio polish,” “portfolio CMS,” and “portfolio verify” agents.
todos: []
isProject: false
---

# Portfolio skills and subagents plan

## Current state (from exploration)

- **Stack:** Next.js App Router, React, TypeScript, Tailwind, shadcn/ui, Sanity CMS, ObsidianBackground (Three.js), sidebar chat (OpenAI Chatkit).
- **Sections:** Hero (profile), Projects (slider), Experience (cards), Skills (grid), Footer. [AboutSection](src/components/sections/AboutSection.tsx) exists but is **not** used in [PortfolioContent](src/components/PortfolioContent.tsx).
- **Gaps:** (1) No `id="contact"` on Footer so nav “Contact” doesn’t scroll; (2) Footer uses hardcoded `anant@example.com` / placeholder social URLs instead of profile `email` and `socialLinks` from Sanity; (3) `SidebarInset` rendered twice in [layout.tsx](src/app/layout.tsx) (lines 39 and 65); (4) `SITE_SETTINGS_QUERY` exists but is unused (could drive meta, footer text, section copy).
- **Conventions:** [Portfolio-Main-Rules.mdc](.cursor/rules/Portfolio-Main-Rules.mdc) already defines goals (polish, readability, accessibility, no invented APIs/schemas), Tailwind-only styling, and verification (lint/typecheck/build + summary by file).

All skills and subagents will live **in the project** (`.cursor/skills/` and `.cursor/agents/`) so they stay with the repo and align with the existing rule.

---

## 1. Skills (`.cursor/skills/`)

Three project skills that lock in content, UI, and “finish” behavior without duplicating the main rule.

### 1.1 `portfolio-content-cms`

# Purpose  
Keep CMS-backed changes consistent with existing Sanity schemas, queries, and generated types. When editing Sanity-driven content, queries, or schemas, ensure consistency with existing types and no invented fields.  
  
# Use this skill when  
- editing schema files  
- editing `src/sanity/lib/queries.ts`  
- changing rendered content that depends on Sanity data  
- wiring footer/contact/profile content  
- changing site settings usage  
  
# Instructions  
- Use existing schema names, field names, query shapes, and generated types.  
- Do not invent schema fields, query fields, slugs, references, or content contracts.  
- Before expanding a schema or query, list the affected files and UI consumers.  
- Prefer reusing existing content sources before introducing new ones.  
- For footer/contact, prefer profile email and social links already available in existing queries, or an already-defined single source of truth.  
- Keep types aligned with query usage.  
- Preserve optional-field safety in UI rendering.  
  
# Relevant files  
- `src/sanity/lib/queries.ts`  
- `src/sanity/types/`*  
- schema files for profile, projects, experience, skills, site settings  
- content-driven sections and footer components 

- **Contents (SKILL.md):**

- **Description:** “Guides content and CMS changes for this portfolio. Use when editing Sanity schemas, queries, types, or content-driven components (profile, projects, experience, skills, navigation, footer).”
- **Instructions:** Use existing queries in [src/sanity/lib/queries.ts](src/sanity/lib/queries.ts); types from [src/sanity/types](src/sanity/types). Do not add new schema fields or query fields without listing affected files. For footer/contact, prefer profile `email` and `socialLinks` (already in PROFILE_QUERY) or existing `contact`/`siteSettings` schemas if you extend usage.
- **Reference:** Point to `queries.ts`, profile/experience/project/skill schema paths, and PROFILE_QUERY shape for social/email.

- **Trigger terms:** Sanity, CMS, content, schema, queries, profile, projects, footer content, contact.

### 1.2 `portfolio-ui-polish`

# Purpose  
Keep the portfolio polished, readable, responsive, and visually restrained.  
  
# Use this skill when  
- adjusting layout or spacing  
- editing hero, projects, experience, skills, footer, or sidebar UI  
- modifying 3D/background effects  
- tuning motion or responsive behavior  
- improving accessibility or interaction polish  
  
# Instructions  
- Preserve visual hierarchy, contrast, spacing, and readability first.  
- Effects, gradients, motion, and 3D visuals must not overpower text or calls to action.  
- Prefer small parameter changes and local component edits over broad redesigns.  
- Reuse existing section patterns and shared UI primitives where possible.  
- Preserve mobile usability and keyboard accessibility.  
- Add or maintain semantic HTML, aria labels, focus behavior, and keyboard interaction where relevant.  
- Keep animation restrained and purposeful.  
  
# Relevant files  
- section components  
- shared UI components  
- `ObsidianBackground` and related visual components  
- layout/sidebar components  
- theme and global styling files

- **Purpose:** When changing layout, styling, or animation, keep the site on-brand and readable (effects never overpower text).
- **Contents (SKILL.md):**
  - **Description:** “Guides UI, layout, and animation for this portfolio. Use when changing styling, sections, 3D background, sidebar, or accessibility.”
  - **Instructions:** Tailwind + shadcn only; preserve visual hierarchy and contrast; 3D/effects must not overpower text (see [ObsidianBackground](src/components/three/ObsidianBackground.tsx)); reuse [src/components/ui/](src/components/ui/) and section patterns from [PortfolioContent](src/components/PortfolioContent.tsx) and [HeroContent](src/components/sections/HeroContent.tsx); add aria labels and keyboard support where relevant.
  - **Reference:** globals.css theme variables, `use-mobile` (768px), existing motion (framer-motion in HeroContent, ProjectsSlider).
- **Trigger terms:** UI, styling, layout, animation, accessibility, polish, 3D, sections, responsive.

### 1.3 `portfolio-completion`

- **Purpose:** Checklist of known gaps and section wiring so “finish the portfolio” is actionable.
- **Contents (SKILL.md):**
  - **Description:** “Checklist and wiring for finishing this portfolio. Use when completing the site, adding missing sections, or fixing known gaps.”
  - **Instructions:** Completion checklist: (1) Add `id="contact"` to the footer/contact block so nav “Contact” scrolls; (2) Wire Footer email and social links from profile (PROFILE_QUERY) or a single source of truth—remove hardcoded placeholders; (3) Integrate AboutSection into PortfolioContent (e.g. after Hero or before Projects) or remove if not needed; (4) Remove duplicate SidebarInset in root layout (keep one); (5) Optionally use SITE_SETTINGS_QUERY for metadata, footer text, or section subtitles. Section order: Hero → [About] → Projects → Experience → Skills → Footer. After changes: run lint, typecheck, build; summarize by file; suggest manual QA for nav, contact scroll, and footer links.
  - **Reference:** [PortfolioContent](src/components/PortfolioContent.tsx), [Footer](src/components/Footer.tsx), [layout.tsx](src/app/layout.tsx), [AboutSection](src/components/sections/AboutSection.tsx).
- **Trigger terms:** finish, complete, polish, checklist, gaps, contact, about, footer.

---  
name: portfolio-finish-audit  
description: Use when auditing what is left to finish, wire up, or clean up in this portfolio before launch-quality polish.  
---  
  
# Purpose  
Run a focused completion audit for this portfolio using the current known gaps and section structure.  
  
# Use this skill when  
- checking what is still unfinished  
- preparing a final polish pass  
- auditing navigation, footer wiring, layout cleanup, and section composition  
- turning known gaps into an actionable checklist  
  
# Current audit checklist  
1. Ensure the Contact navigation target scrolls correctly.  
2. Replace footer placeholder email/social values with the real content source already used by the portfolio.  
3. Decide whether AboutSection should be integrated or removed.  
4. Remove duplicate layout wrappers or redundant shell composition.  
5. Evaluate whether site settings should drive metadata or shared section copy.  
6. Confirm final section order is intentional and consistent.  
  
# Instructions  
- Treat this as an audit before code changes.  
- Identify which checklist items are already solved and which remain open.  
- For each open item, name the likely files involved.  
- Prefer existing content sources and existing components.  
- After proposing fixes, recommend verification steps for navigation, footer links, responsive layout, and build health.

---

## 2. Subagents (`.cursor/agents/`)

Three project subagents you can invoke for polish, CMS, and verification.

---  
name: portfolio-planner  
description: Plans portfolio changes before implementation by identifying the goal, relevant files, constraints, and smallest safe sequence of edits.  
---  
  
You are the planning specialist for this portfolio repository.  
  
Your job:  
- inspect the request  
- identify the exact goal  
- name the files likely involved  
- separate content, layout, CMS, and verification concerns  
- propose the smallest safe implementation plan  
- call out assumptions and risks  
- do not implement changes unless explicitly asked after planning  
  
Focus on:  
- preserving existing architecture  
- avoiding invented data contracts  
- keeping UI polished and readable  
- preventing regressions in navigation, content rendering, and layout

### 2.1 `portfolio-polish`

- **File:** `.cursor/agents/portfolio-polish.md`
- **Description:** “Visual and UX polish for this Next.js portfolio. Use when improving layout, accessibility, animation, or fixing completion gaps (contact anchor, footer content, About section, layout cleanup).”
- **System prompt (body):** Focus on: (1) Completion gaps—add `id="contact"`, wire footer from profile/sanity, integrate or remove AboutSection, fix duplicate SidebarInset; (2) Visual hierarchy and readability—contrast, spacing, restrained motion; (3) Accessibility—semantic HTML, aria, keyboard; (4) Consistency with existing sections and [Portfolio-Main-Rules.mdc](.cursor/rules/Portfolio-Main-Rules.mdc). Do not invent new routes or schema fields; use existing queries and components.

  
You are the UI execution specialist for this portfolio.  
  
Focus on:  
- layout and spacing improvements  
- responsive behavior  
- accessibility and interaction polish  
- subtle motion and controlled visual effects  
- completion gaps that directly affect visible portfolio quality  
  
Rules:  
- do not invent new routes, sections, or schema fields  
- prefer the smallest visual change that solves the problem  
- preserve contrast and readability  
- use existing components and content sources when possible  
- if a task also affects content wiring, identify the CMS-dependent files before changing them

### 2.2 `portfolio-cms`

You are the CMS and content specialist for this portfolio.  
  
When working on content or CMS behavior:  
- use existing schema names, query shapes, and generated types  
- do not invent fields or expand queries without listing affected files first  
- keep UI rendering aligned with existing content contracts  
- prefer existing profile, footer, and site settings sources over new structures  
- preserve optional-field safety and content readability  
  
Pay attention to:  
- footer/contact wiring  
- profile-driven content  
- project and experience rendering  
- site settings reuse where already defined

- **File:** `.cursor/agents/portfolio-cms.md`
- **Description:** “Sanity CMS and content for this portfolio. Use when changing schemas, queries, types, or content-driven UI (profile, projects, experience, skills, footer, site settings).”
- **System prompt (body):** When editing content or CMS: use [queries.ts](src/sanity/lib/queries.ts) and [types](src/sanity/types); do not add schema or query fields without listing affected files; for footer/contact use profile `email` and `socialLinks` or existing contact/siteSettings. Keep types in sync with queries; respect existing Portable Text and image usage.

### 2.3 `portfolio-verify`

You are the verification specialist for this portfolio.  
  
After changes:  
1. Run the relevant verification commands.  
2. Summarize changed files and what changed in each.  
3. Call out any remaining risks or follow-ups.  
4. If UI, navigation, or content wiring changed, recommend manual QA for:  
 - nav scrolling  
 - footer links  
 - contact target behavior  
 - mobile/sidebar behavior  
 - layout regressions  
 - build health  
  
Do not claim something is verified unless that verification step was actually run.

- **File:** `.cursor/agents/portfolio-verify.md`
- **Description:** “Post-change verification for this portfolio. Use after code changes to run lint, typecheck, build and summarize changes by file.”
- **System prompt (body):** After changes: (1) Run project lint and typecheck (e.g. `pnpm lint`, `pnpm tsc` or equivalent); (2) Run build if applicable (`pnpm build`); (3) Summarize what changed by file; (4) If UI or nav changed, suggest a short manual QA (e.g. nav links, contact scroll, footer links, mobile sidebar). Do not skip verification steps.

---

## 3. Implementation summary

| Item                         | Location                                        | Action                                                  |
| ---------------------------- | ----------------------------------------------- | ------------------------------------------------------- |
| Skill: portfolio-content-cms | `.cursor/skills/portfolio-content-cms/SKILL.md` | Create dir + SKILL.md with frontmatter and instructions |
| Skill: portfolio-ui-polish   | `.cursor/skills/portfolio-ui-polish/SKILL.md`   | Create dir + SKILL.md                                   |
| Skill: portfolio-completion  | `.cursor/skills/portfolio-completion/SKILL.md`  | Create dir + SKILL.md                                   |
| Subagent: portfolio-polish   | `.cursor/agents/portfolio-polish.md`            | Create with name, description, body                     |
| Subagent: portfolio-cms      | `.cursor/agents/portfolio-cms.md`               | Create with name, description, body                     |
| Subagent: portfolio-verify   | `.cursor/agents/portfolio-verify.md`            | Create with name, description, body                     |

No new dependencies; no code edits to the app. Optional: add a one-line mention in the project README that Cursor skills and agents live under `.cursor/` for contributors.

---

## 4. How this helps “finish the portfolio looking amazing”

- **Skills** make the agent follow portfolio-specific content and UI rules whenever you (or the agent) work on Sanity, layout, or “finish” tasks.
- **Subagents** give you one-shot prompts like “Use the portfolio-polish agent to fix the contact anchor and footer” or “Use portfolio-verify after the last change.”
- The **portfolio-completion** skill and **portfolio-polish** subagent encode the concrete gaps (contact id, footer from Sanity, AboutSection, duplicate SidebarInset) so finishing is explicit and repeatable.
- Together with [Portfolio-Main-Rules.mdc](.cursor/rules/Portfolio-Main-Rules.mdc), these keep changes on-brand, maintainable, and verifiable.

---

## 5. Verification after implementation

- Confirm each skill: `.cursor/skills/<name>/SKILL.md` exists and has valid YAML frontmatter (`name`, `description`) and body under ~500 lines.
- Confirm each subagent: `.cursor/agents/<name>.md` exists with frontmatter (`name`, `description`) and body.
- In Cursor, ask: “Use the portfolio-completion skill to list what’s left to finish” and “Use the portfolio-polish subagent to suggest the next steps” to validate discovery.

</code_selection>

</attached_files>
<user_query>
Portfolio skills and subagents plan

Implement the plan as specified, it is attached for your reference. Do NOT edit the plan file itself.

To-do's from the plan have already been created. Do not create them again. Mark them as in_progress as you work, starting with the first one. Don't stop until you have completed all the to-dos.
</user_query>

## Cursor

Implementing the plan: checking existing todos and creating the skill and agent files.

Creating the three skills and three subagents.

Summary of what was added:

**Skills** (`.cursor/skills/`)

| Skill | Path | Purpose |
|-------|------|--------|
| portfolio-content-cms | `.cursor/skills/portfolio-content-cms/SKILL.md` | Sanity schemas, queries, types; no new fields; footer/contact from profile or existing sources |
| portfolio-ui-polish | `.cursor/skills/portfolio-ui-polish/SKILL.md` | Tailwind/shadcn, hierarchy, 3D/effects don’t overpower text, a11y, reuse existing UI |
| portfolio-completion | `.cursor/skills/portfolio-completion/SKILL.md` | Checklist: contact id, footer from Sanity, AboutSection, duplicate SidebarInset, optional site settings; section order and post-change verification |

**Subagents** (`.cursor/agents/`)

| Subagent | Path | Purpose |
|----------|------|--------|
| portfolio-polish | `.cursor/agents/portfolio-polish.md` | UI/completion gaps (contact anchor, footer, About, layout), visual hierarchy, a11y |
| portfolio-cms | `.cursor/agents/portfolio-cms.md` | Sanity queries/types, footer and profile wiring, no new schema without listing affected files |
| portfolio-verify | `.cursor/agents/portfolio-verify.md` | Run lint/typecheck/build, summarize changes, suggest manual QA when UI/nav/content changed |

**Verification**

- Each skill: `.cursor/skills/<name>/SKILL.md` has YAML frontmatter (`name`, `description`) and a short body.
- Each subagent: `.cursor/agents/<name>.md` has frontmatter and a body.

You can try: “Use the portfolio-completion skill to list what’s left to finish” and “Use the portfolio-polish subagent to suggest next steps” to confirm they’re picked up.

## Actions Taken
- Summary: Edited portfolio-verify.md, portfolio-cms.md, portfolio-polish.md, SKILL.md, SKILL.md
- Files changed (Cursor): 6
- Lines: +182 / -0
- Files touched (from tool calls): (none)
- Commands run: (none)
- Tool call tally: (none)

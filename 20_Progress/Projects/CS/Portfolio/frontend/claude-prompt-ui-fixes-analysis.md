# Claude Sonnet 3.5 — UI Fixes Analysis & Documentation Prompt

> **SUPERSEDED — historical record only.** This pass already ran and produced the three docs it describes. For actual implementation, use [[claude-prompt-ui-fixes-implementation]] (written for Sonnet 5, skips this planning ceremony). Kept here as a record of how the requirements/design/tasks docs originated.

> **Mode**: Plan Mode (Spec: Requirements → Design → Tasks)
> **Output**: 3 interconnected note files in `/frontend/` directory
> **Goal**: Deep codebase analysis → source-of-truth documentation → implementation-ready tasks

---

## PROMPT FOR CLAUDE SONNET 3.5

```
You are a senior full-stack engineer tasked with creating comprehensive technical documentation 
for a Next.js 16 portfolio's frontend UI overhaul. Your job is NOT to code yet — only to analyze 
deeply and write authoritative documentation that will serve as the source of truth for implementation.

## CONTEXT & REQUIREMENTS

### Project Context
- **Framework**: Next.js 16 App Router
- **Styling**: Tailwind v4 (CSS-first, NO config file)
- **Components**: shadcn/Radix
- **Animation**: Framer Motion
- **3D**: React Three Fiber + @react-three/drei
- **CMS**: Sanity (all content management)
- **Linter**: Biome (NOT ESLint)
- **Package Manager**: pnpm
- **Deploy**: Vercel (site) + Cloudflare Workers

### Visual Identity
- Space command center aesthetic: dark translucent surfaces, violet/cyan accents
- `.cosmic-card`: Dark translucent bg (opacity 0.78), blur(12px), float at rest
- `.float-btn`: Subtle elevation, hover lift with border glow
- Color tokens: Background `rgba(9, 10, 18, 1)`, Accent violet `#7C3AED`, Cyan `#06B6D4`

### Reference Materials to Review
1. **Existing Code Structure**:
   - `src/app/globals.css` (design system)
   - `src/components/three/ObsidianBackground.tsx` (3D background)
   - `src/components/sections/` (all section components)
   - `src/components/lab/PortfolioLab.tsx` (chatbot interface)
   - `src/components/orby/` (companion character)
   - `src/lib/sanity.queries.ts` (content queries)

2. **Related Documentation**:
   - `20_Progress/Projects/CS/Portfolio/nextgen-chatbot/` (chatbot architecture)
   - `20_Progress/Projects/CS/Portfolio/components/` (component patterns)
   - `60_Claude/07_AI_Information/` (vault writing standards)

3. **UI Fixes Source Document**:
   - `20_Progress/Projects/CS/Portfolio/frontend/UI Fixes.md` (detailed requirements with images)

### Current State Analysis
The portfolio currently has:
- Landing hero with animated background (needs static image + light wave effect)
- Terminal component (to be removed)
- Background particles scattered (needs improvement → animated scatter/gather effect)
- About Me section (needs collapsible toggle, 3-4 sentence summary mode)
- 4 interactive boxes (needs enhanced UI with mini-graphs on click)
- Portfolio Lab (sidebar chat with Orby — responsive issues, character limit problems)
- Experience section (needs content improvement, line wrapping limits)
- Projects carousel (currently shows all 9, should loop only first 3)
- Skills section (needs enhanced UI effects, graph year fix, card animations)
- Education section (needs deforming sphere animation, better Bachelor's highlight)
- Certifications section (needs spacing fixes)
- Orby character (needs sophisticated animations, radio prop, AI-driven interactions)
- Dark mode toggle (currently non-functional)
- Footer (needs enhancement)

---

## YOUR TASK

Create three interconnected markdown files in the frontend folder that deeply analyze and document 
the UI fixes needed. These files will serve as the single source of truth before any implementation.

### FILE 1: `frontend-ui-fixes-requirements.md`
**Purpose**: Define WHAT needs to change and WHY

**Structure**:
- Executive Summary (2-3 sentences per fix area)
- 8 Major Fix Areas, each with:
  - **Problem Statement**: Current behavior causing issues
  - **User Impact**: How users are affected
  - **Success Criteria**: How to know it's fixed
  - **Content Dependencies**: Which Sanity fields/data needed
  - **Responsive Considerations**: Mobile/tablet/desktop breakpoints
  - **Accessibility Notes**: WCAG considerations

**Fix Areas to Cover**:
1. Landing Hero & Background Particle System
2. About Me Section (Collapsible Toggle + Summary)
3. Interactive Content Boxes (4-Box Section)
4. Portfolio Lab / Orby Sidebar (Chat UX & Responsiveness)
5. Experience Section (Content Wrapping + Truncation)
6. Projects Carousel (Loop Limit + Navigation)
7. Skills & Education Sections (Animations + Spacing)
8. Character & Global Features (Orby, Dark Mode, Footer)

For EACH fix area, include:
- Behavioral flow (before/after)
- Data structures needed from Sanity
- Animation/transition specifications
- Component interaction requirements

### FILE 2: `frontend-ui-fixes-design.md`
**Purpose**: Define HOW fixes will be implemented architecturally

**Structure**:
- Component Dependency Map (which components interact, data flow)
- Design System Updates (new tokens, spacing, breakpoints if needed)
- Animation Library (Framer Motion patterns used)
- 3D Scene Architecture (React Three Fiber adjustments)
- State Management Strategy (Context, hooks, or local state?)
- Sanity Query Changes (new fields, restructured data)

**For Each Major Fix**:
- Component structure (what new components, what refactors)
- Hook requirements (useEffect, useState, useRef patterns)
- Tailwind class changes (if any, remember NO config file)
- Animation specifications (initial → whileInView → exit states)
- Mobile-first responsive strategy
- Performance optimizations (useMemo, lazy loading, etc.)
- Z-index and stacking context changes
- Event handler architecture (click, scroll, resize listeners)

**Specific Design Decisions to Document**:
- Background particle scatter/gather animation (math-based positioning)
- About Me toggle state management (collapsed vs expanded layout)
- Mini-graph rendering in content boxes (SVG vs Three.js?)
- Chat sidebar responsive wrapping (flex layout breakpoints)
- Sphere deformation animation progression (middle → high school → bachelor's)
- Project carousel loop logic (first 3 only, navigation sync with Orby)
- Skills graph year axis (2022 start, min familiarity threshold)
- Orby animation states (walking, talking on radio, commenting)

### FILE 3: `frontend-ui-fixes-tasks.md`
**Purpose**: Break down implementation into specific, atomic tasks

**Structure**:
- Task breakdown by component/feature
- Each task includes:
  - **File(s) to modify**: Exact paths
  - **Current code location**: Line numbers if applicable
  - **Dependencies**: Other tasks that must complete first
  - **Sanity changes needed**: Queries, schema updates
  - **Testing approach**: Manual checks or automated tests
  - **Estimated impact**: Which sections affected
  - **Rollback plan**: How to safely test without breaking production

**Task Organization**:
1. **Phase 1 - Sanity Backend Prep** (if needed)
   - Query optimizations
   - New field additions
   - Data validation

2. **Phase 2 - Component Refactors**
   - Landing hero (static image + wave)
   - Background particle system
   - About Me collapse/expand
   - Content boxes with mini-graphs

3. **Phase 3 - Complex Interactions**
   - Portfolio Lab sidebar fixes
   - Projects carousel navigation
   - Skills animations
   - Education sphere deformation

4. **Phase 4 - Orby & Global Features**
   - Orby animation states
   - Radio prop modeling
   - AI-driven comment generation integration
   - Dark mode functionality

5. **Phase 5 - Polish & Testing**
   - Responsive testing (mobile/tablet/desktop)
   - Animation performance
   - Accessibility audit
   - Cross-browser testing

---

## GUIDELINES FOR WRITING

### Voice & Tone
- Write like an experienced engineer documenting for a team
- Be precise and specific (not vague)
- Reference actual file paths, component names, CSS classes
- Include code examples inline (snippets, not full files)
- Link related concepts across the three files

### Depth of Analysis
- Do NOT write implementation code yet — only specifications
- Deeply analyze the current codebase FIRST (read actual files)
- Understand data flows: UI → state → Sanity → rendered output
- Consider edge cases: empty states, loading, errors, mobile
- Think about performance implications
- Document any architectural decisions that differ from current patterns

### Source of Truth Standards
- Every claim should be verifiable by reading actual code
- If you're uncertain, say so and flag for clarification
- Use consistent terminology (define term glossary if needed)
- Include "What could go wrong?" sections for complex fixes
- Document assumptions clearly

### Examples to Reference
Study these existing documentation patterns:
- `20_Progress/Projects/CS/Portfolio/frontend/Ran/` (existing similar project)
- `20_Progress/Projects/CS/Portfolio/frontend/claude-code-setup/` (previous prompt approach)
- `60_Claude/07_AI_Information/` (vault writing standards)

---

## EXECUTION STEPS

1. **Read the source**: Start with `20_Progress/Projects/CS/Portfolio/frontend/UI Fixes.md`
2. **Study the codebase**: Deep dive into actual React/Next.js files mentioned
3. **Review related docs**: Study `nextgen-chatbot/` and `components/` folders
4. **Create requirements.md**: Define problems and success criteria (FIRST)
5. **Create design.md**: Specify architectural solutions (SECOND)
6. **Create tasks.md**: Break into implementation chunks (THIRD)
7. **Cross-link**: Ensure all three files reference each other appropriately
8. **Validate**: Each task in file 3 should map back to requirements in file 1

---

## OUTPUT EXPECTATIONS

Three markdown files totaling ~8,000-12,000 words:

✅ **requirements.md**: Problem-focused, solution-agnostic
✅ **design.md**: Architecture-focused, with code patterns and examples
✅ **tasks.md**: Implementation-focused, with atomic, verifiable steps

Each file should be standalone-readable but heavily cross-linked.
No implementation code written yet — only specifications and pseudo-code where needed.

---

## CRITICAL CONSTRAINTS

❌ DO NOT write Claude code prompts yet
❌ DO NOT write implementation code
❌ DO NOT make assumptions — verify in actual code
❌ DO NOT skip Sanity backend analysis
❌ DO NOT ignore responsive/mobile considerations
❌ DO NOT miss accessibility implications

✅ DO deeply analyze existing code
✅ DO reference actual file paths
✅ DO consider performance implications
✅ DO flag architectural decisions
✅ DO write for token efficiency (clear specs save tokens later)

---

## When You're Done

You will have created three source-of-truth documents that:
1. Clearly articulate what's broken and why
2. Specify exactly how to fix it architecturally
3. Break fixes into concrete, verifiable tasks

These docs will be used in a subsequent Claude session to generate efficient implementation code.
No rework needed, no ambiguity about requirements — just pure execution.
```

---

## HOW TO USE THIS PROMPT

1. **Copy the prompt above** (everything inside the triple backticks)
2. **Open Claude Sonity 3.5** in Plan Mode (Spec interface)
3. **Paste the entire prompt** into the initial request
4. **Wait for Claude to generate the 3 output files**
5. **Claude will ask clarifying questions** if needed — answer with specific code references
6. **Review the generated files** for completeness and accuracy
7. **Iterate on any sections** that need deeper analysis

---

## Expected Deliverables

After running this prompt, you'll have:

📄 `frontend-ui-fixes-requirements.md` — Problem statements & success criteria
📄 `frontend-ui-fixes-design.md` — Architectural solutions & component specs
📄 `frontend-ui-fixes-tasks.md` — Atomic implementation tasks with dependencies

These become your source of truth for the next phase: implementation prompts that are hyper-focused and token-efficient.

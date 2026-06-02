---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - tooling
source_url: https://github.com/addyosmani/agent-skills
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Agent Skills (Addy Osmani)

**What it is:** 23 structured Claude Code skills by Addy Osmani (Google Chrome DevRel lead) covering the full development lifecycle — define, plan, build, verify, review, ship — each as a slash command that activates automatically based on what you're doing.

**What it actually does:** Install via Claude Code marketplace or local clone. The 7 entry-point commands (`/spec`, `/plan`, `/build`, `/test`, `/review`, `/code-simplify`, `/ship`) each activate multiple underlying skills. Key design choices: every skill has a "rationalizations table" that documents excuses agents use to skip steps and rebuts them; every skill ends with evidence requirements ("tests passing" not "seems right"); the `doubt-driven-development` skill runs an adversarial cross-model review when stakes are high. The `context-engineering` skill specifically addresses how to feed agents the right information at the right time — relevant to Jarvis integration. The `source-driven-development` skill grounds every framework decision in official docs with citations. Baked-in engineering principles from Google's SWE Book: Beyoncé Rule (test pyramid), Hyrum's Law (API design), Chesterton's Fence (simplification), Shift Left (CI/CD).

**Why it matters for this vault/workflow:** The skills complement gstack and mattpocock/skills without duplicating them. gstack gives cognitive modes (founder/engineer/QA); mattpocock gives feedback-loop discipline; agent-skills gives a more comprehensive process map for the full SDLC. The `context-engineering` skill is particularly relevant to Jarvis — it's explicit about how to structure `CLAUDE.md`, rules files, and context packing, which directly improves how Claude interacts with the vault. The 3 specialist personas (code-reviewer, test-engineer, security-auditor) work as standalone agents invokable from within any session.

**How to use it:**
```bash
# Via Claude Code marketplace
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills

# Or local
git clone https://github.com/addyosmani/agent-skills.git
claude --plugin-dir /path/to/agent-skills
```

**Failure modes / limitations:** 23 skills is a lot to internalize — without `/using-agent-skills` (the meta-skill that maps incoming work to the right skill), the catalog becomes noise. The `doubt-driven-development` skill triggers cross-model escalation for high-stakes decisions — this requires a second model configured, which may not always be available. The skills reference Google engineering culture (SWE Book, eng-practices guide) which is excellent context but may feel heavyweight for solo projects.

**Verdict:** Install and use primarily through the 7 slash commands rather than invoking individual skills directly — let the entry points route to the right skill automatically.

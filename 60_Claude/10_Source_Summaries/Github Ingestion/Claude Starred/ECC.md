---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - agents
  - tooling
source_url: https://github.com/affaan-m/ECC
notes:
  - "[[40_Resources/CS/Repos]]"
---
# ECC
> [!DECISION] Fork repo, install and copy primarily the security layer. The harness needs to be mimicked into jarvis. Skills, agents, etc. need to be compared with other repos. [REPO'S THAT ARE SIMILAR]
> **Answer:** Similar harness repos (ordered by overlap): gstack (cognitive modes), mattpocock-skills (TDD + feedback loops), ruflo (self-improving swarm), agent-skills-addyosmani (full SDLC pipeline). ECC's unique piece none of the others have: **security layer** — allowlist/denylist for tool invocations. In Claude Code terms this maps directly to *hooks* (pre/post tool-call scripts that can block dangerous operations). Action: extract ECC's security layer → translate to Claude Code hooks in CLAUDE.md. Don't install ECC wholesale. ECC instincts ≈ hooks, ECC skills ≈ slash commands — use mattpocock for skills, ECC only for the security harness.

**What it is:** A multi-component agent harness for Claude Code and other coding agents that adds skills, "instincts" (automatic behaviors), persistent memory, and security hardening in a single installable layer.

**What it actually does:** ECC ships as two npm packages — `ecc-universal` (the core harness) and `ecc-agentshield` (security module). It layers on top of Claude Code's existing tool loop rather than replacing it: skills are markdown prompts, instincts are hooks that fire automatically at the right moment, memory persists context across sessions, and the shield intercepts prompt injection and unsafe tool calls. The GitHub App integration (150+ installs) handles repo-level configuration and updates. The README is multilingual, suggesting production adoption beyond English-speaking communities.

**Why it matters for this vault/workflow:** ECC is the closest thing to an "OS layer" for Claude Code agents — it addresses the same problems Jarvis is solving (context persistence, structured workflows) but at the harness level rather than the vault level. It could complement Jarvis: ECC handles the agent's runtime behavior while Jarvis handles the knowledge graph. The security module (agentshield) is worth attention specifically because unguarded agents running hooks on a real codebase are an attack surface.

**How to use it:** 
```bash
npx ecc-universal   # install core harness
npx ecc-agentshield # install security layer
```
See the GitHub App at github.com/marketplace/ecc-tools for repo-level setup.

**Failure modes / limitations:** Very high star count relative to fork count suggests adoption is broader than contribution — the README's actual architecture is obscured by how comprehensive it is. The "skills, instincts, memory, security" framing is marketing-speak until you read the actual hook implementations. Verify that the hooks don't conflict with existing `.claude/settings.json` hooks before installing into an active project.

**Verdict:** Install and test `ecc-universal` on a throwaway project to understand what "instincts" actually do before committing to it — the security module alone may be worth it.

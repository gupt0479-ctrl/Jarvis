---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - tooling
source_url: https://github.com/davila7/claude-code-templates
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Claude Code Templates

**What it is:** An npm CLI (`npx claude-code-templates`) that browses and installs a catalog of 100+ agents, commands, MCPs, settings, hooks, and skills for Claude Code from an interactive terminal or web dashboard at aitmpl.com.

**What it actually does:** Running `npx claude-code-templates@latest` opens an interactive picker. You select components — e.g., a security-auditor agent, a `/generate-tests` command, a PostgreSQL MCP integration, a pre-commit validation hook — and it writes the right files into your `.claude/` directory. It also ships analytics (`--analytics`), a conversation monitor (`--chats`), a health-check (`--health-check`), and a plugin dashboard (`--plugins`). The catalog aggregates community sources: Anthropic's official skills, wshobson/agents, awesome-claude-code commands, and 30+ others.

**Why it matters for this vault/workflow:** This is the fastest way to discover and install Claude Code extensions that Jarvis doesn't cover — MCP integrations for databases and APIs, pre-built agents for specific roles, and settings configurations. Instead of hunting GitHub for individual skills, this is a single entry point. The analytics tool is also useful for understanding how Claude Code sessions are actually performing.

**How to use it:**
```bash
# Browse and install interactively
npx claude-code-templates@latest

# Install specific components directly
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
npx claude-code-templates@latest --hook git/pre-commit-validation --yes

# Check health of Claude Code install
npx claude-code-templates@latest --health-check
```

**Failure modes / limitations:** The catalog is community-contributed, so quality varies. Aggregated skills may have drifted from their source repos since being added to the catalog. The web dashboard (aitmpl.com) is in beta. Don't install hooks blindly — review what `pre-commit-validation` actually does before wiring it to your git workflow.

**Verdict:** Use it as a discovery tool and install specific components à la carte rather than letting it configure everything — the interactive picker is the actual value.

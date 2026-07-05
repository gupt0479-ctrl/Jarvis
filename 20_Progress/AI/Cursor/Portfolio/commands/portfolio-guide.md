---
setup_status: draft
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Cursor/Portfolio/Setup]]"
---
  # Portfolio Development Guide with ECC

  ## Your Project
  - **Type**: Next.js 16.1.1 Portfolio
  - **CMS**: Sanity v4.22.0
  - **3D**: Three.js + React Three Fiber

  ## Most Used Commands

  | Command | Purpose |
  |---------|---------|
  | `/tdd` | Test-driven development |
  | `/code-review` | Review code after changes |
  | `/build-fix` | Fix build failures |
  | `/security-scan` | Security audit |
  | `/update-docs` | Update documentation |

  ## Common Workflows

  **New Feature:**
  /everything-claude-code:plan "Add feature"
  /tdd
  [implement]
  /code-review

  **Debug Build:**
  /build-fix

  **Before Commit:**
  /security-scan

  ## Model Settings

  - **Default**: `/model sonnet` (60% cheaper, 80%+ tasks)
  - **Complex**: `/model opus` (architecture, debugging)

  ## Token Optimization

  - Use `/clear` between unrelated tasks
  - Use `/compact` at logical breakpoints
  - Disable unused MCP servers
  </parameter>
  </function>
  </tool_call>
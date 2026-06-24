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
# AI Assistant
## MOC
- [[AI Workflow]]
- [[HW__ - ...]]
## Definition
- 
## Resources
- 
### How to use them
1. 
2. 
## AI Summary
**Repository Overview**
This repository is Jan, a desktop-first local AI app built as a monorepo with a React frontend, a Rust Tauri backend, and a pluggable extension runtime.

Key top-level layers:
1. Product and build entry:
README.md, package.json, Makefile
2. Extension SDK and abstractions:
extension.ts, index.ts, types
3. Frontend app (UX + orchestration):
src
4. Native backend (IPC commands + MCP process management):
lib.rs, core
5. Built-in extension implementations:
extensions
6. Docs for MCP behavior and routing:
mcp-servers.mdx, mcp-routing-telemetry.mdx

How the app boots:
1. Frontend initializes platform services:
ServiceHubProvider.tsx, index.ts
2. Frontend creates window.core bridge and extension managers:
ExtensionProvider.tsx, service.ts
3. Backend exposes Tauri commands (including MCP):
lib.rs

---

**Core Components**
1. Service Hub pattern (platform abstraction)
- Frontend code calls services, not raw Tauri directly.
- Tauri implementations are swapped in at runtime.
- MCP service contract and desktop implementation:
types.ts, tauri.ts

2. Extension architecture
- Jan defines typed extension families: Assistant, Conversational, Inference, MCP, RAG, VectorDB.
- Base abstractions:
assistant.ts, conversational.ts, mcp.ts, rag.ts, vector-db.ts

3. State and persistence
- Frontend state is mostly Zustand (assistants, MCP configs, tool approvals, agent mode).
- Thread and message persistence is backend-managed:
commands.rs
- Desktop uses file persistence; mobile uses SQLite:
mod.rs, db.rs

4. Built-in extensions as product modules
- Assistant persistence/migrations:
index.ts
- Conversation storage via core API:
index.ts
- RAG tools (retrieve, list attachments, chunks):
index.ts, tools.ts
- Local inference engine integration:
index.ts

---

**AI Agents and MCP Implementation**
Jan’s “agent behavior” is practical tool-using chat orchestration rather than a separate autonomous planner engine.

1. Agent persona and instructions
- Default assistant instruction sets tool-calling style and reasoning expectations:
useAssistant.ts
- Assistant extension ensures assistant data exists and migrates prompt versions:
index.ts

2. Tool loop in chat turn execution
- After model output, tool calls are processed sequentially.
- Each tool is permission-checked, then routed to RAG or MCP backend.
- Main orchestration path:
$threadId.tsx

3. MCP backend mechanics
- Command surface: list tools, list connected servers, call tool, cancel tool call, activate/deactivate server, config load/save.
commands.rs
- Runtime state tracks running services, active configs, cancellation tokens, monitor tasks, PIDs:
state.rs
- Models for tool/server metadata and runtime settings:
models.rs

4. MCP server lifecycle and resiliency
- Startup from config, process spawn/HTTP/SSE connections, monitoring, reconnect backoff, shutdown contexts:
helpers.rs
- Default MCP config and runtime defaults:
constants.rs
- Lock-file based stale process cleanup for Jan Browser MCP:
lockfile.rs
- Migration path across MCP schema versions:
setup.rs

5. Smart MCP tool routing (critical MCP-at-scale logic)
- Orchestrator loads only relevant server tools when many servers are connected.
- Keyword scoring fallback + optional structured LLM router + telemetry/fallback handling:
mcp-orchestrator.ts, intent-classifier.ts, mcp-router-llm.ts
- Integrated into model transport before each inference call:
custom-chat-transport.ts

---

**How Components Work Together (End-to-End Flow)**
Step-by-step for one user turn with tools:
1. User sends message in thread UI:
$threadId.tsx
2. Custom transport creates model, refreshes tools, optionally smart-routes MCP servers:
custom-chat-transport.ts
3. Model emits tool calls via AI SDK stream.
4. Thread route handles each tool call:
- RAG tool -> RAG extension service
- MCP tool -> MCP Tauri command
$threadId.tsx
5. Backend calls MCP tool over running rmcp service with timeout/cancellation:
commands.rs
6. Tool output is appended; model continues; thread/message persistence updates:
commands.rs

---

**Extending and Customizing the App as an MCP Hub**
1. Add and harden MCP servers
- UI and JSON edit flows:
mcp-servers.tsx
- Config save/load behavior:
commands.rs
- Best practical tweak:
Set capabilities and description fields per server so routing quality improves (these are consumed by server summaries and intent classifier).

2. Tune routing strategy
- Adjust threshold and scoring behavior:
intent-classifier.ts
- Adjust LLM router timeout / schema behavior:
mcp-router-llm.ts
- Observe behavior with tests and optional telemetry:
mcp-routing-telemetry.test.ts, mcp-routing-telemetry.mdx

3. Customize permissions and safety posture
- Global and per-thread tool approval:
useToolApproval.ts
- MCP settings UI toggles:
mcp-servers.tsx

4. Build your own extension
- Extension manager load/activate path:
extension.ts
- Core extension contracts:
extensions
- Build/pack pipeline:
package.json, package.json

5. Make it a stronger MCP control plane
- Add server health dashboards using get_server_summaries and connected server lists.
- Add routing telemetry sink in custom transport around orchestrator callback.
- Add server-specific policy rules before callTool dispatch in thread route.
- Add persistent audit trails for tool calls at thread metadata/message metadata boundary.

---

**Important Patterns and Framework Choices**
1. Plugin-style architecture with typed extension contracts
- Clear interface boundaries between app shell and capabilities.
2. Service-hub facade
- Platform differences are encapsulated in service implementations.
3. Event-driven refresh
- MCP updates propagate via mcp-update events:
setup.rs, useTools.ts
4. Fail-soft design for MCP
- Timeout, cancellation, reconnect, fallback to full tool list, stale process cleanup.
5. Practical orchestrator pattern
- Server-level preselection before model call to shrink tool exposure/context size.

---

**Learning Recommendations**
If your goal is to learn agent and MCP implementation from this repo, focus in this order:

1. Start with runtime flow
- custom-chat-transport.ts
- $threadId.tsx

2. Then read MCP backend lifecycle
- commands.rs
- helpers.rs
- state.rs

3. Then study smart routing deeply
- mcp-orchestrator.ts
- intent-classifier.ts
- mcp-router-llm.ts

4. Then inspect extension design and persistence
- extensions
- index.ts
- index.ts
- commands.rs

5. Finally validate understanding through tests/docs
- mcp-orchestrator.test.ts
- mcp-routing-telemetry.test.ts
- mcp-servers.mdx

Natural next steps:
1. I can produce a call-graph style walkthrough for one specific MCP server type (stdio vs HTTP vs SSE) from UI click to backend process lifecycle.
2. I can give you a concrete “build your own MCP hub variant” checklist with exact files to fork and what to change first.
3. I can map this architecture to a minimal standalone template so you can recreate the same agent+MCP pipeline in a smaller project.

## Common mistakes
- 
## Mini-test (answer without looking)
- [ ] Flashcards
- [ ] 
## Flashcards (best 3–8)


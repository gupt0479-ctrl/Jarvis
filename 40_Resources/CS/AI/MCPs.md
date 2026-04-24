---
type: concept
status: seed
created: 2026-03-04
updated: 2026-07-27
related_progress:
  - "[[AI Workflow]]"
  - "[[Gen AI Roadmap]]"
tags:
  - concept
next: "[[Cursor AI]]"
track:
  - ai
prerequisites: []
used_in: []
evidence:
  - "[[60_Claude/45_Outputs/Vault Enrichment Prompt]]"
difficulty: 3
mastery_level: novice
mastery_score: null
last_drilled: 2026-04-25
next_drill: 2026-05-05
drill_interval: 10
---
## The Setup

## Resources

## What is MCP and why does it matter?
MCP stands for **Model Context Protocol** - it's the standard way to give Cursor's AI agent access to your actual tools: your files, your Git history, your GitHub issues. Without MCP, the AI can only see what you paste into the chat. With MCP, it can _act_.
### Cursor 
Cursor is a game-changer for developers, especially when you know how to make it work for you. After building 7+ products for clients, I’ve nailed down the most efficient way to use Cursor with minimal mistakes. Here’s everything you need to know to get started as a beginner:
1. *Plan Before Coding*: Start with a solid plan. Use ChatGPT to create your **PRD**, database design, color palette, and **project structure**. Save these as .md files in Cursor to stay organized. Trust me, a clear roadmap saves you hours.
2. *Start with a Strong Foundation*: Cursor shines when you give it something solid to build on. Tools like V0 can generate the initial UI code – refine that in Cursor to reduce mistakes and rework.
3. *Leverage*: Cursor has a directory with tech-specific prompts. Customize them for your project using a `.cursorrules` file. This improves precision, especially for your stack.
4. *Tag Relevant Docs*: Sync official docs (Next.js, Supabase, etc.) into Cursor. Reference them using @LibraryName, or add your own docs with @Docs → Add new doc.
5. *Stay Updated with @Web*: Use the web search feature to get the latest information while working. Cursor will pull real-time answers directly from the internet.
6. *Save Working Code Snippets*: Whenever Cursor generates great code, save it as .md files for future reference. It’s a time-saver for similar tasks down the line.
7. *Query the Entire Codebase*: With @Codebase, you can ask questions about your project, and Cursor will search your codebase for relevant insights.
8. *Fast Edits*: Highlight code, press ⌘ K, and tell Cursor how to modify it. Or, generate new code with ⌘ K without selecting anything.
9. *Visual Feedback with Images*: Not happy with your UI? Take a screenshot and upload it in Cursor’s chat for better context.
10. *Learn with AI*: Ask Cursor to explain code as if you’re a beginner. Over time, you’ll spot patterns and improve naturally.
11. *Use Code Templates*: Don’t reinvent the wheel. Use boilerplates for common elements like auth, payments, and databases to kickstart your project.
Cursor is insanely powerful when you set it up right.
### AI Workflow Integration Plan
Think of your setup as **3 lanes**, each with a default tool:
1. **Lane A - Study + writing (long context) → Claude**
	- Use Claude Projects as “course workspaces”
	    - Upload: lecture PDFs, problem sets, rubrics, your notes, transcripts.
	    - Outputs: clean study notes, practice questions, checklists, office-hour questions.
2. **Lane B — Fast tutoring + reusable workspaces → ChatGPT Projects**
	- One ChatGPT Project per: a course, a recurring assignment type, or a product.
	- Save:
	    - Your markdown prompt templates (Role/Objective/Instructions/Notes)
	    - Your formatting requirements (Google-doc friendly / Obsidian / code-only)
	    - Your “don’t do X” constraints.
3. **Lane C — Coding + refactors inside the repo → VS Code + Codex**
	- Use Codex for:
	    - “Explain this file”
	    - “Find the bug”
	    - “Refactor this component but keep behavior”
	    - “Add tests / fix failing tests”
	- Use ChatGPT/Claude for:
	    - writing the spec, acceptance criteria, and edge cases _before_ Codex edits the repo.
## 5.2 What Cursor is in the MCP model  
For your workflow, think in these terms:  
- **Cursor = MCP client / host environment**  
- **Supabase / GitHub / filesystem / browser-use / internal tools = MCP servers**  
That means Cursor itself is not “the MCP.”  
Cursor is the environment that **uses MCP servers**.  
## 5.3 What MCP is useful for inside a codebase  
Use MCP when the agent needs reliable access to something outside plain repo files, such as:  
- database schemas  
- external docs  
- tickets  
- PRs  
- deployment metadata  
- design systems  
- analytics dashboards  
- browser tooling  
- internal APIs  
## 5.4 Cursor MCP setup details that matter now  
Official docs note:  
- MCP connects Cursor to external systems and data  
- servers can be managed in **Settings → Features → Model Context Protocol**  
- disabled servers can be toggled on/off  
- use environment variables instead of hardcoding secrets for stdio server configs  
- for cloud agents, MCP configs are encrypted at rest and sensitive fields are redacted after saving.
### Security note  
Treat MCP as production-grade tooling, not a toy:  
- do not hardcode secrets  
- use the smallest set of servers you actually need  
- review tool permissions  
- keep servers isolated where possible  
- add approval or hooks around risky operations when appropriate
## 5.5 MCP transports: what matters practically  
The MCP specification defines standard transports including:  
- `stdio`  
- `Streamable HTTP`  
The docs recommend broad client support for stdio when possible.
### Practical rule  
For local development:  
- start with `stdio` servers first  
- use environment variables  
- only move to remote/http patterns when you actually need shared or hosted servers  
## MCPs
1. *Filesystem MCP* Lets the agent locate, read, and update files across your repo — no more manually copying code snippets into the chat.
2. *Git MCP*: Summarizes recent changes, drafts clean commit messages, generates changelogs, and flags risky diffs automatically.
3. *GitHub MCP*: Pulls issue and PR context, drafts PR descriptions, and links your code changes to existing tickets.
4. *Obsidian Second brain manager*: The agent modifies the notes based on the file properties of each note, modifies the content only which was asked to modify. Make sure to not touch files that were specifically asked not to cover. Make the notes better, interconnected and keep a track of the changes being made per file. 

---

## Deep Dive

### One-Sentence Version

MCP is a JSON-RPC protocol that lets an AI model call external tools (databases, file systems, APIs) through a standardized client-server interface instead of relying on whatever the user pastes into the chat.

### What It Is

Model Context Protocol defines a contract between a **host** (the AI-powered editor or agent), a **client** (the protocol handler inside that host), and one or more **servers** (each exposing a set of tools). The server advertises capabilities — read a file, query a database, list GitHub issues — and the client invokes them on behalf of the model.

The transport layer is usually `stdio` for local servers (a subprocess the host spawns) or `Streamable HTTP` for remote ones. The model never talks to the server directly; the client mediates, enforces permissions, and handles serialization.

This matters because without MCP, every tool integration is bespoke. With it, one protocol covers filesystem access, Git operations, database queries, and browser automation — the same way HTTP standardized web requests regardless of what the server does behind the endpoint.

### Why It Matters

- Without MCP, an AI agent can only work with what fits in its context window. It cannot inspect a live database schema, read a file it hasn't been shown, or check the status of a GitHub PR.
- With MCP, the agent gains **action capability**: it can read, write, and query external systems through structured tool calls.
- The protocol is open (Anthropic published the spec), so it works across Cursor, Claude Desktop, Kiro, and any client that implements the handshake.
- In this vault, the Obsidian Local REST API acts as an MCP server — that's how AI tools read and modify notes without manual copy-paste.

### Real Example

In the Jarvis vault right now: Kiro connects to the `obsidian-local-rest-api` MCP server. When a spec task says "read the note at `40_Resources/CS/AI/MCPs.md`," Kiro's MCP client sends a JSON-RPC request to the Obsidian server, which returns the note content. The model never opens a file browser — it calls a tool, gets structured data back, and acts on it.

Another example from the Cursor workflow: connecting a Supabase MCP server lets the agent inspect your database schema before writing a migration, instead of guessing table names from code comments.

### Contrast With

**MCP vs. plain function calling**: Function calling (OpenAI-style) lets a model output a JSON blob that your application code interprets. MCP goes further — it standardizes discovery (the server advertises what tools exist), invocation (JSON-RPC with typed parameters), and transport (stdio or HTTP). Function calling is "the model suggests an action." MCP is "the model executes an action through a protocol."

**MCP vs. plugins/extensions**: Browser plugins (like ChatGPT plugins, now deprecated) were platform-locked and required marketplace approval. MCP servers are local processes you control, with no marketplace gatekeeping. You can write a server in any language, run it on your machine, and connect it to any MCP-compatible client.

### Source Anchors

- MCP specification: published by Anthropic, defines the client-server handshake, tool advertisement, and transport layers
- Cursor MCP docs: Settings → Features → Model Context Protocol for server management
- [[Gen AI Day - 2]] — session notes covering MCP as "connectors + permissions + tool menu"
- [[AI Workflow]] — integration plan showing MCP in the coding lane

---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: wsl
title: "Sanity plugin functionality"
started_at: 2026-03-25T23:28:21
ended_at: 2026-03-25T23:28:21
exported_at: 2026-07-30T19:56:24
project: portfolio
cwd: "/home/anant_gupta/projects/portfolio"
session_id: a15ec528-c8ea-4b1a-a64e-0c7a3d948e7c
status: raw
turn_count: 2
tools_used:
files_changed_count: 0
lines_added: 0
lines_removed: 0
tags:
  - input
  - ai-conversation
  - cursor
  - wsl
---

# Sanity plugin functionality

## You

<user_query>
Show me how the Sanity plugin works
</user_query>

## Cursor

The user wants an overview of the Sanity plugin they just installed. Let me check the STATUS.md file for the MCP server authentication status, then provide an overview.

Now I have enough context to provide the user with an overview of the Sanity plugin. Let me also check if there's an mcp_auth tool that needs to be called for authentication.

Here's an overview of what the **Sanity plugin** gives you in this workspace:

---

## What's Included

### MCP Server - `Sanity`
The core of the plugin. It gives me direct tool access to your Sanity Content Lake, so I can:
- **Query content** with GROQ — find documents, filter by type, search full-text or semantically
- **Read and deploy schemas** — inspect your schema, create new types, deploy changes to the cloud
- **Manage documents** — create, patch, publish, unpublish, and delete documents without leaving the editor
- **Generate and transform images** — AI-powered image operations on Sanity image fields
- **Search documentation** — look up official Sanity docs in real time rather than relying on potentially stale training data
- **Version and release management** — create document versions for content releases

### Skills (auto-applied when relevant)
Four bundled skills that guide my behavior on Sanity tasks:

| Skill | When it activates |
|---|---|
| `sanity-best-practices` | Any schema, GROQ, TypeGen, or Next.js/Sanity integration work |
| `content-modeling-best-practices` | Designing or refactoring content types and schemas |
| `content-experimentation-best-practices` | A/B testing and CMS-managed variants |
| `seo-aeo-best-practices` | Metadata, Open Graph, JSON-LD, sitemap work |

### Commands (invoke with `/`)
- `/deploy-schema` — Deploy your local Sanity schema to the Content Lake
- `/typegen` — Run Sanity TypeGen to regenerate TypeScript types from your schema
- `/review` — Review code for Sanity best practices
- `/sanity` — List available Sanity help topics and skills

---

## Authentication Required

The MCP server needs to be authenticated to your Sanity account before it can access your project's data. Let me trigger the auth flow now:

The MCP server is already connected and authenticated - no extra login step needed. Here's a summary of all available MCP tools:

**Schema & Studio**
- `get_schema`, `list_workspace_schemas`, `deploy_schema`

**Document Operations**
- `query_documents`, `get_document`, `create_documents_from_json`, `create_documents_from_markdown`
- `patch_document_from_json`, `patch_document_from_markdown`
- `publish_documents`, `unpublish_documents`, `discard_drafts`

**Versioning & Releases**
- `create_version`, `version_replace_document`, `version_discard`, `version_unpublish_document`

**Images**
- `generate_image`, `transform_image`

**Project Management**
- `list_projects`, `list_organizations`, `create_project`, `list_datasets`, `create_dataset`, `add_cors_origin`

**Search & Docs**
- `semantic_search`, `list_embeddings_indices`
- `search_docs`, `read_docs`, `list_sanity_rules`, `get_sanity_rules`, `migration_guide`

---

You're all set. You can now ask things like:

- "Show me all my Sanity documents of type `project`"
- "Add a new `blogPost` schema type"
- "Update the title of document `abc123`"
- "What does my current schema look like?"
- `/typegen` to regenerate TypeScript types after schema changes
- `/deploy-schema` to push local schema changes to Sanity

The MCP server is already connected and available - it has tools available. No `mcp_auth` tool is needed. It seems the server is already authenticated or doesn't require explicit authentication. Let me note this to the user.

## Actions Taken
- Summary: Read SERVER_METADATA.json, INSTRUCTIONS.md, STATUS.md
- Files changed (Cursor): 0
- Lines: +0 / -0
- Files touched (from tool calls): (none)
- Commands run: (none)
- Tool call tally: (none)

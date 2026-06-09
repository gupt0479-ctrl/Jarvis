---
epoch: 1775009686263
modelKey: "claude-sonnet-4.5|github-copilot"
topic: "Claude Code with Obsidian Integration"



tags:
  - copilot-conversation
---

**user**: i have currently installed claude code cli and have ollama with cloud models running. I want to use obsidian with claude code in such a manner that it remembers everything that we have done. I want to integrate api's from claude code directly like obsidian, google drive, gmail, etc. Explore the notes about setting up claude code with obsidian.
[Context: Notes: 40_Resources/CS/AI/AI Workflow.md]
[Timestamp: 2026/03/31 21:14:46]

**ai**: # Setting Up Claude Code CLI with Obsidian Integration

Based on your current setup (Claude Code CLI + Ollama + Obsidian), here's a comprehensive guide to create a persistent memory system with direct API integrations.

## Current State Analysis

**What you have:**
- Claude Code CLI installed
- Ollama with cloud models
- Obsidian vault with extensive AI workflow documentation

**What you want:**
- Claude Code to remember all conversations and actions
- Direct API integrations (Obsidian, Google Drive, Gmail)
- Seamless workflow between tools

## Architecture Overview

```
┌─────────────────┐
│  Claude Code    │
│     CLI         │
└────────┬────────┘
         │
         ├──────────> Obsidian (MCP)
         ├──────────> Google Drive (MCP)
         ├──────────> Gmail (MCP)
         └──────────> Memory Store (Persistent Context)
```

## Step 1: Enable Persistent Memory in Claude Code

### Option A: Using Project Context Files

Create a dedicated project folder structure:

```bash
mkdir -p ~/claude-obsidian-workspace
cd ~/claude-obsidian-workspace

# Create context files
touch .claud-context.md
touch .project-memory.md
```

**`.claud-context.md` template:**
```markdown
# Claude Code Workspace Context

## Project Overview
- Purpose: AI-assisted knowledge management and automation
- Tools: Claude Code CLI, Obsidian, Ollama
- Vault Location: [your vault path]

## Active Goals
- [ ] Integrate Obsidian with Claude Code
- [ ] Set up Google Drive sync
- [ ] Configure Gmail automation

## Preferences
- Code style: [your preferences]
- Documentation format: Markdown
- Always reference Obsidian notes when relevant

## Recent Context
[Auto-updated by Claude Code]
```

### Option B: Using Claude Code's Built-in Memory

Configure Claude Code to save conversation history:

```bash
# Set environment variable for persistent sessions
export CLAUDE_CODE_MEMORY_PATH="$HOME/.claude-code/memory"

# Create memory directory
mkdir -p $HOME/.claude-code/memory

# Add to your ~/.bashrc or ~/.zshrc
echo 'export CLAUDE_CODE_MEMORY_PATH="$HOME/.claude-code/memory"' >> ~/.zshrc
```

## Step 2: Set Up MCP (Model Context Protocol) Integrations

### Install MCP Server for Obsidian

**Create MCP server configuration:**

```bash
# Create MCP config directory
mkdir -p ~/.config/claude-code/mcp-servers

# Create Obsidian MCP config
cat > ~/.config/claude-code/mcp-servers/obsidian.json << 'EOF'
{
  "name": "obsidian",
  "command": "node",
  "args": ["/path/to/obsidian-mcp-server/index.js"],
  "env": {
    "OBSIDIAN_VAULT_PATH": "/path/to/your/vault",
    "OBSIDIAN_API_KEY": "your-api-key-if-needed"
  }
}
EOF
```

### Create Custom Obsidian MCP Server

Since there isn't an official Obsidian MCP server yet, create a simple one:

**`obsidian-mcp-server/package.json`:**
```json
{
  "name": "obsidian-mcp-server",
  "version": "1.0.0",
  "type": "module",
  "dependencies": {
    "@anthropic-ai/sdk": "^0.20.0",
    "chokidar": "^3.5.3"
  }
}
```

**`obsidian-mcp-server/index.js`:**
```javascript
#!/usr/bin/env node

import fs from 'fs/promises';
import path from 'path';
import chokidar from 'chokidar';

const VAULT_PATH = process.env.OBSIDIAN_VAULT_PATH;

// MCP Server Implementation
const server = {
  name: "obsidian",
  version: "1.0.0",
  
  tools: [
    {
      name: "search_notes",
      description: "Search Obsidian vault for notes matching query",
      parameters: {
        type: "object",
        properties: {
          query: {
            type: "string",
            description: "Search query"
          }
        },
        required: ["query"]
      }
    },
    {
      name: "read_note",
      description: "Read content of specific note",
      parameters: {
        type: "object",
        properties: {
          path: {
            type: "string",
            description: "Path to note relative to vault"
          }
        },
        required: ["path"]
      }
    },
    {
      name: "create_note",
      description: "Create new note in vault",
      parameters: {
        type: "object",
        properties: {
          path: {
            type: "string",
            description: "Path for new note"
          },
          content: {
            type: "string",
            description: "Note content"
          }
        },
        required: ["path", "content"]
      }
    },
    {
      name: "append_to_note",
      description: "Append content to existing note",
      parameters: {
        type: "object",
        properties: {
          path: {
            type: "string",
            description: "Path to note"
          },
          content: {
            type: "string",
            description: "Content to append"
          }
        },
        required: ["path", "content"]
      }
    }
  ],
  
  async handleToolCall(toolName, parameters) {
    switch(toolName) {
      case "search_notes":
        return await this.searchNotes(parameters.query);
      case "read_note":
        return await this.readNote(parameters.path);
      case "create_note":
        return await this.createNote(parameters.path, parameters.content);
      case "append_to_note":
        return await this.appendToNote(parameters.path, parameters.content);
      default:
        throw new Error(`Unknown tool: ${toolName}`);
    }
  },
  
  async searchNotes(query) {
    const files = await this.getAllMarkdownFiles(VAULT_PATH);
    const results = [];
    
    for (const file of files) {
      const content = await fs.readFile(file, 'utf-8');
      if (content.toLowerCase().includes(query.toLowerCase())) {
        const relativePath = path.relative(VAULT_PATH, file);
        const excerpt = this.getExcerpt(content, query);
        results.push({ path: relativePath, excerpt });
      }
    }
    
    return results;
  },
  
  async readNote(notePath) {
    const fullPath = path.join(VAULT_PATH, notePath);
    const content = await fs.readFile(fullPath, 'utf-8');
    return { path: notePath, content };
  },
  
  async createNote(notePath, content) {
    const fullPath = path.join(VAULT_PATH, notePath);
    await fs.mkdir(path.dirname(fullPath), { recursive: true });
    await fs.writeFile(fullPath, content);
    return { success: true, path: notePath };
  },
  
  async appendToNote(notePath, content) {
    const fullPath = path.join(VAULT_PATH, notePath);
    await fs.appendFile(fullPath, '\n' + content);
    return { success: true, path: notePath };
  },
  
  async getAllMarkdownFiles(dir) {
    const files = [];
    const entries = await fs.readdir(dir, { withFileTypes: true });
    
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        files.push(...await this.getAllMarkdownFiles(fullPath));
      } else if (entry.name.endsWith('.md')) {
        files.push(fullPath);
      }
    }
    
    return files;
  },
  
  getExcerpt(content, query, contextLength = 150) {
    const index = content.toLowerCase().indexOf(query.toLowerCase());
    if (index === -1) return content.slice(0, contextLength);
    
    const start = Math.max(0, index - contextLength / 2);
    const end = Math.min(content.length, index + query.length + contextLength / 2);
    
    return '...' + content.slice(start, end) + '...';
  }
};

// Start MCP server
console.log(JSON.stringify({
  jsonrpc: "2.0",
  result: server
}));

// Handle incoming requests via stdin
process.stdin.on('data', async (data) => {
  try {
    const request = JSON.parse(data.toString());
    const result = await server.handleToolCall(
      request.params.name,
      request.params.arguments
    );
    
    console.log(JSON.stringify({
      jsonrpc: "2.0",
      id: request.id,
      result: result
    }));
  } catch (error) {
    console.error(JSON.stringify({
      jsonrpc: "2.0",
      id: request?.id,
      error: { message: error.message }
    }));
  }
});
```

### Install and Configure the Server

```bash
cd obsidian-mcp-server
npm install
chmod +x index.js

# Test the server
OBSIDIAN_VAULT_PATH="/path/to/your/vault" node index.js
```

## Step 3: Configure Claude Code to Use MCP Servers

**Edit Claude Code configuration:**

```bash
# Create or edit Claude Code config
nano ~/.config/claude-code/config.json
```

**`config.json`:**
```json
{
  "mcpServers": {
    "obsidian": {
      "command": "node",
      "args": ["/absolute/path/to/obsidian-mcp-server/index.js"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "/absolute/path/to/your/vault"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    }
  },
  "memory": {
    "enabled": true,
    "path": "$HOME/.claude-code/memory",
    "autoSave": true
  }
}
```

## Step 4: Set Up Google Drive Integration

### Install Google Drive MCP Server

```bash
npm install -g @modelcontextprotocol/server-gdrive
```

**Add to `config.json`:**
```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"],
      "env": {
        "GDRIVE_CLIENT_ID": "your-client-id",
        "GDRIVE_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

**Get Google Drive credentials:**
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create new project or select existing
3. Enable Google Drive API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download credentials JSON
6. Extract `client_id` and `client_secret`

## Step 5: Set Up Gmail Integration

**Add Gmail MCP server to `config.json`:**
```json
{
  "mcpServers": {
    "gmail": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gmail"],
      "env": {
        "GMAIL_CLIENT_ID": "your-gmail-client-id",
        "GMAIL_CLIENT_SECRET": "your-gmail-client-secret"
      }
    }
  }
}
```

## Step 6: Create Workflow Prompts

### Create Context-Aware Prompt System

**Create `~/claude-prompts/obsidian-aware.md`:**
```markdown
# System Prompt for Obsidian-Integrated Claude

You have access to the following tools:

## Obsidian Tools
- search_notes: Search vault for relevant notes
- read_note: Read specific note content
- create_note: Create new notes
- append_to_note: Add content to existing notes

## Workflow Rules
1. Before answering questions about past work, search relevant notes
2. Always save important decisions and learnings to notes
3. Reference existing notes using [[note-title]] format
4. Append conversation summaries to daily notes

## Memory Strategy
- Check "Daily Notes/[today's date].md" for today's context
- Search "Projects/" for ongoing work
- Reference "40_Resources/CS/AI/" for AI workflow details

## Example Workflow
User: "What was that automation I built last week?"
1. Search notes: query="automation last week"
2. Read relevant notes
3. Provide answer with [[note-references]]
4. Append summary to today's daily note
```

### Create Startup Script

**`~/bin/claude-obsidian`:**
```bash
#!/bin/bash

# Set environment
export OBSIDIAN_VAULT_PATH="$HOME/path/to/vault"
export CLAUDE_CODE_MEMORY_PATH="$HOME/.claude-code/memory"

# Create today's daily note if it doesn't exist
TODAY=$(date +%Y-%m-%d)
DAILY_NOTE="$OBSIDIAN_VAULT_PATH/Daily Notes/$TODAY.md"

if [ ! -f "$DAILY_NOTE" ]; then
  cat > "$DAILY_NOTE" << EOF
---
date: $TODAY
tags: [daily-note]
---

# $TODAY

## Tasks
- [ ] 

## Notes


## Claude Conversations
<!-- Auto-appended by Claude Code -->

EOF
fi

# Start Claude Code with context
claude-code --config ~/.config/claude-code/config.json \
            --system-prompt "$(cat ~/claude-prompts/obsidian-aware.md)" \
            --context-file "$DAILY_NOTE"
```

Make it executable:
```bash
chmod +x ~/bin/claude-obsidian
```

## Step 7: Usage Examples

### Example 1: Search and Reference Notes

```bash
claude-obsidian

# In Claude Code:
> Search my notes for "AI workflow automation"
> Read the AI Workflow note
> Based on that note, help me build the weekly learning summary automation
```

Claude will:
1. Search vault using `search_notes`
2. Read [[AI Workflow]] using `read_note`
3. Generate automation code
4. Append conversation to today's daily note

### Example 2: Create Project Documentation

```bash
# In Claude Code:
> I just built a new Obsidian MCP server. Help me document it.
> Create a note at "Projects/MCP Servers/Obsidian Integration.md"
> Include: setup steps, configuration, usage examples
```

Claude will:
1. Create note using `create_note`
2. Generate comprehensive documentation
3. Cross-reference related notes
4. Update today's daily note with progress

### Example 3: Automated Daily Standup

**Create `~/bin/daily-standup`:**
```bash
#!/bin/bash

TODAY=$(date +%Y-%m-%d)
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)

claude-code << EOF
Search my notes for work done on $YESTERDAY
Read yesterday's daily note: Daily Notes/$YESTERDAY.md
Generate a standup summary:
- What I did yesterday
- What I'm doing today
- Blockers

Save to Daily Notes/$TODAY.md under "## Standup"
EOF
```

## Step 8: Advanced Memory Persistence

### Create Conversation Logger

**`obsidian-mcp-server/logger.js`:**
```javascript
import fs from 'fs/promises';
import path from 'path';

export async function logConversation(vaultPath, conversation) {
  const today = new Date().toISOString().split('T')[0];
  const dailyNote = path.join(vaultPath, 'Daily Notes', `${today}.md`);
  
  const timestamp = new Date().toLocaleTimeString();
  const logEntry = `\n### ${timestamp}\n${conversation}\n`;
  
  await fs.appendFile(dailyNote, logEntry);
}
```

### Auto-Save Important Decisions

**Add to Claude Code config:**
```json
{
  "hooks": {
    "afterResponse": {
      "script": "node ~/.config/claude-code/hooks/save-important.js"
    }
  }
}
```

**`save-important.js`:**
```javascript
// Detects important decisions and saves to notes
if (response.includes("decision:") || response.includes("important:")) {
  // Append to decisions log
  appendToNote("Decisions Log.md", response);
}
```

## Step 9: Integration Testing

### Test Checklist

```bash
# Test Obsidian integration
claude-code
> Search notes for "AI workflow"
> Read the AI Workflow note
> Create a test note at "Test/integration-test.md"

# Test Google Drive (after OAuth setup)
> List files in my Google Drive
> Create a document called "Claude Integration Test"

# Test Gmail (after OAuth setup)
> Search my emails for "github copilot"
> Draft an email to myself with subject "Test from Claude"

# Test memory persistence
> Remember that my favorite color is blue
# Close and reopen Claude Code
> What's my favorite color?
```

## Step 10: Workflow Optimization

### Create Aliases in Obsidian

Add to your Obsidian vault's `.obsidian/plugins/` or use Templater:

**Claude Quick Commands:**
- `@claude-search [query]` → Trigger Claude to search notes
- `@claude-summarize [[note]]` → Summarize specific note
- `@claude-explain [concept]` → Explain with vault context

### Set Up Hotkeys

**Add to your shell config:**
```bash
# Quick Claude commands
alias cs='claude-code --quick "Search my notes for"'
alias cr='claude-code --quick "Read note at"'
alias cc='claude-code --quick "Create note"'
```

## Troubleshooting

### Common Issues

**1. Claude doesn't remember past conversations:**
- Check `CLAUDE_CODE_MEMORY_PATH` is set
- Verify memory directory exists and is writable
- Ensure `--context-file` points to valid note

**2. MCP servers not loading:**
```bash
# Debug MCP servers
claude-code --debug-mcp
```

**3. Obsidian notes not found:**
- Verify `OBSIDIAN_VAULT_PATH` is correct
- Check file permissions
- Test with `ls $OBSIDIAN_VAULT_PATH`

**4. Google Drive/Gmail auth failing:**
- Re-run OAuth flow
- Check credentials expiry
- Verify API permissions in Google Cloud Console

## Next Steps

1. **Test the basic Obsidian integration** with the MCP server
2. **Set up OAuth for Google services** following their documentation
3. **Create your daily workflow script** combining all integrations
4. **Build automation scripts** for repetitive tasks
5. **Document your setup** in your vault for future reference

Would you like me to:
1. Help you debug any specific integration?
2. Create more advanced automation scripts?
3. Set up the Google OAuth flow step-by-step?
4. Build custom MCP tools for your specific workflows?
[Timestamp: 2026/03/31 21:15:54]
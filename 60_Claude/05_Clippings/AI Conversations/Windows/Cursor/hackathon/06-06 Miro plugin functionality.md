---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: windows
title: "Miro plugin functionality"
started_at: 2026-06-06T15:13:05
ended_at: 2026-06-06T21:17:18
exported_at: 2026-07-30T19:56:24
project: hackathon
cwd: "D:\\projects\\hackathon"
session_id: a9c1e758-c240-4be2-aa04-55b15c5b86f7
status: raw
turn_count: 11
tools_used:
  AskQuestion: 1
  CallMcpTool: 1
  CreatePlan: 1
  Glob: 7
  Grep: 1
  Read: 14
  Shell: 2
  StrReplace: 3
  TodoWrite: 3
  WebSearch: 16
  Write: 20
files_touched:
  - "C:\\Users\\Anant Gupta\\.cursor\\plugins\\cache\\cursor-public\\miro\\9627168a40c694c61a8734cbcdd452d21e560bdc\\skills\\miro-mcp\\SKILL.md"
  - "C:\\Users\\Anant Gupta\\.cursor\\projects\\d-projects-hackathon\\mcps\\plugin-miro-miro\\STATUS.md"
  - "C:\\Users\\Anant Gupta\\.cursor\\projects\\d-projects-hackathon\\mcps\\plugin-miro-miro"
  - "C:\\Users\\Anant Gupta\\.cursor\\projects\\d-projects-hackathon\\mcps\\plugin-miro-miro\\tools\\mcp_auth.json"
  - "D:\\projects\\hackathon\\docs"
  - "D:\\projects\\hackathon"
  - "C:\\Users\\Anant Gupta\\.cursor\\projects\\d-projects-hackathon\\mcps\\plugin-miro-miro\\SERVER_METADATA.json"
  - "C:\\Users\\Anant Gupta\\.cursor\\projects\\d-projects-hackathon\\mcps\\plugin-miro-miro\\tools\\layout_get_dsl.json"
  - "C:\\Users\\Anant Gupta\\.cursor\\projects\\d-projects-hackathon\\mcps\\plugin-miro-miro\\tools\\layout_create.json"
  - "C:\\Users\\Anant Gupta\\.cursor\\projects\\d-projects-hackathon\\mcps\\plugin-miro-miro\\tools\\prototype_create.json"
  - "C:\\Users\\Anant Gupta\\.cursor\\projects\\d-projects-hackathon\\mcps\\plugin-miro-miro\\tools\\prototype_read.json"
  - "C:\\Users\\Anant Gupta\\.cursor\\projects\\d-projects-hackathon\\mcps\\plugin-miro-miro\\tools\\code_widget_create.json"
  - "D:\\projects\\hackathon\\docs\\RESEARCH.md"
  - "D:\\projects\\hackathon\\docs\\PLAYBOOK.md"
  - "D:\\projects\\hackathon\\AGENTS.md"
  - "D:\\projects\\hackathon\\docs\\00-START-HERE.md"
  - "D:\\projects\\hackathon\\docs\\01-strategy\\hackathon-playbook.md"
  - "D:\\projects\\hackathon\\docs\\01-strategy\\tool-matrix.md"
  - "D:\\projects\\hackathon\\docs\\01-strategy\\miro-mcp-guide.md"
  - "D:\\projects\\hackathon\\docs\\02-product\\PRD-template.md"
  - "D:\\projects\\hackathon\\docs\\02-product\\prd.md"
  - "D:\\projects\\hackathon\\docs\\03-architecture\\system-architecture.md"
  - "D:\\projects\\hackathon\\docs\\03-architecture\\data-model.md"
  - "D:\\projects\\hackathon\\docs\\03-architecture\\api-contract.md"
  - "D:\\projects\\hackathon\\docs\\03-architecture\\security.md"
  - "D:\\projects\\hackathon\\docs\\03-architecture\\cicd-deploy.md"
  - "D:\\projects\\hackathon\\docs\\04-workflow\\docs-to-miro.md"
  - "D:\\projects\\hackathon\\docs\\04-workflow\\miro-to-lovable.md"
  - "D:\\projects\\hackathon\\docs\\04-workflow\\lovable-to-cursor.md"
  - "D:\\projects\\hackathon\\docs\\05-memory\\decisions.md"
  - "D:\\projects\\hackathon\\docs\\05-memory\\prompts-library.md"
  - "D:\\projects\\hackathon\\.claude\\settings.json"
  - "C:\\Users\\Anant Gupta\\.cursor\\skills-cursor\\create-hook\\SKILL.md"
  - "D:\\projects\\hackathon\\.claude"
files_changed_count: 20
lines_added: 2369
lines_removed: 2
tags:
  - input
  - ai-conversation
  - cursor
  - windows
---

# Miro plugin functionality

## You

<plugin_info kind="matched_installed">
display_name: Miro
description: Secure access to Miro boards. Enables AI to read board context, create diagrams, and generate code with enterprise-grade security.
skills:
  - miro-mcp: This skill teaches how to use Miro MCP tools effectively for creating diagrams, documents, tables, and extracting context from Miro boards. Use when the user asks about Miro capabilities, wants to create content on Miro boards, or needs to work with Miro board data.
commands:
  - browse: List and explore items on a Miro board
  - diagram: Create a diagram on a Miro board from a text description
  - doc: Create a document (Google Docs-style) on a Miro board
  - summarize: Generate documentation or summary from a Miro board
  - table: Create a table on a Miro board with specified columns
mcp_servers:
  - miro
</plugin_info>
<user_query>
Show me how the Miro plugin works
</user_query>

## Cursor

I'll pull the Miro plugin overview from its skill and MCP server docs, then check whether authentication is required.

[REDACTED]

Checking the auth tool schema and starting Miro authentication.

[REDACTED]

[REDACTED]

# Miro Plugin Overview

The Miro plugin connects Cursor to your Miro boards so the agent can **read board context** and **create visual content** — diagrams, documents, and tables — with enterprise-grade security.

---

## Slash Commands

You can invoke these directly with `/` in chat:

| Command | What it does |
|---------|----------------|
| `/browse` | List and explore items on a Miro board |
| `/diagram` | Create a diagram from a text description |
| `/doc` | Create a Google Docs-style document on a board |
| `/summarize` | Generate documentation or a summary from a board |
| `/table` | Create a table with specified columns |

---

## How It Works (3 Layers)

### 1. MCP Server (`miro`)
The underlying integration. Tools are grouped into:

**Create content**
- `diagram_create` — flowcharts, mind maps, UML, ER diagrams (natural language or Mermaid)
- `doc_create` / `doc_update` — markdown documents on boards
- `table_create` / `table_sync_rows` — tables with text and dropdown columns

**Read content**
- `context_explore` — high-level board overview (frames, docs, tables, diagrams)
- `context_get` — detailed content from a specific item
- `board_list_items` — browse items, filter by type or frame
- `table_list_rows` — read table data
- `image_get_data` / `image_get_url` — work with images

**Edit documents**
- `doc_get` — read document content
- `doc_update` — find-and-replace edits

### 2. Skill (`miro-mcp`)
Used automatically when you ask about Miro or want board work done. It encodes best practices — spacing, positioning, workflows — so the agent uses the tools correctly.

### 3. Agent (automatic)
You can also just ask in plain language, e.g.:
- *"Create a flowchart on my board for user registration"*
- *"Summarize what's on this Miro board"*
- *"Add a sprint planning table to my board"*

The agent picks the right tools and follows the skill guidance.

---

## Typical Workflows

**Create a diagram**
```
/diagram on board https://miro.com/app/board/uXjV... 
User registration: start → enter email → validate → create account
```

**Explore then extract**
1. `context_explore` — see what's on the board
2. `context_get` — pull details from specific frames, docs, or diagrams

**Create structured content**
- Documents support markdown (headings, lists, bold, links)
- Tables support text columns and color-coded select/dropdown columns
- Diagrams auto-detect type or you can specify: flowchart, mindmap, uml_class, uml_sequence, entity_relationship

**Board URLs**
Paste full Miro URLs — the tools extract `board_id` and `item_id` automatically, including `moveToWidget` links.

---

## Authentication Required

The Miro MCP server **needs authentication** before any board operations work. I started the auth flow, but it timed out after 2 minutes.

To connect your Miro account:
1. Run `/browse` or ask me to work with a board again — that should re-trigger the auth prompt
2. Complete the OAuth/sign-in flow in the browser when prompted
3. Once connected, all tools above become available

---

## Quick Examples

| You say… | What happens |
|----------|----------------|
| `/diagram` + description | Diagram created on your board |
| `/doc` + markdown content | Document added to the board |
| `/table` + columns/rows | Table created or updated |
| `/summarize` + board URL | Documentation generated from board content |
| `/browse` + board URL | Items listed and explored |

If you share a Miro board URL and what you want (diagram, doc, table, or summary), I can walk through a concrete example once you're authenticated.

[REDACTED]

**Tool calls:**

- `Read` — `C:\Users\Anant Gupta\.cursor\plugins\cache\cursor-public\miro\9627168a40c694c61a8734cbcdd452d21e560bdc\skills\miro-mcp\SKILL.md`
- `Read` — `C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\STATUS.md`
- `Glob` — pattern `**/*`, path `C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro`
- `Read` — `C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\mcp_auth.json`
- `CallMcpTool` — `{"server":"plugin-miro-miro","toolName":"mcp_auth","arguments":{}}`

## You

<external_links>
### Potentially Relevant Websearch Results

You should respond as if these information are known to you. Refrain from saying "I am unable to browse the internet" or "I don't have access to the internet" or "I'm unable to provide real-time news updates". This is your internet search results. Please always cite any links you referenced from the above search results in your response in markdown format.

-------
Website URL: https://miro.com/app/dashboard/space/0cSxp1dXLN16U5m28NBjgy
Website Title: 
Website Content:

____

Website URL: https://developers.miro.com/docs/rest-api-build-your-first-hello-world-app?utm_source=your_apps
Website Title: Quickstart
Website Content:
Jump to Content

Miro Developer PlatformMCPDocumentationResourcesMarketplaceCommunity

DocumentationAPI ReferenceChangelog

main

---

MCPDocumentationResourcesMarketplaceCommunityBuild your appMiro Developer Platform

Documentation

Build your app

main

Documentation

Quickstart

Quickstart

## Platform Essentials

* Introduction
* Web SDK vs REST API
* Getting started  
   * Developer team  
         * Create a Developer team  
         * Change the Developer team name  
         * Delete the Developer team  
   * Migrating a developer app
* App manifest
* Concepts  
   * Boards  
   * Board items  
         * Children inside parent items  
   * App card  
         * App card use cases  
         * Edit, update, and keep app cards synced  
         * Backend flow for app cards  
         * Enable REST API authentication from Miro's Web SDK authorization  
         * Enable 2-way sync between app cards and GitHub cards  
   * Card  
   * Connector  
   * Embed  
   * Events  
   * Frame  
   * Image  
   * Mind map (Experimental)  
   * Preview  
   * Shape  
   * Sticky note  
   * Storage  
   * Text  
   * Tag
* Migrate from v1 to v2  
   * Web SDK comparison guide  
   * Web SDK reference guide  
   * REST API comparison guide  
   * REST API reference guide

## MCP

* Introduction
* Miro's MCP Server
* Connecting to Miro's MCP Server
* Miro MCP Server Tools & Prompts
* Connecting Miro's MCP Server to MCP-compatible clients
* Tutorial: How to Generate Diagrams from Code w/ Miro MCP & VSCode + GitHub Copilot
* Tutorial: Build a Node.js app from a Miro Board with Miro MCP + Cursor
* Tutorial: How to Build a Landing Page from a Miro Board w/ Lovable + Miro MCP
* 🛠 Miro MCP Server FAQ and Troubleshooting

## Web SDK

* Introduction  
   * Miro Web SDK and board items  
   * App panels and modals
* Guided onboarding  
   * Onboarding essentials  
         * 1) Create your first board item with the Web SDK  
         * 2) Update an item's properties with \`sync()\`  
         * 3) Run your first app in Miro  
         * 4) Interact with your app in Miro  
         * 5) Join the conversation  
         * 6) Install a Marketplace app  
         * 7) Add Mirotone to an existing app  
         * Onboarding wrap-up  
         * Challenge: Where's Miro?  
   * Submit and share your app  
         * 1) Share an app outside of a developer team  
         * 2) Understand app submission requirements  
         * 3) Publish a Miro app  
         * 4) Share your ideas with us  
         * Submit and share wrap-up  
   * In-depth training modules  
         * 1) Create your 1st Miro app locally  
         * 2) Build a full-stack Miro app
* Getting started  
   * Quickstart  
   * Video: try the Web SDK in less than 1 minute  
   * Build your first Hello World app  
         * Build a Web SDK app  
         * Build a REST API app  
         * Build a full-stack (Next.js) app  
         * Enable running apps as instant apps
* How-Tos & tutorials  
   * Use the browser developer tools with the Miro Web SDK  
   * Update and sync item properties  
   * Add icon click to your app  
   * Add an icon to your app  
   * Add drag and drop to your app  
   * Add permission scopes to your app  
   * Add search and filter to your app  
   * Build a calendar app in Miro  
   * Convert sticky notes to shapes  
   * Create mind map from CSV  
   * Add custom actions to your app  
   * Deploy a Miro app  
   * Log in to a third-party service using OAuth  
   * Enable 2-way sync between app cards and GitHub cards  
   * Enable REST API authentication from Miro's Web SDK authorization  
   * Integrate a digital asset manager in Miro  
   * Convert frame coordinates to board coordinates  
   * SVG app icon optimization guidelines  
   * Upload images and SVGs as base64-encoded strings  
   * Connect the Miro Web SDK to a backend (Firebase)  
   * Video: Deploy a Next.js App on AWS Amplify  
   * Video: Integrate OpenAI + Miro  
   * Build collaborative app experiences  
   * Display banner/modal on a Miro board using DynamoDB  
   * Display banner/modal on a Miro board using AWS S3
* Reference  
   * Interact with boards and items  
   * Rate limiting  
   * Error handling  
   * Board  
   * Card  
   * Board UI  
   * Viewport  
   * Notifications  
   * App card  
   * Experimental  
   * Realtime Events  
   * Tag  
   * Custom Action Management  
   * Shape  
   * Frame  
   * Image  
   * Sticky Note  
   * Shape experimental  
   * Embed  
   * Connector  
   * Unsupported  
   * Mindmap Node  
   * Preview  
   * Text  
   * Storage collection  
   * Storage  
   * Collaboration  
   * Session  
   * Attention  
   * Group  
   * History  
   * Tools

## REST API

* Introduction
* Getting started  
   * Quickstart  
   * Video: try the REST API in less than 3 minutes  
   * Build your first Hello World REST API app
* How-To's & tutorials  
   * Get started with OAuth 2.0 and Miro  
   * Enable REST API authentication from Miro's Web SDK authorization  
   * Access Enterprise APIs  
   * Create sticky notes and tags  
   * Convert code to diagram with Miro PlantUML  
   * Get user info and email  
   * Create an image from a data URL source  
   * Work with connectors  
   * Securely manage boards and teams at scale  
   * Enable 2-way sync between app cards and GitHub cards  
   * Set up a test endpoint for webhooks with Pipedream  
   * Troubleshoot OAuth2.0  
   * Video: OAuth Essentials for Frontenders
* Miro Node.js client  
   * Miro Node.js client Readme  
   * Miro Node.js client quickstart for task automation  
   * Miro Node.js client quickstart with OAuth and Express  
   * Implement data storage  
   * Reference documentation
* Miro Python client
* Reference

## Marketplace

* Miro Marketplace
* Get ready for Marketplace  
   * App design guidelines  
   * App security guidelines  
   * App development policy  
   * App listing guidelines  
   * Build and deploy your app  
   * Your Marketplace profile
* Publish your app
* Monetization  
   * Monetization with Miro + Stripe  
   * Monetization with Miro + Salable (Subscription Management)  
   * Provide pricing details for your app
* App Metrics

## SCIM API

* Introduction
* User lifecycle management
* Getting started
* Concepts  
   * Rate limits
* Reference  
   * Users  
   * Groups  
   * Discovery features

## Live Embed

* Introduction
* Getting started  
   * Authentication  
   * oEmbed support
* How-Tos & tutorials  
   * Live Embed with a direct link  
   * Live Embed view-only mode  
   * Live Embed with BoardsPicker for registered users  
   * Live Embed with BoardsPicker for unregistered users
* Reference

## Resources

* Resources overview
* Changelog
* Roadmap
* Mirotone
* Miro app examples
* Miro Postman сollection
* Policies  
   * Developer terms of use  
   * App development policy  
   * Lifecycle policy  
   * Deprecation policy

Powered by 

# Quickstart

This tutorial shows you how to get a simple app running in Miro. This app uses our REST APIs.  
If you've never built a Miro app before, you're in the right place. Welcome, and let's get started!  
By the end of this guide, you'll have a board that has a sticky note with the text **Hello, World!**.

# 

Prerequisites

Before you begin, ensure that you have the following prerequisites:

* Your Miro user account has a Developer team.

## 

Step 1: create your app in Miro

1. Sign in to Miro, and then click your user account avatar.
2. From the drop-down menu, select **Settings**.
3. In the app settings view, click the **Your apps** tab.
4. In the **Your apps** view, click **\+ Create new app**.  
    
**Figure 1.** To start creating a new app from your app settings, click **\+ Create new app**.
5. On the **Create new app** modal:  
   1. In the **App name** input field, enter the name of your app.  
   For example: **Hello world.**  
   2. Select the **Expire user authorization token** checkbox to enable the expiring access token and refresh token feature for REST API authorization.  
   After creating the app, it's no longer possible to change the user authorization token from expiring to non-expiring.  
   Using an expiring access token and refresh token enhances your application's security. An access token expires in 1 hour and a refresh token expires in 60 days. When a new access token is requested, you also get a new refresh token.  
   In this scenario, the old access token and refresh token are no longer valid.  
   If you enable this feature, when you exchange an authorization code to an access token, you will also get back a refresh token.  
   For more information, see the REST API authorization flow for expiring tokens.  
   3. Click **Create app**.  
         
   **Figure 2.** Create a new app.

## 

Step 2: configure your app in Miro

You can configure your app in one of the following ways:

* Edit the plain text app manifest in the online editor.
* Select the appropriate options in the app settings UI.

This step described how to configure your app using the app manifest editor.

1. On the app settings page, click **Edit in Manifest**.  
    
**Figure 3.** Click **Edit in Manifest** to open the app manifest editor.
2. In the app manifest editor, set at least the following properties:  
    
**Figure 4.** Configure your app by editing the app manifest.  
   * appName: the name of the app that you entered in the **App name** input field, on the **Create new app** modal.  
   * scopes: the Miro REST API and the Web SDK implement user access control through scopes.  
   Scopes define the permissions your app requires to interact with a board and to work as designed.  
   When users install your app, they are prompted to provide consent for the required scopes.  
   For example, to enable your app to read from and write to the board, specify the following permissions:  
         * `board:read`  
         * `board:write`
3. Once done, save your settings by clicking **Save**.
4. To go back to the app settings UI and proceed with the app installation, in the top-right corner of the page click **Edit in UI**.

## 

Step 3: install the app

In the app settings UI, do the following:

1. At the bottom of the app settings page, click **Install app and get OAuth token**.
2. On the **Install app to get OAuth token** dialog:  
i. From the **Select a team** drop-down menu, select **Dev team**.  
    
**Figure 5.** Select a team.  
ii. Click **Install & authorize**. A message notifies you that the app is successfully installed, and you get your access token.  
You need this access token in the next steps where you call the APIs to create a board and create a sticky note item on the board.  
    
**Figure 6.** Access token.  
iii . Click **Close**.

#### 

Service Account Use Case for REST API

If you plan to create an app and use it as a **service account** (i.e. no users for the app, just automate certain things on the board with the REST API) then you won't need to implement the full OAuth flow in your app. You'll need to decide if you want expiring tokens (recommended as a security best practice) or non-expiring (fine for test applications). If you're going with the non-expiring approach, then once you get your access token from following the steps above, you are done and ready to use the access token to call Miro's REST API endpoints.

If you've decided to go with the expiring token, then you'll need to implement some logic to get new access token using refresh token. We also have example code to show you how to implement the refresh token logic in our node-oauth app-example in GitHub.

## 

Step 4: create a board

Now that you have an access token, navigate to the Create board reference documentation. To create a board, you need to construct an HTTP request. The documentation includes a sandbox to help you construct these requests by simply filling in the parameter fields.

Screenshot of the Create board documentation page  
**Figure 7.** Make a REST API call in the interactive REST API playground to create a board.

To make the create board API call:

1. Copy the access token you saved earlier into the **Authentication** field.
2. Input a name for your new board in the `name` field. For example, you could use "new board".
3. Click **Try It!** to execute the API call.
4. To see the result of the executed API call, open your Miro dashboard.  
You should see a new board, with the title you used in your API call.

The Miro REST API reference documentation is intentionally designed to make it easy for you to explore and test each API endpoint. Simply use the access token you created, and you can execute API calls from the documentation, and even view a log of your recent API activity.

Updated 3 months ago 

---

What's next

Create your Developer team to start building apps.

* Create a Developer team

* * Prerequisites  
   * * Step 1: create your app in Miro  
         * Step 2: configure your app in Miro  
         * Step 3: install the app  
         * Step 4: create a board
____

Website URL: https://developers.miro.com/?utm_source=sidebar
Website Title: Miro Developer Platform
Website Content:
Jump to Content

Miro Developer PlatformDocumentationResourcesMarketplaceCommunity

DocumentationAPI ReferenceChangelog

main

---

DocumentationResourcesMarketplaceCommunityLoginMiro Developer Platform

Login

main

Home
____

Website URL: https://developers.miro.com/docs/guided-onboarding
Website Title: Onboarding essentials
Website Content:
Jump to Content

Miro Developer PlatformMCPDocumentationResourcesMarketplaceCommunity

DocumentationAPI ReferenceChangelog

main

---

MCPDocumentationResourcesMarketplaceCommunityBuild your appMiro Developer Platform

Documentation

Build your app

main

Documentation

Onboarding essentials

Onboarding essentials

## Platform Essentials

* Introduction
* Web SDK vs REST API
* Getting started  
   * Developer team  
         * Create a Developer team  
         * Change the Developer team name  
         * Delete the Developer team  
   * Migrating a developer app
* App manifest
* Concepts  
   * Boards  
   * Board items  
         * Children inside parent items  
   * App card  
         * App card use cases  
         * Edit, update, and keep app cards synced  
         * Backend flow for app cards  
         * Enable REST API authentication from Miro's Web SDK authorization  
         * Enable 2-way sync between app cards and GitHub cards  
   * Card  
   * Connector  
   * Embed  
   * Events  
   * Frame  
   * Image  
   * Mind map (Experimental)  
   * Preview  
   * Shape  
   * Sticky note  
   * Storage  
   * Text  
   * Tag
* Migrate from v1 to v2  
   * Web SDK comparison guide  
   * Web SDK reference guide  
   * REST API comparison guide  
   * REST API reference guide

## MCP

* Introduction
* Miro's MCP Server
* Connecting to Miro's MCP Server
* Miro MCP Server Tools & Prompts
* Connecting Miro's MCP Server to MCP-compatible clients
* Tutorial: How to Generate Diagrams from Code w/ Miro MCP & VSCode + GitHub Copilot
* Tutorial: Build a Node.js app from a Miro Board with Miro MCP + Cursor
* Tutorial: How to Build a Landing Page from a Miro Board w/ Lovable + Miro MCP
* 🛠 Miro MCP Server FAQ and Troubleshooting

## Web SDK

* Introduction  
   * Miro Web SDK and board items  
   * App panels and modals
* Guided onboarding  
   * Onboarding essentials  
         * 1) Create your first board item with the Web SDK  
         * 2) Update an item's properties with \`sync()\`  
         * 3) Run your first app in Miro  
         * 4) Interact with your app in Miro  
         * 5) Join the conversation  
         * 6) Install a Marketplace app  
         * 7) Add Mirotone to an existing app  
         * Onboarding wrap-up  
         * Challenge: Where's Miro?  
   * Submit and share your app  
         * 1) Share an app outside of a developer team  
         * 2) Understand app submission requirements  
         * 3) Publish a Miro app  
         * 4) Share your ideas with us  
         * Submit and share wrap-up  
   * In-depth training modules  
         * 1) Create your 1st Miro app locally  
         * 2) Build a full-stack Miro app
* Getting started  
   * Quickstart  
   * Video: try the Web SDK in less than 1 minute  
   * Build your first Hello World app  
         * Build a Web SDK app  
         * Build a REST API app  
         * Build a full-stack (Next.js) app  
         * Enable running apps as instant apps
* How-Tos & tutorials  
   * Use the browser developer tools with the Miro Web SDK  
   * Update and sync item properties  
   * Add icon click to your app  
   * Add an icon to your app  
   * Add drag and drop to your app  
   * Add permission scopes to your app  
   * Add search and filter to your app  
   * Build a calendar app in Miro  
   * Convert sticky notes to shapes  
   * Create mind map from CSV  
   * Add custom actions to your app  
   * Deploy a Miro app  
   * Log in to a third-party service using OAuth  
   * Enable 2-way sync between app cards and GitHub cards  
   * Enable REST API authentication from Miro's Web SDK authorization  
   * Integrate a digital asset manager in Miro  
   * Convert frame coordinates to board coordinates  
   * SVG app icon optimization guidelines  
   * Upload images and SVGs as base64-encoded strings  
   * Connect the Miro Web SDK to a backend (Firebase)  
   * Video: Deploy a Next.js App on AWS Amplify  
   * Video: Integrate OpenAI + Miro  
   * Build collaborative app experiences  
   * Display banner/modal on a Miro board using DynamoDB  
   * Display banner/modal on a Miro board using AWS S3
* Reference  
   * Interact with boards and items  
   * Rate limiting  
   * Error handling  
   * Board  
   * Card  
   * Board UI  
   * Viewport  
   * Notifications  
   * App card  
   * Experimental  
   * Realtime Events  
   * Tag  
   * Custom Action Management  
   * Shape  
   * Frame  
   * Image  
   * Sticky Note  
   * Shape experimental  
   * Embed  
   * Connector  
   * Unsupported  
   * Mindmap Node  
   * Preview  
   * Text  
   * Storage collection  
   * Storage  
   * Collaboration  
   * Session  
   * Attention  
   * Group  
   * History  
   * Tools

## REST API

* Introduction
* Getting started  
   * Quickstart  
   * Video: try the REST API in less than 3 minutes  
   * Build your first Hello World REST API app
* How-To's & tutorials  
   * Get started with OAuth 2.0 and Miro  
   * Enable REST API authentication from Miro's Web SDK authorization  
   * Access Enterprise APIs  
   * Create sticky notes and tags  
   * Convert code to diagram with Miro PlantUML  
   * Get user info and email  
   * Create an image from a data URL source  
   * Work with connectors  
   * Securely manage boards and teams at scale  
   * Enable 2-way sync between app cards and GitHub cards  
   * Set up a test endpoint for webhooks with Pipedream  
   * Troubleshoot OAuth2.0  
   * Video: OAuth Essentials for Frontenders
* Miro Node.js client  
   * Miro Node.js client Readme  
   * Miro Node.js client quickstart for task automation  
   * Miro Node.js client quickstart with OAuth and Express  
   * Implement data storage  
   * Reference documentation
* Miro Python client
* Reference

## Marketplace

* Miro Marketplace
* Get ready for Marketplace  
   * App design guidelines  
   * App security guidelines  
   * App development policy  
   * App listing guidelines  
   * Build and deploy your app  
   * Your Marketplace profile
* Publish your app
* Monetization  
   * Monetization with Miro + Stripe  
   * Monetization with Miro + Salable (Subscription Management)  
   * Provide pricing details for your app
* App Metrics

## SCIM API

* Introduction
* User lifecycle management
* Getting started
* Concepts  
   * Rate limits
* Reference  
   * Users  
   * Groups  
   * Discovery features

## Live Embed

* Introduction
* Getting started  
   * Authentication  
   * oEmbed support
* How-Tos & tutorials  
   * Live Embed with a direct link  
   * Live Embed view-only mode  
   * Live Embed with BoardsPicker for registered users  
   * Live Embed with BoardsPicker for unregistered users
* Reference

## Resources

* Resources overview
* Changelog
* Roadmap
* Mirotone
* Miro app examples
* Miro Postman сollection
* Policies  
   * Developer terms of use  
   * App development policy  
   * Lifecycle policy  
   * Deprecation policy

Powered by 

# Onboarding essentials

## 

Guided onboarding for developers

Hey there, and welcome, dev! Join us on this guided onboarding flow, where we take you from making your first Web SDK call to creating your first Miro app locally.

You’ll find a mix of onboarding tasks and more in-depth modules to get you up to speed and have some fun along the way!

**💡 A few details 🧐**

Each task features:

* The learning objectives.
* An estimated time to completion.
* A progress bar to let you know where you're at and how much is left for you to complete the onboarding flow.
* The next task to take you to the next level of your journey towards creating your own Miro apps from scratch!

It's time to get rolling! Get started with onboarding Task 1: create your first board item with the Web SDK

Updated 3 months ago 

---

What's next

In the first task of the guided onboarding, you use the Miro Web SDK to create a board.

* Task 1: create your first board item with the Web SDK

* * Guided onboarding for developers
____

</external_links>
<plugin_info kind="matched_installed">
display_name: Supabase
description: Access your Supabase projects and perform tasks like managing tables, fetching config, and querying data.
skills:
  - supabase-postgres-best-practices: Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configurations.
  - supabase: Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues); client libraries and SSR integrations (supabase-js, @supabase/ssr) in Next.js, React, SvelteKit, Astro, Remix; auth issues (login, logout, sessions, JWT, cookies, getSession, getUser, getClaims, RLS); Supabase CLI or MCP server; schema changes, migrations, security audits, Postgres extensions (pg_graphql, pg_cron, pg_vector).
mcp_servers:
  - supabase
</plugin_info>
<timestamp>Saturday, Jun 6, 2026, 2:12 PM (UTC+4)</timestamp>
<user_query>
We are going to working on this: "https://miro.com/app/dashboard/space/0cSxp1dXLN16U5m28NBjgy " I created a template which is ai playground. I also came across the rest api settings page: "https://developers.miro.com/docs/rest-api-build-your-first-hello-world-app?utm_source=your_apps " and more developer resources: "https://developers.miro.com/?utm_source=sidebar ", "https://developers.miro.com/docs/guided-onboarding ". These are only few official documents that I have found about miro. This seems really useful to plan my entire idea out from PRD, memory and documents that I will lay out in the `@docs/` folder. What I do not wish to do is manually enter anything onto these boards. I have connected miro to lovable and cursor so far. Let's figure out what exactly you can do with this mcp. How useful is it to use as a developer? I can see the portotype of the app I wish to build but I do not want to waste my time building trash ui. Yes, the ui generated on miro is trash. I do not want to spend my time fixing the ui or anything. It's just a prototype and something for me to visualize what exactly i have written in my docs folder. I will then use that prototype to build a better ui frontend entirely on lovable(we got credits). This ui should be three.js components/3d components. Whatever that lovable works best with to build outstanding ui. Everyone is going to be vibe coding in this hackathon. We are going to be a step ahead by planning how to use each tool. We need to lay out what exactly is miro useful for in this process. We already have our backend with supabase and lovable does a decent job with the connectors. I will then use you to copy all the front end and some supabase created by lovable onto here. Yes, we are not going to be working on the lovable cloned repositry. We will copy, improve and paste the code into this project which is a much better workflow. I do not wish to waste time building this ui and the entire process that I have defined you. I will spend most of my time writing the docs. It's going to be your job to build the miro board, lovable prompts and copying the ui onto here. Supabase is mostly going to be our backend but it also depends on the track that we have been provided with. We need to lay out each and every single layer of architecture before we set out to build a single thing. What I have described does not cover securtiy, api, ci/cd pipelines, authentication, etc. You know exactly what is missing in everything that I have described - it lacks professionalism of an acual developer. This is going to be our stand out point. We will be professional and actually produce each and every single layer of operations to build an app from the start to the end. 

Explained you in a lot of detail regarding what exactly I wish to do in this hackathon. We do not have the track yet, we are setting up all our tools for success and laying out what needs to be step by step. Figure out what exactly all the tools and workflow I have described above can help me win this hackathon. I am participating as a solo developer, the hackathon is for 8 hours in total but only 4 hours for building. This is unrealistic to do each and every single layer of production and deployement. But what are we? Professionals, we do it all. We do it correctly, with no mistakes. We are going to stick to what hackathon winners do and build a beautiful app/website. Set me up for success here.
</user_query>

## Cursor

I'll research the current state of your project and the Miro MCP capabilities so I can give you an honest, professional workflow plan. Let me explore in parallel.

 The user is planning a hackathon project and wants me to help them understand what Miro MCP can do, assess its usefulness for development, and map out the complete architecture and workflow before they start building. They're looking for a strategic plan first, focusing on how to leverage Miro MCP alongside Lovable, Cursor, and Supabase.

I should explore what they've already set up in their docs folder and workspace, then clarify a few things like the hackathon theme and whether they want to re-authenticate with Miro since the connection timed out earlier. The core challenge is figuring out how to use Miro MCP to automatically generate boards and diagrams rather than manually creating them, and then integrating that into a professional workflow that covers security, APIs, CI/CD, and auth.

The workspace is empty — this is a greenfield project. Let me confirm the git state and check the Miro tool schemas so I can be precise about what the MCP can actually do.

 The workspace is completely empty—no existing structure or files to work with. Let me verify the current state with git to confirm we're starting from scratch.

This project is greenfield (no git, no files). I found the Miro MCP has more tools than the skill advertised — including `layout_*` (UI mockup generation), `prototype_*`, and `code_widget_*`. These are central to your goal, so let me read those schemas.

 I'm seeing there's actually a broader toolkit available beyond what was initially listed—there are prototype management tools, code widget controls for boards, layout and UI mockup generation capabilities, board management functions, commenting systems, and image handling. The layout tools in particular seem to be what powers the prototype UI generation feature.

I should focus on understanding the key schemas for layout and prototype creation since those are most relevant to the user's goal of generating a visualizable UI prototype on Miro that can then be rebuilt in Lovable. Let me examine the most critical ones to assess how useful Miro would actually be for this workflow.

I've now mapped exactly what this Miro MCP can do, and it changes the strategic picture significantly. Before I write the plan, here's the key finding and two scoping questions.

## What the Miro MCP actually is (honest developer assessment)

It is **not** a UI builder you ship, and you're right that Miro's own AI UI is throwaway. But via MCP it becomes something more useful: a **bidirectional visual planning surface** driven by your docs. The toolset is richer than the plugin advertised:

- `diagram_create` / `diagram_get_dsl` — architecture diagrams, ERDs, sequence/flow diagrams, system maps (this is the highest-value tool for you).
- `prototype_create` / `prototype_read` — I generate **clean HTML screens**, Miro renders them as a clickable prototype with navigation flow. Crucially, `prototype_read` gives back HTML + a structural summary (sections, components, nav connectors).
- `layout_create` / `layout_get_dsl` — native Miro wireframe items (frames, shapes) from a DSL.
- `doc_create` / `doc_update`, `table_create` / `table_sync_rows`, `code_widget_create` — docs, spec tables, code snippets on the board.
- `context_explore` / `context_get` — read your existing "AI playground" board back into context.

**The strategic insight that wins you time:** the prototype is *not* throwaway. Because I author the prototype HTML from your `docs/`, that same HTML + structure becomes the **exact spec I hand to Lovable** ("rebuild this screen as a Three.js/R3F experience"). So Miro = the visual contract between your docs and Lovable, not manual busywork. You never type on the board — I drive it all through MCP. (One caveat: Miro auth timed out earlier; we'll need to re-trigger it before I can push to the board.)

Before I lock the full plan, two decisions that change its shape:

 I'm getting a clearer picture of how the Miro MCP works—the `prototype_create` function takes HTML screens and renders them as interactive prototypes on the board, which means I can generate HTML and have Miro turn it into clickable prototypes with navigation connectors. The `prototype_read` function lets me read back the HTML, structural summary, and navigation flow, while `layout_create` and `layout_get_dsl` handle the layout side of things.

The other capabilities—`diagram_create` for flowcharts and architecture diagrams, `doc_create` for markdown docs, `table_create` for task trackers and data models, `code_widget_create` for syntax-highlighted snippets, and `context_explore` to read existing board contents—all give me a rich set of tools for visual planning.

The real insight here is that Miro MCP isn't a UI builder for shipping—it's a bidirectional visual planning surface. The user mentioned the UI generated on Miro is trash, but that's probably from Miro's built-in AI. With MCP and Cursor, I can generate clean HTML prototypes from their docs, push them as prototype screens, and feed that same HTML structure into Lovable as the spec. The prototype becomes the bridge between planning and implementation, not throwaway work.

Now I have enough to form a plan, though the request is huge and somewhat ambiguous. The user wants an honest assessment of Miro MCP usefulness for developers and a complete tool and workflow architecture for their setup.

Before I commit to a plan, I need to resolve some critical ambiguities. Miro auth timed out, so I can't actually push to the board right now—but I can still set up the docs and workflow. The bigger question is what they actually want from this session: are they looking for just the strategy, PRD template, architecture docs, and workflow playbook (track-agnostic), or do they also want me to scaffold the actual app repo with Next.js, Supabase, and CI/CD setup? Given that there's no track yet and they said "set me up for success," I think the answer is mostly documentation and workflow scaffolding, with repo decisions deferred.

There's also the tech stack question for the final app repo—since Lovable typically generates React + Vite + Tailwind + Supabase, and they want three.js/3D, the target is probably Vite + React + TypeScript + Tailwind + React Three Fiber, or possibly Next.js. That choice matters for the architecture doc. I should ask a couple of focused questions to clarify scope and target framework before I finalize the plan.

Locked in: **docs-only** playbook, architecture targeting **Next.js (App Router) + react-three-fiber + Tailwind + Supabase**, fully track-agnostic. Here's the plan.

 The user wants a docs-only playbook for a Next.js stack, so I'm planning to create a markdown-based documentation structure in the docs/ folder that's track-agnostic but tailored to the Next.js architecture.

I'm organizing the docs into five main sections: a quick-start guide, strategy and tool guidance (including the Miro MCP workflow), product templates, architecture layers and conventions, step-by-step workflow guides for moving from docs to Miro to Lovable to Cursor, and a memory file for tracking decisions and context throughout the build.

I'm realizing this could be a lot of files, so I need to keep it tight and actionable for a 4-hour sprint — everything should be skimmable and directly useful. I'm also considering whether to include an AGENTS.md at the root level as the proper Cursor memory mechanism for persistent guidance and conventions, since the user emphasized comprehensive coverage across all layers.

For the 4-hour build window, I'm mapping out a realistic timeline: locking the MVP scope first, pushing architecture and schema to Miro, having Lovable generate the R3F UI while Supabase gets wired, then migrating that into the Next.js repo for refinement, wiring auth and APIs, deploying to Vercel, and leaving buffer for a demo script. The architecture spans Next.js App Router with R3F and Tailwind on the frontend, Supabase Auth with SSR middleware, Next.js route handlers and server actions for the backend, Postgres with RLS policies for data, environment-based security, GitHub and Vercel for CI/CD, and minimal observability through Vercel's built-in tools.

Now I'm laying out the documentation structure with markdown file paths and pulling in references from the Miro files and external docs I've reviewed.

**Tool calls:**

- `Glob` — pattern `**/*`, path `D:\projects\hackathon\docs`
- `Glob` — pattern `*`, path `D:\projects\hackathon`
- `Read` — `C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\SERVER_METADATA.json`
- `Shell` — `git -C "D:\projects\hackathon" status 2>&1; echo "---FILES---"; ls -la "D:\projects\hackathon" 2>&1`
- `Glob` — pattern `tools/*.json`, path `C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro`
- `Read` — `C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\layout_get_dsl.json`
- `Read` — `C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\layout_create.json`
- `Read` — `C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\prototype_create.json`
- `Read` — `C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\prototype_read.json`
- `Read` — `C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\code_widget_create.json`
- `AskQuestion` — `{"title":"Scope & stack for the hackathon setup","questions":[{"id":"scope","prompt":"What do you want this session to produce? (You have no track yet, so everything will be track-agnostic and reusable.)","options":[{"id":"docs_only","label":"Just the docs/ playbook: PRD template, memory/context fil…`
- `CreatePlan` — `{"name":"Hackathon Docs Playbook","overview":"Build a complete, track-agnostic docs/ playbook in D:\\projects\\hackathon that defines the winning solo-hackathon workflow (Miro MCP -> Lovable -> Cursor -> Supabase -> Vercel), a fill-in PRD, a full professional architecture covering every layer (auth,…`

## You

<timestamp>Saturday, Jun 6, 2026, 2:36 PM (UTC+4)</timestamp>
<user_query>
You are a senior engineer preparing to win a solo hackathon. Track unknown — drops at start. Build window: ~4 hours. Stack: Next.js App Router + react-three-fiber + Tailwind + Supabase + Vercel.
Tools available: Miro, Lovable, Cursor, GitHub Copilot, Kiro, ElevenLabs, Claude (with MCP tools). The goal of this session is pure research. No app code. No bloated doc structure. Output is 3 files.

Part 1 — Deep tool research
Use web search on each tool. Read actual docs, changelogs, community posts from 2025–2026. Do not assume anything. For every capability claim, note the source URL. If you can't verify something, mark it [UNVERIFIED].
Miro

What is the full list of MCP tools available in the Miro MCP server? What does each one actually do?
How does prototype_create work — what HTML does it accept, what does it render on the board?
What does prototype_read return — is the output structured enough to paste directly into a Lovable prompt as a UI spec?
What are diagram_create, layout_create, context_explore good for, and what are their real limits?
Auth expiry: what breaks and how fast? What's the recovery path mid-sprint?
Honest verdict: what is Miro genuinely irreplaceable for vs. what's just friction?

Lovable

Current state (mid-2026): does it support react-three-fiber and 3D scenes out of the box?
How deep is its Supabase integration — auth, RLS, schema generation, edge functions?
What breaks when you export/copy its output into a standalone Next.js repo?
What prompting patterns produce the least throwaway code and the most portable components?
Can it scaffold a full feature (auth + data + UI) from a single prompt, or does it fall apart beyond simple CRUD?
What's the honest failure mode that trips up people at hackathons?

Cursor

What does Cursor's repo-context (codebase indexing, @codebase, .cursorrules) actually give you that a plain chat interface doesn't?
What is the optimal workflow for handing it a Lovable-generated frontend and saying "clean this up / wire this to Supabase"?
How does Cursor handle multi-file refactors in 2026 — is it reliable enough to trust for a 4h sprint?
What do .cursorrules / AGENTS.md conventions actually affect in Cursor's behavior?
Where does Cursor fall apart and slow you down vs. speed you up?

GitHub Copilot

Beyond autocomplete: what does Copilot for PRs do in 2026 — summary, review, security scan?
Is there a CLI or workspace command that lets you trigger a review without opening a PR?
Can it catch AI-generated slop patterns (dead code, unnecessary abstractions, wrong error handling)?
For a solo 4h build, what is the real ROI? Is it worth context-switching to it at all?
Honest verdict: is there a moment in the sprint where Copilot is the best tool, or is it purely ambient autocomplete?

Kiro

What is Kiro actually — a doc generator, a spec agent, or an execution agent? What does it produce?
Walk through the full Kiro workflow: requirements → design → tasks. What does each artifact look like?
Can Kiro's task output be fed directly into Cursor as structured context that changes how Cursor codes?
What is Kiro's latency for a non-trivial feature spec? Is it fast enough to use mid-sprint or only in pre-build?
What does Kiro do better than just writing a PRD yourself or having an LLM write one?
Honest verdict: use it in the 20 minutes before the track drops, or skip it entirely?

ElevenLabs

Full product surface in 2026: voice generation, sound effects API, conversational AI agents, dubbing, what else?
What is the real-time conversational AI agent feature — what does it take to embed one in a web app?
What APIs exist and what do they return? Is there an SDK for Next.js?
Integration time estimate: how long does it realistically take to go from zero to a working ElevenLabs feature in a Next.js app?
What's a demo-worthy use that takes under 30 minutes and creates a wow moment for judges?
Honest verdict: worth the integration time for a 4h build, or better saved for polish in the last 20 minutes?

Part 2 — Winning problem research
Search: "hackathon winning strategies 2025 2026", "what makes a hackathon demo win", "hackathon judging criteria breakdown", "solo hackathon tips from winners".
Answer these specifically:

What do judges consistently reward across different tracks?
What does a 90-second demo need to show to win?
What's the pattern of demos that look impressive but lose?
How should problem selection change based on available tools (especially 3D/visual stack + voice)?
What problem types naturally benefit from react-three-fiber as a visual layer?

Part 3 — Role assignment and handoff chain
Based only on what the research above revealed, produce:

A single sentence per tool: "This tool owns ___."
A linear timeline showing the 4h sprint — who does what in each 20-minute block, and what artifact gets handed off.
Flag any tools that are redundant given the stack, and say so plainly.

Output
Write exactly 3 files:
docs/RESEARCH.md — all Part 1 findings, organized by tool, with source URLs. Honest, no marketing. If something is weak, say it's weak.
docs/PLAYBOOK.md — the complete 4h sprint plan derived from the research: role per tool, handoff chain, 20-minute timeline blocks, winning-demo principles from Part 2. This is the one file you open at the start of the hackathon.
AGENTS.md (repo root) — conventions every agent in this repo must follow. Tool boundaries, naming conventions, what not to do.
No other files. No PRD (track unknown). No architecture (problem unknown). Those come after the track drops.
</user_query>

## Cursor

The plan has changed substantially — this is now a pure-research task with exactly 3 markdown deliverables. The 3 outputs are all markdown, and you've given an explicit directive to write them, so I'll do the verified research first (read-only), then write the files.

Let me start the deep research. I already have the authoritative Miro MCP tool list from the installed server schemas; I'll corroborate behavior and research the other tools via web in parallel.

 The user has given me a new, specific directive: three files with web search verification for each tool. I'm in Plan mode, so I need to decide whether to update the plan and ask for confirmation or proceed directly with this clear specification.

The key tension is between the system reminder that I must not make edits until explicitly instructed, and the plan mode guardrail that allows markdown file edits. Since the output files are all markdown and the user has explicitly asked me to write them, I think the right move is to proceed with the research (which is read-only and definitely allowed) and then write the three markdown files.

For the research phase, I have the tool schemas locally from the installed MCPs, so I can rely on those as the authoritative source rather than doing web searches for basic tool information. I should focus my searches on the strategic analysis and competitive positioning aspects instead. I'll continue with the remaining searches from wave 1 and then move into wave 2 to cover hackathon strategy. I'm also planning to enumerate the full Miro tool list from the 35 tool files I've reviewed to ensure accuracy for the RESEARCH.md documentation.

Strong results. Now the second wave: Cursor refactor reliability, Copilot CLI, Kiro latency/CLI, and the Part 2 winning-demo research.

 Now I'm moving into the second batch of searches—looking at Cursor's multi-file refactoring reliability in 2026 and where it breaks down, GitHub Copilot's CLI code review capabilities without needing a PR, and Kiro's latency performance with its CLI tool.

I'm also queuing up searches on hackathon winning strategies, what makes a 90-second demo compelling, demos that look flashy but fail with judges, and when react-three-fiber actually adds value to products versus being unnecessary overhead.

Let me run all of these in parallel.

I have deep, sourced coverage on every tool plus the winning-demo research. One targeted gap remains — the user specifically asked about Miro MCP auth expiry behavior, so let me verify that precisely before writing.

 I've got solid research across all the tools and the winning-strategy angle ready to write the three files. I need to double-check the Miro auth expiry behavior since the user specifically asked about what breaks, how quickly, and the recovery path mid-sprint — but I'm missing concrete token expiry duration data for the Miro MCP, so I'll need to flag that gap carefully.

I now have everything I need, including the critical Miro auth gotcha (the "Last One Wins" 1:1 rule — directly relevant since you've connected Miro to both Lovable and Cursor). Writing the three deliverables now.

 The Miro MCP "Last One Wins" authentication rule is the critical gotcha here — since they've connected Miro to both Lovable and Cursor, authenticating in one will drop the other. The recovery path is clearing all MCP tokens in Cursor and reconnecting through the MCP settings while viewing a board in the correct team. Now I'm ready to write out the three files.

I'll organize them by tool with verified sources and clear [UNVERIFIED] tags where needed. Starting with RESEARCH.md as the comprehensive reference, then PLAYBOOK.md for the operational guide, and finally AGENTS.md for the agent-specific setup. Let me write these deliverables now. layout_create handles native board items like frames, sticky notes, shapes, and text via DSL in bulk, useful for wireframes but can hit rate limits with hundreds of items. Auth is the critical constraint—Miro uses OAuth with a "last one wins" rule that drops other connections, so having it linked to both Lovable and Cursor creates friction; the recovery path is clearing MCP tokens in Cursor and reconnecting. Miro's real value is architecture diagrams from documentation and bidirectional prototype HTML as a spec contract, though manual board management and AI credit costs add overhead. Lovable supports 3D via React Three Fiber and has the deepest backend integration through Supabase, auto-generating schema, tables, RLS policies, auth flows, and edge functions while managing secrets securely.

The main risk with Lovable's Supabase integration is RLS gaps—AI-generated policies often default to overly permissive rules, and there's a documented case of 18k users exposed due to missing RLS, so auditing is mandatory. Exporting to Next.js requires translating Vite environment variables, React Router file structure to App Router, adding 'use client' directives, converting useEffect fetches to Server Components, and swapping Supabase client patterns for the SSR cookie client, though most components port with minimal edits. Lovable scaffolds full CRUD features with Supabase cleanly but struggles with anything beyond simple data operations or complex business logic. Cursor's strength is codebase indexing through a local vector index and semantic search via @codebase, with .cursorignore and AGENTS.md files controlling what gets indexed.

Multi-file refactoring in Cursor degrades significantly past 5 files due to context saturation, often failing around 9+ files with wrong edits or hallucinated imports—reliability jumps from under 50% to over 90% by chunking work into ≤5 files, committing between chunks, pinning types upfront, and using Tab/Inline Edit for 60-70% of changes instead of full Agent mode. GitHub Copilot's 2026 PR review feature runs as an agentic tool that self-reviews code before opening a PR, applying severity labels and grouped comments, with the coding agent also handling code scanning, secret scanning, and dependency CVE checks in workflows.

The CLI `/review` command on staged changes is the highest-ROI moment—it catches security, auth, and logic bugs before commit without touching files. Kiro is an AWS agentic IDE launched in July 2025 that generates structured specs (requirements.md, design.md, tasks.md) from requirements or design-first workflows, and those task files can be pasted directly into Cursor as context.

For a 4-hour sprint, Kiro's spec generation takes minutes and works best in the 20 minutes before/after a track drop to establish a single source of truth, then hand off tasks to Cursor—skip running Kiro's executor mid-sprint due to latency and interaction limits. ElevenLabs in 2026 offers TTS, sound effects, ElevenAgents (real-time conversational AI with voice+chat, 70+ languages, MCP support), and SDKs across React, React Native, Swift, and Python; embedding a conversational agent uses the React hook with WebRTC for voice and WebSocket for text, secured via domain allowlist or optional auth.

Integrating a voice agent into Next.js takes 20–40 minutes with the public agent + React hook + optional API route for signed URLs if private—a demo-worthy live voice agent grounded in a knowledge base is a strong wow moment, so prioritize it only if voice is core to the golden path, not last-minute polish. Judges consistently reward clear problem definition, working stable demos, measurable impact, differentiation, and memorable storytelling across a ~5x20% rubric; a 90-second pitch hooks with a relatable stat (15s), delivers one-line solution + differentiator, shows the golden path in action, and closes with impact—the pattern that loses is overscoping, building a model instead of a product, requiring too much explanation, or depending on live APIs.

For the 3D + voice stack, pick problems where spatial representation reveals insight (data hard to grasp in 2D) or voice removes friction (hands-free, accessibility, conversational onboarding); R3F shines for data viz (globes, point clouds, 3D charts from CSV), product configurators, network maps, geographic data, or immersive storytelling with camera waypoints—3D must be load-bearing to the insight, not decoration.

Each tool owns a specific piece: Kiro owns the spec, Miro owns the visual contract and architecture, Lovable owns first-pass UI + Supabase scaffolding, Supabase owns data/auth/RLS/serverless logic, Cursor owns the real repo and integration, Copilot CLI owns the pre-commit security gate, ElevenLabs owns voice if it's core, and Vercel owns deployment.

Watch for redundancy: Kiro vs Cursor planning (Kiro optional if time-pressed), Copilot autocomplete vs Cursor Tab (only the CLI review gate matters), Lovable vs hand-wiring Supabase (Lovable first-pass but RLS must be re-audited), and Miro prototype vs Lovable UI (Miro is the spec, don't polish it twice).

The 4-hour timeline breaks into 12 twenty-minute blocks, starting with pre-build setup (tools authed, repo skeleton, AGENTS.md ready). Block 0 locks the problem to the track—one-sentence problem statement, golden path, the one wow moment—and decides if 3D and voice are truly load-bearing, producing tasks.md and a demo script. Block 1 moves to Miro for the architecture diagram and flow.

Block 1 continues with prototype HTML screens of the golden path and finalizes the Supabase schema. Block 2 feeds those prototype screens into Lovable as a UI spec, building the R3F interface and connecting Supabase auth and RLS. Block 3 iterates the golden-path screens in Lovable while tables and RLS are generated, then exports to GitHub. Block 4 scaffolds Next.js in Cursor, copies components from the export in chunks of five files or fewer, and commits between each. Block 5 fixes Vite-to-Next gotchas like environment variables, routing, and 'use client' directives, then wires Supabase SSR cookie auth with middleware. Block 6 re-audits RLS with negative tests, implements route handlers and server actions, and optimizes the R3D scene with instanced meshes and device pixel ratio caps. Block 7 either integrates ElevenLabs voice if it's core to the experience or deepens the golden path further.

Block 8 runs the Copilot CLI review gate on staged changes to catch security issues and bugs, fixes any findings, then deploys to Vercel for a preview URL. Block 9 freezes features, seeds deterministic demo data with offline fallback, and pre-records a backup video. Block 10 polishes only what's on the golden path and does a quick Lighthouse pass. Block 11 rehearses the 90-second pitch, writes a README for judges, and submits early. The hard constraints are no new features after 3:00, commits between chunks, mandatory RLS negative tests and backup video, 3D as load-bearing, and voice only if core.

Now I'm writing AGENTS.md to document conventions every agent must follow—tool boundaries, naming, and what to avoid—keeping it tight since it loads into context every session. I'm creating all three files under the hackathon workspace at D:\projects\hackathon.

Now I'm starting RESEARCH.md.

Now the playbook.

Now the AGENTS.md at repo root — kept tight since it loads into every agent's context.

I left one shortened placeholder URL in `RESEARCH.md`. Let me fix it to the full link.

 I should verify the files are in place and check for any lint issues, then update the plan file to reflect the new direction since the scope shifted. Let me also make sure there aren't any broken links left in the research section.

Done. Three files written, all sourced and honest.

## What I produced

- **`docs/RESEARCH.md`** — Part 1 + 2, organized by tool with source URLs and `[UNVERIFIED]` tags where I couldn't confirm specifics.
- **`docs/PLAYBOOK.md`** — Part 3 (ownership + redundancy), winning principles, the twelve 20-minute blocks, pre-build checklist, hard rules. This is the file you open when the track drops.
- **`AGENTS.md`** (repo root) — tight conventions, tool boundaries, security/RLS rules, migration rules, multi-file discipline, and a "Do NOT" list. Kept short so it's cheap to load into every agent.

## The findings that should change how you operate

- **Miro's one real superpower is the prototype loop, not the diagrams.** `prototype_create` renders actual HTML, and `prototype_read` returns that HTML *plus* a structured component/interaction/navigation summary — so the prototype becomes a literal spec you paste into Lovable. That's the irreplaceable bit. Everything else is friction (image-upload dance, AI-credit `context_get`, board housekeeping).
- **Critical auth gotcha for your exact setup:** Miro enforces a "Last One Wins" 1:1 rule — authenticating in Cursor can silently drop your Lovable connection and vice versa. Recovery is `Cursor: Clear all MCP Tokens` → reconnect while viewing a board in the right team. Source: [Miro MCP FAQ](https://developers.miro.com/docs/miro-mcp-server-faq-and-troubleshooting).
- **Lovable → Next.js is a port, not an export.** Lovable ships Vite + React Router + client Supabase; budget time for `VITE_`→`NEXT_PUBLIC_`, App Router routing, `'use client'`, `@supabase/ssr`, and a fresh shadcn install. And its **RLS is the documented failure mode** — assume it's wrong and run a negative test.
- **Two tools are largely redundant for you:** Copilot ambient autocomplete (Cursor Tab covers it — use only the CLI `/review` gate), and Kiro (Cursor Plan mode + a `tasks.md` does the same; use Kiro only if EARS structure earns 20 min). I flagged both plainly in the playbook.
- **ElevenLabs is conditional:** ~20–40 min to a working voice agent, high wow — but only worth it if voice is load-bearing on the golden path.

I stayed in plan mode and only wrote the three markdown files you specified — no app code, no PRD, no architecture (correctly deferred until the track drops). One note: the `agent-tools/*.txt` files you may see are temp dumps the web-search tool created; they're not part of the deliverables and can be deleted.

If you want, when you're ready to build I can scaffold the pre-build checklist items (Next.js repo + Supabase client + Vercel link) — just say the word and I'll switch to agent mode.

**Tool calls:**

- `WebSearch` — `{"search_term":"Miro MCP server tools prototype_create prototype_read 2026 capabilities","explanation":"Verify Miro MCP tool behavior against official docs"}`
- `WebSearch` — `{"search_term":"Lovable AI react three fiber 3D scenes support 2026","explanation":"Check if Lovable supports R3F/3D out of the box"}`
- `WebSearch` — `{"search_term":"Lovable Supabase integration auth RLS edge functions schema 2026","explanation":"Assess Lovable Supabase integration depth"}`
- `WebSearch` — `{"search_term":"Lovable export code to standalone Next.js repo problems portability","explanation":"Find what breaks moving Lovable output to Next.js"}`
- `WebSearch` — `{"search_term":"Cursor AGENTS.md .cursorrules codebase indexing @codebase 2026","explanation":"Verify Cursor repo-context features and rules behavior"}`
- `WebSearch` — `{"search_term":"GitHub Copilot pull request code review security scan 2026 features","explanation":"Research Copilot PR review and security capabilities"}`
- `WebSearch` — `{"search_term":"AWS Kiro spec driven development requirements design tasks workflow","explanation":"Understand what Kiro is and produces"}`
- `WebSearch` — `{"search_term":"ElevenLabs API products conversational AI agents SDK Next.js 2026","explanation":"Map ElevenLabs product surface and Next.js SDK"}`
- `WebSearch` — `{"search_term":"Cursor multi-file refactor reliability 2026 agent where it fails large changes","explanation":"Assess Cursor multi-file refactor reliability and failure modes"}`
- `WebSearch` — `{"search_term":"GitHub Copilot CLI code review command without opening pull request 2026","explanation":"Find Copilot CLI/local review trigger without a PR"}`
- `WebSearch` — `{"search_term":"AWS Kiro CLI speed latency spec generation time autopilot vibe coding 2026","explanation":"Gauge Kiro latency and CLI availability for mid-sprint use"}`
- `WebSearch` — `{"search_term":"hackathon winning strategies 2026 what judges reward demo tips from winners","explanation":"Gather hackathon winning strategy and judging criteria"}`
- `WebSearch` — `{"search_term":"what makes a hackathon demo win 90 second pitch judging criteria breakdown","explanation":"Understand winning demo structure and judging criteria"}`
- `WebSearch` — `{"search_term":"hackathon projects that look impressive but lose common mistakes demo fails","explanation":"Identify anti-patterns of impressive-but-losing demos"}`
- `WebSearch` — `{"search_term":"react three fiber use cases product ideas data visualization 3D web app 2026","explanation":"Find problem types that benefit from R3F visual layer"}`
- `WebSearch` — `{"search_term":"Miro MCP server OAuth authentication token expiry re-authenticate session 2026","explanation":"Verify Miro MCP auth/token expiry and recovery path"}`
- `Write` — `D:\projects\hackathon\docs\RESEARCH.md`
- `Write` — `D:\projects\hackathon\docs\PLAYBOOK.md`
- `Write` — `D:\projects\hackathon\AGENTS.md`
- `StrReplace` — `D:\projects\hackathon\docs\RESEARCH.md`

## You

<user_query>
# Goal

Implement the plan as specified, it is attached for your reference. Do NOT edit the plan file itself.

To-do's from the plan have already been created. Do not create them again. Mark them as in_progress as you work, starting with the first one. Don't stop until you have completed all the to-dos.
</user_query>

## Cursor

I'll implement the full docs playbook from the plan. First I'll see what's already in the repo, then work through each todo in order.

[REDACTED]

I'll read the existing docs and align the new structure with them.

[REDACTED]

Creating the full docs structure per the plan, integrating with the existing RESEARCH.md and PLAYBOOK.md.

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

All plan todos are complete. Here's what was built:

## Delivered structure (19 files)

| Section | Files |
|---------|-------|
| **Index** | `docs/00-START-HERE.md` |
| **Strategy** | `hackathon-playbook.md`, `tool-matrix.md`, `miro-mcp-guide.md` |
| **Product** | `PRD-template.md`, `prd.md` (placeholder) |
| **Architecture** | `system-architecture.md`, `data-model.md`, `api-contract.md`, `security.md`, `cicd-deploy.md` |
| **Workflow** | `docs-to-miro.md`, `miro-to-lovable.md`, `lovable-to-cursor.md` |
| **Memory** | `decisions.md`, `prompts-library.md` |
| **Root** | `AGENTS.md` (updated with links to full docs tree) |

Existing **`docs/RESEARCH.md`** and **`docs/PLAYBOOK.md`** are kept and linked from `00-START-HERE.md` — RESEARCH = sourced tool deep-dive; PLAYBOOK = minute-by-minute 20-min blocks.

## Where to start

1. **Now:** `docs/00-START-HERE.md`
2. **When track drops:** fill `docs/02-product/prd.md` → open `docs/PLAYBOOK.md`
3. **Any agent session:** `AGENTS.md` + `docs/05-memory/prompts-library.md`

No app code was written (per plan). Next step when you're ready: scaffold the Next.js repo from the pre-build checklist in `docs/03-architecture/cicd-deploy.md`.

[REDACTED]

**Tool calls:**

- `Glob` — pattern `**/*`, path `D:\projects\hackathon`
- `TodoWrite` — `{"todos":[{"id":"index","content":"Create docs/00-START-HERE.md index with usage guide and links","status":"in_progress"}],"merge":true}`
- `Read` — `D:\projects\hackathon\AGENTS.md`
- `Read` — `D:\projects\hackathon\docs\PLAYBOOK.md`
- `Read` — `D:\projects\hackathon\docs\RESEARCH.md`
- `Write` — `D:\projects\hackathon\docs\00-START-HERE.md`
- `Write` — `D:\projects\hackathon\docs\01-strategy\hackathon-playbook.md`
- `Write` — `D:\projects\hackathon\docs\01-strategy\tool-matrix.md`
- `Write` — `D:\projects\hackathon\docs\01-strategy\miro-mcp-guide.md`
- `Write` — `D:\projects\hackathon\docs\02-product\PRD-template.md`
- `Write` — `D:\projects\hackathon\docs\02-product\prd.md`
- `TodoWrite` — `{"todos":[{"id":"index","content":"Create docs/00-START-HERE.md index with usage guide and links","status":"completed"},{"id":"strategy","content":"Write docs/01-strategy/ files: hackathon-playbook (timeline + judging criteria), tool-matrix, miro-mcp-guide","status":"completed"},{"id":"product","con…`
- `Write` — `D:\projects\hackathon\docs\03-architecture\system-architecture.md`
- `Write` — `D:\projects\hackathon\docs\03-architecture\data-model.md`
- `Write` — `D:\projects\hackathon\docs\03-architecture\api-contract.md`
- `Write` — `D:\projects\hackathon\docs\03-architecture\security.md`
- `Write` — `D:\projects\hackathon\docs\03-architecture\cicd-deploy.md`
- `Write` — `D:\projects\hackathon\docs\04-workflow\docs-to-miro.md`
- `Write` — `D:\projects\hackathon\docs\04-workflow\miro-to-lovable.md`
- `Write` — `D:\projects\hackathon\docs\04-workflow\lovable-to-cursor.md`
- `Write` — `D:\projects\hackathon\docs\05-memory\decisions.md`
- `Write` — `D:\projects\hackathon\docs\05-memory\prompts-library.md`
- `Write` — `D:\projects\hackathon\AGENTS.md`
- `TodoWrite` — `{"todos":[{"id":"architecture","content":"Write docs/03-architecture/ files: system-architecture, data-model, api-contract, security, cicd-deploy","status":"completed"},{"id":"workflow","content":"Write docs/04-workflow/ files: docs-to-miro, miro-to-lovable, lovable-to-cursor","status":"completed"},…`
- `Glob` — pattern `**/*`, path `D:\projects\hackathon`

## You

<user_query>
Implement the plan as specified, it is attached for your reference. Do NOT edit the plan file itself.

To-do's from the plan have already been created. Do not create them again. Mark them as in_progress as you work, starting with the first one. Don't stop until you have completed all the to-dos.
</user_query>

## You

<user_query>
For the code present, we get this error:
```
Value is not accepted. Valid values: "PreToolUse", "PostToolUse", "PostToolUseFailure", "PostToolBatch", "Notification", "UserPromptSubmit", "UserPromptExpansion", "SessionStart", "SessionEnd", "Stop", "StopFailure", "SubagentStart", "SubagentStop", "PreCompact", "PostCompact", "PermissionRequest", "PermissionDenied", "Setup", "TeammateIdle", "TaskCreated", "TaskCompleted", "Elicitation", "ElicitationResult", "ConfigChange", "WorktreeCreate", "WorktreeRemove", "InstructionsLoaded", "CwdChanged", "FileChanged", "MessageDisplay".
```
Fix it, verify, and then give a concise explanation. @.claude/settings.json:2-5 
</user_query>

## Cursor

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

**Fix:** Renamed the hook event keys in `.claude/settings.json`:

- `PreToolCall` → `PreToolUse`
- `PostToolCall` → `PostToolUse`

**Verified:** JSON parses cleanly; all three hook keys (`PreToolUse`, `PostToolUse`, `UserPromptSubmit`) match the schema’s allowed event names.

**Why:** Claude Code’s hooks schema uses `PreToolUse` / `PostToolUse`, not `PreToolCall` / `PostToolCall`. The old names look like Cursor-style naming, but this file is validated against Claude’s event list — hence the error. Your matchers and hook commands are unchanged; only the event labels were wrong.

[REDACTED]

**Tool calls:**

- `Read` — `D:\projects\hackathon\.claude\settings.json`
- `Read` — `C:\Users\Anant Gupta\.cursor\skills-cursor\create-hook\SKILL.md`
- `Grep` — pattern `PreToolUse|PreToolCall`, path `D:\projects\hackathon`
- `Glob` — pattern `**/*`, path `D:\projects\hackathon\.claude`
- `StrReplace` — `D:\projects\hackathon\.claude\settings.json`
- `StrReplace` — `D:\projects\hackathon\.claude\settings.json`
- `Shell` — `python -c "import json; p=r'D:\projects\hackathon\.claude\settings.json'; d=json.load(open(p)); valid={'PreToolUse','PostToolUse','PostToolUseFailure','PostToolBatch','Notification','UserPromptSubmit','UserPromptExpansion','SessionStart','SessionEnd','Stop','StopFailure','SubagentStart','SubagentStop','PreCompact','PostCompact','PermissionRequest','PermissionDenied','Setup','TeammateIdle','TaskCreated','TaskCompleted','Elicitation','ElicitationResult','ConfigChange','WorktreeCreate','WorktreeRemove','InstructionsLoaded','CwdChanged','FileChanged','MessageDisplay'}; keys=set(d.get('hooks',{}).keys()); bad=keys-valid; print('JSON: OK'); print('Hook keys:', sorted(keys)); print('Invalid:', sorted(bad) if bad else 'none')"`

## Actions Taken
- Summary: Edited settings.json, AGENTS.md, prompts-library.md, decisions.md, lovable-to-cursor.md
- Files changed (Cursor): 20
- Lines: +2369 / -2
- Files touched (from tool calls): C:\Users\Anant Gupta\.cursor\plugins\cache\cursor-public\miro\9627168a40c694c61a8734cbcdd452d21e560bdc\skills\miro-mcp\SKILL.md, C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\STATUS.md, C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro, C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\mcp_auth.json, D:\projects\hackathon\docs, D:\projects\hackathon, C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\SERVER_METADATA.json, C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\layout_get_dsl.json, C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\layout_create.json, C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\prototype_create.json, C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\prototype_read.json, C:\Users\Anant Gupta\.cursor\projects\d-projects-hackathon\mcps\plugin-miro-miro\tools\code_widget_create.json, D:\projects\hackathon\docs\RESEARCH.md, D:\projects\hackathon\docs\PLAYBOOK.md, D:\projects\hackathon\AGENTS.md, D:\projects\hackathon\docs\00-START-HERE.md, D:\projects\hackathon\docs\01-strategy\hackathon-playbook.md, D:\projects\hackathon\docs\01-strategy\tool-matrix.md, D:\projects\hackathon\docs\01-strategy\miro-mcp-guide.md, D:\projects\hackathon\docs\02-product\PRD-template.md, D:\projects\hackathon\docs\02-product\prd.md, D:\projects\hackathon\docs\03-architecture\system-architecture.md, D:\projects\hackathon\docs\03-architecture\data-model.md, D:\projects\hackathon\docs\03-architecture\api-contract.md, D:\projects\hackathon\docs\03-architecture\security.md, D:\projects\hackathon\docs\03-architecture\cicd-deploy.md, D:\projects\hackathon\docs\04-workflow\docs-to-miro.md, D:\projects\hackathon\docs\04-workflow\miro-to-lovable.md, D:\projects\hackathon\docs\04-workflow\lovable-to-cursor.md, D:\projects\hackathon\docs\05-memory\decisions.md, D:\projects\hackathon\docs\05-memory\prompts-library.md, D:\projects\hackathon\.claude\settings.json, C:\Users\Anant Gupta\.cursor\skills-cursor\create-hook\SKILL.md, D:\projects\hackathon\.claude
- Commands run: git -C "D:\projects\hackathon" status 2>&1; echo "---FILES---"; ls -la "D:\projects\hackathon" 2>&1, python -c "import json; p=r'D:\projects\hackathon\.claude\settings.json'; d=json.load(open(p)); valid={'PreToolUse','PostToolUse','PostToolUseFailure','PostToolBatch','Notification','UserPromptSubmit','UserPromptExpansion','SessionStart','SessionEnd','Stop','StopFailure','SubagentStart','SubagentStop','PreCompact','PostCompact','PermissionRequest','PermissionDenied','Setup','TeammateIdle','TaskCreated','TaskCompleted','Elicitation','ElicitationResult','ConfigChange','WorktreeCreate','WorktreeRemove','InstructionsLoaded','CwdChanged','FileChanged','MessageDisplay'}; keys=set(d.get('hooks',{}).keys()); bad=keys-valid; print('JSON: OK'); print('Hook keys:', sorted(keys)); print('Invalid:', sorted(bad) if bad else 'none')"
- Tool call tally: AskQuestion (1), CallMcpTool (1), CreatePlan (1), Glob (7), Grep (1), Read (14), Shell (2), StrReplace (3), TodoWrite (3), WebSearch (16), Write (20)

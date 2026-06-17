---
title: "Where teams and agents work together"
source: "https://app.notion.com/p/vardymov/Guide-to-Building-Agents-37e6d4f3a294801fb1e2d507d84e6ca2"
author:
published:
created: 2026-06-17
description: "A collaborative AI workspace, built on your company context. Build and orchestrate agents right alongside your team's projects, meetings, and connected apps."
tags:
  - "clippings"
---
## Guide to Building Agents

## The Engineer’s Guide to AI Agents

### How Chatbots Become Systems That Can Actually Do Work

I’m sure you’ve heard the word “agent” thrown around a lot recently. Every AI startup says it is building agents. Every coding tool has an agent mode. Every productivity app suddenly claims it can take work off your plate. The term sounds complicated, but the core idea is actually pretty simple: an agent is a model wrapped in a system that lets it take actions.

A normal chatbot is mostly question-and-answer based. You type something in, the model predicts a response, and then the interaction waits for your next message. It can explain a concept, write a paragraph, summarize an article, or generate code, but by itself it is not really acting in the outside world. It can tell you what terminal command to run, but it cannot run that command unless another system gives it access to a terminal. It can suggest how to update your calendar, but it cannot touch your calendar unless it has a calendar tool. It can write an email, but it cannot send the email unless it has access to an email API.

An agent is what happens when you place a model inside an execution loop. Instead of just returning one answer, the agent can reason about a goal, decide what action to take, call a tool, observe the result, update its plan, and keep going until the task is complete. That is the simplest way to understand agents: they are chatbots that can use tools, remember context, and continue acting toward an objective.

The most important part is that the model is not the entire agent. The model is the reasoning component, but the actual system is much bigger. The agent also needs a harness, tools, memory, context management, sandboxing, permissions, subagents, state tracking, logging, and evaluation. If the model is the engine, the harness is the rest of the car: the steering, brakes, dashboard, sensors, seatbelt, and road rules.

This is why two products can use the same underlying model and feel completely different. One coding agent might hallucinate file paths, make random edits, and break your repo. Another might inspect your codebase, make a targeted patch, run tests, fix the failure, and summarize the final diff. The difference is not only the model. The difference is the harness.

## 1\. Chatbots Answer. Agents Act.

A chatbot is reactive. You ask a question, it gives you an answer. It can be extremely useful, but the interaction usually stays inside the conversation. A chatbot can explain how to fix a bug, but it does not automatically inspect your files, edit your code, run your test suite, or open a pull request.

An agent is connected to an environment. It receives a goal and can take steps toward that goal. Those steps might include reading files, searching a codebase, calling an API, opening a browser, running a shell command, creating a draft, checking a calendar, querying a database, or asking another specialized agent to handle a subtask.

The easiest way to frame it is this:

Chatbot: User asks question → Model returns answer Agent: User gives goal → Model chooses action → Tool executes action → Model observes result → Repeat

A chatbot predicts the next response. An agent repeatedly decides the next action.

For example, if you ask a chatbot, “How do I add password reset to my app?” it might explain the flow. It might tell you to create a reset token, store it in a database, email the user, validate the token, and update the password. That answer may be helpful, but the actual work is still on you.

If you ask a coding agent the same thing, a good one can inspect your repo, find your auth routes, read your user model, look at your existing tests, create a patch, run the test suite, observe failures, fix them, and return a summary of what changed.

That gives us the clean definition:

> An agent is a model inside an execution loop, connected to tools, memory, context, and control logic.

This definition matters because it keeps you from falling for vague marketing. If something is called an agent, ask what loop it runs in, what tools it has, what memory it uses, what context it sees, what permissions it has, and how it knows when to stop.

## 2\. The Agent Loop

At the center of almost every agent is a loop. The loop is simple enough to understand in one diagram:

┌────────────────────┐ │ User Goal │ │ "Fix the login bug" │ └─────────┬──────────┘ │ ▼ ┌────────────────────┐ │ Build Context │ │ prompt + memory + │ │ tools + task state │ └─────────┬──────────┘ │ ▼ ┌────────────────────┐ │ Model Call │ │ reasons about next │ │ best action │ └─────────┬──────────┘ │ ▼ ┌────────────────────┐ │ Tool Call? │ │ read file, run test,│ │ call API, search... │ └──────┬────────┬─────┘ │ yes │ no ▼ ▼ ┌────────────┐ ┌────────────────────┐ │ Execute │ │ Final Answer │ │ Tool │ │ summarize result │ └─────┬──────┘ └────────────────────┘ │ ▼ ┌────────────────────┐ │ Observe Result │ │ output, error, diff,│ │ search results │ └─────────┬──────────┘ │ └────────── back to model

The loop usually has three repeating phases: reasoning, action, and observation. In the reasoning phase, the model decides what to do next. In the action phase, the harness executes the tool the model selected. In the observation phase, the result of that tool call is passed back into the model so it can update its understanding.

A minimal version of this loop looks like this:

while (!done) { const response = await model.call({ messages, tools, }); if (response.toolCall) { const result = await runTool(response.toolCall); messages.push({ role: "tool", content: result, }); } else { done = true; return response.content; } }

That snippet is obviously simplified, but it captures the heart of the system. The model is not directly running code or touching APIs. It is asking for a tool to be called. The harness validates and executes that tool, then gives the result back to the model.

A coding agent’s loop might look like this in practice:

User goal: "Fix the login bug and add a regression test." Agent loop: 1. Search the codebase for login-related files. 2. Read the relevant route, service, and test files. 3. Identify the likely bug. 4. Apply a small patch. 5. Run the login test suite. 6. Observe the failure output. 7. Fix the issue. 8. Run the tests again. 9. Ask a reviewer subagent to inspect the diff. 10. Summarize the changed files and remaining risks.

This loop is simple, but simple does not mean easy. Most of the engineering difficulty comes from making the loop reliable. The model may choose the wrong tool, pass bad arguments, misunderstand a tool result, repeat a failed action, or get distracted by irrelevant context. The harness has to manage all of that.

A production agent usually needs step limits, timeouts, retries, error handling, logging, permissions, approval gates, and fallback behavior. Without those, the agent can spin forever, make unsafe changes, or continue confidently down the wrong path.

The model supplies the reasoning, but the harness supplies the discipline.

## 3\. The Harness Is the Real Product

The harness is the system around the model. It calls the model, builds the prompt, loads memory, exposes tools, validates actions, manages context, runs subagents, catches failures, and decides when the task is done.

This is the part of agent engineering that most people underestimate. They think building an agent means choosing a model and writing a clever prompt. That might be enough for a demo, but it is not enough for a reliable product.

A serious harness answers questions like these:

What system instructions should the model receive? What tools is the model allowed to call? What user memory should be loaded? What recent messages should be included? What files, docs, or database rows are relevant? What should happen when a tool fails? How many steps can the agent take before stopping? Which actions require human approval? How should tool outputs be summarized? How should agent runs be logged and evaluated?

A high-level harness architecture looks like this:

┌──────────────────────────────────────────────────────────┐ │ Agent Harness │ │ │ │ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │ │ │ Memory │ │ Context │ │ Tool │ │ │ │ Store │ │ Manager │ │ Registry │ │ │ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ │ │ │ │ │ │ │ └──────────┬────────┴──────────┬────────┘ │ │ ▼ ▼ │ │ ┌────────────────────────────────┐ │ │ │ Model Call │ │ │ │ system prompt + messages + │ │ │ │ memories + tools + state │ │ │ └──────────────┬─────────────────┘ │ │ │ │ │ ▼ │ │ ┌────────────────────────────────┐ │ │ │ Action Validator │ │ │ │ permissions, auth, safety, │ │ │ │ sandbox rules │ │ │ └──────────────┬─────────────────┘ │ │ │ │ │ ▼ │ │ ┌────────────────────────────────┐ │ │ │ Tool Execution │ │ │ │ files, APIs, terminal, browser │ │ │ └────────────────────────────────┘ │ │ │ └──────────────────────────────────────────────────────────┘

The harness also creates separation between the model’s request and the system’s actual behavior. The model can ask to run a terminal command, but the harness decides whether that command is allowed. The model can ask to send an email, but the harness can create a draft instead. The model can ask to edit code, but the harness can apply the edit inside a sandbox and show a diff before anything is merged.

That distinction is critical. You do not want the model to have raw, unrestricted access to everything. You want the model to operate through controlled interfaces.

This is why the harness is often more important than people realize. The model may be the most exciting part, but the harness is what makes the agent usable.

## 4\. Tools Are Usually API Wrappers

Tools are how agents touch the world. A tool is usually just an API wrapper with a description and a schema that the model can understand.

That is the part a lot of people miss. When someone says, “The agent can check your calendar,” what they usually mean is that the harness exposes a calendar tool. Under the hood, that tool calls the Google Calendar API, Microsoft Graph API, or some internal calendar service. When someone says, “The agent can send an email,” the tool is probably wrapping the Gmail API, Outlook API, SendGrid, Resend, or some other email provider.

A tool is not magic. It is a normal function.

Model wants action: "Create a calendar event tomorrow at 3 PM." Tool wrapper: createCalendarEvent({ title, startTime, endTime, attendees }) External API: Google Calendar API / Outlook API / internal calendar service Observation returned to model: "Event created successfully."

A simple tool wrapper might look like this:

const getWeatherTool = { name: "get\_weather", description: "Get the current weather for a city.", parameters: { type: "object", properties: { city: { type: "string", description: "The city to get weather for", }, }, required: \["city"\], }, execute: async ({ city }) => { const response = await fetch( \`https://api.weather.com/current?city=${encodeURIComponent(city)}\`, { headers: { Authorization: \`Bearer${process.env.WEATHER\_API\_KEY}\`, }, } ); return await response.json(); }, };

The model does not need to know every detail of the weather API. It only needs to know that a tool called

get\_weather

exists, what it does, and what arguments it requires. The harness handles the actual API call.

This pattern applies almost everywhere:

Agent tool Real underlying system ------------------------------------------------ read\_file Filesystem API run\_tests Shell / terminal process search\_code ripgrep, source graph, vector index send\_email Gmail API, Outlook API, SendGrid create\_event Google Calendar API, Microsoft Graph query\_database SQL database driver search\_docs Vector database or search index open\_browser Browser automation environment create\_ticket Linear, Jira, GitHub Issues API

This is why tool design matters so much. Tools define the agent’s action space. If the tool is too broad, the agent becomes risky. If the tool is too narrow, the agent becomes useless. If the tool description is bad, the model will call it at the wrong time. If the output is too noisy, the model will misunderstand what happened.

A good tool is narrow, predictable, and easy for the model to use correctly.

## 5\. Tool Auth: Who Is the Agent Acting As?

Once tools call real APIs, authentication becomes one of the most important technical details. A tool does not just “send an email” in the abstract. It sends an email as some user, service account, organization, or app. That means the harness has to know whose credentials are being used and what permissions those credentials have.

There are generally a few auth patterns for agent tools.

The first is service-level auth. This is when the backend uses its own API key or service account to call an external service. For example, a weather tool might use the company’s Weather API key. The user does not need to connect their own account because the data is not personal.

User → Agent → Weather Tool → Company API Key → Weather API

The second is user-delegated auth. This is when the user connects their own account through OAuth, and the agent acts with the user’s permission. Calendar, Gmail, Notion, Slack, GitHub, and Google Drive tools often work this way. The tool uses an access token tied to the user, and the agent can only do what the user authorized.

User connects Google account │ ▼ OAuth token stored securely │ ▼ Agent calls calendar tool │ ▼ Tool calls Google Calendar API as that user

The third is internal permissioned auth. In a company setting, the agent may call internal APIs. The harness has to enforce the company’s permission model. If a human user is not allowed to access a certain customer record, the agent should not be allowed to access it on their behalf.

This point is extremely important: an agent should not become a permission bypass. If the user cannot do something manually, the agent generally should not be able to do it for them.

A tool call with auth should be treated as a privileged action. The harness should know:

Who requested the action? Which user or service account is the tool using? What scopes does the token have? Is this action read-only or write-capable? Does this action require approval? Should this action be logged? Can the result contain sensitive data?

For example, an email tool might have different permission levels:

Low risk: - Search emails - Read a thread - Create a draft Higher risk: - Send an email - Forward attachments - Delete emails - Apply labels to thousands of messages

A good harness may allow the agent to create a draft automatically, but require human confirmation before sending it. That is not just a UX choice. It is a permission and safety boundary.

Tool auth is one of the places where agent engineering becomes real infrastructure. You need secure token storage, scoped permissions, audit logs, rate limits, revocation, and clear user consent. The model may decide what action it wants to take, but the harness needs to decide whether the agent is allowed to take that action as that user.

## 6\. Sandboxes: Where Agents Are Allowed to Act

If tools are what let an agent take action, the sandbox is what determines where those actions are allowed to happen. This matters because once an agent can write files, run commands, install packages, call APIs, or interact with external services, it stops being a passive chatbot and becomes an active software system.

A sandbox is an isolated environment where the agent can safely perform work without immediately affecting the real world. For a coding agent, that might mean a temporary copy of a repository where the agent can read files, edit code, run tests, and inspect errors. For a browser agent, it might mean a controlled browser session with limited permissions. For a data agent, it might mean a read-only database replica or restricted query environment.

The common idea is that the agent gets enough power to make progress, but not unlimited power over production systems.

A coding agent sandbox might look like this:

┌──────────────────────────────────────────────────────────┐ │ Agent Sandbox │ │ │ │ Temporary repo clone │ │ ┌────────────────────────────────────────────────────┐ │ │ │ /workspace/app │ │ │ │ ├── src/ │ │ │ │ ├── tests/ │ │ │ │ ├── package.json │ │ │ │ └── README.md │ │ │ └────────────────────────────────────────────────────┘ │ │ │ │ Available actions: │ │ - read files │ │ - apply patches │ │ - run tests │ │ - run type checks │ │ │ │ Restricted actions: │ │ - read secrets outside workspace │ │ - access production database │ │ - deploy to production │ │ - delete arbitrary system files │ │ │ └──────────────────────────────────────────────────────────┘

The agent’s full workflow might look like this:

User request │ ▼ Harness creates sandbox │ ▼ Repo is cloned into isolated workspace │ ▼ Agent reads files and makes edits │ ▼ Agent runs tests inside sandbox │ ▼ Harness extracts diff │ ▼ User reviews patch │ ▼ Patch is applied to real repo only after approval

This is especially important for coding agents because writing code is not just text generation. A useful coding agent needs to execute commands, run tests, inspect the filesystem, and sometimes install dependencies. If you let it do all of that directly on your real machine with full permissions, you are trusting a probabilistic system with a lot of power.

A sandbox reduces the blast radius. If the agent makes a bad edit, runs the wrong command, or creates a broken intermediate state, the damage is contained. The harness can discard the sandbox and start again.

There are different levels of sandboxing:

Level 1: Temporary folder - Agent edits a copy of the project. - Simple, but weaker isolation. Level 2: Container - Agent runs inside Docker or a similar container. - Better filesystem and dependency isolation. Level 3: MicroVM or remote execution environment - Agent gets a fresh machine-like environment per run. - Stronger security and reproducibility. Level 4: Permissioned production workflow - Agent never directly mutates production. - It proposes changes, opens drafts, or creates PRs.

Sandboxes are not only for safety. They are also for reliability. Because each run can start from a known state, the agent’s work becomes easier to reproduce. If the agent succeeds, the harness can extract a clean diff. If it fails, the harness can preserve logs or discard the environment.

For non-coding agents, sandboxing often shows up as reversible or approval-gated actions. An email agent creates a draft instead of sending. A calendar agent proposes an event instead of inviting everyone immediately. A database agent queries a read-only replica instead of writing to production. A finance agent simulates a trade instead of placing one.

The cleanest mental model is this:

Tools give the agent hands. Memory gives it continuity. Context gives it awareness. The sandbox gives it a safe room to work in.

Without a sandbox, an agent with tools is powerful but risky. With a sandbox, the agent can do real work while the system still maintains control.

## 7\. Memory: How Agents Remember Things

Memory lets an agent preserve useful information beyond a single model call. Without memory, every agent run starts from scratch unless the harness manually includes previous messages. With memory, the agent can remember user preferences, project structure, previous decisions, known bugs, recurring workflows, and long-term goals.

There are several kinds of memory in agent systems.

The first is conversation memory. This is the recent back-and-forth in a specific chat thread. It helps the agent understand what the user means by “that file,” “the previous bug,” or “the thing we discussed earlier.” Conversation memory is often stored as turns in a database keyed by chat ID.

A simple conversation memory table might look like this:

CREATE TABLE chat\_messages ( id UUID PRIMARY KEY, chat\_id TEXT NOT NULL, role TEXT NOT NULL, content TEXT NOT NULL, created\_at TIMESTAMP NOT NULL DEFAULT NOW() );

When the agent is summoned, the harness retrieves the recent turns:

const recentMessages = await db.chatMessages.findMany({ where: { chatId }, orderBy: { createdAt: "desc" }, take: 20, });

This is what people usually mean when they say an agent has thread-based memory. The thread ID or chat ID becomes the key. The harness uses it to reconstruct the recent conversation before calling the model.

The second kind is task memory. This tracks what has happened during the current job. For a coding agent, task memory might include which files were inspected, which files were changed, which commands were run, which tests failed, and what assumptions the agent has made so far. Task memory prevents the agent from repeatedly inspecting the same file or forgetting its own progress.

The third kind is long-term user memory. This stores durable preferences or facts that should carry across conversations. For example, the agent might remember that a user prefers concise explanations, uses TypeScript and Next.js, wants minimal diffs, or prefers a certain coding style.

The fourth kind is semantic memory. This is usually powered by embeddings. Instead of retrieving only the most recent messages, the harness can search over stored memories, documents, previous conversations, or project notes based on meaning.

The memory system looks roughly like this:

┌────────────────────┐ │ User request │ └─────────┬──────────┘ │ ▼ ┌────────────────────┐ │ Retrieve recent │ │ thread messages │ └─────────┬──────────┘ │ ▼ ┌────────────────────┐ │ Retrieve relevant │ │ semantic memories │ └─────────┬──────────┘ │ ▼ ┌────────────────────┐ │ Build model context │ │ with selected memory│ └────────────────────┘

Memory is powerful, but it can hurt the agent if handled poorly. Agents should not remember everything forever. Too much memory pollutes the context window. Outdated memory can actively mislead the model. If the agent remembers that a repo uses Jest, but the repo later migrates to Vitest, that memory becomes harmful.

Good memory systems need source tracking, freshness, user control, and pruning. Memory is not magic. It is storage plus retrieval plus judgment.

## 8\. Context Management: The Agent’s Working Memory

Context management is one of the most important parts of agent engineering. The model does not automatically know everything. It only sees what the harness places into its context window. That includes the system prompt, user request, recent messages, retrieved memories, tool outputs, file contents, summaries, and task state.

If the harness gives the model the wrong context, the model will make bad decisions. If the harness gives the model too much context, the model may miss the detail that matters. A strong agent system is constantly deciding what to retrieve, what to summarize, what to discard, and what to keep visible for the next step.

This is especially obvious in coding agents. A real codebase can have thousands of files. The agent should not dump the whole repo into the prompt. That would be expensive, slow, and confusing. Instead, the agent should progressively gather context.

A good coding agent might gather context like this:

User goal: "Fix the login bug." Bad context strategy: Dump the entire repo into the prompt. Good context strategy: 1. Search for login/auth files. 2. Read the route and service files. 3. Read the related tests. 4. Summarize the relevant behavior. 5. Make a small patch. 6. Run the focused test. 7. Feed the test output back into context.

The context manager is basically the model’s working memory:

┌──────────────────────────────────────────────────────────┐ │ Context Window │ │ │ │ System prompt │ │ Developer instructions │ │ User request │ │ Recent conversation turns │ │ Relevant memories │ │ Current task state │ │ Selected file snippets │ │ Tool results │ │ Summaries of long outputs │ │ │ └──────────────────────────────────────────────────────────┘

The hard part is choosing what goes in. For a coding agent, the harness may include the current task, a summary of inspected files, the specific code snippets being edited, the latest test failure, and a list of changed files. It may exclude old logs, irrelevant files, repeated tool results, and stale memory.

Context management also includes compression. Tool outputs can be huge. Test logs, stack traces, search results, and file contents can quickly fill the context window. A good harness trims or summarizes these outputs while preserving the important details. For a failing test, the model usually needs the command, the failing test name, the error message, the expected value, the received value, and maybe a few stack frames. It does not need thousands of unrelated log lines.

A useful task state summary might look like this:

Task state: - Goal: Fix login redirect bug after expired session. - Inspected files: - src/auth/session.ts - src/routes/login.ts - tests/login.test.ts - Current hypothesis: - Expired sessions are redirecting to /dashboard instead of /login. - Changed files: - src/auth/session.ts - Latest test failure: - expected redirect "/login", received "/dashboard" - Next step: - Inspect redirect logic after session validation.

This is much easier for the model to use than a messy transcript of every previous step.

Context management is also one of the main reasons subagents are useful. Instead of forcing one agent to hold the entire problem in one giant context window, the parent agent can launch specialized threads with smaller, focused context. A reviewer subagent does not need the full chat history. It only needs the goal, the diff, and the test output. A search subagent does not need the implementation details. It only needs the search objective and repo structure.

Good context management makes agents feel smart. Bad context management makes even strong models look dumb.

## 9\. Subagents and Threads

Subagents are one of the more misunderstood parts of agent architecture. A subagent is usually not a magical separate AI being. Most of the time, it is a separate model invocation, separate thread, or separate harness instance with a narrower role.

The parent agent owns the overall task. It understands the user’s goal, maintains the main task state, and decides what needs to happen next. When part of the task would benefit from specialized focus, the parent can launch a subagent. That subagent receives a smaller objective, a specialized system prompt, a narrower slice of context, and sometimes a different set of tools.

Here is the high-level diagram:

┌──────────────────────────────────────────────────────────┐ │ Parent Agent │ │ │ │ Goal: "Add password reset and tests" │ │ │ │ Responsibilities: │ │ - Own overall plan │ │ - Decide what subagents to launch │ │ - Merge subagent outputs │ │ - Make final decisions │ │ │ └───────┬───────────────────┬───────────────────┬──────────┘ │ │ │ ▼ ▼ ▼ ┌──────────────┐ ┌──────────────┐ ┌────────────────┐ │ Search │ │ Reviewer │ │ Documentation │ │ Subagent │ │ Subagent │ │ Subagent │ │ │ │ │ │ │ │ Finds files │ │ Reviews diff │ │ Writes summary │ └──────────────┘ └──────────────┘ └────────────────┘

Each subagent can run in its own thread. This matters because threads are one way to isolate context. The reviewer thread does not need the entire conversation. It might only need the user goal, the diff, and the test output. The search thread might only need the repo index and a search objective. The documentation thread might only need the final implementation and API behavior.

A subagent call might look like this:

const review = await runSubagent({ threadName: "code-review", systemPrompt: "You are a strict senior code reviewer.", context: { userGoal, diff, testOutput, }, task: "Find bugs, missing tests, security issues, and risky assumptions.", });

The point of the subagent is not that it has a different brain. It may use the same model as the parent agent. The difference is the role, context, tools, and objective.

A useful way to think about it is this:

Parent thread: Broad context, owns the full task, coordinates everything. Search subagent thread: Narrow context, finds relevant information. Reviewer subagent thread: Narrow context, critiques the work. Execution subagent thread: Narrow context, performs a specific patch or action. Summary subagent thread: Narrow context, explains the final result.

Subagents can also have different permissions. A reviewer subagent may only need read access. A search subagent may only need code search. An implementation subagent may need patching tools but not deployment tools. This lets the harness apply the principle of least privilege.

The parent agent then receives the subagent’s output and decides what to do with it. This is important. Subagents should usually advise or complete narrow tasks, but the parent should remain responsible for coordination. If the reviewer finds a bug, the parent decides whether to patch it. If the search subagent finds relevant files, the parent decides which ones to read. If the documentation subagent writes a summary, the parent decides whether it matches the final work.

Subagents are useful, but they can also create unnecessary complexity. More agents does not automatically mean better results. A poorly designed multi-agent system can become a group chat where agents talk forever without producing useful work. Subagents work best when there is a clear separation of concerns, a narrow objective, and a structured output.

The best way to think about subagents is that they are focused threads of cognition. The parent agent has the big picture. Each subagent gets a smaller window, a sharper role, and a more specific job.

## 10\. Planning, State, and Error Recovery

Real tasks are messy. Files are missing. Tests fail. APIs return errors. Requirements are ambiguous. The model makes wrong assumptions. A serious agent needs to recover from these problems instead of collapsing after the first failure.

One common pattern is plan-first execution. Before editing files or calling high-impact tools, the agent creates a short plan. For a coding task, the plan might be: inspect relevant files, identify the bug, make a minimal patch, add a regression test, run the test suite, and summarize the result. This plan gives the agent a roadmap and gives the harness a way to track progress.

The plan should not be treated as sacred. It is a working hypothesis. As the agent observes new information, the plan may change. If the codebase structure is different than expected, the agent should update its approach. If a test failure reveals a deeper issue, the agent should revise the plan rather than blindly continue.

A good planning flow looks like this:

Goal │ ▼ Initial plan │ ▼ Inspect environment │ ▼ Revise plan based on reality │ ▼ Act │ ▼ Observe result │ ▼ Continue, revise, or stop

State tracking is what lets the harness keep the agent grounded. During a task, the harness can track which files have been inspected, which tools have been called, which assumptions have been made, what errors occurred, and what remains to be done. This is especially important because the raw conversation transcript can become long and messy.

Error recovery is another key part of orchestration. If a command fails, the agent should read the error and reason about it. If the same command fails repeatedly, the harness should prevent the model from trying the same fix over and over. A good system can detect repeated failure patterns and nudge the agent to re-examine its assumptions, inspect more context, or ask for human input.

This is one of the places where agents start to resemble human workflows. A junior engineer does not always get the first implementation right. They write code, run tests, see errors, debug, and try again. Agents work similarly, but they need a harness to make that process controlled and observable.

The key idea is that failure becomes input. A test failure is not just a failure. It is information. A stack trace is not just noise. It is context. A rejected tool call is not the end of the task. It is a boundary the agent needs to respect.

## 11\. Safety, Permissions, and Approval Gates

Agents are powerful because they can act. That is also what makes them risky. Once an agent can run commands, edit files, call APIs, send messages, or touch databases, you need a permission model.

A good agent system should distinguish between low-risk, medium-risk, and high-risk actions.

Low risk: - Search documentation - Read files inside a sandbox - Query public data - Create a draft Medium risk: - Modify files in a sandbox - Run tests - Install dependencies in an isolated environment - Update a non-production issue tracker High risk: - Send an email - Delete files - Modify production data - Deploy code - Make purchases - Access secrets

The harness should enforce these boundaries. The model should not be trusted to self-regulate perfectly. If an action is destructive, irreversible, external-facing, or financially meaningful, the harness should require approval or route the action into a safer form.

For example:

Instead of sending an email: Agent creates a draft. Instead of pushing to main: Agent opens a pull request. Instead of writing to production DB: Agent queries a read-only replica. Instead of placing a trade: Agent runs a simulation. Instead of deploying: Agent prepares a deployment plan.

This is not a weakness of agents. It is how real systems are built. Human engineers use code review, staging environments, permission levels, feature flags, and deployment approvals. Agents should operate under similar controls.

A strong permission system also includes secrets management. The agent should not casually see API keys, private credentials, SSH keys, production environment variables, or sensitive user data. Even if the agent is not malicious, exposing secrets increases risk. The harness should limit what the model can read and redact sensitive information when possible.

Approval gates are also important for trust. Users are more likely to trust agents when they can see what the agent plans to do before it does something consequential. “I found the issue and prepared this patch” feels safe. “I edited your production app and deployed it” feels dangerous.

The best agents give users control over important transitions.

## 12\. Evaluation and Observability

If you cannot observe an agent, you cannot improve it. Agent behavior can be hard to debug because it unfolds over multiple steps. The final output may look wrong, but the real mistake might have happened much earlier when the agent retrieved the wrong context, misunderstood a tool result, skipped a test, or repeated a bad assumption.

A serious agent harness should log the important parts of each run:

This makes it possible to reconstruct what happened when something goes wrong.

Evaluation is also harder for agents than for simple model calls. A normal model evaluation might check whether an answer is correct. An agent evaluation has to check whether the agent completed the task, used tools appropriately, avoided unsafe actions, recovered from errors, stayed within budget, and produced an acceptable final result.

For coding agents, evaluation can include:

Did the tests pass? Did the typecheck pass? Was the diff minimal? Did the code match the user request? Did the agent inspect relevant files before editing? Did it avoid touching unrelated files? Did a human reviewer accept the change?

For customer support agents, evaluation might include resolution rate, escalation quality, policy compliance, and user satisfaction. For research agents, evaluation might include citation quality, factual accuracy, source diversity, and synthesis quality.

Observability also helps you improve the harness. If agents repeatedly call the wrong tool, the tool description may be unclear. If they repeatedly miss important files, retrieval may be weak. If they get stuck after test failures, error formatting may be poor. If they use too many steps, the planning strategy may need work.

Agent quality is not a vibe. It can be measured, debugged, and improved like any other software system.

## 13\. What Developers Should Actually Learn

If you want to build agents, the first thing to learn is tool calling. Tool calling is the basic mechanism that lets a model interact with software. You should understand how tools are described, how arguments are validated, how tool results are returned, and how permissions are enforced.

The second thing to learn is orchestration. The agent loop is simple in theory, but production orchestration involves state, retries, timeouts, approval gates, fallbacks, and logging. The difference between a toy agent and a useful agent is usually the orchestration.

The third thing to learn is context engineering. The model is only as good as the context it sees. You need to understand retrieval, search, summarization, truncation, embeddings, document chunking, file indexing, and task state. Context management is one of the highest-leverage skills in agent development.

The fourth thing to learn is memory. Memory is not just saving chat logs. It is deciding what should persist, what should be retrieved, what should expire, and how to prevent stale information from hurting the agent.

The fifth thing to learn is sandboxing. Agents need safe places to work. If an agent can run commands, edit files, or call external services, you need isolation, permissions, resource limits, and approval gates.

The sixth thing to learn is auth and permissions. Tools are often API wrappers, which means agents act through credentials. You need to understand OAuth, scoped tokens, user-delegated auth, service accounts, audit logs, and revocation.

The seventh thing to learn is subagent architecture. Subagents are useful when a task benefits from focused threads with specialized prompts and narrow context. They are not always necessary, but they can be powerful when used carefully.

The eighth thing to learn is evaluation. You need to know whether the agent actually completed the task, whether it did so safely, and whether the result was useful. Without evaluation, you are just guessing.

Finally, you need to learn when not to use agents. Not every AI feature needs an agent loop. If the task is a simple classification, extraction, rewrite, or answer, a single model call may be better. Agents are useful when a task requires multiple steps, tool use, uncertainty reduction, external actions, or iterative feedback. Using an agent where a normal function would work adds cost, latency, and unpredictability.

The best agent builders are not just prompt engineers. They are systems engineers. They know how to wrap models in reliable infrastructure. They understand tools, memory, context, sandboxes, permissions, evals, and product design.

At the end of the day, an agent is just a model in a loop with tools, memory, context, and control logic. That sounds simple because the core abstraction is simple. The hard part is making it reliable enough to trust. That is where the real engineering begins.
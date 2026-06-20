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
# Anthropic
## MOC
- [[W__ L__ - ...]]
- [[HW__ - ...]]
## Definition
- 
## Resources
- 
### Custom Instructions
1. Use the `#` command to enter "memory mode" - this lets you edit your `CLAUDE.md` files intelligently. Just type something like: `# Use comments sparingly. Only comment complex code.`. 
	- Claude will merge this instruction into your `CLAUDE.md` file automatically.
2. You can rewind the conversation by pressing `Escape` *twice*.
3. `/compact`: The `/compact` command summarizes your entire conversation history while preserving the key information Claude has learned. This is ideal when:
	- Claude has gained valuable knowledge about your project
	- You want to continue with related tasks
	- The conversation has become long but contains important context
4. `/clear`: The `/clear` command completely removes the conversation history, giving you a fresh start. This is most useful when:
	- You're switching to a completely different, unrelated task
	- The current conversation context might confuse Claude for the new task
	- You want to start over without any previous context
## Everything Claude Code (ECC)
### Part 4: Your Daily Workflow with ECC
**Monday: Start New Feature**
- Plan the feature:
    ```bash
    /everything-claude-code:plan "Add certification timeline visualization"
    ```
    → Planner creates blueprint
- Write tests first:
    ```bash
    /tdd
    ```
    → TDD-guide helps write failing tests
- Implement:
    ```bash
    [write your code]
    ```
- Review:
    ```bash
    /code-review
    ```
    → Code-reviewer checks for issues
**Tuesday: Debug Build Error**
- Your build fails:
    ```bash
    pnpm build  # fails with error
    ```
- Run fixer:
    ```bash
    /build-fix
    ```
    → Build-error-resolver analyzes and fixes
**Wednesday: Security Check**
- Before committing:
    ```bash
    /security-scan
    ```
    
    → AgentShield runs 102 security rules

---

**Thursday: Documentation**

- After feature completion:
    
    ```bash
    /update-docs
    ```
    
    → Doc-updater updates relevant docs

---

**Friday: Code Quality**

- Refactor old code:
    
    ```bash
    /refactor-clean
    ```
    
    → Removes dead code, unused imports
## Courses
### Claude Code in Action
1. When you first start Claude in a new project, run the `/init` command. This tells Claude to analyze your entire codebase and understand:
	- The project's purpose and architecture
	- Important commands and critical files
	- Coding patterns and structure
	Types Of files:
	- **CLAUDE.md** - Generated with /init, committed to source control, shared with other engineers
	- **CLAUDE.local.md** - Not shared with other engineers, contains personal instructions and customizations for Claude
	- **~/.claude/CLAUDE.md** - Used with all projects on your machine, contains instructions that you want Claude to follow on all projects
2. When you need Claude to look at specific files, use the `@` symbol followed by the file path. This automatically includes that file's contents in your request to Claude.
3. You can also mention files directly in your `CLAUDE.md` file using the same `@` syntax.
4. **Planning Mode** is best for:
	- Tasks requiring broad understanding of your codebase
	- Multi-step implementations
	- Changes that affect multiple files or components
5. **Thinking Mode** is best for:
	- Complex logic problems
	- Debugging difficult issues
	- Algorithmic challenges
> [!NOTE] You can combine both modes for tasks that require both breadth and depth. Just keep in mind that both features consume additional tokens, so there's a cost consideration for using them.
6. You can rewind the conversation by pressing Escape twice. This shows you all the messages you've sent, allowing you to jump back to an earlier point and continue from there. This technique helps you:
	- Maintain valuable context (like Claude's understanding of your codebase)
	- Remove distracting or irrelevant conversation history
	- Keep Claude focused on the current task
7. To create a custom command, you need to set up a specific folder structure in your project:
	1. Find the `.claude` folder in your project directory
	2. Create a new directory called `commands` inside it
	3. Create a new markdown file with your desired command name (like `audit.md`)
	The filename becomes your command name - so `audit.md` creates the `/audit` command.
8. 
## Common mistakes
- 
## Mini-test (answer without looking)
- [ ] Flashcards
- [ ] 
## Flashcards (best 3–8)


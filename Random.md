---
type: evergreen
status: sprout
created: 2025-10-23
tags:
  - evergreen
notes:
  - "[[40_Resources/CS/Links|Links]]"
  - "[[10_Areas/Links|Links]]"
  - "[[Useful Links]]"
---
# Links
## In General
1. [All pdfs for books](https://en.wikipedia.org/wiki/Anna%27s_Archive)
2. [Website to Learn Anything?](https://learn-anything.xyz/)
3. [Zapier](https://zapier.com/app/home?conversationId=a82a1ddd-6290-43fc-9f8b-3bc4583193f5)
4. [Battery Report](file:///C:/Users/Anant%20Gupta/battery-report.html): **IMPORTANT**
5. [Prof AI](https://prof.ai/login)
6. [Web Archive](https://web.archive.org/) for everything → [[60_Claude/30_Source_Summaries/Vault Web Ingestion/Web Archive|source note]]
7. [AI Analysis of the websites](https://www.similarweb.com/) → [[60_Claude/30_Source_Summaries/Vault Web Ingestion/AI Analysis of the websites (similarweb.com)|source note]]
8. 
## AI
- [AI Search: *For any AI*](https://free.theresanaiforthat.com/ )
- [AI Journaling Deeper](https://app.myentries.ai/journal)
- [Humanize AI text](https://cleverhumanizer.ai/): [Reddit post](https://www.reddit.com/r/DataRecoveryHelp/comments/1l7aj60/humanize_ai/)
- [Humanize AI text](https://ahrefs.com/writing-tools/ai-humanizer): *better*
- [AI Watermark Detector](https://www.gptwatermark.com/)
- [AI Web application creation](https://flatlogic.com/generator?utm_source=sp_auto_dm&utm_referrer=sp_auto_dm)
- [Deploy AI Agents](https://pipedream.com/string)
- [GitHub Profile ReadMe Maker](https://gprm.itsvg.in/) → [[60_Claude/30_Source_Summaries/Vault Web Ingestion/GitHub Profile ReadMe Maker (gprm.itsvg.in)|source note]]
- [Groq: *API creation*](https://console.groq.com/home) → [[60_Claude/30_Source_Summaries/Vault Web Ingestion/Groq API creation (console.groq.com)|source note]]
- [Research AI: Anara](https://anara.com/anantgupta21?checkDevice=true)
- [Research Assistant AI](https://jenni.ai/)
- [Help Study AI: You Learn](https://app.youlearn.ai/)
- [Agent Minimax](https://agent.minimax.io/): OpenClaw
- [Learn to Hack Anything](https://pentestgpt.com/)
- To Learn: [AI Starter Kit](https://flicker-celestite-7b6.notion.site/AI-STARTER-KIT-2026-2f4d180d8c8081e5bb17e2027f7d0cf6)
- 
### Prompting
- [Github: *System Prompts and models for all AI tools*](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) → [[60_Claude/30_Source_Summaries/Vault Web Ingestion/Github System Prompts and models for all AI tools|source note]]
- [Prompt Library: *Guide*](https://tathastu-rh.notion.site/prompt-library-ruben-hassid)
	- [Specific](https://tathastu-rh.notion.site/chatgpt-gemini-claude-grok-2d99464bdbf98168a9f5f8b1a198b108)
- [Prompt Generator(Decent)](https://docsbot.ai/tools/prompt/chatgpt-prompt-generator)
- [Prompt Maker(More Options)](https://promptweaver.me/)
## For me 
- Portfolio to learn about human body: [Huberman Lab](https://www.hubermanlab.com/)
- Cool af portfolio: [Bruno-simon](https://bruno-simon.com/)
- 
# Data view (Evergreen)
## Inbox
```dataview
TABLE status, created, notes
FROM "00_Inbox"
WHERE type = "evergreen"
SORT status ASC, file.mtime DESC
```
## UMN
```dataview
TABLE status, created, notes
FROM "10_UMN"
WHERE type = "evergreen"
SORT status ASC, file.mtime DESC
```
## Progress and Resources
```dataview
TABLE status, created, notes
FROM "20_Progress" OR "40_Resources"
WHERE type = "evergreen"
SORT status ASC, file.mtime DESC
```
## The rest
```dataview
TABLE status, created, notes
FROM "30_Order" OR "50_Archive" OR "Clippings"
WHERE type = "evergreen"
SORT status ASC, file.mtime DESC
```
# MOC

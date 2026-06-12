---
tags: [portfolio, chatbot, tools, function-calling]
---

# Orby's Closed Tool Set

> [[../INDEX|← Back to Index]] · [[00-orby-overview|Orby Overview]]

## File

`src/lib/chat-tools.ts` — Community 1

## The 6 Tools

| Tool | Return Type | Purpose |
|------|-------------|---------|
| `navigate` | `NavigateResult` | Scroll to a portfolio section |
| `showProject` | `ShowProjectResult` | Display a project evidence card |
| `showExperience` | `ShowExperienceResult` | Display an experience evidence card |
| `lookupFact` | `LookupFactResult` | Look up a specific fact about Anant |
| `getResume` | `GetResumeResult` | Get resume download link |
| `contact` | `ContactResult` | Open contact form / provide contact info |

## Key Exports

| Export | Role |
|--------|------|
| `buildChatTools()` | Builds tool definitions array for the AI SDK |
| `getSanityClient()` | Returns server client for tool data fetching |
| `SECTION_IDS` | Map of section names to DOM IDs |
| `NONE_SENTINEL` | Sentinel value for "no result" |
| `toEnum()` | Converts string to typed enum |
| `Catalog` | Type for the full Sanity catalog |
| `ChatTools` | Type for the built tools array |

## Tool Result Types

```typescript
// All results are discriminated unions
type NavigateResult = { section: string; scrollId: string }
type ShowProjectResult = { project: Project | null }
type ShowExperienceResult = { experience: Experience | null }
type LookupFactResult = { fact: string; source: string }
type GetResumeResult = { url: string }
type ContactResult = { email: string; formAvailable: boolean }
```

## Evidence Cards (UI Side — Community 17)

When Orby calls `showProject` or `showExperience`, the frontend renders an evidence card:

| Component | File | Purpose |
|-----------|------|---------|
| `ProjectEvidenceCard()` | `src/components/lab/cards/ProjectEvidenceCard.tsx` | Shows project info inline |
| `ExperienceEvidenceCard()` | `src/components/lab/cards/ExperienceEvidenceCard.tsx` | Shows experience inline |
| `ToolResultRenderer()` | `src/components/lab/cards/ToolResultRenderer.tsx` | Dispatches to correct card |
| `EvidenceCard()` | `src/components/lab/EvidenceCard.tsx` | Base evidence card wrapper |

## SECTION_IDS Map

Maps tool section names to actual DOM scroll targets, enabling `navigate` tool to reliably scroll the page.

## See Also
- [[01-api-route|API Route (builds and passes tools)]]
- [[../components/02-lab-chat-ui|Lab UI (renders tool results)]]

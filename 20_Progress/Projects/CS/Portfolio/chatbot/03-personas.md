---
tags: [portfolio, chatbot, personas, orby]
---

# Orby Personas

> [[../INDEX|← Back to Index]] · [[00-orby-overview|Orby Overview]]

## Overview

4 personas live in `src/lib/personas/`. Each defines Orby's tone, vocabulary, and response style. The user selects a persona via `PersonaSelector` in the Lab UI.

## Files — Community 1

| File | Persona | Tone |
|------|---------|------|
| `src/lib/personas/recruiter.ts` | Recruiter | Professional, metrics-focused, concise |
| `src/lib/personas/friend.ts` | Friend | Casual, enthusiastic, first-name basis |
| `src/lib/personas/weirdo.ts` | Weirdo | Playful, quirky, unexpected analogies |
| `src/lib/personas/ceo.ts` | CEO | Strategic, high-level, business-minded |

## Persona Index — `src/lib/personas/index.ts`

```typescript
export type Persona = 'recruiter' | 'friend' | 'weirdo' | 'ceo'
export const PERSONAS: Persona[] = ['recruiter', 'friend', 'weirdo', 'ceo']
export const PERSONA_BLOCKS: Record<Persona, string>  // system prompt snippets
export function getPersonaBlock(persona: Persona): string
```

`getPersonaBlock()` is called in `POST()` to append the persona block to the base system prompt.

## Eval Fixtures

Each persona has eval fixtures in `evals/fixtures/`:
- `system-prompt-recruiter.txt`
- `system-prompt-friend.txt`
- `system-prompt-weirdo.txt`
- `system-prompt-ceo.txt`
- `system-prompt.txt` (base, no persona)

And persona-specific warmth evals in `evals/personas/`:
- `recruiter-warmth.yaml`
- `friend-warmth.yaml`
- `weirdo-warmth.yaml`
- `ceo-warmth.yaml`

## UI — PersonaSelector

`src/components/lab/PersonaSelector.tsx` — Community 4

```typescript
type Persona = 'recruiter' | 'friend' | 'weirdo' | 'ceo'
interface PersonaSelectorProps { ... }
const PERSONA_CONFIG: Record<Persona, { label, icon, description }>
```

User picks persona in the Lab panel header; state flows into `PortfolioLab` which passes it to the chat API calls.

## See Also
- [[05-evals|Eval Suite (persona warmth tests)]]
- [[../components/02-lab-chat-ui|Lab UI (PersonaSelector location)]]

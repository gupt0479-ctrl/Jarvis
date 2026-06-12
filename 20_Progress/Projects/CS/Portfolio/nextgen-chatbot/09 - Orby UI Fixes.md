# 09 - Orby UI Fixes

> Implementation plan for the Portfolio Lab sidebar chatbot UI overhaul. Branch: `Chatbot`.

---

## Problems Being Fixed

From the screenshots and user review:

1. **Space hog** — Orby character + pre-chat elements (chips, power prompt) stay visible even after conversation starts, pushing chat messages off-screen
2. **Left-aligned chips** — Quick-prompt chips use `flex-wrap` and sit left-aligned; should be centered, one per row
3. **Power prompt text visible** — The full `<pre>` block with the hand-crafted prompt is displayed; user only needs to copy it, not see it
4. **No per-persona history** — Switching personas destroys the current conversation; switching back gives an empty chat
5. **Orby never waves** — The `wave` pose is wired in OrbyCanvas but never triggered
6. **No copy feedback from Orby** — When user copies the power prompt, Orby says nothing

---

## Files Changed

| File | What |
|------|------|
| `src/components/lab/SuggestedChips.tsx` | Centered column layout |
| `src/components/lab/PowerPromptBlock.tsx` | Remove prompt `<pre>` block; add `onCopied` callback |
| `src/components/lab/PanelOrby.tsx` | Wave → disappear flow; copy confirmation cloud |
| `src/components/lab/PortfolioLab.tsx` | Per-persona history; `chatStarted` state; new conditional layout |

---

## Detailed Changes

### SuggestedChips.tsx

Container class: `flex flex-wrap gap-1.5` → `flex flex-col items-center gap-2`  
Each chip button: add `w-full max-w-[260px] text-center`

Result: chips appear stacked vertically, centered in the sidebar.

---

### PowerPromptBlock.tsx

- Remove the `<pre>{text}</pre>` block — prompt text is no longer visible in the UI
- Add prop: `onCopied?: () => void`
- In `handleCopy`: after `setCopied(true)`, call `onCopied?.()`
- Keep: "// power prompt" kicker, subtitle "Hand-crafted prompt — copy, paste, and Orby locks in.", copy icon

User workflow: sees a compact strip with copy icon → clicks → pastes into chat box.

---

### PanelOrby.tsx

New props added:
```ts
isWaving?: boolean          // triggers wave animation; suppresses thinking/responding clouds
onWaveComplete?: () => void // fires after 1500ms — parent sets chatStarted=true
copyConfirmation?: boolean  // shows "Prompt copied — paste it in the chat box ↓" cloud
```

Logic:
- `pose` = `isWaving ? "wave" : "idle"` (passed to OrbyCanvas)
- `useEffect`: when `isWaving` becomes true, `setTimeout(onWaveComplete, 1500)`
- Thinking + responding speech clouds guarded: only render when `!isWaving`
- Third AnimatePresence key for copy confirmation cloud (shown when `copyConfirmation && !isWaving`)

---

### PortfolioLab.tsx

**New state:**
```ts
chatStarted: boolean                            // false = pre-chat UI, true = in-chat UI
orbyWaving: boolean                             // drives PanelOrby.isWaving
promptCopied: boolean                           // drives PanelOrby.copyConfirmation
perPersonaMessages: Record<Persona, ChatMessage[]>  // isolated history per persona
```

**handlePersonaChange** (replaces direct `setPersona`):
- Aborts in-flight API request
- If `chatStarted`, saves current messages into `perPersonaMessages[oldPersona]`
- Loads `perPersonaMessages[newPersona]`; sets `chatStarted = existing.length > 0`
- Resets `orbyWaving = false`

**handleSubmit change:**
- On first message (`!chatStarted`): `setOrbyWaving(true)` — `chatStarted` flips to `true` via `onWaveComplete` 1.5s later
- `chatStarted` added to `useCallback` dep array

**handleCopied:**
```ts
setPromptCopied(true)
setTimeout(() => setPromptCopied(false), 2000)
```

**onPersonaDetected fix:**
`ChatInputBar` prop changed from `onPersonaDetected={setPersona}` → `onPersonaDetected={handlePersonaChange}` so paste-triggered persona switches also save/restore history.

---

## Layout Before/After

### Pre-chat (no messages for current persona)
```
[Header]
[PersonaSelector]
[SuggestedChips — centered, one per row]
[PanelOrby — idle / waving]
[flex-1 spacer]
[PowerPromptBlock — copy-only strip, recruiter/ceo only]
[ChatInputBar]
```

### In-chat (messages exist for current persona)
```
[Header]
[PersonaSelector]
[ChatThread — flex-1, scrollable]
[ChatInputBar]
```

---

## Edge Cases

| Risk | How It's Handled |
|------|-----------------|
| Fast API response during wave | Clouds guarded by `!isWaving` so no overlap |
| Persona switch mid-wave | `abort()` + `setOrbyWaving(false)` in handlePersonaChange |
| In-progress placeholder saved on persona switch | Only save when `chatStarted=true` |
| Stale `chatStarted` closure in handleSubmit | Added to `useCallback` dep array |

---

## Status

- [ ] SuggestedChips CSS fix
- [ ] PowerPromptBlock collapse + onCopied
- [ ] PanelOrby wave/disappear + copy confirmation
- [ ] PortfolioLab state refactor + layout

---

*Plan written: 2026-06-12 | Branch: Chatbot*

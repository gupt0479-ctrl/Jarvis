---
description: Create or open today's daily note, primed with carries from yesterday
---

Open or create today's daily note in `00_Daily/`.

## Steps

1. Determine today's date: `YYYY-MM-DD`.
2. Check if `00_Daily/YYYY-MM-DD.md` exists.
   - **Exists:** open it and show current state. Ask: *"Add entry, review tasks, or close day?"*
   - **New:** create it using `50_Claude/Templates/daily-note.md`.
3. When creating fresh:
   - Pre-fill date and day-of-week header.
   - Pull incomplete tasks from yesterday (`00_Daily/YYYY-MM-DD-1.md`) under `## Carried Forward`.
   - Add a `## Morning Focus` prompt: *"What would make today a win?"*
   - Link back to yesterday: `← [[YYYY-MM-DD-1]]`
4. Accept free-form input during the day — append to `## Log` with `HH:MM —` prefix.
5. **Close-day mode** (triggered by `/closeday` or "close day"):
   - Fill `## Evening Review`: wins, energy, one thing to carry forward.
   - Run task rollover: copy any `- [ ]` items to tomorrow's note stub.
   - Prompt to run `/compress` to log the session.

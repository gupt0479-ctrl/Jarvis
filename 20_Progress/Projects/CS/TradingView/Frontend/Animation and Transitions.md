---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Charts and Data Visualization]]"
  - "[[Micro-interactions and UI Effects]]"
tags:
  - trading
  - frontend
  - ui
  - animation
track:
  - trading
  - ui
next: "Attach alongside the 8 page notes when briefing the coded build"
---
# Animation and Transitions
==Motion on this desk is information, not decoration — something is allowed to move only if its movement tells you something true (this is alive, this just changed, this is where your attention should land), never because a page felt static without it.==
## The rule that governs everything below
Before animating anything, ask what it's communicating. "This agent is running" (a breathing pulse), "this just became true" (a brief highlight flash), "you are here now" (a tab underline sliding to its new position) are all real jobs. "This app feels premium" is not a real job, and motion added purely for that reason is exactly the kind of thing that makes an interface feel busy rather than alive. The desk's whole voice — calm, evidence-first, honest about uncertainty — has to survive in its motion design as much as in its copy.
## Page and route transitions
Moving between top-level pages (Dashboard to Watchlist, Watchlist to My Stocks) is a plain, fast cross-fade — 150 to 200 milliseconds, no slide, no scale, nothing that implies spatial movement between unrelated pages. Moving between tabs on the same page (Position to Research on My Stocks, Grid to Compare on Strategies) is different: these are two views of the *same* thing, so the transition should imply that — a short horizontal slide (20 to 30px) paired with the cross-fade, and the tab underline itself sliding to its new position over the same duration rather than jumping. The distinction matters: a full page change should feel like arriving somewhere new; a tab change should feel like turning your head.
## The modal
`SymbolModal` — the one modal reused everywhere on the desk — rises rather than fades: a slight upward translate (8 to 12px) combined with opacity and a subtle scale-in from 96% to 100%, around 200ms, eased so it settles rather than snaps. The backdrop dims independently on its own slightly slower fade so the background never goes fully dark before the card has finished arriving. Closing reverses the same motion, faster (120 to 150ms) — dismissal should always feel quicker than arrival, the same way closing a door takes less deliberate effort than opening one.
## The pending decision banner
This is the one element on the desk allowed a persistent, structural presence built from motion: a slow, low-amplitude breathing glow in amber, roughly a 3 to 4 second cycle, never fast enough to read as alarm, never so slow it feels forgotten. It doesn't animate in on page load with any flourish — it's simply there, because a pending decision isn't a notification that just arrived, it's a fact that's already true.
## Agent and graph states
Bots-Hub's running-agent nodes and Brain-Journal's graph edges share one motion language: a soft pulse on anything currently active, a brief directional glow traveling along an edge when data actually flows across it (roughly 400 to 600ms, timed to feel like a single pulse of information moving, not a looping animation). Clicking a node in either graph triggers the five-second detail behavior described in their own page notes — the expand-in is quick (150ms), the hold is five full seconds of stillness (nothing should compete with a card the user is actively reading), and the return is a gentle fade-and-settle back into the graph, never an abrupt cut.
## Numbers that change
A confidence value, a P&L figure, a countdown timer — when a number updates after a refresh, it should never just jump to its new value. A brief, quiet highlight (a soft background flash in the relevant semantic color, fading over about 600ms) marks that something changed, giving the eye a chance to notice before the number settles into its new resting state. Countdown timers specifically should tick smoothly rather than jump minute-to-minute in a way that feels like the page stuttered.
## Hover and press states
Every clickable surface on the desk — buttons, table rows, cards, nav items — gets a fast, subtle response: a barely-there lift or brightening on hover (under 100ms), a slightly firmer press-down feedback on click (instant, no easing delay) so the interface never feels like it's thinking about whether to acknowledge a click. These are the smallest animations on the desk and also the most frequent, so restraint matters most here — anything louder than a whisper here would turn constant background noise into constant background distraction.
## What never animates
Text content itself never animates in character-by-character or line-by-line — that reads as performative, not informative, on a desk whose whole personality is "I'm telling you exactly what I found, plainly." Tables never animate their rows sorting or filtering; they simply re-render in the new order, because watching rows physically slide past each other while searching Watchlist would slow down exactly the moment speed matters most. And nothing on this desk ever celebrates — no confetti on a promoted strategy, no bounce on a winning trade. A good outcome here is proof accumulating quietly, not an occasion.
## MVP scope versus the real thing
For the coded, static-data prototype described in the build prompt, motion should stay to the cheap, high-value layer only: hover/press states, tab and modal transitions, and the pending-banner pulse — all trivial to implement with a library like Motion (formerly Framer Motion) and none of them requiring real data to look right. The agent-pulse, graph-edge-glow, and number-change-highlight behaviors described above are real, intended behavior for the production build, not blocking requirements for the first static pass — note them as "nice if time allows," not "must-have for MVP."

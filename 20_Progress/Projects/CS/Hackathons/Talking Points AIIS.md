---
type: brainstorm
status:
created:
related_progress: []
tags:
  - brainstorm
next:
---
## AIIS Hackathon
### Demo
#### SafeReach 3-minute demo talking points
**0:00-0:20 - Problem + user**
- "SafeReach is a disaster-warning and shelter-matching prototype for residents whose medical equipment depends on electricity."
- "For the demo, we follow Maria Alvarez in Travis County. She uses a ventilator and power wheelchair, cannot self-evacuate, needs accessible transport, and receives large-text alerts."
**0:20-0:45 - Map and risk context**
- "The map shows Maria's location, emergency contacts, shelter options, and HHS emPOWER-style ZIP overlays for electricity-dependent residents."
- ZIP `78745` and the county-level risk number: "Travis County has 4,200+ electricity-dependent residents in the demo data."
- "This is not just nearest-shelter routing. SafeReach has to account for backup power, accessibility, medical oxygen, transport, capacity, and timing."
**0:45-1:20 - Trigger warning / Phase 1**
- "A Winter Storm Warning is active, with about 10 hours before impact. SafeReach automatically runs the matching flow."
- Go to `Get to Safety` / shelter view.
- "The winning match is Dell Seton Medical Shelter: 4.2 miles away, 72-hour generator, wheelchair accessible, medical oxygen, and space available."
- "The closer Austin Community Center is only 1.1 miles away, but it is rejected because it has no backup power. For Maria's ventilator, closer is not safer."
- Click confirm transport if useful: "The app models ADA pickup and notifies the shelter and county workflow."
**1:20-1:55 - Communication flow**
- "Once a match is made, the communication agent prepares six outputs: Maria's large-text alert, messages to Sarah and James, shelter intake, OEM confirmation, and an emergency SMS packet."
- "The profile shows why those messages are personalized: verified OEM profile, equipment needs, communication preferences, contacts, and medical notes."
- "The code also includes deterministic fallback text, so the demo still works if the AI call or network fails."
**1:55-2:25 - Two hours out / Phase 1.5**
- "At two hours out, the matching weights shift. Proximity and transport window matter more, but the hard constraint remains: Maria cannot be sent somewhere without power."
- "Dell Seton still wins because it is reachable in time and meets all equipment requirements."
- Mention the visible ETA: "ADA van ETA is 1 hour 45 minutes, and the transport window is closing."
**2:25-2:55 - Storm active / SOS**
- "Now the disaster is active: power outage confirmed, countdown is zero, and the app routes Maria into emergency mode."
- "The SOS screen summarizes resident identity, GPS, equipment, battery status, confirmed shelter, direct call options, and automatic 15-minute location pings."
- "The emergency SMS packet gives Travis County the operational details: status, address, GPS, medical needs, ADA transport requirement, shelter info, contacts, and reference `TXV-2847`."
**2:55-3:00 - Close**
- "SafeReach's core idea is simple: during a disaster, vulnerable residents should not have to figure out which shelter can actually keep them alive. The system turns profile data, shelter capabilities, timing, and communications into one guided emergency flow.".
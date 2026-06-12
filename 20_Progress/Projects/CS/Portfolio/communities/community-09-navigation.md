---
tags: [portfolio, graph, community, navigation, header]
---

# Community 9 — Navigation + Header

> [[../INDEX|← Back to Index]] · [[../communities/community-overview|All Communities]]

**22 nodes · Cohesion: 0.15**

## What This Community Is

The sticky navigation header and mobile sheet overlay. Everything that lets users navigate between portfolio sections.

## Nodes

### HeaderScrolling (`src/components/HeaderScrolling.tsx`)
- `HeaderScrolling.tsx` (both paths)
- `HeaderScrolling()` — sticky header component
- `HeaderScrollingProps`

### Navigation Data
- `buildNavItems()` — builds nav items from CORE_NAV
- `CORE_NAV` — array of section identifiers
- `SECTION_IDS` — section → DOM scroll id map
- `NavItem` — nav link type
- `NavLink()` — individual nav link renderer
- `isExternalHref()` — detects `http://` / `https://` hrefs

### Mobile Sidebar (Radix Sheet)
- `sheet.tsx` (both paths)
- `Sheet()` — Radix Sheet primitive
- `SheetContent()` — sheet panel content

### Sidebar
- `sidebar.tsx` (both paths) — the sidebar component tree
- `useSidebar()` (via Community 67) — open/close state

## Scroll Behavior

`HeaderScrolling()` applies a class change at scroll threshold — transitions from transparent to blurred backdrop as user scrolls down. Uses a scroll event listener or IntersectionObserver.

## SECTION_IDS

Used by both the navigation header AND by Orby's `navigate` tool. Defined in `chat-tools.ts` (Community 1) and imported here — the bridge between UI navigation and AI-driven navigation.

## See Also
- [[../components/01-page-sections|Page Sections]]
- [[../chatbot/04-tools|Orby navigate tool]]

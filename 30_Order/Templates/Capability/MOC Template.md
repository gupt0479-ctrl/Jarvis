---
type: index
status: sprout
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - moc
notes: []
next:
---
# <% tp.file.title %>

## Purpose

One to three sentences: what this folder or note-cluster is for, and who reads it first. State the reason the cluster exists, not what a MOC is.

*Example:* This is the control surface for the Ahnaf mentorship program — every meeting, plan, and open thread lives under this folder. Read this before opening any individual note inside it.

## Map

The actual content of the MOC: short-linked prose explaining the key notes in this folder and how they relate to each other. Every sentence should earn a link. This is what makes a MOC different from a dataview query — write it, don't list it.

*Example:* [[Mentor Details]] holds who the mentor is and how to reach them. [[Plan]] is the standing goals document — its periodic sections are read before every meeting. [[Mentor Meeting Playbook]] is the format every meeting follows; its Session Log is the append-only record of what was actually said.

## Status

Optional. A short table or a few lines of current live state — active threads, blockers, what's next. Omit this section entirely if the folder is reference-only and has no live state worth tracking.

## Dataview

Live, generated queries only, placed at the very bottom, never above the prose Map. If a query would only repeat what the Map already says, skip it.

```dataview
TABLE status, updated
FROM "<folder path>"
SORT updated DESC
```

## Links

Anything relevant that did not fit naturally into the Map's prose — adjacent folders, external resources, or notes this cluster depends on but does not own. Keep this short; most links belong in the Map.

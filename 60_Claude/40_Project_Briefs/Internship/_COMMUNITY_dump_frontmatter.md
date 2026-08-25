---
type: community
members: 5
---

# dump_frontmatter

**Members:** 5 nodes

## Members
- [[.increase_indent()]] - code - vault_writer/writer.py
- [[Dumps None as a blank scalar (matching the plan's `field` empty style     inste]] - rationale - vault_writer/writer.py
- [[Shared YAML rendering (None as blank scalar, indented list items) so     every d]] - rationale - vault_writer/writer.py
- [[_FrontmatterDumper]] - code - vault_writer/writer.py
- [[dump_frontmatter()]] - code - vault_writer/writer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/dump_frontmatter
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_build_frontmatter]]
- 1 edge to [[_COMMUNITY_render_dossier]]

## Top bridge nodes
- [[dump_frontmatter()]] - degree 5, connects to 2 communities
- [[_FrontmatterDumper]] - degree 4, connects to 1 community
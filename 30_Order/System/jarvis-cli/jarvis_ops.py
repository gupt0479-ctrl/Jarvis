#!/usr/bin/env python3
"""Jarvis Ops CLI.

Read-only operational checks for the Jarvis Obsidian vault. The only command
that writes is `report`, which creates a new Markdown report.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


TODAY = dt.date(2026, 4, 24)
DATE_FIELDS = {"created", "updated", "reviewed", "last_drilled", "next_drill"}
REPORT_DIR = Path("60_Claude/50_Reviews/Ops Reports")
SESSION_LOG = Path("60_Claude/10_Session_Logs/log.md")
CONTEXT_FILES = [
    Path("AI_CONTEXT.md"),
    Path("00_Dashboard.md"),
    Path("40_Resources/Obsidian/Vault Operating System.md"),
]
MOJIBAKE_PATTERNS = [
    "â€”",
    "â€“",
    "â€™",
    "â€œ",
    "â€",
    "â€",
    "Â",
    "Ã",
    "ðŸ",
    "â†",
    "â‰",
    "âœ",
    "âš",
    "ï¸",
]


ENRICHMENT_HEADINGS = [
    "One-Sentence Version",
    "Precise Definition",
    "What It Is",
    "Why It Matters",
    "Mechanism",
    "Real Example",
    "Contrast With",
    "Failure Modes",
    "Diagnostic Questions",
    "Source Anchors",
    "Drill Cards",
    "Understanding Proof",
]
ENRICHMENT_FOLDERS = (
    "10_UMN/",
    "20_Progress/",
    "40_Resources/",
    "60_Claude/20_Distilled_Notes/",
)


@dataclass(frozen=True)
class MarkdownFile:
    path: Path
    rel: str
    text: str
    frontmatter: str | None
    meta: dict[str, object]


@dataclass(frozen=True)
class ProjectInfo:
    rel: str
    status: str
    next_action: str
    missing_core_metadata: bool
    mtime: dt.date


@dataclass(frozen=True)
class EnrichmentCandidate:
    rel: str
    note_type: str
    status: str
    track: str
    score: int
    missing: tuple[str, ...]
    word_count: int


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = resolve_vault_root(args.root)
    if not root:
        print("Could not locate the Jarvis vault root. Pass --root PATH.", file=sys.stderr)
        return 2

    files = load_markdown_files(root, include_tools=args.include_tools)
    ctx = build_audit_context(root, files)

    if args.command == "health":
        print_health(ctx, args.limit)
    elif args.command == "context":
        print_context_pack(root, ctx, args.limit)
    elif args.command == "projects":
        print_projects(ctx, args.limit)
    elif args.command == "links":
        print_links(ctx, args.limit)
    elif args.command == "dates":
        print_dates(ctx, args.limit)
    elif args.command == "encoding":
        print_encoding(ctx, args.limit)
    elif args.command == "enrich-candidates":
        print_enrichment_candidates(ctx, args.limit)
    elif args.command == "report":
        report_path = write_report(root, ctx, args.limit)
        print(f"Wrote report: {report_path}")
    else:
        parser.print_help()
        return 2

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="jarvis",
        description="Operational visibility checks for the Jarvis vault.",
    )
    parser.add_argument("--root", type=Path, default=None, help="Vault root path.")
    parser.add_argument(
        "--include-tools",
        action="store_true",
        help="Include hidden tool folders such as .claude, .cursor, and .kiro.",
    )
    parser.add_argument("--limit", type=int, default=25, help="Rows to show per section.")
    parser.add_argument(
        "command",
        choices=["health", "context", "projects", "links", "dates", "encoding", "enrich-candidates", "report"],
    )
    return parser


def resolve_vault_root(explicit: Path | None) -> Path | None:
    candidates: list[Path] = []
    if explicit:
        candidates.append(explicit)
    candidates.append(Path.cwd())
    candidates.extend(Path(__file__).resolve().parents)

    for candidate in candidates:
        path = candidate.resolve()
        if (path / "AI_CONTEXT.md").exists() and (path / ".obsidian").exists():
            return path
    return None


def load_markdown_files(root: Path, include_tools: bool = False) -> list[MarkdownFile]:
    files: list[MarkdownFile] = []
    for path in root.rglob("*.md"):
        if should_skip_path(root, path, include_tools=include_tools):
            continue
        text = read_text(path)
        frontmatter = extract_frontmatter(text)
        meta = parse_frontmatter(frontmatter) if frontmatter is not None else {}
        files.append(MarkdownFile(path=path, rel=relpath(root, path), text=text, frontmatter=frontmatter, meta=meta))
    files.sort(key=lambda item: item.rel.lower())
    return files


def should_skip_path(root: Path, path: Path, include_tools: bool = False) -> bool:
    rel_parts = path.relative_to(root).parts
    if ".git" in rel_parts:
        return True
    if ".obsidian" in rel_parts:
        return True
    if not include_tools and rel_parts and rel_parts[0].startswith("."):
        return True
    return False


def relpath(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return ""


def extract_frontmatter(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    match = re.match(r"(?s)^---\s*\r?\n(.*?)\r?\n---", text)
    if not match:
        return None
    return match.group(1)


def parse_frontmatter(frontmatter: str | None) -> dict[str, object]:
    if not frontmatter:
        return {}
    data: dict[str, object] = {}
    current_key: str | None = None
    for raw_line in frontmatter.splitlines():
        line = raw_line.rstrip()
        key_match = re.match(r"^([A-Za-z0-9_ -]+):\s*(.*)$", line)
        list_match = re.match(r"^\s*-\s+(.*)$", line)

        if key_match:
            key = key_match.group(1).strip()
            value = key_match.group(2).strip()
            current_key = key
            if value == "":
                data[key] = []
            else:
                data[key] = strip_quotes(value)
            continue

        if list_match and current_key:
            value = strip_quotes(list_match.group(1).strip())
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(value)

    return data


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def has_value(meta: dict[str, object], key: str) -> bool:
    value = meta.get(key)
    if value is None:
        return False
    if isinstance(value, list):
        return len(value) > 0
    return str(value).strip() not in {"", "null", "None", "[]"}


def build_audit_context(root: Path, files: list[MarkdownFile]) -> dict[str, object]:
    missing_type = [item for item in files if not has_value(item.meta, "type")]
    missing_status = [item for item in files if not has_value(item.meta, "status")]
    future_dates = collect_future_dates(files)
    projects = collect_projects(files)
    duplicate_filenames = collect_duplicate_filenames(files)
    encoding_hits = collect_encoding_hits(files)
    enrichment_candidates = collect_enrichment_candidates(files)
    broken_links, ambiguous_links = collect_links(root, files)

    return {
        "root": root,
        "files": files,
        "with_frontmatter": [item for item in files if item.frontmatter is not None],
        "missing_type": missing_type,
        "missing_status": missing_status,
        "future_dates": future_dates,
        "projects": projects,
        "duplicate_filenames": duplicate_filenames,
        "encoding_hits": encoding_hits,
        "enrichment_candidates": enrichment_candidates,
        "broken_links": broken_links,
        "ambiguous_links": ambiguous_links,
    }


def collect_future_dates(files: list[MarkdownFile]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for item in files:
        if item.frontmatter is None:
            continue
        for field in DATE_FIELDS:
            value = item.meta.get(field)
            if not isinstance(value, str):
                continue
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value.strip()):
                continue
            parsed = dt.date.fromisoformat(value.strip())
            if parsed > TODAY:
                rows.append({"path": item.rel, "field": field, "date": value.strip()})
    rows.sort(key=lambda row: (row["date"], row["path"], row["field"]))
    return rows


def collect_projects(files: list[MarkdownFile]) -> list[ProjectInfo]:
    rows: list[ProjectInfo] = []
    for item in files:
        if item.rel.startswith("30_Order/Templates/"):
            continue
        if str(item.meta.get("type", "")).strip() != "project":
            continue
        status = str(item.meta.get("status", "")).strip()
        next_action = frontmatter_value(item.meta, "next") if has_value(item.meta, "next") else ""
        mtime = dt.date.fromtimestamp(item.path.stat().st_mtime)
        rows.append(
            ProjectInfo(
                rel=item.rel,
                status=status,
                next_action=next_action,
                missing_core_metadata=not has_value(item.meta, "type") or not has_value(item.meta, "status"),
                mtime=mtime,
            )
        )
    rows.sort(key=lambda row: (row.status == "archived", row.rel.lower()))
    return rows


def frontmatter_value(meta: dict[str, object], key: str) -> str:
    value = meta.get(key)
    if isinstance(value, list):
        return ", ".join(str(item) for item in value).strip()
    if value is None:
        return ""
    return str(value).strip()


def collect_duplicate_filenames(files: list[MarkdownFile]) -> list[tuple[str, int]]:
    counts = Counter(item.path.name for item in files)
    duplicates = [(name, count) for name, count in counts.items() if count > 1]
    duplicates.sort(key=lambda pair: (-pair[1], pair[0].lower()))
    return duplicates


def collect_encoding_hits(files: list[MarkdownFile]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for item in files:
        count = sum(item.text.count(pattern) for pattern in MOJIBAKE_PATTERNS)
        if count:
            rows.append({"path": item.rel, "count": count})
    rows.sort(key=lambda row: (-int(row["count"]), str(row["path"]).lower()))
    return rows


def collect_enrichment_candidates(files: list[MarkdownFile]) -> list[EnrichmentCandidate]:
    rows: list[EnrichmentCandidate] = []
    for item in files:
        if not item.rel.startswith(ENRICHMENT_FOLDERS):
            continue
        if item.rel.startswith("60_Claude/05_Clippings/") or item.rel.startswith("50_Archive/"):
            continue

        note_type = frontmatter_value(item.meta, "type")
        if note_type not in {"concept", "evergreen", "project", "class", "plan"}:
            continue

        enrichment_status = frontmatter_value(item.meta, "enrichment_status")
        if enrichment_status in {"enriched", "complete", "tree"}:
            continue

        headings = extract_headings(item.text)
        missing = tuple(heading for heading in ENRICHMENT_HEADINGS if heading not in headings)
        if not missing:
            continue

        status = frontmatter_value(item.meta, "status")
        words = len(re.findall(r"\b\w+\b", item.text))
        score = len(missing)
        if note_type == "concept":
            score += 5
        if has_value(item.meta, "track"):
            score += 4
        if status in {"seed", "sprout"}:
            score += 3
        if words < 500:
            score += 3
        elif words < 1000:
            score += 1

        rows.append(
            EnrichmentCandidate(
                rel=item.rel,
                note_type=note_type,
                status=status,
                track=frontmatter_value(item.meta, "track"),
                score=score,
                missing=missing,
                word_count=words,
            )
        )

    rows.sort(key=lambda row: (-row.score, row.rel.lower()))
    return rows


def extract_headings(text: str) -> set[str]:
    headings: set[str] = set()
    for match in re.finditer(r"(?m)^#{2,6}\s+(.+?)\s*$", text):
        title = re.sub(r"\s+#.*$", "", match.group(1).strip())
        headings.add(title)
    return headings


def collect_links(root: Path, files: list[MarkdownFile]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    markdown_by_stem: dict[str, list[str]] = defaultdict(list)
    markdown_by_path: dict[str, str] = {}
    all_targets = build_all_file_targets(root)

    for item in files:
        stem_key = normalize_key(item.path.stem)
        markdown_by_stem[stem_key].append(item.rel)
        path_key = normalize_key(item.rel.removesuffix(".md"))
        markdown_by_path[path_key] = item.rel

    broken: list[dict[str, str]] = []
    ambiguous: list[dict[str, str]] = []

    for item in files:
        for raw_target in find_wikilinks(item.text):
            target = clean_wikilink_target(raw_target)
            if should_ignore_link(item.rel, target):
                continue
            key = normalize_key(target)
            leaf_key = normalize_key(Path(target).name)

            if "/" in target or "\\" in target:
                if key in markdown_by_path or key in all_targets:
                    continue
                broken.append({"source": item.rel, "target": raw_target})
                continue

            matches = markdown_by_stem.get(leaf_key, [])
            if len(matches) == 1:
                continue
            if len(matches) > 1:
                ambiguous.append({"source": item.rel, "target": raw_target, "matches": str(len(matches))})
                continue
            if leaf_key in all_targets:
                continue
            broken.append({"source": item.rel, "target": raw_target})

    broken.sort(key=lambda row: (row["source"].lower(), row["target"].lower()))
    ambiguous.sort(key=lambda row: (row["source"].lower(), row["target"].lower()))
    return broken, ambiguous


def build_all_file_targets(root: Path) -> set[str]:
    targets: set[str] = set()
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.relative_to(root).parts:
            continue
        rel = relpath(root, path)
        no_suffix = rel.rsplit(".", 1)[0] if "." in Path(rel).name else rel
        targets.add(normalize_key(no_suffix))
        targets.add(normalize_key(Path(no_suffix).name))
    return targets


def find_wikilinks(text: str) -> Iterable[str]:
    for match in re.finditer(r"\[\[([^\]]+)\]\]", text):
        yield match.group(1)


def clean_wikilink_target(raw_target: str) -> str:
    target = raw_target.split("|", 1)[0].split("#", 1)[0].strip()
    if target.lower().endswith(".md"):
        target = target[:-3]
    return target


def normalize_key(value: str) -> str:
    return value.replace("\\", "/").strip().lower()


def should_ignore_link(source_rel: str, target: str) -> bool:
    if not target:
        return True
    if target.startswith("file:"):
        return True
    if "..." in target:
        return True
    if is_template_heavy_path(source_rel) and is_placeholder_target(target):
        return True
    return False


def is_template_heavy_path(rel: str) -> bool:
    return (
        rel.startswith("30_Order/Templates/")
        or rel.startswith(".claude/skills/")
        or rel.startswith(".claude/agents/")
        or rel.startswith(".kiro/specs/")
    )


def is_placeholder_target(target: str) -> bool:
    placeholder_words = {
        "a",
        "b",
        "note",
        "note a",
        "note b",
        "real note",
        "nonexistent",
        "project",
        "project 1",
        "project 2",
        "related project",
        "topic",
        "source title",
        "concept 1",
        "concept 2",
        "entity 1",
        "entity 2",
        "related 1",
        "related 2",
        "x",
        "y",
    }
    key = normalize_key(target)
    if key in placeholder_words:
        return True
    if "yyyy" in key or "wxx" in key or "[" in key or "]" in key:
        return True
    return False


def print_health(ctx: dict[str, object], limit: int) -> None:
    files = typed_list(ctx["files"], MarkdownFile)
    projects = typed_list(ctx["projects"], ProjectInfo)
    active_projects = [row for row in projects if row.status != "archived"]
    missing_next = [row for row in active_projects if not row.next_action]

    print("# Jarvis Health")
    print()
    print(f"- Markdown files scanned: {len(files)}")
    print(f"- Files with frontmatter: {len(typed_list(ctx['with_frontmatter'], MarkdownFile))}")
    print(f"- Files missing `type`: {len(typed_list(ctx['missing_type'], MarkdownFile))}")
    print(f"- Files missing `status`: {len(typed_list(ctx['missing_status'], MarkdownFile))}")
    print(f"- Future-dated metadata fields: {len(ctx['future_dates'])}")
    print(f"- Project notes: {len(projects)}")
    print(f"- Active projects missing `next`: {len(missing_next)}")
    print(f"- Duplicate filenames: {len(ctx['duplicate_filenames'])}")
    print(f"- Files with likely mojibake: {len(ctx['encoding_hits'])}")
    print(f"- Enrichment candidates: {len(ctx['enrichment_candidates'])}")
    print(f"- Broken wikilinks: {len(ctx['broken_links'])}")
    print(f"- Ambiguous wikilinks: {len(ctx['ambiguous_links'])}")
    print()
    print("## Top Duplicate Filenames")
    print_table(["Count", "Name"], [(str(count), name) for name, count in ctx["duplicate_filenames"][:limit]])


def print_context_pack(root: Path, ctx: dict[str, object], limit: int) -> None:
    print("# Jarvis Context Pack")
    print()
    for rel in CONTEXT_FILES:
        print(f"## {rel.as_posix()}")
        text = read_text(root / rel)
        print(extract_brief(text, max_lines=24))
        print()

    print(f"## {SESSION_LOG.as_posix()} Tail")
    log_text = read_text(root / SESSION_LOG)
    print(tail_headings(log_text, max_headings=5))
    print()

    print("## Active Projects")
    projects = [row for row in typed_list(ctx["projects"], ProjectInfo) if row.status != "archived"]
    rows = [(row.rel, row.status, row.next_action or "(missing)") for row in projects[:limit]]
    print_table(["Path", "Status", "Next"], rows)


def print_projects(ctx: dict[str, object], limit: int) -> None:
    print("# Project Audit")
    print()
    projects = typed_list(ctx["projects"], ProjectInfo)
    active = [row for row in projects if row.status != "archived"]
    missing_next = [row for row in active if not row.next_action]
    stale_cutoff = TODAY - dt.timedelta(days=30)
    stale = [row for row in active if row.mtime < stale_cutoff]

    print(f"- Project notes: {len(projects)}")
    print(f"- Active project notes: {len(active)}")
    print(f"- Active projects missing `next`: {len(missing_next)}")
    print(f"- Active projects stale by file mtime: {len(stale)}")
    print()
    print("## Missing Next Actions")
    print_table(["Path", "Status", "Modified"], [(row.rel, row.status, row.mtime.isoformat()) for row in missing_next[:limit]])
    print()
    print("## Active Projects")
    print_table(["Path", "Status", "Next"], [(row.rel, row.status, row.next_action or "(missing)") for row in active[:limit]])


def print_links(ctx: dict[str, object], limit: int) -> None:
    print("# Link Audit")
    print()
    print(f"- Broken wikilinks: {len(ctx['broken_links'])}")
    print(f"- Ambiguous wikilinks: {len(ctx['ambiguous_links'])}")
    print()
    print("## Broken Wikilinks")
    print_table(["Source", "Target"], [(row["source"], row["target"]) for row in ctx["broken_links"][:limit]])
    print()
    print("## Ambiguous Wikilinks")
    print_table(
        ["Source", "Target", "Matches"],
        [(row["source"], row["target"], row["matches"]) for row in ctx["ambiguous_links"][:limit]],
    )


def print_dates(ctx: dict[str, object], limit: int) -> None:
    print("# Future Date Audit")
    print()
    print(f"- Future-dated metadata fields after {TODAY.isoformat()}: {len(ctx['future_dates'])}")
    print()
    print_table(
        ["Path", "Field", "Date"],
        [(row["path"], row["field"], row["date"]) for row in ctx["future_dates"][:limit]],
    )


def print_encoding(ctx: dict[str, object], limit: int) -> None:
    print("# Encoding Audit")
    print()
    print(f"- Files with likely mojibake: {len(ctx['encoding_hits'])}")
    print()
    print_table(["Hits", "Path"], [(str(row["count"]), row["path"]) for row in ctx["encoding_hits"][:limit]])


def print_enrichment_candidates(ctx: dict[str, object], limit: int) -> None:
    print("# Enrichment Candidates")
    print()
    candidates = typed_list(ctx["enrichment_candidates"], EnrichmentCandidate)
    print(f"- Candidate notes: {len(candidates)}")
    print("- Score favors tracked concepts, seed/sprout notes, and short notes missing learning sections.")
    print()
    rows = [
        (
            str(row.score),
            row.rel,
            row.note_type,
            row.status,
            row.track or "-",
            str(len(row.missing)),
            ", ".join(row.missing[:4]),
        )
        for row in candidates[:limit]
    ]
    print_table(["Score", "Path", "Type", "Status", "Track", "Missing", "Top Missing"], rows)


def write_report(root: Path, ctx: dict[str, object], limit: int) -> Path:
    report_dir = root / REPORT_DIR
    report_dir.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = report_dir / f"Jarvis Ops Report - {TODAY.isoformat()} {timestamp}.md"
    projects = typed_list(ctx["projects"], ProjectInfo)
    active_projects = [row for row in projects if row.status != "archived"]
    missing_next = [row for row in active_projects if not row.next_action]

    lines = [
        "---",
        "type: review",
        "status: complete",
        f"created: {TODAY.isoformat()}",
        "tags:",
        "  - review",
        "  - ops",
        "  - vault-health",
        "notes:",
        "  - \"[[00_Dashboard]]\"",
        "  - \"[[60_Claude/60_Indexes/Vault Health Dashboard]]\"",
        "---",
        "",
        f"# Jarvis Ops Report - {TODAY.isoformat()}",
        "",
        "## Summary",
        "",
        f"- Markdown files scanned: {len(ctx['files'])}",
        f"- Files with frontmatter: {len(ctx['with_frontmatter'])}",
        f"- Files missing `type`: {len(ctx['missing_type'])}",
        f"- Files missing `status`: {len(ctx['missing_status'])}",
        f"- Future-dated metadata fields: {len(ctx['future_dates'])}",
        f"- Project notes: {len(projects)}",
        f"- Active projects missing `next`: {len(missing_next)}",
        f"- Duplicate filenames: {len(ctx['duplicate_filenames'])}",
        f"- Files with likely mojibake: {len(ctx['encoding_hits'])}",
        f"- Enrichment candidates: {len(ctx['enrichment_candidates'])}",
        f"- Broken wikilinks: {len(ctx['broken_links'])}",
        f"- Ambiguous wikilinks: {len(ctx['ambiguous_links'])}",
        "",
        "## Highest Priority Findings",
        "",
        "- Add `next` actions to active projects that are still live.",
        "- Review future-dated `updated` and `last_drilled` fields before trusting dashboard freshness.",
        "- Treat duplicate course note names as path-sensitive links, especially `Week - N.md` files.",
        "- Fix mojibake only in curated batches; do not bulk rewrite archive or clipping material.",
        "",
        "## Active Projects Missing `next`",
        "",
        markdown_table(["Path", "Status", "Modified"], [(row.rel, row.status, row.mtime.isoformat()) for row in missing_next[:limit]]),
        "",
        "## Future-Dated Metadata",
        "",
        markdown_table(
            ["Path", "Field", "Date"],
            [(row["path"], row["field"], row["date"]) for row in ctx["future_dates"][:limit]],
        ),
        "",
        "## Likely Encoding Damage",
        "",
        markdown_table(["Hits", "Path"], [(str(row["count"]), row["path"]) for row in ctx["encoding_hits"][:limit]]),
        "",
        "## Link Health Samples",
        "",
        "### Broken Wikilinks",
        "",
        markdown_table(["Source", "Target"], [(row["source"], row["target"]) for row in ctx["broken_links"][:limit]]),
        "",
        "### Ambiguous Wikilinks",
        "",
        markdown_table(
            ["Source", "Target", "Matches"],
            [(row["source"], row["target"], row["matches"]) for row in ctx["ambiguous_links"][:limit]],
        ),
        "",
        "## Enrichment Candidates",
        "",
        markdown_table(
            ["Score", "Path", "Type", "Status", "Missing"],
            [
                (str(row.score), row.rel, row.note_type, row.status, str(len(row.missing)))
                for row in typed_list(ctx["enrichment_candidates"], EnrichmentCandidate)[:limit]
            ],
        ),
        "",
        "## Recommended Next Commands",
        "",
        "```powershell",
        ".\\30_Order\\System\\jarvis-cli\\jarvis.ps1 projects",
        ".\\30_Order\\System\\jarvis-cli\\jarvis.ps1 dates",
        ".\\30_Order\\System\\jarvis-cli\\jarvis.ps1 links --limit 50",
        ".\\30_Order\\System\\jarvis-cli\\jarvis.ps1 enrich-candidates --limit 25",
        "```",
        "",
        "This report is diagnostic only. It did not modify existing notes.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def typed_list(value: object, expected_type: type) -> list:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, expected_type)]


def print_table(headers: list[str], rows: list[tuple[str, ...]]) -> None:
    if not rows:
        print("(none)")
        return
    widths = [len(header) for header in headers]
    for row in rows:
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(str(cell)))
    print(" | ".join(header.ljust(widths[idx]) for idx, header in enumerate(headers)))
    print(" | ".join("-" * widths[idx] for idx, _ in enumerate(headers)))
    for row in rows:
        print(" | ".join(str(cell).ljust(widths[idx]) for idx, cell in enumerate(row)))


def markdown_table(headers: list[str], rows: list[tuple[str, ...]]) -> str:
    if not rows:
        return "_None found._"
    output = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        escaped = [str(cell).replace("|", "\\|") for cell in row]
        output.append("| " + " | ".join(escaped) + " |")
    return "\n".join(output)


def extract_brief(text: str, max_lines: int) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    meaningful: list[str] = []
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if line.strip() == "---":
            continue
        if line.strip():
            meaningful.append(line)
        if len(meaningful) >= max_lines:
            break
    return "\n".join(meaningful) if meaningful else "(empty)"


def tail_headings(text: str, max_headings: int) -> str:
    chunks = re.split(r"(?m)^(?=#{2,3}\s+)", text)
    chunks = [chunk.strip() for chunk in chunks if re.match(r"^#{2,3}\s+", chunk.strip())]
    selected = chunks[-max_headings:]
    shortened = [first_lines(chunk, max_lines=16) for chunk in selected]
    return "\n\n".join(shortened) if shortened else "(no session entries)"


def first_lines(text: str, max_lines: int) -> str:
    lines = text.splitlines()
    if len(lines) <= max_lines:
        return text
    return "\n".join(lines[:max_lines] + ["..."])


if __name__ == "__main__":
    raise SystemExit(main())

"""Read/write exported-cursor-composers.json without UTF-8 BOM issues."""
import json
from pathlib import Path

DEFAULT_INDEX_PATH = Path(__file__).parent.parent / "exported-cursor-composers.json"


def load_exported_index(index_path: Path) -> set[str]:
    if not index_path.exists():
        return set()
    try:
        # utf-8-sig strips a BOM if PowerShell or another tool wrote one
        data = json.loads(index_path.read_text(encoding="utf-8-sig"))
        if not isinstance(data, list):
            return set()
        return {str(x) for x in data}
    except (json.JSONDecodeError, OSError, TypeError):
        return set()


def save_exported_index(index_path: Path, composer_ids: list[str]) -> None:
    unique = sorted(set(composer_ids))
    index_path.write_text(
        json.dumps(unique, indent=2) + "\n",
        encoding="utf-8",
    )


def append_exported_composer(index_path: Path, composer_id: str) -> bool:
    """Append one ID. Returns True if added, False if already present."""
    ids = list(load_exported_index(index_path))
    if composer_id in ids:
        return False
    ids.append(composer_id)
    save_exported_index(index_path, ids)
    return True

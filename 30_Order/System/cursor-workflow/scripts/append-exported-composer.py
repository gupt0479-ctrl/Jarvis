#!/usr/bin/env python3
"""Append one composer UUID to exported-cursor-composers.json (BOM-safe).

Use this from the export skill instead of PowerShell Set-Content, which can
write a UTF-8 BOM and break json.loads() in list-cursor-composers.py.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from composer_index import DEFAULT_INDEX_PATH, append_exported_composer


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("composer_id", help="Composer UUID to append")
    ap.add_argument("--index", default=str(DEFAULT_INDEX_PATH))
    args = ap.parse_args()

    index_path = Path(args.index)
    if append_exported_composer(index_path, args.composer_id):
        print(f"APPENDED:{args.composer_id}")
    else:
        print(f"SKIPPED:{args.composer_id} (already in index)")


if __name__ == "__main__":
    main()

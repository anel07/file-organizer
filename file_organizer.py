#!/usr/bin/env python3
"""
file_organizer.py

Beginner-friendly script to organize files in a folder by file type.
Usage:
    python file_organizer.py --path "/path/to/folder" [--dry-run]

"""

import argparse
from pathlib import Path
import shutil
import sys

# Default mapping: category -> extensions
EXTENSIONS_MAP = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".odt", ".txt", ".rtf"},
    "Spreadsheets": {".xls", ".xlsx", ".csv", ".ods"},
    "Presentations": {".ppt", ".pptx", ".odp"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "Code": {".py", ".js", ".java", ".cpp", ".c", ".rb", ".go", ".ts"},
    "Audio": {".mp3", ".wav", ".ogg", ".m4a"},
    "Video": {".mp4", ".mkv", ".mov", ".avi"},
}

# Where unknown extensions will go
OTHER_DIR_NAME = "Others"


def categorize(file_path: Path):
    """Return category name for given file based on extension."""
    ext = file_path.suffix.lower()
    for category, exts in EXTENSIONS_MAP.items():
        if ext in exts:
            return category
    return OTHER_DIR_NAME


def make_unique(dst: Path) -> Path:
    """If dst exists, append a counter before extension to make it unique.
    e.g., report.pdf -> report (1).pdf -> report (2).pdf
    """
    if not dst.exists():
        return dst
    parent = dst.parent
    stem = dst.stem
    suffix = dst.suffix
    i = 1
    while True:
        candidate = parent / f"{stem} ({i}){suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def organize(target_path: Path, dry_run: bool = False):
    if not target_path.exists():
        print(f"Error: Path does not exist: {target_path}")
        return
    if not target_path.is_dir():
        print(f"Error: Path is not a directory: {target_path}")
        return

    for item in target_path.iterdir():
        # skip directories
        if item.is_dir():
            continue
        # skip hidden files (optional)
        if item.name.startswith('.'):
            continue

        category = categorize(item)
        dest_dir = target_path / category
        dest_file = dest_dir / item.name

        if dry_run:
            print(f"[DRY-RUN] Would move: {item.name} -> {category}/{item.name}")
            continue

        dest_dir.mkdir(exist_ok=True)
        unique_dest = make_unique(dest_file)
        try:
            shutil.move(str(item), str(unique_dest))
            print(f"Moved: {item.name} -> {unique_dest.relative_to(target_path)}")
        except Exception as e:
            print(f"Failed to move {item.name}: {e}")

    print("\nDone.")


def parse_args():
    parser = argparse.ArgumentParser(description="Organize files in a folder by file type")
    parser.add_argument('--path', required=True, help='Path to the folder to organize')
    parser.add_argument('--dry-run', action='store_true', help='Show what would happen without moving files')
    return parser.parse_args()


def main():
    args = parse_args()
    target = Path(args.path).expanduser()
    organize(target, dry_run=args.dry_run)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nCancelled by user')
        sys.exit(1)

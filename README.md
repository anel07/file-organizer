# File-organizer
Beginner-friendly file organizer script that sorts files by type.

This small utility organizes files inside a target folder into subfolders by file type. It's useful for cleaning up a messy `Downloads` folder or organizing project assets.

## Features
- Moves files into folders by extension (e.g., `Images/`, `PDFs/`, `Docs/`).
- Handles duplicate file names by appending a counter.
- Optional `--dry-run` mode to preview changes without moving files.
- Cross-platform (Windows / macOS / Linux) — requires Python 3.7+

## How to use
1. Clone or create a repo named `file-organizer` and add these two files: `README.md` and `file_organizer.py`.
2. Install Python 3.7+ if you don't have it already.
3. Run the script from the command line:

```bash
# SAFETY
# Always try --dry-run first so you can review planned moves.
# The script only moves files (not directories) and will create new subfolders as needed.
# Preview what would happen (does not move files) 
python file_organizer.py --path "/path/to/your/folder" --dry-run

# Actually organize files
python file_organizer.py --path "C:/Users/Anne/Downloads"

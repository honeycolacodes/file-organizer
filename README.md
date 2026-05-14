# 🗂️ File Organizer

A Python script that automatically sorts files in any folder into subfolders by file type.

## What it does
- Scans a folder for files
- Sorts them into: Images, Videos, Documents, Audio, Archives, Code, Other
- Works on any folder — just change one line

## How to use
1. Clone this repo
2. Open `organizer.py` and change `folder_to_organize` to your target folder
3. Run: `python organizer.py`

## Example output
```
Moved: vacation.jpg → Images/
Moved: resume.pdf → Documents/
Moved: song.mp3 → Audio/
Done! Your folder is organized.
```

## Tech used
- Python 3
- `os` and `shutil` (built-in libraries, no install needed)

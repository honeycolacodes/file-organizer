import os
import shutil

# The folder you want to organize (change this to any folder path)
folder_to_organize = os.path.expanduser("~/Downloads")

# File types and which folder they belong in
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
}

def organize_folder(folder):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        # Skip folders, only process files
        if os.path.isdir(filepath):
            continue

        # Get the file extension
        ext = os.path.splitext(filename)[1].lower()

        # Find which category it belongs to
        moved = False
        for category, extensions in file_types.items():
            if ext in extensions:
                dest_folder = os.path.join(folder, category)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(dest_folder, filename))
                print(f"Moved: {filename} → {category}/")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder, "Other")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(other_folder, filename))
            print(f"Moved: {filename} → Other/")

organize_folder(folder_to_organize)
print("Done! Your folder is organized.")

import os
import shutil
import time
from datetime import datetime

# File categories by extension
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.wmv'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.java', '.cpp', '.js', '.html', '.css', '.c', '.ts'],
    'Executables': ['.exe', '.msi', '.bat', '.sh'],
    'Others': []  # fallback
}

def is_hidden_or_system(file):
    return file.startswith('.') or file.lower() in ['thumbs.db', 'desktop.ini']

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def log_action(action):
    with open("file_sort_log.txt", "a") as log:
        log.write(f"{datetime.now()}: {action}\n")

def auto_sort_files(directory):
    os.chdir(directory)
    files = os.listdir()

    for file in files:
        if os.path.isdir(file) or is_hidden_or_system(file):
            continue

        _, file_ext = os.path.splitext(file)
        if not file_ext:
            continue

        category = get_category(file_ext)
        folder_name = os.path.join(directory, category)

        # Create category folder if not exists
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            log_action(f"Created folder: {folder_name}")

        try:
            shutil.move(file, os.path.join(folder_name, file))
            log_action(f"Moved file: {file} ➜ {category}/")
        except Exception as e:
            log_action(f"Error moving {file}: {str(e)}")

def monitor_folder(directory, interval=5):
    print(f"\n📁 Monitoring: {directory}")
    print("Sorting new files every", interval, "seconds. Press Ctrl+C to stop.\n")

    seen_files = set(os.listdir(directory))

    try:
        while True:
            time.sleep(interval)
            current_files = set(os.listdir(directory))
            new_files = current_files - seen_files

            if new_files:
                print("📦 New file(s) detected. Sorting...")
                auto_sort_files(directory)

            seen_files = set(os.listdir(directory))

    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")

if __name__ == "__main__":
    folder_path = input("🔍 Enter folder path to auto-sort: ").strip()

    if os.path.isdir(folder_path):
        monitor_folder(folder_path, interval=5)
    else:
        print("❌ Invalid folder path.")

# 📂 File Organizer (Real-Time Folder Organizer)

A Python script that automatically monitors and sorts files into folders based on their extensions. Organize your cluttered directories into structured folders like Images, Documents, Videos, Music, Archives, and more — all in real-time with logging enabled!

---

## ✨ Features

- 📁 **Monitors folders** continuously for new files
- 📦 **Auto-sorts files** by type (Images, Documents, Code, Music, Videos, etc.)
- 🧠 **Extension-based categorization**
- 🧾 **Logging** of every action in `file_sort_log.txt`
- ❌ Skips system/hidden files like `Thumbs.db`, `.DS_Store`, etc.
- 🔄 Runs continuously until you stop it (Ctrl+C)

---

## 🧠 How it Works:-

1. You input a folder path.
2. The script watches that folder for new files.
3. When new files appear, they are sorted into subfolders based on their extension (e.g., `.jpg` ➜ `Images/`, `.pdf` ➜ `Documents/`).
4. All actions (moves, errors, folder creations) are logged in `file_sort_log.txt`.

---

## 📦 File Categories

The script classifies files into:

- **Images** – `.jpg`, `.png`, `.svg`, etc.
- **Documents** – `.pdf`, `.docx`, `.pptx`, `.txt`, etc.
- **Music** – `.mp3`, `.wav`, etc.
- **Videos** – `.mp4`, `.mkv`, `.mov`, etc.
- **Archives** – `.zip`, `.rar`, `.7z`, etc.
- **Code** – `.py`, `.cpp`, `.html`, etc.
- **Executables** – `.exe`, `.bat`, `.sh`, etc.
- **Others** – uncategorized extensions

---

## ⚙️ Requirements

- Python 3.7+
- tkinter
- No external libraries required (uses standard library only)

---

## 🚀 How to Run

### 1️⃣ Clone the repository or copy the script

```bash
git clone https://github.com/SupritMandal015/file_organizer.git
```

### 2️⃣ Run the python script 

```bash
python file_sorter.py

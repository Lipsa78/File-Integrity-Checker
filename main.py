import hashlib
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
import datetime

# ===== Function to calculate SHA-256 hash of a file =====
def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# ===== Save the calculated hash to a .hash file =====
def save_hash(file_path, hash_value):
    with open(file_path + ".hash", "w") as f:
        f.write(hash_value)

# ===== Log the integrity check results to a log file =====
def log_result(file_path, result):
    with open("integrity_log.txt", "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {file_path} - {result}\n")

# ===== Main function to check file integrity =====
def check_integrity(file_path):
    if not os.path.exists(file_path):
        messagebox.showerror("Error", "Invalid file path!")
        return

    current_hash = calculate_hash(file_path)

    try:
        with open(file_path + ".hash", "r") as f:
            saved_hash = f.read()
    except FileNotFoundError:
        # Save initial hash if not found
        save_hash(file_path, current_hash)
        messagebox.showinfo("Hash Saved", f"No previous hash found for:\n{file_path}\nHash saved for future checks.")
        log_result(file_path, "Hash saved (initial)")
        return

    # Compare current hash with saved hash
    if current_hash == saved_hash:
        messagebox.showinfo("Integrity Check", f"File is intact:\n{file_path}")
        log_result(file_path, "File OK")
    else:
        messagebox.showwarning("Integrity Check", f"File has been modified:\n{file_path}")
        log_result(file_path, "File Modified!")

# ===== File selection with filters for common file types =====
def browse_files():
    file_paths = filedialog.askopenfilenames(
        title="Select files to check",
        filetypes=[
            ("All Supported Files", "*.pdf *.docx *.pptx *.txt"),
            ("PDF Files", "*.pdf"),
            ("Word Documents", "*.docx"),
            ("PowerPoint Presentations", "*.pptx"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*"),
        ]
    )
    for path in file_paths:
        check_integrity(path)

# ================= GUI SETUP =================
root = tk.Tk()
root.title("Advanced File Integrity Checker")
root.geometry("500x400")
root.configure(bg="#f0f4f8")

# Optional: Set custom window icon
try:
    root.iconbitmap("icon.ico")
except:
    pass  # Ignore if icon not available

# Optional: Load and display logo image
try:
    logo = PhotoImage(file="logo.png")
    logo_label = tk.Label(root, image=logo, bg="#f0f4f8")
    logo_label.pack(pady=10)
except:
    pass  # Skip if logo not found

# GUI Title
title = tk.Label(root, text="Advanced File Integrity Checker", font=("Helvetica", 16, "bold"), bg="#f0f4f8")
title.pack(pady=5)

# GUI Description
desc = tk.Label(root, text="Click below to select one or more files to verify.", font=("Helvetica", 12), bg="#f0f4f8")
desc.pack(pady=5)

# Browse Button
browse_btn = tk.Button(
    root,
    text="Select Files",
    command=browse_files,
    font=("Helvetica", 12),
    bg="#0078D7",
    fg="white",
    padx=12,
    pady=6
)
browse_btn.pack(pady=20)

# Footer Text
footer = tk.Label(root, text="Built using Python & hashlib", font=("Helvetica", 10), fg="gray", bg="#f0f4f8")
footer.pack(side="bottom", pady=10)

# Start the GUI loop
root.mainloop()

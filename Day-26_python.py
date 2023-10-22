# Implement a basic text editor with save and load functionality.
print("\nRuban Gino Singh - Day 26 of #100DaysOfCode\n")

print("Python program to implement a basic text editor with save and load functionality.\n")

import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
        window.title(f"Text Editor - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
        window.title(f"Text Editor - {file_path}")

window = tk.Tk()
window.title("Text Editor")

menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

text = tk.Text(window)
text.pack(expand="yes", fill="both")

window.mainloop()

# --------------------------------------------------------- #
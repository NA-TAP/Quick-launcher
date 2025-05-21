import tkinter as tk
from tkinter import filedialog

def save_as():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text.get("1.0", tk.END))

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, content)

# Create the main application window
notepad = tk.Tk()
notepad.title("Notepad")

# Set a default font for the text widget
font_size_16 = ("Courier New", 16)

# Create a frame for buttons
button_frame = tk.Frame(notepad)
button_frame.pack(fill=tk.X)

open_button = tk.Button(button_frame, text="Open", command=open_file)
open_button.pack(side=tk.LEFT, padx=5, pady=5)

saveas_button = tk.Button(button_frame, text="Save As", command=save_as)
saveas_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create a Text widget for user input
text = tk.Text(notepad, font=font_size_16)
text.pack(fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
notepad.mainloop()



import tkinter as tk

# Create the main application window
notepad = tk.Tk()
notepad.title("Notepad")  # Set the window title

# Set a default font for the text widget
font_size_16 = ("Arial", 16)

# Create a Text widget for user input
text = tk.Text(notepad, font=font_size_16)
text.pack(fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
notepad.mainloop()



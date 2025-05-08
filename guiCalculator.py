import tkinter as tk
from tkinter import ttk
import math

# Create main window
app = tk.Tk()
app.title("Calculator")
app.resizable(True, True)  # Allow resizing

# Create display
display = tk.Entry(app, width=35, justify="right", font=('Arial', 14))
display.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')

def button_click(value):
    if value == 'C':
        display.delete(0, tk.END)
    elif value == '\u2327':
        # Get current display content
        current = display.get()
        # Remove last character
        display.delete(0, tk.END)
        # Insert updated text (excluding last char)
        display.insert(0, current[:-1])
    elif value == '=':
        try:
            gg = display.get()
            gg = gg.replace('^', '**')
            gg = gg.replace('sqrt', 'math.sqrt')
            gg = gg.replace('cbrt', 'math.cbrt')
            gg = gg.replace('x', '*')
            gg = gg.replace('mod', '%')
            gg = gg.replace('sin', 'math.sin')
            gg = gg.replace('cos', 'math.cos')
            gg = gg.replace('tan', 'math.tan')
            result = eval(gg)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current + str(value))

# Define buttons
buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', 'x', '\u2327',
    '1', '2', '3', '-', 'M+',
    '0', '.', '=', '+', 'MR',
    '^', 'sqrt', 'cbrt', '.999\n999', 'mod',
    '(', ')', 'sin', 'cos', 'tan'
]

# Create and place buttons
row = 1
col = 0
for button in buttons:
    btn = tk.Button(
        app,
        text=button,
        width=5,
        height=2,
        font=('Arial', 12),
        command=lambda x=button: button_click(x)
    )
    btn.grid(
        row=row,
        column=col,
        sticky='nsew',
        padx=2,
        pady=2
    )
    col += 1
    if col > 4:
        col = 0
        row += 1

# Configure grid to be resizable
for i in range(5):
    app.grid_columnconfigure(i, weight=1)
for i in range(row + 1):
    app.grid_rowconfigure(i, weight=1)

# Start main loop
app.mainloop()

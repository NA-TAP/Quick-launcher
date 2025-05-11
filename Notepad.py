import tkinter as tk
notepad = tk.Tk
notepad.title = 'Notepad'
def let_us_do_key_checker(event):
  global key
  key = event.char
  

notepad.bind('<Key>', let_us_do_key_checker)
font_size_16 = ("Arial", 16)
text = tk.Text(notepad, font=font_size_16)
text.pack(fill=tk.BOTH, expand=True)
while True:
  text.insert(tk.END, key)



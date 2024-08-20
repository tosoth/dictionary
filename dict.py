import tkinter as tk
from tkhtmlview import HTMLLabel

import datetime
import os
import sys

from pystardict import Dictionary

dicts_dir = 'C:\\Users\\2346318\\coding'
dict1 = Dictionary(os.path.join(dicts_dir, 'Collins5'))

# Define the function to display HTML content
def show_html_content(event=None):
    global the_word, html_label
    the_word = input_box.get()

    html_content = dict1.dict[the_word]

    if 'html_label' in globals():
        html_label.pack_forget()  # Remove the old HTMLLabel widget

    html_label = HTMLLabel(root, html=html_content)
    html_label.pack()
    
    input_box.select_range(0, tk.END)
    input_box.icursor(tk.END)

def exit_app(event=None):
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Collins5 stardict app")

input_box = tk.Entry(root, width=50)
input_box.pack(pady=10)

# Create a button to trigger the HTML display
button = tk.Button(root, text="Start", command=show_html_content)
button.pack(pady=20)

# Bind the Enter key to the button click event
root.bind('<Return>', show_html_content)
root.bind('<Escape>', exit_app)

# Set focus to the input box when the app starts
input_box.focus_set()


# Run the application
root.mainloop()

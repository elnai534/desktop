import tkinter as tk
from config import impath, x, cycle, check, event_number
from gif_handler import load_gifs
from events import event
from gif_handler import load_gifs

# Set the path to the assets folder relative to the project directory
impath = "assets"

# Initialize tkinter window
window = tk.Tk()
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black')

# Load GIFs
gifs = load_gifs(impath)

# Create and pack label for displaying GIFs
label = tk.Label(window, bd=0, bg='black')
label.pack()

# Start event loop
window.after(1, event, cycle, check, event_number, x, window, label, gifs)
window.mainloop()

import tkinter as tk
import random

def load_gifs(impath):
    # Load gifs from impath
    return {
        'idle': [tk.PhotoImage(file=f'{impath}idle.gif', format=f'gif -index {i}') for i in range(5)],
        'idle_to_sleep': [tk.PhotoImage(file=f'{impath}idle_to_sleep.gif', format=f'gif -index {i}') for i in range(8)],
        'sleep': [tk.PhotoImage(file=f'{impath}sleep.gif', format=f'gif -index {i}') for i in range(3)],
        'sleep_to_idle': [tk.PhotoImage(file=f'{impath}sleep_to_idle.gif', format=f'gif -index {i}') for i in range(8)],
        'walk_positive': [tk.PhotoImage(file=f'{impath}walking_positive.gif', format=f'gif -index {i}') for i in range(8)],
        'walk_negative': [tk.PhotoImage(file=f'{impath}walking_negative.gif', format=f'gif -index {i}') for i in range(8)],
    }

def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randint(first_num, last_num)
    return cycle, event_number

def update_frame(cycle, check, event_number, x, window, label, gifs):
    frames = gifs.get('idle') if check == 0 else gifs.get('walk_positive')  # Add conditions for other actions
    frame = frames[cycle]
    cycle, event_number = gif_work(cycle, frames, event_number, 1, 9)

    window.geometry(f'100x100+{x}+1050')
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x, window, label, gifs)

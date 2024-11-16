import random
from gif_handler import gif_work, update_frame
from config import idle_num, sleep_num, walk_left, walk_right

def event(cycle, check, event_number, x, window, label, gifs):
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400, update_frame, cycle, check, event_number, x, window, label, gifs)
    elif event_number == 5:
        check = 1
        print('idle to sleep')
        window.after(100, update_frame, cycle, check, event_number, x, window, label, gifs)
    elif event_number in walk_left:
        check = 4
        print('walking left')
        window.after(100, update_frame, cycle, check, event_number, x, window, label, gifs)
    elif event_number in walk_right:
        check = 5
        print('walking right')
        window.after(100, update_frame, cycle, check, event_number, x, window, label, gifs)
    elif event_number in sleep_num:
        check = 2
        print('sleeping')
        window.after(1000, update_frame, cycle, check, event_number, x, window, label, gifs)
    elif event_number == 14:
        check = 3
        print('sleep to idle')
        window.after(100, update_frame, cycle, check, event_number, x, window, label, gifs)

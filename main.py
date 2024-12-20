import tkinter as tk
import time

root = tk.Tk()
screen_width = root.winfo_screenwidth()
work_height = root.winfo_screenheight()
root.destroy()

class Elina:
    def __init__(self):
        self.window = tk.Tk()

        self.idle = [
            tk.PhotoImage(file='assets/idle1.png'),
            tk.PhotoImage(file='assets/idle2.png')
        ]
        self.kiss = [
            tk.PhotoImage(file='assets/kiss1.png'),
            tk.PhotoImage(file='assets/kiss3.png'),
            tk.PhotoImage(file='assets/kiss4.png'),
            tk.PhotoImage(file='assets/kiss5.png'),
            tk.PhotoImage(file='assets/kiss6.5.png'),
            tk.PhotoImage(file='assets/kiss6.png'),
            tk.PhotoImage(file='assets/kiss7.png'),
            tk.PhotoImage(file='assets/kiss8.png'),
            tk.PhotoImage(file='assets/kiss9.png')
        ]
        self.wave = [
            tk.PhotoImage(file='assets/w1.png'),
            tk.PhotoImage(file='assets/w2.png'),
            tk.PhotoImage(file='assets/w3.png'),
            tk.PhotoImage(file='assets/w4.png'),
            tk.PhotoImage(file='assets/w5.png'),
            tk.PhotoImage(file='assets/w6.png')
        ]

        self.i_frame = 0
        self.state = 0  # 0: idle, 1: kiss, 2: wave
        self.animation_interval = 600  

        self.frame = self.idle[0]

        self.window.config(highlightbackground='black')
        self.label = tk.Label(self.window, bd=0, bg='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'black')

        self.label.pack(padx=0, pady=0, expand=True, fill=tk.BOTH)  

        self.x = int(screen_width * 0.8)
        self.y = work_height - 180  

        self.window.bind('<Button-1>', self.on_click)

        self.window.after(1, self.update)
        self.window.mainloop()

    def on_click(self, event):
        """Handle mouse click to trigger animations."""
        if self.state == 0:  
            self.state = 1
            self.animation_interval = 200  
        elif self.state == 1: 
            self.state = 2
            self.animation_interval = 250  
        elif self.state == 2:  
            self.state = 0
            self.animation_interval = 900  

    def animate(self, array):
        """Handles frame animation within the given array."""
        if self.i_frame < len(array) - 1:
            self.i_frame += 1
        else:
            self.i_frame = 0
            if self.state != 0: 
                self.state = 0
                self.animation_interval = 900  #idle speed resets
        return array[self.i_frame]

    def update(self):
        """Update the animation based on the current state."""
        if self.state == 0:  # Idle
            self.frame = self.animate(self.idle)
        elif self.state == 1:  # Kiss
            self.frame = self.animate(self.kiss)
        elif self.state == 2:  # Wave
            self.frame = self.animate(self.wave)

        self.window.geometry(f'64x180+{self.x}+{self.y}')  # Skinnier but taller window
        self.label.configure(image=self.frame)

        self.window.after(self.animation_interval, self.update)

elina = Elina()

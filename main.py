import tkinter as tk
from PIL import Image, ImageTk

#screen dimensions
root = tk.Tk()
screen_width = root.winfo_screenwidth()
work_height = root.winfo_screenheight()
root.destroy()

class Elina:
    def __init__(self):
        self.window = tk.Tk()

        #animations
        self.idle = [
            self.load_image('assets/idle1.png'),
            self.load_image('assets/idle2.png')
        ]
        self.kiss = [
            self.load_image('assets/kiss1.png'),
            self.load_image('assets/kiss3.png'),
            self.load_image('assets/kiss4.png'),
            self.load_image('assets/kiss5.png'),
            self.load_image('assets/kiss6.5.png'),
            self.load_image('assets/kiss6.png'),
            self.load_image('assets/kiss7.png'),
            self.load_image('assets/kiss8.png'),
            self.load_image('assets/kiss9.png')
        ]
        self.wave = [
            self.load_image('assets/w1.png'),
            self.load_image('assets/w2.png'),
            self.load_image('assets/w3.png'),
            self.load_image('assets/w4.png'),
            self.load_image('assets/w5.png'),
            self.load_image('assets/w6.png')
        ]

        self.i_frame = 0
        self.state = 0  # 0: idle, 1: kiss, 2: wave
        self.animation_interval = 600 

        self.frame = self.idle[0]

        self.animation_width = self.frame.width()
        self.animation_height = self.frame.height()

        #transparent window
        self.window.geometry(f'{self.animation_width}x{self.animation_height}')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'green')  

        #canvas
        self.canvas = tk.Canvas(
            self.window,
            width=self.animation_width,
            height=self.animation_height,
            highlightthickness=0,
            bg='green'  #transparent color
        )
        self.canvas.pack()

        self.label = tk.Label(self.canvas, bd=0, bg='green')  #transparent color
        self.label.place(x=0, y=0, width=self.animation_width, height=self.animation_height)

        taskbar_height = 38  
        self.x = int(screen_width * 0.8)
        self.y = work_height - self.animation_height - taskbar_height 

        self.window.bind('<Button-1>', self.on_click)

        self.window.after(1, self.update)
        self.window.mainloop()

    def load_image(self, filepath):
        """Load an image without altering its opacity."""
        img = Image.open(filepath).convert("RGBA")
        return ImageTk.PhotoImage(img)

    def on_click(self, event):
        """Handle mouse click to trigger animations."""
        if self.state == 0:  #idle, switch to kiss
            self.state = 1
            self.animation_interval = 200  #speed change
        elif self.state == 1:  # Kiss, switch to wave
            self.state = 2
            self.animation_interval = 250  #speed change
        elif self.state == 2:  # Wave, return to idle
            self.state = 0
            self.animation_interval = 600  #speed change

    def animate(self, array):
        """Handles frame animation within the given array."""
        if self.i_frame < len(array) - 1:
            self.i_frame += 1
        else:
            self.i_frame = 0
            if self.state != 0:  #return to idle after kiss or wave
                self.state = 0
                self.animation_interval = 600  #speed reset
        return array[self.i_frame]

    def update(self):
        """Update the animation based on the current state."""
        if self.state == 0:  #Idle
            self.frame = self.animate(self.idle)
        elif self.state == 1:  #Kiss
            self.frame = self.animate(self.kiss)
        elif self.state == 2:  #Wave
            self.frame = self.animate(self.wave)

        self.window.geometry(f'{self.animation_width}x{self.animation_height}+{self.x}+{self.y}')
        self.label.configure(image=self.frame)

        #next update
        self.window.after(self.animation_interval, self.update)

elina = Elina()

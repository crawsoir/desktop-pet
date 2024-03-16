import tkinter as tk
from win32api import GetMonitorInfo, MonitorFromPoint

class Pet:
    xwin = 0
    ywin = 0
    w = 500
    h = 500

    def __init__(self):

        #tkinter create root window
        self.root = tk.Tk()
        self.root.title('Testing...')

        self.default = tk.PhotoImage(file="default.png")
        self.eat = tk.PhotoImage(file="eat.png")

        self.canvas = tk.Canvas(self.root, bg="#aba2a3", width=self.w, height=self.h, highlightthickness=0)
        self.canvas_id = self.canvas.create_image(250, 250, image = self.default)
        self.canvas.pack()

        self.root.overrideredirect(True)
        self.root.wm_attributes('-transparentcolor','#aba2a3')

        #position the screen
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()

        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws/2-self.w, hs-self._get_taskbar_coords()-self.h))

        self.root.bind('<B1-Motion>', self._move)
        self.root.bind('<Button-1>', self._get_pos)
        self.root.bind('<ButtonRelease-1>', self._snap_to_taskbar)
        self.root.mainloop()

        
    def _get_pos(self, event):
        self.xwin = event.x
        self.ywin = event.y

    def _move(self, event):
        self.root.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')
        self.canvas.itemconfig(self.canvas_id, image = self.eat)

    def _snap_to_taskbar(self, event):
        window_y = self.root.winfo_screenheight()-self._get_taskbar_coords()-self.h
        self.root.geometry(f'+{event.x_root - self.xwin}+{window_y}')
        self.canvas.itemconfig(self.canvas_id, image = self.default)

    def _get_taskbar_coords(self):
        #get taskbar height
        monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
        monitor_area = monitor_info.get("Monitor")
        work_area = monitor_info.get("Work")
        return monitor_area[3]-work_area[3]



    
    
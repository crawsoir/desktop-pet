from tkinter import *
from win32api import GetMonitorInfo, MonitorFromPoint

w = 500
h = 500

#get taskbar height
monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")
work_area = monitor_info.get("Work")

#tkinter
root = Tk()
root.title('Testing...')

default = PhotoImage(file="default.png")
eat = PhotoImage(file="eat.png")

canvas = Canvas(root, bg="#aba2a3", width=w, height=h, highlightthickness=0)
canvas.create_image(250, 250, image=default)
canvas.pack()

root.overrideredirect(True)
root.wm_attributes('-transparentcolor','#aba2a3')

#position the screen
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

offset = monitor_area[3]-work_area[3]
root.geometry('%dx%d+%d+%d' % (w, h, ws/2-w, hs-offset-h))
root.mainloop()


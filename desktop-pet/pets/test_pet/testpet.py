import tkinter as tk

from . import test_pet_idle_state as idle
from . import test_pet_constants as constants
from utils import animator, context, helpers
from . import test_pet_sleep_state as sleep
class TestPet():
    w = constants.WIDTH
    h = constants.HEIGHT

    def __init__(self):
        # tkinter create root window
        self.root = tk.Tk()
        self.root.title('Test Pet')

        self.root.overrideredirect(True)
        self.root.wm_attributes('-transparentcolor', constants.TRANSPARENCY)
        self.root.configure(background=constants.TRANSPARENCY)

        # position the screen
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws/2-self.w, hs-helpers.get_taskbar_height()-self.h))

        self.root.bind('<Button-3>', self._do_popup)

        #right-click menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Quit", command=self.root.destroy)

        # initialize animator
        self.anim = animator.Animator(self.root)
        self.anim.add_animation('test_pet_idle', constants.ASSETS_PATH, 1)
        self.anim.add_animation('test_pet_blink', constants.ASSETS_PATH, 1)
        self.anim.add_animation('test_pet_yawn', constants.ASSETS_PATH, 8)
        self.anim.add_animation('closing', constants.ASSETS_PATH, 3)
        self.anim.add_animation('opening', constants.ASSETS_PATH, 3)
        self.anim.add_animation('asleep', constants.ASSETS_PATH, 2)
        self.anim.add_animation('sleeping', constants.ASSETS_PATH, 4)

        # initialize the state machine
        self.context = context.Context(idle.TestPetIdleState(), self.root, self.anim)

        self.root.mainloop()


    def _do_popup(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)
        self.menu.grab_release()


'''
class TestPet():
    # this colour becomes the background, and is then set to be transparent
    xwin = 0
    ywin = 0
    w = constants.WIDTH
    h = constants.HEIGHT


    def __init__(self):
        # tkinter create root window
        self.root = tk.Tk()
        self.root.title('Test Pet')

        self.root.overrideredirect(True)
        self.root.wm_attributes('-transparentcolor', constants.TRANSPARENCY)
        self.root.configure(background=constants.TRANSPARENCY)

        # position the screen
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()

        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws/2-self.w, hs-self._get_taskbar_coords()-self.h))

        #bind events to functions 
        self.root.bind('<B1-Motion>', self._move)
        self.root.bind('<Button-1>', self._set_mouse_pos)
        self.root.bind('<Button-3>', self._do_popup)
        self.root.bind('<ButtonRelease-1>', self._snap_to_taskbar)

        # initialize the state machine
        init_state = idle.TestPetIdleState()
        context.Context(init_state, self.root)

        #right-click menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Quit", command=self.root.destroy)

        self.root.mainloop()

    def _set_mouse_pos(self, event):
        self.xwin = event.x
        self.ywin = event.y

    def _move(self, event):
        self.root.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')

    def _snap_to_taskbar(self, event):
        window_y = self.root.winfo_screenheight()-self._get_taskbar_coords()-self.h
        self.root.geometry(f'+{event.x_root - self.xwin}+{window_y}')

    def _get_taskbar_coords(self):
        #get taskbar height
        monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
        monitor_area = monitor_info.get("Monitor")
        work_area = monitor_info.get("Work")
        return monitor_area[3]-work_area[3]
    
    def _do_popup(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)
        self.menu.grab_release()
'''
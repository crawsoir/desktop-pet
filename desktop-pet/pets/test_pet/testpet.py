from utils import context
from . import test_pet_idle_state as idle
from win32api import GetMonitorInfo, MonitorFromPoint
import tkinter as tk


class TestPet():
    # this colour becomes the background, and is then set to be transparent
    TRANSPARENCY = '#aba2a3'

    def __init__(self):
        # tkinter create root window
        self.root = tk.Tk()
        self.root.title('Test Pet')

        #self.root.overrideredirect(True)
        self.root.wm_attributes('-transparentcolor', self.TRANSPARENCY)

        # position the screen
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()

        # initialize the state machine
        init_state = idle.TestPetIdleState()
        context.Context(init_state, self.root)

        self.root.mainloop()
        
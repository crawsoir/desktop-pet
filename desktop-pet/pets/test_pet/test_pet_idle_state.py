import random

import tkinter as tk
from win32api import GetMonitorInfo, MonitorFromPoint

from . import test_pet_constants as constants
from . import test_pet_sleep_state as sleep
from utils import state, helpers

class TestPetIdleState(state.State):
    w = constants.WIDTH
    h = constants.HEIGHT
    xwin = 0
    ywin = 0
    blinking = False

    def enter(self) -> None:
        self.context.animator.play("test_pet_idle")

        #bind events to functions 
        self.context.root.bind('<B1-Motion>', self._move)
        self.context.root.bind('<Button-1>', self._set_mouse_pos)
        self.context.root.bind('<ButtonRelease-1>', self._snap_to_taskbar)

        self.update() #TODO: state machine calls update after enter returns?

    def update(self) -> None:
        if self.blinking:
            self.blinking = False
            self.context.animator.play("test_pet_blink")
            self.id=self.context.root.after(350, self.update) #TODO: move back to state machine?
        else:
            self.blinking = True
            self.context.animator.play("test_pet_idle")
            self.id=self.context.root.after(random.randint(1000,6000), self.update)
        

    def exit(self) -> None:
        self.context.root.unbind('<B1-Motion>')
        self.context.root.unbind('<Button-1>')
        self.context.root.unbind('<ButtonRelease-1>')
        if self.id != None:
            self.context.root.after_cancel(self.id)

    def _set_mouse_pos(self, event):
        self.xwin = event.x
        self.ywin = event.y

    def _move(self, event):
        self.context.root.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')

    def _snap_to_taskbar(self, event):
        window_y = self.context.root.winfo_screenheight()-helpers.get_taskbar_height()-self.h
        self.context.root.geometry(f'+{event.x_root - self.xwin}+{window_y}')
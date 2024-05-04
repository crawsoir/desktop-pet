import random

from . import test_pet_constants as constants
from . import test_pet_yawn_state as yawn
from utils import state, helpers

class TestPetIdleState(state.State):
    w = constants.WIDTH
    h = constants.HEIGHT
    hovering = False
    blink_timer = 50

    def enter(self, env={'xwin': 0, 'ywin':0}) -> None:
        self.xwin = env['xwin']
        self.ywin = env['ywin']
        self.id = None

        self.context.animator.play("test_pet_idle", loop=True)

        #bind events to functions 
        self.context.root.bind('<Button-1>', self._set_mouse_pos)
        self.context.root.bind('<B1-Motion>', self._move)
        self.context.root.bind('<ButtonRelease-1>', self._snap_to_taskbar)

    def update(self) -> None:

        if self.blink_timer == 0: # TODO: make a tkinter timer class 
            self.blink_timer = 20
            if self.context.animator.current_animation == "test_pet_idle":
                self.context.animator.play("test_pet_blink", loop=True)
            else:
                self.context.animator.play("test_pet_idle", loop=True)
        else:
            self.blink_timer -= 1
        

    def exit(self) -> None:
        self.context.root.unbind('<B1-Motion>')
        self.context.root.unbind('<Button-1>')
        self.context.root.unbind('<ButtonRelease-1>')
        if self.id != None:
            self.context.root.after_cancel(self.id)


    def _set_mouse_pos(self, event):
        self.hovering = True
        self.xwin = event.x
        self.ywin = event.y

    def _move(self, event):
        self.context.root.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')

    def _snap_to_taskbar(self, event):
        self.hovering = False
        window_y = self.context.root.winfo_screenheight()-helpers.get_taskbar_height()-self.h
        self.context.root.geometry(f'+{event.x_root - self.xwin}+{window_y}')
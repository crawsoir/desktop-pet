import random

from . import test_pet_constants as constants
from . import test_pet_yawn_state as yawn
from utils import state, helpers, timer #TODO: put some of these utils into a single file
#TODO: put all states in one file?
class TestPetIdleState(state.State):

    def enter(self, env={'xwin': 0, 'ywin':0}) -> None:
        self.w = constants.WIDTH
        self.h = constants.HEIGHT
        self.mouse_hovering = False
        self.blinking = False

        # mouse offset relative to window
        self.xwin = env['xwin']
        self.ywin = env['ywin']
        
        self.context.animator.play("test_pet_idle")

        #bind events to functions 
        self.context.root.bind('<Button-1>', self._set_mouse_pos)
        self.context.root.bind('<B1-Motion>', self._move)
        self.context.root.bind('<ButtonRelease-1>', self._snap_to_taskbar)

        self.timer = timer.TkinterTimer(self.context.root)

    def update(self) -> None:
        if self.timer.is_stopped:
            if self.blinking:
                if random.randint(0,2) == 0 and not self.mouse_hovering:
                    print("yawning")
                    self.context.transition_to(yawn.TestPetYawnState())
                    return

                self.context.animator.play("test_pet_idle")
                self.blinking = False
                self.timer.start(random.randint(3000,6000))
            else:
                self.context.animator.play("test_pet_blink")
                self.blinking = True
                self.timer.start(600)


    def exit(self) -> None:
        self.context.root.unbind('<B1-Motion>')
        self.context.root.unbind('<Button-1>')
        self.context.root.unbind('<ButtonRelease-1>')

    def _set_mouse_pos(self, event):
        self.mouse_hovering = True
        self.xwin = event.x
        self.ywin = event.y

    def _move(self, event):
        self.context.root.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')

    def _snap_to_taskbar(self, event=None):
        x_pos = event.x_root if event else self.xwin
        self.mouse_hovering = False
        window_y = self.context.root.winfo_screenheight()-helpers.get_taskbar_height()-self.h
        self.context.root.geometry(f'+{x_pos - self.xwin}+{window_y}')
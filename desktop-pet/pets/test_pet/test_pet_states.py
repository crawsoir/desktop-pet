import random

from . import test_pet_constants as constants
from utils import state, helpers, timer #TODO: put some of these utils into a single file

class TestPetIdleState(state.State):

    def enter(self, env={'x_offset': 0, 'y_offset':0}) -> None:
        self.mouse_hovering = False
        self.blinking = False

        # mouse offset relative to window, assumes a transition to idle where
        # the mouse is already held down
        self.x_offset = env['x_offset']
        self.y_offset = env['y_offset']
        if self.x_offset != 0 or self.y_offset != 0:
            self.mouse_hovering = True
        
        self.context.animator.play("test_pet_idle")

        #bind events to functions 
        self.context.root.bind('<Button-1>', self._set_mouse_pos)
        self.context.root.bind('<B1-Motion>', self._move)
        self.context.root.bind('<ButtonRelease-1>', self._snap_to_taskbar)
        self.timer = timer.TkinterTimer(self.context.root)

    def update(self) -> None:
        if self.timer.is_stopped:
            if self.blinking:
                if random.randint(0,1) == 0 and not self.mouse_hovering:
                    self.context.transition_to(TestPetYawnState())
                    return

                self.context.animator.play("test_pet_idle")
                self.blinking = False
                self.timer.start(random.randint(3000,6000))
            else:
                self.context.animator.play("test_pet_blink")
                self.blinking = True
                self.timer.start(600)

    def exit(self) -> None:
        self._snap_to_taskbar()
        self.context.root.unbind('<B1-Motion>')
        self.context.root.unbind('<Button-1>')
        self.context.root.unbind('<ButtonRelease-1>')

    def _set_mouse_pos(self, event):
        self.mouse_hovering = True
        self.x_offset = event.x
        self.y_offset = event.y

    def _move(self, event):
        self.context.root.geometry(f'+{event.x_root - self.x_offset}+{event.y_root - self.y_offset}')

    def _snap_to_taskbar(self, event=None):
        self.mouse_hovering = False
        x_pos = event.x_root - self.x_offset if event else self.context.root.winfo_x()
        #TODO: could put these calculations into a helper
        y_pos = self.context.root.winfo_screenheight()-helpers.get_taskbar_height()-constants.HEIGHT
        self.context.root.geometry(f'+{x_pos}+{y_pos}')


class TestPetYawnState(state.State):

    def enter(self) -> None:
        self.context.animator.play("test_pet_yawn", callback = self._switch_state)
        self.context.root.bind('<Button-1>', self._switch_to_idle)

    def update(self) -> None:
        pass

    def exit(self) -> None:
        self.context.root.unbind('<Button-1>')

    def _switch_to_idle(self, event):
        self.context.transition_to(TestPetIdleState(), {'x_offset': event.x, 'y_offset': event.y})

    def _switch_state(self):
        if random.randint(0, 1) == 0:
            self.context.transition_to(TestPetSleepState())
        else:
            self.context.transition_to(TestPetIdleState())


class TestPetSleepState(state.State):

    def enter(self) -> None:
        self.context.animator.play("sleeping", callback = self.done_sleeping)
        self.context.root.bind('<Button-1>', self._switch_to_idle)
        self.update()

    def update(self) -> None:
        pass

    def exit(self) -> None:
        self.context.root.unbind('<Button-1>')

    def done_sleeping(self):
        self.context.animator.play("asleep", loop = True)

    def _switch_to_idle(self, event):
        self.context.transition_to(TestPetIdleState(), {'x_offset': event.x, 'y_offset': event.y})
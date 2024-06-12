import random

import send2trash

from utils import state, helpers, timer #TODO: put some of these utils into a single file


def _switch_to_idle(context, x_offset=0, y_offset=0):
    context.transition_to(TestPetIdleState(), {'x_offset': x_offset, 'y_offset': y_offset})

class TestPetIdleState(state.State):

    def enter(self, env={'x_offset': 0, 'y_offset':0}) -> None:
        self.mouse_clicked = False
        self.blinking = False
        self.eating = False #TODO: add to env 

        # mouse offset relative to window, assumes a transition to idle where
        # the mouse is already held down
        self.x_offset = env['x_offset']
        self.y_offset = env['y_offset']
        if self.x_offset != 0 or self.y_offset != 0:
            self.mouse_clicked = True

        #bind events to functions 
        self.context.root.bind('<Button-1>', self._set_mouse_pos)
        self.context.root.bind('<B1-Motion>', self._move)
        self.context.root.bind('<ButtonRelease-1>', self._snap_to_taskbar)
        self.context.root.dnd_bind('<<DropEnter>>', self._file_entered)
                  
        self.context.animator.play("idle")
        self.timer = timer.TkinterTimer(self.context.root)

    def update(self) -> None:
        if self.eating:
            self.context.transition_to(TestPetEatState())

        if self.timer.is_stopped:
            if self.blinking:
                if random.randint(0,10) == 0 and not self.mouse_clicked:
                    self.context.transition_to(TestPetYawnState())
                    return

                self.context.animator.play("idle")
                self.blinking = False
                self.timer.start(random.randint(3000,6000))
            else:
                self.context.animator.play("blink")
                self.blinking = True
                self.timer.start(600)

    def exit(self) -> None:
        self._snap_to_taskbar()
        self.context.root.unbind('<B1-Motion>')
        self.context.root.unbind('<Button-1>')
        self.context.root.unbind('<ButtonRelease-1>')
        self.context.root.unbind('<<DropEnter>>')

    def _file_entered(self, event):
        self.eating = True

    def _set_mouse_pos(self, event):
        self.mouse_clicked = True
        self.x_offset = event.x
        self.y_offset = event.y

    def _move(self, event):
        self.context.root.geometry(f'+{event.x_root - self.x_offset}+{event.y_root - self.y_offset}')

    def _snap_to_taskbar(self, event=None):
        self.mouse_clicked = False
        x_pos = event.x_root - self.x_offset if event else self.context.root.winfo_x()
        #TODO: could put these calculations into a helper

        screen_height = self.context.root.winfo_screenheight()
        win_height = self.context.root.winfo_height()
        y_pos = screen_height-helpers.get_taskbar_height()-win_height
        self.context.root.geometry(f'+{x_pos}+{y_pos}')


class TestPetYawnState(state.State):

    def enter(self) -> None:
        self.context.animator.play("yawn", callback = self._switch_state)
        self.context.root.bind('<Button-1>', lambda event:_switch_to_idle(self.context, event.x, event.y))

    def update(self) -> None:
        pass

    def exit(self) -> None:
        self.context.root.unbind('<Button-1>')

    def _switch_state(self):
        if random.randint(0, 1) == 0:
            self.context.transition_to(TestPetSleepState())
        else:
            self.context.transition_to(TestPetIdleState())


class TestPetSleepState(state.State):

    def enter(self) -> None:
        self.context.animator.play("sleeping", callback = self.done_sleeping)
        self.context.root.bind('<Button-1>', lambda event:_switch_to_idle(self.context, event.x, event.y))

        self.timer = timer.TkinterTimer(self.context.root)
        self.timer.start(random.randint(30000,100000))

    def update(self) -> None:
        if self.timer.is_stopped:
            self.context.transition_to(TestPetIdleState())

    def exit(self) -> None:
        self.context.root.unbind('<Button-1>')

    def done_sleeping(self):
        self.context.animator.play("asleep", loop = True)


class TestPetEatState(state.State):

    def enter(self) -> None:
        self.mouse_clicked = False
        self.x = 0
        self.y = 0

        self.context.animator.play("opening")
        self.context.root.bind('<Button-1>', self._mouse_clicked)
        self.context.root.bind('<ButtonRelease-1>', self._mouse_released)
        self.context.root.dnd_bind('<<Drop>>', self._file_dropped)
        self.context.root.dnd_bind('<<DropLeave>>', 
                                   lambda event:_switch_to_idle(self.context, event.x_root, event.y_root))

    def update(self) -> None:
        pass

    def exit(self) -> None:
        self.context.root.unbind('<<Drop>>')
        self.context.root.unbind('<<DropLeave>>')

    def _mouse_clicked(self, event):
        self.x = event.x
        self.y = event.y

    def _mouse_released(self, event):
        self.x = 0
        self.y = 0

    def _file_dropped(self, event):
        send2trash.send2trash(event.data[1:-1].replace("/", "\\"))
        self.context.animator.play("closing", callback = _switch_to_idle(self.context))
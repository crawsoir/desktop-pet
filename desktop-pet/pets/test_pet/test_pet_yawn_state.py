import random

from . import test_pet_idle_state as idle
from . import test_pet_sleep_state as sleep
from utils import state

class TestPetYawnState(state.State):

    def enter(self) -> None:
        self.context.animator.play("test_pet_yawn", callback = self.switch_state)
        self.context.root.bind('<Button-1>', self._switch_to_idle)
        self.update()

    def update(self) -> None:
        pass

    def exit(self) -> None:
        self.context.root.unbind('<Button-1>')

    def _switch_to_idle(self, event):
        self.context.transition_to(idle.TestPetIdleState(), {'xwin': event.x, 'ywin': event.y})

    def switch_state(self):
        if random.randint(0, 1) == 0:
            self.context.transition_to(sleep.TestPetSleepState())
        else:
            self.context.transition_to(idle.TestPetIdleState())
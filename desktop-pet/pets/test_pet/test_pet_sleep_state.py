import random

from . import test_pet_idle_state as idle
from utils import state

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
        self.context.transition_to(idle.TestPetIdleState(), {'xwin': event.x, 'ywin': event.y})

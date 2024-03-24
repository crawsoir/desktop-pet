import random

from . import test_pet_constants as constants
from . import test_pet_idle_state as idle
from utils import state, helpers

class TestPetYawnState(state.State):

    def enter(self) -> None:
        self.context.animator.play("test_pet_yawn")
        self.context.root.bind('<Button-1>', self._switch_to_idle)
        self.update()

    def update(self) -> None:
        pass

    def exit(self) -> None:
        self.context.root.unbind('<Button-1>')

    def _switch_to_idle(self, event):
        self.context.transition_to(idle.TestPetIdleState(), {'xwin': event.x, 'ywin': event.y})
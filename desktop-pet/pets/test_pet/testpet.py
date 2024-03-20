from utils import context
from . import test_pet_idle_state as idle

class TestPet():
    def __init__(self):
        state = idle.TestPetIdleState()
        context.Context(state)
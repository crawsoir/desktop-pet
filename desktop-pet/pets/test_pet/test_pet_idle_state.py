from utils import state

class TestPetIdleState(state.State):
    def enter(self) -> None:
        print("entering")

    def update(self) -> None:
        print("updating")

    def exit(self) -> None:
        print("exiting")

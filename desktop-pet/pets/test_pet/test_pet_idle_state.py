from utils import state
import tkinter as tk


class TestPetIdleState(state.State):
    def enter(self) -> None:
        print("entering")
        self.update()

    def update(self) -> None:
        print("updating")

    def exit(self) -> None:
        print("exiting")

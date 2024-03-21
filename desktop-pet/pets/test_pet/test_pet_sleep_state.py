import random

from PIL import Image, ImageTk
import tkinter as tk

from . import test_pet_constants as constants
from utils import state


class TestPetSleepState(state.State):
    # number of frames
    max_sleep_frames = 2

    def enter(self) -> None:
        # prepare and size the animation frames
        self.asleep_frames = []
        for i in range(self.max_sleep_frames):
            img = Image.open(constants.ASSETS_PATH + 
                             f'\\asleep{i}.png').resize((constants.WIDTH, constants.HEIGHT))
            self.asleep_frames.append(ImageTk.PhotoImage(img))

        self.current_frame = 0

        # configure the tkinter label
        self.label = tk.Label(self.context.root, bd=0, bg=constants.TRANSPARENCY)
        self.label.configure(image = self.asleep_frames[self.current_frame])
        self.label.pack()
        self.update()

    def update(self) -> None:
        self.current_frame = (self.current_frame + 1) % self.max_sleep_frames
        self.label.configure(image = self.asleep_frames[self.current_frame])
        self.label.after(400, self.update)


    def exit(self) -> None:
        self.label.destroy()

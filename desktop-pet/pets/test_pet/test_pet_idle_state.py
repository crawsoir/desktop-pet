import random

from PIL import Image, ImageTk
import tkinter as tk

from . import test_pet_constants as constants
from . import test_pet_sleep_state as sleep
from utils import state


class TestPetIdleState(state.State):
    # number of frames
    max_idle_frames = 2
    max_yawn_frames = 8

    yawn_count = 0
    yawning = False

    def enter(self) -> None:
        # prepare and size the animation frames
        self.idle_frames = []
        for i in range(self.max_idle_frames):
            img = Image.open(constants.ASSETS_PATH + 
                             f'\\test_pet_idle{i}.png').resize((constants.WIDTH, constants.HEIGHT))
            self.idle_frames.append(ImageTk.PhotoImage(img))

        self.yawn_frames = []
        for i in range(self.max_yawn_frames):
            img = Image.open(constants.ASSETS_PATH + 
                             f'\\test_pet_yawn{i}.png').resize((constants.WIDTH, constants.HEIGHT))
            self.yawn_frames.append(ImageTk.PhotoImage(img))

        ''' old code for reference, TODO delete later
        self.idle_frames = [tk.PhotoImage(file=constants.ASSETS_PATH + f'\\idle\\test_pet_idle{i}.png')
                            for i in range(self.max_frames)]
        '''
        self.current_frame = 0
        self.yawn_frame = 0

        # configure the tkinter label
        self.label = tk.Label(self.context.root, bd=0, bg=constants.TRANSPARENCY)
        self.label.configure(image = self.idle_frames[self.current_frame])
        self.label.pack()
        self.update()

    def update(self) -> None:
        # yawning animation 
        if self.yawning:
            self.yawn_frame = (self.yawn_frame + 1) % self.max_yawn_frames
            self.label.configure(image = self.yawn_frames[self.yawn_frame])
            if self.yawn_frame == 0:
                self.yawning = False
                self.yawn_count += 1
            if self.yawn_count > 3:
                sleep_state = sleep.TestPetSleepState()
                self.context.transition_to(sleep_state)
                return
            self.id=self.label.after(300, self.update)
            return
        else: 
            self.yawning = random.randint(0, 25 - 5*self.yawn_count) == 0

        # default animation
        self.current_frame = (self.current_frame + 1) % self.max_idle_frames
        self.label.configure(image = self.idle_frames[self.current_frame])

        # eyes open faster
        if self.current_frame == 1:
            self.id=self.label.after(400, self.update)
        else:
            self.id=self.label.after(random.randint(4000,6000), self.update)

    def exit(self) -> None:
        if self.id != None:
            self.label.after_cancel(self.id)
        self.label.destroy()

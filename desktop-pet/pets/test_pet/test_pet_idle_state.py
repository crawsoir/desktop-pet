from utils import state
from . import test_pet_constants as constants
import tkinter as tk
from PIL import Image, ImageTk


class TestPetIdleState(state.State):
    # TODO: optimize by moving animation code to an animation manager?
    # number of frames
    max_frames = 2

    def enter(self) -> None:
        # prepare and size the animation frames
        self.idle_frames = []
        for i in range(self.max_frames):
            #TODO width and height as constants
            img = Image.open(constants.ASSETS_PATH + f'\\idle\\test_pet_idle{i}.png').resize((500, 500))
            self.idle_frames.append(ImageTk.PhotoImage(img))

        ''' old code for reference, TODO delete later
        self.idle_frames = [tk.PhotoImage(file=constants.ASSETS_PATH + f'\\idle\\test_pet_idle{i}.png')
                            for i in range(self.max_frames)]
        '''
        self.current_frame = 0

        # configure the tkinter label
        self.label = tk.Label(self.context.root, bd=0, bg=constants.TRANSPARENCY)
        self.label.configure(image = self.idle_frames[self.current_frame])
        self.label.pack()
        self.update()

    def update(self) -> None:
        self.current_frame = (self.current_frame + 1) % self.max_frames
        self.label.configure(image = self.idle_frames[self.current_frame])

        # eyes open faster
        if self.current_frame == 1:
            self.label.after(500, self.update)
        else:
            self.label.after(5000, self.update)

    def exit(self) -> None:
        self.label.destroy()

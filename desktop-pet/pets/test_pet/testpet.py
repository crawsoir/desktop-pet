import tkinter as tk

from .test_pet_states import TestPetIdleState as idle
from . import test_pet_constants as constants
from utils import animator, context, helpers

class TestPet():

    def __init__(self):
        self.w = constants.WIDTH
        self.h = constants.HEIGHT

        # tkinter create root window
        self.root = tk.Tk()
        self.root.title('Test Pet')

        self.root.overrideredirect(True)
        self.root.wm_attributes('-transparentcolor', constants.TRANSPARENCY)
        self.root.wm_attributes('-topmost', True)
        self.root.configure(background=constants.TRANSPARENCY)

        # position the screen
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws/2-self.w, hs-helpers.get_taskbar_height()-self.h))

        self.root.bind('<Button-3>', self._do_popup)

        #right-click menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Quit", command=self.root.destroy)

        # initialize animator
        self.anim = animator.Animator(self.root)
        self.anim.add_animation('idle', constants.ASSETS_PATH, 1)
        self.anim.add_animation('blink', constants.ASSETS_PATH, 1)
        self.anim.add_animation('yawn', constants.ASSETS_PATH, 8)
        self.anim.add_animation('closing', constants.ASSETS_PATH, 3)
        self.anim.add_animation('opening', constants.ASSETS_PATH, 3)
        self.anim.add_animation('asleep', constants.ASSETS_PATH, 2)
        self.anim.add_animation('sleeping', constants.ASSETS_PATH, 4)

        # initialize the state machine
        self.context = context.Context(idle(), self.root, self.anim)

        self.root.mainloop()


    def _do_popup(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)
        self.menu.grab_release()
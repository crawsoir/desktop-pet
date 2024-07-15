import tkinter as tk

from tkinterdnd2 import TkinterDnD, DND_FILES

from .test_pet_states import TestPetIdleState as idle
from utils import animator, context, helpers


TRANSPARENCY = '#aba2a3'
ASSETS_PATH = 'desktop-pet\\pets\\test_pet\\sprites'
WIDTH = 500
HEIGHT = 500

class TestPet():

    def __init__(self):
        # tkinter create root window
        self.root = TkinterDnD.Tk()
        self.root.title('Test Pet')

        self.root.overrideredirect(True)
        self.root.wm_attributes('-transparentcolor', TRANSPARENCY)
        self.root.wm_attributes('-topmost', True)
        self.root.configure(background=TRANSPARENCY)

        # position the screen
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, ws/2-WIDTH, hs-helpers.get_taskbar_height()-HEIGHT))

        # event binds
        self.root.bind('<Button-3>', self._do_popup)
        self.root.drop_target_register(DND_FILES)

        # right-click menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Quit", command=self.root.destroy)

        # initialize animator
        self.anim = animator.Animator(self.root, default_resize = (500, 500))
        self.anim.add_animation('idle', ASSETS_PATH, 1)
        self.anim.add_animation('blink', ASSETS_PATH, 1)
        self.anim.add_animation('yawn', ASSETS_PATH, 8)
        self.anim.add_animation('closing', ASSETS_PATH, 3, fps=6)
        self.anim.add_animation('opening', ASSETS_PATH, 3, fps=5)
        self.anim.add_animation('asleep', ASSETS_PATH, 2)
        self.anim.add_animation('sleeping', ASSETS_PATH, 4)

        # initialize the state machine
        self.context = context.Context(idle(), self.root, self.anim)

        self.root.mainloop()


    def _do_popup(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)
        self.menu.grab_release()
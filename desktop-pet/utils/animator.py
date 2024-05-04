from PIL import Image, ImageTk
import tkinter as tk


class Animator():
    def __init__(self, parent):
        self.animations = {}
        self.anim_meta = {}
        #TODO get trasparent colour automatically
        self.label = tk.Label(parent, bd=0, bg='#aba2a3')
        self.label.pack()
        self.parent = parent
        self._id = None

        self._curr_animation = None
        self._curr_frame = 0
        self._loop = False

    def add_animation(self, anim_name, file_path, num_frames, start_frame=0, fps=3):
        if anim_name in self.animations:
            raise Exception(f'{anim_name} is already the name of an animation')
        
        self.animations[anim_name] = []
        for i in range(start_frame, num_frames):
            #TODO: get size automatically
            img = Image.open(file_path + f'\\{anim_name}{i}.png').resize((500, 500))
            self.animations[anim_name].append(ImageTk.PhotoImage(img))
        self.anim_meta[anim_name] = {'fps': 1000//fps, 'len': num_frames}

    def del_animation(self, anim_name):
        if anim_name in self.animations:
            self.animations.pop(anim_name)
            self.anim_meta.pop(anim_name)

    def play(self, anim_name, loop = False, callback = None):
        if self._id is not None:
            self.label.after_cancel(self._id)

        self._loop = loop
        self._curr_animation = anim_name
        self._curr_frame = 0
        self._callback = callback
        self._play_loop()

    def _play_loop(self):
        self.label.configure(image = self.animations[self._curr_animation][self._curr_frame])
        self._curr_frame = (self._curr_frame + 1) % self.anim_meta[self._curr_animation]['len']

        # end of animation
        if self._curr_frame == 0 and not self._loop:
            if self._callback:
                self._callback() #temp fix, callback only runs for non loops. gotta add the context loop
            self._id = None
            return
        
        self._id = self.label.after(self.anim_meta[self._curr_animation]['fps'], self._play_loop)
    
    @property
    def current_animation(self):
        return self._curr_animation

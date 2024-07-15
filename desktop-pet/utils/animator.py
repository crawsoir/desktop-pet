from PIL import Image, ImageTk
import tkinter as tk


class Animator():
    
    FPS = "fps"
    LEN = "len"
    BG = "bg"

    def __init__(self, parent, default_bg='#aba2a3', default_resize=None):
        self.default_bg = default_bg
        self.default_resize = default_resize

        self.animations = {}
        self.anim_meta = {}
        self.label = tk.Label(parent, bd=0, bg=default_bg)
        self.label.pack()
        self.parent = parent
        self._id = None

        self._curr_animation = None
        self._curr_frame = 0
        self._loop = False

    def add_animation(self, anim_name, file_path, num_frames, start_frame=0, fps=3, resize=None, bg=None):
        if anim_name in self.animations:
            raise Exception(f'{anim_name} is already the name of an animation')
        # set animation metadata
        self.animations[anim_name] = []
        self.anim_meta[anim_name] = {self.FPS: 1000//fps, self.LEN: num_frames, self.BG: bg if bg else self.default_bg}
        # add each frame to the animation
        for i in range(start_frame, num_frames):
            img = Image.open(file_path + f'\\{anim_name}{i}.png')
            # override default resize if new value provided (note: will always resize if default resize is provided)
            anim_resize = resize if resize else self.default_resize
            if anim_resize: 
                img = img.resize(anim_resize)
            self.animations[anim_name].append(ImageTk.PhotoImage(img))

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
        self.label.configure(image = self.animations[self._curr_animation][self._curr_frame], 
                             bg = self.anim_meta[self._curr_animation][self.BG])
        self._curr_frame = (self._curr_frame + 1) % self.anim_meta[self._curr_animation][self.LEN]

        # end of animation
        if self._curr_frame == 0 and not self._loop:
            if self._callback:
                # important: callback function cannot loop or hang, or else many function 
                # calls will build and never terminate
                self._callback() 
            self._id = None
            return
        
        self._id = self.label.after(self.anim_meta[self._curr_animation][self.FPS], self._play_loop)
    
    @property
    def current_animation(self):
        return self._curr_animation

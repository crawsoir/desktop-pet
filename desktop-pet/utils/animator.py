from PIL import Image, ImageTk
import tkinter as tk


class Animator():
    def __init__(self, parent):
        self.animations = {}
        #TODO get trasparent colour automatically
        self.label = tk.Label(parent, bd=0, bg='#aba2a3')
        self.label.pack()
        self.parent = parent

        self.curr_animation = None
        self.curr_frame = 0

        self._playing = False
        self._paused = False

    def add_animation(self, anim_name, file_path, num_frames, start_frame=0, fps=12):
        if anim_name in self.animations:
            raise Exception(f'{anim_name} is already the name of an animation')
        
        self.animations[anim_name] = []
        for i in range(num_frames):
            #TODO: get size automatically
            img = Image.open(file_path + f'\\{anim_name}{i}.png').resize((500, 500))
            self.animations[anim_name].append(ImageTk.PhotoImage(img))

    def del_animation(self, anim_name):
        if anim_name in self.animations:
            self.animations.pop(anim_name)

    def current_animation(self):
        return self.curr_animation

    def play(self, anim_name):
        self.curr_animation = anim_name
        self.curr_frame = 0
        self._play_loop()

    def _play_loop(self): #TODO: add option to loop or one shot
        self.label.configure(image = self.animations[self.curr_animation][self.curr_frame])
        self.curr_frame = (self.curr_frame + 1) % len(self.animations[self.curr_animation])
        self.label.after(400, self._play_loop) #TODO: use fps

    def pause(self):
        pass

    def resume(self):
        pass

    def stop(self):
        pass

from PIL import Image, ImageTk
import tkinter as tk


class Animator():
    def __init__(self, parent):
        self.animations = {}
        #TODO get trasparent colour automatically
        self.label = tk.Label(parent, bd=0, bg='#aba2a3')
        self.curr_animation = None

    def add_animation(self, anim_name, file_path, num_frames, fps=12):
        if anim_name not in self.animations:
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

        pass

    def pause(self, anim_name):
        pass


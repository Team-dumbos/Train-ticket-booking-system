import os
# from PIL import ImageTk, Image
import PIL.Image
import PIL.ImageTk
from tkinter import *



def get_image(path,height = None, width = None):
	fp = open(path,"rb")
	image = PIL.Image.open(fp)
	if height is not None and width is not None:
		image = image.resize((height,width),PIL.Image.ANTIALIAS)
	image_cpy = PIL.ImageTk.PhotoImage(image)
	label1 = Label(image = image_cpy)

	label1.image = image_cpy
	return image_cpy

def get_path(folder, file):
	return os.path.join(folder,file)

def change_page(page1 = None,page2 = None,title = None):
	#changes all contents from page1 to page2
	if page1 is not None:
		for widget in page1:
			widget.remove_grid()

	if title is not None:
		root.title(title)

	if page2 is not None:
		for widget in page2:
			widget.make_grid()

import tkinter as tk


class custom_entry(tk.Entry):
    def __init__(self, container, placeholder,color = 'grey', *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color


    def foc_in(self, *args):
        self.show = '7'
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()
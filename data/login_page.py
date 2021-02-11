# from data.helper_functions import *
try:
	from data.custom_grid import *
	from data.constants import *
except:
	from custom_grid import *
	from constants import *
from tkinter import *


import os
# from tkinter import *
from PIL import ImageTk, Image

def get_image(path,height = None, width = None):
	image = Image.open(path)
	if height is not None and width is not None:
		image = image.resize((height,width),Image.ANTIALIAS)
	image = ImageTk.PhotoImage(image)
	return image

def get_path(folder, file):
	return os.path.join(folder,file)

def get_login_page(root):

	user_image = get_image(get_path('assets','user.png'),200,200)

	user_image_label = Label(root, image = user_image)
	user_image_label = custom_grid(user_image_label,1,1,30,20)

	user_name = Label(root, text = "Username:",font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	user_name = custom_grid(user_name,2,0,30,30)



	return [user_image_label,user_name]

if __name__ == '__main__':
	root = Tk()
	page = get_login_page(root)
	for item in page:
		item.make_grid()
	root.mainloop()
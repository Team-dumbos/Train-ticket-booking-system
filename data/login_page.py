# from data.helper_functions import *
from custom_grid import *
from constants import *
from tkinter import *
import os
from PIL import ImageTk, Image

def get_image(path,height = None, width = None):
	image = Image.open(path)
	if height is not None and width is not None:
		image = image.resize((height,width),Image.ANTIALIAS)
	image_cpy = ImageTk.PhotoImage(image)
	label1 = Label(image = image_cpy)

	label1.image = image_cpy
	return image_cpy

def get_path(folder, file):
	return os.path.join(folder,file)

def get_login_page(root):

	username = StringVar(root)
	password = StringVar(root)

	user_image = get_image(get_path('assets','male_user.jfif'),200,200)

	user_image_label = Label(root, image = user_image)
	user_image_label = custom_grid(user_image_label,1,1,30,20)

	user_name = Label(root, text = "Username:",font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	user_name = custom_grid(user_name,2,0,10)
	username_entry = Entry(root, text= 'Username',textvariable = username,font = ('clean',12))
	username_entry = custom_grid(username_entry,2,1,0,10)

	passwd = Label(root,text = "Password:",font =('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	passwd = custom_grid(passwd,3,0,10,10)
	passwd_entry = Entry(root, text= 'Password',textvariable = password,show= '*',font = ('clean',12))
	passwd_entry = custom_grid(passwd_entry,3,1,0,10)

	return [user_image_label,user_name,username_entry,passwd,passwd_entry]

if __name__ == '__main__':
	root = Tk()
	root.title('Login Page')
	root.geometry('458x480+800+450')

	img1 = Image.open(os.path.join('assets','login_page_bg.jpg'))

	image = img1.resize((450,450),Image.ANTIALIAS)

	test = ImageTk.PhotoImage(image)

	label1 = Label(image = test)

	label1.image = test

	label1.place(x=0,y=0)

	page = get_login_page(root)
	for item in page:
		item.make_grid()
	root.mainloop()
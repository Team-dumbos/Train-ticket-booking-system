
try:
	from data.helper_functions import *
	from data.custom_grid import *
	from data.constants import *
	from data.all_pages import *
except:
	from custom_grid import *
	from constants import *
	from helper_functions import *
	from all_pages import *
from tkinter import *
import os
from PIL import ImageTk, Image
import openpyxl
from xlrd import open_workbook
from tkinter import messagebox
import runpy



def get_login_page(root):
	global username, password, login_page
	username = StringVar(root)
	password = StringVar(root)

	user_image = get_image(get_path('assets','male_user.jfif'),200,200)

	user_image_label = Label(root, image = user_image)
	user_image_label = custom_grid(user_image_label,1,1,30,20)

	user_name = Label(root, text = "Username:",font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	user_name = custom_grid(user_name,2,0,10)
	username_entry = custom_entry(root, text= 'Username',textvariable = username,font = ('clean',12),placeholder = "Enter your username")
	username_entry = custom_grid(username_entry,2,1,0,10)

	passwd = Label(root,text = "Password:",font =('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	passwd = custom_grid(passwd,3,0,10,10)
	passwd_entry = custom_entry(root, text= 'Password',textvariable = password,font = ('clean',12),placeholder = 'enter your password')
	passwd_entry = custom_grid(passwd_entry,3,1,0,10)


	login_button = Button(root,text="Login", font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR, command = lambda : validate_user(root))
	login_button = custom_grid(login_button,4,1,10,10)


	register_button = Button(root,text = "New User? Register here",font = ('clean',13,'underline'), bg = MAIN_COLOR, fg = TERTIARY_COLOR, bd = 0, command = lambda: change_page(login_page,get_page('register_page', root)))
	register_button = custom_grid(register_button,5,1,10,10)

	login_page = [user_image_label,user_name,username_entry,passwd,passwd_entry,login_button,register_button]
	
	return login_page

def validate_user(root):
	loc = os.path.join('data','user_details.xlsx')
	workb = open_workbook(loc)
	sheet1 = workb.sheet_by_index(0)
	if username.get() is not None and password.get() is not None :
		for i  in range(10000):
			try:
				user_val = sheet1.cell_value(i,0)
			except:
				continue

			user_pass = sheet1.cell_value(i,4)
			if user_val == username.get():
				if user_pass == password.get():
					print("Successfully login")
					root.destroy()
					# change_page(login_page, get_page('register_page', root))
					runpy.run_path(os.path.join('data','main_page.py'))
					break
				else:
					messagebox.showerror('error','Password is Invalid')
					break
		else:
			messagebox.showerror("Error","Username is Invalid")

	else:
		messagebox.showinfo('Error','Please enter your username and password')

	
# to remove this main block
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
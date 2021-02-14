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
from tkcalendar import Calendar, DateEntry
import os
from PIL import ImageTk, Image
import openpyxl
from tkinter import messagebox
from threading import Thread
from xlrd import open_workbook


generated_otp = ''
register_page = None

def get_register_page(root):
	global name,email, gender, date_of_birth, passw, confirm_password, otp, register_page
	name = StringVar(root)
	email = StringVar(root)
	gender = StringVar(root)
	date_of_birth = StringVar(root)
	passw = StringVar(root)
	confirm_password = StringVar(root)
	otp = StringVar(root)

	register_label = Label(root, text = "Register",font = ('clean',30), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	register_label = custom_grid(register_label,1,2,20,30)

	name_label = Label(root,text = "Name:",font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	name_label = custom_grid(name_label,2,1,30,20)

	name_entry = custom_entry(root, textvariable = name,font = ('clean',12),placeholder = "Enter your name")
	name_entry = custom_grid(name_entry,2,2,0,20)

	email_label = Label(root, text="Email:",font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	email_label = custom_grid(email_label,3,1,30,10)

	email_entry = custom_entry(root, textvariable = email,font = ('clean',12),placeholder = "Enter your email")
	email_entry = custom_grid(email_entry,3,2,0,10)

	gender_label = Label(root, text = "Gender:", font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	gender_label = custom_grid(gender_label, 4,1,30,10)

	gender_entry = OptionMenu(root, gender, "Male", "Female","Non-binary")
	gender_entry = custom_grid(gender_entry, 4,2, 0,10,ipadx = 30)

	gender.set('Male')

	date_of_birth_label = Label(root, text = "Date of Birth:",font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	date_of_birth_label = custom_grid(date_of_birth_label,5,1,30,10)

	date_of_birth_entry = DateEntry(root,locale = 'en_IN',date_pattern = "dd/mm/yyyy",width=20, font = ('clean',13),textvariable = date_of_birth, bd = 0)
	date_of_birth_entry = custom_grid(date_of_birth_entry,5,2,0,10)

	password_label = Label(root, text = "Password",font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	password_label = custom_grid(password_label, 6,1,30,10)

	password_entry = custom_entry(root,textvariable = passw,font = ('clean',12),placeholder = "Enter your password")
	password_entry = custom_grid(password_entry,6,2,0,10)

	confirm_password_label = Label(root, text = "Password",font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	confirm_password_label = custom_grid(confirm_password_label, 7,1,30,10)

	confirm_password_entry = custom_entry(root,textvariable = confirm_password,font = ('clean',12),placeholder = "Confirm your password")
	confirm_password_entry = custom_grid(confirm_password_entry,7,2,0,10)

	otp_button = Button(root,text = "Send OTP", font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR, command = lambda: send_otp())
	otp_button = custom_grid(otp_button,8, 2, 0, 10)

	otp_label = Label(root, text = "OTP:", font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	otp_label = custom_grid(otp_label,9, 1, 30, 10)

	otp_entry = custom_entry(root, textvariable = otp,font = ('clean',12),placeholder = "Enter the OTP")
	otp_entry = custom_grid(otp_entry, 9, 2, 0, 10)

	register_button = Button(root,text = "Register", font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR, command = lambda: validate_data(root))
	register_button = custom_grid(register_button,10, 2, 0, 10)
	# print(get_login_page(root))

	# go_to_login_button = Button(root,text = "Go to Login page")

	register_page =  [register_label, name_label, email_label, otp_entry, otp_label, otp_button, gender_entry, register_button, confirm_password_entry, confirm_password_label, password_label, password_entry, email_entry, name_entry,date_of_birth_label,date_of_birth_entry, gender_label]

	return register_page

def validate_data(root):
	#TODO on 13-02-2021

	name_value = name.get()
	email_value = email.get()
	date_of_birth_value = date_of_birth.get()
	gender_value = gender.get()
	password_value = passw.get()
	confirm_password_value = confirm_password.get()
	otp_value = otp.get()

	if name_value == "Enter your name":
		messagebox.showinfo('error','Please enter your name')
		return

	if email_value == "Enter your email":
		messagebox.showinfo('error','Please enter your email')
		return

	if date_of_birth == "":
		messagebox.showinfo('error','Please enter your date of birth')
		return

	if password_value == "Enter your password":
		messagebox.showinfo('error','Please enter your password')
		return

	if password_value != confirm_password_value:
		messagebox.showinfo('error','passwords do not match')
		return

	if otp_value != generated_otp:
		messagebox.showinfo('error','OTP does not match')
		return
	save_register_details(root)
	
def send_otp():
	global generated_otp
	email_value = email.get()
	generated_otp = generate_otp()

	t = Thread(target = send_email, args = (email_value, generated_otp))
	t.start()

def save_register_details(root):
	workb = open_workbook(os.path.join('data','user_details.xlsx'))
	sheet1 = workb.sheet_by_index(0)

	index = -1
	#to find empty set in the workbook to write date
	for i in range(10000):
		try:
			val = sheet1.cell_value(i,0)

		except:
			index = i
			break

	xfile = openpyxl.load_workbook(os.path.join('data','user_details.xlsx'),read_only = False)
	sheet = xfile['users']
	sheet[f'A{index+1}']=name.get()
	sheet[f'B{index+1}'] = email.get()
	sheet[f'C{index+1}']=gender.get()
	sheet[f'D{index+1}']=date_of_birth.get()
	sheet[f'E{index+1}']=passw.get()
	xfile.save(os.path.join('data','user_details.xlsx'))
	
	change_page(register_page, get_page('login_page', root))
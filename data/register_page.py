try:
	from data.helper_functions import *
	from data.custom_grid import *
	from data.constants import *
except:
	from custom_grid import *
	from constants import *
	from helper_functions import *

from tkinter import *
from tkcalendar import Calendar, DateEntry
import os
from PIL import ImageTk, Image
import openpyxl

def get_register_page(root):
	name = StringVar(root)
	email = StringVar(root)
	gender = StringVar(root)
	date_of_birth = StringVar(root)
	passw = StringVar(root)
	confirm_password = StringVar(root)

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

	# go_to_login_button = Button(root,text = "Go to Login page")

	return [register_label, name_label, email_label, gender_entry,	confirm_password_entry, confirm_password_label, password_label, password_entry, email_entry, name_entry,date_of_birth_label,date_of_birth_entry, gender_label]

def validate_data():
	#TODO on 13-02-2021
	pass
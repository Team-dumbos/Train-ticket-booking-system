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

def get_main_page():
	screen = Tk() #--this one , but dont use root, as the name already exists -- okay
	screen.title("")
	#no create and return like previous pages? -- example??? -- like login and register page
	#or else main page is seperate from all others? --its ok do like this itself

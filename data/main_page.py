try:
	from data.helper_functions import *
	from data.custom_grid import *
	from data.constants import *
	from data.all_pages import *
	from data.datetime import *
except:
	from custom_grid import *
	from constants import *
	from helper_functions import *
	from all_pages import *
	from datetime import *
from tkinter import *
import os
import datetime

def username_display():
	pass

def get_main_page(screen): 
	screen.title("Railway Reservation System")
	screen.iconbitmap(os.path.join('assets', 'train-icon.ico'))
	screen.geometry('1280x720')
	screen.configure(bg = MAIN_COLOR)

	clock1 = Clock(root)
	clock1.pack()
	date = dt.datetime.now()
	# Takes the date and formats it.
	format_date = f"{date:%a, %b %d %Y}"


	datetime1 = Label(screen, text = f"{date: %a, %b %d %Y}",font = ('clean',9), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	datetime1 = custom_grid(datetime1,0,30)


	title = Label(screen,text="Welcome to the Railway Reservation System",font = ('clean',22),bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	title = custom_grid(title,1,8,50,50,90)

	dashboard = Button(screen,text = "Dashboard",font = ('clean',15), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	dashboard = custom_grid(dashboard,3,0,50,20,10,10)

	booking = Button(screen,text="Train Ticket Booking",font = ('clean',15), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	booking= custom_grid(booking,5,0,20,20,10,10)

	waiting = Button(screen,text = 'Waiting List',font = ('clean',13), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
	waiting = custom_grid(waiting,7,0,20,20,10,10)

	details = [title,dashboard,booking,waiting,datetime1]

	return details




screen = Tk()

page = get_main_page(screen)
for item in page:
	item.make_grid()

screen.mainloop()


	

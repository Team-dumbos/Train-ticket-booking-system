try:
	from data.helper_functions import *
	from data.custom_grid import *
	from data.constants import *
	from data.all_pages import *
	from data.Marquee import Marquee
except:
	from custom_grid import *
	from constants import *
	from helper_functions import *
	from all_pages import *
	from Marquee import Marquee

from tkinter import *
# from tkinter.ttk import PhotoImage
import os
import datetime

def user_display():
	pass


def refresh_time(date):
	date1 = datetime.datetime.now()
	date.configure(text = f"{date1: %a, %b %d %Y %H:%M:%S}")
	screen.after(1000,lambda: refresh_time(date))

screen = Tk()

screen.title("Railway Reservation System")
try:
	screen.iconbitmap(os.path.join('data','assets', 'train-icon.ico'))
except:
	screen.iconbitmap(os.path.join('assets', 'train-icon.ico'))
screen.geometry('1000x650')
screen.configure(bg = MAIN_COLOR)



date = datetime.datetime.now()


datetime1 = Label(screen, text = f"{date: %a, %b %d %Y %H:%M:%S}",font = ('clean',9), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
datetime1.grid(row = 0,column = 0)


title = Marquee(screen,text="Welcome to the Railway Reservation System",font = ('clean',22),bg = MAIN_COLOR, fg = TERTIARY_COLOR,fps = 200)
title.grid(row = 1,column = 0,padx = 50,pady = 50, ipadx = 100)

frame = Frame(screen,bg = MAIN_COLOR)

frame.grid(row = 2,column = 0,padx = 50)

dashboard = Button(frame,text = "Dashboard",font = ('clean',15), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
dashboard.grid(row = 3,column = 0,padx = 50,pady = 20,ipadx = 100,ipady = 100)

booking = Button(frame,text="Train Ticket Booking",font = ('clean',15), bg = MAIN_COLOR, fg = TERTIARY_COLOR)
booking.grid(row = 3,column = 1,padx = 50,pady = 20,ipadx = 60,ipady = 100)

refresh_time(datetime1)
screen.mainloop()


	

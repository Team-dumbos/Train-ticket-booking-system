from tkinter import *
root = Tk()

from data.constants import *
import os
from data.custom_grid import custom_grid
from data.login_page import *
from PIL import ImageTk, Image


root.geometry('600x400')
root.configure(bg = MAIN_COLOR)
root.title('Railway Reservation')



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




login_page = get_login_page(root)
register_page = []
main_page = []
dashboard_page = []
book_tickets = []
seat_picking = []
payment_page = []
admin_page = []
admin_edit_page = []

change_page(page2 = login_page)

root.mainloop()
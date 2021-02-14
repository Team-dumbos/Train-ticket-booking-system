from tkinter import *
root = Tk()

from data.constants import *
import os
from data.custom_grid import custom_grid
from data.login_page import *
from data.register_page import *
from PIL import ImageTk, Image



root.geometry('500x600')
root.configure(bg = MAIN_COLOR)
root.title('Railway Reservation')



login_page = get_login_page(root)
register_page = get_register_page(root)
main_page = []
dashboard_page = [] 
book_tickets = []
seat_picking = []
payment_page = []
admin_page = []
admin_edit_page = []



change_page(page2 = login_page)

root.mainloop()
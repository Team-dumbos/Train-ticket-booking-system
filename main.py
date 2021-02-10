from tkinter import *


root = Tk()
root.geometry('300x300')

class custom_grid:
	def __init__(self,widget,row,column,padx = None, pady = None, ipadx = None, ipady = None):
		self.widget = widget
		self.row = row
		self.column = column
		self.padx = padx
		self.pady = pady
		self.ipadx = ipadx
		self.ipady = ipady

	def make_grid(self):
		self.widget.grid(row=self.row,column=self.column,padx=self.padx,pady=self.pady,ipadx=self.ipadx,ipady=self.ipady)

	def remove_grid(self):
		self.widget.grid_forget()

def front_page():
	for widget in page1:
		widget.remove_grid()
	for widget in page2:
		widget.make_grid()

def back_page():
	for widget in page2:
		widget.remove_grid()
	for widget in page1:
		widget.make_grid()

greeting_label = Label(root,text="Welcome to IRCTC")
greeting_label = custom_grid(greeting_label,1,1,padx = 30, pady = 20)


submit_button = Button(root,text="Submit",command=front_page)
submit_button = custom_grid(submit_button,2,1)

submit_button1 = Button(root,text="Submit",command=back_page)
submit_button1 = custom_grid(submit_button1,2,1)

greeting_label.make_grid()
submit_button.make_grid()

page1 = [greeting_label,submit_button]
page2 = [submit_button1]

root.mainloop()
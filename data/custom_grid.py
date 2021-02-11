class custom_grid:
	'''
	custom class to implement independent pages using grid
	'''
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
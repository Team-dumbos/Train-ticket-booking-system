try:
	from data.constants import *

except ImportError:
	from constants import *

from tkinter import *

root = Tk()
root.configure(bg = MAIN_COLOR)
root.title('Dashboard')

root.mainloop()

from tkinter import *
import theme

class Rooms(Frame):
	def __init__(self, parent):
		super().__init__(parent, background=theme.background_primary)
		self.pack(fill = BOTH, expand=True)

		self.parent = parent
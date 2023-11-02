from tkinter import *
import data
import theme

class ChessWindow(Frame):
	def __init__(self, parent):
		super().__init__(parent, background=theme.background_primary)
		self.pack(fill=BOTH, expand=True)

		self.parent = parent
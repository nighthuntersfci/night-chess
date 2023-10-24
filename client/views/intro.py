from tkinter import *
import theme

class Intro(Frame):
	def __init__(self, parent, set_view):
		super().__init__(parent, background=theme.background_primary)
		self.pack(fill = BOTH, expand=True)

		# Top Bar
		top = Frame(self, background=theme.background_secondary)
		top.pack(fill=X, side="top")
		top.grid_columnconfigure(0, weight=1)
		top.grid_columnconfigure(2, weight=1)

		Label(top, text="Night Chess", background=theme.background_secondary, foreground=theme.text_primary, font=("Arial", 20)).grid(row=0, column=1, pady=(10, 0))
		Label(top, text="By Night Hunters", background=theme.background_secondary, foreground=theme.text_secondary, font=("Arial", 10)).grid(row=1, column=1, pady=(0, 10))

		
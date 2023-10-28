from tkinter import *
import theme

class Rooms(Frame):
	def __init__(self, parent):
		super().__init__(parent, background=theme.background_primary)
		self.pack(fill = BOTH, expand=True)

		self.parent = parent

		# Top Bar
		top = Frame(self, background=theme.background_secondary)
		top.pack(fill=X, side="top")
		top.grid_columnconfigure(0, weight=1)
		top.grid_columnconfigure(1, weight=1)

		Label(top, text="Rooms", background=theme.background_secondary, foreground=theme.text_primary, font=("Arial", 20)).grid(row=0, column=0, pady=(10, 0))
		Button(top, text="Create Room", background=theme.color_primary, foreground=theme.text_primary, border="0", width=20, activebackground=theme.color_secondary, activeforeground=theme.text_primary).grid(row=0, column=1, pady=20)
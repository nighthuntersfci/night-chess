from tkinter import *
import socket_service
import theme
import asyncio

class Intro(Frame):
	def __init__(self, parent, set_view):
		super().__init__(parent, background=theme.background_primary)
		self.pack(fill = BOTH, expand=True)

		self.set_view = set_view

		# Top Bar
		top = Frame(self, background=theme.background_secondary)
		top.pack(fill=X, side="top")
		top.grid_columnconfigure(0, weight=1)
		top.grid_columnconfigure(2, weight=1)

		Label(top, text="Night Chess", background=theme.background_secondary, foreground=theme.text_primary, font=("Arial", 20)).grid(row=0, column=1, pady=(10, 0))
		Label(top, text="By Night Hunters", background=theme.background_secondary, foreground=theme.text_secondary, font=("Arial", 10)).grid(row=1, column=1, pady=(0, 10))

		prompt = Frame(self, background=theme.background_primary)
		prompt.pack(fill=BOTH, expand=True, side="bottom")
		prompt.grid_columnconfigure(0, weight=1)
		prompt.grid_columnconfigure(2, weight=1)
		prompt.grid_rowconfigure(0, weight=1)
		prompt.grid_rowconfigure(4, weight=1)

		self.name = StringVar()

		Label(prompt, text="Enter Your Name:", background=theme.background_primary, foreground=theme.text_primary, font=("Arial", 30)).grid(row=1, column=1, pady=(10, 0))
		entry = Entry(prompt, background="white", textvariable=self.name, foreground="black", font=("Arial", 15), border="0")
		entry.grid(row=2, column=1)
		
		Button(prompt, text="Enter", background=theme.color_primary, foreground=theme.text_primary, border="0", width=20, activebackground=theme.color_secondary, activeforeground=theme.text_primary, command=self.set_username).grid(row=3, column=1, pady=20)
		

	def set_username(self):
		socket_service.set_username(self.name.get())
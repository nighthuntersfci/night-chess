from tkinter import *
import socket_service
import theme
import data
from views.rooms import Rooms
from utils.paths import get_full_path

class Intro(Frame):
    def __init__(self, parent):
        super().__init__(parent, background=theme.background_primary)
        self.pack(fill=BOTH, expand=True)

        self.parent = parent

        # Top Bar
        top = Frame(self, background=theme.background_secondary)
        top.pack(fill=X, side="top")
        top.grid_columnconfigure(0, weight=1)
        top.grid_columnconfigure(2, weight=1)

        Label(
            top,
            image=PhotoImage(file=get_full_path("assets/logo.png"))
        ).grid(row=0, column=1)

        prompt = Frame(self, background=theme.background_primary)
        prompt.pack(fill=BOTH, expand=True, side="bottom")
        prompt.grid_columnconfigure(0, weight=1)
        prompt.grid_columnconfigure(2, weight=1)
        prompt.grid_rowconfigure(0, weight=1)
        prompt.grid_rowconfigure(4, weight=1)

        self.name = StringVar()

        Label(
            prompt,
            text="Enter Your Name:",
            background=theme.background_primary,
            foreground=theme.text_primary,
            font=("Arial", 30),
        ).grid(row=1, column=1, pady=(10, 0))
        entry = Entry(
            prompt,
            background="white",
            textvariable=self.name,
            foreground="black",
            font=("Arial", 15),
            border="0",
        )
        entry.bind("<Return>", self.set_username)
        entry.grid(row=2, column=1)

        Button(
            prompt,
            text="Enter",
            background=theme.color_primary,
            foreground=theme.text_primary,
            border="0",
            width=20,
            activebackground=theme.color_secondary,
            activeforeground=theme.text_primary,
            command=self.set_username,
        ).grid(row=3, column=1, pady=20)

    def set_username(self, event=0):
        if len(self.name.get()) <= 8:
            socket_service.set_username(self.name.get())
            data.name = self.name.get()

            data.rooms_window = Rooms(self.parent)
            self.destroy()

        else:
            error = Label(
                self,
                text="Your name must be less or equal than 8 characters.",
                font=("Arial", 18),
            )
            error.pack()

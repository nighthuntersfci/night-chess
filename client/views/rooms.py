from tkinter import *
import theme
import data


class Rooms(Frame):
    def __init__(self, parent):
        super().__init__(parent, background=theme.background_primary)
        self.pack(fill=BOTH, expand=True)

        self.parent = parent

        # Top Bar
        top = Frame(self, background=theme.background_secondary)
        top.pack(fill=X, side="top")
        top.grid_columnconfigure(0, weight=1)
        top.grid_columnconfigure(1, weight=1)

        Label(
            top,
            text="Rooms",
            background=theme.background_secondary,
            foreground=theme.text_primary,
            font=("Arial", 20),
        ).grid(row=0, column=0, pady=(10, 0))
        Button(
            top,
            text="Create Room",
            background=theme.color_primary,
            foreground=theme.text_primary,
            border="0",
            width=20,
            activebackground=theme.color_secondary,
            activeforeground=theme.text_primary,
        ).grid(row=0, column=1, pady=20)

        # Rooms List
        list = Frame(self, background=theme.background_primary)
        list.pack(fill=BOTH, expand=True, side="top", padx=30, pady=20)

        for i in range(len(data.rooms)):
            room = Frame(list, background=theme.background_secondary, width=20)
            room.pack(fill=X, pady=10)
            room.grid_columnconfigure(0, weight=1)
            room.grid_columnconfigure(1, weight=1)
            room.grid_columnconfigure(2, weight=1)

            Label(
                room,
                text=data.rooms[i]["name"],
                background=theme.background_secondary,
                foreground=theme.text_primary,
                font=("Arial", 16),
            ).grid(row=0, column=0, pady=5)
            Label(
                room,
                text=(str(data.rooms[i]["amount"]) + "/2"),
                background=theme.background_secondary,
                foreground=theme.text_primary,
                font=("Arial", 16),
            ).grid(row=0, column=1, pady=5)
            button1 = Button(
                room,
                text="Join",
                background=theme.color_primary,
                foreground=theme.text_primary,
                activebackground=theme.color_secondary,
                activeforeground=theme.text_primary,
                border="0",
                width=14,
            )
            button1.grid(row=0, column=2, pady=5)

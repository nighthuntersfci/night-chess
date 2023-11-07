from tkinter import *
import theme
import data
import socket_service
from views.chess_window import ChessWindow


class Rooms(Frame):
    def __init__(self, parent):
        super().__init__(parent, background=theme.background_primary)
        self.pack(fill=BOTH, expand=True)

        self.parent = parent

        # Top Bar
        top = Frame(self, background=theme.background_secondary)
        top.pack(fill=X, side="top")
        top.grid_columnconfigure(0, weight=4)
        top.grid_columnconfigure(1, weight=1)
        top.grid_columnconfigure(2, weight=1)

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
            command=self.create_game
        ).grid(row=0, column=1, pady=20)
        Button(
            top,
            text="Refresh",
            background=theme.color_primary,
            foreground=theme.text_primary,
            border="0",
            width=20,
            activebackground=theme.color_secondary,
            activeforeground=theme.text_primary,
            command=self.refresh
        ).grid(row=0, column=2, pady=20)

        # Rooms List
        self.list = Frame(self, background=theme.background_primary)
        self.list.pack(fill=BOTH, expand=True, side="top", padx=30, pady=20)

        self.load_rooms()

    def load_rooms(self):
        for i in range(len(data.rooms)):
            room = Frame(self.list, background=theme.background_secondary, width=20)
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
                text=(str(len(data.rooms[i]["players"])) + "/2"),
                background=theme.background_secondary,
                foreground=theme.text_primary,
                font=("Arial", 16),
            ).grid(row=0, column=1, pady=5)
            # Check the room is full or not
            stat = NORMAL
            if len(data.rooms[i]["players"]) == 2: 
                status = "Full"
                stat = DISABLED 
                color = theme.disabled_button
            else : 
                status = "Join"
                color = theme.color_primary
            button1 = Button(
                room,
                text=status,
                background=color,
                foreground=theme.text_primary,
                activebackground=theme.color_secondary,
                activeforeground=theme.text_primary,
                border="0",
                width=14,
                state=stat,
                command=lambda: self.join(data.rooms[i], i)
            )
            button1.grid(row=0, column=2, pady=5)

    def refresh(self):  
        
        for widget in self.list.winfo_children():
            widget.destroy()

        self.load_rooms()

    def create_game(self):
        socket_service.sio.emit("create_room")

        data.room_window = ChessWindow(self.parent, False)
        self.destroy()

    def join(self, room, room_id):
        socket_service.sio.emit("join", room_id)

        data.room_window = ChessWindow(self.parent, True, opponent_name=room["players"][0]["name"])
        self.destroy()

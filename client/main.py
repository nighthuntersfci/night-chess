# Dependencies
from tkinter import *
import threading
import socket_service
import os

# Theme
import theme

# Views
from views.intro import Intro


def gui_thread():
    root = Tk()
    root.geometry("960x700")
    root.title("Night Chess: Local Multiplayer")
    root.resizable(False, False)
    root.configure(background=theme.background_primary)
    root.wm_iconphoto(False, PhotoImage(file=os.path.join(os.path.dirname(__file__), "icon.png")))

    Intro(root)

    root.mainloop()


def network_thread():
    socket_service.start()


t1 = threading.Thread(target=gui_thread)
t2 = threading.Thread(target=network_thread)

t1.start()
t2.start()

t1.join()
t2.join()

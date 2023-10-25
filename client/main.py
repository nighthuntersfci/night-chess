# Dependencies
from tkinter import *
import threading
import asyncio
import socket_service
# Theme
import theme

# Views
from views.intro import Intro

def set_view(view): 
	pass

def gui_thread():

	root = Tk()
	root.geometry("960x540")
	root.title("Night Chess: Local Multiplayer")
	root.resizable(False, False)
	root.configure(background=theme.background_primary)
	
	window = Intro(root, set_view)
	root.mainloop()

def network_thread():
	asyncio.run(socket_service.start())

t1 = threading.Thread(target=gui_thread)
t2 = threading.Thread(target=network_thread)

t1.start()
t2.start()

t1.join()
t2.join()

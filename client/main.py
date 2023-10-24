from tkinter import *

# Theme
import theme

# Views
from views.intro import Intro

root = Tk()
root.geometry("960x540")
root.title("Night Chess: Local Multiplayer")
root.resizable(False, False)
root.configure(background=theme.background_primary)

def set_view(view): 
	pass

window = Intro(root, set_view)

root.mainloop()
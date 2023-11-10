from tkinter import PhotoImage
from utils import paths

class Piece:
    def __init__(self, x, y, image, color):
        self.x = x
        self.y = y
        self.image = PhotoImage(file = paths.get_full_path(image))
        self.color = color

    def get_moves(self, data):
        pass

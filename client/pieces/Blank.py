from pieces.Piece import Piece

class Blank(Piece):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/blank.png", "w")


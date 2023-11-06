from pieces.Piece import Piece

class Rook(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_r.png", color)
        else:
            super().__init__(x, y, "assets/b_r.png", color)

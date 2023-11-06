from pieces.Piece import Piece

class Bishop(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_b.png", color)
        else:
            super().__init__(x, y, "assets/b_b.png", color)

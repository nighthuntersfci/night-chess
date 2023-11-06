from pieces.Piece import Piece

class Knight(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_n.png", color)
        else:
            super().__init__(x, y, "assets/b_n.png", color)

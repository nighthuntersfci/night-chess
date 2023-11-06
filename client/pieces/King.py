from pieces.Piece import Piece

class King(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_k.png", color)
        else:
            super().__init__(x, y, "assets/b_k.png", color)

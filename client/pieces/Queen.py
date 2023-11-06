from pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_q.png", color)
        else:
            super().__init__(x, y, "assets/b_q.png", color)

from pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_p.png", color)
        else:
            super().__init__(x, y, "assets/b_p.png", color)
    def get_moves(self, data):
        moves = []
        if self.color == "W":
            moves.append([1, 0])
            if self.x == 1:
                moves.append([2, 0])
        else:
            moves.append([-1, 0])
            if self.x == 6:
                moves.append([-2, 0])
        return moves

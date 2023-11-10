from pieces.Piece import Piece
from pieces.Blank import Blank

class Rook(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_r.png", color)
        else:
            super().__init__(x, y, "assets/b_r.png", color)

    def get_moves(self, data):
        moves = []
        
        for i in range(1, 9):
            if 0 <= self.x + i <= 7:
                if isinstance(data[self.x + i][self.y], Blank):
                    moves.append([i, 0]) 
                else:
                    break
            else: 
                break
        for i in range(1, 9):
            if 0 <= self.x - 1 <= 7:
                if isinstance(data[self.x - i][self.y], Blank):
                    moves.append([-i, 0])
                else:
                    break
            else:
                break
        for i in range(1, 9):
            if 0 <= self.y + i <= 7:
                if isinstance(data[self.x][self.y + i], Blank):
                    moves.append([0, i])
                else:
                    break
            else:
                break
        for i in range(1, 9):
            if 0 <= self.y - 1 <= 7:
                if isinstance(data[self.x][self.y - i], Blank):
                    moves.append([0, -i])
                else:
                    break
            else:
                break
        return moves

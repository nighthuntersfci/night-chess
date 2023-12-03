from pieces.Piece import Piece
from pieces.Blank import Blank
from utils.pieces import is_in_danger

class King(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_k.png", color)
        else:
            super().__init__(x, y, "assets/b_k.png", color)
    def get_moves(self, data):
        moves = []
        possible_moves = [(1,1),(-1,-1),(-1,1),(1,-1),(0,1),(0,-1),(1,0),(-1,0)]
        for i in possible_moves:
            if 0 <= self.x + i[0] <= 7 and 0 <= self.y + i[1] <= 7:
                if self.color != data[self.x + i[0]][self.y + i[1]].color:
                    data_snapshot = data
                    data_snapshot[self.x][self.y] = Blank(self.x, self.y, self.color)
                    if not is_in_danger(self.x + i[0], self.y + i[1], self.color, data_snapshot): 
                        moves.append(i)
        return moves

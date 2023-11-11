from pieces.Piece import Piece
from pieces.Blank import Blank
class Bishop(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_b.png", color)
        else:
            super().__init__(x, y, "assets/b_b.png", color)
    def get_moves(self, data):
        moves = []
        for d in range(1, 8):
            if d != 0:  
                if 0 <= self.x +d  <=7 and 0 <= self.y +d  <= 7:
                    if isinstance(data[self.x+ d][self.y + d ], Blank):
                        moves.append([d,d])
                    else:
                        break
                else: 
                    break
        for d in range(1, 8):
            if d != 0:
                if 0 <= self.x -d  <=7 and 0 <= self.y -d  <= 7:
                    if isinstance(data[self.x -d ][self.y -d ], Blank):
                        moves.append([-d,-d])
                    else:
                        break
                else:
                    break
        for d in range (1, 8):
            if d != 0: 
                if 0 <= self.x +d  <=7 and 0 <= self.y -d  <= 7:
                    if isinstance(data[self.x + d][self.y - d], Blank):
                        moves.append([d,-d])
                    else:
                        break
                else:
                    break
        for d in range (1, 8):
            if d != 0:
                if 0 <= self.x -d  <=7 and 0 <= self.y +d  <= 7:
                    if isinstance(data[self.x -d ][self.y + d], Blank):
                        moves.append([-d,d])
                    else:
                        break
                else:
                    break


        return moves
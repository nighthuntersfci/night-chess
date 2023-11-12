from pieces.Piece import Piece
from pieces.Blank import Blank
class Knight(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_n.png", color)
        else:
            super().__init__(x, y, "assets/b_n.png", color)
   
    def get_moves(self, data):
        moves = []
        for dx in [1,-1, 2, -2]:
            for dy in [1,2,-1,-2]:
                if abs(dx) != abs(dy):
                    new_x = self.x +dx
                    new_y = self.y +dy
                    if 0 <= new_x <=7 and 0<=new_y<=7:
                        if isinstance(data[new_x][new_y] , Blank):
                            moves.append([dx,dy])
                        else:
                            if data[new_x][new_y].color != self.color:
                                moves.append([dx,dy])
                            else:
                                break
          
        return moves

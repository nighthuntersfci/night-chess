from pieces.Piece import Piece

class Knight(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_n.png", color)
        else:
            super().__init__(x, y, "assets/b_n.png", color)
   
    def get_moves(self, data):
        moves = []
            
        for dx in [1,2,-1,-1]:
            for dy in [1,2,-1,-2]:
                if abs(dx) != abs(dy):
                    new_x = self.x +dx
                    new_y = self.y +dy
                    if 0 <= new_x <=7 and 0<=new_y<=7:
                        moves.append([dx,dy])
          
        return moves

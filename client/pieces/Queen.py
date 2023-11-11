from pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_q.png", color)
        else:
            super().__init__(x, y, "assets/b_q.png", color)
    def get_moves(self, data):
        moves = []
            
        for d in range(-7,8):
            if d != 0:  
                if 0 <= self.x +d  <=7 and 0 <= self.y +d  <= 7:
                    moves.append([d,d])
                if 0 <= self.x -d  <=7 and 0 <= self.y -d  <= 7:
                    moves.append([-d,-d])
                if 0 <= self.x +d  <=7 and 0 <= self.y -d  <= 7:
                    moves.append([d,-d])
                if 0 <= self.x -d  <=7 and 0 <= self.y +d  <= 7:
                    moves.append([-d,d])
        for i in range(1, 8):
            if 0 <= self.x + i <= 7:
                    moves.append([i, 0]) 
                
        for i in range(1, 8):
            if 0 <= self.x - i <= 7:
                    moves.append([-i, 0])
              
        for i in range(1, 8):
            if 0 <= self.y + i <= 7:
                    moves.append([0, i])
               
        for i in range(1, 8):
            if 0 <= self.y - i <= 7:
                    moves.append([0, -i])
                
        return moves
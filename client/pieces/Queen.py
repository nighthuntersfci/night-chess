from pieces.Piece import Piece
from pieces.Blank import Blank
class Queen(Piece):
    def __init__(self, x, y, color):
        if color == "W":
            super().__init__(x, y, "assets/w_q.png", color)
        else:
            super().__init__(x, y, "assets/b_q.png", color)
    def get_moves(self, data):
        moves = []

        for d in range(1, 8):
            if d != 0:  
                if 0 <= self.x +d  <=7 and 0 <= self.y +d  <= 7:
                    if isinstance(data[self.x+ d][self.y + d ], Blank):
                        moves.append([d,d])
                    else:
                        if data[self.x + d][self.y + d].color != self.color:
                            moves.append([d,d])
                        break
                else: 
                    break
        for d in range(1, 8):
            if d != 0:
                if 0 <= self.x -d  <=7 and 0 <= self.y -d  <= 7:
                    if isinstance(data[self.x -d ][self.y -d ], Blank):
                        moves.append([-d,-d])
                    else:
                        if data[self.x - d][self.y - d].color != self.color:
                            moves.append([-d,-d])
                        break
                else:
                    break
        for d in range (1, 8):
            if d != 0: 
                if 0 <= self.x +d  <=7 and 0 <= self.y -d  <= 7:
                    if isinstance(data[self.x + d][self.y - d], Blank):
                        moves.append([d,-d])
                    else:
                        if data[self.x + d][self.y - d].color != self.color:
                            moves.append([d,-d])
                        break
                else:
                    break
        for d in range (1, 8):
            if d != 0:
                if 0 <= self.x -d  <=7 and 0 <= self.y +d  <= 7:
                    if isinstance(data[self.x -d ][self.y + d], Blank):
                        moves.append([-d,d])
                    else:
                        if data[self.x - d][self.y + d].color != self.color:
                            moves.append([-d,d])
                        break
                else:
                    break
    
        
        # Straight Movement
        for i in range(1, 9):
            if 0 <= self.x + i <= 7:
                if isinstance(data[self.x + i][self.y], Blank):
                    moves.append([i, 0]) 
                else:
                    if data[self.x + i][self.y].color != self.color:
                        moves.append([i,0])
                    break
            else: 
                break
        for i in range(1, 9):
            if 0 <= self.x - i <= 7:
                if isinstance(data[self.x - i][self.y], Blank):
                    moves.append([-i, 0])
                else:
                    if data[self.x - i][self.y].color != self.color:
                        moves.append([-i,0])
                    break
            else:
                break
        for i in range(1, 9):
            if 0 <= self.y + i <= 7:
                if isinstance(data[self.x][self.y + i], Blank):
                    moves.append([0, i])
                else:
                    if data[self.x][self.y+i].color != self.color:
                        moves.append([0,i])
                    break
            else:
                break
        for i in range(1, 9):
            if 0 <= self.y - i <= 7:
                if isinstance(data[self.x][self.y - i], Blank):
                    moves.append([0, -i])
                else:
                    if data[self.x][self.y-i].color != self.color:
                        moves.append([0,-i])
                    break
            else:
                break
                
        return moves
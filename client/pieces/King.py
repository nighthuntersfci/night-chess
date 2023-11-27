from pieces.Piece import Piece
from pieces.Queen import Queen
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Blank import Blank

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
                    
                    add = True

                    # Vertical Movement
                    for j in range(0,7):
                        if 0 <= self.x + i[0] + j <= 7:
                            if (isinstance(data[self.x + i[0] + j][self.y + i[1]], Queen) or isinstance(data[self.x + i[0] + j][self.y + i[1]], Rook)) and self.color != data[self.x + i[0] + j][self.y + i[1]].color:  
                                add = False
                                break
                            elif not isinstance(data[self.x + i[0] + j][self.y + i[1]], Blank):
                                break
                        
                    if add == True:
                        for j in range(0, 7):
                            if 0 <= (self.x + i[0]) - j <= 7:
                                if (isinstance(data[(self.x + i[0]) - j][self.y + i[1]], Queen) or isinstance(data[(self.x + i[0]) - j][self.y + i[1]], Rook)) and self.color != data[(self.x + i[0]) - j][self.y + i[1]].color:  
                                    add = False
                                    break
                                elif not isinstance(data[self.x + i[0] - j][self.y + i[1]], Blank):
                                    break
                    
                    # Horizontal Movement
                    if add == True:
                        for j in range(0,7):
                            if 0 <= self.y + i[1] + j <= 7:
                                if (isinstance(data[self.x + i[0]][self.y + i[1] + j], Queen) or isinstance(data[self.x + i[0]][(self.y + i[1]) + j], Rook)) and self.color != data[self.x + i[0]][(self.y + i[1]) + j].color:  
                                    add = False
                                    break
                                elif not isinstance(data[self.x + i[0]][self.y + i[1] + j], Blank):
                                    break
                        
                    if add == True:
                        for j in range(0, 7):
                            if 0 <= (self.y + i[1]) - j <= 7:
                                if (isinstance(data[self.x + i[0]][(self.y + i[1]) - j], Queen) or isinstance(data[self.x + i[0]][(self.y + i[1]) - j], Rook)) and self.color !=data[self.x + i[0]][(self.y + i[1]) - j].color:  
                                    add = False
                                    break
                                elif not isinstance(data[self.x + i[0]][self.y + i[1] - j], Blank):
                                    break
                    
                    # Diagonal Right-side 
                    if add == True:
                        for j in range(0,7):
                            if 0 <= self.y + i[1] + j <= 7 and 0 <= self.x + i[0] + j <= 7:
                                if (isinstance(data[self.x + i[0] + j][self.y + i[1] + j], Queen) or isinstance(data[self.x + i[0] + j][(self.y + i[1]) + j], Bishop)) and self.color !=data[self.x + i[0] + j][(self.y + i[1]) + j].color:  
                                    add = False
                                    break
                                elif not isinstance(data[self.x + i[0] + j][self.y + i[1] + j], Blank):
                                    break
                        
                    if add == True:
                        for j in range(0, 7):
                            if 0 <= (self.y + i[1]) - j <= 7 and 0 <= (self.x + i[0]) + j <= 7:
                                if (isinstance(data[self.x + i[0] + j][(self.y + i[1]) - j], Queen) or isinstance(data[self.x + i[0] + j][(self.y + i[1]) - j], Bishop)) and self.color !=data[self.x + i[0] + j][(self.y + i[1]) - j].color:  
                                    add = False
                                    break    
                                elif not isinstance(data[self.x + i[0] + j][self.y + i[1] - j], Blank):
                                    break           

                    # Diagonal Left Side
                    if add == True:
                        for j in range(0,7):
                            if 0 <= self.y + i[1] - j <= 7 and 0 <= self.x + i[0] - j <= 7:
                                if (isinstance(data[self.x + i[0] - j][self.y + i[1] - j], Queen) or isinstance(data[self.x + i[0] - j][(self.y + i[1]) - j], Bishop)) and self.color !=data[self.x + i[0] - j][(self.y + i[1]) - j].color:  
                                    add = False
                                    break
                                elif not isinstance(data[self.x + i[0] - j][self.y + i[1] - j], Blank):
                                    break
                        
                    if add == True:
                        for j in range(0, 7):
                            if 0 <= (self.y + i[1]) + j <= 7 and 0 <= (self.x + i[0]) - j <= 7:
                                if (isinstance(data[self.x + i[0] - j][(self.y + i[1]) + j], Queen) or isinstance(data[self.x + i[0] - j][(self.y + i[1]) + j], Bishop)) and self.color !=data[self.x + i[0] - j][(self.y + i[1]) + j].color:  
                                    add = False
                                    break   
                                elif not isinstance(data[self.x + i[0] - j][self.y + i[1] + j], Blank):
                                    break

                    # Knight movement 
                    if add == True:
                        for dx in [1, -1, 2, -2]:
                            break_outer = False
                            for dy in [1, -1, 2, -2]:
                                if abs(dx) != abs(dy):
                                    if 0 <= self.x + i[0] + dx <= 7 and 0 <= self.y + i[1] + dy <= 7:
                                        if (isinstance(data[self.x + i[0] + dx][self.y + i[1] + dy], Knight)) and self.color !=data[self.x + i[0] + dx][self.y + i[1] + dy].color: 
                                            add = False
                                            break_outer = True
                                            break
                            if break_outer:
                                break
                    
                    if add == True:
                        if self.color == "W":
                            if (isinstance(data[self.x + i[0] + 1][self.y + i[1] + 1], Pawn) or isinstance(data[self.x + i[0] + 1][self.y + i[1] - 1], Pawn)) and (data[self.x + i[0] + 1][self.y + i[1] + 1].color == "B" or data[self.x + i[0] + 1][self.y + i[1] - 1].color == "B"):
                                add = False
                        else:
                            if (isinstance(data[self.x + i[0] - 1][self.y + i[1] + 1], Pawn) or isinstance(data[self.x + i[0] - 1][self.y + i[1] - 1], Pawn)) and (data[self.x + i[0] - 1][self.y + i[1] + 1].color == "B" or data[self.x + i[0] - 1][self.y + i[1] - 1].color == "B"):
                                add = False
                    if add: 
                        moves.append(i)
        return moves

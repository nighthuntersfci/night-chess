from pieces.Queen import Queen
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Blank import Blank

def is_in_danger(x, y, color, data):
	not_in_danger = True

	# Vertical Movement
	for j in range(0,7):
		if 0 <= x + j <= 7:
			if (isinstance(data[x + j][y], Queen) or isinstance(data[x + j][y], Rook)) and color != data[x + j][y].color:  
				not_in_danger = False
				break
			elif not isinstance(data[x + j][y], Blank):
				break
		
	if not_in_danger == True:
		for j in range(0, 7):
			if 0 <= x - j <= 7:
				if (isinstance(data[x - j][y], Queen) or isinstance(data[x - j][y], Rook)) and color != data[x - j][y].color:  
					not_in_danger = False
					break
				elif not isinstance(data[x - j][y], Blank):
					break
	
	# Horizontal Movement
	if not_in_danger == True:
		for j in range(0,7):
			if 0 <= y + j <= 7:
				if (isinstance(data[x][y + j], Queen) or isinstance(data[x][y + j], Rook)) and color != data[x][y + j].color:  
					not_in_danger = False
					break
				elif not isinstance(data[x][y + j], Blank):
					break
		
	if not_in_danger == True:
		for j in range(0, 7):
			if 0 <= y - j <= 7:
				if (isinstance(data[x][y - j], Queen) or isinstance(data[x][y - j], Rook)) and color !=data[x][y - j].color:  
					not_in_danger = False
					break
				elif not isinstance(data[x][y - j], Blank):
					break
	
	# Diagonal Right-side 
	if not_in_danger == True:
		for j in range(0,7):
			if 0 <= y + j <= 7 and 0 <= x + j <= 7:
				if (isinstance(data[x + j][y + j], Queen) or isinstance(data[x + j][y + j], Bishop)) and color !=data[x + j][y + j].color:  
					not_in_danger = False
					break
				elif not isinstance(data[x + j][y + j], Blank):
					break
		
	if not_in_danger == True:
		for j in range(0, 7):
			if 0 <= y - j <= 7 and 0 <= x + j <= 7:
				if (isinstance(data[x + j][y - j], Queen) or isinstance(data[x + j][y - j], Bishop)) and color !=data[x + j][y - j].color:  
					not_in_danger = False
					break    
				elif not isinstance(data[x + j][y - j], Blank):
					break           

	# Diagonal Left Side
	if not_in_danger == True:
		for j in range(0,7):
			if 0 <= y - j <= 7 and 0 <= x - j <= 7:
				if (isinstance(data[x - j][y - j], Queen) or isinstance(data[x - j][y - j], Bishop)) and color !=data[x - j][y - j].color:  
					not_in_danger = False
					break
				elif not isinstance(data[x - j][y - j], Blank):
					break
		
	if not_in_danger == True:
		for j in range(0, 7):
			if 0 <= y + j <= 7 and 0 <= x - j <= 7:
				if (isinstance(data[x - j][y + j], Queen) or isinstance(data[x - j][y + j], Bishop)) and color !=data[x - j][y + j].color:  
					not_in_danger = False
					break   
				elif not isinstance(data[x - j][y + j], Blank):
					break

	# Knight movement 
	if not_in_danger == True:
		for dx in [1, -1, 2, -2]:
			break_outer = False
			for dy in [1, -1, 2, -2]:
				if abs(dx) != abs(dy):
					if 0 <= x + dx <= 7 and 0 <= y + dy <= 7:
						if (isinstance(data[x + dx][y + dy], Knight)) and color !=data[x + dx][y + dy].color: 
							not_in_danger = False
							break_outer = True
							break
			if break_outer:
				break

	 
	if not_in_danger == True:
		if color == "W":
			if (isinstance(data[x + 1][y + 1], Pawn) or isinstance(data[x + 1][y - 1], Pawn)) and (data[x + 1][y + 1].color == "B" or data[x + 1][y - 1].color == "B"):
				not_in_danger = False
		else:
			if (isinstance(data[x - 1][y + 1], Pawn) or isinstance(data[x - 1][y - 1], Pawn)) and (data[x - 1][y + 1].color == "B" or data[x - 1][y - 1].color == "B"):
				not_in_danger = False

	return not not_in_danger

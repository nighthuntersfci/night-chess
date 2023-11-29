from pieces.Queen import Queen
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Blank import Blank

def is_in_danger(x, y, color, data):
	not_in_danger = True

	# Vertical Movement
	for k in range(1, 7):
		if 0 <= x + k <= 7:
			if (isinstance(data[x + k][y], Queen) or isinstance(data[x + k][y], Rook)) and color != data[x + k][y].color:  
				not_in_danger = False
				break
			elif not isinstance(data[x + k][y], Blank):
				break
		
	if not_in_danger == True:
		for k in range(1, 7):
			if 0 <= x - k <= 7:
				if (isinstance(data[x - k][y], Queen) or isinstance(data[x - k][y], Rook)) and color != data[x - k][y].color:  
					not_in_danger = False
					break
				elif not isinstance(data[x - k][y], Blank):
					break
	
	# Horizontal Movement
	if not_in_danger == True:
		for k in range(0,7):
			if 0 <= y + k <= 7:
				if (isinstance(data[x][y + k], Queen) or isinstance(data[x][y + k], Rook)) and color != data[x][y + k].color:  
					not_in_danger = False
					break
				elif not isinstance(data[x][y + k], Blank):
					break
		
	if not_in_danger == True:
		for k in range(1, 7):
			if 0 <= y - k <= 7:
				if (isinstance(data[x][y - k], Queen) or isinstance(data[x][y - k], Rook)) and color !=data[x][y - k].color:  
					not_in_danger = False
					break
				elif not isinstance(data[x][y - k], Blank):
					break
	
	# Diagonal
	if not_in_danger == True:
		for k in range(0,7):
			if 0 <= y + k <= 7 and 0 <= x + k <= 7:
				if (isinstance(data[x + k][y + k], Queen) or isinstance(data[x + k][y + k], Bishop)) and color !=data[x + k][y + k].color:  
					not_in_danger = False
					break
				elif not isinstance(data[x + k][y + k], Blank):
					break
		
	if not_in_danger == True:
		for k in range(1, 7):
			if 0 <= y - k <= 7 and 0 <= x + k <= 7:
				if (isinstance(data[x + k][y - k], Queen) or isinstance(data[x + k][y - k], Bishop)) and color !=data[x + k][y - k].color:  
					not_in_danger = False
					break    
				elif not isinstance(data[x + k][y - k], Blank):
					break           

	if not_in_danger == True:
		for k in range(0,7):
			if 0 <= y - k <= 7 and 0 <= x - k <= 7:
				if (isinstance(data[x - k][y - k], Queen) or isinstance(data[x - k][y - k], Bishop)) and color !=data[x - k][y - k].color:  
					not_in_danger = False
					break
				elif not isinstance(data[x - k][y - k], Blank):
					break
		
	if not_in_danger == True:
		for k in range(1, 7):
			if 0 <= y + k <= 7 and 0 <= x - k <= 7:
				if (isinstance(data[x - k][y + k], Queen) or isinstance(data[x - k][y + k], Bishop)) and color !=data[x - k][y + k].color:  
					not_in_danger = False
					break   
				elif not isinstance(data[x - k][y + k], Blank):
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

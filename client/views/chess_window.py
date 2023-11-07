from tkinter import *
import data
import theme

# Pieces 
from pieces.Blank import Blank
from pieces.Pawn import Pawn
from pieces.Rook import Rook
from pieces.Knight import Knight
from pieces.Bishop import Bishop
from pieces.King import King
from pieces.Queen import Queen

class ChessWindow(Frame):
    def __init__(self, parent, is_black = False, opponent_name = "Empty"):
        
        super().__init__(parent, background=theme.background_primary)
        self.pack(fill=BOTH, expand=True)
        self.grid_columnconfigure(0, weight=1)       
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        image = PhotoImage(width=60, height=60)

        self.is_black = is_black
        self.game_pieces = [[], [], [], [], [], [], [], []]


        for i in range(8):
            for j in range(8):
                self.game_pieces[i].append(Blank(i, j))

        for i in range(8):
            self.game_pieces[1][i] = Pawn(1, i, "W")
            self.game_pieces[6][i] = Pawn(6, i, "B")

        self.game_pieces[0][0] = Rook(0, 0, "W") 
        self.game_pieces[0][7] = Rook(0, 7, "W") 
        self.game_pieces[7][0] = Rook(7, 0, "B") 
        self.game_pieces[7][7] = Rook(7, 7, "B") 

        self.game_pieces[0][1] = Knight(0, 1, "W") 
        self.game_pieces[0][6] = Knight(0, 6, "W") 
        self.game_pieces[7][1] = Knight(7, 1, "B") 
        self.game_pieces[7][6] = Knight(7, 6, "B") 

        self.game_pieces[0][2] = Bishop(0, 1, "W") 
        self.game_pieces[0][5] = Bishop(0, 5, "W") 
        self.game_pieces[7][2] = Bishop(7, 1, "B") 
        self.game_pieces[7][5] = Bishop(7, 5, "B") 

        self.game_pieces[0][4] = King(0, 4, "W")
        self.game_pieces[7][4] = King(7, 4, "B")

        self.game_pieces[0][3] = Queen(0, 3, "W")
        self.game_pieces[7][3] = Queen(7, 3, "B")

        self.parent = parent
        white = '#ffffff'
        black = theme.color_secondary

        if is_black:
            white_name = opponent_name
            black_name = data.name
        else:
            white_name = data.name
            black_name = opponent_name

        # =============================================
        # left side (White)
        left_side = Frame(self, background=theme.background_primary)
        left_side.grid(row=1, column=0)

        white_name_frame = Frame(left_side, bg=white)
        white_name_frame.grid()

        lab1 = Label(white_name_frame , text='White' , font=('arial' , 20 , 'bold') , fg='black' ,bg=white)
        lab1.grid(pady=(10, 0), padx=10)

        self.white_label = Label(white_name_frame , text=white_name , font=('arial' , 15 , 'italic') , fg='black' ,bg=white)
        self.white_label.grid()
        
        # ==============================================
        # right side (black)
        right_side =Frame(self, background=theme.background_primary)
        right_side.grid(row=1, column=2)

        black_name_frame = Frame(right_side, bg=black)
        black_name_frame.grid()

        lab1 = Label(black_name_frame , text='black' , font=('arial' , 20 , 'bold') , fg='white' ,bg=black)
        lab1.grid(pady=(10, 0), padx=10)

        self.black_label = Label(black_name_frame , text=black_name , font=('arial' , 15 , 'italic') , fg='white' ,bg=black)
        self.black_label.grid()
        # =============================================
        # chess board
        board_frame = Frame(self, bg=theme.color_secondary, border=0)
        board_frame.grid(row=1, column=1)
        for i in range(8):
            for j in range(8):
                if is_black == False:
                    x = Button(board_frame, image=self.game_pieces[7 - i][j].image, width=60, height=60, border=0)
                else:
                    x = Button(board_frame, image=self.game_pieces[i][7 - j].image, width=60, height=60, border=0)
                x.grid(row=i, column=j)
                if (i + j) % 2 == 0:
                    x.configure(bg=white, activebackground=white)
                else:
                    x.configure(bg=black, activebackground=black)
        # =============================================
        
        
    def update_opponent_name(self, name):
        if self.is_black:
            self.white_label.configure(text=name)
        else:
            self.black_label.configure(text=name)

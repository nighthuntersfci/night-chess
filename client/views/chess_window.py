from msilib.schema import SelfReg
from tkinter import *
import data
import theme
# 960x580"
# 210+(540x580)+210
class ChessWindow(Frame):
    def __init__(self, parent, black = False):
        
        super().__init__(parent, background='#4a4643', width=1000 , height=800)
        
        self.pack(fill=BOTH, expand=True)
        self.parent = parent
        white = '#ffd39c'
        black = '#5d5a50'
        white_name = "Ahmed"
        black_name = "Salah"
        # =============================================
        # left side (White)
        left_side = Frame(self , width=200 , height=540 , bg='#4a4643')
        left_side.place(x=1 , y=1)

        white_name_frame = Frame(left_side, bg=white, width=170 , height=80)
        white_name_frame.place(x=10, y=20)

        lab1 = Label(white_name_frame , text='White' , font=('arial' , 20 , 'bold') , fg='black' ,bg=white)
        lab1.place(x=5 , y=5)

        lab2 = Label(white_name_frame , text=white_name , font=('arial' , 15 , 'italic') , fg='black' ,bg=white)
        lab2.place(x=10 , y=45)
        
        # ==============================================
        # right side (black)
        right_side =Frame(self , width=210 ,height=540 , bg='#4a4643')
        right_side.place(x=750 , y=1)

        black_name_frame = Frame(right_side, bg=black, width=170 , height=80)
        black_name_frame.place(x=10,y=20)

        lab1 = Label(black_name_frame , text='black' , font=('arial' , 20 , 'bold') , fg='black' ,bg=black)
        lab1.place(x=5 , y=5)

        lab2 = Label(black_name_frame , text=black_name , font=('arial' , 15 , 'italic') , fg='black' ,bg=black)
        lab2.place(x=10 , y=45)
        # =============================================
        # chess board
        board_frame = Frame(self ,bg='#dabd96' ,width=540 ,height=540 , border=4)
        board_frame.grid(padx=210)
        l=[]
        for i in range(8):
            for j in range(8):
                x = Button(board_frame, width=8, height=4)
                x.grid(row=i, column=j)
                if (i + j) % 2 == 0:
                    x.configure(bg=white)
                else:
                    x.configure(bg=black)
                l.append(x)
        # =============================================
        
        
        
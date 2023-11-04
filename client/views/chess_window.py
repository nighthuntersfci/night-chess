from tkinter import *
import data
import theme

class ChessWindow(Frame):
    def __init__(self, parent, black = False):
        
        super().__init__(parent, background=theme.background_primary)
        self.pack(fill=BOTH, expand=True)
		
        self.parent = parent
        white = '#ffffff'
        black = theme.color_primary
        white_name = "Ahmed"
        black_name = "Salah"
        # =============================================
        # left side (White)
        left_side = Frame(self , width=200 , height=540 ,  background=theme.background_primary)
        left_side.place(x=1 , y=1)

        white_name_frame = Frame(left_side, bg=white, width=170 , height=80)
        white_name_frame.place(x=10, y=20)

        lab1 = Label(white_name_frame , text='White' , font=('arial' , 20 , 'bold') , fg='black' ,bg=white)
        lab1.place(x=5 , y=5)

        lab2 = Label(white_name_frame , text=white_name , font=('arial' , 15 , 'italic') , fg='black' ,bg=white)
        lab2.place(x=5 , y=45)
        
        # ==============================================
        # right side (black)
        right_side =Frame(self , width=210 ,height=540, background=theme.background_primary)
        right_side.place(x=750 , y=1)

        black_name_frame = Frame(right_side, bg=black, width=170 , height=80)
        black_name_frame.place(x=10,y=20)

        lab1 = Label(black_name_frame , text='black' , font=('arial' , 20 , 'bold') , fg='white' ,bg=black)
        lab1.place(x=5 , y=5)

        lab2 = Label(black_name_frame , text=black_name , font=('arial' , 15 , 'italic') , fg='white' ,bg=black)
        lab2.place(x=5 , y=45)
        # =============================================
        # chess board
        board_frame = Frame(self ,bg=theme.color_secondary,width=540 ,height=540 , border=5)
        board_frame.grid(padx=210)
        l=[]
        for i in range(8):
            for j in range(8):
                x = Button(board_frame, width=8, height=4, border=0)
                x.grid(row=i, column=j)
                if (i + j) % 2 == 0:
                    x.configure(bg=white, activebackground=white)
                else:
                    x.configure(bg=black, activebackground=black)
                l.append(x)
        # =============================================
        
        
        
from tkinter import *
import data
import theme



class ChessWindow(Frame):
    def __init__(self, parent, black = False):
        
        super().__init__(parent, background=theme.background_primary)
        self.pack(fill=BOTH, expand=True)
        self.grid_columnconfigure(0, weight=1)       
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        image = PhotoImage(width=1, height=1)

        self.parent = parent
        white = '#ffffff'
        black = '#555555'
        white_name = "Ahmed"
        black_name = "Salah"
        # =============================================
        # left side (White)
        left_side = Frame(self, background=theme.background_primary)
        left_side.grid(row=1, column=0)

        white_name_frame = Frame(left_side, bg=white, width=170 , height=80)
        white_name_frame.grid()

        lab1 = Label(white_name_frame , text='White' , font=('arial' , 20 , 'bold') , fg='black' ,bg=white)
        lab1.grid()

        lab2 = Label(white_name_frame , text=white_name , font=('arial' , 15 , 'italic') , fg='black' ,bg=white)
        lab2.grid()
        
        # ==============================================
        # right side (black)
        right_side =Frame(self, background=theme.background_primary)
        right_side.grid(row=1, column=2)

        black_name_frame = Frame(right_side, bg=black, width=170 , height=80)
        black_name_frame.grid()

        lab1 = Label(black_name_frame , text='black' , font=('arial' , 20 , 'bold') , fg='white' ,bg=black)
        lab1.grid()

        lab2 = Label(black_name_frame , text=black_name , font=('arial' , 15 , 'italic') , fg='white' ,bg=black)
        lab2.grid()
        # =============================================
        # chess board
        board_frame = Frame(self, bg=theme.color_secondary, border=0)
        board_frame.grid(row=1, column=1)
        l=[]
        for i in range(8):
            for j in range(8):
                x = Button(board_frame, image=image, width=60, height=60, border=0)
                x.grid(row=i, column=j)
                if (i + j) % 2 == 0:
                    x.configure(bg=white, activebackground=white)
                else:
                    x.configure(bg=black, activebackground=black)
                l.append(x)
        # =============================================
        
        
        

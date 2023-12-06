from tkinter import *
import data
import theme
import socket_service
from utils.pieces import *
from utils.paths import *
from playsound import playsound

# Pieces
from pieces.Blank import Blank
from pieces.Pawn import Pawn
from pieces.Rook import Rook
from pieces.Knight import Knight
from pieces.Bishop import Bishop
from pieces.King import King
from pieces.Queen import Queen

white = "#ffffff"
black = theme.color_secondary


class ChessWindow(Frame):
    def __init__(self, parent, is_black=False, opponent_name="Empty"):
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
        self.buttons = [[], [], [], [], [], [], [], []]
        self.about_to_move = False
        self.about_to_move_piece = None
        self.is_turn = False
        self.checked = False

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

        self.game_pieces[0][2] = Bishop(0, 2, "W")
        self.game_pieces[0][5] = Bishop(0, 5, "W")
        self.game_pieces[7][2] = Bishop(7, 2, "B")
        self.game_pieces[7][5] = Bishop(7, 5, "B")

        self.game_pieces[0][4] = King(0, 4, "W")
        self.game_pieces[7][4] = King(7, 4, "B")

        self.game_pieces[0][3] = Queen(0, 3, "W")
        self.game_pieces[7][3] = Queen(7, 3, "B")

        self.parent = parent

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

        lab1 = Label(
            white_name_frame,
            text="White",
            font=("arial", 20, "bold"),
            fg="black",
            bg=white,
        )
        lab1.grid(pady=(10, 0), padx=10)

        self.white_label = Label(
            white_name_frame,
            text=white_name,
            font=("arial", 15, "italic"),
            fg="black",
            bg=white,
        )
        self.white_label.grid()

        # ==============================================
        # right side (black)
        right_side = Frame(self, background=theme.background_primary)
        right_side.grid(row=1, column=2)

        black_name_frame = Frame(right_side, bg=black)
        black_name_frame.grid()

        lab1 = Label(
            black_name_frame,
            text="black",
            font=("arial", 20, "bold"),
            fg="white",
            bg=black,
        )
        lab1.grid(pady=(10, 0), padx=10)

        self.black_label = Label(
            black_name_frame,
            text=black_name,
            font=("arial", 15, "italic"),
            fg="white",
            bg=black,
        )
        self.black_label.grid()

        # =============================================
        # chess board
        board_frame = Frame(self, bg=theme.color_secondary, border=0)
        board_frame.grid(row=1, column=1)
        for i in range(8):
            for j in range(8):
                if is_black == False:
                    x = Button(
                        board_frame,
                        image=self.game_pieces[7 - i][j].image,
                        width=60,
                        height=60,
                        border=0,
                    )
                    x.configure(command=lambda i=i, j=j: self.click(7 - i, j))
                else:
                    x = Button(
                        board_frame,
                        image=self.game_pieces[i][7 - j].image,
                        width=60,
                        height=60,
                        border=0,
                    )
                    x.configure(command=lambda i=i, j=j: self.click(i, 7 - j))

                x.grid(row=i, column=j)
                self.buttons[i].append(x)
                if (i + j) % 2 == 0:
                    x.configure(bg=white, activebackground=white)
                else:
                    x.configure(bg=black, activebackground=black)

    def recolor(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.buttons[i][j].configure(bg=white, activebackground=white)
                else:
                    self.buttons[i][j].configure(bg=black, activebackground=black)

    def render(self):
        for i in range(8):
            for j in range(8):
                if self.is_black:
                    self.buttons[i][j].configure(image=self.game_pieces[i][7 - j].image)
                else:
                    self.buttons[i][j].configure(image=self.game_pieces[7 - i][j].image)

    def click(self, x, y):
        piece = self.game_pieces[x][y]

        self.recolor()

        if self.is_turn:
            if not isinstance(piece, Blank):
                for i in piece.get_moves(self.game_pieces):
                    if (self.checked and isinstance(piece, King)) or (not self.checked):
                        if self.is_black and piece.color == "B":
                            if (i[0] + i[1]) % 2 == 0:
                                self.buttons[piece.x + i[0]][
                                    7 - piece.y - i[1]
                                ].configure(bg="gray", activebackground="silver")
                            else:
                                self.buttons[piece.x + i[0]][
                                    7 - piece.y - i[1]
                                ].configure(bg="darkgray", activebackground="silver")
                            self.about_to_move = True
                            self.about_to_move_piece = piece
                        elif not self.is_black and piece.color == "W":
                            if (i[0] + i[1]) % 2 == 0:
                                self.buttons[7 - piece.x - i[0]][
                                    piece.y + i[1]
                                ].configure(bg="gray", activebackground="silver")
                            else:
                                self.buttons[7 - piece.x - i[0]][
                                    piece.y + i[1]
                                ].configure(bg="darkgray", activebackground="silver")
                            self.about_to_move = True
                            self.about_to_move_piece = piece

            if self.about_to_move:
                for i in self.about_to_move_piece.get_moves(self.game_pieces):
                    if [x, y] == [
                        self.about_to_move_piece.x + i[0],
                        self.about_to_move_piece.y + i[1],
                    ]:
                        self.is_turn = False

                        self.game_pieces[self.about_to_move_piece.x][
                            self.about_to_move_piece.y
                        ] = Blank(
                            self.about_to_move_piece.x, self.about_to_move_piece.y
                        )
                        self.game_pieces[x][y] = self.about_to_move_piece
                        self.game_pieces[x][y].x = x
                        self.game_pieces[x][y].y = y

                        self.checked = False

                        self.render()

                        if (
                            isinstance(self.game_pieces[x][y], Pawn)
                            and x == 7
                            and self.game_pieces[x][y].color == "W"
                        ) or (
                            isinstance(self.game_pieces[x][y], Pawn)
                            and x == 0
                            and self.game_pieces[x][y].color == "B"
                        ):

                            def set_choice(choice, frame):
                                if choice == "Q":
                                    self.game_pieces[x][y] = Queen(
                                        x, y, self.game_pieces[x][y].color
                                    )
                                elif choice == "N":
                                    self.game_pieces[x][y] = Knight(
                                        x, y, self.game_pieces[x][y].color
                                    )
                                elif choice == "B":
                                    self.game_pieces[x][y] = Bishop(
                                        x, y, self.game_pieces[x][y].color
                                    )
                                elif choice == "R":
                                    self.game_pieces[x][y] = Rook(
                                        x, y, self.game_pieces[x][y].color
                                    )

                                frame.destroy()
                                self.after_movement()

                            promote_pawn(self, self.game_pieces[x][y].color, set_choice)
                        else:
                            self.after_movement()

    def get_piece_data(self):
        piece_data = [[], [], [], [], [], [], [], []]
        for i in range(8):
            for j in range(8):
                string = ""
                if isinstance(self.game_pieces[i][j], Pawn):
                    string = string + "p"
                elif isinstance(self.game_pieces[i][j], Rook):
                    string = string + "r"
                elif isinstance(self.game_pieces[i][j], Knight):
                    string = string + "n"
                elif isinstance(self.game_pieces[i][j], Bishop):
                    string = string + "b"
                elif isinstance(self.game_pieces[i][j], Queen):
                    string = string + "q"
                elif isinstance(self.game_pieces[i][j], King):
                    string = string + "k"
                elif isinstance(self.game_pieces[i][j], Blank):
                    string = "  "

                if self.game_pieces[i][j].color == "W":
                    string = string + "w"
                else:
                    string = string + "b"

                piece_data[i].append(string)

        return piece_data

    def update_board(self, data):
        self.is_turn = True
        for i in range(8):
            for j in range(8):
                if data[i][j][0] == "p":
                    self.game_pieces[i][j] = Pawn(i, j, data[i][j][1].upper())
                elif data[i][j][0] == "r":
                    self.game_pieces[i][j] = Rook(i, j, data[i][j][1].upper())
                elif data[i][j][0] == "n":
                    self.game_pieces[i][j] = Knight(i, j, data[i][j][1].upper())
                elif data[i][j][0] == "b":
                    self.game_pieces[i][j] = Bishop(i, j, data[i][j][1].upper())
                elif data[i][j][0] == "q":
                    self.game_pieces[i][j] = Queen(i, j, data[i][j][1].upper())
                elif data[i][j][0] == "k":
                    self.game_pieces[i][j] = King(i, j, data[i][j][1].upper())
                else:
                    self.game_pieces[i][j] = Blank(i, j)

        self.check_for_check()

        self.render()

    def update_opponent_name(self, name):
        self.is_turn = True
        if self.is_black:
            self.white_label.configure(text=name)
        else:
            self.black_label.configure(text=name)

    def check_for_check(self):
        for i in range(8):
            for j in range(8):
                if isinstance(self.game_pieces[i][j], King) and (
                    (self.is_black and self.game_pieces[i][j].color == "B")
                    or (not self.is_black and self.game_pieces[i][j].color == "W")
                ):
                    if is_in_danger(
                        self.game_pieces[i][j].x,
                        self.game_pieces[i][j].y,
                        self.game_pieces[i][j].color,
                        self.game_pieces,
                    ):
                        self.checked = True

                        check_for_end(i, j, self.game_pieces, False)

    def after_movement(self):
        self.about_to_move = False
        self.about_to_move_piece = None

        socket_service.sio.emit(
            "update_board",
            {"id": data.current_room, "data": self.get_piece_data()},
        )

        self.render()

        # Check if won
        for i in range(8):
            for j in range(8):
                if isinstance(self.game_pieces[i][j], King) and (
                    (self.is_black and self.game_pieces[i][j].color == "W")
                    or (not self.is_black and self.game_pieces[i][j].color == "B")
                ):
                    if is_in_danger(
                        self.game_pieces[i][j].x,
                        self.game_pieces[i][j].y,
                        self.game_pieces[i][j].color,
                        self.game_pieces,
                    ):
                        check_for_end(i, j, self.game_pieces, True)

        try:
            playsound(get_full_path("assets/move.wav"))
        except Exception as e:
            print("Error playing sound", e)

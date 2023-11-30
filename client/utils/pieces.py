from pieces.Queen import Queen
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Blank import Blank

from tkinter import *
import theme
from utils.paths import get_full_path


def is_in_danger(x, y, color, data):
    not_in_danger = True

    # Vertical Movement
    for k in range(1, 7):
        if 0 <= x + k <= 7:
            if (
                isinstance(data[x + k][y], Queen) or isinstance(data[x + k][y], Rook)
            ) and color != data[x + k][y].color:
                not_in_danger = False
                break
            elif not isinstance(data[x + k][y], Blank):
                break

    if not_in_danger == True:
        for k in range(1, 7):
            if 0 <= x - k <= 7:
                if (
                    isinstance(data[x - k][y], Queen)
                    or isinstance(data[x - k][y], Rook)
                ) and color != data[x - k][y].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x - k][y], Blank):
                    break

    # Horizontal Movement
    if not_in_danger == True:
        for k in range(1, 7):
            if 0 <= y + k <= 7:
                if (
                    isinstance(data[x][y + k], Queen)
                    or isinstance(data[x][y + k], Rook)
                ) and color != data[x][y + k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x][y + k], Blank):
                    break

    if not_in_danger == True:
        for k in range(1, 7):
            if 0 <= y - k <= 7:
                if (
                    isinstance(data[x][y - k], Queen)
                    or isinstance(data[x][y - k], Rook)
                ) and color != data[x][y - k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x][y - k], Blank):
                    break

    # Diagonal
    if not_in_danger == True:
        for k in range(1, 7):
            if 0 <= y + k <= 7 and 0 <= x + k <= 7:
                if (
                    isinstance(data[x + k][y + k], Queen)
                    or isinstance(data[x + k][y + k], Bishop)
                ) and color != data[x + k][y + k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x + k][y + k], Blank):
                    break

    if not_in_danger == True:
        for k in range(1, 7):
            if 0 <= y - k <= 7 and 0 <= x + k <= 7:
                if (
                    isinstance(data[x + k][y - k], Queen)
                    or isinstance(data[x + k][y - k], Bishop)
                ) and color != data[x + k][y - k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x + k][y - k], Blank):
                    break

    if not_in_danger == True:
        for k in range(1, 7):
            if 0 <= y - k <= 7 and 0 <= x - k <= 7:
                if (
                    isinstance(data[x - k][y - k], Queen)
                    or isinstance(data[x - k][y - k], Bishop)
                ) and color != data[x - k][y - k].color:
                    not_in_danger = False
                    break
                elif not isinstance(data[x - k][y - k], Blank):
                    break

    if not_in_danger == True:
        for k in range(1, 7):
            if 0 <= y + k <= 7 and 0 <= x - k <= 7:
                if (
                    isinstance(data[x - k][y + k], Queen)
                    or isinstance(data[x - k][y + k], Bishop)
                ) and color != data[x - k][y + k].color:
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
                        if (isinstance(data[x + dx][y + dy], Knight)) and color != data[
                            x + dx
                        ][y + dy].color:
                            not_in_danger = False
                            break_outer = True
                            break
            if break_outer:
                break

    if not_in_danger == True:
        if color == "W":
            if (
                isinstance(data[x + 1][y + 1], Pawn)
                or isinstance(data[x + 1][y - 1], Pawn)
            ) and (data[x + 1][y + 1].color == "B" or data[x + 1][y - 1].color == "B"):
                not_in_danger = False
        else:
            if (
                isinstance(data[x - 1][y + 1], Pawn)
                or isinstance(data[x - 1][y - 1], Pawn)
            ) and (data[x - 1][y + 1].color == "W" or data[x - 1][y - 1].color == "W"):
                not_in_danger = False

    return not not_in_danger


def check_for_end(i, j, data, won):
    if len(data[i][j].get_moves(data)) == 0:
        root = Tk()
        root.geometry("960x540")
        root.resizable(False, False)

        frame = Frame(root, background=theme.background_primary)
        frame.pack(fill=BOTH, expand=True)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(2, weight=1)

        if won == False:
            lb = Label(
                frame,
                text="You Lost",
                font=("Arial", 60),
                background=theme.background_primary,
                foreground="#0e0ed4",
            )
        else:
            lb = Label(
                frame,
                text="You Won",
                font=("Arial", 60),
                background=theme.background_primary,
                foreground="#0e0ed4",
            )
        lb2 = Label(
            frame,
            text="Game Over",
            font=("Arial", 30),
            background=theme.background_primary,
            foreground=theme.text_primary,
        )
        lb.grid(row=1, column=1)
        lb2.grid(row=2, column=1)

        root.mainloop()


# THIS IS UNFINISHED WORK.
def promote_pawn(x, y, color, data):
    choice = ""

    root = Tk()

    def set_choice(ch):
        choice = ch
        root.destroy()

    frame = Frame(root, background=theme.background_primary)
    frame.pack(expand=True, fill=BOTH)

    labl = Label(
        frame,
        text="Choose From List",
        background=theme.background_primary,
        foreground=theme.text_primary,
    )

    if color == "W":
        queen_image = PhotoImage(master=root, file=get_full_path("assets/w_q.png"))
        knight_image = PhotoImage(master=root, file=get_full_path("assets/w_n.png"))
        bishop_image = PhotoImage(master=root, file=get_full_path("assets/w_b.png"))
        rook_image = PhotoImage(master=root, file=get_full_path("assets/w_r.png"))
    else:
        queen_image = PhotoImage(master=root, file=get_full_path("assets/b_q.png"))
        knight_image = PhotoImage(master=root, file=get_full_path("assets/b_n.png"))
        bishop_image = PhotoImage(master=root, file=get_full_path("assets/b_b.png"))
        rook_image = PhotoImage(master=root, file=get_full_path("assets/b_r.png"))

    buttn1 = Button(
        frame,
        text="Queen",
        font=("Arial", 15),
        width=60,
        height=60,
        image=queen_image,
        border=0,
        background=theme.color_primary,
        command=lambda: set_choice("Q"),
    )
    buttn2 = Button(
        frame,
        text="Knight",
        font=("Arial", 15),
        width=60,
        height=60,
        image=knight_image,
        border=0,
        background=theme.color_primary,
        command=lambda: set_choice("N"),
    )
    buttn3 = Button(
        frame,
        text="Bishop",
        font=("Arial", 15),
        width=60,
        height=60,
        image=bishop_image,
        border=0,
        background=theme.color_primary,
        command=lambda: set_choice("B"),
    )
    buttn4 = Button(
        frame,
        text="Rook",
        font=("Arial", 15),
        width=60,
        height=60,
        image=rook_image,
        border=0,
        background=theme.color_primary,
        command=lambda: set_choice("R"),
    )

    labl.pack()

    buttn1.pack(pady=5)
    buttn2.pack(pady=5)
    buttn3.pack(pady=5)
    buttn4.pack(pady=5)

    root.mainloop()

    if choice == "Q":
        data[x][y] = Queen(x, y, color)
    elif choice == "N":
        data[x][y] = Knight(x, y, color)
    elif choice == "B":
        data[x][y] = Bishop(x, y, color)
    elif choice == "R":
        data[x][y] = Rook(x, y, color)

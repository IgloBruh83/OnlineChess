from tkinter import *

class Client:
    def __init__(self):
        root = self.root = Tk()
        root.geometry("620x710")
        root.resizable(False, False)
        root.title("Chess Online")

        # Graphics
        self.sprites = {
            'pawn_w': PhotoImage(file="Graphics/Pawn_White.png"),
            'pawn_b': PhotoImage(file="Graphics/Pawn_Black.png"),
            'knight_w': PhotoImage(file="Graphics/Knight_White.png"),
            'knight_b': PhotoImage(file="Graphics/Knight_Black.png"),
            'bishop_w': PhotoImage(file="Graphics/Bishop_White.png"),
            'bishop_b': PhotoImage(file="Graphics/Bishop_Black.png"),
            'rook_w': PhotoImage(file="Graphics/Rook_White.png"),
            'rook_b': PhotoImage(file="Graphics/Rook_Black.png"),
            'queen_w': PhotoImage(file="Graphics/Queen_White.png"),
            'queen_b': PhotoImage(file="Graphics/Queen_Black.png"),
            'king_w': PhotoImage(file="Graphics/King_White.png"),
            'king_b': PhotoImage(file="Graphics/King_Black.png")
        }


        # Canvas init
        c = self.c = Canvas(root, width=600, height=600)
        c.place(x=10, y=70)

        # Game field
        self.fieldColors = ['white', 'grey']
        for i in range(8):
            for j in range(8):
                c.create_rectangle(75 * i, 75 * j, 75 * (i + 1), 75 * (j + 1), fill=self.fieldColors[(i + j) % 2],
                                   outline="black")
        c.create_rectangle(3, 3, 600, 600, outline="black", width=2)

        # Player prefix (small text above player's nicknames)
        playerPrefix = self.playerPrefix = [Label(root, text="client.prefix", font=('Arial', 12)),
                        Label(root, text="opponent.prefix", font=('Arial', 12))]
        playerPrefix[0].place(x=20, y=25, anchor='w')
        playerPrefix[1].place(x=600, y=25, anchor='e')

        # Game timers
        playerTimer = self.playerTimer = [Label(root, text="XX:00", font=('Arial', 26)),
                       Label(root, text="XX:00", font=('Arial', 26))]
        playerTimer[0].place(x=240, y=35, anchor=CENTER)
        playerTimer[1].place(x=380, y=35, anchor=CENTER)

        # Header separator, static text
        Label(root, text='|\n|\n|', font=('Arial', 12)).place(x=310, y=35, anchor=CENTER)

        # Nicknames
        playerName = self.playerName = [Label(root, text="client.name", font=('Arial', 16)),
                      Label(root, text="opponent.name", font=('Arial', 16))]
        playerName[0].place(x=20, y=50, anchor='w')
        playerName[1].place(x=600, y=50, anchor='e')

        # Bottom hint-text
        hint = self.hint = Label(root, text="root.hint.bottom_text", font=('Arial', 12))
        hint.place(x=310, y=690, anchor=CENTER)
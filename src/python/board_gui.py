from tkinter import Tk, Frame, Grid, Button, N, S, E, W
import random

COLORS = [
    'snow', 'blanched almond', 'lavender blush', 'navy', 'dodger blue',
    'dark turquoise', 'dark olive green', 'green yellow', 'light yellow',
    'sandy brown', 'orange red', 'violet red', 'snow3', 'bisque2',
    'LemonChiffon2', 'honeydew2', 'azure2', 'RoyalBlue3', 'SteelBlue3',
    'LightSkyBlue1', 'LightSteelBlue2', 'LightCyan4', 'turquoise1',
    'DarkSlateGray3', 'SeaGreen2', 'green2', 'DarkOliveGreen1',
    'LightGoldenrod2', 'gold2', 'DarkGoldenrod3', 'IndianRed4', 'wheat1',
    'chocolate3', 'salmon1', 'orange4', 'tomato2', 'DeepPink2', 'pink3',
    'PaleVioletRed4', 'magenta2', 'plum3', 'DarkOrchid4', 'thistle1'
]


class BoardGUI:
    def __init__(self, board):

        self.root = Tk()
        self.board = board

        root = self.root
        root.geometry("500x500")
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        frame = Frame(root)
        frame.grid(row=0, column=0, sticky=N + S + E + W)

        for r in range(board.nrow):
            Grid.rowconfigure(frame, r, weight=1)
            for c in range(board.ncol):
                Grid.columnconfigure(frame, c, weight=1)
                btn = Button(frame)
                btn.grid(row=r, column=c, sticky=N + S + E + W)
                board.grid[r][c].btn = btn

    def display(self):
        board = self.board
        random.shuffle(COLORS)
        for r in range(board.nrow):
            for c in range(board.ncol):
                cell = board.grid[r][c]
                cell.btn.config(bg=COLORS[cell.group])
        self.root.mainloop()
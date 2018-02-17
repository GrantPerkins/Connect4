import tkinter as tk
import tkinter.font as font
class Button(tk.Button):
    def __init__(self, root, game, n):
        super().__init__(root, text=str(n), command= lambda: game.add(n,game.turn), width=3, height=1,
            font=font.Font(family='Helvetica', size=36, weight='bold'))
        self.n = n

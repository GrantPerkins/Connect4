import tkinter as tk
import tkinter.font as font

class Button(tk.Button):
    def __init__(self, root, game, n):
        self.game = game
        self.n = n
        super().__init__(root, text=str(n), command= self.callback, width=3, height=1,
            font=font.Font(family='Helvetica', size=36, weight='bold'), bg="blue")
        self.n = n

    def callback(self):
        if self.game.turn:
            return self.game.add(self.n, self.game.turn)
        else:
            return self.game.add(self.n, self.game.turn)


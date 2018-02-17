import tkinter as tk
from Button import Button
root = tk.Tk()

class Game:
    def __init__(self):
        self.width = 7
        self.height = 6
        self.board = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.team_zero = 0
        self.team_one = 1
        self.turn = 0
        self.canvas = tk.Canvas(relief=tk.FLAT, background="#D2D2D2", width=700, height=700)

    def draw_grid(self):
        self.canvas.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

        buttons = []
        button_windows = []

        for i in range(7):
            buttons.append(Button(i))
            button_windows.append(self.canvas.create_window(i * 100, 0, anchor=tk.NW, window=buttons[-1]))
        for y in range(100, 7 * 100, 100):
            for x in range(0, 7 * 100, 100):
                self.canvas.create_rectangle(x, y, x + 100, y + 100, fill="blue")
                self.canvas.create_oval(x, y, x + 100, y + 100, fill="white")

    def add(self, column, team):
        index = 0
        while True:
            if index<6 and self.board[index][column] == None:
                index += 1
            else:
                index -= 1
                self.board[index][column] = team
                self.draw_chip(column*100, (index+1)*100, team)
                self.turn = self.turn ^ 1
                break

    def draw_chip(self, x, y, team):
        if team == 0:
            color = "red"
        else:
            color = "yellow"
        self.canvas.create_oval(x,y,x+100,y+100,fill=color)
if __name__ == "__main__":
    game = Game()
    game.draw_grid()

    root.resizable(False, False)
    root.title("Connect 4 ML")
    root.mainloop()
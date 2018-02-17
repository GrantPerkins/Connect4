import tkinter as tk
import tkinter.font as font
import sys
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
            buttons.append(Button(root, game, i))
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
            elif index != 0:
                index -= 1
                self.board[index][column] = team
                self.draw_chip(column*100, (index+1)*100, team)
                self.turn = self.turn ^ 1
                if self.process():
                    sys.exit(99)
                break
            else:
                break

    def draw_chip(self, x, y, team):
        if team == 0:
            color = "red"
        else:
            color = "yellow"
        self.canvas.create_oval(x,y,x+100,y+100,fill=color)

    def process(self):
        print("-----------------===================--------------------------")
        for y in range(6):
            for x in range(7):
                for direction in range(4):
                    if self.board[y][x] != None and self.check_four(0, self.board[y][x], x, y, direction):
                        print(direction)
                        return True
        return False

    def check_four(self, n, team, x, y, direction):
        """
        n:
            Number of chips of same color in a row so far; used for recursion
        direction:
            0: horizontal to left
            1: diagonal left
            2: down
            3: diagonal right
        """
        if self.board[y][x] == team:
            if direction == 0:
                if x == 6:
                    return False
                elif n==3:
                    return True
                else:
                    print("horizontal", n, team, "x:", x, "y:", y)
                    return self.check_four(n+1, team, x + 1, y, direction)
            elif direction == 1:
                if x == 6 or y == 5:
                    if n==3 and y==5:
                        return True
                    return False
                elif n==3:
                    return True
                else:
                    #print("diagonal ", n, team, "x:", x, "y:", y, direction)
                    return self.check_four(n + 1, team, x + 1, y + 1, direction)
            elif direction == 2:
                if y == 5:
                    return False
                elif n==3:
                    return True
                else:
                    #print("vertical ", n, team, "x:", x, "y:", y, direction)
                    return self.check_four(n + 1, team, x, y + 1, direction)
            else:
                if x == 0 or y == 5:
                    if n == 3 and y == 5:
                        return True
                    return False
                elif n == 3:
                    return True
                else:
                    #print("diagonal ", n, team, "x:", x, "y:", y, direction)
                    return self.check_four(n + 1, team, x - 1, y + 1, direction)
        return False


if __name__ == "__main__":
    game = Game()
    game.draw_grid()

    root.resizable(False, False)
    root.title("Connect 4 ML")
    root.mainloop()
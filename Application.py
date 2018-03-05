import tkinter as tk
import tkinter.font as font
import sys
from Button import Button
root = tk.Tk()

class Game:
    def __init__(self):
        self.width = 7
        self.height = 6
        self.team_zero = 0
        self.team_one = 1
        self.turn = 0

        self.canvas = tk.Canvas(background="white", width=700, height=800)
        self.canvas.pack(side=tk.BOTTOM, anchor=tk.NW, padx=10)

        buttons = []
        button_windows = []
        for i in range(7):
            buttons.append(Button(root, self, i))
            button_windows.append(self.canvas.create_window(i * 100, 0, anchor=tk.NW, window=buttons[-1]))

        self.menu = tk.Canvas(relief=tk.FLAT, background="white", width=700, height=25)
        self.menu.pack(side=tk.TOP, anchor=tk.NW, padx=10)
        self.quit = tk.Button(root, text="Quit", command=root.destroy, height=1, width=5,
                              font=font.Font(family='Helvetica', size=10), bg="yellow")
        self.restart = tk.Button(root, text="Restart", command=self.draw_grid, height=1, width=5,
                                 font=font.Font(family='Helvetica', size=10), bg="red")
        self.title = tk.Label(root, text="Connect 4", bg="white", font=font.Font(family='Helvetica', size=12))
        self.menu.create_window(700,2,anchor=tk.NE,window=self.quit)
        self.menu.create_window(0, 2, anchor=tk.NW, window=self.restart)
        self.menu.create_window(350, 5, anchor=tk.N, window=self.title)

    def draw_grid(self):
        try:
            self.kill_winner()
        except:
            pass
        self.board = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.winner = False
        self.turn = 0

        for y in range(100, 7 * 100, 100):
            for x in range(0, 7 * 100, 100):
                self.canvas.create_rectangle(x, y, x + 100, y + 100, fill="blue")
                self.canvas.create_oval(x+7, y+7, x + 100-7, y + 100-7, fill="white")

    def add(self, column):
        team = self.turn
        if not self.winner:
            index = 0
            while True:
                if index<6 and self.board[index][column] == None:
                    index += 1
                elif index != 0:
                    index -= 1
                    self.board[index][column] = team
                    self.draw_chip(column*100, (index+1)*100, team)
                    self.turn = self.turn ^ 1
                    self.winner = self.process()
                    if self.winner:
                        self.win_rect = self.canvas.create_rectangle(200, 200, 500, 500, fill=self.winner)
                        self.win_dialogue = self.canvas.create_text(350,350,text="WINNER",width=200,
                                                font=font.Font(family='Helvetica', size=36, weight='bold'),
                                                fill="black")
                        self.close = self.canvas.create_window(500,200, anchor = tk.NE, window=tk.Button(root,
                                                    text="X", command=self.kill_winner,
                                                    font=font.Font(family='Helvetica', size=8),
                                                    width=2))
                    break
                else:
                    break

    def kill_winner(self):
        self.canvas.delete(self.win_dialogue)
        self.canvas.delete(self.close)
        self.canvas.delete(self.win_rect)

    def draw_chip(self, x, y, team):
        if team == 0:
            color = "red"
        else:
            color = "yellow"
        self.canvas.create_oval(x+7,y+7,x+100-7,y+100-7,fill=color)

    def process(self):
        for y in range(6):
            for x in range(7):
                for direction in range(4):
                    if self.board[y][x] != None and self.check_four(0, self.board[y][x], x, y, direction):
                        return "yellow" if self.board[y][x] else "red"
        return False

    def check_four(self, n, team, x, y, direction):
        """
        n:
            Number of chips of same color in a row so far; used for recursion
        team:
            0 or 1, representing team algorithm is checking for.
        direction:
            0: horizontal to left
            1: diagonal going left down
            2: vertical
            3: diagonal goig right down
        """
        if self.board[y][x] == team:
            if n == 3:
                return True
            if direction == 0:
                if x == 6:
                    return False
                else:
                    return self.check_four(n+1, team, x + 1, y, direction)
            elif direction == 1:
                if x == 6 or y == 5:
                    return False
                else:
                    return self.check_four(n + 1, team, x + 1, y + 1, direction)
            elif direction == 2:
                if y == 5:
                    return False
                else:
                    return self.check_four(n + 1, team, x, y + 1, direction)
            else:
                if x == 0 or y == 5:
                    return False
                else:
                    return self.check_four(n + 1, team, x - 1, y + 1, direction)
        return False

if __name__ == "__main__":
    game = Game()
    game.draw_grid()

    root.resizable(False, False)
    root.title("Connect 4 ML")
    root.mainloop()
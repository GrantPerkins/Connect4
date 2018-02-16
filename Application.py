import tkinter as tk

root = tk.Tk()
class Button(tk.Button):
    def __init__(self, n):
        super().__init__(root, text=str(n), command=self.callback,width=10,height=7)
        self.n = n
    def callback(self):
        print("click", self.n)

canvas = tk.Canvas(relief = tk.FLAT, background = "#D2D2D2", width = 812, height = 700)
canvas.pack(side = tk.TOP, anchor = tk.NW, padx = 10, pady = 10)

buttons = []
button_windows = []

for i in range(7):
    buttons.append(Button(i))
    button_windows.append(canvas.create_window(i*116, 0, anchor=tk.NW, window=buttons[-1]))

root.resizable(False, False)
root.title("Connect 4 ML")
root.mainloop()
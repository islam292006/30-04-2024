import tkinter as tk
from random import randint

root = tk.Tk()
root.title("Сапёр на tkinter")

ROWS = 10
COLS = 10
MINES = 10

buttons = {}

for x in range(0, ROWS):
    for y in range(0, COLS):
        btn = tk.Button(root, text='', width=2, height=1, command=lambda x=x, y=y: on_click(x, y))
        btn.grid(row=x, column=y, sticky=tk.N+tk.W+tk.S+tk.E)
        buttons[(x, y)] = btn

mines = []

while len(mines) < MINES:
    x, y = randint(0, ROWS-1), randint(0, COLS-1)
    if (x, y) not in mines:
        mines.append((x, y))

def on_click(x, y):
    if (x, y) in mines:
        buttons[(x, y)].config(text='*', background='red')
        game_over()
    else:
        count = sum(1 for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (x+dx, y+dy) in mines)
        buttons[(x, y)].config(text=str(count))

def game_over():
    for (x, y) in mines:
        buttons[(x, y)].config(background='red')
    for x, y in buttons:
        buttons[(x, y)]['state'] = 'disabled'

root.mainloop()


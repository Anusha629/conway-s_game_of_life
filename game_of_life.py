import tkinter as tk
from tkinter import ttk

WIDTH, HEIGHT = 40, 40
CELL_SIZE = 20
LIVE_CELL_COLOR = "green"
DEAD_CELL_COLOR = "white"


def get_empty_grid(width, height):
    grid = []
    for _ in range(height):
        row = [0] * width
        grid.append(row)
    return grid

def update_grid(grid):
    new_grid = get_empty_grid(WIDTH, HEIGHT)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            live_neighbors = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue  # Skip the current cell
                    new_i, new_j = i + x, j + y
                    if 0 <= new_i < HEIGHT and 0 <= new_j < WIDTH:
                        live_neighbors += grid[new_i][new_j]

            if grid[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

def display_grid(grid):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == 1:
                canvas.itemconfig(cells[i][j], fill=LIVE_CELL_COLOR)
            else:
                canvas.itemconfig(cells[i][j], fill=DEAD_CELL_COLOR)
    root.update()


root = tk.Tk()
root.title("Game of Life")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

canvas = tk.Canvas(frame, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE)
canvas.grid(row=0, column=0, columnspan=2, pady=10)

cells = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

for i in range(HEIGHT):
    for j in range(WIDTH):
        cells[i][j] = canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE, (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE, fill="white")

def initialize_and_display_grid():
    global grid
    grid = get_empty_grid(WIDTH, HEIGHT)
    display_grid(grid)
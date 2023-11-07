
WIDTH, HEIGHT = 40, 40


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

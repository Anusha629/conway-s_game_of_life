
WIDTH, HEIGHT = 40, 40

def get_empty_grid(width, height):
    grid = []
    for _ in range(height):
        row = [0] * width
        grid.append(row)
    return grid

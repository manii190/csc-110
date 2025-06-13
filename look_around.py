def make_grid(width, height):
    grid = []
    for i in range(height):
        row = ['o'] * width
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        print(row)

def in_limits(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return False
    return True

def mark_around(grid, x, y):
    for i in range(max(x - 1, 0), min(x + 2, len(grid))):
        for j in range(max(y - 1, 0), min(y + 2, len(grid[0]))):
            grid[i][j] = 'x'
    return grid







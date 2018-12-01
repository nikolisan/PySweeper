from random import randint
from Tile import Tile
from utilities import *


def create_grid():
    # Y, X = cols, rows
    cols, rows = GRID_SIZE
    grid = [[Tile(x, y) for y in range(cols)] for x in range(rows)]

    for n in range(NUM_BOMBS):
        while True:
            y = randint(0, cols-1)
            x = randint(0, rows-1)
            if not grid[x][y].bomb:
                grid[x][y].bomb = True
                break
    return grid


def inGrid(x, y):
    ROWS, COLS = GRID_SIZE
    if x in range(0, COLS) and y in range(0, ROWS):
        return True
    return False


def adjacent_bombs(grid):
    cols, rows = GRID_SIZE
    for x in range(rows):
        for y in range(cols):
            bombs_around = 0
            if grid[x][y].bomb:
                grid[x][y].label = "B"
            else:
                for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    if inGrid(x + dx, y + dy) and grid[x + dx][y + dy].bomb:
                        bombs_around += 1
                    grid[x][y].label = bombs_around
    return grid


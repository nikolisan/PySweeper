from random import randint
from src.GameState import GameState
from src.Tile import Tile
from src.utilities import *
import time



def set_difficulty(gs:GameState):
    difficulties = {
        "EASY": {
            "NUM_BOMBS" : 10,
            "GRID_SIZE" : (9, 9),
            "CELL_SIZE" : 60
        },
        "MEDIUM": {
            "NUM_BOMBS" : 40,
            "GRID_SIZE" : (16, 16),
            "CELL_SIZE" : 40
        },
        "HARD": {
            "NUM_BOMBS" : 99,
            "GRID_SIZE" : (30, 16),
            "CELL_SIZE" : 30
        }
    }
    
    gs.NUM_BOMBS = difficulties[gs.difficulty]["NUM_BOMBS"]
    gs.GRID_SIZE = difficulties[gs.difficulty]["GRID_SIZE"]
    gs.CELL_SIZE = difficulties[gs.difficulty]["CELL_SIZE"]

    


def new_game(gs:GameState):
    
    gs.marked_bombs = 0
    
    
    set_difficulty(gs) 

    gs.WINDOW_SIZE = (gs.GRID_SIZE[0] * gs.CELL_SIZE, gs.GRID_SIZE[1] * gs.CELL_SIZE + 200)
    
    gs.screen = pygame.display.set_mode(gs.WINDOW_SIZE)
    gs.screen.fill(colors.mainbg)
    gs.FONT_SIZE = int(gs.CELL_SIZE / 2)
    gs.FONT = pygame.font.SysFont("Arial", gs.FONT_SIZE)

    gs.grid = create_grid(gs.GRID_SIZE, gs.NUM_BOMBS)
    gs.grid = adjacent_bombs(gs.grid, gs.GRID_SIZE)
    draw_grid(gs.grid, gs.screen, gs.CELL_SIZE)

    pygame.display.set_caption(f"PySweeper - {gs.difficulty} - Bombs: {str(gs.marked_bombs).zfill(2)}/{gs.NUM_BOMBS}")
    pygame.display.flip()



def create_grid(GRID_SIZE, NUM_BOMBS):
    # Y, X = cols, rows
    cols, rows = GRID_SIZE
    print(f"{cols=} {rows=}")
    grid = [[Tile(x, y) for y in range(cols)] for x in range(rows)]

    for n in range(NUM_BOMBS):
        while True:
            y = randint(0, cols-1)
            x = randint(0, rows-1)
            if not grid[x][y].bomb:
                grid[x][y].bomb = True
                break
    return grid


def inGrid(x, y, GRID_SIZE):
    ROWS, COLS = GRID_SIZE
    if x in range(0, COLS) and y in range(0, ROWS):
        return True
    return False


def adjacent_bombs(grid, GRID_SIZE):
    cols, rows = GRID_SIZE
    for x in range(rows):
        for y in range(cols):
            bombs_around = 0
            if grid[x][y].bomb:
                grid[x][y].label = "B"
            else:
                for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    if inGrid(x + dx, y + dy, GRID_SIZE) and grid[x + dx][y + dy].bomb:
                        bombs_around += 1
                    grid[x][y].label = bombs_around
    return grid


def reveal_zeros(x, y, grid, screen, CELL_SIZE, FONT, GRID_SIZE):

    if not inGrid(x, y, GRID_SIZE) or getattr(grid[x][y], "revealed", False):
        return
    
    grid[x][y].revealed = True

    label = str(grid[x][y].label)
    if label == "0":
        colour_cell(x, y, colors.revealed, colors.revealedBorder, screen=screen, CELL_SIZE=CELL_SIZE)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    reveal_zeros(x + dx, y + dy, grid, screen, CELL_SIZE, FONT, GRID_SIZE)
    else:
        label, label_rect = text_objects(str(grid[x][y].label), FONT, colors.black, colors.white)
        label_rect.center = (y * CELL_SIZE + CELL_SIZE / 2, x * CELL_SIZE + CELL_SIZE / 2)
        screen.blit(label, label_rect)



def reveal_adjacent(x, y, grid, screen, CELL_SIZE, FONT, GRID_SIZE):
    for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        if inGrid(x + dx, y + dy, GRID_SIZE):
            if not grid[x + dx][y + dy].marked and not grid[x + dx][y + dy].revealed:
                if grid[x + dx][y + dy].bomb:
                    # Reveal all bombs and end game
                    for i, row in enumerate(grid):
                        for j, tile in enumerate(row):
                            if tile.bomb:
                                colour_cell(i, j, colors.red, screen=screen, CELL_SIZE=CELL_SIZE)
                    pygame.display.update()
                    print("Game Over")
                    return
                else:
                    reveal_zeros(x + dx, y + dy, grid, screen, CELL_SIZE, FONT, GRID_SIZE)
                


def check_win(grid):
    for row in grid:
        for tile in row:
            if not tile.bomb and not tile.revealed:
                return False
    return True
import sys
from src.game import *
from src.utilities import *

current_difficulty = "MEDIUM"

def new_game():
    # global grid, marked_bombs, NUM_BOMBS, CELL_SIZE, WINDOW_SIZE, BG_COLOR, FONT, screen
    marked_bombs = 0

    NUM_BOMBS = difficulty[current_difficulty]["NUM_BOMBS"]
    GRID_SIZE = difficulty[current_difficulty]["GRID_SIZE"]
    CELL_SIZE = difficulty[current_difficulty]["CELL_SIZE"]
    WINDOW_SIZE = (GRID_SIZE[0] * CELL_SIZE + 200, GRID_SIZE[1] * CELL_SIZE)
    print(GRID_SIZE, CELL_SIZE, WINDOW_SIZE)
    BG_COLOR = colors.mainbg
    screen = pygame.display.set_mode(WINDOW_SIZE)
    FONT_SIZE = int(CELL_SIZE / 2)
    FONT = pygame.font.SysFont("Arial", FONT_SIZE)
    screen.fill(BG_COLOR)

    grid = create_grid(GRID_SIZE, NUM_BOMBS)
    grid = adjacent_bombs(grid, GRID_SIZE)
    draw_grid(grid, screen, CELL_SIZE)
    draw_difficulty_menu(current_difficulty, screen, FONT)
    label, label_rect = text_objects(f"{str(marked_bombs).zfill(2)}/{NUM_BOMBS}", FONT, colors.black, BG_COLOR)
    label_rect = (WINDOW_SIZE[0] - 180, 120)
    screen.blit(label, label_rect)
    pygame.display.update()


    return NUM_BOMBS, CELL_SIZE, GRID_SIZE, WINDOW_SIZE, FONT, screen, grid


def mouse_press(event, grid, GRID_SIZE):
    global marked_bombs
    # pos = (x, y)
    # Button: 1 -> Left, 3 -> Right, 2 -> middle
    pos = event.pos
    button = event.button
    mouseY = int(pos[0] / CELL_SIZE)
    mouseX = int(pos[1] / CELL_SIZE)
    mouseY_to_size = mouseY * CELL_SIZE
    mouseX_to_size = mouseX * CELL_SIZE

    if inGrid(mouseX, mouseY, GRID_SIZE):
        if button == 1:
            if grid[mouseX][mouseY].bomb:
                for i, row in enumerate(grid):
                    for j, tile in enumerate(row):
                        if tile.bomb:
                            colour_cell(i, j, colors.red, screen=screen, CELL_SIZE=CELL_SIZE)
                pygame.display.update()
                print("Game Over")
                return
            elif grid[mouseX][mouseY].revealed:
                marked = 0
                for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    if inGrid(mouseX + dx, mouseY+ dy, GRID_SIZE) and grid[mouseX + dx][mouseY+ dy].marked:
                        marked += 1
                if marked >= int(grid[mouseX][mouseY].label):
                    reveal_adjacent(mouseX, mouseY, grid, screen, CELL_SIZE, FONT, GRID_SIZE)
                    if check_win(grid):
                        for i, row in enumerate(grid):
                            for j, tile in enumerate(row):
                                if tile.bomb:
                                    colour_cell(i, j, colors.green, screen=screen, CELL_SIZE=CELL_SIZE)
                        print("You Win!")
            else:
                grid[mouseX][mouseY].marked = False
                colour_cell(mouseX, mouseY, colors.white, screen=screen, CELL_SIZE=CELL_SIZE)
                reveal_zeros(mouseX, mouseY, grid, screen, CELL_SIZE, FONT, GRID_SIZE)
                if check_win(grid):
                    for i, row in enumerate(grid):
                        for j, tile in enumerate(row):
                            if tile.bomb:
                                colour_cell(i, j, colors.green, CELL_SIZE=CELL_SIZE)
                    print("You Win!")
                

        elif button == 3:
            if grid[mouseX][mouseY].revealed:
                return
            marked = grid[mouseX][mouseY].marked
            check_win(grid)
            if not marked:
                grid[mouseX][mouseY].revealed = False
                if marked_bombs == NUM_BOMBS:
                    return
                colour_cell(mouseX, mouseY, colors.flagged, screen=screen, CELL_SIZE=CELL_SIZE)
                marked_bombs += 1
            else:
                colour_cell(mouseX, mouseY, colors.white, screen=screen, CELL_SIZE=CELL_SIZE)
                marked_bombs -= 1

            marked = not(grid[mouseX][mouseY].marked)
            grid[mouseX][mouseY].marked = marked

            
            label, label_rect = text_objects(f"{str(marked_bombs).zfill(2)}/{NUM_BOMBS}", FONT, colors.black, colors.mainbg)
            label_rect = (WINDOW_SIZE[0] - 180, WINDOW_SIZE[1] - 450)
            screen.blit(label, label_rect)

    pygame.display.update()


NUM_BOMBS, CELL_SIZE, GRID_SIZE, WINDOW_SIZE, FONT, screen, grid = new_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press(event, grid, GRID_SIZE)

        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        if inButtonReset(pos, WINDOW_SIZE):
            draw_button_1((WINDOW_SIZE[0] - 180, 25, 125, 50), colors.blue, screen, FONT)
            if pressed[0]:
                NUM_BOMBS, CELL_SIZE, GRID_SIZE, WINDOW_SIZE, FONT, screen, grid = new_game()
        else:
            draw_button_1((WINDOW_SIZE[0] - 180, 25, 125, 50), colors.darkBlue, screen, FONT)



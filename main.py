import sys
from src.GameState import GameState
from src.game import *
from src.utilities import *


def mouse_press(event, gs:GameState):
    global marked_bombs
    # pos = (x, y)
    # Button: 1 -> Left, 3 -> Right, 2 -> middle
    pos = event.pos
    button = event.button
    mouseY = int(pos[0] / gs.CELL_SIZE)
    mouseX = int(pos[1] / gs.CELL_SIZE)
    mouseY_to_size = mouseY * gs.CELL_SIZE
    mouseX_to_size = mouseX * gs.CELL_SIZE

    if inGrid(mouseX, mouseY, gs.GRID_SIZE):
        if button == 1:
            if gs.grid[mouseX][mouseY].bomb:
                for i, row in enumerate(gs.grid):
                    for j, tile in enumerate(row):
                        if tile.bomb:
                            colour_cell(i, j, colors.red, screen=gs.screen, CELL_SIZE=gs.CELL_SIZE)
                pygame.draw.rect(gs.screen, colors.dark_red, (gs.WINDOW_SIZE[0] - gs.WINDOW_SIZE[0] // 2 - 150 , gs.WINDOW_SIZE[1] - gs.WINDOW_SIZE[1] //2 - 200, 300, 200), 0)
                pygame.draw.rect(gs.screen, colors.black, (gs.WINDOW_SIZE[0] - gs.WINDOW_SIZE[0] // 2 - 150 , gs.WINDOW_SIZE[1] - gs.WINDOW_SIZE[1] //2 - 200, 300, 200), 1)
                pygame.display.update()
                return
            elif gs.grid[mouseX][mouseY].revealed:
                marked = 0
                for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    if inGrid(mouseX + dx, mouseY+ dy, gs.GRID_SIZE) and gs.grid[mouseX + dx][mouseY+ dy].marked:
                        marked += 1
                if marked >= int(gs.grid[mouseX][mouseY].label):
                    reveal_adjacent(mouseX, mouseY, gs.grid, gs.screen, gs.CELL_SIZE, gs.FONT, gs.GRID_SIZE)
                    if check_win(gs.grid):
                        for i, row in enumerate(gs.grid):
                            for j, tile in enumerate(row):
                                if tile.bomb:
                                    colour_cell(i, j, colors.green,screen=gs.screen, CELL_SIZE=gs.CELL_SIZE)
                        pygame.draw.rect(gs.screen, colors.dark_green, (gs.WINDOW_SIZE[0] - gs.WINDOW_SIZE[0] // 2 - 150 , gs.WINDOW_SIZE[1] - gs.WINDOW_SIZE[1] //2 - 200, 300, 200), 0)
                        pygame.draw.rect(gs.screen, colors.black, (gs.WINDOW_SIZE[0] - gs.WINDOW_SIZE[0] // 2 - 150 , gs.WINDOW_SIZE[1] - gs.WINDOW_SIZE[1] //2 - 200, 300, 200), 1)
                        pygame.display.update()
            else:
                gs.grid[mouseX][mouseY].marked = False
                colour_cell(mouseX, mouseY, colors.white, screen=gs.screen, CELL_SIZE=gs.CELL_SIZE)
                reveal_zeros(mouseX, mouseY, gs.grid, gs.screen, gs.CELL_SIZE, gs.FONT, gs.GRID_SIZE)
                if check_win(gs.grid):
                    for i, row in enumerate(gs.grid):
                        for j, tile in enumerate(row):
                            if tile.bomb:
                                colour_cell(i, j, colors.green, CELL_SIZE=gs.CELL_SIZE)
                    print("You Win!")
                

        elif button == 3:
            if gs.grid[mouseX][mouseY].revealed:
                return
            marked = gs.grid[mouseX][mouseY].marked
            check_win(gs.grid)
            if not marked:
                gs.grid[mouseX][mouseY].revealed = False
                if gs.marked_bombs == gs.NUM_BOMBS:
                    return
                colour_cell(mouseX, mouseY, colors.flagged, screen=gs.screen, CELL_SIZE=gs.CELL_SIZE)
                gs.marked_bombs += 1
            else:
                colour_cell(mouseX, mouseY, colors.white, screen=gs.screen, CELL_SIZE=gs.CELL_SIZE)
                gs.marked_bombs -= 1

            marked = not(gs.grid[mouseX][mouseY].marked)
            gs.grid[mouseX][mouseY].marked = marked

            
            pygame.display.set_caption(f"PySweeper - {gs.difficulty} - Bombs: {str(game_state.marked_bombs).zfill(2)}/{game_state.NUM_BOMBS}")
            
    pygame.display.update()


# ----------------------------------------------------- #



difficulty = "EASY"

game_state = GameState(difficulty)

pygame.init()
pygame.font.init()

new_game(game_state)
game_state.buttons = draw_menu(game_state)  # <-- Assign returned buttons list



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press(event, game_state)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        
        for btn in game_state.buttons:
            if btn.is_hovered(mouse_x, mouse_y):
                btn.draw(game_state.screen, game_state.FONT, color=colors.cyan)
                if pressed[0]:
                    btn.click()
            else:
                btn.draw(game_state.screen, game_state.FONT)

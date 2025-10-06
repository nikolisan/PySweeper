import pygame
import src.game as game
import src.colors as colors
from src.GameState import GameState
from src.Button import Button


def text_objects(text, font, color, bg):
    text_surface = font.render(text, True, color, bg)
    return text_surface, text_surface.get_rect()


def draw_grid(grid, screen, CELL_SIZE):
    for i, row in enumerate(grid):
        y = i * CELL_SIZE
        for j, tile in enumerate(row):
            x = j * CELL_SIZE
            # if tile.bomb:
            #     pygame.draw.rect(screen, colors.red, (x, y, CELL_SIZE, CELL_SIZE), 0)
            # else:
            #     pygame.draw.rect(screen, colors.white, (x, y, CELL_SIZE, CELL_SIZE), 0)
            pygame.draw.rect(screen, colors.white, (x, y, CELL_SIZE, CELL_SIZE), 0)
            pygame.draw.rect(screen, colors.black, (x, y, CELL_SIZE, CELL_SIZE), 1)
    pygame.display.flip()


def inButton(mousePos, btnRect):
    # btnRect = Rect(left, top, width, height) -> Rect
    x, y = mousePos
    left, top, w, h = btnRect
    if x in range(left, left+w) and y in range(top, top + h):
        return True
    return False


def colour_cell(i, j , colour, bg=colors.black, screen=None, CELL_SIZE=None):
    pygame.draw.rect(screen, colour, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
    pygame.draw.rect(screen, bg, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


    
def draw_menu(gs:GameState):
    difficulties = ["EASY", "MEDIUM", "HARD"]
    buttons = []
    # No need to fill here, do it in btn_difficulty
    for i, diff in enumerate(difficulties[::-1]):
        selected_difficulty = True if diff == gs.difficulty else False
        w, h = 125, 50
        x = gs.WINDOW_SIZE[0] - 150 - i * (w + 50)
        y = gs.WINDOW_SIZE[1] - 60
        
        btn = Button(x, y, w, h, diff, selected=selected_difficulty)
        btn.on_click = lambda btn=btn: btn_difficulty(gs, btn)
        btn.draw(gs.screen, gs.FONT )
        buttons.append(btn)
    
    reset_btn = Button(gs.WINDOW_SIZE[0] - 150, gs.WINDOW_SIZE[1] - 190, 125, 50, "RESET", on_click=lambda: reset_game(gs))
    reset_btn.draw(gs.screen,gs.FONT)
    buttons.append(reset_btn)
    
    pygame.display.flip()
    return buttons


def get_difficulty_from_pos(pos):
    difficulties = ["EASY", "MEDIUM", "HARD"]
    for i, diff in enumerate(difficulties):
        x = 20 + i * 140
        y = 25
        w, h = 120, 50
        if x <= pos[0] <= x + w and y <= pos[1] <= y + h:
            return diff
    return None


def reset_game(gs:GameState):
    game.new_game(gs)
    

def btn_difficulty(gs: GameState, btn: Button):
    
    gs.difficulty = btn.get_label()
    reset_game(gs)
    gs.buttons = draw_menu(gs)     # Assign new buttons list
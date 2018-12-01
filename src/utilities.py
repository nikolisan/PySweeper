import pygame
import game
import colors

def text_objects(text, font, color, bg):
    text_surface = font.render(text, True, color, bg)
    return text_surface, text_surface.get_rect()


def draw_button_1(position, color):
    pygame.draw.rect(screen, color, position, 0)
    label, label_rect = text_objects("RESET", FONT, colors.white, None)
    label_rect.center = (position[0]+position[2]/2, position[1]+position[3]/2)
    screen.blit(label, label_rect)
    pygame.display.update()


def draw_grid(grid):
    for i, row in enumerate(grid):
        y = i * CELL_SIZE
        for j, tile in enumerate(row):
            x = j * CELL_SIZE
            if tile.bomb:
                pygame.draw.rect(screen, colors.red, (x, y, CELL_SIZE, CELL_SIZE), 0)
            else:
                pygame.draw.rect(screen, colors.white, (x, y, CELL_SIZE, CELL_SIZE), 0)
            pygame.draw.rect(screen, colors.black, (x, y, CELL_SIZE, CELL_SIZE), 1)
    pygame.display.update()


def inButtonReset(pos):
    x, y = pos
    if x in range(WINDOW_SIZE[0]-150, WINDOW_SIZE[0]-24) and y in range(25, 76):
        return True
    return False


WINDOW_SIZE = (800, 600)
GAME_SIZE = (600, 600)
NUM_BOMBS = 10
GRID_SIZE = (10, 10)
CELL_SIZE = int(GAME_SIZE[0]/NUM_BOMBS)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("PySweeper")
pygame.init()
pygame.font.init()

screen.fill(colors.pink)
FONT = pygame.font.SysFont("Comic Sans MS", 35)

draw_button_1((WINDOW_SIZE[0] - 150, 25, 125, 50), colors.darkBlue)


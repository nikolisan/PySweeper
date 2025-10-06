import pygame
import src.game as game
import src.colors as colors


def text_objects(text, font, color, bg):
    text_surface = font.render(text, True, color, bg)
    return text_surface, text_surface.get_rect()


def draw_button_1(position, color, screen, FONT):
    pygame.draw.rect(screen, color, position, 0)
    label, label_rect = text_objects("RESET", FONT, colors.white, None)
    label_rect.center = (position[0]+position[2]/2, position[1]+position[3]/2)
    screen.blit(label, label_rect)
    pygame.display.update()


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
    pygame.display.update()


def inButtonReset(pos, WINDOW_SIZE):
    x, y = pos
    if x in range(WINDOW_SIZE[0]-150, WINDOW_SIZE[0]-24) and y in range(25, 76):
        return True
    return False


def colour_cell(i, j , colour, bg=colors.black, screen=None, CELL_SIZE=None):
    pygame.draw.rect(screen, colour, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
    pygame.draw.rect(screen, bg, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


def draw_difficulty_menu(selected=None, screen=None, FONT=None):
    difficulties = ["EASY", "MEDIUM", "HARD"]
    for i, diff in enumerate(difficulties):
        color = colors.flagged if diff == selected else colors.darkBlue
        x = 20 + i * 140
        y = 25
        w, h = 100, 40
        pygame.draw.rect(screen, color, (x, y, w, h), 0)
        label, label_rect = text_objects(diff, FONT, colors.white, color)
        label_rect.center = (x + w // 2, y + h // 2)
        screen.blit(label, label_rect)
    pygame.display.update()


def get_difficulty_from_pos(pos):
    difficulties = ["EASY", "MEDIUM", "HARD"]
    for i, diff in enumerate(difficulties):
        x = 20 + i * 140
        y = 25
        w, h = 120, 50
        if x <= pos[0] <= x + w and y <= pos[1] <= y + h:
            return diff
    return None


difficulty = {
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



# NUM_BOMBS = difficulty["HARD"]["NUM_BOMBS"]
# GRID_SIZE = difficulty["HARD"]["GRID_SIZE"]
# CELL_SIZE = difficulty["HARD"]["CELL_SIZE"]
# WINDOW_SIZE = (GRID_SIZE[0] * CELL_SIZE + 200, GRID_SIZE[1] * CELL_SIZE)
# BG_COLOR = colors.mainbg

# screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("PySweeper")
pygame.init()
pygame.font.init()

# screen.fill(BG_COLOR)
# FONT_SIZE = int(CELL_SIZE / 2)
# FONT = pygame.font.SysFont("Arial", FONT_SIZE)

# label, label_rect = text_objects("Bombs:", FONT, colors.black, BG_COLOR)
# label_rect = (WINDOW_SIZE[0] - 180, 100)
# screen.blit(label, label_rect)


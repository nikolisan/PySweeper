import sys
from game import *
from utilities import *


def new_game():
    global grid
    grid = create_grid()
    grid = adjacent_bombs(grid)
    draw_grid(grid)


def mouse_press(event):
    # pos = (x, y)
    # Button: 1 -> Left, 3 -> Right, 2 -> middle
    pos = event.pos
    button = event.button
    mouseY = int(pos[0] / CELL_SIZE)
    mouseX = int(pos[1] / CELL_SIZE)
    mouseY_to_size = mouseY * CELL_SIZE
    mouseX_to_size = mouseX * CELL_SIZE

    if inGrid(mouseX, mouseY):
        if button == 1:
            label, label_rect = text_objects("F", FONT, colors.white, colors.white)
            label_rect.center = (mouseY_to_size + CELL_SIZE / 2, mouseX_to_size + CELL_SIZE / 2)
            screen.blit(label, label_rect)
            label, label_rect = text_objects(str(grid[mouseX][mouseY].label), FONT, colors.black, colors.white)
            label_rect.center = (mouseY_to_size + CELL_SIZE / 2, mouseX_to_size + CELL_SIZE / 2)
            screen.blit(label, label_rect)
        elif button == 3:
            label, label_rect = text_objects("F", FONT, colors.black, colors.white)
            label_rect.center = (mouseY_to_size + CELL_SIZE/2, mouseX_to_size+CELL_SIZE/2)
            screen.blit(label, label_rect)
    pygame.display.update()


new_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press(event)

        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        if inButtonReset(pos):
            draw_button_1((WINDOW_SIZE[0] - 150, 25, 125, 50), colors.blue)
            if pressed[0]:
                new_game()
        else:
            draw_button_1((WINDOW_SIZE[0] - 150, 25, 125, 50), colors.darkBlue)



import pygame
from src.utilities import *

def text_objects(text, font, color, bg):
    text_surface = font.render(text, True, color, bg)
    return text_surface, text_surface.get_rect()

class Button:
    def __init__(self, left, top, width, height, label, selected = False, on_click=None):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.label = label
        self.selected = selected
        self.enabled = True
        self.visible = True
        self.on_click = on_click
    
    def __repr__(self):
        return f'Button("{self.get_label()}")'
    
    def click(self):
        if self.enabled and self.on_click:
            self.on_click()       
        
    def get_label(self):
        return self.label

    def is_hovered(self, mouse_x, mouse_y):
        """Check if the mouse is over the button."""
        return (
            self.visible and
            self.left <= mouse_x < self.left + self.width and
            self.top <= mouse_y < self.top + self.height
        )

    def set_visible(self, visible):
        self.visible = visible

    def draw(self, screen, FONT, color = None):
        """
        Draw the button on the given surface.
        You should implement the actual drawing logic based on your rendering system.
        """
        if not self.visible:
            return
        
        position = (self.left, self.top, self.width, self.height)
        if not color:
            color = colors.flagged if self.selected else colors.darkBlue
        
        pygame.draw.rect(screen, color, position, 0)
        label, label_rect = text_objects(self.label, FONT, colors.white, None)
        label_rect.center = (position[0] + position[2] // 2, position[1] + position[3] // 2)
        screen.blit(label, label_rect)
        pygame.display.update()

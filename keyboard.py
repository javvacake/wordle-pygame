import pygame
from pygame_vkeyboard import *
from colours import *
from os.path import join, dirname

pygame.init()

pygame.font.init()
FONT = pygame.font.SysFont("assets\Helvetica Neu Bold.ttf", 10)

class KeyboardRenderer(VKeyboardRenderer):
    def __init__(self, font_name, text_color, cursor_color, selection_color, background_color, background_key_color, background_input_color, text_special_key_color=None, background_special_key_color=None):
        super().__init__(font_name, text_color, cursor_color, selection_color, background_color, background_key_color, background_input_color, text_special_key_color, background_special_key_color)
    
    # def draw_background(self, surface, position, size):
    #     pygame.draw.rect(surface, (0, 0, 0, 150), position + size)

    def draw_character_key(self, surface, key, special=False):
        # pygame.draw.rect(surface, WHITE, key.position + (key.size, key.size), 1)
        # surface.blit(FONT.render(key.value, 1, WHITE, None), key.position)
        # background_colour = self.key_background_color
        pass

KeyboardRenderer.WORDLE = KeyboardRenderer(
    #pygame.font.Font(join(dirname("assets/"), "Helvetica Neu Bold.ttf"), 10), # Key font name/path
    pygame.font.Font("assets\Helvetica Neu Bold.ttf", 10),
    (WHITE, WHITE), # Text color for key and text box (one per state: released, pressed).
    BLACK, # Text box cursor color.
    GREY, # Color to highlight the selected key.
    GREY, # Keyboard background color.
    (GREY, GREY), # Key background color (one per state, as for the text color).
    WHITE, # Text input background color.
)
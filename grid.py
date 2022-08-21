import string
import pygame
from colours import GREEN, YELLOW, GREY, BLACK, WHITE

pygame.font.init()
FONT = pygame.font.Font("helveticaneue\Helvetica Neu Bold.ttf", 20)

LETTERS = list(string.ascii_uppercase)

class Grid:
    def __init__(self):
        self.matrix = [[Cell(i, j)] for j in range(5) for i in range(6)]
        self.current_row = 0
        self.current_col = 0

    # TODO: finish function
    def enter_letter(self, letter):
        letter = chr(letter).upper()
        if letter in LETTERS:
            if self.current_col == 5:
                return
            else:
                self.matrix[self.current_row][self.current_col].assign_letter(letter)
                self.current_col += 1

    # TODO: finish function
    def backspace(self):
        if self.current_col < 1:
            return

    def draw(self, window):
        for row in self.matrix:
            for cell in row:
                cell.draw(window)

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.letter = None
        self.bg_colour = None
        self.x = (col + 1) * 60
        self.y = (row + 1) * 60
        self.size = 50
        self.entered = False

    def get_letter(self):
        return self.letter

    def set_letter(self, letter):
        self.letter = letter

    def delete_letter(self):
        self.letter = None
    
    # TODO: finish function
    def draw(self, window):
        bg_colour = self.bg_colour if self.entered else WHITE
        
        pygame.draw.rect(window, bg_colour, pygame.Rect(self.x, self.y, self.size, self.size))
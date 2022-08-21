import string
import pygame
from colours import GREEN, YELLOW, GREY, BLACK, WHITE

pygame.font.init()
FONT = pygame.font.Font("helveticaneue\Helvetica Neu Bold.ttf", 60)

LETTERS = list(string.ascii_uppercase)

class Grid:
    def __init__(self):
        self.matrix = [[Square(i, j) for i in range(5)] for j in range(6)]
        self.current_row = 0
        self.current_col = 0

    # TODO: finish function
    def enter_letter(self, letter):
        print("To enter: ", self.current_row, " ", self.current_col)
        letter = letter.upper()
        if self.current_col == 5:
            return
        
        self.matrix[self.current_row][self.current_col].set_letter(letter)
        self.current_col += 1
        # print("Enter_letter row/col: ", self.current_row, " ", self.current_col)

    # TODO: finish function
    def backspace(self):
        if self.current_col < 0:
            self.current_col = 0
            return
        
        self.current_col = self.current_col - 1
        self.matrix[self.current_row][self.current_col].set_letter(None)

    def get_word(self):
        word = ""
        for square in self.matrix[self.current_row]:
            try:
                word += square.get_letter()
            except:
                return word
        return word

    def draw(self, window):
        # print("drawing cells")
        for row in self.matrix:
            for square in row:
                square.draw(window)

class Square:
    def __init__(self, col, row):
        self.row = row
        self.col = col
        self.letter = None
        self.bg_colour = None
        self.size = 60
        self.x = (col + 1) * (self.size + 15)
        self.y = (row + 1) * (self.size + 15)
        self.entered_row = False

    def get_letter(self):
        return self.letter

    def set_letter(self, letter):
        self.letter = letter

    def delete_letter(self):
        self.letter = None
    
    # TODO: finish function
    def draw(self, window):
        bg_colour = self.bg_colour if self.entered_row else WHITE
        
        # Border rectangle
        border_colour = BLACK
        pygame.draw.rect(window, border_colour, pygame.Rect(self.x, self.y, self.size, self.size))

        # if not self.entered_row:
        # Actual rectangle
        pygame.draw.rect(window, bg_colour, pygame.Rect(self.x + 2, self.y + 2, self.size - 4, self.size - 4))

        if self.letter != None:
            # Add text
            text_col = BLACK # if not self.entered_row else WHITE
            text = FONT.render(self.letter, False, text_col)
            window.blit(text, (self.x + 10, self.y - 5))
            # print("draw(cell) row/col: ", self.row, " ", self.col)
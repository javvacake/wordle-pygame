import pygame
import random
from pygame.locals import *
from grid import Grid
from rules import Rules
from letters import LETTERS
from words import *
from colours import *

pygame.init()

pygame.font.init()
FONT = pygame.font.Font("assets\Helvetica Neu Bold.ttf", 20)
ICON = pygame.image.load("assets\icon.png")

class UserInterface():
    WIDTH = 575
    HEIGHT = 800

    def __init__(self):
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption("Wordle (Fake)")
        pygame.display.set_icon(ICON)
        self.final_word = self.generate_word()
        self.grid = Grid()
        self.guess = 0
        self.letter_count = 0
        # print(self.final_word) # Test
        self.event_handler()

    def generate_word(self):
        # return "close" # Test
        return random.choice(WORDS)

    def check_real_word(self, word):
        return True if word in WORDS else False

    def display_message(self, text, end: bool):
        if end:
            text = "The word was {}. Better luck next time!".format(self.final_word)

        message_box = FONT.render(text, False, BLACK)
        self.screen.blit(message_box, (90, 620))
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.time.set_timer(pygame.USEREVENT, 500)

    def render(self):
        self.screen.fill(WHITE)
        self.grid.draw(self.screen)
        pygame.display.update()

    def event_handler(self):
        rules = Rules()
        running = True

        while running:
            if self.letter_count < 0:
                self.letter_count = 0
            elif self.letter_count > 4:
                self.letter_count = 4

            for event in pygame.event.get():
                # Player closes window
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # print(pygame.key.name(event.key) + " " + str(self.letter_count)) # Test
                    
                    if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        running = False
                        pygame.quit()
                        quit()

                    elif event.key == pygame.K_BACKSPACE:
                        self.grid.backspace()
                        if self.letter_count != 0:
                            self.letter_count -= 1

                    elif pygame.key.name(event.key) in LETTERS:
                        input_letter = pygame.key.name(event.key)
                        self.grid.enter_letter(input_letter)
                        self.letter_count += 1

                    elif pygame.key.name(event.key) not in LETTERS and event.key != pygame.K_RETURN:
                        self.display_message("Please input a letter", False)

                    elif event.key == pygame.K_RETURN:
                        if self.grid.current_col < 5:
                            self.display_message("Please input a 5-letter word", False)

                        self.letter_count = 0
                        guessed_word = self.grid.get_word().lower()
                        # Check if word is correct
                        if self.check_real_word(guessed_word) and self.grid.current_col == 5:
                            results = rules.check_colours(guessed_word, self.final_word)
                            self.grid.enter_word(results)
                            self.guess += 1
                            self.render() # Necessary placement

                        if not self.check_real_word(guessed_word) and self.grid.current_col == 5:
                            self.display_message("Not in word list", False)
                            pass

                        if guessed_word == self.final_word:
                            pygame.event.set_blocked([pygame.KEYDOWN, pygame.KEYUP])
                            self.display_message("Congrats!", False)

                        if self.guess == 6 and guessed_word != self.final_word:
                            self.display_message(None, True)

            # No more guesses left
            if self.guess > 5:
                self.render()

            self.render()

        pygame.quit()
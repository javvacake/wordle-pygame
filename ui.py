import pygame
import random
from words import *
# from wordle import Wordle
from grid import Grid
from letters import LETTERS
from colours import *

pygame.init()

pygame.font.init()
FONT = pygame.font.Font("helveticaneue\Helvetica Neu Bold.ttf", 20)

class UserInterface():
    WIDTH = 500
    HEIGHT = 700

    def __init__(self):
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption("Wordle (Fake)")
        self.final_word = self.generate_word()
        self.grid = Grid()
        self.guess = 0
        self.letter_count = 0
        print(self.final_word) # Test
        self.event_handler()

    def generate_word(self):
        return random.choice(WORDS)

    def check_real_word(self, word):
        return True if word in WORDS else False

    def error_message(self, text):
        message_box = FONT.render(text, False, BLACK)
        self.screen.blit(message_box, (90, 620))
        pygame.display.update()
        pygame.time.delay(500)

    def render(self):
        self.screen.fill(WHITE)
        self.grid.draw(self.screen)
        pygame.display.update()

    # TODO:
    def event_handler(self):
        running = True

        while running:
            if self.letter_count < 0:
                self.letter_count = 0

            for event in pygame.event.get():
                # Player closes window
                if event.type == pygame.QUIT:
                    print("Player chose to quit")
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    print(pygame.key.name(event.key) + " " + str(self.letter_count)) # Test

                    # if self.letter_count > 5:
                    #         self.error_message("1 Please input a 5-letter word")
                    #         pass #?

                    if event.key == pygame.K_BACKSPACE:
                        self.grid.backspace()
                        self.letter_count -= 1
                        # self.render()

                    elif pygame.key.name(event.key) in LETTERS:
                        print("In alphabet") # Test
                        self.letter_count += 1
                        if self.letter_count > 5: # Account for backspace
                            self.error_message("Out of space")

                        input_letter = pygame.key.name(event.key)
                        self.grid.enter_letter(input_letter)
                        # self.render()

                    elif pygame.key.name(event.key) not in LETTERS and event.key != pygame.K_RETURN:
                        self.error_message("Please input a letter")
                        print("Not in alphabet") # Test

                    elif event.key == pygame.K_RETURN:
                        if self.letter_count < 5:
                            self.error_message("2 Please input a 5-letter word")
                            # self.grid.backspace()

                        self.letter_count = 0
                        guessed_word = self.grid.get_word().lower()
                        # Check if word is correct
                        if self.check_real_word(guessed_word):
                            # Do the colour thing
                            print("valid word") # Test
                            # self.render()
                        else:
                            self.error_message("Word not in directory")
                            print("Word not in directory") # Test
                            pass

                        if self.final_word == guessed_word:
                            print("YAY") # Test
                            # self.render()
                    # else:
                    #     input_letter = pygame.key.name(event.key)
                    #     self.grid.enter_letter(input_letter)

            # No more guesses left
            if self.guess > 5:
                self.render()

            self.render() # TODO: throws traceback error

        pygame.quit()
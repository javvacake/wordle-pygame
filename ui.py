import pygame
from wordle import Wordle
from grid import Grid
from colours import WHITE

pygame.init()
pygame.font.init()
FONT = pygame.font.Font("helveticaneue\Helvetica Neu Bold.ttf", 20)

class UserInterface:
    WIDTH = 500
    HEIGHT = 700

    def __init__(self):
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.grid = Grid()
        self.guess = 1
        self.event_handler()

    def render(self):
        self.screen.fill(WHITE)
        self.grid.draw(self.screen)
        pygame.display.update()

    # TODO:
    def event_handler(self):
        running = True

        while running:
            for event in pygame.event.get():
                # Player closes window
                if event.type == pygame.QUIT:
                    print("Player chose to quit")
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.grid.backspace()
                    # elif event.key == pygame.K_RETURN:
                        # Check if word is correct
                        # If not...

            # No more guesses left
            if self.guess > 6:
                self.render()

            self.render() # TODO: throws traceback error

        pygame.quit()
        
#     screen.fill((255, 255, 255)) # Fill background with white
#     pygame.display.flip() # Flip the display? Acc turns it white
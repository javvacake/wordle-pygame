import random
from words import *

class Wordle:
    def __init__(self):
        self.word = self.generate_word()
        self.guess = 1

    def generate_word():
        return random.choice(WORDS)


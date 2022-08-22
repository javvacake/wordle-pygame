from colours import *

class Rules:
    def __init__(self):
        self.final_word = [None] * 5
        self.guessed_word = [None] * 5
        self.colour_results = [None] * 5
        self.instances_of_letter = [None] *5

    def str_to_array(self, word):
        return list(word)

    def check_colours(self, guessed_word, final_word):
        self.colour_results = [None] * 5
        self.guessed_word = self.str_to_array(guessed_word)
        self.final_word = self.str_to_array(final_word)

        remaining_guessed_letters = self.guessed_word
        remaining_final_letters = self.final_word

        for index, letter in enumerate(self.guessed_word):
            if (self.guessed_word[index] == self.final_word[index]):
                remaining_final_letters[index] = ""
                remaining_guessed_letters[index] = ""
                self.colour_results[index] = "GREEN"
            else:
                self.colour_results[index] = "GREY"

        for index, letter in enumerate(self.guessed_word):
            if ((remaining_guessed_letters[index] in remaining_final_letters) and (self.guessed_word[index] != self.final_word[index])):
                new_index = remaining_final_letters.index(self.guessed_word[index])
                remaining_final_letters[new_index] = ""

                remaining_guessed_letters[index] = ""
                self.colour_results[index] = "YELLOW"

        return self.colour_results
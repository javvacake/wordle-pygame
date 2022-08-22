from colours import *

class Rules:
    def __init__(self):
        self.final_word = [None] * 5
        self.guessed_word = [None] * 5
        self.colour_results = [None] * 5

    def str_to_array(self, word):
        return list(word)

    def check_colours(self, guessed_word, final_word):
        self.guessed_word = self.str_to_array(guessed_word)
        self.final_word = self.str_to_array(final_word)

        for guessed_pos, letter in enumerate(self.guessed_word):
            # print(guessed_pos) # Test
            for final_pos, char in enumerate(self.final_word):
                # print(final_pos) # Test

                # Green tile
                if letter == char and guessed_pos == final_pos:
                    self.colour_results[guessed_pos] = "GREEN"
                    print("green ", letter) # Test
                    break

                # Yellow tile
                if letter == char and guessed_pos != final_pos:
                    self.colour_results[guessed_pos] = "YELLOW"
                    print("yellow ", letter) # Test
                    
                    print(guessed_pos, " ", final_pos)
                    if final_pos != 4:
                        break
                    else:
                        continue

                # Grey tile
                if letter != char:
                    if self.colour_results[guessed_pos] == "YELLOW":
                        break

                    self.colour_results[guessed_pos] = "GREY"
                    print("grey ", letter) # Test

        return self.colour_results
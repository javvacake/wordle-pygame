from colours import *

class Rules:
    def __init__(self):
        self.final_word = [None] * 5
        self.guessed_word = [None] * 5
        self.colour_results = [None] * 5
        self.instances_of_letter = [None] *5

    def str_to_array(self, word):
        return list(word)

    # Count instances of each letter so if an input word has 2 of the same letter and
    # the final_word has only 1 instance of the letter, only 1 of the letters is highlighted
    def count_instances():
        pass

    def check_colours(self, guessed_word, final_word):
        self.colour_results = [None] * 5
        self.guessed_word = self.str_to_array(guessed_word)
        self.final_word = self.str_to_array(final_word)

        for guessed_pos, letter in enumerate(self.guessed_word):
            # print(guessed_pos) # Test
            # print("Guessed letter: ", self.guessed_word[guessed_pos]) # Test

            for final_pos, char in enumerate(self.final_word):
                print("Guessed letter: {} and Final letter: {}".format(self.guessed_word[guessed_pos], self.final_word[final_pos])) # Test

                # Green tile
                if letter == char and guessed_pos == final_pos:
                    self.colour_results[guessed_pos] = "GREEN"
                    print("green ", letter) # Test
                    break

                # Yellow tile
                if letter == char and guessed_pos != final_pos:
                    print("Entering yellow")
                    self.colour_results[guessed_pos] = "YELLOW"
                    print("yellow ", letter) # Test
                    
                    # TODO: cannot for the life of me solve this.
                    # where guessed = pants and target = socks, s is stil yellow.
                    # Completed maybe?
                    print(guessed_pos, " fp:", final_pos)
                    if final_pos != 4:
                        # print("cont")
                        continue
                    else:
                        # print("break")
                        break

                # Grey tile
                if letter != char:
                    # print("Entering grey")
                    if self.colour_results[guessed_pos] == "YELLOW":
                        print("Breaking with {} at {} and colour of {}".format(self.final_word[final_pos], guessed_pos,self.colour_results[guessed_pos]))
                        continue # Was `break`

                    self.colour_results[guessed_pos] = "GREY"
                    print("grey ", letter) # Test

                # for i, let in enumerate(self.guessed_word): # Test
                #     print(let, " ", self.colour_results[i])

        return self.colour_results
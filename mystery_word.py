# import choice from random library
from random import choice

# global constant, read file 
NUM_TURNS = 8
WORDS_FILE = "words.txt"

# set up modes
easy_mode_words = []
normal_mode_words = []
hard_mode_words = []

with open(WORDS_FILE, 'r') as game_data:
   for line in game_data:
       if len(line) == 4 or len(line) <= 6:
           easy_mode_words.append(line)
       if len(line) == 6 or len(line) <= 8:
           normal_mode_words.append(line)
       if len(line) >= 8:
            hard_mode_words.append(line)

#print(easy_mode_words)

# game list
userlevel = input("please select level: 1 for Easy, 2 for Normal, 3 for Hard:")
if userlevel == 1
game_list == easy_mode_words
elif userlevel == 2
game_list == normal_mode_words
elif userlevel == 3
game_list == hard_mode_words

# select word to play
word_to_play = choice(game_list)
print(f"the word has{len(word_to_play)}")




if __name__ == "__main__":
    main()




        
       
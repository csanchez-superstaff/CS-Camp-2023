# IMPORT MODULES

import random
import string
from WORDS import words
from VISUALS import snowman

# FUNCTION NAME: get_valid_word
# PARAMETERS: words
# DESCRIPTION: gets rid of words containing "-" or " "

def get_valid_word(words):

    word = random.choice(words)
    
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

# FUNCTION NAME: play
# PARAMETERS: none
# DESCRIPTION: lets the user play "snowman" when called

def play():

    # VARIABLES

    # word to guess
    word = get_valid_word(words)
    # letters in the word
    word_letters = set(word)
    # guessed letters
    used_letters = set()
    # valid letters
    alphabet = set(string.ascii_uppercase)
    # number of attempts
    lives = 7

    # GAME LOOP
    while len(word_letters) > 0 and lives > 0:

        # print lives       
        print("You have", lives, "lives left!")

        # print used letters separated by " " using join()
        print("You have used these letters: ", " ".join(used_letters))

        # print snowman visuals
        print(snowman[lives])

        # declare empty list to store the letters in word      
        word_list = []

        # go through each letter in word
        for letter in word:
            # add guessed letters
            if letter in used_letters:
                word_list += letter
            # add "-" for every letter not guessed
            else:
                word_list += "-"

        # print letters of word (hidden and uncovered)
        print('Current word: ', ' '.join(word_list))

        # USER INPUT

        # prompt user input
        user_letter = input('Guess a letter: ').upper()

        # validate input (in alphabet and not a repeat)
        if user_letter in alphabet - used_letters:
            
            # add letter to used_letters
            used_letters.add(user_letter)
            
            # input is part of word
            if user_letter in word_letters:

                # remove letter from word_letters
                word_letters.remove(user_letter)
                # print message
                print("\nGood Job!")

            # user input isn't part of word
            else:

                # remove 1 live
                lives = lives - 1
                # print message
                print('\nYour letter,', user_letter, 'is not in the word.')

        # user input is a repeat
        elif user_letter in used_letters:
            
            print('\nYou have already used that letter. Guess another letter.')

        # invalid input
        else:
            
            print('\nThat is not a valid letter.')

    # RESULTS

    # lost all lives
    if lives == 0:
        
        print(snowman[lives])
        print('The snowman melted, sorry. The word was', word)
    
    # word guess correctly
    else:
        
        print('YAY! You guessed the word', word, '!!')

# START PLAYING (call play function)
play()
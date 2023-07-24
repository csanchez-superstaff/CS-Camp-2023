# IMPORT MODULES

# FUNCTION NAME: get_valid_word
# PARAMETERS: words
# DESCRIPTION: gets rid of words containing "-" or " "

# FUNCTION NAME: play
# PARAMETERS: none
# DESCRIPTION: lets the user play "snowman" when called

    # VARIABLES

    # word to guess
    
    # letters in the word
    
    # guessed letters
    
    # valid letters
    
    # number of attempts
    

    # GAME LOOP
    
        # print lives

        # print used letters separated by " " using join()

        # print snowman visuals
        
        # declare empty list to store the letters in word       

        # go through each letter in word
    
            # add guessed letters to list

            # add "-" to list for every letter not guessed

        # print letters of word (hidden and uncovered)

        # USER INPUT

        # prompt user input

        # validate input (in alphabet and not a repeat)
            
            # add letter to used_letters
                    
            # input is part of word
                
                # remove letter from word_letters 
                
                # print message

            # user input isn't part of word

                # remove 1 live
                
                # print message

        # user input is a repeat
            
        # invalid input

    # RESULTS

    # lost all lives
    
    # word was guess correctly

# START PLAYING (call play function)

# START YOUR CODE HERE - SECTION 2

# function name: print_board
# parameters: board

# function name: winner
# parameters: board, player

# function name: win_conditions
# parameters: board

# END YOUR CODE HERE

def play():

    # START YOUR CODE HERE - SECTION 1

    # variables: player, turn, board

    # END YOUR CODE HERE

    # game loop
    while True:

        # START YOUR CODE HERE - SECTION 3

        # print board

        # prompt user input

        # END YOUR CODE HERE

        # validate input
        if not move.isdigit() or int(move) >= 10 or int(move) < 1:
            print("Invalid input. Enter a number from 1-9")
            continue
        
        # validate plays
        if board[move] == " ":
            board[move] = player
            turn += 1
        else:
            print("That spot is filled. Try another spot")
            continue
        
        # START YOUR CODE HERE - SECTION 4
        
        # check for winner

        # check for tie
        
        # change player

        # END YOUR CODE HERE

# start playing
play()
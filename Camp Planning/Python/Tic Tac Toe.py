def print_board(board):
    
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])

def winner(board, player):
    
    print_board(board)
    print("Game Over")
    print(player + " wins!")

def win_combination(board):

    # horizontal
    if board["7"] == board["8"] == board["9"] != " ":
        return True
    elif board["4"] == board["5"] == board["6"] != " ":
        return True
    elif board["1"] == board["2"] == board["3"] != " ":
        return True

    # vertical
    elif board["7"] == board["4"] == board["1"] != " ":
        return True
    elif board["8"] == board["5"] == board["2"] != " ":
        return True
    elif board["9"] == board["6"] == board["3"] != " ":
        return True

    # diagonal
    elif board["7"] == board["5"] == board["3"] != " ":
        return True
    elif board["1"] == board["5"] == board["9"] != " ":
        return True
    
    # no winner yet
    else: 
        return False

def play():

    # variables
    player = "X"
    turn = 0
    board = {"7": " " , "8": " " , "9": " " ,
            "4": " " , "5": " " , "6": " " ,
            "1": " " , "2": " " , "3": " " }
    
    # game loop
    while True:

        # print board
        print_board(board)

        # prompt user input
        move = input(player + " it's your turn!\n")

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

        # check for winner
        if win_combination(board):
            winner(board, player)
            break

        # tie
        if turn >= 9:
            print("Game Over")             
            print("It's a Tie!!")
            break
        
        # change player
        if player == "X":
            player = "O"
        else:
            player = "X"

# start playing
play()
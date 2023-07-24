import random

def play():
    
    user = input("Enter 'rock', 'paper', or 'scissors'\n")
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == "END":
        return user
    
    if user != "rock" and user != "paper" and user != "scissors":
        return "That is not fair"

    print(computer)

    # TIE
    if user == computer:
        return "Tie!"

    # PLAYER WINS
    if user == 'rock' and computer == 'scissors':
        return "You Win!"

    if user == 'paper' and computer == 'rock':
        return "You Win!"

    if user == 'scissors' and computer == 'paper':
        return "You Win!"

    # COMPUTER WINS
    else: 
        return "You Lose!"
    
while True:
    result = play()
    if result == "END":
        print("Good Game!")
        break
    print(result)
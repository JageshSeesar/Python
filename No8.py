print("**************************************************************************")
print("WELCOME TO THE ROCK-PAPER-SCISSORS GAME")
print("**************************************************************************")
choice = input("Press Y to continue: ")

while choice:
        player1 = input("Player 1 | Enter either :- rock, paper or scissors -->")
        player2 = input("Player 2 | Enter either :- rock, paper or scissors -->")

        if player1 == player2:
            print("DRAW! Try Again")
        elif (player1 == "rock") and (player2 == "scissors"):
            print("Player 1 Wins")
        elif (player2 == "rock") and (player1 == "scissors"):
            print("Player 2 Wins")

        elif (player1 == "scissors") and (player2 == "paper"):
            print("Player 1 Wins")
        elif (player2 == "scissors") and (player1 == "paper"):
            print("Player 2 Wins")

        elif (player1 == "paper") and (player2 == "rock"):
            print("Player 1 Wins")
        elif (player2 == "paper") and (player1 == "rock"):
            print("Player 2 Wins")
        else:
            print("*******************************************")
            print("Invalid game word| Reason:")
            print("1. game word was entirely wrongly written")
            print("2. game word was not in lowercase")
            print("*******************************************")

        choice = input("Do you want to play again ? enter Y or N: ")
        if choice == 'n' or choice == 'N':
            break

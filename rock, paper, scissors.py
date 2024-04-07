import random

def play_game():
    myList = ["Rock", "Paper", "Scissors"]
    z = random.choice(myList)

    while True:
        try:
            player = input("Rock, Paper or Scissors?: ").strip().capitalize()
            if player not in myList:
                raise ValueError("Invalid input. Please choose Rock, Paper, or Scissors.")
            break
        except ValueError as ve:
            print("Errorrrrz")

    if player.lower() == z.lower():
        print("It's a tie!")
    elif player == "Rock":
        if z == "Scissors":
            print("You win! Rock smashes Scissors.")
        else:
            print("You lose! Paper covers Rock.")
    elif player == "Paper":
        if z == "Rock":
            print("You win! Paper covers Rock.")
        else:
            print("You lose! Scissors cuts Paper.")
    elif player == "Scissors":
        if z == "Paper":
            print("You win! Scissors cuts Paper.")
        else:
            print("You lose! Rock smashes Scissors.")

    print("Your choice:", player)
    print("Computer's choice:", z)

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes" and play_again != "y":
        break
print("Thank you for playing!")
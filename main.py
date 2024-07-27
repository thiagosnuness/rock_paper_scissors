# Rock, paper, scissors

import random
from replit import clear
from rock_paper_scissors_art import rock, paper, scissors

game_images = [rock, paper, scissors]
clear()
user_choice = int(input("What do you choose?Type 0 for Rock, 1 for Paper or 2 \
for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

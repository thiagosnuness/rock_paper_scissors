"""
main.py

Entry point for the Rock, Paper, Scissors game.

This module initializes the game and manages the game loop.
It prompts the user to play a game of Rock, paper, scissors and continues
to run until the user decides to quit.
"""

from replit import clear

from game import Game


def main():
    """
    Run the Rock, Paper, Scissors game.

    Clears the console, and prompts the user to start a new game.
    The user can play multiple rounds of Rock, Paper, Scissors
    until they choose to exit.
    """
    clear()
    while True:
        user_choice = get_user_choice()
        if user_choice == 9:
            break

        game = Game(user_choice)
        game.determine_winner()


def get_user_choice():
    """
    Prompt the user to enter their choice.

    Returns:
        int: The user's choice.
    """
    while True:
        try:
            user_choice = int(input(
                "\nType 0 for Rock, 1 for Paper or 2 for Scissors, "
                "and 9 for exit.\nWhat do you choose? "
            ))
            if user_choice in (0, 1, 2, 9):
                return user_choice
            else:
                print("\nInvalid input. Please enter '0', '1', '2' or '9'.")
        except ValueError:
            print("\nInvalid input. Please enter '0', '1', '2' or '9'.")


if __name__ == "__main__":
    main()

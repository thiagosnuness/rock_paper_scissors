"""
game.py

This module defines the Game class, which represents a game of
Rock, Paper, Scissors. The game logic includes user input handling,
random selection for the computer's move, and determining the winner based
on standard Rock, Paper, Scissors rules.
"""

import random
from art import rock, paper, scissors


class Game:
    """
    Represents a game of Rock, Paper, Scissors.

    Attributes:
        __logos (list): The logos used in the game.
        __user_choice (int): The user choice in the game.
        __computer_choice (int): The random computer choice in the game.
    """
    def __init__(self, user_choice):
        """
        Initialize the game with two players and their choices.

        Args:
            user_choice (int): The user choice in the game.
        """
        self.__logos = [rock, paper, scissors]
        self.__user_choice = user_choice
        self.__computer_choice = random.randint(0, 2)

    def get_logo(self, choice):
        """
        Get the logo for the given choice.

        Args:
            choice (int): The choice (0 for Rock, 1 for Paper, 2 for Scissors).

        Returns:
            str: The logo for the given choice.
        """
        return self.__logos[choice]

    def determine_winner(self):
        """
        Determine and display the winner of the game based on
        the Rock, Paper, Scissors game rule.
        """
        print(f"\nUser: \n{self.get_logo(self.__user_choice)}")
        print(f"\nComputer: \n{self.get_logo(self.__computer_choice)}")
        if self.__user_choice == 0 and self.__computer_choice == 2:
            print("\nYou win!")
        elif self.__computer_choice == 0 and self.__user_choice == 2:
            print("\nYou lose")
        elif self.__computer_choice > self.__user_choice:
            print("\nYou lose")
        elif self.__user_choice > self.__computer_choice:
            print("\nYou win!")
        elif self.__computer_choice == self.__user_choice:
            print("\nIt's a draw")

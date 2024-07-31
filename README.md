# Rock, Paper, Scissors Game

Rock, Paper, Scissors is a classic hand game that is often played between two people. This project is an implementation of the game in Python, allowing a user to play against the computer.

## Project Structure

The project is organized into several files:

- **`main.py`**: The entry point that initializes and runs the game.
- **`game.py`**: Contains the `Game` class with the main logic for Rock, Paper, Scissors.
- **`art.py`**: Contains the ASCII art for the game's logos.

## How to Run

### Requirements

- Python 3.x

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/thiagosnuness/rock_paper_scissors.git
    cd rock_paper_scissors
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

3. Follow the on-screen instructions to play.

## Code Overview

### `main.py`

This script is the entry point for the game. It runs the game and handles user interactions.

- **Functionality**:
  - Clears the console.
  - Prompts the user to start a new game.
  - Handles multiple rounds of Rock, Paper, Scissors until the user chooses to exit.
  - Validates user input to ensure valid choices are made.

### `game.py`

This file defines the `Game` class, which manages the game flow, including:

- **Attributes**:
  - `__logos`: List of ASCII art for the game choices (Rock, Paper, Scissors).
  - `__user_choice`: The choice made by the user.
  - `__computer_choice`: The choice made by the computer (randomly selected).

- **Methods**:
  - `__init__(self, user_choice)`: Initializes the game with the user's choice and a random computer choice.
  - `get_logo(self, choice)`: Returns the ASCII art for the given choice.
  - `determine_winner(self)`: Determines and displays the winner based on standard Rock, Paper, Scissors rules.

### `art.py`

This file contains the ASCII art for the Rock, Paper, Scissors logos.

- **Logos**:
  - `rock`: ASCII art for Rock.
  - `paper`: ASCII art for Paper.
  - `scissors`: ASCII art for Scissors.

## Contributing

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

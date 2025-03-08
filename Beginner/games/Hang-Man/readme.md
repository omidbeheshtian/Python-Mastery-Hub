# Hangman(Word Guessing Game)

This is a simple word-guessing game written in Python. The program randomly selects a word from a predefined list, and the player must guess the word one letter at a time.

## How to Play

1. The game starts by displaying a series of dashes (`-`), representing the hidden word.
2. The player is prompted to enter a single letter.
3. If the guessed letter is in the word, it is revealed in its correct position.
4. If the guessed letter is incorrect, the number of remaining attempts decreases.
5. The game continues until:
   - The player successfully guesses the word (wins).
   - The player runs out of attempts (loses).
6. If the player loses, the correct word is displayed.

## Features

- Random word selection from a list
- Case-insensitive input handling
- Prevents duplicate guesses
- Displays remaining attempts
- Provides clear feedback to the player

## Requirements

- Python 3.x

## How to Run

1. Save the script as `hangman.py`.
2. Open a terminal or command prompt.
3. Navigate to the script's directory.
4. Run the script using:

   ```sh
   python hangman.py

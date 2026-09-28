# game.py
# Handles the number guessing game

import random


def play_guessing_game():
    """Play a number guessing game with limited attempts."""

    secret_number = random.randint(1, 10)
    attempts = 3

    print("Assistant: I'm thinking of a number between 1 and 10.")
    print(f"Assistant: You have {attempts} attempts.")

    for attempt in range(1, attempts + 1):

        try:
            guess = int(input(f"You (Attempt {attempt}): "))

            if guess < 1 or guess > 10:
                print("Assistant: Please enter a number between 1 and 10.")
                continue

            if guess == secret_number:
                print("Assistant: Congratulations! You guessed it!")
                return

            elif guess < secret_number:
                print("Assistant: Too low!")

            else:
                print("Assistant: Too high!")

        except ValueError:
            print("Assistant: Please enter a valid number.")

    print(f"Assistant: Game over! The number was {secret_number}.")
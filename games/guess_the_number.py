"""
guess_the_number.py

A simple number guessing game where the player tries to guess a randomly selected number within a certain range.

Author: Rachid Sahli
Date: 2025-08-04
"""

import random


def play():
    """
    
    Runs one round of the number guessing game.
    Generates a random number and allows the user up to 7 attempts.
    """
    MAX_ATTEMPTS = 7
    attempts = 0
    mystery_number = random.randint(1, 100)

    print('\n-- Guess the mystery number! --')
    print('The mystery number is between 1 and 100.')
    print(f'You have {MAX_ATTEMPTS} chances.\n')

    while attempts < MAX_ATTEMPTS:
        try:
            user_number = int(input('Enter a number: '))
            while user_number not in range(1, 101):
                user_number = int(input('Enter a number between 1 and 100: '))
        except ValueError:
            print('Please enter a valid number.')
            continue

        if user_number == mystery_number:
            print("Well done! You've found the mystery number!")
            break
        elif user_number < mystery_number:
            print("Too small! Try again.")
        else:
            print("Too big! Try again.")

        attempts += 1
        print(f"Remaining attempts: {MAX_ATTEMPTS - attempts}\n")

    if attempts == MAX_ATTEMPTS:
        print(f"Game over! The mystery number was {mystery_number}.")


def main():
    while True:
        play()
        replay = input('Do you want to play again? (y/n): ').strip().lower()
        if replay != 'y':
            print('Thanks for playing! See you next time.')
            break


if __name__ == "__main__":
    main()

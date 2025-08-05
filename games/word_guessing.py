"""
word_guessing.py

A simple game consisting of guessing a randomly selected word.

Author: Rachid Sahli
Date: 2025-08-05
"""

import random

def play():
    """
    
    Runs one round of the word guessing game.
    Selects a random word and allows the user up to 12 attempts.
    """

    MAX_ATTEMPTS = 12
    attempts = 0
    guesses = []

    WORDS = ['computer', 'science', 'cool', 'banana', 'tennis',
             'python', 'water', 'tower', 'car', 'mathematics',
             'programming', 'backpack', 'door']
    mystery_word = random.choice(WORDS)

    print('\n-- Guess the mystery word! --')
    name = input('What is your name? : ')
    print(f'Good luck {name}! You have {MAX_ATTEMPTS} chances.\n')

    while attempts < MAX_ATTEMPTS:
        while True:

            for i in mystery_word:
                if i in guesses:
                    print(i, end=' ')
                else:
                    print('_', end=' ')
            print('\n')

            print(f'{attempts} / {MAX_ATTEMPTS} mistakes.\n')

            user_guess = input('Enter a character : ').replace(' ','').lower()
        
            if len(user_guess) != 1:
                print('\nEnter a unique character.')
                continue

            if not user_guess.isalpha():
                print('That\'s not a letter. Please try again.')
                continue
            
            break
        
        if user_guess in mystery_word:
            print('Well done, you just found a letter.')
            guesses.append(user_guess)
        
        elif user_guess not in mystery_word:
            print(f'Wrong, {user_guess} is not in the mystery word.')
            attempts += 1
        
        if all(c in guesses for c in mystery_word):
            print('You won. The mystery word was :', mystery_word)
            break
        
        if attempts == MAX_ATTEMPTS:
            print('Too bad, the mystery word was :', mystery_word)
            break


def main():
    while True:
        play()
        replay = input('Do you want to play again? (y/n): ').strip().lower()
        if replay != 'y':
            print('Thanks for playing! See you next time.')
            break

if __name__ == '__main__':
    main()
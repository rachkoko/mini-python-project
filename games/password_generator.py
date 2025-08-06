"""
password_generator.py

A program that generates a random password.

Author: Rachid Sahli
Date: 2025/08/06
"""

import random
import string

def ask_int(question, min_value=1):
    """
    Ask the user for an integer greater than or equal to min_value.
    """
    while True:
        try:
            value = int(input(question))
            if value < min_value:
                print(f"Error! The value must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("Error! Please enter a valid length.")


def ask_yes_no(question):
    """
    Ask the user for a "y" or "n" answer.
    """
    while True:
        value = input(question).lower()
        if value not in ["y", "n"]:
                print("Error! Answer with y or n.")
                continue
        return value


def get_possible_characters(cap, low, spec, dig):
    """
    Return a string of characters based on user's choices.
    """
    chars = ""
    if cap == "y":
         chars += string.ascii_uppercase
    if low == "y":
         chars += string.ascii_lowercase
    if spec == "y":
         chars += string.punctuation
    if dig == "y":
         chars += string.digits
    return chars
     

def generate_password():
    """
    Generates a password based on criteria chosen by the user.
    """
    length_p = ask_int("\nWhat is the desired length of the password?: ", min_value=9)
    cap = ask_yes_no("Include capital letters? (y/n): ")
    low = ask_yes_no("Include lowercase letters? (y/n): ")
    spec = ask_yes_no("Include special characters? (y/n): ")
    dig = ask_yes_no("Include numbers? (y/n): ")

    chars = get_possible_characters(cap, low, spec, dig)

    if not chars:
        print("\nError: No characters selected, password cannot be generated.")
        return None
    
    password_user = "".join(random.choice(chars) for _ in range(length_p))
    return f"Password: {password_user}"


def main():
    while True:
        result = generate_password()
        if result:
            print(result)
        else:
            break
        regenerate = ask_yes_no("\nDo you want to reset your password? (y/n): ")
        if regenerate != "y":
            print("Thank you, see you soon.")
            break

if __name__ == "__main__":
     main()
"""
Generate a random magic number between 0 and 10.
Keep asking the user to guess the number until they guess correctly.
After each guess, print whether the guess was too high, too low, or correct.
The user should have a maximum of 3 guesses.
"""
from random import randint

magic_num = randint(0, 10)
is_correct = False
guesses = 3

while not is_correct and guesses > 0:
    user_input = int(input("Guess the number: "))

    if user_input == magic_num:
        is_correct = True
    elif user_input > magic_num:
        print("Too high!")
    else:
        print("Too low!")

    guesses -= 1

print("Correct!" if is_correct else f"Game Over! The number was {magic_num}.")

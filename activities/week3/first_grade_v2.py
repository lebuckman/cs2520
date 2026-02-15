"""
If the first integer is less than the second, swap them (avoid negatives)
"""
from random import randint

number1, number2 = randint(0, 9), randint(0, 9)

if (number1 < number2):
    number1, number2 = number2, number1

user_answer = int(input(f"What is {number1} - {number2}? "))
is_correct = user_answer == number1 - number2

print("Correct!" if is_correct else "Wrong!")

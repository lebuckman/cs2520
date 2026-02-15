"""
Randomly generate two single-digit integers
Prompt the student to enter an answer
Display a message to indicate whether the answer is true or false
"""
from random import randint

number1 = randint(0, 9)
number2 = randint(0, 9)

user_answer = int(input(f"What is {number1} + {number2}? "))
is_correct = user_answer == number1 + number2

print("Correct!" if is_correct else "Wrong!")

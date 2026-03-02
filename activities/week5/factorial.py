"""
Create a program that calculates the factorial of a positive integer.
"""

factorial = int(input("Enter a positive integer: "))
count = factorial - 1

print(f"Factorial of {factorial}!: ", end="")

while count >= 1:
    factorial *= count
    count -= 1

print(factorial)

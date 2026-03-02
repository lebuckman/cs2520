"""
Create a program that calculates the greatest common divisor (GCD) of 
two positive integers using Euclid's algorithm.
"""

num_a = int(input("Enter first positive integer: "))
num_b = int(input("Enter second positive integer: "))

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b
    else:
        num_b = num_b - num_a

print(f"GCD is {num_a}")

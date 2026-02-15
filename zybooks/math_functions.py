""" Output x^z, x^(y^z), |x-y| , and the square root of x^z. """
import math

x = float(input("Enter a value for x: "))
y = float(input("Enter a value for y: "))
z = float(input("Enter a value for z: "))

print(f"x^z: {x ** z:.2f}")
print(f"x^(y^z): {x ** (y ** z):.2f}")
print(f"|x-y|: {math.fabs(x - y):.2f}")
print(f"√(x^z): {math.sqrt(x ** z):.2f}")

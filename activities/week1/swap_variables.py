"""
Swap the values of two variables. ("Java way")
"""
num1 = 10
num2 = 20

print(f"Before swap: num1 = {num1}, num2 = {num2}")

temp = num1
num1 = num2
num2 = temp

print(f"After swap: num1 = {num1}, num2 = {num2}")


"""
Swap the values of two variables. ("Pythonic way" -> Tuple unpacking)
"""
num1 = 10
num2 = 20

print(f"Before swap: num1 = {num1}, num2 = {num2}")

num1, num2 = num2, num1

print(f"After swap: num1 = {num1}, num2 = {num2}")

"""
If a number is divisible by 3 only, print "Fizz"
If a number is divisible by 5 only, print "Buzz"
If a number is divisible by both 3 and 5, print "FizzBuzz"
Otherwise, print the number itself.
"""
user_input = int(input("Enter an integer: "))

if user_input % 15 == 0:
    print("FizzBuzz")
elif user_input % 3 == 0:
    print("Fizz")
elif user_input % 5 == 0:
    print("Buzz")
else:
    print(user_input)

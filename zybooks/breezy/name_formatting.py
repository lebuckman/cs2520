"""
Write a program that reads a person's name and formats as follows: firstName middleName lastName

ex: Pat Silly Doe -> Doe, P.S.
ex: Julia Clark -> Clark, J.
"""

name = input("Enter your name: ").split()

if len(name) == 2:
    first, last = name
    print(f"{last}, {first[0]}.")
elif len(name) == 3:
    first, middle, last = name
    print(f"{last}, {first[0]}.{middle[0]}.")
else:
    print("Invalid input.")


"""
Alternatively:

name = input("Enter your name: ").split()
initials = "".join(f"{part[0]}." for part in name[:-1])
print(f"{name[-1]}, {initials}")

"""

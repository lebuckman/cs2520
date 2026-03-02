"""
Write a program that takes in a line of text as input, and outputs that line of text in reverse.
The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.
"""
text = input("Enter text to reverse (or 'Done' to exit): ")

while text.lower() not in "done":
    reversed_text = text[::-1]
    print(f"Reversed: {reversed_text}")
    text = input("Enter text to reverse (or 'Done' to exit): ")

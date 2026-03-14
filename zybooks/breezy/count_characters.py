"""
Write a program whose input is a string which contains a character and a phrase, 
and whose output indicates the number of times the character appears in the phrase

ex: n Monday -> 1 n
ex: z Today is Monday -> 0 z's
"""

user_input = input()
char = user_input[0]
phrase = user_input[2:]

count = phrase.count(char)

if count == 1:
    print(f"1 {char}")
else:
    print(f"{count} {char}'s")

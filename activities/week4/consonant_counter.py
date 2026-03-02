VOWELS = "aeiou"

user_input = input("Enter a string: ")
consonant_count = 0

for char in user_input.lower():
    if char.isalpha() and char not in VOWELS:
        consonant_count += 1

print(f"\"{user_input}\" has {consonant_count} consonants")

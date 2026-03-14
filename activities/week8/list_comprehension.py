""" Convert all words in the list to uppercase """

words = ["python", "java", "c++", "javascript"]

words = [word.upper() for word in words]

print(words)


""" Given a list of words, create a new list containing only the words with > 4 letters """

words = ["apple", "cat", "banana", "dog", "elephant", "bat"]

words = [word for word in words if len(word) > 4]

print(words)

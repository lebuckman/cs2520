"""
Write an algorithm to determine if a given string is a palindrome. 
Assume the input string is case-sensitive and non-empty.
"""


def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("madam"))   # True
print(is_palindrome("Madam"))   # False
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))   # False


"""
Alternatively (without slicing):

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

"""

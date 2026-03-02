def is_in(str1, str2):
    if not str1 or not str2:
        return False

    return (str1 in str2) or (str2 in str1)


print(is_in("cat", "concatenate"))  # True
print(is_in("pencil", "pen"))       # True
print(is_in("dog", "god"))          # False
print(is_in("", "cat"))             # False
print(is_in("cat", "")) 	        # False

"""
Alternatively:

def is_in(str1, str2):
    both_non_empty = bool(str1 and str2)
    one_in_other = str1 in str2 or str2 in str1
    
    return both_non_empty and one_in_other
"""
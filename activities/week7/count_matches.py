"""
Write an algorithm to count the number of matches of a pattern in a given text.
"""


def count_substring(string, sub_string):
    n = len(string)
    m = len(sub_string)
    count = 0

    for i in range(n - m + 1):
        for j in range(m):
            if string[i + j] != sub_string[j]:
                break
        else:
            count += 1

    return count


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)

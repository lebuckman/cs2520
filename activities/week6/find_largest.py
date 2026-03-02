""" Use of max() is not allowed in this problem. """


def find_largest(arr):
    if not arr:
        return None

    maxval = arr[0]
    for num in arr:
        if num > maxval:
            maxval = num

    return maxval


print(find_largest([3, 1, 4, 1, 5, 9]))
print(find_largest([]))

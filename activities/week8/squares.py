numbers = [10, 25, 30, 45, 60, 75, 90]


def square_10_multiples(arr):
    result = []
    for num in arr:
        if num % 10 == 0:
            result.append(num ** 2)

    return result


print(square_10_multiples(numbers))


""" Alternatively """
result = [num ** 2 for num in numbers if num % 10 == 0]
print(result)

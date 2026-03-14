from functools import reduce

""" Given the list, keep only numbers > 30 and divisible by 5 """

numbers = [10, 25, 30, 45, 60, 75, 90]

result = filter(lambda x: x > 30 and x % 5 == 0, numbers)
# result = [num for num in numbers if num > 30 and num % 5 == 0]

print(list(result))  # [45, 60, 75, 90]


""" Given the list, create a new list that contains the squares of only numbers divisible by 10 """

numbers = [5, 12, 17, 20, 33, 40, 55, 60]

mod_ten = filter(lambda x: x % 10 == 0, numbers)
square_mod_ten = map(lambda x: x ** 2, mod_ten)
# result = [num ** 2 for num in numbers if num % 5 == 0]

print(list(square_mod_ten))  # [400, 1600, 3600]


""" Given the list, find the largest number using reduce() """

numbers = [15, 3, 27, 9, 42, 8]

maximum = reduce(lambda x, y: x if x > y else y, numbers)

print(maximum)


""" Given the list, using reduce(), find total number of characters in words combined """

words = ["Python", "is", "powerful", "and", "simple"]  # 25

total_len = reduce(lambda total, word: total + len(word), words, 0)

print(total_len)

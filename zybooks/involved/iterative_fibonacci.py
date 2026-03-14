"""Write an algorithm to compute the nth Fibonacci number using an iterative approach."""


def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(2))  # 1
print(fibonacci(7))  # 13
print(fibonacci(10))  # 55

# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

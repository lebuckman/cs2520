"""Write an algorithm to compute the nth Fibonacci number using an iterative approach."""


def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    n1, n2 = 0, 1
    count = 2
    while count <= n:
        nth = n1 + n2
        n1, n2 = n2, nth
        count += 1

    return n2


print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(7))  # 13
print(fibonacci(10)) # 55

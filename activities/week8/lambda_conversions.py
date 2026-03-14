def add_and_square(a, b):
    return (a + b) ** 2


def check_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


def calculate_price(price, is_member):
    if is_member:
        discount = 0.20
    else:
        discount = 0.05
    return price - (price * discount)


""" Convert the above functions into lambda functions """

add_and_square = lambda a, b: (a + b) ** 2

check_even = lambda n: "Even" if n % 2 == 0 else "Odd"

calculate_price = lambda price, is_member: price - (price * (.20 if is_member else .05))
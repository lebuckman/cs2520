""" 
Trace code to better understand how Python handles 
variable scope and function definitions. 
"""


def f(x):
    def g():
        x = "abc"
        print(f"from g, x = {x}")

    def h():
        z = x
        print(f"form h, z = {z}")
    x = x + 1
    print(f"from x, x = {x}")
    h()
    g()
    print(f"from x, x = {x}")
    return g


x = 3
z = f(x)
print(f"x = {x}")
print(f"z = {z}")
z()

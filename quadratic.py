# Replace the "ANSWER HERE" for your answer

import math
def roots(a, b, c):
    discriminante= b**2 - 4*a*c
    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante)) / (2*a)
        r2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"({r1}, {r2})"
    elif discriminante == 0:
        r = -b / (2*a)
        return f"({r})"
    else:
        return "( )"
print(roots(1,-3,2))
print(roots(1, 2, 3))

def value_y(a, b, c, x):
    return a*x**2 + b*x + c
print(value_y(1, -3, 2, 0))

def to_string(a, b, c):
    if a == 0 and b != 0:
        if c == 0:
            return f"f(x) = {b} * X"
        else:
            return f"f(x) = {b} * X + {c}"
        
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    
    if a != 0:
        if b == 0 and c == 0:
            return f"f(x) = {a} * X^2"
        elif b == 0:
            return f"f(x) = {a} * X^2 + {c}"
        elif c == 0:
            return f"f(x) = {a} * X^2 + {b} * X"
        else:
            return f"f(x) = {a} * X^2 + {b} * X + {c}"
print(to_string(2, -3, 1))
print(to_string(2, 0, 5))


def derivation(a, b, c):
    A = 2 * a
    B = b
    if A == 0:
        return f"f'(x) = {B}"
    if B == 0:
        return f"f'(x) = {A} * X"
    else:
        return f"f'(x) = {A} * X + {B}"
print(derivation(2, -3, 1))
print (derivation(2, 0, 5))

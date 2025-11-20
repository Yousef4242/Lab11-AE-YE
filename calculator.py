# https://github.com/Yousef4242/Lab11-AE-YE.git
# Partner 1: Yousef El-Dakkak
# Partner 2: Aiden E

import math


def square_root(a):
    """
    Returns sqrt(a).
    Raises ValueError if a < 0.
    """
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)


def hypotenuse(a, b):
    """
    Returns the hypotenuse length given legs a and b.
    """
    return math.hypot(a, b)


def add(a, b):
    """
    Returns a + b.
    """
    return a + b


def subtract(a, b):
    """
    Returns a - b.
    """
    return a - b


def mul(a, b):
    """
    Returns a * b.
    """
    return a * b


def div(a, b):
    """
    Returns a / b.
    Raises ZeroDivisionError if b == 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def logarithm(a, b):
    """
    Returns log base a of b, i.e. log_a(b).
    Raises ValueError if a <= 0, a == 1, or b <= 0.
    """
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid arguments for logarithm.")
    return math.log(b, a)


def exp(a, b):
    """
    Returns a raised to the power b.
    """
    return a ** b

import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def square(x):
    return x * x

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)

def log(x, base=10):
    if x <= 0:
        raise ValueError("Log input must be > 0.")
    if base is None:
        return math.log(x)  # natural log
    if base <= 0 or base == 1:
        raise ValueError("Log base must be > 0 and != 1.")
    return math.log(x, base)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def percentage(value, total=None):
    """
    If total is None: convert value into a percentage fraction (value/100).
      e.g., percentage(25) -> 0.25
    If total is provided: compute 'value percent of total'.
      e.g., percentage(25, 200) -> 50
    """
    if total is None:
        return value / 100.0
    return (value / 100.0) * total
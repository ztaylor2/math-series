"""401d7 day 2 lab assignment. Mike Shinners & Zach Taylor."""


fibonacci_numbers = {}


def fibonacci(n):
    """creates a fibonacci series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n not in fibonacci_numbers:
        fibonacci_numbers.update({n: fibonacci(n - 1) + fibonacci(n - 2)})
    return fibonacci_numbers[n]


lucas_numbers = {}


def lucas(n):
    """creates a lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n not in lucas_numbers:
        lucas_numbers.update({n: lucas(n - 1) + lucas(n - 2)})
    return lucas_numbers[n]


def sum_series(n, first=0, second=1):
    """creates a sum_seris"""
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + \
            sum_series(n - 2, first, second)


if __name__ == "__main__":
    print("This module defines functions that implement mathematical series.")
    print()
    print("fibonacci(n): ")
    print("Returns the nth value of the fibonacci series")
    print("fibonacci(5): ")
    print(fibonacci(5))
    print()
    print("lucas(n): ")
    print("Returns the nth value of the lucas series")
    print("lucas(5): ")
    print(lucas(5))
    print()
    print("sum_series(n, first=0, second=1): ")
    print("Returns the nth value of a sum series")
    print("If no initial values are given it will default to fibonacci")
    print("sum_series(5): ")
    print(sum_series(5))
    print("sum_series(5, 5, 5): ")
    print(sum_series(5, 2, 1))

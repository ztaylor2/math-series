"""401d7 day 2 lab assignment. Mike Shinners & Zach Taylor."""


def fibonacci(n):
    """creates a fibonacci series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """creates a lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first=0, second=1):
    """creates a lucas series"""
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return lucas(n - 1) + lucas(n - 2)

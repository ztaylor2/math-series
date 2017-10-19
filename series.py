"""401d7 day 2 lab assignment. Mike Shinners & Zach Taylor."""


fibonacci_numbers = {}


def fibonacci(n):
    """Create a fibonacci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n not in fibonacci_numbers:
        fibonacci_numbers.update({n: fibonacci(n - 1) + fibonacci(n - 2)})
    return fibonacci_numbers[n]


lucas_numbers = {}


def lucas(n):
    """Create a lucas series."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n not in lucas_numbers:
        lucas_numbers.update({n: lucas(n - 1) + lucas(n - 2)})
    return lucas_numbers[n]


def sum_series(n, first=0, second=1):
    """Create a sum_seris."""
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + \
            sum_series(n - 2, first, second)


if __name__ == "__main__":
    output = """
    This module defines functions that implement mathematical series.

    fibonacci(n):
    Returns the nth value of the fibonacci series
    >>> fibonacci(5):
    {}

    lucas(n):
    Returns the nth value of the lucas series
    >>> lucas(5):
    {}

    sum_series(n, first=0, second=1):
    Returns the nth value of a sum series
    If no initial values are given it will default to fibonacci
    >>> sum_series(5):
    {}

    >>> sum_series(5, 5, 5):
    {}
"""

    print(output.format(fibonacci(5), lucas(5),
                        sum_series(5), sum_series(5, 2, 1)))

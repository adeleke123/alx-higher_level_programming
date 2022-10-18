#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Args: Adds two number a and b.
        :param a: first number input,
        :param b: second number input.

    Raise: TypeError - if not an integers or floats.

    Returns: addition of a and b (an integer).
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

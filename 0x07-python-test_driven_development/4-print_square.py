#!/usr/bin/python3


def print_square(size):
    """
    Args: Prints a square with the character '#'
        :param size: length of the square (must be and integer).

    Raises:
        TypeError - if size is not an integer, is a float and < 0,
        ValueError - if size < 0.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()

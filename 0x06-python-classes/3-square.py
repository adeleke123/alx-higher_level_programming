#!/usr/bin/python3
"""Area of a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Private instance attribute with size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of the Square"""
        return self.__size ** 2

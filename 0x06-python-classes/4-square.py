#!/usr/bin/python3
"""Access and update private attribute"""


class Square:
    """Class square"""

    def __init__(self, size=0):
        """Square with the size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of the Square"""
        return self.__size ** 2

    @property
    def size(self):
        """Private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size private attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

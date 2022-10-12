#!/usr/bin/python3
"""Printing a square"""


class Square:
    """Class square that defines a square"""

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

    def my_print(self):
        """Print Square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        """getting private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting Size private attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

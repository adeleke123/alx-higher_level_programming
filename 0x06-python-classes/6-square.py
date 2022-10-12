#!/usr/bin/python3
"""Corordinates of a Square"""


class Square:
    """Square defines a geometric shape square"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor for Square class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set of the size attribute"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position attribute"""
        if not type(value) is tuple or len(value) != 2 \
                or not type(value[0]) is int or not type(value[1]) is int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Area returns the current square area"""
        return self.__size**2

    def my_print(self):
        """Prints the square forming by '#' symbol"""
        if self.__size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

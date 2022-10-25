#!/usr/bin/python3
"""A Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from a Rectangle"""

    def __init__(self, size):
        """
        Initializing the square

        Args:
            size: size of the square (positive int)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

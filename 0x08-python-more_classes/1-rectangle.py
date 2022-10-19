#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """Args: A class Rectangle that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializer of rectangle class

        Args:
            width: the width of the rectangle (int)
            height: the height of the rectangle (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Args: Width getter (integer)

        Raise: TypeError - if width not an integer,
        ValueError - if width is < 0.

        Returns: the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args: Width setter (integer).

        Raises:
            TypeError: if value not an integer
            ValueError: if value is < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Args: Height getter (integer)

        Raise:
            TypeError - if value not an integer
            ValueError - if value is < 0

        Returns: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args: Height setter (integer).

        Raises:
            TypeError: if value not an integer,
            ValueError: if value is < 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

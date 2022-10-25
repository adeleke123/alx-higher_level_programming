#!/usr/bin/python3
"""A class Full rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """initialization of the Full Rectangle

        Args:
            width: must be positive (int)
            height: must be positive (int)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

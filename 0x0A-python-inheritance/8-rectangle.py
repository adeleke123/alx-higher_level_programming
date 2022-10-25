#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """initialization of a new Rectangle
        Args:
            width: The width of the new Rectangle (int)
            height: The height of the new Rectangle (int)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

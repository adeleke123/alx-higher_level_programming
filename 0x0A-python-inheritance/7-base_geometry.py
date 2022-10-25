#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """Public instance method - integer_validator"""
    def area(self):
        """Raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Checks integer value

        Args:
            name: name of the value (str)
            value: the value(int)

        Raises:
            TypeError - if value is not an integer
            ValueError - if value <= 0
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

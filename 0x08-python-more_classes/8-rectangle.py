#!/usr/bin/python3
"""Compare rectangles"""


class Rectangle:
    """Rectangle class

    Args:
        width: private instance attribute (int)
        height: private instance attribute (int)
        number_of_instances: public class attribute (int)
        print_symbol: public class attribute (str)
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializer of rectangle class

        Args:
            width: the width of the rectangle (int)
            height: the height of the rectangle (int)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter

        Returns:
            (int): the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter

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
        """Height getter

        Returns:
            the height of the rectangle  (int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle

        Returns:
            the rectangle area (int)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle

        Returns:
            0 if one of width or height is none
            the rectangle perimeter (int)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints out the rectangle

        Returns:
            the geometric format with print_symbol (str)
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return ((symbol * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """The canonical string representation of the class

        Returns:
            the string representation of the class (str)
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Deletes instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare between two rectangle

        Args:
            rect_1: the first rectangle (Rectangle)
            rect_2: the second rectangle (Rectangle)

        Raises:
            TypeError: if one of the given two args is not an instance of
            Rectangle

        Returns:
            the biggest rectangle (Rectangle)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        return rect_2

#!/usr/bin/python3
"""Adds attributes to objects."""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible.
    Args:

        obj: The object to add an attribute to (any)
        attr (str): the attribute to 5add to obj
        value (any): The value of att

    Raises:
        TypeError - If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

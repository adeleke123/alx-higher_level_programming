#!/usr/bin/python3
"""Class MyList"""


class MyList(list):
    """A  list class"""
    def print_sorted(self):
        """Prints the sorted list"""
        if issubclass(MyList, list):
            print(sorted(self))

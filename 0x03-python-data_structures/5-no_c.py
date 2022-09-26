#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string."""
    return my_string.translate({ord(c): None for c in "cC"})

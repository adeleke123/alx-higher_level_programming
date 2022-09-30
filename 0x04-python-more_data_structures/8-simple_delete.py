#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    a_dictionary.pop(key, None)
    return a_dictionary

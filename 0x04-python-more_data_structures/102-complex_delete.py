#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    dict_keys = list(a_dictionary.keys())

    for dict_value in dict_keys:
        if value == a_dictionary.get(dict_value):
            del a_dictionary[dict_value]
    return (a_dictionary)

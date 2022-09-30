#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple."""
    if my_list and len(my_list):
        x = 0
        y = 0
        for tups in my_list:
            x += (tups[0] * tups[1])
            y += tups[1]
        return (x / y)
    return 0

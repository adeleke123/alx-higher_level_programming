#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a number"""
    val = int(repr(number)[-1])
    print("{}".format(val), end="")
    return val

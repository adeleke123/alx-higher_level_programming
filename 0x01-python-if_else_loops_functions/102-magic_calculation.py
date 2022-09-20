#!/usr/bin/python3
def magic_calculation(a, b, c):
    """a function that does exactly the same as the Python bytecode"""
    if a < b:
        return c
    if c > b:
        return a + b
    return (a * b) - c

#!/usr/bin/python3
if __name__ == "__main__":
    """imports all functions from file calculator_1.py and handles
    basic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = sys.argv[2]
    if ops not in '*+-/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if ops == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif ops == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif ops == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))

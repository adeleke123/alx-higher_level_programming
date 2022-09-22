#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition of all arguments"""
    import sys
    adds = 0
    num_arg = sys.argv

    for i in range(1, len(num_arg)):
        adds += int(num_arg[i])
    print(adds)

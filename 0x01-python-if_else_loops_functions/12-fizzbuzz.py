#!/usr/bin/python3
def fizzbuzz():
    """Prints numbers 1 to 100 separated by a space
    For multiples of three, print Fizz instead of the number
    For multiples of five, print Buzz instead of the number
    For multiples of three and five, print FizzBuzz instead of the number
    """
    for i in range(1, 101):
        if (i % 15 == 0):
            print("FizzBuzz ", end="")
        elif (i % 3 == 0):
            print("Fizz ", end="")
        elif (i % 5 == 0):
            print("Buzz ", end="")
        else:
            print("{:d} ".format(i), end="")

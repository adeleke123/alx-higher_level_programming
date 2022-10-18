#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Args: Divides all element of a matrix.
        :param matrix: must be a list of lists of integers or floats.
        :param div: a number (integer or float), can't be equal to 0,
                    used in dividing all elements of the matrix,
                    rounded to 2 decimal places.
    Raises:
    TypeError - if list of lists is not integers or floats, if each row of the matrix is not same size.
    ZeroDivisionError - if div equal to 0.

    Returns: new matrix.
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError(
            "Each row of the matrix must have the same size")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    new_matrix = [[eval("{:.2f}".format(num / div)) for num in row]
                  for row in matrix]
    return new_matrix

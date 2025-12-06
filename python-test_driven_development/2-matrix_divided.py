
#!/usr/bin/python3
"""This module provides the matrix_divided function."""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.
    Args:
        matrix (list of lists): matrix of integers/floats.
        div (int or float): number to divide all matrix elements by.
    Raises:
        TypeError: if matrix is not a list of lists of integers/floats.
        TypeError: if rows are not the same size.
        TypeError: if div is not a number.
        ZeroDivisionError: if div is zero.
    Returns:
        list: new matrix with each value divided by div and rounded to 2 decimals.
    """

    # Validate matrix
    if (not isinstance(matrix, list) or
        not matrix or
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate row size + contents
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division (inf is allowed, will produce 0.0)
    return [[round(element / div, 2) for element in row] for row in matrix]

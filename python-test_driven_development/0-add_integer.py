#!/usr/bin/python3
"""
This module contains the add_integer function.
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b.

    Both a and b must be integers or floats.
    Floats are casted to integers unless they are NaN or infinity.
    Raises:
        TypeError: if a or b are not integers or floats.
        ValueError: if a or b are NaN.
        OverflowError: if a or b are infinite.
    Returns:
        int: the sum of a and b.
    """

    # Validate types
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN
    if isinstance(a, float) and a != a:
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and b != b:
        raise ValueError("cannot convert float NaN to integer")

    # Check for infinity
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")

    # Safe conversion
    a = int(a)
    b = int(b)

    return a + b

#!/usr/bin/python3
"""Technical interview preparation:
A function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        current_row = triangle[-1]
        next_row = [1] + [current_row[i] + current_row[i + 1] for i in range(len(current_row) - 1)] + [1]
        triangle.append(next_row)
    return triangle

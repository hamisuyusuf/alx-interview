#!/usr/bin/python3
"""Module to generate Pascal's Triangle."""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle


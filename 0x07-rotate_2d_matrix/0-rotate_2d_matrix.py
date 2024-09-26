#!/usr/bin/python3
'''
  matrix
'''


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): A 2D list representing the matrix.

    Returns:
        None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

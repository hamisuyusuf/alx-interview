#!/usr/bin/python3
"""
    0x02. Minimum Operations
"""


def minOperations(n):
    """

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0

    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

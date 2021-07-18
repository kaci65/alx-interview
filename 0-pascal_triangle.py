#!/usr/bin/python3
"""
function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
"""

from itertools import combinations


def pascal_func(num, k):
    """function to calculate factorial"""
    res = len(list(combinations(range(num), k)))
    return(res)


def pascal_triangle(n):
    """function to return factorial of list of ints"""
    tri = []
    for count in range(n):
        row = []
        for i in range(count + 1):
            row.append(pascal_func(count, i))
        tri.append(row)
    return(tri)

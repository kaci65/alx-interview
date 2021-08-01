#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0

"""


def minOperations(n):
    """return minimum number of operations needed"""
    if (n == 1):
        return 0
    count = 0
    i = 2
    while n > 1:
        while n % i == 0:
            count += i
            n /= i
        i += 1
    return count

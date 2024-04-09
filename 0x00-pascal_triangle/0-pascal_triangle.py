#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """Return a list of lists representing the Pascal's triangle of n rows."""
    if n <= 0:
        return []
    t = [[1]]
    for _ in range(1, n):
        r = [1] + [t[-1][i] + t[-1][i+1] for i in range(len(t[-1]) - 1)] + [1]
        t.append(r)
    return t

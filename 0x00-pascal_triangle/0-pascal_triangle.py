#!/usr/bin/python3
"""generates a pascal triangle"""

def pascal_triangle(n):

    """
    Returns:
        list(list(int)): list of lists of integers
    """
    if n <= 0:
        return []
    
    pascal_triangle = [0] * n

    for i in range(n):
        new = [0] * (i + 1)
        new[0] = 1
        new[len(new) - 1] = 1

        for j in range (1, i):
            if j > 0 and j < len(new):
                x = pascal_triangle[i - 1][j]
                y = pascal_triangle[i - 1][j - 1]
                new[j] = x + y

        pascal_triangle[i] = new

    return pascal_triangle

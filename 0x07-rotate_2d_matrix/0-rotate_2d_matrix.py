#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Ritate a 2d square matrix 90 degrees
    Args:
        matrix (list): 2d square
    Return: 
        None
    """
    n = len(matrix)
    """Transpose the matrix"""
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]


rotate_2d_matrix(matrix)
print(matrix)

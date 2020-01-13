#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module have a function that divides all elements of a matrix.
for that we use the function def matrix_divided(matrix, div)

"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix..

        matrix_divided: description
            matrix must be a list of lists of integers or floats, 
            otherwise raise a TypeError
            Each row of the matrix must be of the same size, 
            otherwise raise a TypeError
            div must be a number (integer or float), 
            otherwise raise a TypeError
            div cant be equal to 0, otherwise raise a ZeroDivisionError

    Args:
        matrix (list of lists): The first parameter of ints or floats
        div (int/float): second parameter

    Returns:
        New matrix with the results

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    """

    if len(matrix[0]) == 0:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    elif len(matrix[0]) != 0:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] is not int:
                    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
                    break
    elif len(matrix[0]) != 0:
        i = 1
        while i < len(matrix):
            if len(matrix[i]) != len(matrix[0]):
                raise TypeError('Each row of the matrix must have the same size')
            i += 1
    if div is not int and div is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

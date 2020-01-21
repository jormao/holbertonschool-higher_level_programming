#!/usr/bin/python3
""" 1-number_of_lines.py - Number of lines"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file
    ARGS:
        filename: file .txt
    """
    line_number = 0
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            line_number += 1
    return line_number

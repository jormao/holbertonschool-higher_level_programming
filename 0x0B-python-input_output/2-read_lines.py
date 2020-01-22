#!/usr/bin/python3
"""2-read_lines.py - Read n lines"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a file (UTF8) and prints it to stdout
    ARGS:
        filename: file txt
        nb_lines: number of lines to read
    """
    line_number = 0
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            line_number += 1
            if line_number <= nb_lines or nb_lines <= 0:
                print(a_line, end="")

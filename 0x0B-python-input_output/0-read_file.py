#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout
    ARGS: filename: file
    """
    line_number = 0
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            line_number += 1
            print('{}'.format(a_line.rstrip()))

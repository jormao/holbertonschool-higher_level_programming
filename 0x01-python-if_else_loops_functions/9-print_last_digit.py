#!/usr/bin/python3
def print_last_digit(number):
    a = 1
    if (number < 0):
        a = -1
    last_digit = (number * a) % 10
    print("{:d}".format(last_digit), end='')
    return (last_digit)

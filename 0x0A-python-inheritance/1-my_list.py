#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
1-my_list.py: class MyList that inherits from list

"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))

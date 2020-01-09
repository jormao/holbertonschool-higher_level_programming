#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
0-square.py: is an empty class Square that defines a square:
"""
class Square(size):
    """class Square that defines a square

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    pass

    def __init__(self, size):
        """Initializer with default radius of 1.0"""
        self.size = size  # Create an instance variable radius

    def get_size(self):
        """Return the size of this Square"""
        return self.size

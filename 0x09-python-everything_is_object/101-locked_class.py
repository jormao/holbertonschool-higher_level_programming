#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
101-locked_class.py: a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name
"""


class LockedClass:
    """Class lockedclass  that prevent dinamically creating new instance
    Attributes:
        with out attributes
    """

    __slots__ = ['first_name']

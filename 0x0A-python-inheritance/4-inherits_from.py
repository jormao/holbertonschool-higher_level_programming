#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
4-inherits_from.py: Only sub class of
"""


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False."""
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
            return True
    else:
        False

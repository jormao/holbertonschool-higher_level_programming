#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Class Base with the attributes for the other class
that inherits from Base

"""

import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None or type(list_objs) is not list:
            list_objs = []
        


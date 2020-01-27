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
        """ function to save a json how string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ rites the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as a_file:
            if list_objs is None:
                return a_file.write(cls.to_json_string(None))
            my_list = []
            for i in list_objs:
                my_list.append(i.to_dictionary())
            return a_file.write(cls.to_json_string(my_list))

# Python - Almost a circle

## Background Context

he AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:

    Import
    Exceptions
    Class
    Private attribute
    Getter/Setter
    Class method
    Static method
    Inheritance
    Unittest
    Read/Write file

    args and kwargs
    Serialization/Deserialization
    JSON

## Resources


    args/kwargs
    JSON encoder and decoder
    unittest module
    Python test cheatsheet

## Learning Objectives

### General


    What is Unit testing and how to implement it in a large project
    How to serialize and deserialize a Class
    How to write and read a JSON file
    What is *args and how to use it
    What is **kwargs and how to use it
    How to handle named arguments in a function

## Requirements

### Python Scripts

llowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

### Python Unit Tests


    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    All your test files should be inside a folder tests
    You have to use the unittest module
    All your test files should be python files (extension: .py)
    All your test files and folders should start with test_
    Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
    All your tests should be executed by using this command: python3 -m unittest discover tests
    You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
    We strongly encourage you to work together on test cases so that you don’t miss any edge case

| TASKS | DESCRIPTION |
| ------|--------------|
| models/base.py, models/__init__.py | Write the first class Base |
| models/rectangle.py | Write the class Rectangle that inherits from Base |
| models/rectangle.py | Update the class Rectangle by adding validation of all setter methods and instantiation|
| models/rectangle.py | Update the class Rectangle by adding the public method def area(self) |
| models/rectangle.py | Update the class Rectangle by adding the public method def display(self)|
| models/rectangle.py | Update the class Rectangle by overriding the __str__ method |
| models/rectangle.py | Update the class Rectangle by improving the public method def display(self)|
| models/rectangle.py | Update the class Rectangle by adding the public method def update(self, *args)|
| models/rectangle.py | Update the class Rectangle by updating the public method def update(self, *args)|
| models/square.py | Write the class Square that inherits from Rectangle |
| models/square.py | Update the class Square by adding the public getter and setter size|
| models/square.py | Update the class Square by adding the public method def update(self, *args, **kwargs) |
| models/rectangle.py | Update the class Rectangle by adding the public method def to_dictionary(self)|
| models/square.py | Update the class Square by adding the public method def to_dictionary(self)|
| models/base.py | JSON is one of the standard formats for sharing data representation.|
| models/base.py | Update the class Base by adding the class method def save_to_file(cls, list_objs)|
| models/base.py | Update the class Base by adding the static method def from_json_string(json_string)|
| models/base.py | Update the class Base by adding the class method def create(cls, **dictionary)|
| models/base.py | Update the class Base by adding the class method def load_from_file(cls)|
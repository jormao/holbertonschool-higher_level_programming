# Python - Inheritance

## Resources

### Read or watch:


    Inheritance
    Multiple inheritance
    Inheritance in Python
    Learn to Program 10 : Inheritance Magic Methods

## Learning Objectives

### General


    Why Python programming is awesome (dont forget to tweet today, with the hashtag #pythoniscool :))
    What is a superclass, baseclass or parentclass
    What is a subclass
    How to list all attributes and methods of a class or instance
    When can an instance have new attributes
    How to inherit class from another
    How to define a class with multiple base classes
    What is the default class every class inherit from
    How to override a method or attribute inherited from the base class
    Which attributes or methods are available by heritage to subclasses
    What is the purpose of inheritance
    What are, when and how to use isinstance, issubclass, type and super built-in functions

## Requirements

### Python Scripts


    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7.*)
    All your files must be executable
    The length of your files will be tested using wc

### Python Test Cases


    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    All your test files should be inside a folder tests
    All your test files should be text files (extension: .txt)
    All your tests should be executed by using this command: python3 -m doctest ./tests/*
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    We strongly encourage you to work together on test cases, so that you dont miss any edge case

| TASKS | DESCRIPTIONS |
|----------| ----------------|
| 0-lookup.py | function that returns the list of available attributes and methods of an object|
| 1-my_list.py, tests/1-my_list.txt| class MyList that inherits from list|
| 2-is_same_class.py | function that returns True if the object is exactly an instance of the specified class ; otherwise False|
| 3-is_kind_of_class.py | returns True if the object is an instance of a class that inherited from, the specified class ; otherwise False.|
| 4-inherits_from.py | function that returns True if the object is an instance of a class that inherited from the specified class otherwise False|
| 5-base_geometry.py | an empty class BaseGeometry.|
| 6-base_geometry.py | class BaseGeometry (based on 5-base_geometry.py).|
| 7-base_geometry.py, tests/7-base_geometry.txt| class BaseGeometry |
| 8-rectangle.py | class Rectangle that inherits from BaseGeometry (7-base_geometry.py).|
| 9-rectangle.py | class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)|
| 10-square.py | class Square that inherits from Rectangle (9-rectangle.py) |
| 11-square.py | class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).|
| 100-my_int.py |  a class MyInt that inherits from int|
| 101-add_attribute.py | function that adds a new attribute to an object if its possible | 

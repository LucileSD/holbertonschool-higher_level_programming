#!/usr/bin/python3
"""
    student class file
"""


class Student:
    """
        class to define a student
    """
    def __init__(self, first_name, last_name, age):
        """
            initiate the class
            args:
                first_name
                last_name
                age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            a function that retrieves a dictionary representation
            of a Student instance
            args:
                attrs: attributes
            return:
                the dictionary description with simple data structure
        """
        if type(attrs) is list:
            x = {}
            for at in attrs:
                if hasattr(self, at):
                    x[at] = getattr(self, at)
            return x
        return self.__dict__

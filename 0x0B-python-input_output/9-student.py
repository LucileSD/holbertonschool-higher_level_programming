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

    def to_json(self):
        """
            a function that retrieves a dictionary representation
            of a Student instance
            return:
                the dictionary description with simple data structure
        """
        return self.__dict__

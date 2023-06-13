#!/usr/bin/python3
"""A class Student that defines a student by:
- Public instance attributes: age, first and last name
"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student with the attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the Student object"""
        return self.__dict__

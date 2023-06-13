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

    def to_json(self, attrs=None):
        """Create a dictionary representation of the Student,
        considering only the specified attributes in the given list.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reload from json
        """
        for k, v in json.items():
            setattr(self, k, v)

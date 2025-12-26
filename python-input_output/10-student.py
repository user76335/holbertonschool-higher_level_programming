#!/usr/bin/python3
"""Student class module"""


class Student:
    """Defines a Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation.
        If attrs is a list, only selected attributes are returned.
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

        return self.__dict__

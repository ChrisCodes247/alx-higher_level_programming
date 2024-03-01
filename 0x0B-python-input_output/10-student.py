#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """class constructor.

        Args:
            first_name (str): students first name
            last_name (str): students last name
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student.

        If attrs is a list of strings, represent only those attributes
        included in the list.

        Args:
            attrs (list): (optional) The attributes to represent.
        """
        if (type(attrs) == list and all(type(ele) == str for
            ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return (self.__dict__)

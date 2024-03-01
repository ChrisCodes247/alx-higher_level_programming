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

    def to_json(self):
        """Get a dictionary representation of the student."""
        return (self.__dict__)

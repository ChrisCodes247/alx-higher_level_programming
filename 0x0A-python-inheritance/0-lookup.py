#!/usr/bin/python3
"""Defines an object llookup function"""


def lookup(obj):
    """Checks list of available attributes and methods.

    Args:
        obj: an object of a class

    Returns: a list object of available attributes and methods of a class.
    """

    lst = dir(obj)
    return (lst)

#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file and prints to stdout."""
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")

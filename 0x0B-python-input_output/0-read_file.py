#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file and prints to stdout.

    Args:
        filename (string): name of file to read

    Returns:
        prints contents to stdout
    """
    with open(filename, 'r', encoding="utf-8") as a_file:
        content = a_file.read()
        print(content, end="")
